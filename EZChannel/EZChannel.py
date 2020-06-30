import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'ez-')



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.Game('ez-info'))


@client.command()
async def info(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
    

    
    

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
 
      

@client.command()
async def purge(ctx, amount=500000000000000000000000000000000000000000000000):
    await ctx.channel.purge(limit=amount)




#region    
# @client.command(aliases=['8ball'])
# async def _8ball(ctx, *, question):
#    responses = []
#endregion

client.run('NzI2NTMwOTcwNDU0NTg5NDcx.Xvex2A.JtXdTNKylGCZpkNeKZcqq320pBM')
