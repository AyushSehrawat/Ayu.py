import discord

import discord_pass

from discord.ext import commands, tasks

from itertools import cycle

import joke_api

import random

import datetime

client = commands.Bot(command_prefix='!')
client.remove_command("help")
status = cycle(['Try !help', 'Try !server', 'Try !password', 'Try !ping', 'Try !server', 'Try !help', 'Try !pingme',
                'Try !help', 'Try !joke', 'Try !memcount', 'Try !help', 'Try !invite', 'Try !pingme', 'Try !server'])


@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready')
    channel = client.get_channel(id=Any of your channel id here)
    await channel.send(f'Hi! I am `online!`')


@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='Developers')
    await member.add_roles(role)
    welcome = client.get_channel(id=Any of your channel id here)
    embedvf = discord.Embed(title=f"Welcome to the Server", description=None, color=0xFF0000)
    embedvf.set_thumbnail(url=member.avatar_url)
    embedvf.add_field(name=f'{member.name}', value=f'{member.name} Joined the server!', inline=False)
    await welcome.send(embed=embedvf)


@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.command(aliases=['help'])
async def _help(ctx):
    embedvar = discord.Embed(title="All the bot commands", description=None, color=0x00ff00)
    embedvar.add_field(name="!ping", value="Tells the bot latency", inline=False)
    embedvar.add_field(name="!pingme", value="Pings you back", inline=False)
    embedvar.add_field(name="!hello", value="Returns Hello", inline=False)
    embedvar.add_field(name="!password", value="Generates a unique password", inline=False)
    embedvar.add_field(name="!8ball", value="Tell the chances of happening (write the question with it )", inline=False)
    embedvar.add_field(name="!joke", value="Returns a joke", inline=False)
    embedvar.add_field(name="!memcount", value="Returns the total members in the server", inline=False)
    embedvar.add_field(name="!invite", value="Creates a invite", inline=False)
    embedvar.add_field(name="!server", value="Returns information about the server", inline=False)
    await ctx.send(embed=embedvar)


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


@client.command()
async def server(ctx):
    roles = [role.name for role in ctx.guild.roles]
    roles.remove('@everyone')
    roles.remove('Python')  # My bot name is python
    embedva = discord.Embed(title="Info About The Server", description=None, color=0x00FFFF)
    embedva.add_field(name="Server Name", value=f"{ctx.guild}", inline=False)
    embedva.add_field(name="Region", value=f"{ctx.guild.region}", inline=False)
    embedva.add_field(name="Created", value=f"{ctx.guild.created_at.strftime('%A, %B %d %Y @ %H:%M:%S %p')}",
                      inline=False)
    embedva.add_field(name="Owner", value=f"{ctx.guild.owner}", inline=False)
    embedva.add_field(name="Channels", value=f"There are {len(ctx.guild.channels)} channels", inline=False)
    embedva.add_field(name="Text Channels", value=f"There are {len(ctx.guild.text_channels)} text-channels",
                      inline=False)
    embedva.add_field(name="Voice Channels", value=f"There are {len(ctx.guild.voice_channels)} voice-channels",
                      inline=False)
    embedva.add_field(name="Verification level", value=f"{ctx.guild.verification_level}", inline=False)
    embedva.add_field(name="Total Roles", value=f"There are {len(ctx.guild.roles)} roles", inline=False)
    embedva.add_field(name="Roles", value=f"{'  |  '.join(roles)}", inline=False)
    embedva.add_field(name="Server ID", value=f"{ctx.guild.id}", inline=False)
    await ctx.send(embed=embedva)


@client.command(aliases=['user'])
async def _user(ctx, member: discord.Member):
    roles = [role.name for role in member.roles[1:]]
    embedv = discord.Embed(title=f"Info About {member.name}", description=None, color=0x00FF00)
    embedv.set_thumbnail(url=member.avatar_url)
    embedv.add_field(name="Joined: ", value=f"{member.joined_at.strftime('%A, %B %d %Y @ %H:%M:%S %p')}", inline=False)
    embedv.add_field(name="Created: ", value=f"{member.created_at.strftime('%A, %B %d %Y @ %H:%M:%S %p')}",
                     inline=False)
    embedv.add_field(name="Total Roles", value=f"{len(member.roles)}", inline=False)
    embedv.add_field(name="Roles", value=f"{' | '.join(roles)}", inline=False)
    embedv.add_field(name='ID', value=f"{member.id}", inline=False)
    await ctx.send(embed=embedv)


client.run('Your token')
