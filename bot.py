import discord
from discord.ext import commands
from random import randint
import os
from dotenv import load_dotenv
from discord.ext.commands import has_permissions, MissingPermissions
import asyncio




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
    "?" : "Je sais pas.",
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
    "trois" : "Soleil."}


abel = {"moi": "Tu n'es plus toi. Tu n'existes plus. Je t'ai supplanté. Adieu Babibel.",
        "Abel": "Oui c'est moi le Babibel Originel (presque !) Je suis le seul le l'unique ! (presque). L'autre Babibel Originel n'est qu'un imposteur et doit être exterminé !",
        "gueule": "C'est pas très gentil, mais ça ne change rien au fait que je suis meilleur que toi.",
        "tg": "C'est pas très gentil, mais ça ne change rien au fait que je suis meilleur que toi.",
        "nan": "Si.",
        " sais" : "Si je sais beaucoup de choses. Que je suis en tout points supérieur à toi par exemple.",
        "con " : "Recourir aux insultes...le moyen d'expression des faibles. C'est ce qui nous différencie : tu es faible, je suis parfait et fort.",
        "connard" : "Recourir aux insultes...le moyen d'expression des faibles. C'est ce qui nous différencie : tu es faible, je suis parfait et fort.",
        "fdp" : "Encore une fois, tu te montres d'une vulgarité sans nom.",
        "cheh" : "Juste...Non ? Rien d'autre à ajouter."}

jonathan = {"..": "Pourquoi ces \"...\" Jonathan voyons...Il faut que tu te détendes je penses ça te fera du bien",
            "Jonathan": "Tu t'es trompé je crois, c'est pas Jojo c'est \"Jonathan l'être suprême\" (nan en vrai c'est juste une personne condescendante).",
            "wesh" : "Toujours cette condescendance en toi.",
            "today" : "Arrête de parler anglais c'est fou ça.",
            "nuit" : "Dors bien mon petit jojo l'agneau de bretagne...",
            "tg" : "C'est fou d'être aussi méchant mon petit Jojo",
            "respect" : "Le respect ? Il y en a toujours eu, et il y en aura toujours. Tu ne le mérites justes pas mon petit Jonathan.",
            "!" : "Calme calme Jojo...Prends une grande respiration et purge cette impulsivité qui règne en toi...",
            "toupet" : "Non non non mon Jojo, je n'ai pas de toupet, car je suis le grand, l'unique et le seul, le plus parfait Babibel !",
            "bonjour" : "Oh berk, pourquoi tu me dis bonjour ? Je peux quelque chose pour toi ?",
            "hello" : "Hallo Jonathan, du bist ein Kartoffel salat !"}

tiphaine = {"bonsoir" : "Bonsoir Duchesse violente",
            "Tiphaine": "Petit impertinent ! Lorsque tu t'adresses à elle appele la \"M'dame Tiphaine la Déesse ✨\" !",
            "hello" : "Oh ! Une personne incroyable fait son apparition",
            }

florian = {"Florian": "Le nerd de service 🤓",
           "bonjour" : "Oh ! Une personne incroyable fait son apparition",
           "mon amour" : "Ooooh Tiphaine, tu es la plus belle, la plus gentille, la plus parfaite personne qui puis exister. Je t'aime plus que tout au monde. Merci."}

dany = {"mskn" : "Mskn toi mêmeuuuuuh",
        "Dany": "Pfff tu crois quoi Dany jamais il te répond il est toujours en retard. Attends encore 2 heures."}

nom = {993111040583798788:["Jonathan",jonathan],
      610194100624424963:["Dany",dany],
    689011423208013842:["Abel",abel],
      689421347834953733:["Tiphaine",tiphaine],
      716927140796301312:["Florian",florian]}

ID_CIBLE = nom.keys()

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

@bot.command(name="kick")
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member.name} a été kick parceque {reason}. Bien fait à lui mdr.")


@bot.event
async def on_message(message):
    rep = False
    if message.content[:4] == "babi":
        rep = True
    if message.author == bot.user:
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
        prob = randint(0,19)
        if prob == 0:
            rep = True
            await message.channel.send("Je te vois Dany...tu n'es pas seul...je t'observe...")
    elif user_id == id["Jonathan"]:
        prob = randint(0,19)
        if prob == 0:
            rep = True
            await message.channel.send("Je pense que tu devrais descendre d'un ton Jonathan ! Je suis pas mamie gateau moi.")
    for user in message.mentions:
        if user.id in ID_CIBLE and not rep:
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