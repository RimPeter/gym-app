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
workout_data = workout.get_all_values()

cumulative = SHEET.worksheet('cumulative')
cumulative_data = cumulative.get_all_values()



# Creating a Python dictionary with exercises as keys and muscle types as values
with open('exercisedict.json', 'r') as file:
    exercise_dict = json.load(file)

with open('muscledict.json', 'r') as file:
    muscle_dict = json.load(file)



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

def choose_exercise():
    muscle_type = input_muscle_data() 
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

def update_cumulative(chosen_exercise, total_weight):
    cumulative_exercises = cumulative.col_values(1)
    if chosen_exercise not in cumulative_exercises:
        cumulative.append_row([chosen_exercise, total_weight])
    else:
        row_number = cumulative_exercises.index(chosen_exercise) + 1
        current_value = cumulative.cell(row_number, 2).value
        new_value = int(current_value) + total_weight if current_value.isdigit() else total_weight
        cumulative.update_cell(row_number, 2, new_value)

def get_integer_input(prompt):
    '''
    For "repetition" input and "weight" input inside exerecise_values() function
    '''
    while True:
        try:
            user_input = int(input(prompt))
            if user_input > 0:
                return user_input
            else:
                print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def exerecise_values():
    chosen_exercise = choose_exercise()
    total_weight = 0
    sets = get_integer_input('Enter the number of sets:\n')
    for set_number in range(sets):
        repetition = get_integer_input(f'Input repetition for set {set_number + 1}:\n')
        weight = get_integer_input(f'Input weight for set {set_number + 1} (in kg):\n')
        each_set = chosen_exercise, int(set_number+1), int(repetition), int(weight), int(repetition)*int(weight)
        workout.append_row(each_set)
        print(f"Set {set_number + 1}: Repetitions = {repetition}, Weight = {weight}kg")
        total_weight += repetition * weight
    update_cumulative(chosen_exercise, total_weight)
    
exerecise_values()

def print_my_workout(data):
    each_exercise = list(set(exercise[0] for exercise in data[1:]))
    each_exercise.sort()  

    print("Select an exercise type to print:")
    for index, exercise in enumerate(each_exercise, start=1):
        print(f"{index}. {exercise}")

    try:
        choice_index = int(input('Enter the index number of the workout to print:\n')) - 1
        chosen_exercise = each_exercise[choice_index]
    except (ValueError, IndexError):
        print("Invalid selection. Please enter a valid index number.")
        return
    print(data[0])

    for exercise in data[1:]:
        if exercise[0] == chosen_exercise:
            print(exercise)

#print_my_workout(workout_data)

def print_sum_of_all_weights():
    for row in cumulative_data:
        print(row)
        
#print_sum_of_all_weights()

