import random
import tkinter as tk

window = tk.Tk()
window.title("Хто хоче стати мільйонером?")
window.geometry("1080x550")
window.configure(bg = 'lightgray')



qa = {
    'У якому році "Титанік" затонув в Атлантичному океані?': {
        'right answer': '1912', 
        'incorrect answer1': '1914',
        'incorrect answer2': '2001',
        'incorrect answer3': '1897' 
        },
    'Яка столиця Португалії?': {
        'right answer': 'Лісабон', 
        'incorrect answer1': 'Вена',
        'incorrect answer2': 'Париж',
        'incorrect answer3': 'Чилі' 
        },
    'В якій країні знаходиться Стоунхендж?': {
        'right answer': 'Великобританія', 
        'incorrect answer1': 'Китай',
        'incorrect answer2': 'Америка',
        'incorrect answer3': 'Австрія' 
        },
    'Хто винайшов рукотворні газовані напої?': {
        'right answer': 'Джозеф Пристлі', 
        'incorrect answer1': 'Антуан Лоран',
        'incorrect answer2': 'Ян Ингенхауз',
        'incorrect answer3': 'Уильям Пристли'
    }
}


def random_q():
    '''
    Random question
    '''
    global qa
    if qa:
        keys = [key for key, value in qa.items()]
        rq = random.choice(keys)
        return rq

fifty_fifty_used = False

def fifty_fifty():

    global fifty_fifty_used

    if not fifty_fifty_used:

        question = label['text']
        current_question = qa[question]
        answers = list(current_question.values())
        right_answer = current_question['right answer']
        answers.remove(right_answer)
        incorrect_answer = random.choice(answers)

        display_answers = [right_answer, incorrect_answer]
        random.shuffle(display_answers)

        button1.config(text = display_answers[0], command = lambda: check_answer(display_answers[0]))
        button2.config(text = display_answers[1], command = lambda: check_answer(display_answers[1]))

        button3.pack_forget()
        button4.pack_forget()
        
        fifty_fifty_used = True
        button5['state'] = tk.DISABLED

def friend_hand():
    
    question = label['text']
    current_question = qa[question]
    answers = list(current_question.values())
    friend_choice = random.choice(answers)
    button1.config(text = friend_choice, command = lambda: check_answer(friend_choice))

    button2.pack_forget()
    button3.pack_forget()
    button4.pack_forget()

    button6['state'] = tk.DISABLED
    button5['state'] = tk.DISABLED

def display_question():
    global label2
    if qa:
        keyq = random_q()
        question = keyq
        answers = list(qa[keyq].values())
        label.config(text = question)
        buttons = [button1, button2, button3, button4]

        random.shuffle(buttons)

        for i in range(len(answers)):
            buttons[i].config(text=answers[i], command=lambda ans=answers[i]: check_answer(ans))

        if not fifty_fifty_used:
            button5['state'] = tk.NORMAL

        label.pack()
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button6.pack()
        button7.pack_forget()
        label2.pack_forget()
        
    elif not qa:
        if balance == 1000000:
            label1 = tk.Label(window, text = "Ви мільйонер!")
            button7.pack_forget()
            label.pack_forget()
            label2.pack_forget()
            label1.pack()
        elif balance < 1000000:
            label1 = tk.Label(window, text = "Гра завершена")
            label3 = tk.Label(window, text = f"Ваш баланс: {balance}")
            label4 = tk.Label(window, text = f"Неправильні відповіді: {incorrect_answers} Правильні: {right_answers}")

            button7.pack_forget()
            label.pack_forget()
            label2.pack_forget()
            label1.pack()
            label4.pack()
            label3.pack()

balance = 0
right_answers = 0
incorrect_answers = 0   

def check_answer(selected_answer):

    global qa, label2, button7, right_answers, incorrect_answers, balance

    for key, value in qa.items():

        if selected_answer == value['right answer']:
            
            balance += 250000
            right_answers += 1

            button1.pack_forget()
            button2.pack_forget()
            button3.pack_forget()
            button4.pack_forget()
            button5.pack_forget()
            button6.pack_forget()
            label.pack_forget()
            

            label2 = tk.Label(window, text="Правильна відповідь")
            label2.pack()
            button7.pack()
            if key in qa:
                del qa[key]
            return right_answers

        elif selected_answer in [value['incorrect answer1'], value['incorrect answer2'], value['incorrect answer3']]:
            
            incorrect_answers += 1

            print(incorrect_answers)
            button1.pack_forget()
            button2.pack_forget()
            button3.pack_forget()
            button4.pack_forget()
            button5.pack_forget()
            button6.pack_forget()
            label.pack_forget()
            
            print("Неправильна відповідь!")
            label2 = tk.Label(window, text = "Неправильна відповідь!")
            label2.pack()
            button7.pack()
            if key in qa:
                del qa[key]
            return incorrect_answers

def hide_start_screen():
    label_start.pack_forget()
    button_start.pack_forget()
    label_help.pack_forget()

def start_game():
    hide_start_screen()
    display_question()

label_start = tk.Label(window, text = "Хочете стати мільйонером?")
label_help = tk.Label(window, text = "У вас є можливість використати підсказки такі як 50 на 50(1 раз) та дзвінок другу(1 раз)")
label_start.config(justify="center", font = ("Arial", 12), bg='lightgray')
label_start.pack()
label_help.pack()
button_start = tk.Button(window, text='Почати гру', command = start_game)
button_start.pack()
    
button1 = tk.Button(window, text = '', command = None)
button2 = tk.Button(window, text = '', command = None)
button3 = tk.Button(window, text = '', command = None)
button4 = tk.Button(window, text = '', command = None)
button5 = tk.Button(window, text = '50/50', command = fifty_fifty)
button6 = tk.Button(window, text = 'Дзвінок другу', command = friend_hand)
button7 = tk.Button(window, text = 'Далі', command = display_question)
button_show_balance = tk.Button(window, text = '', comman = None)
button_show_answers = tk.Button(window, text = 'Ваш баланс: ', comman = None)

button1.pack_forget()
button2.pack_forget()
button3.pack_forget()
button4.pack_forget()
button5.pack_forget()
button6.pack_forget()
          
label = tk.Label(window, text = "")
label.config(justify = "center", font = ("Arial", 18), bg = 'lightgray')
label.pack()

window.mainloop()







