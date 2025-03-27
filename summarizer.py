from openai import OpenAI


class Summarizer:
    def __init__(self, api_key, language):
        self.client = OpenAI(api_key=api_key)
        self.language = language

    def summarize(self, text):
        response = self.client.responses.create(
            model="gpt-4o",
            instructions=f"Please summarize this text with language {self.language}",
            input=text,
        )
        return response.output_text
