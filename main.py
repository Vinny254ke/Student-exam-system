from tkinter import *
from tkinter import Tk, simpledialog, messagebox
from tkinter.ttk import Progressbar, Combobox
from PIL import Image, ImageTk
import sqlite3
import pickle


con = sqlite3.connect('systeminfo.db')
c = con.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, marks TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS analyse (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, answer TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS questions (id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, marks TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS teachers (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS results (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, marks TEXT)")
con.commit()

import requests
from bs4 import BeautifulSoup

import random
import datetime




def define_word(word):
    try:
        url = f"https://www.dictionary.com/browse/{word}"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            definition = soup.find('meta', attrs={'name': 'description'})['content']
            messagebox.showinfo("Results", definition)
        else:
            messagebox.showinfo("Results", "Failed to fetch definition")
    except:
        messagebox.showinfo("Results", "No internet connection..connect and try again")

def translate(text, target_lang='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_lang)
    messagebox.showinfo("Results", translation.text)

def get_weather_forecast(city):
    # You'll need to replace 'YOUR_API_KEY' with a valid API key from a weather API provider
    try:
        api_key = 'YOUR_API_KEY'
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            description = data['weather'][0]['description']
            temperature = data['main']['temp']
            messagebox.showinfo("Results", f"Weather forecast for {city}: {description}, Temperature: {temperature}°C")
        else:
            messagebox.showinfo("Results", "Failed to fetch weather forecast")
    except:
        messagebox.showinfo("Results", "No internet connection..connect and try again")

def get_news_headlines():
    try:
        url = "https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'xml')
            headlines = soup.find_all('title')[1:]  # Skip the first title (feed title)
            for idx, headline in enumerate(headlines, start=1):
                messagebox.showinfo("Results", f"{idx}. {headline.text}")
        else:
            messagebox.showinfo("Results", "Failed to fetch news headlines")
    except:
        messagebox.showinfo("Results", "No internet connection..connect and try again")

def get_random_joke():
    try:
        url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url)
        if response.status_code == 200:
            joke_data = response.json()
            messagebox.showinfo("Results", joke_data['setup'])
            messagebox.showinfo("Results", joke_data['punchline'])
        else:
            messagebox.showinfo("Results", "Failed to fetch random joke")
    except:
        messagebox.showinfo("Results", "No internet connection..connect and try again")

def bot_command(command):
    if command == 'show menu':
        show_menu()
    elif command == 'help':
        show_help()
    elif command == 'quit':
        exit_bot()
    elif command == 'greet':
        greet()
    elif command.startswith('echo '):
        echo(command)
    elif command == 'time':
        show_time()
    elif command == 'about':
        about_app()
    elif command == 'date':
        show_date()
    elif command == 'calculate':
        calculate()
    elif command.startswith('define '):
        define_word(command[7:])
    elif command.startswith('translate '):
        text = command[10:]
        translate(text)
    elif command.startswith('weather '):
        city = command[8:]
        get_weather_forecast(city)
    elif command == 'news':
        get_news_headlines()
    elif command == 'joke':
        try:
            get_random_joke()
        except:
            if "joke" in input1.lower():
                messagebox.showinfo("Results", random.choice(jokes))
    elif command == 'exit':
        exit_bot()
    else:
        if "fact" in input1.lower():
            messagebox.showinfo("Results", random.choice(facts))
        else:
            messagebox.showinfo("Results", "I'm sorry, I didn't understand that. Type 'help' or 'show menu' to see available commands?")


def show_menu():
    menu = """
    Available commands:
    [1.] Show menu
    [2.] Help
    [3.] Greet
    [4.] Echo <message>
    [5.] Time
    [6.] Date
    [7.] Calculate
    [8.] Exit
    [9.] Define_word
    [10.] Translate
    [11.] Weather_forecast
    [12.] News_headline
    [13.] Jokes
    [14.] About
    """
    messagebox.showinfo("Results", menu)

def show_help():
    help_text = """
    Here are some available commands: 
    - 'show menu': Display the bot menu
    - 'help': Show help information
    - 'greet': Greet the user
    - 'echo <message>': Echo back the provided message
    - 'time': Show the current time
    - 'date': Show the current date
    - 'calculate': Perform simple arithmetic calculations
    - 'about': Gives you the overview how the system works
    - 'exit': Exit the bot
    *****************************************
        Requires internet connection
    
    - 'define': Defines words
    - 'calculate': Get calculations of any expression
    - 'weather': Get the current weather forecast
    - 'news': Get latest news headlines
    - 'jokes': Get ribcracking jokes
    """
    messagebox.showinfo("Results", help_text)

def greet():
    messagebox.showinfo("Results", "Hello! How can I assist you today?")
def about_app():
    about = '''This is a system developed by Vincent Odhiambo. A 18yrs old self
    taught python programmer. This is the first version and it may have limited
    features. The current one uses multiple windows display but in future, we would
    advance a bit and use a single window. Incase one of the windows is not displaying, check it through the
    taskbar. The aim of this project was to reduce paperwork in school.
    To start using the system, you must acquire the admin details to register
    yourself. Check the readme.txt file. The entry fields are for all the access levels.
    Note: Some features may not work properly, ignore.
    '''
    messagebox.showinfo("Results", about)
def echo(command):
    message = command[5:]  # Extract message from command
    messagebox.showinfo("Results", message)

def show_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    messagebox.showinfo("Results", current_time)

def show_date():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    messagebox.showinfo("Results", current_date)

def calculate():
    expression = simpledialog.askstring("Results", "Enter expression to calculate: ")
    try:
        result = eval(expression)
        messagebox.showinfo("Result:", result)
    except Exception as e:
        messagebox.showinfo("Results", e)

# Define responses for different types of entertainment
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you get when you cross a snowman and a vampire? Frostbite!",
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!"
]

facts = [
    "The shortest war in history lasted only 38 minutes. It was between Britain and Zanzibar in 1896.",
    "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion of the metal.",
    "Peanuts are not nuts. They are legumes!"
]

def exit_bot():
    messagebox.showinfo("Results", "Goodbye!")
    system.destroy()


def bot_access(users_input):
    bot_command(users_input)
#bot_access('help')
# Interactive command loop
def wait():
    while True:
        main()
        user_input = input('\n' + "Enter command: ")
        bot_command(user_input)



###############################################################################

def login():
    global username4
    username4 = name_entry.get()
    password = password_entry.get()
    if username4 and password:
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username4, password))
        loaded_users = c.fetchone()
        if loaded_users:
            messagebox.showinfo("SUCCESS", "You have successfully logged in")
            name_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            main_window()
            
        else:
            messagebox.showerror("INVALID DETAILS", "No such account..Please contact your admin to register first")
            name_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
    else:
        messagebox.showerror("NO INPUT", "Please provide username and password")
        

