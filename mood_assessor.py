from pathlib import Path
import datetime

def open_file():
    filepath = Path('data','mood_diary.txt')
    f = open(filepath, encoding = 'utf-8', mode = 'a')
    return f


        
def rating_mood():
    keep_going = True
    while keep_going:
        mood = input("Hey, what is your mood today? ").lower()
        if mood in ['happy', 'relaxed', 'apathetic', 'sad', 'angry']:
            keep_going = False
            if mood =='happy':
                mood = 2
            elif mood =='relaxed':
                mood = 1
            elif mood =='apathetic':
                mood = 0
            elif mood =='sad':
                mood = -1
            elif mood =='angry':
                mood = -2
            return mood

def recording_mood():
    f = open_file()
    mood = rating_mood()
    date_today = datetime.date.today()
    date_today = str(date_today)
    f.write(f'{mood} , {date_today}\n')
    f.close()


def check_entry_today():
    date_today = datetime.date.today()
    date_today = str(date_today)
    filepath = Path('data','mood_diary.txt')
    f = open(filepath, encoding = 'utf-8', mode = 'r')
    all_lines = f.read().strip() 
    if date_today in all_lines:
        print('Sorry, you have already entered your mood today.')
        f.close()
    else:
        recording_mood()

def check_entry_correct():
    filepath = Path('data', 'mood_diary.txt')
    f = open(filepath, encoding='utf-8', mode='r')
    lines = f.readlines()
    try:
        if len(lines) >= 7:
            values = lines[-7:]
            return values
        else:
            return False
    finally:
        f.close()
 

def diagnose():
    mood_overall = check_entry_correct()
    if not mood_overall:
        return False
    clean_mood = []
    for line in mood_overall:
       parts = line.split(' , ')
       mood = int(parts[0])
       clean_mood.append(mood)
    counter_for_manic = 0
    counter_for_depressive = 0
    counter_for_schizoid = 0
    counter_for_happy = 0
    counter_for_relaxed = 0
    counter_for_apathetic = 0
    counter_for_sad = 0
    counter_for_angry = 0
    avg_mood = 0
    for mood in clean_mood:
        if mood == 2:
            counter_for_manic += 1
            counter_for_happy += 1
        elif mood == 1:
            counter_for_relaxed += 1
        elif mood == 0:
            counter_for_apathetic += 1
            counter_for_schizoid += 1
        elif mood == -1:
            counter_for_depressive += 1
            counter_for_sad += 1
        elif mood == -2:
            counter_for_angry += 1
        avg_mood += mood

    avg_mood = round(avg_mood / 7)

    if counter_for_manic >= 5:
        diagnosis = "manic"
    elif counter_for_depressive >= 4:
        diagnosis = "depressive"
    elif counter_for_schizoid >= 6:
        diagnosis = "schizoid"
    else:
        if avg_mood == 2:
            diagnosis = "happy"
        elif avg_mood == 1:
            diagnosis = "relaxed"
        elif avg_mood == 0:
            diagnosis = "apathetic"
        elif avg_mood == -1:
            diagnosis = "sad"
        elif avg_mood == -2:
            diagnosis = "angry"
    
    print(f"Your diagnosis: {diagnosis}!")

def assess_mood():
    check_entry_today()
    diagnose()


