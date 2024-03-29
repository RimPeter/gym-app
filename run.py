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


with open('exercisedict.json', 'r') as file:
    exercise_dict = json.load(file)

with open('muscledict.json', 'r') as file:
    muscle_dict = json.load(file)


def input_muscle_data():
    '''
    Input muscle type, check validity, and return choice.
    '''
    muscle_type_choice = False
    while muscle_type_choice is not True:
        muscle_type = input(
            '\nPlease, input muscle type you want to exercise!\n'
            )
        muscle_type = muscle_type.lower()
        if muscle_type in muscle_dict:
            muscle_type_choice = True
        else:
            keys_list = list(muscle_dict.keys())
            print('\nThe muscle types you can select are:\n')
            for i in range(0, len(keys_list), 5):  #Process in chunks of 5
                print(', '.join(keys_list[i:i+5]))
    return muscle_type


def select_exercise():
    '''
    Select exercise based on muscle type; validate choice.
    '''
    muscle_type = input_muscle_data()
    for muscle_key in muscle_dict.keys():
        if muscle_key == muscle_type:
            print(f'\nYou have selected {muscle_key} muscle type.')
            for index, exercise in enumerate(muscle_dict[muscle_key], start=1):
                print(f'{index}. {exercise}')
            while True:
                user_input = input("Please select index number for exercise: \n")
                try:
                    index = int(user_input) - 1
                    if index >= 0 and index < len(muscle_dict[muscle_key]):
                        selected_exercise = muscle_dict[muscle_key][index]
                        print(f"\nThe selected exercise is: {selected_exercise}")
                        break
                    else:
                        print("\nInvalid index.")
                        print("Select within the range of the list.")
                except ValueError:
                    print("\nPlease enter a valid integer.")
    return selected_exercise


def number_of_sets():
    '''
    Get number of sets; ensure positive integer.
    '''
    while True:
        try:
            number_of_set = int(input('\nEnter number of sets!\n'))
            if number_of_set > 0:
                return number_of_set
            else:
                print("\nPlease enter a number greater than zero.")
        except ValueError:
            print("\nPlease enter a valid integer.")


def update_cumulative(selected_exercise, total_weight):
    '''
    Update 'cumulative' sheet with exercise/weight.
    '''
    cumulative_exercises = cumulative.col_values(1)
    if selected_exercise not in cumulative_exercises:
        cumulative.append_row([selected_exercise, total_weight])
    else:
        row_number = cumulative_exercises.index(selected_exercise) + 1
        current_value = cumulative.cell(row_number, 2).value
        if current_value.isdigit():
            new_value = int(current_value) + total_weight
        else:
            new_value = total_weight

        cumulative.update_cell(row_number, 2, new_value)


def get_integer_input(prompt):
    '''
    Get integer input for repetitions/weight.
    '''
    while True:
        try:
            user_input = int(input(prompt))
            if user_input > 0:
                return user_input
            else:
                print("\nPlease enter a number greater than zero.")
        except ValueError:
            print("\nInvalid input. Please enter a valid integer.")


def exercise_values():
    '''
    Record workout data and update 'cumulative' sheet.
    '''
    selected_exercise = select_exercise()
    total_weight = 0
    sets = get_integer_input('Enter the number of sets:\n')
    for set_number in range(sets):
        rep = get_integer_input(
            f'Input repetition for set {set_number + 1}:\n')
        weight = get_integer_input(
            f'Input weight for set {set_number + 1} (in kg):\n')
        each_set = (
            selected_exercise,
            int(set_number+1),
            int(rep),
            int(weight),
            int(rep)*int(weight)
            )
        workout.append_row(each_set)
        print(
            f"Set {set_number + 1}: Repetitions = {rep}, Weight = {weight}kg"
            )
        total_weight += rep * weight
    update_cumulative(selected_exercise, total_weight)


