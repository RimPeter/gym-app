
# Creating a Python dictionary with exercises as keys and muscle types as values

exercise_dict = {
    "Bench Press (Flat, Incline, Decline)": ["Pectorals", "Triceps", "Shoulders"],
    "Dumbbell Flyes (Flat, Incline, Decline)": ["Pectorals", "Shoulders"],
    "Chest Dips": ["Pectorals", "Triceps"],
    "Push-Ups": ["Pectorals", "Triceps", "Shoulders"],
    "Cable Crossovers": ["Pectorals"],
    "Deadlift": ["Lower Back", "Glutes", "Hamstrings", "Upper Back", "Forearms"],
    "Pull-Ups/Chin-Ups": ["Lats", "Biceps", "Shoulders"],
    "Bent-Over Rows (Barbell, Dumbbell)": ["Upper Back", "Lats", "Biceps"],
    "T-Bar Row": ["Upper Back", "Lats", "Middle Back"],
    "Lat Pulldowns": ["Lats", "Upper Back", "Biceps"],
    "Seated Cable Rows": ["Middle Back", "Lats", "Biceps"],
    "Overhead Press (Barbell, Dumbbell)": ["Shoulders", "Triceps"],
    "Lateral Raises (Dumbbell, Cable)": ["Shoulder Deltoids"],
    "Front Raises (Dumbbell, Cable)": ["Front Deltoids"],
    "Rear Delt Flyes (Dumbbell, Machine)": ["Rear Deltoids"],
    "Shrugs (Barbell, Dumbbell)": ["Trapezius"],
    "Bicep Curls (Barbell, Dumbbell, Cable)": ["Biceps"],
    "Hammer Curls": ["Biceps", "Forearm"],
    "Preacher Curls": ["Biceps"],
    "Concentration Curls": ["Biceps"],
    "EZ-Bar Curls": ["Biceps"],
    "Tricep Extensions (Skullcrushers)": ["Triceps"],
    "Tricep Pushdowns (Cable)": ["Triceps"],
    "Overhead Tricep Extension (Dumbbell, Cable)": ["Triceps"],
    "Dips": ["Triceps", "Chest"],
    "Close-Grip Bench Press": ["Triceps", "Chest"],
    "Squats (Back Squat, Front Squat, Overhead Squat)": ["Quadriceps", "Hamstrings", "Glutes", "Lower Back"],
    "Leg Press": ["Quadriceps", "Hamstrings", "Glutes"],
    "Lunges (Barbell, Dumbbell)": ["Quadriceps", "Hamstrings", "Glutes"],
    "Leg Extensions": ["Quadriceps"],
    "Hamstring Curls (Lying, Seated)": ["Hamstrings"],
    "Calf Raises (Seated, Standing)": ["Calves"],
    "Deadlifts (Traditional, Sumo, Romanian)": ["Hamstrings", "Glutes", "Lower Back", "Upper Back"],
    "Crunches": ["Abdominals"],
    "Russian Twists": ["Obliques", "Abdominals"],
    "Leg Raises (Hanging, Lying)": ["Lower Abdominals", "Hip Flexors"],
    "Planks": ["Abdominals", "Lower Back", "Shoulders"],
    "Cable Woodchoppers": ["Obliques", "Abdominals"],
    "Clean and Press": ["Shoulders", "Upper Back", "Hamstrings", "Glutes", "Quadriceps"],
    "Snatch": ["Shoulders", "Upper Back", "Hamstrings", "Glutes", "Quadriceps"],
    "Thrusters": ["Shoulders", "Quadriceps", "Glutes", "Upper Back"],
    "Kettlebell Swings": ["Hamstrings", "Glutes", "Lower Back", "Shoulders"],
    "Farmers Walk": ["Forearms", "Shoulders", "Upper Back", "Core"]
}

