# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code thta you can easily call over and over.",
# }

# #Retrieving items from dictionary
# # print(programming_dictionary["Bug"])

# #Adding new items to dictionary if the "Loop" str already exists the value will be changed
# programming_dictionary["Loop"] = "The action of doing something over and over again"



# for key in programming_dictionary:
#     print(programming_dictionary[key])
    
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# student_grades = {}
# for student in student_scores:
#   score = student_scores[student]
#   if score > 90:
#     student_grades[student] = "Outstanding"
#   elif score > 80:
#     student_grades[student] = "Exceeds Expectations"
#   elif score > 70:
#     student_grades[student] = "Acceptable"
#   else:
#     student_grades[student] = "Fail"
    
# print(student_grades)

# travel_log = {
#     "France": {"cities_visited": ["Nanci", "Paris", "Marselie"], "total_visitis": 12},
#     "Germany": {"cities_visited": ["Frankfurt","Hannover","Berlin"], "total_visitis":15}
# }

# print(travel_log["Germany"]["total_visitis"])

# travel_log = [
#    { 
#     "Country": "France",
#     "cities_visited": ["Nanci", "Paris", "Marselie"],
#     "total_visitis": 12
#     },
#     {
#     "Country": "Germany", 
#      "cities_visited": ["Frankfurt","Hannover","Berlin"],
#      "total_visitis":15
#      }
# ]

# print(travel_log[0]["cities_visited"][1])
bids = {}
bidding_finished = False



def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder] 
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highest_bid}\n')
        

while not bidding_finished:
    name = input('What is your name?\n')
    price = int(input('Whar is your bid? $\n'))
    bids[name] = price
    aws = input('Are there any other bidders?Type yes or no\n')
    if aws == 'no':
        bidding_finished = True
        find_highest_bidder(bids)


        
