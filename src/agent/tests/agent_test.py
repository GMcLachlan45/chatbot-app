import pytest
from agent import Agent

nltk_dependencies = [
    'popular',
    'vader_lexicon'
]

agent = Agent(
    [],
    nltk_dependencies,
    "../../config/dataset.json",
    "../../chat_model",
    tokenizer_path = "../../tokenizer.pickle",
    label_encoder_path = "../../label_encoder.pickle"
)

def synonym_test():
    assert agent.query("What medicine should I take for a migraine?") == agent.query("What medication should I take for a migraine?")

def sentiment_test():
    query = agent.query("Hey doctor, I feel sick")
    valid = query.startswith("I'm sorry to hear that!")
    valid = valid or query.startswith("That doesn't sound very good.")
    valid = valid or query.startswith("I'm sorry you feel this way.")
    valid = valid or query.startswith("I hope I can help you feel better!")
    valid = valid or query.startswith("Hold on, we'll get you feeling better in no time!")
    valid = valid or query.startswith("I'll work my hardest to help you feel better.")
    assert valid

def spellcheck_test():
    assert agent.query("What medacine should I take for a migraine?") == agent.query("What medicine should I take for a migraine?")