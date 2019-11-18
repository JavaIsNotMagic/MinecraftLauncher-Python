import discord,json,requests,os,sys

TOKEN = 'NjQ1NzQzNTI1MzQ2MDE3MzEw.XdH6Iw.kQBuo0njWbDqRCqAkpd4-5OIkgg'

def getGithubIssues():
    url = "https://api.github.com/repos/JavaIsNotMagic/MinecraftLauncher-Python/issues"
    msg = None
    r = requests.get(url)
    print(r.text)
    my_dict = json.loads(r.text)
    n = len(my_dict)
    x = 0
    if n == 0:
        msg = "No issues found!"
        return msg
    #end
    while x < n:
        msg = "Issue text: " + my_dict[x]['body']
        obj = my_dict[x]['labels']
        print(obj)
        return msg
        x += 1
    #end
#end

client = discord.Client()
supported_commands = ['help', 'issues list', 'hello', 'helpdesk stop', 'version']
help_message = "Supported Commands: " + str(supported_commands).strip(r'"').strip(',').strip('[').strip(']')
def ehelp():
    return help_message
#end
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    #end
    if message.content.startswith('hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('issues list'):
        msg = getGithubIssues()
        await client.send_message(message.channel, msg)
    elif message.content.startswith('helpdesk stop'):
        msg = "Stopping helpdesk bot.."
        await client.send_message(message.channel, msg)
        sys.exit(0) #Exit successfully
    elif message.content.startswith('help'):
        msg = ehelp()
        await client.send_message(message.channel, msg)
    elif message.content.startswith('version'):
        msg = "HelpdeskBot v0.0.0.1a"
        await client.send_message(message.channel, msg)
        #end
    #end
#end
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    welcome_message = "Helpdesk bot online"
    print(welcome_message)

client.run(TOKEN)
