import tkinter as tk

# 创建一个窗口
largeFontStyle = ("Arial", 40, "bold")
smallFontStyle = ("Arial", 16)
digitsFontStyle = ("Arial", 24, "bold")
defaultFontStyle = ("Arial", 20)

offWhite = "#F8FAFF"
white = "#FFFFFF"
lightBlue = "#CCEDFF"
lightGray = "#F5F5F5"
labelColor = "#25265E"
red = "#FF0000"
orange="#FFA500"
yellow="#FFFF00"
green="#008000"
blue="#0000FF"
indigo="#00FFFF"
purple="#800080"
addition = "+"
subtraction = "-"
multiplication = "x"
division = "÷"

class Calculator:
    def __init__(self):
        self.window=tk.Tk()
        
        #self.window.geometry("600x600")
        self.window.configure(bg=lightGray)
        #self.window.geometry("375x667")#unnecessary
        self.window.resizable(0, 0)
        self.window.title("Handy Calculator")
        self.totalExpression = "0"
        self.displayLabel,self.label=self.createDisplayLabel()
        self.mode=self.createDisplayMode()
        #根据运算符显示对应的运算式   0：加法 1：减法 2乘法  3：除法
        self.operational_character=addition
        self.displayButton= (tk.Canvas(self.window))
        self.displayButton=self.createDisplayButton()
        
    def createDisplayLabel(self):
        frame = tk.Frame(self.window, height=221, bg=lightGray)
        frame.pack()
        label = tk.Label(frame, text=self.totalExpression, 
                              anchor=tk.N, bg=lightGray,height=1,
                               fg=labelColor, padx=24, font=smallFontStyle)
        label.pack()
        return frame,label
    
    def createDisplayMode(self):
        frame = tk.Frame(self.window, height=221, bg=lightGray,padx=10, pady=10)
        frame.pack()
        add_button      = tk.Button(frame, text="加法", padx=10, pady=10,command=lambda: self.set_symbol(addition))
        subtract_button = tk.Button(frame, text="减法", padx=10, pady=10,command=lambda: self.set_symbol(subtraction))
        multiply_button = tk.Button(frame, text="除法", padx=10, pady=10,command=lambda: self.set_symbol(multiplication))
        divide_button   = tk.Button(frame, text="乘法", padx=10, pady=10,command=lambda: self.set_symbol(division))
        # 使用grid布局排列操作按钮
        add_button.grid(row=0, column=0)
        subtract_button.grid(row=0, column=1)
        multiply_button.grid(row=0, column=2)
        divide_button.grid(row=0, column=3)
        return (add_button,subtract_button,multiply_button,divide_button)

    def set_symbol(self,current_value):
        self.operational_character=current_value
        self.displayButton=self.createDisplayButton()

    def get_operational_character(self):
        return self.operational_character
    
    def destroy_frame(self):
        self.displayButton.destroy()

    def createDisplayButton(self):
        self.destroy_frame()
        canvas = tk.Canvas(self.window)
        scrollbar = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.configure(yscrollcommand=scrollbar.set)
        frame = tk.Frame(canvas, height=221, bg=lightGray)
        frame.pack(side="top") 
        operation= self.get_operational_character()   
        for x in range(1, 10):
            for y in range(1, 10):
                text = "{:<{width}}".format(f"{x}{operation}{y}", width=5)
                button = tk.Button(frame, text=text, padx=10, pady=10, command=lambda x=x, y=y: self.calculate_ans(x, y))
                button.grid(row=x, column=y)
        return canvas
    
    def calculate_ans(self,x,y):
        operation=self.get_operational_character()
        if operation==addition:
            result = x + y
            self.totalExpression = f"{x} + {y} = {result}"
        if operation==subtraction:
            result = x - y
            self.totalExpression = f"{x} - {y} = {result}"
        if operation==multiplication:
            result = x * y
            self.totalExpression = f"{x} x {y} = {result}"
        if operation==division:
            result = x / y
            self.totalExpression = f"{x} ÷ {y} = {result}"
        self.label.config(text=self.totalExpression)

    def run(self):
        self.window.mainloop()

# 运行主循环
if __name__ == "__main__":
    calc = Calculator()
    calc.run()