def register():
    password = password_entry2.get()
    username = name_entry2.get()
    if username and password:
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        loaded_users = c.fetchall()
        if loaded_users:
            messagebox.showerror("INVALID", "Username and password already exist")
            name_entry2.delete(0, 'end')
            password_entry2.delete(0, 'end')
        else:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            c.execute("INSERT INTO analyse (username, answer) VALUES (?, ?)", (username, '##########')) 
            con.commit()                 
            messagebox.showinfo("SUCCESS", "User saved successfully")
            window1.destroy()
    else:
        messagebox.showerror("INPUT ERROR", "Please provide complete details")

def register_teacher():
    password = password_entry2.get()
    username = name_entry2.get()
    if username and password:
        c.execute("SELECT * FROM teachers WHERE username=? AND password=?", (username, password))
        loaded_users = c.fetchall()
        if loaded_users:
            messagebox.showerror("INVALID", "Username and password already exist")
            name_entry2.delete(0, 'end')
            password_entry2.delete(0, 'end')
        else:
            c.execute("INSERT INTO teachers (username, password) VALUES (?, ?)", (username, password))
            con.commit()                 
            messagebox.showinfo("SUCCESS", "User saved successfully")
            window1.destroy()
    else:
        messagebox.showerror("INPUT ERROR", "Please provide complete details")

def back3():
    window3.destroy()

def attempt_question():
    c.execute("SELECT question FROM questions")
    questions = c.fetchall()
    if questions:
        for question1 in questions:
            question = question1[0]
            yesno = messagebox.askyesno("Do you want to attempt this question", question)
            if yesno > 0:
                answer2 = simpledialog.askstring("QUESTION", question)
                c.execute("UPDATE analyse SET answer = ? WHERE username = ?", (answer2, username4))
                con.commit()
    else:
        messagebox.showinfo("ERROR", "No questions available at the moment")


def Keep():
    question = name_entry4.get()
    marks = marks_entry4.get()
    if question and marks:
        c.execute("INSERT INTO questions (question, marks) VALUES(?, ?)", (question, marks))
        messagebox.showinfo('Success', 'Question uploaded successfully')
        question = name_entry4.delete(0, 'end')
        marks = marks_entry4.delete(0, 'end')
    else:
        messagebox.showinfo('Invalid', 'Please provide both inputs')        
