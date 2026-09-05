import os
import threading
from flask import Flask
import discord
from discord import app_commands

# =========================
# SERVIDOR WEB PARA O RENDER
# =========================

app = Flask(__name__)

@app.route("/")
def home():
    return "🥊 UFCCord está online!"

def iniciar_servidor():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

threading.Thread(target=iniciar_servidor, daemon=True).start()

# =========================
# BOT DO DISCORD
# =========================

class UFCCord(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
        print("✅ Comandos sincronizados!")

bot = UFCCord()


@bot.event
async def on_ready():
    print(f"🥊 UFCCord conectado como {bot.user}")


# =========================
# /ufc
# =========================

@bot.tree.command(name="ufc", description="Mostra informações do UFCCord")
async def ufc(interaction: discord.Interaction):

    embed = discord.Embed(
        title="🥊 UFCCord",
        description="Seu bot de UFC está funcionando!",
    )

    embed.add_field(
        name="👊 Comandos",
        value="`/lutador` • `/campeoes` • `/ufc`",
        inline=False
    )

    await interaction.response.send_message(embed=embed)


# =========================
# /lutador
# =========================

@bot.tree.command(name="lutador", description="Mostra informações de um lutador")
@app_commands.describe(nome="Nome do lutador")
async def lutador(interaction: discord.Interaction, nome: str):

    lutadores = {
        "jon jones": {
            "categoria": "Peso-pesado",
            "cartel": "28-1-0",
            "estilo": "Wrestling / MMA"
        },
        "alex pereira": {
            "categoria": "Meio-pesado",
            "cartel
