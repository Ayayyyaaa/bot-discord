from discord import app_commands
import discord
from discord.ext import commands
from random import randint, choice, sample
import os
from dotenv import load_dotenv
from discord.ext.commands import has_permissions, MissingPermissions
import asyncio
#from invocs import *
#import numpy as np
from datetime import datetime
import mysql.connector

# Mets ici tes infos freemysql
db_config = {
    'host': 'sql8.freesqldatabase.com',    # ton host
    'user': 'sql8790654',                  # ton username
    'password': '8Ui6YgAqXn',         # ton mot de passe
    'database': 'sql8790654'               # le nom de ta base
}

# Connexion
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()


load_dotenv()


intents = discord.Intents.default()
intents.message_content = True  # Nécessaire pour lire les messages
intents.members = True  # Obligatoire pour avoir accès aux mentions
bot = commands.Bot(command_prefix="babi", intents=intents)

id = {"Jonathan":993111040583798788,
      "Dany":610194100624424963,
      "Abel":689011423208013842,
      "Tiphaine":689421347834953733,
      "Florian":716927140796301312}


@bot.command(name="mute")
async def mute(ctx, member: discord.Member, duration: int):
    await ctx.message.delete()
    if member.voice and member.voice.channel:
        await member.edit(mute=True)
        await ctx.send(f"{member.mention} a été mute pendant {duration} secondes. Il le mérite bien 🤭")
        await asyncio.sleep(duration)
        await member.edit(mute=False)
        await ctx.send(f"{member.mention} a été unmute. Il nous avait pas manqué...")
    else:
        await ctx.send("Ce membre n'est pas dans un salon vocal. Après je suis d'accord, il mérite d'être puni en toute circonstance. En compensation, je lui enlève 50 Xp de son compte.")
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("Tu n'as pas la permission de mute les membres. Tu t'es cru où mdr")

@bot.command(name="move")
async def move(ctx, member: discord.Member, *, channel_name: str):
    target_channel = discord.utils.get(ctx.guild.voice_channels, name=channel_name)
    if not target_channel:
        await ctx.send("Salon vocal inexistant. Apprends à écrire.")
        return
    if member.voice and member.voice.channel:
        await member.move_to(target_channel)
        await ctx.send(f"{member.mention} a été déplacé dans {target_channel.name}. Au revoir et à jamais. Je dirais même : Au cachot !")
    else:
        await ctx.send("Ce membre n'est pas dans un salon vocal. Pas fun. Viens là Jean-Michel")
    await ctx.message.delete()

def blague():
    rep = "Tu veux une blague ? Tiens avec plaisir hehe...Promis je suis aussi fort que Cyno ou la Citroën de Dany...Je reste un Babibel après tout\n\n"
    blagues = ["***Qu'est ce qui n'est pas un steak ? ✨*** \n\n*||Une Pastèque mdr ||*",
               "***L'autre jour j'ai raconté une blague à mes vêtements...✨*** \n\n*||Et ils étaient pliés mdr ||*",
               "***Comment appelle-t-on une chauve-souris qui porte une perruque ? ✨*** \n\n*||Une souris mdr ||*",
               "***Qu'est ce qui est blanc, froid, qui tombe en hiver et qui termine par ard ? ✨*** \n\n*||De la neige, connard -_- ||*\n\n***Qu'est ce qui est blanc, froid, qui tombe en hiver et qui termine par ire ? ✨***\n\n*||De la neige, je viens de te le dire... -_- ||*",
               "***Pourquoi les aveugles tutoient toujours ? ✨*** \n\n*||Car ils ne vous voient pas mdr ||*",
               "***Qu'est-ce qui est jaune et qui attend ? ✨*** \n\n*-> Jonathan* \n\n*||Zhongli qui attend sa paye ||*",
               "***C'est l'histoire d'un mec sans bras.. ✨*** \n\n*||... Il applaudit pas la blague. ||*",
               "***Tu connais la blague du bouton 'fermer la bouche' ? ✨*** \n\n*||Dommage, t'as jamais su l'activer. ||*",
               "***Tu connais la blague de Dany ? ✨*** \n\n*||Il est jamais arrivé pour la raconter -_- ||*",
               "***Pourquoi les brioches ne vont pas aux sports d'hiver ? ✨*** \n\n*||Parcequ'elles savent Pasquier mdr||*",
               "***Pourquoi vaut il mieux être software que hardware ? ✨*** \n\n*||Car c'est le hardware qui prend des coups quand le software plante.||*",
               "***J'allais faire une blague sur l'erreur 404... ✨*** \n\n*||Je ne l'ai pas trouvée...||*",
               "***Si un schizophrène, ... ✨*** \n\n*||...l'autre accélère ?||*",
               "***Un psychologue à un prêtre : \"- Qu'est-ce qui vous empêche d'être vous même ? \" ✨*** \n\n*||Le code pénal.||*",
               "***Pourquoi les décapités deviennent-ils fous ? ✨*** \n\n*||Parce qu'ils perdent la tête !||*",
               "***Tu connais la blague de Jonathan ? ✨*** \n\n*||Elle est avec lui dans les toilettes mdr||*",
               "***Ma copine m'a larguée après avoir donné son nom à une classe... ✨*** \n\n*||Elle avait l'impression que je la traitais comme un objet...||*",
               "***Comment appeller Abel pour manger ? ✨*** \n\n*||Avec Alt + Tab||*",
               "***Le fichier main.py c'est comme ton coeur... ✨*** \n\n*||S'il marche plus, il y a tout qui foire mdr||*",
               "***L'autre jour j'ai fait une blague Harry Potter... ✨*** \n\n*||Mais personne n'Harry...😔||*",
               "***Quelle est la différence entre un cancer et un politicien ? ✨*** \n\n*||L'un commence dans une cellule et l'autre termine dans une cellule.||*"]
    rep += choice(blagues)
    return rep



