print("=" * 67)
print("Assignment 01")
print("=" * 67)
print("Question 1")
print("=" * 67)
print("Question i (Comments)")
#Author: O'Neal Jean 
#Assignment: #1
print("=" * 67)
print("Question ii -> 4 variables")
#String 
gym_member = "Alex Alliton"

#Float 
prefered_weight_kg = 20.5 

#Int 
highest_reps = 25

#boolean 
membershi_active = True
print("=" * 67)
print("Question iii -> dictionary")
#Dictionary -> This dictionary has values of integers that are within Tuples. The keys are string and the values are Tupeles 
# str: (int, int, int)
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (20, 100, 25),
    "Taylor": (30, 21, 45)
}
print("=" * 67)

print("Question iv Loop:")
#The loop to calculate the total workout minutes: 
for name, stats in list(workout_stats.items()):
    total = sum(stats)
    workout_stats[f"{name}_Total"] = total 
print(workout_stats)
print("=" * 67)

print("Question v")
#Here is a two dimensional array  where the first element contains of all strings and the rest contains one string (for the name)
# and 3 integers representing the workout minutes. 
workout_list = [
    ["Name", "Yoga", "Running", "Weightlifting"]
] 
#Extracting the workout minutes from the dictionary 
for name, stats in workout_stats.items(): 
    if isinstance(stats, tuple):
     workout_list.append([name, stats[0], stats[1], stats[2]])

#Displaying the 2D Array
for row in workout_list:
    print(row)

print("=" * 67)
print("Question vi -> Slicing the workout_list")
#Slicing the workout_list 
#Extract and print the minutes of yoga and running for ALL students: 
#Going through each row that is starting from ALEX instead of the columns such as Name, Yoga etc.
for row in workout_list: 
   print(row[0], row[1:3])
print(" ")
#Extracting and printing the minutes for Weightlifting for the last two friends
last_two_friends = workout_list[-2:]
for row in last_two_friends: 
    print(f"{row[0]}, Weightlifting: {row[-1:]}")
print("=" * 67)
print("Question vii -> if statement within a loop:")
#Question G 
for name, stats in workout_stats.items():
    if isinstance(stats, int): #looking for the totals
        if stats >= 120: 
            friend_name = name.replace("_Total", "")
            print(f"Great job staying active {friend_name}")


print("=" * 67)
print("Question viii -> Input Feature.") 
search_name = input("Enter your friend's name to find them within the system:")
if search_name in workout_stats: 
    stats = workout_stats[search_name]
    yoga = stats[0]
    Running = stats[1]
    weightlifting = stats[2]
    total = sum(stats)

    print(f"Workout Summary for {search_name}:")
    print(f"Yoga: {yoga} minutes")
    print(f"Running: {Running} minutes")
    print(f"weightlifitng: {weightlifting} minutes")
    print(f"Total Workout Time: {total} minutes")
else: 
    print(f"Friend {search_name} not found in the records.")
print("=" * 67)
print("Question ix")
#Question i.  
totals = {}
for name, value in workout_stats.items(): 
    if isinstance(value, int):
        friend_name = name.replace("_Total", "")
        totals[friend_name] = value
        print(totals)
high_total = max(totals, key = totals.get) 
lowest_total = min(totals, key = totals.get)


print(f"{high_total} has the highest total workout: {totals[high_total]}")
print(f"{lowest_total} has the lowest total workout: {totals[lowest_total]}")
print("=" * 67)