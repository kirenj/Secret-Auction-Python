from replit import clear
from art import logo

print(logo)

def winner_check():
  win_num = 0
  for i in auction_bids:
    if auction_bids[i] > win_num:
      win_num = auction_bids[i]

  for j in auction_bids:
    if auction_bids[j] == win_num:
      print(f"The winner is {j} with a bid of ${auction_bids[j]}")

print("Welcome to the secret auction program!")

auction_bids = {}

bid_continue = True

while bid_continue == True:
  
  name = input("What is your name: ")
  bid = int(input("What's your bid: $"))
  bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

  auction_bids[name] = bid
    
  if bidders == 'yes':
    bid_continue = True
    clear()     
  else:
    winner_check()
    bid_continue = False
    print(auction_bids)

  
  

  
    