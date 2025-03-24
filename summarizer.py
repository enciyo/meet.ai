import openai
import os

class Summarizer:
    def __init__(self, api_key,language):
        openai.api_key = api_key
        self.model_engine = "text-davinci-003"
        self.language = language

    def summarize(self, text):
        prompt = f"Please summarize this with language {self.language}:\n{text}\n"
        completion = openai.Completion.create(engine=self.model_engine,prompt=prompt)
        summary = completion.choices[0].message.content
        return summary
