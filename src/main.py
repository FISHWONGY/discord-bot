import discord
from discord.ext import commands
import os
import emoji
import random
import requests
from lxml import html
from datetime import datetime, timedelta, time

TOKEN = 'YOUR_TOKEN'

# Set a prefix for your bot
client = commands.Bot(command_prefix='!')


# Bot on ready and give it a status
@client.event
async def on_ready():
    activity = discord.Game(name='Cooking Mama')
    await client.change_presence(status=discord.Status.online, activity=activity)
    print('Bot is running')


# Command for me to clear msg
@client.command(pass_context=True)
async def clear(ctx):
    my_dc = ['fourdigit_id']
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=100):
        messages.append(message)

    if str(ctx.author).split("#")[1] in my_dc:
        await channel.delete_messages(messages)
        await ctx.send('10 messages deleted')
    else:
        await ctx.send('邊個比你del msg?^_^')


# Command that delete the msg only from BOT
@client.command(pass_context=True)
async def clearbotmsg(ctx):
    def predicate(message):
        return message.author.bot
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=20).filter(predicate):
        messages.append(message)

    await channel.delete_messages(messages)


# Reading in txt file for the command !chickensoup
poem_list = []
for root, dirs, files in os.walk('/folder_path'):
    for file in files:
        if file.endswith('.txt'):
            with open(os.path.join(root, file), 'r') as f:
                text = f.read()
                poem_list.append(text)

poemHeader_list = [
    'Here is something for you :)',
    'This is for you ;)',
    'I have got something for you :)',
    'This is just for you (:'
]


@client.command()
async def chickensoup(ctx):
    embed = discord.Embed(
        title='',
        description=random.choice(poem_list),
        color=discord.Color.dark_red()
    )

    embed.set_author(name=random.choice(poemHeader_list))

    await ctx.send(embed=embed)


# Reading in file for the !sonnet command
sonnet_list = []
for root, dirs, files in os.walk('/folder_path'):
    for file in files:
        if file.endswith('.txt'):
            with open(os.path.join(root, file), 'r') as f:
                text2 = f.read()
                sonnet_list.append(text2)


@client.command()
async def sonnet(ctx):
    embed = discord.Embed(
        title='',
        description=random.choice(sonnet_list),
        color=discord.Color.dark_blue()
    )

    embed.set_author(name='AI generated sonnet')

    await ctx.send(embed=embed)


dailyStoic_list = [
    'https://scontent-lht6-1.xx.fbcdn.net/v/t1.0-9/96642608_2606479732909214_1178146448831676416_n.jpg?_nc_cat=111&ccb=1-3&_nc_sid=2c4854&_nc_ohc=UwAa91Ksd3UAX8uXKpU&_nc_ht=scontent-lht6-1.xx&oh=4efdabdabfa87fe4d6dc32e919e32172&oe=607559FE',
    'https://scontent-lht6-1.xx.fbcdn.net/v/t31.0-8/13391671_1762170334006829_4426169166173703076_o.png?_nc_cat=111&ccb=1-3&_nc_sid=9267fe&_nc_ohc=8J29DPjVzfcAX9c763j&_nc_oc=AQnpLNAu2cIh9Y5vlEjdzpG8fbxGDP5-kgVPCMXfXKCXKavivvR9bmWszYkrVhWwWK0&_nc_ht=scontent-lht6-1.xx&oh=6a8a1c395796f260a9a13b06e2ddfccb&oe=6074A6A8',
    'https://scontent-lhr8-2.xx.fbcdn.net/v/t1.0-9/114152140_2663326553891198_5419408039190079842_n.png?_nc_cat=105&ccb=1-3&_nc_sid=2c4854&_nc_ohc=Bq64pvl07OEAX9KxMkd&_nc_ht=scontent-lhr8-2.xx&oh=2445245720c2fd118459799c48a91650&oe=6074E5D3'
]

# Command - stoic
# send out photo from daily stoic
@client.command()
async def stoic(ctx):
    embed = discord.Embed(
        title='Daily Stoic',
        description='',
        color=discord.Color.light_grey()
    )

    embed.set_image(url=random.choice(dailyStoic_list))

    await ctx.send(embed=embed)


# Just a write a command for all Youtube playlist instead
@client.command()
async def playlist(ctx):
    await ctx.send('Conan - \nhttps://www.youtube.com/playlist?list=PLCTUHJBBYiHCsRI6zSzOl676tZf3__Aju\n\n'
                   'Anime - \nhttps://www.youtube.com/playlist?list=PLchRM81iB8u-3LQMwhbDDEaRdSWQlPmcu\n\n'
                   'Korean - \nhttps://www.youtube.com/playlist?list=PLchRM81iB8u8UHE2_uqTxEe0mw_1qWcp4\n\n'
                   'Cartoon - \nhttps://www.youtube.com/playlist?list=PLchRM81iB8u8a-f32Ln2AlJvhjj869bOn')


# Command to make fun for Ferrari lmao
@client.command()
async def ferrarislow(ctx):
    await ctx.send('If Charles was leading on Lap 1, '
                   'by the time we get to the end of the straight, he will be last\n'
                   'https://youtu.be/T04o8fOhBU4')

carlosMeme_List = [
    'https://pbs.twimg.com/media/EX_3kHaWoAIjOL3.jpg',
    'https://preview.redd.it/6qvgudpuu6h51.jpg?auto=webp&s=160b2845995a3e46bb621ff9476b0a94c3a7867b',
    'https://www.meme-arsenal.com/memes/6adecfa8002e0b35f10ea4a1ade9951a.jpg',
    'https://i.ibb.co/jf7QNhK/Screenshot-20210312-130307.jpg',
    'https://media.discordapp.net/attachments/810854425983057950/820809471173460019/image0.jpg'
]


