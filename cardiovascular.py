from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("CARDIOVASCULAR SYMPTOMS TEST")
window.geometry("700x600")
window.configure(background="SandyBrown")

ques1 = StringVar(value = "0")
ques1_label = Label(window , text = "DO YOU FEEL SHORTNESS OF BREATHING DURING ROUTINE ACTIVITIES? " , bg="salmon")
ques1_label.place(relx=0.5 , rely = 0.1 , anchor = CENTER)
ques1_r1 = Radiobutton(window , text = "Yes " , variable = ques1, value = "Yes")
ques1_r1.place(relx=0.5 , rely = 0.15 , anchor = CENTER)
ques1_r2= Radiobutton(window , text = "No" , variable = ques1, value = "No")
ques1_r2.place(relx=0.5 , rely = 0.2 , anchor = CENTER)


ques2 = StringVar(value = "0")
ques2_label = Label(window , text = "DO YOU HAVE SWELLING IN FEET/ANKLE/LEGS OR ABDOMEN?" , bg="salmon")
ques2_label.place(relx=0.5 , rely = 0.25 , anchor = CENTER)
ques2_r1 = Radiobutton(window , text = "Yes " , variable = ques2, value = "Yes")
ques2_r1.place(relx=0.5 , rely = 0.3 , anchor = CENTER)
ques2_r2= Radiobutton(window , text = "No" , variable = ques2, value = "No")
ques2_r2.place(relx=0.5 , rely = 0.35 , anchor = CENTER)



ques3 = StringVar(value = "0")
ques3_label = Label(window , text = "DO YOU FEEL ANY OF THESE SYMPTOMS - CONFUSION , DISORIENTATION OR LOSS OF MEMORY?" , bg="salmon")
ques3_label.place(relx=0.5 , rely = 0.4 , anchor = CENTER)
ques3_r1 = Radiobutton(window , text = "Yes " , variable = ques3, value = "Yes")
ques3_r1.place(relx=0.5 , rely = 0.45 , anchor = CENTER)
ques3_r2= Radiobutton(window , text = "No" , variable = ques3, value = "No")
ques3_r2.place(relx=0.5 , rely = 0.5 , anchor = CENTER)



ques4 = StringVar(value = "0")
ques4_label = Label(window , text = "DO YOU FEEL SHORTNESS OF BREATHING WHILE A REST/LYING DOWN?" , bg="salmon")
ques4_label.place(relx=0.5 , rely = 0.55 , anchor = CENTER)
ques4_r1 = Radiobutton(window , text = "Yes " , variable = ques4, value = "Yes")
ques4_r1.place(relx=0.5 , rely = 0.6 , anchor = CENTER)
ques4_r2= Radiobutton(window , text = "No" , variable = ques4, value = "No")
ques4_r2.place(relx=0.5 , rely = 0.65 , anchor = CENTER)




ques5 = StringVar(value = "0")
ques5_label = Label(window , text = "DO YOU EXPERIENCE PERSISTANCE WHEEZING/COUGHING THAT PRODUCE WHITE OR PINK BLOOD TINGED MUCUS" , bg="salmon")
ques5_label.place(relx=0.5 , rely = 0.7 , anchor = CENTER)
ques5_r1 = Radiobutton(window , text = "Yes " , variable = ques5, value = "Yes")
ques5_r1.place(relx=0.5 , rely = 0.75 , anchor = CENTER)
ques5_r2= Radiobutton(window , text = "No" , variable = ques5, value = "No")
ques5_r2.place(relx=0.5 , rely = 0.8 , anchor = CENTER)




def cardiovascular_score():
    score = 0
    if ques1.get()=="Yes":
        score+=10
    if ques2.get()=="Yes":
        score+=10
    if ques3.get()=="Yes":
        score+=10 
    if ques4.get()=="Yes":
        score+=10  
    if ques5.get()=="Yes":
        score+=10       

    if score ==10:
        messagebox.showinfo("Report" ,"You don't need to visit a doctor")  

    elif score > 10 and score < 30:
        messagebox.showinfo("Report" ,"You might perhaps need to visit a doctor")          
    
    else :
        messagebox.showinfo("Report" ,"You should strongly visit a doctor") 


btn = Button(window , text = "Click me" , command = cardiovascular_score )   
btn.place(relx=0.5 , rely = 0.9, anchor = CENTER)        




window.mainloop()