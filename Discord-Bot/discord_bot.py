import discord
import joke_api
# Find the joke-api file attached

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hello'):
        await message.channel.send("Hello")

    if message.content.startswith('$help'):
        await message.channel.send('Following are the commands\n$hello\n$joke')

    if message.content.startswith('mental'):
        await message.channel.send('Any kind of abuse is not allowed')

    if message.content.startswith('$joke'):
        joke = joke_api.get_joke()
        print(joke)

        if not joke:
            await message.channel.send("Couldn't get joke from API. Try again later.")
        else:
            await message.channel.send(joke['setup'] + '\n' + joke['punchline'])


client.run('Your bot token here!')

