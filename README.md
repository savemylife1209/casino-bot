# Casino Bot

Casino Bot is a Discord bot that allows users to play casino-style games, manage bets, and earn bonuses.

## Features
- Customizable betting system
- Bonus multiplier with cooldown
- Easy-to-use commands
- Modular design for adding new features

## Requirements
- Python 3.8 or higher
- Dependencies listed in `requirements.txt`

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/casino-bot.git
   cd casino-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the bot:
   - Rename `config.yml` to `config.yml` if not already done.
   - Update the `config.yml` file with your bot's settings.
   - Add your bot token to the `.env` file:
     ```
     TOKEN=your-bot-token
     ```

4. Run the bot:
   ```bash
   python bot.py
   ```

## Usage
- Use the prefix `/` to interact with the bot.
- Example commands:
  - `/bet <amount>`: Place a bet.
  - `/bonus`: Claim your bonus (subject to cooldown).

## License
This project is licensed under the [Apache License 2.0](LICENSE).
