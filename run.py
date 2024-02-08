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

with open('muscledict.json', 'r') as file:
    muscle_dict = json.load(file)


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

def number_of_sets():
    while True:
        try:
            number_of_set = int(input('Enter number of sets!\n'))
            if number_of_set > 0:
                return number_of_set
            else:
                print("Please enter a number greater than zero.")
        except ValueError:
            print("Please enter a valid integer.")

#number_of_set = number_of_sets()
def exerecise_values():
    for set_number in range(int(number_of_sets())):
        repetition = input('input repetition\n')
        weight = input('input weight\n')
        print(repetition, weight)
        
exerecise_values()