def add_questions():
    window2 = Toplevel()
    window2.geometry("500x600")
    window2.resizable(0, 0)
    window2.configure(bg="grey")
    window2.title("QUESTIONS window")
    question_label4 = Label(window2, text = 'QUESTION:')
    question_label4.place(x=80, y=200)
    global name_entry4
    name_entry4 = Entry(window2, textvariable = "StringVar40()", font = ('arial', 15, 'bold'))
    name_entry4.place(x=180, y=200)

    marks_label4 = Label(window2, text = 'MARKS:')
    marks_label4.place(x=80, y=270)
    global marks_entry4
    marks_entry4 = Entry(window2, textvariable = "StringVar6()", font = ('arial', 15, 'bold'))
    marks_entry4.place(x=180, y=270)
    proceedbtn2 = Button(window2, text="Proceed", command=Keep)
    proceedbtn2.place(x=230, y=350)
    

def checkout():
    radio = IntVar()
    selected = radio.get()
    if selected == 1:
        messagebox.showinfo("verified", "Correct option chosen")
        pass
    
    elif selected == 2:
        messagebox.showinfo("verified", "Incorrect option chosen")
        pass
    else:
        messagebox.showinfo("Invalid", "No option chosen")
        pass
from tkinter import END

def fetch_answer():
    selected_username = combo_box.get()
    answer_area.delete(1.0, END)  # Clear previous content

    c.execute("SELECT question, answer FROM users INNER JOIN questions ON users.id = questions.id WHERE username = ?", (selected_username,))
    answers = c.fetchall()
    if answers:
        for question, answer in answers:
            answer_area.insert(END, f"Question: {question}\nAnswer: {answer}\n\n")
    else:
        answer_area.insert(END, "No answers available for this user.")



def teachers_window():
    global window3
    window3 = Toplevel()
    window3.geometry("1350x800")
    window3.title("Teachers_window")
    window3.configure(bg="#2e2e2e")
    label3 = Label(window3, text="Teachers Mode", font = ('algerian', 50, 'bold'), relief=RIDGE)
    label3.place(x=350, y=10)

    c.execute("SELECT username FROM users")
    current_users = c.fetchall()
    global combo_box
    combo_box = Combobox(window3, values=[user[0] for user in current_users])
    combo_box.place(x=500, y=150)
    fetch_button = Button(window3, text="Fetch Answer", command=fetch_answer)
    fetch_button.place(x=600, y=200)
    global answer_area
    answer_area = Text(window3, wrap='word', height=10, width=50)
    answer_area.place(x=500, y=250)


    button8 = Button(window3, text="Add question", bg="grey", bd = 10, command=add_questions)
    button8.place(x=750, y=150)
    back_button = Button(window3, text="Back", command=back3)
    back_button.place(x=570, y=480)
    radio = IntVar()
    marking_radio1 = Radiobutton(window3, text="Correct", variable=radio, value=1, bg="blue", fg="white", font=("Helvetica", 10))
    marking_radio1.place(x=600, y=600)

    marking_radio2 = Radiobutton(window3, text="Incorrect", variable=radio, value=2, bg="blue", fg="white", font=("Helvetica", 10))
    marking_radio2.place(x=680, y=600)

    proceed_button = Button(window3, text="Proceed", command=checkout)
    proceed_button.place(x=600, y=650)

    


def teachers_mode():
    global username4
    username4 = name_entry.get()
    password = password_entry.get()
    if username4 and password:
        c.execute("SELECT * FROM teachers WHERE username=? AND password=?", (username4, password))
        loaded_users = c.fetchone()
        if loaded_users:
            messagebox.showinfo("SUCCESS", "You have successfully logged in")
            name_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            teachers_window()
            
        else:
            messagebox.showerror("INVALID DETAILS", "No such account..Please contact your admin to register first")
            name_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
    else:
        messagebox.showerror("NO INPUT", "Please provide username and password")
    
def exit_system():
    system.destroy()

def back():
    admin.destroy()

def back2():
    window.destroy()