def update_exercise_worksheet():
    '''
    Retrieves and returns the current data from the 'exercise' or 'cumulative'
    worksheet. These functions are used to refresh the local representation of
    worksheet data, ensuring the script works with the most up-to-date
    information from the Google Sheet.
    '''
    workout = SHEET.worksheet('exercise')
    exercise_data = workout.get_all_values()
    return exercise_data


def update_cumulative_worksheet():
    '''
    Retrieves and returns the current data from the 'exercise' or 'cumulative'
    worksheet. These functions are used to refresh the local representation of
    worksheet data, ensuring the script works with the most up-to-date
    information from the Google Sheet.
    '''
    cumulative = SHEET.worksheet('cumulative')
    cumulative_data = cumulative.get_all_values()
    return cumulative_data


def print_my_workout():
    '''
    Print workout data for selected exercise.
    '''
    data = update_exercise_worksheet()
    each_exercise = list(set(exercise[0] for exercise in data[1:]))
    each_exercise.sort()

    print("\nSelect an exercise type to print:")
    for index, exercise in enumerate(each_exercise, start=1):
        print(f"{index}. {exercise}")

    try:
        choice_index = int(input(
            'Enter the index number of the workout to print:\n')) - 1
        selected_exercise = each_exercise[choice_index]
    except (ValueError, IndexError):
        print("\nInvalid selection. Please enter a valid index number.")
        return
    print(data[0])

    for exercise in data[1:]:
        if exercise[0] == selected_exercise:
            print(exercise)


def print_sum_of_all_weights():
    '''
    Print total weights for all exercises.
    '''
    cumulative_data = update_cumulative_worksheet()
    for row in cumulative_data:
        print(row)


def remove_cumulative(rows_to_delete):
    '''
    This function adjusts the cumulative totals in the 'cumulative'
    worksheet by subtracting the weights specified in the rows.
    If the new cumulative weight of an exercise drops to zero,
    the corresponding row is deleted from the worksheet.
    '''
    for row in rows_to_delete:
        exercise_name = row[0]
        weight_to_subtract = int(row[4])
        cumulative_exercises = cumulative.col_values(1)
        if exercise_name in cumulative_exercises:
            row_index = cumulative_exercises.index(exercise_name) + 1
            current_weight = int(cumulative.cell(row_index, 2).value)
            new_weight = max(0, current_weight - weight_to_subtract)
            # If new_weight is zero, delete the row.
            if new_weight == 0:
                cumulative.delete_rows(row_index)
            else:
                cumulative.update_cell(row_index, 2, new_weight)


def delete_recent_rows_of_workout():
    '''
    Delete recent rows based on user input.
    '''
    total_rows = len(workout.get_all_values())
    print(f"Current total number of rows: {total_rows}")
    num_rows_to_delete = int(input(
        "Enter the number of last rows you want to delete: "))

    if num_rows_to_delete <= 0 or num_rows_to_delete > total_rows:
        print("Invalid number of rows to delete.")
        print("Please enter a positive number less than")
        print("or equal to the total number of rows.")
        return

    start_row = total_rows - num_rows_to_delete + 1
    rows_to_delete = workout.get(f"A{start_row}:E{total_rows}")
    remove_cumulative(rows_to_delete)
    workout.delete_rows(start_row, total_rows)
    print(f"Deleted the last {num_rows_to_delete} rows.")


def main():
    '''
    Main menu for user actions.
    '''
    while True:
        print("\n******************")
        print("GYM APP: MAIN MENU")
        print("******************\n")
        print("Please, select from the folowing 5 options:")
        print("1. Enter my workout data")
        print("2. Print my workout data")
        print("3. Print sum of all weights for each exercise")
        print("4. Delete recent inputs")
        print("5. Exit")

        choice = input("Enter option (1/2/3/4/5): \n")

        if choice == '1':
            exercise_values()
        elif choice == '2':
            print_my_workout()
        elif choice == '3':
            print_sum_of_all_weights()
        elif choice == '4':
            delete_recent_rows_of_workout()
        elif choice == '5':
            print("\nExiting program.")
            break
        else:
            print("\nInvalid choice. Please enter a valid option (1/2/3/4/5).")


main()
