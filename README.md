# Freddy 🤖

Freddy is a Telegram bot in Python, designed to be a friendly AI assistant that cheerfully responds to incoming user messages on behalf of you. It is directly connected to the user business chat (for premium Telegram users only). The implementation is straightforward and conveys the purpose of sending and receiving text messages from Telegram direct chat. The code uses the `python-telegram-bot` library for Telegram API communication and is connected to the Google Gemini API for AI magic.

## Before You Start
You need to have a business Telegram account (Premium) to connect a bot to your chat. Follow these steps:
1. Create your bot from [@BotFather](https://t.me/botfather) on Telegram and enable business mode from bot settings.
2. Go to `Settings > Telegram Business > Chatbots` and integrate your bot into your chat.

More details about Telegram Business can be found [here](https://telegram.org/blog/telegram-business/).




## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/7azmi/Freddy.git
    ```
2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Add environment variables:
    ```sh
    export BOT_TOKEN=<obtain it from @BotFather on Telegram. Do not forget to enable business mode!>
    export GEMINI_API_KEY=<Gemini API key, you can get it for free from https://ai.google.dev>
    export BUSINESS_CHAT_ID=<your telegram chat id>
    ```
4. Personalize your AI instructions in `ai_instructions.txt`.
5. Run the app locally:
    ```sh
    python app.py
    ```

## Contributing
This project is complete as it serves its purpose. It demonstrates that bots can be integrated with Telegram business chats and interact with users.
