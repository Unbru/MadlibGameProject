# color database
BLUE = "\033[34m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
WHITE = "\033[0m"

# instructions
print(f"""{BLUE}
=========================- MADLIB -=========================

You will make a story using your own words. 
This is the story template you will be using, 
please make each word grammatically correct: {WHITE}

I did a {YELLOW}(adjective1){WHITE} thing. 
I {GREEN}(verb1){WHITE} this thing. 
In {YELLOW}(adjective2){WHITE} the thing was {YELLOW}(adjective3){WHITE}. 
Well, im a bit {YELLOW}(adjective4){WHITE} to tell you, but... 
I was {GREEN}(verb2){WHITE} a {RED}(noun1){WHITE}. 
Yeah, yeah, I know it was a {YELLOW}(adjective1){WHITE} thing to do. 
But I had to do it, if I didnt, {RED}(noun2){WHITE} would have {GREEN}(verb3){WHITE} the whole {RED}(noun3){WHITE}. 
{BLUE}
==================================================
{WHITE}""")

# user input
adjective1 = input(f"Enter an {YELLOW}adjective{WHITE} word: ")
adjective2 = input(f"Enter an {YELLOW}adjective{WHITE}: ")
adjective3 = input(f"Enter an {YELLOW}adjective{WHITE}: ")
adjective4 = input(f"Enter an {YELLOW}adjective{WHITE}: ")
verb1 = input(f"Enter a {GREEN}verb{WHITE}: ")
verb2 = input(f"Enter a {GREEN}verb{WHITE}: ")
verb3 = input(f"Enter a {GREEN}verb{WHITE}: ")
noun1 = input(f"Enter a {RED}noun{WHITE}: ")
noun2 = input(f"Enter a {RED}noun{WHITE}: ")
noun3 = input(f"Enter a {RED}noun{WHITE}: ")

print()

# final output with madlib result
print("Final results:")

print()

print(f"I did a {YELLOW}{adjective1}{WHITE} thing.")
print(f"I {GREEN}{verb1}{WHITE} this thing.")
print(f"In {YELLOW}{adjective2}{WHITE} the thing was {YELLOW}{adjective3}{WHITE}.")
print(f"Well, im a bit {YELLOW}{adjective4}{WHITE} to tell you, but...")
print(f"I was {GREEN}{verb2}{WHITE} a {RED}{noun1}{WHITE}.")
print(f"Yeah, yeah, I know it was a {YELLOW}{adjective1}{WHITE} thing to do.")
print(f"But I had to do it, if I didnt, {RED}{noun2}{WHITE} would have {GREEN}{verb3}{WHITE} the whole {RED}{noun3}{WHITE}.")