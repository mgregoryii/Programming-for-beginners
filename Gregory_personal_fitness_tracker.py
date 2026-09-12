# I attempted the basic level difficulty
#---Workout Session--- 1

#Select workout: 
# 1. Running
# 2. Weight Training
# 3. Swimming
# 4. Yoga
# 5. Cycling
# Enter your choice (1-5): 2
# Enter calories burned (1-2000): 180
# Enter duration in minutes (1-720): 45

# Workout Report
# Workout: Weight Training
# Calories burned: 180.0
# Duration: 45.0 minutes
# Calories per minute: 4.0
# Intensity: Low
# Results: Weight Training | 180.0 | 45.0 minutes | 4.0 | Low

# ---Workout Session--- 2

# Select workout: 
# 1. Running
# 2. Weight Training
# 3. Swimming
# 4. Yoga
# 5. Cycling
# Enter your choice (1-5): 3
# Enter calories burned (1-2000): 300
# Enter duration in minutes (1-720): 40

# Workout Report
# Workout: Swimming
# Calories burned: 300.0
# Duration: 40.0 minutes
# Calories per minute: 7.5
# Intensity: Moderate
# Results: Swimming | 300.0 | 40.0 minutes | 7.5 | Moderate

# ---Workout Session--- 3

# Select workout: 
# 1. Running
# 2. Weight Training
# 3. Swimming
# 4. Yoga
# 5. Cycling
# Enter your choice (1-5): 4
# Enter calories burned (1-2000): 320
# Enter duration in minutes (1-720): 30

# Workout Report
# Workout: Yoga
# Calories burned: 320.0
# Duration: 30.0 minutes
# Calories per minute: 10.7
# Intensity: High
# Results: Yoga | 320.0 | 30.0 minutes | 10.7 | High

# ---Workout Session--- 4

# Select workout: 
# 1. Running
# 2. Weight Training
# 3. Swimming
# 4. Yoga
# 5. Cycling
# Enter your choice (1-5): 3 
# Enter calories burned (1-2000): 250
# Enter duration in minutes (1-720): 50

# Workout Report
# Workout: Swimming
# Calories burned: 250.0
# Duration: 50.0 minutes
# Calories per minute: 5.0
# Intensity: Moderate
# Results: Swimming | 250.0 | 50.0 minutes | 5.0 | Moderate

# ---Workout Session--- 5

# Select workout: 
#1. Running
#2. Weight Training
#3. Swimming
#4. Yoga
#5. Cycling
#Enter your choice (1-5): 2
#Enter calories burned (1-2000): 200
#Enter duration in minutes (1-720): 20
#Workout Report
#Workout: Weight Training
#Calories burned: 200.0
#Duration: 20.0 minutes
#Calories per minute: 10.0
#Intensity: High
#Results: Weight Training | 200.0 | 20.0 minutes | 10.0 | High


# This code is designed to track a user's fitness activity over 5x rounds of exercises to symbolize 1x week of fitness activity.
# First we welcome the user.
print("Welcome to the Fitness Tracker!\nThis tracker is designed to record your fitness activity according to 5 excersises.\nYou will log 3 workouts.")

# Next we prompt the user for their input selecting from 5x excersises, calorie selection between 1-2000, duration in minutes from 1-720
# and the intensity is auto selected based on the calorie and duration inputs. Error checking is applied for workout, calorie, and duration
# selection.

def workout_name():
    print("\nSelect workout: ")
    print("1. Running")
    print("2. Weight Training")
    print("3. Swimming")
    print("4. Yoga")
    print("5. Cycling")

    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))

            if 1 <= choice <=5:
                workout_name = {
                    1: "Running",
                    2: "Weight Training",
                    3: "Swimming",
                    4: "Yoga",
                    5: "Cycling"
                }
                return workout_name[choice]

            else:
                print("Error: Please enter a number from 1 to 5.")

        except ValueError:
            print("Error: Please enter a valid number from 1 to 5.")

def get_calories():   
    while True:
        try:
            calories = float(input("Enter calories burned (1-2000): "))

            if 1 <= calories <= 2000:
                return calories
            else:
                print("Error: Calories must be between 1 and 2000.")

        except ValueError:
            print("Error: Please enter a valid number.")

def get_duration():
    while True:
        try:
            duration = float(input("Enter duration in minutes (1-720): "))
            if 1 <= duration <= 720:
                return duration
            else:
                print("Error: Calories must be between 1 and 720.")
            
        except ValueError:
            print("Error: Please enter a valid number.")

def calories_per_minute(calories, duration): 
    return round(calories / duration, 1)

def get_intensity(rate):
    if rate < 5.0:
        return "Low"
    elif rate < 10.0:
        return "Moderate"
    else:
        return "High"

# Main loop iterates the 5x prompting the user each time for inputs and printing the results below each workout section recording.

for session in range(1, 6):
    print(f"\n---Workout Session--- {session}")

    workout = workout_name()

    calories = get_calories()
    duration = get_duration()

    rate = calories_per_minute(calories, duration)
    intensity = get_intensity(rate)

    print("\nWorkout Report")
    print(f"Workout: {workout}")
    print(f"Calories burned: {calories}")
    print(f"Duration: {duration} minutes")
    print(f"Calories per minute: {rate:.1f}")
    print(f"Intensity: {intensity}")
    print(f"Results: {workout} | {calories} | {duration} minutes | {rate:.1f} | {intensity}")


# Conclusion message - displayed only after all 5 sessions 
print("\nAll workouts logged. Great job staying active!")