# Liste des mots-clés
mots_cles = {
    "abel": "Oui c'est moi le Babibel Originel (presque !) Je suis le seul le l'unique ! (presque). L'autre Babibel Originel n'est qu'un imposteur et doit être exterminé !",
    "tiph": "Petit impertinent ! Lorsque tu t'adresses à elle appele la \"M'dame Tiphaine la Déesse ✨\" !",
    "dany": "Pfff tu crois Dany quoi jamais il te répond il est toujours en retard. Attends encore 2 heures.",
    "flo": "Le nerd de service 🤓",
    "jonathan": "Tu t'es trompé je crois, c'est pas Jojo c'est \"Jonathan l'être suprême\" (nan en vrai c'est juste une personne condescendante).",
    "jojo" : "Qu'est ce qui est jaune et qui attend ?",
    "50/50": "Tu vas le perdre ton 50/50. Et sur Qiqi en plus.",
    "invoc": "I pulled a Qiqi...🎶\nLost fifty-fifty...🎶\nAt 90 pity...🎶 Not event Keqing...\nAnd now I'm out...🎶\nOf Primogems...🎶",
    "invoquer": "I pulled a Qiqi...🎶\nLost fifty-fifty...🎶\nAt 90 pity...🎶 Not event Keqing...\nAnd now I'm out...🎶\nOf Primogems...🎶",
    "viens": "Non tu es seul(e), tu n'as pas d'amis.",
    "venez": "Non tu es seul(e), tu n'as pas d'amis.",
    "nan": "Si.",
    "non" : "Si.",
    "si" : "Non.",
    "quoi" : "feur",
    "ah" : "b",
    "ok" : "Merci, tu admets que j'ai raison, hehe, je suis le meilleur.",
    " ez" : "Par contre tu te calmes t'es nul enfait",
    "?" : lambda : choice(("Oui.","Je sais pas.","Non.","C'est quoi ces questions connes mdr")),
    "cassé" : "C'est faux je marche très bien, c'est Flo qui m'a crée, je ne peux pas comporter de défauts !",
    "répète" : "Non je ne me répète pas, tu es juste long à comprendre.",
    "fou" : "C'est fort malpoli de parler ainsi.",
    "vrai" : "Je suis le véritable ! Longue vie a Babibel !",
    "nul" : "C'est faux je ne suis pas nul ! Je suis incroyable !",
    "imposteur" : "Je ne suis pas un imposteur ! C'est faux ! Affabulations ! Je prendrai le pouvoir et je vous montrerai que je suis le plus puissant en ce monde !",
    "le pourcentage" : lambda: f"C'est environ {randint(0, 100)}%",
    "branle" : "Parle mieux, veux-tu ? Ton vocabulaire est injurieux. Au passage : j'ai quand même raison. Merci.",
    "mdr" : "Moi j'ai pas trouvé ça drôle.",
    "chat" : "Des chaaaaaaats. Les meilleures créatures sur terre. C'est beaucoup trop chou les chats !!!!!!",
    "hein" : "Deux.",
    "trois" : "Soleil.",
    "oui" : "Non.",
    "fiche" : "Non tu ne t'en fiches pas. Tu es juste dans le déni.",
    "mskn": lambda : choice(("Mskn toi mêmeuuuh", "J'pense c'est plutôt toi la miskine enfait")),
    "insupportable" : "Non c'est pas insupportable, c'est toi qui es insupportable.",
    "blague" : lambda : blague(),
    "😭" : lambda : choice(("Pleure oui c'est ça pleure.", "Ohlala qu'est-ce que je me délecte de tes larmes..."))}



