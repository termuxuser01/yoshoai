from chatterbot.logic import LogicAdapter

class UserDismissLogicAdapter(LogicAdapter):
    """Logic adpater for checking if the user says good bye"""

    def __init__(self, chatbot, **kwargs):
        
        self.byes = [
                "bye", "good bye", "see you", 
                "farewell", "take care", "bye now",
                "ciao", "bye now"
                ]


        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        for bye in self.byes:
            if bye == statement.text:
                print("We have a match!")
                return True
            else:
                continue

        print("no match")
        return False

    def process(self, input_statement, aditional):
        from difflib import SequenceMatcher as sm
        yosho_byes = [
                "see ya masta!", "don't go masta!"
                ]
        
        input_statement.text = yosho_byes[0]

        return input_statement




        


