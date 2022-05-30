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

    elif message.content.upper().find("DIE") != -1:
        emb1 = discord.Embed(title='no haha dont youre so sexy :woozy_face: :fuckboy:')
        await message.channel.send(embed=emb1)


    #tarot command
    elif message.content.upper().startswith('!TAROT'):
        ran6 = random.randint(0, 64)
        if ran6 == 0:
            emb1 = discord.Embed(title="0. The Fool", description="Innocence, freedom, new beginnings, faith")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698621139777486958/IMG_20200411_144112154.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 1:
            emb1 = discord.Embed(title="1. The Magician", description="Creation, manifestation, willpower, skill")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698621424964861952/IMG_20200411_144233165.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 2:
            emb1 = discord.Embed(title="2. The High Priestess", description="Intuition, higher self, spirituality, subconscious")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698623480404377700/IMG_20200411_145848359.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 3:
            emb1 = discord.Embed(title="3. The Empress", description="Harmony, fertility, feminity, nature")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698626006914695168/IMG_20200411_150905787.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 4:
            emb1 = discord.Embed(title="4. The Emperor", description="Masculinity, authority, power, stability")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698626495580602469/IMG_20200411_150935519.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 5:
            emb1 = discord.Embed(title="5. The Hierophant", description="Spiritual guidance, religion, tradition, beliefs")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698626866927501372/IMG_20200411_144334480.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 6:
            emb1 = discord.Embed(title="6. The Lovers", description="Partnership, harmony, love, soul connections")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698627836864364554/IMG_20200411_151546443.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 7:
            emb1 = discord.Embed(title="7. The Chariot", description="Victory, success, determination, self-discipline")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698628173428162590/IMG_20200411_151619471.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 8:
            emb1 = discord.Embed(title="8. Strength", description="Inner strength, courage, bravery, confidence")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698628479515885628/IMG_20200411_151634420.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 9:
            emb1 = discord.Embed(title="9. The Hermit", description="Solitude, soul-searching, self-reflection, spiritual enlightenment")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698628876670337074/IMG_20200411_151648638.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 10:
            emb1 = discord.Embed(title="10. Wheel of Fortune", description="Luck, destiny, fate, change")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698629330498224258/IMG_20200411_151700178.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 11:
            emb1 = discord.Embed(title="11. Justice", description="Justice, truth, honesty, consequences")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698630275734700073/IMG_20200411_152604120.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 12:
            emb1 = discord.Embed(title="12. The Hanged Man", description="Trapped, uncertainty, lack of direction, letting go")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698630583017930872/IMG_20200411_152623379.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 13:
            emb1 = discord.Embed(title="13. Death", description="Transformation, letting go of the past, endings, new beginnings")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698630975088754789/IMG_20200411_152635056.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 14:
            emb1 = discord.Embed(title="14. Temperance", description="Moderation, balance, patience, inner calm")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698631294392991744/IMG_20200411_152648741.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 15:
            emb1 = discord.Embed(title="15. The Devil", description="Addictions, restrictions, mental illness, dependency")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698631584865190048/IMG_20200411_152657881.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 16:
            emb1 = discord.Embed(title="16. The Tower", description="Sudden upheaval, trauma, unexpected change, disaster")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698632453027397632/IMG_20200411_144548381.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 17:
            emb1 = discord.Embed(title="17. The Star", description="Hope, inspiration, healing, renewal")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698632796209545216/IMG_20200411_144806265.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 18:
            emb1 = discord.Embed(title="18. The Moon", description="Anxiety, intuition, dreams, illusion")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698633357914800128/IMG_20200411_153508784.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 19:
            emb1 = discord.Embed(title="19. The Sun", description="Vitality, vibrancy, optimism, freedom")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698633608599961673/IMG_20200411_153519992.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 20:
            emb1 = discord.Embed(title="20. Judgement", description="Forgiveness, decisiveness, judgement, self-assessment")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698633970094571530/IMG_20200411_153529135.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 21:
            emb1 = discord.Embed(title="21. The World", description="Fulfillment, completion, achievement, wholeness")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698634289553604718/IMG_20200411_153539345.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 23:
            emb1 = discord.Embed(title="Ace of Swords", description="New beginnings, good news, potential, growth")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698640418354757792/IMG_20200411_160534585.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 24:
            emb1 = discord.Embed(title="Two of Swords", description="Stalemate, difficult decisions, denial, truce")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698640819149733909/IMG_20200411_160547463.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 25:
            emb1 = discord.Embed(title="Three of Swords", description="Heartbreak, betrayal, separation, grief")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698641120623722546/IMG_20200411_160601212.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 26:
            emb1 = discord.Embed(title="Four of Swords", description="Burn out, stress, self protection, needing solitude")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698641380653793400/IMG_20200411_160612757.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 27:
            emb1 = discord.Embed(title="Five of Swords", description="Defeat, surrender, walking away, falling apart")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698641757683843072/IMG_20200411_160644221.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 28:
            emb1 = discord.Embed(title="Six of Swords", description="Healing, progress, moving forward, relief")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698642715143045180/IMG_20200411_161516224.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 29:
            emb1 = discord.Embed(title="Seven of Swords", description="Deceit, lies, dangerous behavior, sly behavior/motives")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698642988233916519/IMG_20200411_161530229.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 30:
            emb1 = discord.Embed(title="Eight of Swords", description="Victimized, negativity, fear, powerless")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698643425469267988/IMG_20200411_161549790.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 31:
            emb1 = discord.Embed(title="Nine of Swords", description="Breaking point, regret, focusing on the past, despair")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698643809583628318/IMG_20200411_161604267.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 32:
            emb1 = discord.Embed(title="Ten of Swords", description="Backstabbing, betrayal, nail in the coffin, goodbyes")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698644123447590952/IMG_20200411_161617411.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 33:
            emb1 = discord.Embed(title="Page of Swords", description="Planning, patience, using the mind, fairness")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698644721098162226/IMG_20200411_162335015.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 34:
            emb1 = discord.Embed(title="Knight of Swords", description="Determination, impulsive, ambitious, carpe diem (seize the moment)")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698645122317025311/IMG_20200411_162348961.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 35:
            emb1 = discord.Embed(title="Queen of Swords", description="Witty, independent, communicative, honest")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698645522268946502/IMG_20200411_162402039.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 36:
            emb1 = discord.Embed(title="King of Swords", description="Structure, routine, lawful, morals")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698646028731154573/IMG_20200411_162416255.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 37:
            emb1 = discord.Embed(title="Ace of Cups", description="New relationships, love, new beginnings, celebrations")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698734982365184020/IMG_20200411_222144708.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 38:
            emb1 = discord.Embed(title="Two of Cups", description="Partnership, unity, love, compatibility")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698735336188018688/IMG_20200411_222158579.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 39:
            emb1 = discord.Embed(title="Three of Cups", description="Reunions, celebrations, gatherings, happy times")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698735658742710344/IMG_20200411_222213330.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 40:
            emb1 = discord.Embed(title="Four of Cups", description="Missed opportunities, apathy, nostalgia, negativity")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698736126898470942/IMG_20200411_222225741.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 41:
            emb1 = discord.Embed(title="Five of Cups", description="Grief, sadness, mourning, abandonment")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698736467299794984/IMG_20200411_222237018.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 42:
            emb1 = discord.Embed(title="Six of Cups", description="Childhood memories, homesickness, youthfulness, childish activities")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698737250783199232/IMG_20200411_223028858.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 43:
            emb1 = discord.Embed(title="Seven of Cups", description="Choices, decisions, dreaming, meditation")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698737638026379334/IMG_20200411_223057516.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 44:
            emb1 = discord.Embed(title="Eight of Cups", description="Escapism, withdrawal, disappointment, loneliness")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698738457337659412/IMG_20200411_223113665.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 45:
            emb1 = discord.Embed(title="Nine of Cups", description="Triumph, prosperity, abundance, rewards")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698738784874922104/IMG_20200411_223132501.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 46:
            emb1 = discord.Embed(title="Ten of Cups", description="Celebration, fulfillment, family, happy ever after")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698739089415077928/IMG_20200411_223151788.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 47:
            emb1 = discord.Embed(title="Page of Cups", description="Inner child, kindness, innocence, naivety")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698740542116331580/IMG_20200411_224203703.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 48:
            emb1 = discord.Embed(title="Knight of Cups", description="Following the heart, chivalry, diplomatic, artistic")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698741227264409650/IMG_20200411_224215966.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 49:
            emb1 = discord.Embed(title="Queen of Cups", description="Mature female, kindness, healer, supporter")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698741661093724200/IMG_20200411_224230979.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 50:
            emb1 = discord.Embed(title="King of Cups", description="Mature male, diplomatic, devoted, family oriented")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/698741943835951144/IMG_20200411_224246798.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 51:
            emb1 = discord.Embed(title="Ace of Pentacles", description="Manifestation, new financial opportunities, money, prosperity")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/699088425436839956/IMG_20200412_213337325.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 52:
            emb1 = discord.Embed(title="Two of Pentacles", description="Balance, adaptability, resourcefulness, flexibility")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/699089077223292928/IMG_20200412_213356195.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 53:
            emb1 = discord.Embed(title="Three of Pentacles", description="Teamwork, goals, effort, apprenticeship")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/699090399204999198/IMG_20200412_213413612.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 54:
            emb1 = discord.Embed(title="Four of Pentacles", description="Holding onto things, boundaries, keeping to yourself, control")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/699091399496433664/IMG_20200412_213427430.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 55:
            emb1 = discord.Embed(title="Five of Pentacles", description="Financial loss, struggle, bad luck, negative change")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/699092821998698496/IMG_20200412_213441973.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 56:
            emb1 = discord.Embed(title="Six of Pentacles", description="Gifts, generosity, equality, growth")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/699093529753813052/IMG_20200412_213455392.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 57:
            emb1 = discord.Embed(title="Seven of Pentacles", description="Contemplation, financial rewards, results, finishing projects")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/699094300578939000/IMG_20200412_213625953.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 58:
            emb1 = discord.Embed(title="Eight of Pentacles", description="Craftsmanship, quality, reputation, skill")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/699095387042086993/IMG_20200412_213638773.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 59:
            emb1 = discord.Embed(title="Nine of Pentacles", description="Independence, wisdom, maturity, freedom")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/699099967054151691/IMG_20200412_213651712.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 60:
            emb1 = discord.Embed(title="Ten of Pentacles", description="Inheritance, privilege, unexpected financial gain, traditional")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/699104154295074816/IMG_20200412_213722207.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 61:
            emb1 = discord.Embed(title="Page of Pentacles", description="Responsibility, opportunities, support, ambitions")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/699106806571728996/IMG_20200412_213734622.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 62:
            emb1 = discord.Embed(title="Knight of Pentacles", description="Dedication, loyalty, routine, productivity")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/699107476468924437/IMG_20200412_213750238.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 63:
            emb1 = discord.Embed(title="Queen of Pentacles", description="Patience, nurture, healing, businessman/woman")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/699109635461742642/IMG_20200412_213802116.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 64:
            emb1 = discord.Embed(title="King of Pentacles", description="Entrepreneurship, steadiness, leadership, discipline")
            emb1.set_image(url="https://cdn.discordapp.com/attachments/698615103016140810/699110556392620063/IMG_20200412_213815329.jpg")
            await message.channel.send(embed=emb1)
        #8ball command
    elif message.content.upper().startswith('!8BALL'):
        ran1 = random.randint(1, 13)
        if ran1 == 1:
            emb1 = discord.Embed(title='8Ball', description='Fuck you, No', colour=0xff0000)
            await message.channel.send(embed=emb1)
        if ran1 == 2:
            emb1 = discord.Embed(title='8Ball', description='Get rEKT, NO!', colour=0xff0000)
            await message.channel.send(embed=emb1)
        if ran1 == 3:
            emb1 = discord.Embed(title='8Ball', description='Hm.. Thats a solid fucking no from me.', colour=0xff0000)
            await message.channel.send(embed=emb1)
        if ran1 == 4:
            emb1 = discord.Embed(title='8Ball', description='Indeedidly nOPE.', colour=0xff0000)
            await message.channel.send(embed=emb1)
        if ran1 == 5:
            emb1 = discord.Embed(title='8Ball', description='Why are you asking me these questions, I have no clue.', colour=0x0000ff)
            await message.channel.send(embed=emb1)
        if ran1 == 6:
            emb1 = discord.Embed(title='8Ball', description='Im not a fucking psychic, Ask someone else.', colour=0x0000ff)
            await message.channel.send(embed=emb1)
        if ran1 == 7:
            emb1 = discord.Embed(title='8Ball', description='Go ask another person and leave me the fuck alone.', colour=0x0000ff)
            await message.channel.send(embed=emb1)
        if ran1 == 8:
            emb1 = discord.Embed(title='8Ball', description='I honestly have no fucking idea.', colour=0x0000ff)
            await message.channel.send(embed=emb1)
        if ran1 == 9:
            emb1 = discord.Embed(title='8Ball', description='Fuck yes, All the way!', colour=0x00ff00)
            await message.channel.send(embed=emb1)
        if ran1 == 10:
            emb1 = discord.Embed(title='8Ball', description='Thats a solid cucking n- I mean yes.', colour=0x00ff00)
            await message.channel.send(embed=emb1)
        if ran1 == 11:
            emb1 = discord.Embed(title='8Ball', description='Hmm.. Yes.. Now can you leave me alone? Im trying to do nothing.', colour=0x00ff00)
            await message.channel.send(embed=emb1)
        if ran1 == 12:
            emb1 = discord.Embed(title='8Ball', description='Yis', colour=0x00ff00)
            await message.channel.send(embed=emb1)
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
        await message.channel.send(embed=emb1)\
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
        ran6 = random.randint(1, 9)
        if ran6 == 1:
            emb1 = discord.Embed(colour=0x00ff00)
            emb1.set_image(url="https://cdn.discordapp.com/attachments/688801208810733574/700749009496702977/20200417_104215.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 2:
            emb1 = discord.Embed(colour=0x00ff00)
            emb1.set_image(url="https://cdn.discordapp.com/attachments/688801208810733574/700749010293489684/received_513765259306055.jpeg")
            await message.channel.send(embed=emb1)
        if ran6 == 3:
            emb1 = discord.Embed(colour=0x00ff00)
            emb1.set_image(url="https://cdn.discordapp.com/attachments/688801208810733574/700749010520113192/USER_SCOPED_TEMP_DATA_MSGR_PHOTO_FOR_UPLOAD_1586748009274.jpeg")
            await message.channel.send(embed=emb1)
        if ran6 == 4:
            emb1 = discord.Embed(colour=0x00ff00)
            emb1.set_image(url="https://cdn.discordapp.com/attachments/688801208810733574/700749010998263818/USER_SCOPED_TEMP_DATA_MSGR_PHOTO_FOR_UPLOAD_1586540131067.jpeg")
            await message.channel.send(embed=emb1)
        if ran6 == 5:
            emb1 = discord.Embed(colour=0x00ff00)
            emb1.set_image(url="https://cdn.discordapp.com/attachments/688801208810733574/700749011425951784/USER_SCOPED_TEMP_DATA_MSGR_PHOTO_FOR_UPLOAD_1584549627669.jpeg")
            await message.channel.send(embed=emb1)
        if ran6 == 6:
            emb1 = discord.Embed(colour=0x00ff00)
            emb1.set_image(url="https://cdn.discordapp.com/attachments/688801208810733574/700749011757563985/20200317_152708.jpg")
            await message.channel.send(embed=emb1)
        if ran6 == 7:
            emb1 = discord.Embed(colour=0x00ff00)
            emb1.set_image(url="https://cdn.discordapp.com/attachments/688801208810733574/700749012168343593/USER_SCOPED_TEMP_DATA_MSGR_PHOTO_FOR_UPLOAD_1584198779127.jpeg")
            await message.channel.send(embed=emb1)
        if ran6 == 8:
            emb1 = discord.Embed(colour=0x00ff00)
            emb1.set_image(url="https://cdn.discordapp.com/attachments/688801208810733574/700749012474658906/USER_SCOPED_TEMP_DATA_MSGR_PHOTO_FOR_UPLOAD_1584048346777.jpeg")
            await message.channel.send(embed=emb1)
        if ran6 == 9:
            emb1 = discord.Embed(colour=0x00ff00)
            emb1.set_image(url="https://cdn.discordapp.com/attachments/688801208810733574/700749160625864734/20200228_112201.jpg")
            await message.channel.send(embed=emb1)

client.run(storage.TOKEN)