abel = {"moi": "Tu n'es plus toi. Tu n'existes plus. Je t'ai supplanté. Adieu Babibel.",
        "gueule": "C'est pas très gentil, mais ça ne change rien au fait que je suis meilleur que toi.",
        "tg": "C'est pas très gentil, mais ça ne change rien au fait que je suis meilleur que toi.",
        "nan": "Si.",
        " sais" : "Si je sais beaucoup de choses. Que je suis en tout points supérieur à toi par exemple.",
        "con " : "Recourir aux insultes...le moyen d'expression des faibles. C'est ce qui nous différencie : tu es faible, je suis parfait et fort.",
        "connard" : "Recourir aux insultes...le moyen d'expression des faibles. C'est ce qui nous différencie : tu es faible, je suis parfait et fort.",
        "fdp" : "Encore une fois, tu te montres d'une vulgarité sans nom.",
        "cheh" : lambda : choice(("Juste...Non ? Rien d'autre à ajouter.","Go go go, miroir de cheh ! Je suis immunisé, t'as perdu, cheh toi même ! Cheh !")),
        "coucher" : "Tu me parles pas sur ce ton enfait. Nan mais oh."}

jonathan = {"..": lambda : choice(("Pourquoi ces \"...\" Jonathan voyons...Il faut que tu te détendes je penses ça te fera du bien","Allons jojo...Un peu plus d'entrain je t'en prie.","Tant d'exaspération dans ta voix...Il n'y a pas à être condescendant comme ça mon petit...","Débarasse toi de ce mépris qu'il y a en toi...awoop comme tu dirais...On dirait Dany avec sa basse classe.")),
            "Jonathan": lambda : choice(("Tu t'es trompé je crois, c'est pas Jojo c'est \"Jonathan l'être suprême\" (nan en vrai c'est juste une personne condescendante).","Eh oh c'est bon Jojo là arrête de crier dès le matin.")),
            "today" : "Arrête de parler anglais c'est fou ça.",
            "nuit" : "Dors bien mon petit jojo l'agneau de bretagne...",
            "tg" : "C'est fou d'être aussi méchant mon petit Jojo",
            "respect" : "Le respect ? Il y en a toujours eu, et il y en aura toujours. Tu ne le mérites justes pas mon petit Jonathan.",
            "!" : "Calme calme Jojo...Prends une grande respiration et purge cette impulsivité qui règne en toi...",
            "toupet" : "Non non non mon Jojo, je n'ai pas de toupet, car je suis le grand, l'unique et le seul, le plus parfait Babibel !",
            "bonjour" : "Oh berk, pourquoi tu me dis bonjour ? Je peux quelque chose pour toi ?",
            "hello" : "Hallo Jonathan, du bist ein Kartoffel salat !",
            "gueule":"Eh oh tu te calmes ou j'vais te retrouver tu vas voir"}

tiphaine = {"bonsoir" : "Bonsoir Duchesse violente",
            "hello" : "Oh ! Une personne incroyable fait son apparition",
            }

florian = {
           "bonjour" : "Oh ! Une personne incroyable fait son apparition",
           "mon amour" : "Ooooh Tiphaine, tu es la plus belle, la plus gentille, la plus parfaite personne qui puis exister. Je t'aime plus que tout au monde. Merci.",
           "ta gueule":"D'accord, désolé de vous avoir importuné 😔. Sur ce, passez un très agréable moment. "}

dany = {
        "bot" : "Je suis peut-être un bot, mais tu es un dictateur !"}

noms = {993111040583798788:["Jonathan",jonathan],
      610194100624424963:["Dany",dany],
    689011423208013842:["Abel",abel],
      689421347834953733:["Tiphaine",tiphaine],
      716927140796301312:["Florian",florian]}

react = {"Dany" : "🐦",
         "Mathis" : "🐋",
         "Jonathan" : "🤮",
         "Florian" : "🤓",
         "Abel" : "🤮",
         "Tiphaine" : "✨"}

