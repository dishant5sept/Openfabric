class AppModel:
    def __init__(self):
        self.request = InputClass()
        self.response = OutputClass()

class InputClass:
    def __init__(self, prompt=""):
        self.prompt = prompt

class OutputClass:
    def __init__(self):
        self.message = ""
