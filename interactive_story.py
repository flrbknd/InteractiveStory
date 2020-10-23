# -*- coding: utf-8 -*-
"""
Latest version: 23.10.2020. 

@author: bkndflr

"""

# DEFINING INTERACTIVE TEXT METHODS #

class InteractiveText:
  def __init__(self, text):
    self.text =  text
    self.options = []
  
  def add_storyline(self, text):
    self.options.append(text)
    
  def play_story(self):
    starting_point = self
    print("1", starting_point.text)
    while starting_point.options != []:
      user_choice = input("Please enter 'A' or 'B' to continue: ") 
      if user_choice not in ["A", "a", "B", "b"]:
        print("Please choose from 'A' and 'B' options only. ")
        continue
      option_index = 0 if user_choice in ["A", "a"] else 1     
      next_part = starting_point.options[option_index]
      starting_point = next_part
      print(next_part.text)
    
# USER GREETING #

user_name = input("Hello, what's your name?")

# CREATE TEXT BITS #

text_root = InteractiveText("""
You are walking your dog late at night, when you pass by an old, deserted mansion. 
It looks dark and gloomy, you remember that folks in your neighborhood call it the Haunted House. 

Suddenly your dog pulls the leash and you drop the handle. Your dogs runs into the haunted garden. 
What do you do?

A ) Follow your dog.
B ) Too scared. You go home. 
""")

choice_a = InteractiveText("""
You are calling your dog's name, but no replies. 
The house is empty, there is dust everywhere. Suddenly a wardrobe opens.

What do you do?

                           
A ) Stay.
B ) Run away as fast as you can. 
""")

choice_a_a = InteractiveText("""
In the wardrobe there is a ghost and but it's very kind. 
It helps you find your dog and offers you your dreamjob. 

You win. 
                             

""")
choice_a_b = """
As you run you see your dog in front of the house waiting for you. 

You run home together, you are safe. 

"""

choice_b = InteractiveText("""
At home you go to bed, but lie awake for hours, you are too worried because your dog has not returned yet. 
What do you do?
                           

A ) Nothing.
B ) You get up and go back to the haunted house.
""")
choice_b_a = InteractiveText("""
Your dog never returns. You hear stories that it lives with a ghost now. 

You lose.
                             
""")
choice_b_b = InteractiveText("""
On your way to the haunted house you bump into your dog. It's coming together with a ghost. 

From now on you have two pets.
""")

# INITIALIZE STORY #

text_root.add_storyline(choice_a)
text_root.add_storyline(choice_b)
choice_a.add_storyline(choice_a_a)
choice_a.add_storyline(choice_a_b)
choice_b.add_storyline(choice_b_a)
choice_b.add_storyline(choice_b_b)

# PLAY STORY #

text_root.play_story()


