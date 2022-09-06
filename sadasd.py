import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import random
import time

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="*", intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio("C:\\Users\\aknez\\Desktop\\ben.mp3")
        player = voice.play(source)

@client.command()
async def fuckoff(ctx):
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('C:\\Users\\aknez\\Desktop\\phone-drop-2.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)
    time.sleep(1)
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()

@client.command()
async def adampiska(ctx):
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('C:\\Users\\aknez\\Desktop\\whistle-tune.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

@client.command()
async def q(ctx):
    yesno = random.randint(1, 2)
    if yesno == 1:
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('C:\\Users\\aknez\\Desktop\\yes.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)
    if yesno == 2:
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('C:\\Users\\aknez\\Desktop\\no.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

@client.command()
async def brh(ctx):
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('C:\\Users\\aknez\\Desktop\\burp-11.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

@client.command()
async def commands(ctx):
    await ctx.send(":fireworks:__**List of Commands**__:fireworks:\n"
":telephone:**join**: Ben joins a voice channel\n"
":no_entry_sign:**fuckoff**: Ben leaves a voice channel\n"                  
":question:**q**: Ask Ben a question\n"                   
":kissing:**adampiska**: Ben wistles\n"                                   
":face_vomiting:**brh**: Ben burps\n"
"_All commands start with a_ *\n")





client.run("MTAxNDk4NTQ0OTE5MTc2ODI1Ng.GS3HV3.LXMPQPNilBrP7A-zX1dQ3bglijsRsc_R2o0ZG4")