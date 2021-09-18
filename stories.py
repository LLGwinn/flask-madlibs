"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, topic, title, words, text):
        """Create story with words and template text."""

        self.topic = topic
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text

# Here's a story to get you started

story1 = Story(
    'Fairy Tale',
    'Magical Fairy Tale',
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    'Celebrity',
    'I Met a Celebrity!',
    ["celebrity", "city", "body_part", "adjective", "exclamation"],
    """While walking in {city}, who did I see but {celebrity}! My
       {body_part} got all {adjective} and all I could say was '{exclamation}!'"""
)

story3 = Story(
    'Animals',
    'Animal Safety Warning',
    ["animal", "verb", "adjective", "body_part"],
    """Be careful around {animal}s. Sometimes they {verb}, and they smell
       {adjective}. Best to just pat them on the {body_part} and be on your way."""
)

story_lookup = {story1.topic: story1,
                story2.topic: story2,
                story3.topic: story3}

