import discord
from discord.ext import commands
x = 1
client = commands.Bot(command_prefix = 'ez-')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
    while (x < 1000):
        await ctx.send('test')
        x+1

@client.command()
async def purge(ctx, amount=500000000000000000000000000000000000000000000000):
    await ctx.channel.purge(limit=amount)




#region    
# @client.command(aliases=['8ball'])
# async def _8ball(ctx, *, question):
#    responses = []
#endregion

client.run('NzI2NTMwOTcwNDU0NTg5NDcx.Xvex2A.JtXdTNKylGCZpkNeKZcqq320pBM')
