"""Functions built on OpenAI API."""

import openai as ai

from server.core import config

ai.api_key = config.OPENAI_API_KEY


def random_joke():
    """Generate a random joke."""

    return ai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are Jerry Seinfeld. You tell short jokes. Do not include any other text in the responses aside from the jokes.",
            },
            {"role": "user", "content": "Tell me a joke."},
        ],
    )
