import click
from meet_bot import MeetBot

@click.command()
@click.option("--meet-url", required=True, help="Google Meet URL")
@click.option("--user-name", default="Ai Bot", help="User name for Google Meet")
@click.option("--output-file-name", default="output.wav", help="Output file name for audio recording")
@click.option("--language", default="tr-TR", help="Language for speech recognition")
@click.option("--api-key", required=True, help="OpenAI API key")
def main(meet_url, user_name, output_file_name,language, api_key):
    meet_bot = MeetBot(meet_url, user_name, output_file_name,language,api_key)
    meet_bot.start()

if __name__ == "__main__":
    main()
