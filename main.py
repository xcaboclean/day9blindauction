from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
clear()
print(logo)
stop_auction = True
blind_auction = {}
highest_bid = -1
while stop_auction:
  name = input("What is your name?")
  bid = input("What's your bid? :$")
  response = input("Are there any other bidders? Type 'yes' or 'no'.") 
  blind_auction[name] = float(bid)
  stop_auction =  (response == "yes")

print(blind_auction)

for person in blind_auction:
  if blind_auction[person] > highest_bid:
    highest_bid = blind_auction[person]
    highest_bid_name = person

print(highest_bid_name, highest_bid)