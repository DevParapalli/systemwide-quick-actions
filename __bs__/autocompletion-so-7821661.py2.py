""" https://stackoverflow.com/questions/7821661/how-to-code-autocompletion-in-python """

import readline

class MyCompleter(object):  # Custom completer

    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:  # on first trigger, build possible matches
            if text:  # cache matches (entries that start with entered text)
                self.matches = [s for s in self.options 
                                    if s and s.startswith(text)]
                """
                # In case of completion in arbitrary part of string 
                self.matches = [s for s in self.options 
                   if text in s] 
                """
            else:  # no text entered, all matches possible
                self.matches = self.options[:]

        # return match indexed by state
        try: 
            return self.matches[state]
        except IndexError:
            return None

keywords = ["hello", "hi", "how are you", "goodbye", "great"]
completer = MyCompleter(keywords)
readline.set_completer(completer.complete)
readline.parse_and_bind('tab: complete')
for kw in keywords:
    readline.add_history(kw)

input = raw_input("Input: ")
print("You entered", input)