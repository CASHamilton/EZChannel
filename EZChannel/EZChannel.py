import discord
import urllib.parse
import random
from datetime import datetime
from discord.ext import commands
############################################Case_insensitive MASSIVELY REDUCES PERFORMANCE ||| line 5
client = commands.Bot(command_prefix = 'ez-', case_insensitive=True)
modeenabled = 0
textts = False

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

@client.event
async def on_guild_join(guild): #Thanks to the GitHub user 0xicl33n for this code!
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('Hey there! For a list of commands please type ez-help. \nPlease remember that this bot is a work in progress and some commands may not work properly yet! \nTo enable Text-to-Speech mode type ez-tts')
        break 


@client.command()
async def Register(ctx):
    author = ctx.message.author
    print (author)

    registry= open('author', "w+")#I TXT FILE IS IN NORMAL AREA FIX ASAP.
    registry.write('Test')
    registry.close()




@client.command()
async def code(ctx):
    """Shows a Github link to code"""
    
    global textts
    if textts == True:
        await ctx.send('I am coded by Kelton the Conqueror. Here is his GitHub!', tts=True)
        await ctx.send ('https://github.com/KeltontheConqueror/')
    else:   
        await ctx.send('I am coded by Kelton the Conqueror. Here is his GitHub!')
        await ctx.send ('https://github.com/KeltontheConqueror/')

@client.command() 
async def tts(ctx):
    """Makes bot respond with text-to-speech messages"""
    print ("TTS On")
    global textts
    if textts == False:
        textts = True
        await ctx.send('TTS mode enabled')
    elif textts == True:
        textts = False
        await ctx.send('TTS mode disabled')
    else:
         await ctx.send('Error code 1 see (readme for details)')
    
@client.command()
async def breakfast(ctx):
    """Shows you what to eat for breakfast"""
    eat = ['Waffels','Panckakes','Toast', 'Eggs','Cereal','Yogurt','Oatmeal/Poridge',]
    await ctx.send ('Eat some'); await ctx.send (random.choice(eat))

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

    location = ['Pleasent_Park','Steamy_Stacks','Sweaty_Sands','Salty_Springs','The_Authority','Frenzy_Farm','Holly_Hedges','Lazy_Lake','Retail_Row','The_Yacht','The_Fortilla','Rickety_Rig','Misty_Meadows','Catty_Corner','A_Random_House_In_The_Middle_Of_Nowhere']
    weapon = ['AR','Shotgun','SMG','Sniper','Harpoon','Pistol','Pickaxe_Only']
    await ctx.send('Land at '); await ctx.send (random.choice(location))
    await ctx.send('\nYou can only use '); await ctx.send(random.choice(weapon))

@client.command()
async def pi(ctx):
    """Shows pi in 17 digits. because why not?"""
    await ctx.send(3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827785771342757789609173637178721468440901224953430146549585371050792279689258923542019956112129021960864034418159813629774771309960518707211349999998372978049951059731732816096318595024459455346908302642522308253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863882353787593751957781857780532171226806613001927876611195909216420198938095257201065485863278865936153381827968230301952035301852968995773622599413891249721775283479131515574857242454150695950829533116861727855889075098381754637464939319255060400927701671139009848824012858361603563707660104710181942955596198946767837449448255379774726847104047534646208046684259069491293313677028989152104752162056966024058038150193511253382430035587640247496473263914199272604269922796782354781636009341721641219924586315030286182974555706749838505494588586926995690927210797509302955321165344987202755960236480665499119881834797753566369807426542527862551818417574672890977772793800081647060016145249192173217214772350141441973568548161361157352552133475741849468438523323907394143334547762416862518983569485562099219222184272550254256887671790494601653466804988627232791786085784383827967976681454100953883786360950680064225125205117392984896084128488626945604241965285022210661186306744278622039194945047123713786960956364371917287467764657573962413890865832645995813390478027590)

@client.command()
async def roulette(ctx):
    """Good ol' Russian Roulette"""
    outcomes=['Death','Coma','Lost Limbs','Winner']
    await ctx.send(random.choice(outcomes))
           
@client.command()
async def ping(ctx):
    """Shows latency in Miliseconds"""
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')  
    

   

    
 
@client.command()
async def purge(ctx, amount=500000000000000000000000000000000000000000000000):
    """Purges channel of messages. examples|| ez-purge, ez-purge 5"""
    global textts
    await ctx.channel.purge(limit=amount)
    if textts == False:
        await ctx.send ('Channel purged. (use the command ez-tts to turn on voice notifications for this event)')
    elif textts == True:
        await ctx.send ('Channel purged.',tts=True)
    else:
        await ctx.send ('Error code 2 (See readme for details)')


#Examples
#region    
# @client.command(aliases=['8ball'])
# async def _8ball(ctx, *, question):
#    responses = []
#endregion 


client.run(key)
