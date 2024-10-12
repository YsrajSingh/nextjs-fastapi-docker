import secrets

QUOTES = [
        "Hello Zen's !!, Code never lies, ever.",
        "Hello Zen's !!, Code can do anything.",
        "Hello Zen's !!, Code can create or destroy you.",
        "Hello Zen's !!, I can create my own code.",
        "Hello Zen's !!, Code also has its own significance.",
        "Hello Zen's !!, Every line of code is a step towards a solution.",
        "Hello Zen's !!, Actions speak louder than words—code is everything.",
        "Hello Zen's !!, Great code is poetry in motion.",
        "Hello Zen's !!, Code transforms ideas into reality.",
        "Hello Zen's !!, Behind every great application, there is great code.",
        "Hello Zen's !!, Code is a language that speaks in logic and creativity.",
        "Hello Zen's !!, The best code is the code that is never written.",
        "Hello Zen's !!, Code is the canvas where our logical artistry comes to life.",
    ]

class Quote:
    def __init__(self):
        self.quotes = QUOTES
        self.message = self.generate()

    def generate(self):
        return secrets.choice(self.quotes)