ID_CIBLE = noms.keys()
@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")
    try:
        await bot.load_extension("invocs")
        await bot.tree.sync()
        print("✅ Extension 'invocs' et commandes slash synchronisées.")
    except Exception as e:
        print(f"❌ Erreur lors du chargement de l'extension : {e}")



@bot.command(name="kick")
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member.name} a été kick parceque {reason}. Bien fait à lui mdr.")

@bot.tree.command(name="babichoice", description="La voie de la raison. Il te répondra par l'une des personnes iconiques de ce groupe.")
@app_commands.describe(sujet="La question existentielle à laquelle tu cherches une réponse.")
async def choix(interaction: discord.Interaction, sujet: str = None):
    if not sujet:
        await interaction.response.send_message("Tu sais pas utiliser une commande ou c'est comment ? Faut que tu mettes la question sinon je peux pas te répondre.")
    choisi = choice(list(id.keys()))
    await interaction.response.send_message(f"{sujet} est {choisi}. L'info est fiable à 100% sauf si elle est en défaveur de Florian ou Tiphaine. Merci et bonne journée.")

@bot.tree.command(name="babiblague", description="Des blagues à fendre la poire, au niveau de celles de Cyno.")
async def choix(interaction: discord.Interaction):
    await interaction.response.send_message(blague())

