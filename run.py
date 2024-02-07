import gspread
import json
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('gym_app')

workout = SHEET.worksheet('exercise')
data = workout.get_all_values()
#print(data)




# Creating a Python dictionary with exercises as keys and muscle types as values
with open('exercisedict.json', 'r') as file:
    exercise_dict = json.load(file)


muscle_dict = {
    "pectorals": [
        "bench press (flat, incline, decline)",
        "dumbbell flyes (flat, incline, decline)",
        "chest dips",
        "push-ups",
        "cable crossovers"
    ],
    "triceps": [
        "bench press (flat, incline, decline)",
        "chest dips",
        "push-ups",
        "overhead press (barbell, dumbbell)",
        "tricep extensions (skullcrushers)",
        "tricep pushdowns (cable)",
        "overhead tricep extension (dumbbell, cable)",
        "dips",
        "close-grip bench press"
    ],
    "shoulders": [
        "bench press (flat, incline, decline)",
        "dumbbell flyes (flat, incline, decline)",
        "push-ups",
        "pull-ups/chin-ups",
        "overhead press (barbell, dumbbell)",
        "planks",
        "clean and press",
        "snatch",
        "thrusters",
        "kettlebell swings",
        "farmers walk"
    ],
    "lower back": [
        "deadlift",
        "squats (back squat, front squat, overhead squat)",
        "deadlifts (traditional, sumo, romanian)",
        "planks",
        "kettlebell swings"
    ],
    "glutes": [
        "deadlift",
        "squats (back squat, front squat, overhead squat)",
        "leg press",
        "lunges (barbell, dumbbell)",
        "deadlifts (traditional, sumo, romanian)",
        "clean and press",
        "snatch",
        "thrusters",
        "kettlebell swings"
    ],
    "hamstrings": [
        "deadlift",
        "squats (back squat, front squat, overhead squat)",
        "leg press",
        "lunges (barbell, dumbbell)",
        "hamstring curls (lying, seated)",
        "deadlifts (traditional, sumo, romanian)",
        "clean and press",
        "snatch",
        "kettlebell swings"
    ],
    "upper back": [
        "deadlift",
        "bent-over rows (barbell, dumbbell)",
        "t-bar row",
        "lat pulldowns",
        "deadlifts (traditional, sumo, romanian)",
        "clean and press",
        "snatch",
        "thrusters",
        "farmers walk"
    ],
    "forearms": ["deadlift", "farmers walk"],
    "lats": [
        "pull-ups/chin-ups",
        "bent-over rows (barbell, dumbbell)",
        "t-bar row",
        "lat pulldowns",
        "seated cable rows"
    ],
    "biceps": [
        "pull-ups/chin-ups",
        "bent-over rows (barbell, dumbbell)",
        "lat pulldowns",
        "seated cable rows",
        "bicep curls (barbell, dumbbell, cable)",
        "hammer curls",
        "preacher curls",
        "concentration curls",
        "ez-bar curls"
    ],
    "middle back": ["t-bar row", "seated cable rows"],
    "shoulder deltoids": ["lateral raises (dumbbell, cable)"],
    "front deltoids": ["front raises (dumbbell, cable)"],
    "rear deltoids": ["rear delt flyes (dumbbell, machine)"],
    "trapezius": ["shrugs (barbell, dumbbell)"],
    "forearm": ["hammer curls"],
    "chest": ["dips", "close-grip bench press"],
    "quadriceps": [
        "squats (back squat, front squat, overhead squat)",
        "leg press",
        "lunges (barbell, dumbbell)",
        "leg extensions",
        "clean and press",
        "snatch",
        "thrusters"
    ],
    "calves": ["calf raises (seated, standing)"],
    "abdominals": [
        "crunches",
        "russian twists",
        "planks",
        "cable woodchoppers"
    ],
    "obliques": ["russian twists", "cable woodchoppers"],
    "lower abdominals": ["leg raises (hanging, lying)"],
    "hip flexors": ["leg raises (hanging, lying)"],
    "core": ["farmers walk"]
}


'''
create an app, where you can put the following data in:
1 exercise
2 number of sets
3 number of repetition per each set
4 the weight for each set

after that the app calculates which muscles has been effected by the exercise regarding:
1 sum of all weight (sets * reps * weight) by muscle type(column) by each exercise(row)
2 sum of weight by exercise

also:
ability to add, remove and modify exercise

'''

'''
input tree:

1 enter exercise
    1 enter set (repetition * weight)
        1 enter value of reps and weight --> ['reps', 'weight', 'reps', ...('set' value)] 
        2 options for all kinds of printing:
            1 recent input
            2 muscles effected and values
            3 restart input tree
            4 exit program
        3 restart input tree
        4 exit program
2 change dictionary
    1 delete exercise
    2 modify exercise
    3 add exercise
    4 restart input tree
    5 exit program
3 exit program
'''

# muscle_type = input('input muscle type you want to exercise!')
# muscle_type = muscle_type.lower()

# print(muscle_type)

# print(muscle_dict.keys())
# for muscle_key in muscle_dict.keys():
#     if muscle_key == muscle_type:
#         print(f'you have chosen {muscle_key} type')
#         for index, exercise in enumerate(muscle_dict[muscle_key], start=1):
#             print(f'{index}. {exercise}')
            
#         user_input = input("Enter the index number to select an exercise: \n")
#         #print(muscle_dict[muscle_key])
        
#         try:
#             index = int(user_input) - 1

#             # Access and print the exercise at the chosen index
#             if index >= 0 and index < len(muscle_dict[muscle_key]):
#                 print(f"The exercise at index {user_input} is: {muscle_dict[muscle_key][index]}")
#             else:
#                 print("Invalid index. Please enter a number within the range of the list.")
#         except ValueError:
#             # Handle the case where the input is not an integer
#             print("Please enter a valid integer.")
#         chosen_exercise = muscle_dict[muscle_key][index]

# number_of_sets = input('enter number of sets!')

# for set_number in range(int(number_of_sets)):
#     repetition = input('input repetition\n')
#     weight = input('input weight\n')
#     print(repetition, weight)
    

# workout_data = SHEET.worksheet('exercise').get_all_values()
# print(workout_data)

def input_muscle_data():
    '''
    Get workout input data from user
    '''
    
    muscle_type_choice = False
    while muscle_type_choice != True:
        muscle_type = input('input muscle type you want to exercise!\n')
        muscle_type = muscle_type.lower()
        
        if muscle_type in muscle_dict:
            muscle_type_choice = True
            print('True')
        else:
            print('False')
            keys_list = list(muscle_dict.keys())
            print('The muscle types you can choose are:')
            print(keys_list)
    return muscle_type

muscle_type = input_muscle_data()  
print(muscle_type)

def choose_exercise():
    for muscle_key in muscle_dict.keys():
        if muscle_key == muscle_type:
            print(f'You have chosen {muscle_key} muscle type.')
            for index, exercise in enumerate(muscle_dict[muscle_key], start=1):
                print(f'{index}. {exercise}')
            
            while True:  
                user_input = input("Enter the index number to select an exercise: \n")
                
                try:
                    index = int(user_input) - 1
                    
                    if index >= 0 and index < len(muscle_dict[muscle_key]):
                        chosen_exercise = muscle_dict[muscle_key][index]
                        print(f"The exercise at index {user_input} is: {chosen_exercise}")
                        break  
                    else:
                        print("Invalid index. Please enter a number within the range of the list.")
                except ValueError:
                    print("Please enter a valid integer.")
    return chosen_exercise

print(choose_exercise())

