import sqlite3
import numpy as np
from datetime import datetime
from discord import app_commands
import discord
from discord.ext import commands
from math import exp

conn = sqlite3.connect("invocs.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,  -- ID Discord
    name TEXT
)
""")

# Table des personnages
cursor.execute("""
CREATE TABLE IF NOT EXISTS characters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    rarity INTEGER
)
""")

# Table des armes
cursor.execute("""
CREATE TABLE IF NOT EXISTS weapons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    rarity INTEGER
)
""")

# Table des artéfacts
cursor.execute("""
CREATE TABLE IF NOT EXISTS artifacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    effect TEXT,
    rarity INTEGER
)
""")

# Table inventaire (personnages, armes, artéfacts)
cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory (
    user_id INTEGER,
    item_type TEXT,  -- 'character', 'weapon', 'artifact'
    item_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS invocations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    item_name TEXT,
    rarity INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS pity (
    user_id INTEGER PRIMARY KEY,
    pity_counter_5 INTEGER DEFAULT 0,
    fifty_fifty_lost_5 INTEGER DEFAULT 0,
    pity_counter_4 INTEGER DEFAULT 0
)
""")


# Table des équipements d’un joueur
cursor.execute("""
CREATE TABLE IF NOT EXISTS equipment (
    user_id INTEGER,
    character_id INTEGER,
    weapon_id INTEGER,
    artifact_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (character_id) REFERENCES characters(id),
    FOREIGN KEY (weapon_id) REFERENCES weapons(id),
    FOREIGN KEY (artifact_id) REFERENCES artifacts(id)
)
""")



# Sauvegarde et fermeture
conn.commit()
conn.close()

print("✅ Base de données initialisée avec succès !")


items = {
    6: ["Skirk", "Escoffier", "Kokomi","Neuvilette","Le Babibel Artificiel"],
    5: ["Diluc", "Mona", "Qiqi", "Keqing", "Jean"],  # Persos 5*
    4: ["Razor", "Sucrose", "Bennett", "Chongyun"],  # Persos 4*
    3: ["Épée en fer", "Arc du chasseur", "Catalyseur rouillé"]  # Armes 3*
}

class Invoc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="invocs", description="Invoque un perso ou une arme")
    @app_commands.describe(nombre="Nombre d'invocs : multi (10) ou single (1)")
    async def invocs(self, interaction: discord.Interaction, nombre: int = 1):
        if type(nombre) != int:
            await interaction.response.send_message("Tu dois mettre le nombre d'invocs !", ephemeral=True)
            return
        if nombre not in (1, 10):
            await interaction.response.send_message("C'est soit multi soit single ya quoi de compliqué à comprendre... -_-", ephemeral=True)
            return
        user_id = interaction.user.id

        conn = sqlite3.connect("invocs.db")
        cursor = conn.cursor()

        # Récupère pity
        cursor.execute("SELECT pity_counter_5, fifty_fifty_lost_5, pity_counter_4 FROM pity WHERE user_id = ?", (user_id,))
        data = cursor.fetchone()
        pity_counter_5 = data[0] if data else 0
        fifty_fifty_lost_5 = data[1] if data else 0
        pity_counter_4 = data[2] if data else 0

        results = []

        for i in range(nombre):
            rarity = self.get_rarity(pity_counter_4, pity_counter_5)
            print()
            # Reset ou incrémentation pity
            if rarity == 5:
                pity_counter_5 = 0
            else:
                pity_counter_5 += 1

            if rarity == 4:
                pity_counter_4 = 0
            else:
                pity_counter_4 += 1

            # 50/50 sur 5*
            if rarity == 5:
                is_rate_up = np.random.rand() < 0.5 if fifty_fifty_lost_5 == 0 else True
                if is_rate_up:
                    item = np.random.choice(items[6])
                    fifty_fifty_lost_5 = 0
                else:
                    item = np.random.choice(items[5])
                    fifty_fifty_lost_5 = 1
            else:
                item = np.random.choice(items[rarity])
            print(rarity,item)
            if rarity == 3:
                results.append(f"• {item} ({rarity}★)")
            else:
                results.append(f"• **{item}** ({rarity}★)")

            # Insère chaque invocation dans la BDD
            cursor.execute("INSERT INTO invocations (user_id, item_name, rarity) VALUES (?, ?, ?)", (user_id, item, rarity))
        cursor.execute("INSERT OR REPLACE INTO pity (user_id, pity_counter_5, fifty_fifty_lost_5, pity_counter_4) VALUES (?, ?, ?, ?)", (user_id, pity_counter_5, fifty_fifty_lost_5, pity_counter_4))
        conn.commit()

        # Ferme proprement
        cursor.close()
        conn.close()

        await interaction.response.send_message(f"🎉 Tu as obtenu :\n" + "\n".join(results))

    def get_rarity(self, pity4,pity5):
        if pity5 >= 90:
            return 5
        elif pity4 >= 10:
            return 4
        elif pity5 >= 75:
            return np.random.choice([5, 4, 3], p=[0.006*exp(pity5-75), 0.13, 0.870-0.006*exp(pity5-75)])
        else:
            return np.random.choice([5, 4, 3], p=[0.006, 0.13, 0.864])

async def setup(bot):
    await bot.add_cog(Invoc(bot))