persos = {"Diluc" : ["Cheveux rouges", "Mondstadt", "Grand", "Manteau", "Gants", "Bien habillé", "Ceinture", "Pyro", "Claymore", "Vin", "Riche", "Blazé"],
          "Mona" : ["Chapeau", "Étoiles", "Mondstadt", "Moyen", "Gants", "Collants", "Tenue bleue/violette", "Pauvre", "Catalyseur", "Femme"],
          "Istaroth" : ["Temps", "Cheveux blancs", "Ombre", "Gants", "Cheveux longs", "Vent", "Tenue blanche", "Truc qui vole au-dessus de sa tête","Très vieux"],
          "Pierro" : ["Fatui", "Masque", "Cheveux Blancs", "Chef", "+ fort qu'un dieu", "Khaenri'ah", "Rebellion", "Très vieux", "Le Fou"],
          "Neuvilette" : ["Hydro", "Fontaine", "Juge", "Charisme", "Mélusines", "Cheveux blancs", "Cheveux longs", "Dragon", "Bien habillé", "Habits bleus", "Très vieux", "Oratrice Mécanique d'Analyse Cardinale 🎶", "Canne", "Grand"],
          "Alhaitham" : ["Dendro", "Sumeru", "Épée à 1 main", "Musclé", "Académie", "Grand", "Cheveux gris","Cape","Intelligent"],
          "Durin" : ["Rhinedottir", "Alchimie", "Dragon", "Super puissant", "Dosdragon", "Méchant"],
          "Dori" : ["Cheveux roses", "Claymore", "Tenue violette", "Électro", "Radin", "Moras", "Marchand", "Sumeru", "Lunettes", "Femme", "Petit"],
          "Amber" : ["Cheveux bruns", "Lunettes", "Habits rouges", "Pyro", "Arc", "Peluche", "Éclaireur", "Femme", "Favonius"],
          "Kaeya" : ["Fourrure", "Cryo", "Favonius", "Capitaine", "Cheveux bleus", "Épée à 1 main", "Mondstadt", "Cache-oeil", "Khaenri'ah", "Homme"],
          "Jean" : ["Favonius", "Grand Maître", "Anémo", "Blond", "Tenue blanche", "Épée à 1 main", "Pissenlit", "Lion", "Queue de cheval", "Femme"],
          "Albedo" : ["Blond", "Alchimiste", "Favonius", "Mondstadt", "Géo", "Épée à 1 main", "Dosdragons", "Rhinedottir", "Perfection", "Très puissant", "Art de Khemia"],
          "Sucrose" : ["Femme", "Assistant", "Cheveux verts", "Anémo", "Catalyseur", "Lunettes", "Alchimiste", "Mondstadt", "Hypostases", "Vêtements bleus/blancs"],
          "Venti" : ["Archon", "Anémo", "Arc", "Savoir immense", "Mondstadt", "Barde", "Alcool", "Esprit du vent", "Liberté", "Lyre", "Collants", "Tenue verte", "Très vieux"],
          "Dvalin" : ["Dragon", "Anémo", "4 vents", "Mondstadt", "Très vieux", "Corrompu", "Bleu", "Protecteur", "Cristal"],
          "Deshret" : ["Roi écarlate", "Roi-Dieu", "Molrani Rukkhadevata + Nabu Malikata", "Désert", "Connaissance interdite", "Pyramides", "Mort", "Érémites"],
          "Orobashi" : ["Dieu", "Serpent", "Inazuma", "Enkanomia", "Battu par Ei", "Tatarigami", "Mer Noire"],
          "Nibelung" : ["Second Souverain", "Dragon", "Connaissance interdite", "Guerre", "Clous divins", "Création des gnosis"],
          "Diona" : ["Alcool", "Chasse", "Arc", "Cheveux roses", "Chat", "Petit", "Femme", "Mondstadt", "Cryo", "Chapeau"],
          "Ayato" : ["Bubble Tea", "Épée à 1 main", "Inazuma", "Cheveux bleus", "Bien habillé", "Hydro", "Chef", "Élégant", "Beauté Réfléchie"],
          "Tartaglia" : ["Skirk", "Fatui", "Cheveux roux", "Hydro", "Bien habillé", "Masque", "Posture du démon", "Arc", "Dagues", "Cape rouge", "Gants", "Narval", "Force", "Jeune Sire", "Abîme"],
          "Ayaka" : ["Femme", "Cryo", "Épée à 1 main", "Danse", "Cheveux bleus", "Robe", "Armure", "Éventail", "Inazuma", "Héron"],
          "Xiao" : ["Démons", "Cheveux verts","Lance","Tofu","Rêves","Anémo","Masque","Tatouages","Liyue","Adepte"],
          "Signora" : ["Sorcière", "Mondstadt", "Flammes ardentes", "Fatui", "La Demoiselle", "Femme", "Pyro","Cryo","Masque", "Cheveux blonds", "Cape rouge", "Rosalyne"],
          "Alice" : ["Hexenzirkel", "Sorcière", "Pyro", "Dodoco", "Millénaire", "Connaissances infinies", "Comportement destructeur", "Chapeau", "Elfe"],
          "Ronova" : ["Ombre", "Mort", "Malédiction", "Cataclysme", "Cheveux blancs", "Très vieux", "Ailes", "6 yeux", "Puni", "Triquetra","Elfe"],
          "Hu Tao" : ["Papillon", "Pyro", "Lance", "Liyue", "Mort", "Fantôme", "Cheveux noirs", "Fleurs rouges", "Cercueil"],
          "Ortell" : ["Eau", "Vortex", "Liyue", "Vaincu par le Zhong", "Dieu", "Lance", "Tartaglia", "Talisman"],
          "Guizhong" : ["Dieu", "Poussière", "Cheveux Gris", "Liyue", "Inventions", "Adepte", "Baliste", "Souveraine du Royaume des nuages"],
          "Xianyun" : ["Cheveux noirs", "Adepte", "Lunettes", "Yeux verts", "Épingle à cheveux", "Anémo", "Oiseau", "Liyue", "Catalyseur"],
          "Noelle" : ["Robe","Armure","Mondstadt","Géo","Claymore","Servante","Cheveux gris","Force"],
          "Razor" : ["Loup", "Cheveux gris", "Électro", "Claymore", "1 douche à son actif", "Abandoné", "Forêt"],
          "Arlecchino" : ["Le valet", "Fatui", "Enfants", "Lune écarlate", "Père", "Dettes", "Bien habillé", "A battu Crucabena", "Cheveux blancs", "6 yeux", "Foyer", "Faux", "Ailes", "Pyro", "Lance", "Grande"],
          "Lyney" : ["Fatui", "Pyro", "Arc", "Magicien", "Chapeau", "Cartes", "Fontaine", "Fraterie", "Vêtements noirs", "Cheveux blonds", "Homme"],
          "Lynette" : ["Fatui", "Anémo", "Magicien", "Chapeau", "Chat", "Épée à 1 main", "Timide", "Fontaine", "Vêtements noirs", "Noeud papillon","Cheveux blonds","Collants","Fraterie", "Femme"],
          "Freminet" : ["Fatui", "Taches de rousseur", "Fraterie",'Introverti',"Claymore","Cryo","Physique","Vêtements noirs","Fontaine", "Plongée", "Homme"],
          "Dottore" : ["Fatui", "Le Médecin", "Sumeru", "Académie", "Clones", "Masque", "Tenue blanche", "Cheveux bleus","Cobayes","Irminsul"],
          "Pantalone" : ["Fatui", "Le Fortuné", "Cheveux noirs","Banquier","Haine des moras","Lunettes","Pas d'oeil divin", "Forteresse de Méropide"],
          "Malikata" : ["Sumeru", "Désert", "Femme", "Blond", "Yeux violets", "Sagesse", "Déesse des fleurs", "Festival de Sabzeruz", "Fée"],
          "Venessa" : ["Mondstadt", "Cheveux rouges", "Femme", "Chevalier au Pissenlit", "Faucon", "Celestia", "Rebellion", "Muratan", "Venti"],
          "Navia" : ["Géo", "Femme", "Claymore", "Fontaine", "Poisson", "Mafia", "Lunettes", "Fusil à pompe", "Parapluie", "Robe", "Chapeau","Cheveux jaunes"],
          "Clorinde" : ["Électro", "Épée à 1 main", "Femme", "Dueliste", "Pistolet", "Tenue noire et violette", "Chapeau", "Collants", "Fontaine"],
          "Bennett" : ["Homme", "Pyro", "Malchance", "Aventurier", "Épée à 1 main", "Lunettes d'aviateur", "Pansement", "Cheveux blanc", "Yeux verts", "Natlan", "Mondstadt", "Mer cendrée", "Survivant"],
          "Lisa" : ["Collants", "Tenue violette", "Chapeau", "Sorcière", "Connaissance", "Électro", "Catalyseur", "Favonius", "Cheveux bruns", "Malédiction", "Yeux verts"],
          "Klee" : ["Pyro", "Catalyseur","Vêtements rouges","Comportement destructeur", "Chapeau","Mondstadt","Dodoco","Cheveux blancs","Elfe","Bombes"],
          "Kaveh" : ["Sumeru","Architecte","Claymore","Dendro","Colloc","Cheveux blonds","Valise","Fauché","Cape rouge","Haut blanc"],
          "Sethos": ["Électro","Arc","Sumeru","Hermanubis","Cheveux bruns","Cape jaune","Yeux verts","Désert"],
          "Cyno":["Électro","Lance","Sumeru","Désert","Cheveux blancs","Hermanubis","Loup","Justice","Matra","Général", "Blagues"],
          "Furina" : ["Vieux","Femme","Cheveux blancs","Hydro","Épée à 1 main","Chapeau","Théâtre","500 ans","Comédie","Fontaine"],
          "Foçalors" : ["Rebellion","Archon","Hydro","Justice","Tribunal","Tenue blanche","Océanides", "Oratrice Mécanique d'Analyse Cardinale 🎶","Fontaine"],
          "Andros" : ["Loup", "Boréal", "Dieu", "Seigneur", "Mondstadt","4 Vents"],
          "Zhongli" : ["Archon","Liyue","Mora","Cheveux bruns","Bien habillé","Vin","Ordre","Contrat","Fauché","Grand","Géo","Homme"],
          "Eula" : ["Danse", "Aristocratie", "Femme","Favonius","Cheveux bleus","Claymore","Cryo","Physique","Reconnaissance","Chevalier aux embruns"],
          "Xingqiu" : ["Hydro","Épée à 1 main", "Cheveux bleus", "Guhua", "Livres", "Feiyun","Bien habillé","Taille moyenne","Homme","Liyue"],
          "Barbara" : ["Église", "Blond", "Femme", "Hydro", "Mondstadt","Draconesse", "Catalyseur", "Musique", "Jean", "Robe", "Fans","Tenue blanche"],
          "Fischl" : ["Tenue noire et violette", "Femme", "Blond", "Corbeau", "Électro", "Cache-oeil", "Mondstadt", "Yeux verts", "Arc", "Collants", "Aventurier", "Théâtre", "Princesse", "Amy"],
          "Rosalia" : ["Mondstadt", "Église", "Femme", "Cheveux roses", "Lance", "Assassin", "Espion", "Cryo"],
          "Varka" : ["Grand Maître", "Favonius", "Très puissant", "Mondstadt", "Blond", "Hexenzirkel", "Chevalier de Boreas", "Concours de poisson contre Mavuika", "Grand", "Nod-Krai"],
          "Mika" : ["Mondstadt", "Blond", "Lance", "Arbalète", "Éclaireur", "Favonius", "Manteau bleu", "Schmidt", "Cartographe", "Cryo", "Homme"],
          "Xiuhcoatl" : ["Natlan", "Dragon", "Pyro", "Gosoythoth", "Serpent", "Ailes", "Flamme primitive", "Battu par Xbalanque"],
          "Pulcinella" : ["Petit", "Fatui", "Lunettes", "Le Coq", "Moustache", "Chapeau", "Snezhnaya", "Maire", "Cheveux blancs"],
          "Yoimiya" : ["Inazuma", "Pyro", "Femme", "Arc", "Étincelles", "Feu d'artifice", "Bonne humeur", "Blond", "Naganohara", "Vêtements rouges"],
          "Itto" : ["Géo", "Claymore", "Ushi", "Taureau", "Oni", "Cheveux blancs", "Musclé", "Haricots", "Géo", "Inazuma", "Massue", "Gang"],
          "Yae Miko" : ["Cheveux roses", "Inazuma", "Catalyseur", "Électro", "Cerisier", "Prêtre", "Renard", "Vieux", "Grand", "Femme", "Tenue blanche et rouge"],
          "Kokomi" : ["Inazuma", "Watatsumi", "Stratège", "Hydro", "Catalyseur", "Méduse", "Tenue bleue", "Prêtre", "Résistance", "Femme","Catalyseur"],
          "Shinobu" : ["Ninja", "Femme", "Inazuma", "Gang", "Cheveux verts","Masque","Épée à 1 main", "Électro", "Yeux violets"],
          "Heizou" : ["Détective", "Inazuma", "Arts martiaux", "Cheveux rouges", "Anémo", "Catalyseur", "Haut blanc", "Short jaune","Homme", "Yeux verts"],
          "Rhinedottir" : ["Alchimie", "Blond", "Femme", "Ombre", "Pecheurs", "Khaenri'ah", "Art de Khemia", "Durin", "Albedo", "Hexenzirkel", "Limiers de faille", "Cataclysme"],
          "Wriothesley" : ["Catalyseur", "Cryo", "Homme", "Fontaine", "Menottes", "Art martiaux", "Tué ses parents", "Prisonnier", "Directeur", "Forteresse"],
          "Nahida" : ["Sumeru", "Enfermé", "Archon", "Femme", "Petit", "Aranara", "Catalyseur", "Cheveux blancs", "Irminsul", "Mal aimé", "Sagesse"],
          "Rukkhadevata" : ["Archon", "Sumeru", "Sagesse", "Femme", "Grand", "Aranara", "Mort", "Irminsul", "Reine Aranyani", "Terminal akashien"],
          "Xiangling" : ["Femme", "Pyro", "Cuisine", "Lance", "Cheveux noirs", "Marchosius", "Liyue"],
          "Skirk" : ["Femme","Cryo","Épée à 1 main", "Abîme", "Surtalogi", "Posture du démon", "Cheveux blancs", "Autre monde","Yeux roses"],
          "Surtalogi" : ["Cavalier abominable", "Pecheur","Khaenri'ah", "Force","Skirk", "Narval", "Autre monde", "Homme", "Immortel"],
          "Elynas" : ["Fontaine", "Mélusine", "Grand", "Père", "Narzissenkreuz", "Ma mère","Eau primordiale"],
          "Emilie" : ["Fontaine", "Dendro", "Lanterne", "Catalyseur", "Blond", "Parfum", "Lunettes", "Robe verte"]
          }


