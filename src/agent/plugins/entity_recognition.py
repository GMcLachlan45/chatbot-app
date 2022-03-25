from plugins.agent_plugin import AgentPlugin
import nltk

class EntityRecognition(AgentPlugin):
    def parse(self, query):
            named_ent = nltk.ne_chunk(query, binary=True)
        
            ne_set = []
            for i in named_ent:
                if type(i) == nltk.tree.Tree:
                    st = ""
                    for j in range (len(i)):
                        st = st + " " + i[j][0]
                        ne_set.append(st.strip())
            if "Hello" in ne_set:
                ne_set.pop(0)
            if "Hi" in ne_set:
                ne_set.pop(0)
            if "Hey" in ne_set:
                ne_set.pop(0)


            return ne_set