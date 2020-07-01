import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = 'ez-')



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.Game('ez-help'))


@client.command()
async def fortniteroulette(ctx):
    """Gives a random drop spot and weapon"""
    location = ['PLEASENT_PARK','STEAMY_STACKS','SWEATY_SANDS','SALTY_SPRINGS','THE_AUTHORITY','FRENZY_FARM','HOLLY_HEDGES','LAZY_LAKE','RETAIL_ROW','THE_YACHT','THE_FORTILLA','RICKETY_RIG','MISTY_MEADOWS','CATTY_CORNER','A_RANDOM_HOUSE_IN_THE_MIDDLE_OF_NOWHERE']
    weapon = ['AR','SHOTGUN','SMG','SNIPER','HARPOON','PISTOL']
    await ctx.send('Land at '); await ctx.send ({random.choice(location)})
    await ctx.send('\nYou can only use '); await ctx.send({random.choice(weapon)})

    

    
    

@client.command()
async def ping(ctx):
    """Shows latency in Miliseconds"""
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
 
      

@client.command()
async def purge(ctx, amount=500000000000000000000000000000000000000000000000):
    """Purges channel of messages. examples|| ez-purge, ez-purge 5"""
    await ctx.channel.purge(limit=amount)




#region    
# @client.command(aliases=['8ball'])
# async def _8ball(ctx, *, question):
#    responses = []
#endregion

client.run('NzI2NTMwOTcwNDU0NTg5NDcx.Xvex2A.JtXdTNKylGCZpkNeKZcqq320pBM')
