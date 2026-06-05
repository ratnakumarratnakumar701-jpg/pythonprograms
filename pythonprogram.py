import tkinter as tk
root = tk.Tk()
root.title("Drawing Pad")


canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack(pady=10)

last_x, last_y = None, None

def start_paint(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def paint(event):
    global last_x, last_y
    
    canvas.create_line(last_x, last_y, event.x, event.y, 
                       width=3, fill="black", capstyle=tk.ROUND, smooth=True)
    last_x, last_y = event.x, event.y

def reset(event):
    global last_x, last_y
    last_x, last_y = None, None


canvas.bind("<Button-1>", start_paint)      
canvas.bind("<B1-Motion>", paint)          
canvas.bind("<ButtonRelease-1>", reset)    


def clear_canvas():
    canvas.delete("all")

clear_btn = tk.Button(root, text="Clear", command=clear_canvas)
clear_btn.pack()

root.mainloop()
