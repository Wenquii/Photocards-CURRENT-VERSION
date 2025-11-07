# Discord Photocards Bot

## Overview
This is a Discord bot that simulates virtual photocard collection in Discord servers. Users can collect, view, lock, and unlock photocards from various collections. The bot was originally created for Korean pop fan communities where photocard collecting is popular.

## Project Status
**Current State**: Bot is successfully configured and running in Replit environment. Connected to Discord as STAYNNIES#3081.

## Recent Changes (November 7, 2025)
- Imported GitHub repository and configured for Replit environment
- Installed Python 3.11 and dependencies (discord.py, pillow, flask)
- Fixed import errors: Changed `a_collections.a_collections` to `a_collections.a_collection` throughout the codebase
- Fixed Discord bot initialization to include required intents for message content
- Fixed bot.py to use correct token variable
- **Fixed critical channel filter bug**: Changed from checking `message.channel.name` to `message.channel.id` - this was preventing all commands from working
- Added ALLOWED_CHANNELS constant for better configuration management
- Fixed Image.ANTIALIAS deprecation warning (changed to Image.LANCZOS)
- Created .gitignore for Python project
- Configured workflow to run bot as console application
- Added DISCORD_PHOTOCARD_TOKEN secret for bot authentication

## Architecture

### Core Components
- **bot.py**: Main entry point. Handles Discord client initialization and message routing
- **commands/**: Command handler classes using factory pattern
  - base_class.py: Abstract base class and command registry
  - Individual command files: help, view, preview, unlock, lock, debug, a_collections
- **db/**: SQLite database management
  - schema.sql: User collection data schema
  - db.py: Database handler with CRUD operations
- **a_collections/**: Photocard collection management
  - a_collection.py: Collection class and collection loading
  - files/: Directory for photocard image files
- **image/**: Image processing for collection displays
  - image.py: Generates composite images of collections with PIL

### Technology Stack
- **Language**: Python 3.11
- **Main Libraries**:
  - discord.py 2.6.4: Discord bot framework
  - Pillow 12.0.0: Image processing
  - Flask 3.1.2: (included in requirements but not actively used)
- **Database**: SQLite (user_data.db)
- **Environment**: Replit with Nix package management

### Bot Commands
Command prefix: `tcg!`

Available commands:
- `collections` - List all available photocard collections
- `view <collection>` - View your collected cards
- `preview <collection>` - Preview all cards in a collection (admin)
- `unlock <collection> <n> <@user>` - Unlock cards for a user (admin)
- `lock <collection> <n> <@user>` - Lock/remove cards from a user (admin)
- `debug <@user>` - Show debug info for a user (admin)
- `help` - Display help information

### Admin Users
Admin user IDs are defined in constants.py:
- 935057263079600149
- 1351844085547405352
- 1022257383751303209

## Configuration

### Environment Variables
- `DISCORD_PHOTOCARD_TOKEN`: Discord bot authentication token (required)

### Database
- Type: SQLite
- File: user_data.db (auto-created, gitignored)
- Schema: Tracks user ID, photo group (collection), and photo ID ownership

### Workflow
- Name: discord-bot
- Command: `python bot.py`
- Output Type: Console
- Status: Running

## Project Structure
```
.
├── bot.py                 # Main bot entry point
├── constants.py          # Configuration constants
├── requirements.txt      # Python dependencies
├── commands/            # Command handlers
│   ├── __init__.py
│   ├── base_class.py   # Command factory pattern
│   ├── a_collections.py
│   ├── debug.py
│   ├── help.py
│   ├── lock.py
│   ├── preview.py
│   ├── unlock.py
│   └── view.py
├── db/                  # Database layer
│   ├── __init__.py
│   ├── db.py
│   └── schema.sql
├── a_collections/       # Collection management
│   ├── __init__.py
│   ├── a_collection.py
│   └── files/          # Photocard images
└── image/              # Image processing
    ├── __init__.py
    └── image.py
```

## Known Limitations
- Not designed to scale across multiple Discord servers (one bot per server)
- Channel restriction: Bot only responds in channel "1394358047635280013"
- Collections must be manually added to the a_collections/files/ directory
- All images in a collection must have identical dimensions

## Development Notes

### Adding New Collections
1. Create a new directory in `a_collections/files/` with the collection name
2. Add photocard images (PNG/JPG/JPEG) to the directory
3. Add a preview image (preview.jpg/png) for locked cards
4. All images must have identical dimensions

### Discord Intents
The bot requires the following intents:
- Default intents
- Message content intent (enabled in bot.py)

Make sure these are enabled in the Discord Developer Portal for your bot application.

## Future Enhancements
From original TODO:
- Add commands to create new collections via Discord interface
- Consider PostgreSQL for better scalability
- Multi-server support with proper isolation
