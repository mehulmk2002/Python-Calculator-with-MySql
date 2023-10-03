from tkinter import *
import datetime
import pymysql.cursors
gui = Tk()
class calculator:
    def __init__(self,gui):
        self.expression=''
        self.equation=''
        self.eq=''
        self.gui()

    def press(self,num):      
        self.expression=self.expression+str(num)
        self.equation.set(self.expression)
        self.eq=self.expression
    def equalpress(self):
        try:
            total=str(eval(self.expression))
            self.equation.set(total)
            self.eq=self.expression
            self.expression=''
            print(self.eq)
        except:
            self.equation.set(" error ")
            self.expression = ""
    def clear(self):
        self.expression=''
        self.equation.set('')
    def saveRes(self,v):
        current_time = datetime.datetime.now()
        db=pymysql.connect(host='localhost',
                                user='root',
                                password='Mysql12345',
                                database='calculator',
                                cursorclass=pymysql.cursors.DictCursor)
        cursor=db.cursor()
        total=str(eval(self.eq))
        sql = "INSERT INTO calculator(Equation, \
        Result, Date_Time) \
        VALUES ('%s', '%s', '%s')" % \
        (self.eq, total, current_time)

    
        try:        
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        db.close()
    
    def delete(self,v):
        db=pymysql.connect(host='localhost',
                                    user='root',
                                    password='Mysql12345',
                                    database='calculator',
                                    cursorclass=pymysql.cursors.DictCursor)
        cursor = db.cursor()

       
        sql = "DELETE FROM calculator WHERE Date_Time = '%s'" % (v)
        try:
         
            cursor.execute(sql)
           
            db.commit()
        except:
            db.rollback()

        db.close()
        
    def history(self):
        import pymysql.cursors
       
        root = Toplevel(gui)
    
       
        root.title("history")
    
       
        root.geometry("400x400")
    
       


        db=pymysql.connect(host='localhost',
                                        user='root',
                                        password='Mysql12345',
                                        database='calculator',
                                        cursorclass=pymysql.cursors.DictCursor)
        cur=db.cursor()

      
        sql = "select * from calculator"
        try:
        
            cur.execute(sql)
  
            rt=cur.fetchone()
            print(rt)
            results = cur.fetchall()
            r=1
            c=0
            id=Button(root,text="id",bg='green').grid(row=0,column=0,padx=(2, 2),pady=(2,2))
            expression=Button(root,text="expression",bg='green').grid(row=0,column=1,padx=(2, 2),pady=(2,2))
            Total=Button(root,text="Total",bg='green').grid(row=0,column=2,padx=(2, 2),pady=(2,2))
            Date_Time=Button(root,text="Date_Time",bg='green').grid(row=0,column=3,padx=(2, 2),pady=(2,2))
            op=Button(root,text="*",bg='green').grid(row=0,column=4,padx=(2, 2),pady=(2,2))
            for row in results:
                for val in row.values():
                    
                    btn=Button(root,text=val,bg='light green').grid(row=r,column=c,padx=(2, 2),pady=(2,2))
                    c=c+1
                btn=Button(root,text="DELETE",bg='red',command=lambda: self.delete(val)).grid(row=r,column=c,padx=(2, 2),pady=(2,2))
                r=r+1
                c=0
        except:
         print ("Error: unable to fetch data")

       
        db.close()



    def gui(self):
        
        gui.configure(background="light green")

        gui.title("Simple Calculator")


        gui.geometry("300x200")

        self.equation = StringVar()

        expression_field = Entry(gui, textvariable=self.equation)

        expression_field.grid(columnspan=4, ipadx=70,pady=10)

        button1 = Button(gui, text=' 1 ', fg='black', bg='#FF1493',
                        command=lambda: self.press(1), height=1, width=7)
        button1.grid(row=2, column=0)

        button2 = Button(gui, text=' 2 ', fg='black', bg='#FF1493',
                        command=lambda: self.press(2), height=1, width=7)
        button2.grid(row=2, column=1)

        button3 = Button(gui, text=' 3 ', fg='black', bg='#FF1493',
                        command=lambda: self.press(3), height=1, width=7)
        button3.grid(row=2, column=2)

        button4 = Button(gui, text=' 4 ', fg='black', bg='#FF1493',
                        command=lambda: self.press(4), height=1, width=7)
        button4.grid(row=3, column=0)

        button5 = Button(gui, text=' 5 ', fg='black', bg='#FF1493',
                        command=lambda: self.press(5), height=1, width=7)
        button5.grid(row=3, column=1)

        button6 = Button(gui, text=' 6 ', fg='black', bg='#FF1493',
                        command=lambda: self.press(6), height=1, width=7)
        button6.grid(row=3, column=2)

        button7 = Button(gui, text=' 7 ', fg='black', bg='#FF1493',
                        command=lambda: self.press(7), height=1, width=7)
        button7.grid(row=4, column=0)

        button8 = Button(gui, text=' 8 ', fg='black', bg='#FF1493',
                        command=lambda: self.press(8), height=1, width=7)
        button8.grid(row=4, column=1)

        button9 = Button(gui, text=' 9 ', fg='black', bg='#FF1493',
                        command=lambda: self.press(9), height=1, width=7)
        button9.grid(row=4, column=2)

        button0 = Button(gui, text=' 0 ', fg='black', bg='#FF1493',
                        command=lambda: self.press(0), height=1, width=7)
        button0.grid(row=5, column=0)

        plus = Button(gui, text=' + ', fg='black', bg='#FF1493',
                    command=lambda: self.press("+"), height=1, width=7)
        plus.grid(row=2, column=3)
        
        minus = Button(gui, text=' - ', fg='black', bg='#FF1493',
                    command=lambda: self.press("-"), height=1, width=7)
        minus.grid(row=3, column=3)

        multiply = Button(gui, text=' * ', fg='black', bg='#FF1493',
                        command=lambda: self.press("*"), height=1, width=7)
        multiply.grid(row=4, column=3)

        divide = Button(gui, text=' / ', fg='black', bg='#FF1493',
                        command=lambda: self.press("/"), height=1, width=7)
        divide.grid(row=5, column=3)

        equal = Button(gui, text=' = ', fg='black', bg='#D2691E',
                    command=self.equalpress, height=1, width=7)
        equal.grid(row=5, column=2)

        clear = Button(gui, text='Clear', fg='black', bg='red',
                    command=self.clear, height=1, width=7)
        clear.grid(row=5, column='1')

        Decimal= Button(gui, text='.', fg='black', bg='#FF1493',
                        command=lambda: self.press('.'), height=1, width=7)
        Decimal.grid(row=6, column=0)
        save=Button(gui, text='save', fg='black', bg='#32CD32',
					command=lambda: self.saveRes('sumit'), height=1, width=7)
        save.grid(row=6, column=1)   
        his=Button(gui, text='History', fg='black', bg='#008080',
					command=lambda: self.history(), height=1, width=7)
        his.grid(row=6, column=2)  
pn=calculator(gui)

gui.mainloop()