def add_new_user():
    global window1
    window1 = Toplevel()
    window1.geometry("500x600")
    window1.resizable(0, 0)
    window1.configure(bg="grey")
    window1.title("Registration window")
    name_label2 = Label(window1, text = 'NAME:')
    name_label2.place(x=80, y=200)
    global name_entry2
    name_entry2 = Entry(window1, textvariable = "StringVar10()", font = ('arial', 15, 'bold'))
    name_entry2.place(x=180, y=200)
   
    password_label2 = Label(window1, text = "PASSWORD:")
    password_label2.place(x=80, y=240)
    global password_entry2
    password_entry2 = Entry(window1, show='*', textvariable="StringVar67()", font = ('arial', 15, 'bold'))
    password_entry2.place(x=200, y=240)
    
    title2_label = Label(window1, text = 'REGISTER NEW STUDENT', bg="grey", font = ('arial', 20, 'bold'))
    title2_label.place(x=80, y=140)
    button6 = Button(window1, text="Register", command = register)
    button6.place(x=170, y=300)


def add_new_teacher():
    global window1
    window1 = Toplevel()
    window1.geometry("500x600")
    window1.resizable(0, 0)
    window1.configure(bg="grey")
    window1.title("Registration window")
    name_label2 = Label(window1, text = 'NAME:')
    name_label2.place(x=80, y=200)
    global name_entry2
    name_entry2 = Entry(window1, textvariable = "StringVar61()", font = ('arial', 15, 'bold'))
    name_entry2.place(x=180, y=200)
   
    password_label2 = Label(window1, text = "PASSWORD:")
    password_label2.place(x=80, y=240)
    global password_entry2
    password_entry2 = Entry(window1, show='*', textvariable="StringVar11()", font = ('arial', 15, 'bold'))
    password_entry2.place(x=200, y=240)
    
    title2_label = Label(window1, text = 'REGISTER NEW TEACHER', bg="grey", font = ('arial', 20, 'bold'))
    title2_label.place(x=80, y=140)
    button6 = Button(window1, text="Register", command = register_teacher)
    button6.place(x=170, y=300)        

