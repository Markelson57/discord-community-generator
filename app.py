import discord
from discord.ext import commands
import json

# ======================
# CONFIGURACIÓN
# ======================

TOKEN = "TU_TOKEN_AQUI"  # ⚠️ Reemplaza con tu token real
GUILD_ID = 123456789012345678  # ⚠️ Reemplaza con el ID de tu servidor
JSON_FILE = "plantilla_publica.json"

# ======================
# INTENTS
# ======================

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ======================
# FUNCIÓN PARA PERMISOS
# ======================

def build_overwrites(guild, allowed_roles):
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(view_channel=False)
    }

    staff_roles = ["Fundador", "Administrador", "Moderador"]

    for role in guild.roles:
        if role.name in staff_roles or role.name in allowed_roles:
            overwrites[role] = discord.PermissionOverwrite(
                view_channel=True,
                read_messages=True,
                connect=True,
                speak=True
            )

    return overwrites

# ======================
# EVENTO READY
# ======================

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")

    guild = bot.get_guild(GUILD_ID)
    if not guild:
        print(f"❌ Servidor no encontrado con ID {GUILD_ID}.")
        await bot.close()
        return

    # Verificar permisos del bot
    bot_member = guild.me
    if not bot_member.guild_permissions.administrator:
        print("❌ El bot necesita permisos de administrador.")
        await bot.close()
        return

    # ======================
    # LEER JSON
    # ======================

    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            template = json.load(f)
    except Exception as e:
        print(f"❌ Error al leer el archivo {JSON_FILE}: {e}")
        await bot.close()
        return

    # ======================
    # CREAR ROLES
    # ======================

    print("🎭 Creando roles (pueden estar vacíos)...")
    for role_data in template.get("roles", []):
        try:
            role_name = role_data.get("role_name", "Rol Vacío")
            perms = discord.Permissions.none()
            if role_data.get("permissions") == "Administrador":
                perms = discord.Permissions(administrator=True)

            role = await guild.create_role(
                name=role_name,
                color=discord.Color(int(role_data.get("color", "#808080")[1:], 16)),
                permissions=perms
            )
            print(f"  - Rol '{role.name}' creado.")
        except Exception as e:
            print(f"  - Error al crear rol: {e}")

    # ======================
    # CREAR CATEGORÍAS Y CANALES
    # ======================

    print("📁 Creando categorías y canales (pueden estar vacíos)...")
    for category_data in template.get("categories", []):
        try:
            category_name = category_data.get("category_name", "Categoría Vacía")
            if "allowed_roles" in category_data and category_data["allowed_roles"]:
                overwrites = build_overwrites(guild, category_data["allowed_roles"])
                category = await guild.create_category(category_name, overwrites=overwrites)
            else:
                category = await guild.create_category(category_name)

            print(f"  - Categoría '{category.name}' creada.")

            for channel_data in category_data.get("channels", []):
                try:
                    channel_name = channel_data.get("channel_name", "Canal Vacío")
                    channel_type = channel_data.get("channel_type", "text")
                    if channel_type.lower() == "text":
                        channel = await category.create_text_channel(channel_name)
                    else:
                        channel = await category.create_voice_channel(channel_name)
                    print(f"    - Canal '{channel.name}' creado.")
                except Exception as e:
                    print(f"    - Error al crear canal: {e}")
        except Exception as e:
            print(f"  - Error al crear categoría: {e}")

    print("✅ Plantilla pública aplicada correctamente")
    await bot.close()

# ======================
# EJECUTAR BOT
# ======================

try:
    bot.run(TOKEN)
except Exception as e:
    print(f"❌ Error al ejecutar el bot: {e}")
