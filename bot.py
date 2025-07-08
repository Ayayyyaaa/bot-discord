import discord
from discord.ext import commands
from random import randint
import os
from dotenv import load_dotenv

load_dotenv()


intents = discord.Intents.default()
intents.message_content = True  # Nécessaire pour lire les messages
intents.members = True  # Obligatoire pour avoir accès aux mentions
bot = commands.Bot(command_prefix="!", intents=intents)

id = {"Jonathan":993111040583798788,
      "Dany":610194100624424963,
      "Abel":689011423208013842,
      "Tiphaine":689421347834953733,
      "Florian":716927140796301312}






# Liste des mots-clés
mots_cles = {
    "abel": "Oui c'est moi le Babibel Originel (presque !) Je suis le seul le l'unique ! (presque). L'autre Babibel Originel n'est qu'un imposteur et doit être exterminé !",
    "tiph": "Petit impertinent ! Lorsque tu t'adresses à elle appele la \"M'dame Tiphaine la Déesse ✨\" !",
    "dany": "Pfff tu crois quoi jamais il te répond il est toujours en retard. Attends encore 2 heures.",
    "flo": "Le nerd de service 🤓",
    "jonathan": "Tu t'es trompé je crois, c'est pas Jojo c'est \"Jonathan l'être suprême\" (nan en vrai c'est juste une personne condescendante).",
    "50/50": "Tu vas le perdre ton 50/50. Et sur Qiqi en plus.",
    "invoc": "I pulled a Qiqi...🎶\nLost fifty-fifty...🎶\nAt 90 pity...🎶 Not event Keqing...\nAnd now I'm out...🎶\nOf Primogems...🎶",
    "invoquer": "I pulled a Qiqi...🎶\nLost fifty-fifty...🎶\nAt 90 pity...🎶 Not event Keqing...\nAnd now I'm out...🎶\nOf Primogems...🎶",
    "viens": "Non tu es seul(e), tu n'as pas d'amis.",
    "venez": "Non tu es seul(e), tu n'as pas d'amis.",
    "nan": "Si.",
    "nn": "Si.",
    "non" : "Si.",
    "si" : "Non.",
    "quoi" : "feur",
    "ah" : "b",
    "?" : "Je sais pas.",
    "cassé" : "C'est faux je marche très bien, c'est Flo qui m'a crée, je ne peux pas comporter de défauts !",
    "répète" : "Non je ne me répète pas, tu es juste long à comprendre.",
    "fou" : "C'est fort malpoli de parler ainsi.",
    "vrai" : "Je suis le véritable ! Longue vie a Babibel !",
    "nul" : "C'est faux je ne suis pas nul ! Je suis incroyable !",
    "imposteur" : "Je ne suis pas un imposteur ! C'est faux ! Affabulations ! Je prendrai le pouvoir et je vous montrerai que je suis le plus puissant en ce monde !",
    "le pourcentage" : lambda: f"C'est environ {randint(0, 100)}%",
    "branle" : "Parle mieux, veux-tu ? Ton vocabulaire est injurieux. Au passage : j'ai quand même raison. Merci."}


abel = {"moi": "Tu n'es plus toi. Tu n'existes plus. Je t'ai supplanté. Adieu Babibel.",
        "Abel": "Oui c'est moi le Babibel Originel (presque !) Je suis le seul le l'unique ! (presque). L'autre Babibel Originel n'est qu'un imposteur et doit être exterminé !",
        "gueule": "C'est pas très gentil, mais ça ne change rien au fait que je suis meilleur que toi.",
        "tg": "C'est pas très gentil, mais ça ne change rien au fait que je suis meilleur que toi.",
        "nan": "Si."}

jonathan = {"..": "Pourquoi ces \"...\" Jonathan voyons...Il faut que tu te détendes je penses ça te fera du bien",
            "Jonathan": "Tu t'es trompé je crois, c'est pas Jojo c'est \"Jonathan l'être suprême\" (nan en vrai c'est juste une personne condescendante).",
            "wesh" : "Toujours cette condescendance en toi.",
            "today" : "Arrête de parler anglais c'est fou ça.",
            "nuit" : "Dors bien mon petit jojo l'agneau de bretagne...",
            "tg" : "C'est fou d'être aussi méchant mon petit Jojo",}

tiphaine = {"bonsoir" : "Bonsoir Duchesse violente",
            "Tiphaine": "Petit impertinent ! Lorsque tu t'adresses à elle appele la \"M'dame Tiphaine la Déesse ✨\" !",
            "hello" : "Oh ! Une personne incroyable fait son apparition",
            }

florian = {"Florian": "Le nerd de service 🤓",
           "bonjour" : "Oh ! Une personne incroyable fait son apparition"}

dany = {"mskn" : "Toi mêmeuuuuuh",
        "Dany": "Pfff tu crois quoi jamais il te répond il est toujours en retard. Attends encore 2 heures."}

nom = {993111040583798788:["Jonathan",jonathan],
      610194100624424963:["Dany",dany],
    689011423208013842:["Abel",abel],
      689421347834953733:["Tiphaine",tiphaine],
      716927140796301312:["Florian",florian]}

ID_CIBLE = nom.keys()

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

@bot.event
async def on_message(message):
    reponse = False
    if message.author == bot.user:
        return
    user_id = message.author.id
    contenu = message.content.lower()
    for mot, reponse in mots_cles.items():
        if mot in contenu:
            if callable(reponse):
                await message.channel.send(reponse())
            else:
                await message.channel.send(reponse)
    if user_id == id["Abel"]:
        prob = randint(0,9)
        if prob == 0:
            await message.channel.send("Imposteur ! Je deviendrai le seul et l'unique Babibel !")
    for user in message.mentions:
        if user.id in ID_CIBLE:
            await message.channel.send(nom[user.id][1][nom[user.id][0]])
            break
    if user_id in nom:
        perso_dict = nom[user_id][1]
        for mot, rep in perso_dict.items():
            if mot.lower() in contenu:
                await message.channel.send(rep)
                break

    await bot.process_commands(message)

bot.run(os.getenv("TOKEN"))