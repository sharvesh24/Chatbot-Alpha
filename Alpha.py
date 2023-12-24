import json 
from difflib import get_close_matches 
import datetime 
import pywhatkit
import wikipedia
import pyjokes


def load_data(file): 
    with open(file, 'r') as f:
        data= dict(json.load(f))
    return data
def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=2)

def match_(user_question, questions):
    matches= list(get_close_matches(user_question, questions, n=1, cutoff=0.6))
    return matches[0] if matches else None

def get_answer(question, data):
    for q in data["questions"]:
        if q["question"] == question:
            return q["answer"]

def alpha():
    data = dict(load_data('D://Programs//Chatbot//Chatbot//Data.json'))

    while True:
        user = input('USER: ')

        if user.lower()=='quit':
            break
        match = match_(user, [q["question"] for q in data["questions"]])

        if match:
            answer = get_answer(match, data)
            print(f'ALPHA: {answer}')
        elif 'play' in user:
            song = user.replace('play', '')
            print('ALPHA: Playing...')
            pywhatkit.playonyt(song)
        elif 'time' in user:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(f'ALPHA: {time}')
        elif 'who is' in user:
            person = user.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(f'ALPHA: {info}')
        elif 'joke' in user:
            print("ALPHA: ",pyjokes.get_joke())
        else:
            print('ALPHA: I don\'t know the answer. Can you teach me?')
            new =input('Type the answer or "skip" to skip: ')
            if new == 'skip':
                break
            else:
                data["questions"].append({'question': user, "answer": new})
                save_data('D://Programs//Chatbot//Chatbot//Data.json', data)
                print('ALPHA: Thanks! I learned a new response')
if __name__ == '__main__':
    alpha()