from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for person in blind_auction:
    if blind_auction[person] > highest_bid:
      highest_bid = blind_auction[person]
      highest_bid_name = person

  print(f"The winner is {highest_bid_name} with a bid of ${highest_bid}")

clear()
print(logo)
stop_auction = True
blind_auction = {}
highest_bid = -1
while stop_auction:
  name = input("What is your name? ")
  bid = int(input("What's your bid? :$"))
  response = input("Are there any other bidders? Type 'yes' or 'no'.") 
  blind_auction[name] = bid
  find_highest_bidder(blind_auction)
  stop_auction =  (response == "yes")
  


