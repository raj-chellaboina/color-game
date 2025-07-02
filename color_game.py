from tkinter import *
import random
import pygame


colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']

score=0
time=30
def correct():
    sound_file= "C:\\Users\\Raj CH\\Downloads\\correct-choice-43861.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
def wrong():
    sound_file= "C:\\Users\\Raj CH\\Downloads\\negative_beeps-6008.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
def victory():
    sound_file= "C:\\Users\\Raj CH\\Downloads\\success-fanfare-trumpets-6185.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def poorperformence():
    sound_file= "C:\\Users\\Raj CH\\Downloads\\buzzer-or-wrong-answer-20582.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def sound():
    sound_file= "C:\\Users\\Raj CH\\Downloads\\Pubg Theme song ! Pubg Remix.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def start_game(event):
    
    but.destroy()
    e.config(bg="white")
    if time==30:
        count_down()
    next_color()

def next_color():
    

    global score
    global time
    if time>0:
       
        e.focus_get()
        
        if e.get().lower()==colours[1].lower():
            score+=1
            l.config(text="Correct Answer :)")
            correct()
        else:
            l.config(text="Wrong Anser :(")
            wrong()
        e.delete(0,END)

        random.shuffle(colours)
        lable.config(fg=str(colours[1]),text=str(colours[0]))
        score_lable.config(text="score"+str(score))
    else:
        if score>5:
            victory()
            lable.destroy()
            message.config(text="Congratulations!!..:)",font=('Helvetica',20))
            score_lable.config(text="Final score "+str(score),font=('Helvetica',30))
            time_lable.destroy()
            instructions.destroy()
            l.destroy()
            e.destroy()
        elif score>2:
            victory()
            lable.destroy()
            message.config(text="good job!!...:)",font=('Helvetica',20))
            score_lable.config(text="Final score "+str(score),font=('Helvetica',30))
            time_lable.destroy()
            instructions.destroy()
            l.destroy()
            e.destroy()
        else:
            poorperformence()
            lable.destroy()
            message.config(text="better luck next time :)",font=('Helvetica',20))
            score_lable.config(text="Final score "+str(score),font=('Helvetica',30))
            time_lable.destroy()
            instructions.destroy()
            l.destroy()
            e.destroy()

def count_down():
    global time
    if time>0:
        time-=1

    time_lable.config(text="Time left"+str(time))
    time_lable.after(1000,count_down)

window=Tk()
sound()
window.config(bg="cyan")

window.geometry("400x400")
window.title("color game")
instructions=Label(text="Note : please enter text color show in below ",font=(20),bg="cyan")
instructions.pack()
score_lable=Label(text="press enter to start ",font=(10),bg="cyan")
score_lable.pack()
time_lable=Label(text="Time left"+str(time),font=(8),bg="cyan")
time_lable.pack()

message=Label( text=" Enter color ",font=(8),fg="red",bg="cyan")
message.pack()
l=Label(window,text="All the best",bg="cyan",font=(8))
l.pack()
lable=Label(font=('Helvetica', 60),bg="cyan")
lable.pack()
e=Entry(window,width=35)

window.bind('<Return>',start_game)

e.pack()
e.focus_set()

def rules():
    w=Tk()
    w.config(bg="yellow")
    w.geometry("500x200")
    la=Label(w,text=" press Enter button to strat the game Enter color of the text",bg="yellow",font=(20))
    la.pack()
    sound_file= "C:\\Users\\Raj CH\\Downloads\\3dsrv917ab6bbd0b123b1fc7537b6bcc4d1fc.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    w.mainloop()
    
but=Button(window,text="rules",command=rules,bg="gray")
but.pack()

window.mainloop()

