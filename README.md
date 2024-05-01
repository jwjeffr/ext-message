# ext-message
## Library for sending messages to an external app

This is a simple library for sending files to external apps. As of now, this is only compatible with Discord, but with plans to expand to Slack, Email, and SMS.

To install:

```bash
pip install ext-message
```

To create an environment file, you will need a Discord bot API key (bots are creatable [here](https://discord.com/developers/applications)) and your Discord user ID. Then, run:

```bash
echo user_id=${USER_ID} > .env
echo api_key=${API_KEY} >> .env
```

Or at these manually in `example.env` and run `mv example.env .env`. Then, run:

```bash
ext-message example.txt
```

or any other text file. You can also specify a custom environment file using `--env`:

```bash
ext-message example.txt --env example.env
```

You need to be sharing a server with your bot in order to receive the message.