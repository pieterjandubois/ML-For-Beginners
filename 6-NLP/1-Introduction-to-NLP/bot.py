import random

random_responses = ["That is quite interesting, please tell me more.",
                        "I see. Do go on.",
                        "Why do you say that?",
                        "Funny weather we've been having, isn't it?",
                        "Let's change the subject.",
                        "Did you catch the game last night?"]

print("Hello, I am Marvin, the simple robot.")
print("You can end this conversation at any time by typing 'bye'")
print("After typing each answer, press 'enter'")
print("How are you today")

bot_name = "Elisa (bot)"

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        break
    else:
        response = random.choice(random_responses)
    print(f"{bot_name}: {response}")

print("It was nice talking to you, bye!")




