import time
import tkinter as tk

def tick(time1=''):
    #get the current time from the pc
    time2 = time.strftime('%H:%m:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)

        clock.after(200, tick)
        
root = tk.Tk()
clock = tk.Label(root, font=('arial', 20, 'bold'), bg = 'white')
clock.pack(fill='both', expand=1)
tick()
root.mainloop()
                 
