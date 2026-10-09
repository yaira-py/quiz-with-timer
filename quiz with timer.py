import tkinter as tk
from tkinter import messagebox
import time


class QuizApp:
    def __init__(self,root):
        self.root=root
        self.timer_id=None
        
        self.root.title('Quiz With Timer')
        self.root.geometry('450x400')

        self.time_lb=tk.Label(self.root,text='Timer⏲️:00',font=("Arial",12,'bold'),fg='#333333')
        self.time_lb.pack(pady=10)

        self.questions=[{'q':'what item envoles pikachu into raichu','options':['fire stone','thunder stone','water stone',
                            'leaf stone'],'ans':'thunder stone'},
                            {'q':'mewtwo was cloned from which pokemon','options':['ditto','arceus','clefairy','mew'],'ans':'mew'},
                            {'q':'which is gen1 grass starter','options':['bulbasaur','charmander','pikachu','squitle'],'ans':'bulbasaur'},
                            {'q':"who is ash main kanto rival",'options':['gary','brock','misty','lt.surge'],'ans':'gary'},
                            {'q':"primary type of pikachu",'options':['electric','water','normal','fire'],'ans':'electric'},
                            {'q':'who is the rock type gym leader of pewter city','options':['misty','blaine','erika','brock'],'ans':'brock'}]

        self.score=0
        self.currect_q=0
        self.time_left=20

        self.ques_lb=tk.Label(self.root,text='Your question is',font=("Arial",14,'bold'),fg='#333333')
        self.ques_lb.pack(pady=10)

        self.btns_frame=tk.Frame(self.root)
        self.btns_frame.pack(pady=15,padx=10,anchor='w',fill='x')

        self.btn1=tk.Button(self.btns_frame,text='option1',font=("Arial",12,'bold'),bg="#51995b",fg="#F5F5F5")
        self.btn1.pack(pady=10)

        self.btn2=tk.Button(self.btns_frame,text='option2',font=("Arial",12,'bold'),bg="#51995b",fg="#F5F5F5")
        self.btn2.pack(pady=10)

        self.btn3=tk.Button(self.btns_frame,text='option3',font=("Arial",12,'bold'),bg="#51995b",fg="#F5F5F5")
        self.btn3.pack(pady=10)

        self.btn4=tk.Button(self.btns_frame,text='option4',font=("Arial",12,'bold'),bg="#51995b",fg="#F5F5F5")
        self.btn4.pack(pady=10)

        self.restart_btn= tk.Button(self.root,text= 'restart again?',bg="#860E0E",fg='white',command=self.restart_quiz)


        self.ans_text=tk.Label(self.root,text='',font=('Arial',14),fg='#333333')
        self.ans_text.pack(pady=10)

    
        self.show_question()
        self.update_timer()


    def update_timer(self):
        self.time_lb.config(text=f'Timer⏲️: {self.time_left}')

        if self.time_left>0:
            self.time_left-=1
            self.timer_id=self.root.after(1000,self.update_timer)

        else:
            self.time_lb.config(text="Time's Up")
            self.timer_id=None
            self.ques_lb.config(text=f'Quiz end. score: {self.score}/{len(self.questions)}')
                         
            self.btn1.pack_forget()
            self.btn2.pack_forget()
            self.btn3.pack_forget()
            self.btn4.pack_forget()
            self.ans_text.config(text='')
            
            self.restart_btn.pack()



    def show_question(self):
        self.ans_text.config(text='')
        q_data =self.questions[self.currect_q]
        self.ques_lb.config(text=q_data['q'])

        self.btn1.config(text=q_data['options'][0],command=lambda opt=q_data['options'][0]: self.check_ans(opt))
        self.btn2.config(text=q_data['options'][1],command=lambda opt=q_data['options'][1]: self.check_ans(opt))
        self.btn3.config(text=q_data['options'][2],command=lambda opt=q_data['options'][2]: self.check_ans(opt))
        self.btn4.config(text=q_data['options'][3],command=lambda opt=q_data['options'][3]: self.check_ans(opt))

    

    def check_ans(self,selected_option):
        q_data= self.questions[self.currect_q]
        self.ans_text.pack(pady=10)

        if selected_option== q_data['ans']:
            self.ans_text.config(text='correct')
            self.score+= 1

        else:
            self.ans_text.config(text='incorrect')  

        self.currect_q+=1
        if self.currect_q<len(self.questions):
            self.root.after(1000, self.show_question)

        else: 
            if self.timer_id is not None:
               self.root.after(1000,self.timer_id)
               self.ques_lb.config(text=f'Quiz end. score: {self.score}/{len(self.questions)}')
                           
               self.btn1.pack_forget()
               self.btn2.pack_forget()
               self.btn3.pack_forget()
               self.btn4.pack_forget()

               self.ans_text.pack_forget()
            

            self.root.after(1000,self.next_q)



    def next_q(self):
        if self.currect_q< len(self.questions):
            self.show_question()

        else:
            self.ques_lb.config(text=f'Quiz end. score: {self.score}/{len(self.questions)}')

            self.btn1.pack_forget()
            self.btn2.pack_forget()
            self.btn3.pack_forget()
            self.btn4.pack_forget()
            self.ans_text.pack_forget()

            self.restart_btn= tk.Button(self.root,text= 'restart again?',bg="#860E0E",fg='white',command=self.restart_quiz)
            self.restart_btn.pack()

    def restart_quiz(self):
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)

        self.currect_q=0
        self.timer_id=None
        self.score=0
        self.time_left=20

        self.restart_btn.pack_forget()
        self.btn1.pack(pady=10)
        self.btn2.pack(pady=10)
        self.btn3.pack(pady=10)
        self.btn4.pack(pady=10)
        self.ans_text.pack(pady=10)

        self.show_question()
        self.update_timer()

    





if __name__=="__main__":
    window=tk.Tk()
    app=QuizApp(window)
    window.mainloop()
