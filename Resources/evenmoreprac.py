counties = ("Arapahoe","Denver","Jefferson")
for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict.get(county))

# get county with voters
# first variable is assigned to keys(counties) second variable is assigned to values(voters)

for county, voters in counties_dict.items():
    print(county, voters)

voting_data = [{"county":"Arapahoe","registered_voters": 422829},{"county":"Denver","registered_voters": 463353},{"county":"Jefferson","registered_voters": 463353}]

for county_dict in voting_data:
    print(county_dict)

# Nested for loop
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

# intial code
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

# modified code with f-strings
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# original code
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

# modified code with f-strings
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
    
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)


for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


