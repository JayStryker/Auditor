import discord
from discord.ext import commands

TOKEN = 'NTIyNTc3NjY2Mjg1NTAyNDg0.DvNAZA.qqTVZxaJwvIcORzzK4OC0D1DuOg'

client = commands.Bot(command_prefix = 'a!')
client.remove_command('help')

players = {}

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Music on discord | version 1.0.1'))
    print('Bot Online')

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='Auditor Commands')
    embed.add_field(name='Music Commands', value='a!play <song url> a!stop <stops song a!pause <pauses song a!resume <resumes song> a!join <joins voice channel> a!leave <leaves voice channel', inline=False)

    await client.send_message(author, embed=embed)
    await client.say('Check your dms')

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
	embed = discord.Embed(
		title = "Succsess!",
		description = "Connected to the Voice Channel.",
		colour = discord.colour.green()
	)
	await client.send_message(ctx.message.channel, embed=embed)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
	if voice_client is None:
		embed = discord.Embed(
			title = "Succsess!",
			description = "Disconnected from the Voice Channel.",
			colour = discord.colour.green()
		)
		await client.send_message(ctx.message.channel, embed=embed)
    await voice_client.disconnect()
	embed = discord.Embed(
		title = "Succsess!",
		description = "Disconnected from the Voice Channel.",
		colour = discord.colour.green()
	)
	await client.send_message(ctx.message.channel, embed=embed)

@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()
	embed = discord.Embed(
		title = "Now Playing...",
		description = "Playing " + url + ".",
		colour = discord.colour.green()
	)
	await client.send_message(ctx.message.channel, embed=embed)


@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()
	embed = discord.Embed(
		title = "Stopping!",
		description = "Stopping the music.",
		colour = discord.colour.green()
	)
	await client.send_message(ctx.message.channel, embed=embed)

@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()
	embed = discord.Embed(
		title = "Resuming!",
		description = "Resuming the music.",
		colour = discord.colour.green()
	)
	await client.send_message(ctx.message.channel, embed=embed)

@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()
	embed = discord.Embed(
		title = "Pasuing!",
		description = "Pasuing the music.",
		colour = discord.colour.green()
	)
	await client.send_message(ctx.message.channel, embed=embed)

client.run(TOKEN)


