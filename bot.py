import os
import discord
from discord import app_commands

class UFCCord(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

bot = UFCCord()


@bot.event
async def on_ready():
    print(f"🥊 UFCCord online como {bot.user}")


@bot.tree.command(name="ufc", description="Mostra o UFCCord")
async def ufc(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🥊 **UFCCord** está online!\nUse `/lutador` para consultar um lutador."
    )


@bot.tree.command(name="lutador", description="Consulta um lutador")
@app_commands.describe(nome="Nome do lutador")
async def lutador(interaction: discord.Interaction, nome: str):

    lutadores = {
        "jon jones": "🥊 Jon Jones\n🏆 Peso-pesado\n📊 Cartel: 28-1-0",
        "alex pereira": "🥊 Alex Pereira\n🏆 Meio-pesado\n📊 Cartel: 13-3-0",
        "islam makhachev": "🥊 Islam Makhachev\n🏆 Meio-médio\n📊 Cartel: 28-1-0"
    }

    resultado = lutadores.get(nome.lower())

    if resultado:
        await interaction.response.send_message(resultado)
    else:
        await interaction.response.send_message(
            f"❌ Não encontrei **{nome}**."
        )


@bot.tree.command(name="campeoes", description="Mostra os campeões")
async def campeoes(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🏆 **CAMPEÕES UFC**\n\n"
        "🥊 Peso-pesado — A definir\n"
        "⚡ Meio-pesado — A definir\n"
        "🔥 Meio-médio — A definir\n"
        "🥋 Leve — A definir"
    )


TOKEN = os.environ.get("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN não foi configurado no Render.")

bot.run(TOKEN)
