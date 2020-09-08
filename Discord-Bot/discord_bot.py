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

    if message.content.startswith('$joke'):
        joke = joke_api.get_joke()
        print(joke)

        if not joke:
            await message.channel.send("Couldn't get joke from API. Try again later.")
        else:
            await message.channel.send(joke['setup'] + '\n' + joke['punchline'])


client.run('Your bot token here!')


# Instructions-
# Sign in or register to discord server!
# Then create a guild/server
# Then go to https://discord.com/developers/applications
# Create a new application here with the name of your bot as the application!
# Then you can also add a profile picture to your bot there!
# Then go to OAuth2 tab in the portal and check bot button under the scope
# A new tab will open! There give bot admin permissions
# A link will be generated and then add it to your discord server or guild
# Now the bot will be offline, to activate it do the following-
# Go to bot tab in discord dev portal! Then find reveal token button. Click on it and it will reveal a token. Copy it and paste it in [client.run('Your bot token here!')].
# Then open cmd and run discord file.
# Boom! It will start your bot! Now you can edit the code accroding to you!