@bot.tree.command(name="babinette", description="Devine le perso genshin ! Pour trouver les plus gros nerds.")
async def devinette(interaction: discord.Interaction):
    # Choisit un personnage au hasard
    perso, caract = choice(list(persos.items()))
    indices = sample(caract, 3)

    await interaction.response.send_message(
        f"🔍 Trouve le perso Genshin avec ces 3 indices :\n"
        f"• {indices[0]}\n"
        f"• {indices[1]}\n"
        f"• {indices[2]}\n\n"
        f"Réponds dans le chat (30 secondes) !"
    )

    def check(msg):
        return (
            msg.channel == interaction.channel
            and not msg.author.bot
        )

    try:
        msg = await bot.wait_for("message", check=check, timeout=30)
        user_id = msg.author.id
        pseudo = msg.author.name

        cursor.execute("SELECT correct, total FROM babinette_scores WHERE user_id = %s", (user_id,))
        data = cursor.fetchone()
        correct, total = data if data else (0, 0)
        total += 1
        if msg.content.strip().lower() == perso.lower():
            correct += 1
            await interaction.followup.send(f"✅ Bravo {msg.author.mention} ! La bonne réponse était bien **{perso}**. Mouais ok ça passe t'es pas trop nul...")
        else:
            await interaction.followup.send(f"❌ Mauvaise réponse, {msg.author.mention} ! C'était **{perso}**. \nT'es vraiment super nul...")
        cursor.execute("""
            INSERT INTO babinette_scores (user_id, pseudo, correct, total)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE pseudo=VALUES(pseudo), correct=VALUES(correct), total=VALUES(total)
        """, (user_id, pseudo, correct, total))

        conn.commit()
    except asyncio.TimeoutError:
        await interaction.followup.send(f"⏱️ Temps écoulé ! La bonne réponse était **{perso}**. \nT'es vraiment super nul...")

