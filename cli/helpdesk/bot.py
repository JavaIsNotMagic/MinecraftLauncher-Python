import discord,json,requests,os

TOKEN = 'NjQ1NzQzNTI1MzQ2MDE3MzEw.XdHBzg.IXVv_oeKTtaLfel6aIPArePAxUs'

def getGithubIssues():
    url = "https://api.github.com/repos/JavaIsNotMagic/MinecraftLauncher-Python/issues"
    msg = None
    r = requests.get(url)
    my_dict = json.loads(r.text)
    n = len(my_dict)
    x = 0
    if n == 0:
        msg = "No issues found!"
        return msg
    #end
    while x < n:
        msg = "Issue no. " + str(x) + " Issue text: " + my_dict[x]['body']
        return msg
        x += 1
    #end
#end

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    #end
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    #end
    if message.content.startswith('!issues list'):
        msg = getGithubIssues()
        await client.send_message(message.channel, msg)
    #end
    if message.content.startswith('!help'):
        msg = "!hello - Test command. Mentions you in chat. !issues list - List all the issues foud on github."
        await client.send_message(message.channel, msg)
    #end
    if message.content.startswith('!helpdesk stop')
        msg = "Helpdesk going offline."
        await client.send_message(message.channel, msg)
        sys.exit(0)
    #end
#end
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
