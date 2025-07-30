message=input('Enter your code for your message')
team=input('Which team is this?')

if message== '1999'and team=='A':
    print("There is a traitor in team B. Find him without letting the team know cause it can be anyone.")
elif message== '2422'and team=='B':
    print("The president is in danger. Keep a watch over him secretly.")
elif message=='1832'and team=='C':
    print("There is a traitor in team A. He is off gaurd for now because of wrong information. This is the best chance to catch him.")
elif message=='3943'and team=='D':
    print("Assasinate the minister.")
else:
    print("INTRUDER ALERT!")