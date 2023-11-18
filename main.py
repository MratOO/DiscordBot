import random
import settings
import discord
from discord.ext import commands


def run():
    intents = discord.Intents.all()

    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        '''запуск бота'''
        print(bot.user)
        print(bot.user.id)
        print('Bot ready to work my Master')

    @bot.command(
        aliases=['p'],
        help='This is help',
        description='Disc',
        brief='brr',
        enabled=False
    )
    async def ping(ctx):
        ''' Check '''
        await ctx.send('pong blya')

    @bot.command()
    async def say(ctx, what='What?'):
        """Потворяет одно слово"""
        await ctx.send(what)

    @bot.command()
    async def say2(ctx, *what):
        '''Полностью повторяет все слова'''
        await ctx.send(' '.join(what))

    @bot.command()
    async def say3(ctx, what='What?', why='Why?'):
        """Складывает слова"""
        await ctx.send(what + why)

    @bot.command()
    async def choices(ctx, *options):
        '''random choices'''
        await ctx.send(random.choice(options))

    @bot.command()
    async def add(ctx, one, two):
        await ctx.send(one + two)

    bot.run(settings.DISCORD_API_SECRET)


if __name__ == '__main__':
    run()