# Command to make fun of carlos
@client.command()
async def poorcarlos(ctx):
    embed = discord.Embed(
        title='Poor Carlos T_T',
        description='',
        color=discord.Color.dark_grey()
    )

    embed.set_image(url=random.choice(carlosMeme_List))

    await ctx.send(embed=embed)


# Command that get the most recent F1 news
@client.command()
async def f1news(ctx):
    page = requests.get('https://www.formula1.com/en/latest/all.html')
    tree = html.fromstring(page.content)
    story_headers = tree.xpath('//p[@class = "f1--s no-margin"]/text()')
    story_link = tree.xpath('//a[@class = "f1-cc f1-cc--reg-primary f1-cc--white-solid f1-image--hover-zoom"]/@href')
    data = []
    for (item1, item2) in zip(story_headers, story_link):
        data.append(item1 + '\n' + "https://www.formula1.com" + item2)

    await ctx.send('** -- Newest from F1.com -- **' + '\n\n' + data[0])


# Command for next race count down
@client.command()
async def nextrace(ctx):
    def dateDiffInSeconds(date1, date2):
        timedelta = date2 - date1
        return timedelta.days * 24 * 3600 + timedelta.seconds

    def daysHoursMinutesSecondsFromSeconds(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        return (days, hours, minutes, seconds)

    fp1_date = datetime.strptime('2021-05-20 10:30:00', '%Y-%m-%d %H:%M:%S')
    fp2_date = datetime.strptime('2021-05-20 14:00:00', '%Y-%m-%d %H:%M:%S')
    fp3_date = datetime.strptime('2021-05-22 11:00:00', '%Y-%m-%d %H:%M:%S')
    quali_date = datetime.strptime('2021-05-22 14:00:00', '%Y-%m-%d %H:%M:%S')
    race_date = datetime.strptime('2021-05-23 14:00:00', '%Y-%m-%d %H:%M:%S')
    now = datetime.now()

    embed = discord.Embed(
        title='',
        description=
        '**FP1 in - **\n' +
            str("%d days, %d hours %d minutes %d seconds" % daysHoursMinutesSecondsFromSeconds(
                dateDiffInSeconds(now, fp1_date))) + '\n\n'
        '**FP2 in - **\n' +
            str("%d days, %d hours %d minutes %d seconds" % daysHoursMinutesSecondsFromSeconds(
                dateDiffInSeconds(now, fp2_date))) + '\n\n'
        '**FP3 in - **\n' +
            str("%d days, %d hours %d minutes %d seconds" % daysHoursMinutesSecondsFromSeconds(
                dateDiffInSeconds(now, fp3_date))) + '\n\n' 
        '**Qualifying in - **\n' +
            str("%d days, %d hours %d minutes %d seconds" % daysHoursMinutesSecondsFromSeconds(
                dateDiffInSeconds(now, quali_date))) + '\n\n'                                              
        '**GP in **\n' +
            str("%d days, %d hours %d minutes %d seconds" % daysHoursMinutesSecondsFromSeconds(
                dateDiffInSeconds(now, race_date))),
        color=discord.Color.red()
    )

    embed.set_author(name=emoji.emojize(':calendar:') + ' ' + 'COUNTDOWN\nNext race info @ Monaco ')
    embed.set_thumbnail(url=random.choice(dr_morning + gr_night + cs_morning))

    await ctx.send(embed=embed)


# Command for random generating name
@client.command()
async def iam(ctx):
    def readtxt(filename):
        with open(filename) as f:
            lines = f.readlines()
            return lines

    adjtxt = readtxt(~/adjective.txt')
    advtxt = readtxt('~/adverb.txt')
    nountxt = readtxt('~/noun.txt')

    adj = [x.rstrip("\n") for x in adjtxt]
    adj = [x.capitalize() for x in adj]

    adv = [x.rstrip("\n") for x in advtxt]
    adv = [x.capitalize() for x in adv]

    noun = [x.rstrip("\n") for x in nountxt]
    noun = [x.capitalize() for x in noun]

    embed = discord.Embed(
        title='',
        description=random.choice(adj) + ' ' + random.choice(adv) + ' ' + random.choice(noun) + ' ' +
                    emoji.emojize(':smirk:'),
        color=discord.Color.lighter_gray()
    )

    embed.set_author(name='@' + str(ctx.author).split("#")[0] + ' You are...')

    await ctx.send(embed=embed)



# Help Command
# Add a help command to remind myself the shit I have
@client.command()
async def menu(ctx):
    embed = discord.Embed(
        title='Here is the command menu for this bot',
        description='',
        color=discord.Color.dark_grey()
    )

    embed.set_thumbnail(url='https://img.ruten.com.tw/s1/7/60/69/21908868290665_812.jpg')
    embed.set_author(name='COOKING MENU')
    embed.add_field(name='!chickensoup', value='Send you chicken soup message', inline=False)
    embed.add_field(name='!stoic', value='Send you stoicism quotes', inline=False)
    embed.add_field(name='!sonnet', value='AI generates Shakespeare sonnet', inline=False)
    embed.add_field(name='!f1news', value='Gives you the newest piece from F1.com', inline=False)
    embed.add_field(name='!nextrace', value='Count down till next race', inline=False)
    embed.add_field(name='!clear', value='Clear 10 messages in this channel', inline=True)
    embed.add_field(name='!clearobtmsg', value='Clear recent bot messages in this channel', inline=True)
    embed.add_field(name='!menu', value='Help menu', inline=True)
    embed.set_footer(text='-\nEnd of menu\nOff to play cooking mama ^_^')

    await ctx.send(embed=embed)

client.run(TOKEN)
