# modules
import discord
import asyncio

from discord.ext import commands
from discord.ext.commands import *

# var
token = "token"
cid = "client_id"
owner = "owners_name"
oid = "ownersid"

# prefix and status setup
bot = commands.Bot(command_prefix='!',activity=discord.Activity(type=discord.ActivityType.watching, name="<this is a activity status>"))

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == bot.user:
        return
        
# when ready
@bot.event
async def on_ready():
    print(f'<message you want it to show in terminal when bot is ready to use>')
    
# help cmd
bot.remove_command('help')
    # above line removes the default crappy help command

@bot.command(aliases=['help'])
async def helplist(ctx):
    embed=discord.Embed(title="**<set a title for list>**", description="my prefix is: `!`", color=discord.Color.<choose a color e.g. blue>())
    # the above line sets the embed's heading title and shows prefix when use, also sets the embed's color
    embed.add_field(name='<catagory1>:', value="<command names>", inline=False)
    # you can copy the above line of code to add more fields (including catagory name and commands)
    embed.set_footer(text="<instructions or anything u want to set as footer>\n(Information requested by: {})".format(ctx.author.display_name))
    # the above line sets its footer, the {} shows who requested the help list as a format of user's nickname [e.g. whatever u set as server nickname], you can change it to (ctx.author) to show username and tags [e.g. Evancio#0001], you can change it to (ctx.author.name) to show ONLY username [e.g. Evancio]
    await ctx.send(embed=embed)
    # send the embed out
    
@bot.command()
async def echo(ctx):
    await ctx.send(f'Hello {ctx.author.name}!')
    # this command is !echo, it sends "Hello {username of the sender}!" when you use the command

# start
bot.run(token)
