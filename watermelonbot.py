import random
import requests
import COVID19Py
import discord
from tcp_latency import measure_latency
import json
import psutil
from subprocess import check_output
import pandas
import storage
import tarot
import taroy
import ball
import sushi
from pymongo import MongoClient
from pandas import DataFrame

client = discord.Client()

CONNECTION_STRING = storage.MONGO
db = MongoClient(CONNECTION_STRING)
dbname = db.get_database('discord-db')
coll = dbname['sorry-count']

@client.event
async def on_ready():
    print("I AM ON!")
    print("current cpu usage: ", + psutil.cpu_percent())

@client.event
async def on_message(message):
    if message.content.find("!hi") != -1:
        await message.channel.send("Henlo!")
    elif message.content == "!test":
        await message.channel.send("This works!")

    #roll command
    elif message.content.upper().startswith('!ROLL'):
        args = message.content.split(' ')
        ran1 = random.randint(1, int(args[1]))
        emb1 = discord.Embed(title='The number you rolled is!', description='%s' % ran1, colour=0x00ff00)
        await message.channel.send(embed=emb1)

    #change bot status command
    elif message.content.upper().startswith('!GAME'):
        args = message.content.split(' ')
        game = discord.Game(name=("%s" % (" ".join(args[1:]))))
        await client.change_presence(status=discord.Status.online, activity=game)

    #amish command
    elif message.content == "!howamishami":
        ran2 = random.randint(1, 100)
        emb1 = discord.Embed(title='Amish Meter!', description="You are " + '%s' % ran2 + "% amish!", colour=0x00ff00)
        await message.channel.send(embed=emb1)

    #british command
    elif message.content == "!howbritishami":
        ran3 = random.randint(1, 100)
        emb1 = discord.Embed(title='British Meter!', description="You are " + '%s' % ran3 + "% British!", colour=0x00ff00)
        await message.channel.send(embed=emb1)

    #birtish command with name
    elif message.content.upper().startswith('!HOWBRITISHIS'):
        args = message.content.split(' ')
        ran4 = random.randint(1, 100)
        emb1 = discord.Embed(title='British Meter!', description="THE BRITISH METER DEFINES " + args[1] + " AS " + '%s' % ran4 + "% BRITISH!!!", colour=0x00ff00)
        await message.channel.send(embed=emb1)

    #amish command with name
    elif message.content.upper().startswith('!HOWAMISHIS'):
        args = message.content.split(' ')
        ran5 = random.randint(1, 100)
        emb1 = discord.Embed(title='Amish Meter!', description="THE AMISH METER DEFINES " + args[1] + " AS " + '%s' % ran5 + "% AMISH!!!", colour=0x00ff00)
        await message.channel.send(embed=emb1)

    #chaotic cat
    elif message.content.upper().find("AAAAAA") != -1:
        emb1 = discord.Embed(title='AAAAAAAAAA')
        emb1.set_image(url="https://cdn.discordapp.com/attachments/654771641166856203/698609942437036092/Screenshot_20200411-150553.jpg")
        await message.channel.send(embed=emb1)


    elif message.content.upper().find("SORRY") != -1:
        if message.author.id == 192800639707906049:
            data = DataFrame(coll.find({'user_id': 192800639707906049}))
            nCount = data['count'].values
            mnCount = nCount[0] + 1
            # emb1 = discord.Embed(title='APOLOGY')
            # emb1.set_image(url="https://cdn.discordapp.com/attachments/721455118104526868/878763816412921896/Screenshot_20210715-201403_Photos.jpg")
            coll.update_one({'user_id': 192800639707906049},{'$set':{'count': mnCount.item(),}})
            await message.channel.send('@everyone ABBY HAS NOW SAID SORRY ' + str(mnCount.item()) + ' TIMES!!!!!!!!!!!')

    elif message.content.upper().find(" DIE ") != -1:
        emb1 = discord.Embed(title='no haha dont youre so sexy :woozy_face: :fuckboy:')
        await message.channel.send(embed=emb1)

    #tarot command
    elif message.content.upper().startswith('!TAROT'):
        await message.channel.send(embed = tarot.card())

    #taroy command
    elif message.content.upper().startswith('!TAROY'):
        # await message.channel.send(embed = taroy.cord())
        await message.channel.send("TAROY??? HAHA you fuckin idiot learn how to spell whydontcha")

    #8ball command
    elif message.content.upper().startswith('!8BALL'):
        await message.channel.send(embed = ball.ball())

    #covid19 case command
    elif message.content.upper().startswith("!COVID"):
        covid19 = COVID19Py.COVID19(data_source="jhu")
        latest = covid19.getLatest()
        emb1 = discord.Embed(title='CurrentCases', description=str(latest), colour=0x00ff00)
        await message.channel.send(embed=emb1)

    #covid19 test comamnd
    elif message.content.upper().startswith("!COVIDC"):
        covid19 = COVID19Py.COVID19(data_source="csbs")
        latest1 = covid19.getChanges()
        emb1 = discord.Embed(title='CurrentCases', description=str(latest1[1]), colour=0x00ff00)
        await message.channel.send(embed=emb1)

    #ping command
    elif message.content.upper().startswith('!PING'):
        ping = str(measure_latency(host='google.com'))
        ping2 = ping.replace("]", "")
        ping3 = ping2.replace("[", "")
        emb1 = discord.Embed(title="Current Latency", description=ping3, colour=0x00ff00)
        await message.channel.send(embed=emb1)

    #help command
    elif message.content.upper().startswith('!HELP'):
        emb1 = discord.Embed(title='Help', description="Current Commands", colour=0x00ff00)
        emb1.add_field(name="!8ball", value="8ball attempts to answer your questions", inline=False)
        emb1.add_field(name="!roll [number]", value="Generates a random number between 0 and specified number", inline=False)
        emb1.add_field(name="!covid", value="Gives a live number of confirmed COVID19 Cases", inline=False)
        emb1.add_field(name="!ping", value="Returns Current Latency", inline=False)
        emb1.add_field(name="!triptoy", value="Sends a random trippy site", inline=False)
        emb1.add_field(name="!howamishis [name]", value="Returns the individual's amish level in a precentage", inline=False)
        emb1.add_field(name="!howbritishis [name]", value="Returns the individual's british level in a precentage", inline=False)
        emb1.add_field(name="!cat", value="Gives you a cat pic :D", inline=False)
        emb1.add_field(name="!catgif", value="Gives you cat gif :DD", inline=False)
        await message.channel.send(embed=emb1)

    #triptoy command
    elif message.content.upper().startswith('!TRIPTOY'):
        ran1 = random.randint(1, 3)
        if ran1 == 1:
            emb1 = discord.Embed(title='TripToy!', url="http://erppy.co", colour=0xff0000)
            await message.channel.send(embed=emb1)
        if ran1 == 2:
            emb1 = discord.Embed(title='TripToy!', url="http://erppy.co", colour=0xff0000)
            await message.channel.send(embed=emb1)
        if ran1 == 3:
            emb1 = discord.Embed(title='TripToy!', url="http://erppy.co", colour=0xff0000)
            await message.channel.send(embed=emb1)

    #cat command (gif)
    elif message.content.upper().startswith('!CATGIF'):
        emb1 = discord.Embed(colour=0x00ff00)
        req = requests.get('http://thecatapi.com/api/images/get?format=src&type=gif')
        emb1.set_image(url="%s" % req.url)
        await message.channel.send(embed=emb1)

    #cat command (png/jpg)
    elif message.content.upper().startswith('!CAT'):
        emb1 = discord.Embed(colour=0x00ff00)
        ran1 = random.randint(1, 2)
        if ran1 == 1:
            req = requests.get('http://thecatapi.com/api/images/get?format=src&type=png')
            emb1.set_image(url="%s" % req.url)
            await message.channel.send(embed=emb1)
        if ran1 == 2:
            req1 = requests.get('http://thecatapi.com/api/images/get?format=src&type=jpg')
            emb1.set_image(url="%s" % req1.url)
            await message.channel.send(embed=emb1)

    elif message.content.upper().startswith('!BAT'):
        emb1 = discord.Embed(title="Fuckin Bats", url="https://cdn.discordapp.com/attachments/518798189982384169/698656050408063138/Why-not.mp4", colour=0x00ff00)
        await message.channel.send(embed=emb1)

    elif message.content.upper().startswith('!STATS'):
        emb1 = discord.Embed(title="Server Status", colour=0xff0000)
        emb1.add_field(name="CPU Usage: ", value=str(psutil.cpu_percent()) + "%")
        emb1.add_field(name="RAM Usage: ", value=str(psutil.virtual_memory()[2]) + "% " + "[" + str(round((psutil.virtual_memory()[3] / 1000000), 2)) + "/" + str(round((psutil.virtual_memory()[0] / 1000000), 2)) + "]MB")
        await message.channel.send(embed=emb1)

    elif message.content.upper().startswith('!SUSHI'):
        await message.channel.send(embed = sushi.sushi())

client.run(storage.TOKEN)
