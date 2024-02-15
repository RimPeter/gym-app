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


def input_muscle_data():
    '''
    Input a muscle type, ensures it's valid per muscle_dict, and returns the choice.
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
    '''
    select an exercise based on their chosen muscle type, validating choice against muscle_dict.
    '''
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
    '''
    Number of sets to perform, ensuring a positive integer is provided.
    '''
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
    '''
    Updates 'cumulative' worksheet with exercise and total weight, avoiding duplicates and summing weights.
    '''
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
    This function is used for "repetition" input and "weight" input inside exerecise_values() function
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

def exercise_values():
    '''
    Takes workout data (exercise, sets, reps, weight) to the 'workout' sheet, and updates cumulative sums in 'cumulative' sheet.
    Inputs are integers and updates are based on valid, non-duplicate exercise data.
    '''
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
    


def print_my_workout(data):
    '''
    Print all data for chosen exercise 
    '''
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



def print_sum_of_all_weights():
    '''
    Print the sum of all weights for each exercise done
    '''
    for row in cumulative_data:
        print(row)
        
def remove_cumulative(rows_to_delete):
    '''
    Reduces the cumulative total by the 5th column (sum of weights) values of workout worksheet
    '''
    for row in rows_to_delete:
        exercise_name = row[0]
        weight_to_subtract = int(row[4])
        
        cumulative_exercises = cumulative.col_values(1)
        if exercise_name in cumulative_exercises:
            row_index = cumulative_exercises.index(exercise_name) + 1
            current_weight = int(cumulative.cell(row_index, 2).value)
            new_weight = max(0, current_weight - weight_to_subtract)
            cumulative.update_cell(row_index, 2, new_weight)
        
def delete_recent_rows_of_workout():
    '''
    Delete recent rows, number of rows deleted are defined by input
    '''
    workout_data = workout.get_all_values()
    total_rows = len(workout.get_all_values())
    print(f"Current total number of rows: {total_rows}")
    num_rows_to_delete = int(input("Enter the number of last rows you want to delete: "))

    if num_rows_to_delete <= 0 or num_rows_to_delete > total_rows:
        print("Invalid number of rows to delete. Please enter a positive number less than or equal to the total number of rows.")
        return

    start_row = total_rows - num_rows_to_delete + 1
    rows_to_delete = workout.get(f"A{start_row}:E{total_rows}")
    remove_cumulative(rows_to_delete)
    workout.delete_rows(start_row, total_rows)
    print(f"Deleted the last {num_rows_to_delete} rows.")
      
def main():
    '''
    Options for user to decide which function to trigger
    '''
    while True:
        print("\nChoose an option:")
        print("1. Enter workout data")
        print("2. Print my workout")
        print("3. Print sum of all weights")
        print("4. Delete recent inputs")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            exercise_values()
        elif choice == '2':
            print_my_workout(workout_data)
        elif choice == '3':
            print_sum_of_all_weights()
        elif choice == '4':
            delete_recent_rows_of_workout()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4).")

main()