def reset_database():
    try:
        # Drop existing tables
        c.execute("DROP TABLE IF EXISTS users")
        c.execute("DROP TABLE IF EXISTS questions")
        c.execute("DROP TABLE IF EXISTS teachers")
        c.execute("DROP TABLE IF EXISTS results")
        
        # Recreate tables
        c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, answer TEXT)")
        c.execute("CREATE TABLE IF NOT EXISTS questions (id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, marks TEXT)")
        c.execute("CREATE TABLE IF NOT EXISTS teachers (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
        c.execute("CREATE TABLE IF NOT EXISTS results (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, score TEXT)")
        
        con.commit()
        messagebox.showinfo("Database Reset", "Database has been reset to default.")
    except Exception as e:
        messagebox.showerror("Database Reset Error", f"An error occurred: {str(e)}")

def admin_access():
    if name_entry.get() == "admin" and password_entry.get() == "password":
        global admin
        admin = Toplevel()
        admin.title("Admin_window")
        admin.geometry("1350x800+0+0")
        admin.resizable(0, 0)
        admin.configure(bg="#2e2e2e")
        #image = Image.open("photo4.jpg")
        #image = image.resize((1300, 800))
        #admin_image = ImageTk.PhotoImage(image)

        #back_label = Label(admin, image=admin_image)
        #back_label.place(x=0, y=0, relwidth=1, relheight=1)
        back_button = Button(admin, text="Back", bg="grey", bd = 10, command=back)
        back_button.place(x=580, y=500)
        title2 = Label(admin, text = "ADMIN MODE", font = ("arial", 50, "bold"), bg = "grey", relief=GROOVE)
        title2.place(x=400, y=10)

       ##############################################################################
        button4 = Button(admin, text="Register student", bg="grey", bd = 10, command=add_new_user)
        button4.place(x=560, y=400)

        button5 = Button(admin, text="Reset system to default", bg="grey", bd = 10, command = reset_database)
        button5.place(x=350, y=400)
        button7 = Button(admin, text="Register teacher", bg="grey", bd = 10, command=add_new_teacher)
        button7.place(x=760, y=400)

        #button7 = Button(admin, text="Add Announcement", bg="grey", bd = 10, command=add_announcement)
        #button7.place(x=870, y=400)

        
        button7 = Button(admin, text="Change password", bg="grey", bd = 10)
        button7.place(x=550, y=300)
        #name_label = Label(admin, text = 'NAME', bd = 4, font = ('arial', 20, 'bold'), relief = SUNKEN)
        #name_label.place(x=400, y=200)


        #name_entry1 = Entry(admin, textvariable = "StringVar2()", font = ('arial', 15, 'bold'), bd = 10)
        #name_entry1.place(x=500, y=200)

        #password_label1 = Label(admin, text = "PASSWORD", bd=4, font = ('arial', 20, 'bold'), relief = SUNKEN)
        #password_label1.place(x=400, y=260)

        #password_entry1 = Entry(admin, textvariable="StringVar()", font = ('arial', 15, 'bold'), bd = 10)
        #password_entry1.place(x=620, y=260)
        name_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
    else:
        messagebox.showerror("INCORRECT", "Please provide valid details ")

    
def interact_with_bot():
    global input1
    input1 = simpledialog.askstring('Developers BOT', "Enter command or type 'help' to see available commands")
    bot_command(input1)
def main_window():
    global window
    window = Toplevel()
    window.geometry("1350x800+0+0")
    window.title("Main_window")
    window.configure(bg="#2e2e2e")
    #frame1 = Frame(window, width=10, bg="white")
    #frame1.pack(side=BOTTOM)
    label3 = Label(window, text="Students Mode", font = ('algerian', 50, 'bold'), relief=RIDGE)
    label3.place(x=360, y=10)


    results_button = Button(window, text="Results",bd=5, relief=RIDGE)
    results_button.place(x=720, y=400)

    
    attempt_button = Button(window, text="Attempt questions", bd=5, relief=RIDGE, command = attempt_question)
    attempt_button.place(x=430, y=400)
    
    back2_button = Button(window, text = "Back", width=8, bd=5, command = back2)
    back2_button.place(x=600, y=480)
system = Tk()
system.title("DIGITAL EXAMINATION SYSTEM")
system.configure()
system.geometry("1350x800+0+0")
system.resizable(0, 0)

bar = Progressbar(system, length=500)
bar['value'] = 200

image = Image.open("photo5.jpg")
image = image.resize((1350, 800))
background_image = ImageTk.PhotoImage(image)
background_label = Label(system, image = background_image)
background_label.place(x=0, y=0, relwidth=1, relheight = 1)

titleframe = Frame(system, bg="grey", relief=RIDGE)
titleframe.pack(side=BOTTOM)


title1 = Label(system, text = "DIGITAL EXAMINATION SYSTEM", font = ("arial", 50, "bold"), bg = "grey", relief=GROOVE)
title1.place(x=100, y=10)

title7 = Label(system, text = "Provide the required credentials and click on the account below", font = ("arial", 20, "bold"), bg = "red")
title7.place(x=200, y=100)


button1 = Button(system, text="Student Access", bg="grey", bd = 5, command=login)
button1.place(x=580, y=350)

#button2 = Button(system, text="Register", bg="grey", bd = 10, command=register)
#button2.place(x=480, y=350)
##############################################################################

name_label = Label(system, text = 'NAME', bd = 4, font = ('arial', 20, 'bold'), relief = SUNKEN)
name_label.place(x=400, y=200)

name_entry = Entry(system, textvariable = "StringVar2()", font = ('arial', 15, 'bold'), bd = 10)
name_entry.place(x=500, y=200)
name_entry.focus()

bot_button = Button(system, text = 'MENU', width = 5, bd = 5, font = ('arial', 10, 'bold'), command = interact_with_bot)
bot_button.place(x=1250, y=20)



password_label = Label(system, text = "PASSWORD", bd=4, font = ('arial', 20, 'bold'), relief = SUNKEN)
password_label.place(x=400, y=260)

password_entry = Entry(system, show = '*', textvariable="StringVar()", font = ('arial', 15, 'bold'), bd = 10)
password_entry.place(x=580, y=260)
password_entry.focus()
admin_access = Button(system, text = "Admin Access", bg="grey", bd=5, command=admin_access)
admin_access.place(x=580, y=450)

admin_access = Button(system, text = "Teachers Access", bg="grey", bd=5, command=teachers_mode)
admin_access.place(x=570, y=510)

exit_button = Button(system, text="Exit system", bg="black", fg = 'red', bd=5, command=exit_system)
exit_button.place(x=590, y=580)



footer1_label = Label(system, text="Developed by Vinnytech. Incase of any enquires or feedback contact 0784102855 or email me at petertom13249@gmail.com", font = ("latin", 10))
footer1_label.place(x=320, y=670)
footer2_label = Label(system, text = 'Version 1.0.2')
footer2_label.place(x=600, y=700)

if __name__ == '__main__':
    messagebox.showinfo('WELCOME', 'Visit menu option to learn more. Thankyou.')
    system.mainloop()
    con.close()
