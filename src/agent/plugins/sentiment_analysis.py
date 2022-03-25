from plugins.agent_plugin import AgentPlugin
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class SentimentAnalysis(AgentPlugin):
    def parse(self, query):
        sentiment = SentimentIntensityAnalyzer().polarity_scores(query)
        return sentiment['compound'] #return a value between -1 and 1 indicating negativity

       