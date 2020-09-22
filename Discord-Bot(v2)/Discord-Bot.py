import discord

import discord_pass

from discord.ext import commands, tasks

from itertools import cycle

import joke_api

import random

client = commands.Bot(command_prefix='!')
client.remove_command("help")
status = cycle(['Try !commandinfo', 'Try !password', 'Try !ping', 'Try commandinfo', 'Try !pingme',
                'Try !commandinfo', 'Try !joke', 'Try !memcount', 'Try !commandinfo', 'Try !invite', 'Try !pingme'])


@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready')
    channel = client.get_channel(id= #your channel id)
    await channel.send(f'Hi! I am `online!`')


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.command()
async def commandinfo(ctx):
    await ctx.send(f'{ctx.author.mention} Here are the commands - '
                   f'\n `!pingme` - Pings you'
                   f'\n `!hello` - Says you hello'
                   f'\n `!password` - Generates a unique password for you'
                   f'\n `!ping` - Returns Pong'
                   f'\n `!joke` - Returns you a joke'
                   f"\n `!8ball` - You should enter a question after it, and it will tell it's chances of happening"
                   f"\n `!memcount` - Total members in the server"
                   f"\n `!invite` - creates a instant invite")


@client.command()
async def pingme(ctx):
    await ctx.send(f'{ctx.author.mention}')


@client.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}')


@client.command()
async def password(ctx):
    passwor = discord_pass.secure_password_gen()
    await ctx.send(f'{ctx.author.mention} Check your dm for the password! ')
    await ctx.author.send(f'You password is \n `{passwor}`')


@client.command()
async def ping(ctx):
    await ctx.send(f'{ctx.author.mention} Pong {round(client.latency * 1000)}ms')


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain',
                 'It is decidedly so',
                 'Without a doubt',
                 'Yes, definitely',
                 'You may rely on it',
                 'As i see it, yes',
                 'Most likely',
                 'Outlook good',
                 'Yes',
                 'Signs point to yes',
                 'Reply haze, try again',
                 'Ask again later',
                 'Better now tell you now',
                 'Cannot predict now',
                 'Concentrate and ask again',
                 'Do not count on it',
                 'My reply is no',
                 'My sources say now',
                 'Outlook not so good',
                 'Very doubtful']
    await ctx.send(f'{ctx.author.mention}\n Question: {question} \n Answer: {random.choice(responses)}')


@client.command()
async def joke(ctx):
    jokes = joke_api.get_joke()
    if not jokes:
        await ctx.channel.send("Couldn't get joke from API. Try again later.")
    else:
        await ctx.channel.send(jokes['setup'] + '\n' + jokes['punchline'])


@client.command()
@commands.has_any_role('Owner', 'Moderators')
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')


@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')


@client.command()
@commands.has_any_role('Owner', 'Moderators')
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


@client.command()
async def memcount(ctx):
    await ctx.send(f'There are: {ctx.guild.member_count} members in the server')


@client.command()
async def invite(ctx):
    inv = str(await ctx.channel.create_invite(unique=False))
    await ctx.send(inv)


client.run('Your token')
