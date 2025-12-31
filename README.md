# Discord Community Generator

🎮 **Discord Community Generator** es un bot de Discord diseñado para crear comunidades gaming automáticamente usando plantillas genéricas. Permite generar **roles**, **categorías** y **canales de texto o voz** a partir de una estructura base, adaptable a cualquier temática de juegos. Ideal para integrarlo con IA que rellene la plantilla automáticamente o para personalizar manualmente la comunidad.

---

## 🔹 Características

- Crear roles automáticamente según una plantilla genérica.
- Crear categorías y canales de texto/voz.
- Aplicar permisos por categoría usando roles específicos.
- Compatible con plantillas vacías para que una IA o usuario rellene los nombres.
- Permite mantener un flujo de trabajo profesional y organizado en comunidades gaming.
- Totalmente adaptable a cualquier juego o temática.

---

## 📁 Estructura del proyecto

```
discord-community-generator/
│
├─ bot.py                 # Código principal del bot
├─ plantilla_publica.json  # Plantilla genérica con campos vacíos
├─ README.md              # Documentación del proyecto
└─ requirements.txt       # Dependencias de Python
```

---

## ⚙️ Requisitos

- Python 3.10 o superior
- Librería `discord.py`
- Token de bot de Discord con permisos de administrador
- ID del servidor de Discord donde se aplicará la plantilla

---

## 📝 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/Markelson57/discord-community-generator/tree/main
cd discord-community-generator
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Configura el bot:

- Abre `bot.py` y reemplaza:

```python
TOKEN = "TU_TOKEN_AQUI"
GUILD_ID = TU_ID_DE_SERVIDOR
JSON_FILE = "plantilla_publica.json"
```

- Modifica `plantilla_publica.json` si quieres personalizar la comunidad, o deja los campos vacíos para que la IA los genere.

---

## 🚀 Uso

1. Ejecuta el bot:

```bash
python bot.py
```

2. El bot:

- Creará roles según la plantilla.
- Creará categorías y canales.
- Aplicará permisos según los roles indicados en `allowed_roles`.

3. Una vez terminado, el bot se desconectará automáticamente.

---

## 📄 Plantilla genérica (`plantilla_publica.json`)

Ejemplo de campos que puedes rellenar:

```json
{
  "community_name": "",
  "description": "",
  "roles": [
    { "role_type": "", "description": "", "permissions": "" }
  ],
  "categories": [
    {
      "category_type": "",
      "description": "",
      "allowed_roles": [""],
      "channels": [
        { "channel_name": "", "channel_type": "" }
      ]
    }
  ],
  "instructions": ""
}
```

- `role_type` → tipo de rol (staff, juego, general, especial)  
- `permissions` → "Administrador" o vacío  
- `category_type` → tipo de categoría (información, general, juego, otros)  
- `channel_type` → `"text"` o `"voice"`  

---

## 🤖 Integración con IA

Puedes usar esta plantilla como **base de datos** para que una IA (por ejemplo ChatGPT) genere:

- Nombres de roles y categorías.
- Canales de texto y voz.
- Organización por juegos o temáticas.

Ejemplo de solicitud a la IA:

> "Usa la plantilla base y crea una comunidad para FPS con roles de staff, roles por juego (CS:GO, Valorant) y categorías de chat general y competitivo."

---

## ⚠️ Advertencias

- El bot **borra todos los canales y roles** (excepto @everyone y el bot) antes de crear los nuevos.  
- Asegúrate de probarlo en un servidor de prueba antes de usarlo en tu servidor principal.

---

## 📌 Contribuciones

Si quieres mejorar esta plantilla o añadir compatibilidad con más tipos de roles y permisos, siéntete libre de abrir un **pull request**.

---

## 📄 Licencia

MIT License

