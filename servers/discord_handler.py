import discord

client = discord.Client()

discord_key = "ODMwMjYwMTM4NTMwMzA4MDk2.YHEGAg._5nbD-p3Tkck23zm6E2PqD5Aovs"

    

def discord_chat(client, key, cb, fun, verbose):
    @client.event
    async def on_ready():
        print("i am on discord masta!")

    @client.event
    async def on_message(message):
        if(message.author == client.user):
            return
        else:
            try:
                response, quit = fun(cb, message.content)
                if(verbose):
                    print("Me:{}\nYosho:{}".format(message.content, response))
                if(quit):
                    await message.channel.send(response)
                    raise a
                await message.channel.send(response)
            except NameError:
                import sys

                sys.exit(0)
    
    client.run(key)

