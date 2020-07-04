import discord
import urllib.parse
import random
from datetime import datetime
from discord.ext import commands
############################################Case_insensitive MASSIVELY REDUCES PERFORMANCE ||| line 5
client = commands.Bot(command_prefix = 'ez-', case_insensitive=True)
modeenabled = 0


f=open("Files/Bot_key.txt", "r")
if f.mode == 'r':
    key =f.read()
    print(key)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.Game('ez-help')) #Set status
    now = datetime.now().time() # time object
    print("now =", now,)

@client.command()
async def breakfast(ctx):
    """Shows you what to eat for breakfast"""
    eat = ['waffels','panckakes','avacado toast', 'eggs','cereal','yogurt','Oatmeal/Poridge','berries']
    await ctx.send ('Eat some'); await ctx.send ({random.choice(eat)})

@client.command()
async def search(ctx, *, searchquery: str):
    '''Google anything. (Big thanks to the GitHub user AlexApps99 for this awesome and funny script!)'''
    
    await ctx.send('<https://lmgtfy.com/?iie=1&q={}>'
                   .format(urllib.parse.quote_plus(searchquery)))

@client.command()
async def devmode(ctx):
    """Enables Dev Mode"""
    global modeenabled
    if (modeenabled == 0):
        modeenabled = 1
        await ctx.send('Dev Mode On')
    else:
        modeenabled = 0
        await ctx.send('Dev Mode Off')

@client.command()
async def consoleping(ctx):
       
    """Pings developer console"""
    global modeenabled
    if (modeenabled == 1):
        print (f'Pong! {round(client.latency * 1000)}ms')
        await ctx.send ('Console Pinged')
    else:
        await ctx.send ('Enable Dev Mode with ez-devmode')

@client.command()
async def fortniteroulette(ctx):
    """Gives a random drop spot and weapon"""
    location = ['PLEASENT_PARK','STEAMY_STACKS','SWEATY_SANDS','SALTY_SPRINGS','THE_AUTHORITY','FRENZY_FARM','HOLLY_HEDGES','LAZY_LAKE','RETAIL_ROW','THE_YACHT','THE_FORTILLA','RICKETY_RIG','MISTY_MEADOWS','CATTY_CORNER','A_RANDOM_HOUSE_IN_THE_MIDDLE_OF_NOWHERE']
    weapon = ['AR','SHOTGUN','SMG','SNIPER','HARPOON','PISTOL','Pickaxe_Only']
    await ctx.send('Land at '); await ctx.send ({random.choice(location)})
    await ctx.send('\nYou can only use '); await ctx.send({random.choice(weapon)})

@client.command()
async def pi(ctx):
    """Shows pi in 17 digits. because why not?"""
    await ctx.send(3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827785771342757789609173637178721468440901224953430146549585371050792279689258923542019956112129021960864034418159813629774771309960518707211349999998372978049951059731732816096318595024459455346908302642522308253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863882353787593751957781857780532171226806613001927876611195909216420198938095257201065485863278865936153381827968230301952035301852968995773622599413891249721775283479131515574857242454150695950829533116861727855889075098381754637464939319255060400927701671139009848824012858361603563707660104710181942955596198946767837449448255379774726847104047534646208046684259069491293313677028989152104752162056966024058038150193511253382430035587640247496473263914199272604269922796782354781636009341721641219924586315030286182974555706749838505494588586926995690927210797509302955321165344987202755960236480665499119881834797753566369807426542527862551818417574672890977772793800081647060016145249192173217214772350141441973568548161361157352552133475741849468438523323907394143334547762416862518983569485562099219222184272550254256887671790494601653466804988627232791786085784383827967976681454100953883786360950680064225125205117392984896084128488626945604241965285022210661186306744278622039194945047123713786960956364371917287467764657573962413890865832645995813390478027590)

@client.command()
async def roulette(ctx):
    """Good ol' Russian Roulette"""
    outcomes=['Death','Coma','Lost Limbs','Winner']
    await ctx.send({random.choice(outcomes)})
           
@client.command()
async def ping(ctx):
    """Shows latency in Miliseconds"""
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def rockpaperscissors(ctx, message):
    """Plays rock paper scissors"""
    async def on_message(message):
        
        rps = ['Rock','Paper','Scissors']
        await ctx.send ('please choose: rock, paper, or scissors (lower case please)')
        if message.content.startswith('rock'):
            userinput = ('rock')
        elif message.content.startswith('paper'):
            userinput = ('paper')
        elif message.content.startswith('scissors'):
            userinput - ('scissors')
        else:
            await ctx.send ('That is not a valid option. (Are you trying to Dynamite me???)')
    global rps
    global userinput
    random.choice(rps)
    print (rps) 
    if userinput is rps:
        ctx.send ('We chose the same')
    elif rps == ('Rock') and userinput == ('paper'):
        await ctx.send ('You beat me. I played Rock')
    elif rps == ('Rock') and userinput == ('scissors'):
        await ctx.send ('I beat you. I played Rock')
    elif rps == ('Paper') and userinput == ('rock'):
        await ctx.send ('I beat you. I played Paper')
    elif rps == ('Paper') and userinput == ('scissors'):
        await ctx.send ('You beat me. I played Paper')
    elif rps == ('Scissors') and userinput == ('rock'):
        await ctx.send ('You beat me. I played Scissors')
    elif rps == ('Scissors') and userinput == ('paper'):
        await ctx.send ('I beat you. I played Scissors')
    else:
        await ctx.send ('Uh oh. that was not supposed to happen. Please let Kelton the Conqueror know ASAP. \nSorry for the inconvenience')




    
 
@client.command()
async def purge(ctx, amount=500000000000000000000000000000000000000000000000):
    """Purges channel of messages. examples|| ez-purge, ez-purge 5"""
    await ctx.channel.purge(limit=amount)


#Examples
#region    
# @client.command(aliases=['8ball'])
# async def _8ball(ctx, *, question):
#    responses = []
#endregion 


client.run(key)