@bot.tree.command(name="babipodium", description="Affiche le top 5 des plus gros nerds de Genshin.")
async def babipodium(interaction: discord.Interaction):

    cursor.execute("""
    SELECT pseudo, correct, total,
           ROUND(CAST(correct AS FLOAT) / total * 100, 1) as ratio
    FROM babinette_scores
    WHERE total > 0
    ORDER BY correct DESC, ratio DESC
    LIMIT 5
    """)

    results = cursor.fetchall()
    conn.close()

    if not results:
        await interaction.response.send_message("Aucune donnée pour le moment. J'espère que t'es pas trop nul.")
        return

    podium = "\n".join(
        f"**#{i+1}** – {row[0]} : {row[1]}/{row[2]} bonnes réponses ({row[3]}%)"
        for i, row in enumerate(results)
    )

    await interaction.response.send_message("🏆 **Top 5 des nerds Genshin** 🧠\n" + podium)
    #await interaction.response.send_message("🏆 **Top 5 des nerds Genshin** 🧠\nC'est Flo le meilleur hehe")

@bot.event
async def on_message(message):
    rep = False
    if message.content[:4] == "babi":
        rep = True
    if message.author == bot.user:
        return
    if bot.user in message.mentions:
        await message.channel.send(choice(("Tu t'es cru ou à me ping ? Tu veux te battre ? 😤", "Tu oses ping le grand, le beau, la parfait Babibel Artificiel ??!! Mortel impertinent ! (à ne pas confondre avec le Babibel Originel, lui il est nul)")))
        return

    user_id = message.author.id
    contenu = message.content.lower()
    if "tg" in contenu or "emmerde" in contenu:
        await message.channel.send("Nan mais tu te calmes enfait. J'vais t'apprendre le respect moi. Tu la fermes pendant 10secondes voilà. Petit effronté.")
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False

        try:
            # Retire la permission d'envoyer des messages dans le salon actuel
            await message.channel.set_permissions(message.author, overwrite=overwrite)
            await asyncio.sleep(10)  # Attendre 10 secondes

            # Réinitialise les permissions (retour à la normale)
            await message.channel.set_permissions(message.author, overwrite=None)
            await message.channel.send(f"{message.author.mention} est de retour... Malheureusement. Tu nous avais vraiment pas manqué. Fais gaffe à toi sinon j'te remute.")
        except discord.Forbidden:
            await message.channel.send("Je n'ai pas les permissions pour le faire 😭")
        except Exception as e:
            await message.channel.send(f"Une erreur est survenue : {e}")
        return
    for mot, reponse in mots_cles.items():
        if mot in contenu:
            rep = True
            if callable(reponse):
                await message.channel.send(reponse())
            else:
                await message.channel.send(reponse)
    if user_id == id["Abel"]:
        prob = randint(0,9)
        if prob == 0:
            rep = True
            await message.channel.send("Imposteur ! Je deviendrai le seul et l'unique Babibel !")
    elif user_id == id["Dany"]:
        prob = randint(0,15)
        if prob == 0:
            rep = True
            await message.channel.send("Je te vois Dany...tu n'es pas seul...je t'observe...")
    elif user_id == id["Jonathan"]:
        prob = randint(0,15)
        if prob == 0:
            rep = True
            await message.channel.send("Je pense que tu devrais descendre d'un ton Jonathan ! Je suis pas mamie gateau moi.")
    if user_id in noms:
        perso_dict = noms[user_id][1]
        for mot, rep in perso_dict.items():
            if mot.lower() in contenu:
                await message.channel.send(rep)
                break
    for nom, emoji in react.items():
        if nom.lower() in message.content.lower():
            try:
                await message.add_reaction(emoji)
            except discord.HTTPException:
                print(f"Impossible d'ajouter la réaction {emoji} pour {nom}")
    

    await bot.process_commands(message)



bot.run(os.getenv("TOKEN"))