muscle_dict = {
    'Pectorals': [
        'Bench Press (Flat, Incline, Decline)',
        'Dumbbell Flyes (Flat, Incline, Decline)',
        'Chest Dips',
        'Push-Ups',
        'Cable Crossovers'
    ],
    'Triceps': [
        'Bench Press (Flat, Incline, Decline)',
        'Chest Dips',
        'Push-Ups',
        'Overhead Press (Barbell, Dumbbell)',
        'Tricep Extensions (Skullcrushers)',
        'Tricep Pushdowns (Cable)',
        'Overhead Tricep Extension (Dumbbell, Cable)',
        'Dips',
        'Close-Grip Bench Press'
    ],
    'Shoulders': [
        'Bench Press (Flat, Incline, Decline)',
        'Dumbbell Flyes (Flat, Incline, Decline)',
        'Push-Ups',
        'Pull-Ups/Chin-Ups',
        'Overhead Press (Barbell, Dumbbell)',
        'Planks',
        'Clean and Press',
        'Snatch',
        'Thrusters',
        'Kettlebell Swings',
        'Farmers Walk'
    ],
     'Lower Back': [
        'Deadlift',
        'Squats (Back Squat, Front Squat, Overhead Squat)',
        'Deadlifts (Traditional, Sumo, Romanian)',
        'Planks',
        'Kettlebell Swings'
    ],
    'Glutes': [
        'Deadlift',
        'Squats (Back Squat, Front Squat, Overhead Squat)',
        'Leg Press',
        'Lunges (Barbell, Dumbbell)',
        'Deadlifts (Traditional, Sumo, Romanian)',
        'Clean and Press',
        'Snatch',
        'Thrusters',
        'Kettlebell Swings'
    ],
    'Hamstrings': [
        'Deadlift',
        'Squats (Back Squat, Front Squat, Overhead Squat)',
        'Leg Press',
        'Lunges (Barbell, Dumbbell)',
        'Hamstring Curls (Lying, Seated)',
        'Deadlifts (Traditional, Sumo, Romanian)',
        'Clean and Press',
        'Snatch',
        'Kettlebell Swings'
    ],
    'Upper Back': [
        'Deadlift',
        'Bent-Over Rows (Barbell, Dumbbell)',
        'T-Bar Row',
        'Lat Pulldowns',
        'Deadlifts (Traditional, Sumo, Romanian)',
        'Clean and Press',
        'Snatch',
        'Thrusters',
        'Farmers Walk'
    ],
    'Forearms': ['Deadlift', 'Farmers Walk'],
    'Lats': [
        'Pull-Ups/Chin-Ups',
        'Bent-Over Rows (Barbell, Dumbbell)',
        'T-Bar Row',
        'Lat Pulldowns',
        'Seated Cable Rows'
    ],
    'Biceps': [
        'Pull-Ups/Chin-Ups',
        'Bent-Over Rows (Barbell, Dumbbell)',
        'Lat Pulldowns',
        'Seated Cable Rows',
        'Bicep Curls (Barbell, Dumbbell, Cable)',
        'Hammer Curls',
        'Preacher Curls',
        'Concentration Curls',
        'EZ-Bar Curls'
    ],
    'Middle Back': ['T-Bar Row', 'Seated Cable Rows'],
    'Shoulder Deltoids': ['Lateral Raises (Dumbbell, Cable)'],
    'Front Deltoids': ['Front Raises (Dumbbell, Cable)'],
    'Rear Deltoids': ['Rear Delt Flyes (Dumbbell, Machine)'],
    'Trapezius': ['Shrugs (Barbell, Dumbbell)'],
    'Forearm': ['Hammer Curls'],
    'Chest': ['Dips', 'Close-Grip Bench Press'],
    'Quadriceps': [
        'Squats (Back Squat, Front Squat, Overhead Squat)',
        'Leg Press',
        'Lunges (Barbell, Dumbbell)',
        'Leg Extensions',
        'Clean and Press',
        'Snatch',
        'Thrusters'
    ],
    'Calves': ['Calf Raises (Seated, Standing)'],
    'Abdominals': [
        'Crunches',
        'Russian Twists',
        'Planks',
        'Cable Woodchoppers'
    ],
    'Obliques': ['Russian Twists', 'Cable Woodchoppers'],
    'Lower Abdominals': ['Leg Raises (Hanging, Lying)'],
    'Hip Flexors': ['Leg Raises (Hanging, Lying)'],
    'Core': ['Farmers Walk']
}

