#İmport
import discord
from discord.ext import commands
from discord import app_commands
import os
import aiohttp



bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=discord.Intents.all())

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

#region events
#Hazır komutu
@bot.event
async def on_ready():
    print("ready")

#Sunucuya katılanlar
@bot.event
async def on_member_join(member:discord.Member):
    channel = discord.utils.get(member.guild.text_channels, name="Hoşgeldin mesajı yazılmasını istediğiniz kanal")
    await channel.send(f"{member} Hoşgeldin")
    print(f"{member.mention} Hoşgeldin")


#Sunucudan ayrılanlar
@bot.event
async def on_member_remove(member:discord.Member):
    channel = discord.utils.get(member.guild.text_channels, name="Ayrıldı mesajı yazılmasını istediğiniz kanal")
    await  channel.send(f"{member} Ayrıldı")
    print(f"{member.mention} Ayrıldı")

#Link atılmasını engelleme
@bot.event
async def on_message(message):
    if 'https://' in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} Link atma." )
    else:
        await bot.process_commands(message)

#endregion

#region commands

#İnformation
@bot.command()
async def info(ctx):
    Vemembed = discord.Embed(title="info_title", description='açıklama', color=discord.Color.random(), url='url')
    Vemembed.set_author(name="yapımcı ismi", url='url', icon_url='icon url')
    Vemembed.add_field(name='name', value='value')
    Vemembed.add_field(name='Version', value='value')
    Vemembed.set_image(url='imageurl')
    Vemembed.set_footer(text="footer")
    await ctx.send(embed=Vemembed)

#Random Köpek
@bot.command()
async def köpek(ctx):
   async with aiohttp.ClientSession() as session:
      request3 = await session.get('https://some-random-api.ml/img/dog')
      dogjson = await request3.json()

      request4 = await session.get('https://some-random-api.ml/facts/dog')
      factjson = await request4.json()

   embed = discord.Embed(title="Köpek!", color=discord.Color.random())
   embed.set_image(url=dogjson['link'])
   embed.set_footer(text=factjson['fact'])
   await ctx.send(embed=embed)


#Random Kedi
@bot.command()
async def kedi(ctx):
   async with aiohttp.ClientSession() as session:
      request3 = await session.get('https://some-random-api.ml/img/cat')
      catjson = await request3.json()

      request4 = await session.get('https://some-random-api.ml/facts/cat')
      factjson = await request4.json()

   embed = discord.Embed(title="Kedi!", color=discord.Color.random())
   embed.set_image(url=catjson['link'])
   embed.set_footer(text=factjson['fact'])
   await ctx.send(embed=embed)


#Random Kuş
@bot.command()
async def kuş(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/bird')
      birdjson = await request.json()

      request2 = await session.get('https://some-random-api.ml/facts/bird')
      factjson = await request2.json()

   embed = discord.Embed(title="Kuş!", color=discord.Color.random())
   embed.set_image(url=birdjson['link'])
   embed.set_footer(text=factjson['fact'])
   await ctx.send(embed=embed)

#Random Panda
@bot.command()
async def panda(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/panda')
      pandajson = await request.json()

      request2 = await session.get('https://some-random-api.ml/facts/panda')
      factjson = await request2.json()

   embed = discord.Embed(title="Panda!", color=discord.Color.random())
   embed.set_image(url=pandajson['link'])
   embed.set_footer(text=factjson['fact'])
   await ctx.send(embed=embed)


#Fotoğraf ve Spotify linki
@bot.command()
async def a(ctx):
    await ctx.send("asdfg", file=discord.File(".png"))
    await ctx.send("https://open.spotify.com/")


#Test
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

#Selam
@bot.command(name='selam', description="nt")
async def command(ctx):
    await ctx.reply(f"Selam {ctx.author.name}")

#Ping
@bot.command()
async def ping(ctx):
    await ctx.reply(f"Pong!!! {round(bot.latency * 1000)}ms!!")

#İnvite
@bot.command()
async def on_invite_command(invite):
    channel = bot.get_channel(1061690186657964075)
    embed = discord.Embed(title="İnvite",description=f"Oluşturan: {invite.inviter}")

#kick
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member, *, reason=None):
    if reason == None:
        reason="nt"
    await ctx.guild.kick(member)
    await ctx.send(f"{member.mention} {reason}dan dolayı banlandı.")







#endregion

#Bot run
bot.run('TOKEN')
