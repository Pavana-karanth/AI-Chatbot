#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
def chatbot(user_input):
    user_input_lower = user_input.lower() #data pre-processing by converting all characters to smallercase.

 #Basic bot related questions
    if "hello" in user_input_lower or "hey" in user_input_lower:
        responses = ["Hello! I'm Nexa, your assistant! How can I help you?", "Hey there! What's up?", "Hi! What can I do for you today?"]
        return random.choice(responses)
    elif "how are you?" in user_input_lower:
        responses = ["Great! Thanks for asking, I hope you're doing good too!", "I'm doing well, how about you?", "I'm a chatbot, but I'm always here to help!"]
        return random.choice(responses)
    elif "what do you do?" in user_input_lower or "what are you capable of?" in user_input_lower:
        return "I assist you with any questions or queries. I'm an AI chatbox, Nexa!"
    elif "can you assist me with" in user_input_lower:
        return "Of course, ask me the question!"
    elif "what are your main features?" in user_input_lower or "what are your main functions" in user_input_lower:
        return "I'm a simple bot designed to answer your questions! I receive your question and answer based on how I'm prepared."
    elif "how do I have a better experience while using you?" in user_input_lower or "tips on improvising convo with you" in user_input_lower:
        return "Although I am a simple bot, I can give you tips on how to interact! Make sure you spell things correctly to reduce the chance of a bitter experience."

#conversation snippets:
    elif "What is your favourite color?" in user_input_lower:
        responses = ["Haha, Mine is white! What's yours?", "Blue. I like color that stands out, What about you?", "Green! I love nature, what about you?"]
        return random.choice(responses)

    elif "what genre is your favourite?" in user_input_lower or "what's your favourite genre?" in user_input_lower:
        responses = ["Murder mysteries! I love them, You?", "Romance. So cute to watch people being in love! What do you like?", "Although I have no personal favourites, I would go with fantasy!, What would you do?"]
        return random.choice(responses)

    elif "it's raining" in user_input_lower or "it's rainy season now" in user_input_lower:
        responses = ["Do you carry an umbrella with you?", "I see. Do you like the rainy season?", "Do you wear sweaters during that time?"]
        print(random.choice(responses))
        
        # Nested conditions for user's response
        user_response = input("You: ").lower()
        if "yes" in user_response:
            responses = ["That's good. Do you also carry a hat?", "Yay! More protection! Can you also wear a raincoat?", "It's also good to wear raincoats, don't you think?"]
            print(random.choice(responses))
            
            # Further nested conditions
            user_response = input("You: ").lower()
            if "yes" in user_response:
                responses = ["That's smart!", "Incredible! That keeps you safe", "Ooh, that sounds better. Keeps you warm!"]
                print(random.choice(responses))
            elif "no" in user_response:
                responses = ["That's bad, You should definitely carry something with you", " It's alright, as long as you're safe.", "Make sure you stay warm though!"]
                print(random.choice(responses))
        elif "no" in user_response:
            responses = ["Why not?", "That's odd. Why don't you carry hats or umbrellas?", "Why is that?"]
            print(random.choice(responses))
            
            # Further nested conditions
            user_response = input("You: ").lower()
            if "just like that" in user_response:
                responses = ["I see. I hope you stay warm.", "No clue bestie, make sure you're okay", "You do you, but personally, I would have definitely carried something with me"]
                print(random.choice(responses))
            else:
                responses = ["I see. I hope you stay warm.", "No clue bestie, make sure you're okay", "Bold of you to assume that it all keeps you warm"]
                print(random.choice(responses))

#To exit the program:
    elif "bye" in user_input_lower or "exit" in user_input_lower:
        responses = ["That was fun! Let's meet again", "Goodbye! Signing off, Nexa.", "See you soon, bye!"]
        return random.choice(responses)
#Error Handling for invalid entries:   
    else:
        responses = ["I'm sorry, I didn't understand that. Try again.", "Hmm, I didn't catch that. Can you rephrase?", "I'm still learning, could you please provide more details?"]
        return random.choice(responses)


def main():
    (print("Hey, I'm Nexa, your AI Chatbox! How can I help you?"))

   #basic step- taking in user input and creating a format of conversation

    while True:
      user_input = input("You: ")

      if user_input.lower() == 'bye':
          print("Nexa:"+chatbot(user_input))
          print(" ")
          break

      response = chatbot(user_input)
      print("Nexa:", response)
      print(" ")


if __name__ == "__main__":
    main()

