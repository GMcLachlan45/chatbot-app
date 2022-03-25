import nltk
from plugins.agent_plugin import AgentPlugin

class PosTag(AgentPlugin):
    def parse(self, query):
        token = nltk.word_tokenize(query)
        tagged = nltk.pos_tag(token)
        
        return tagged