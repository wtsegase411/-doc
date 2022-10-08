from tkinter import *
import check
root = Tk()
root.geometry("450x400")
root.title(" BBB project ")
tex = Text(master=root)

def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    if (check.check(INPUT)):
        Output.insert(END, 'Correct syntax')
    else:
        Output.insert(END, "Wrong syntax\n")
        Output.insert(END, check.fixSyntax(INPUT))

def clearToTextInput():
    inputtxt.delete('1.0','end')
    Output.delete('1.0','end')

l = Label(text="Check URL syntax ")
inputtxt = Text(root, height=8,
                width=40,
                bg="light yellow")

Output = Text(root, height=8,
              width=40,
              bg="light cyan")

Display = Button(root, height=2,
                 width=15,
                 text="Result",
                 command=lambda: Take_input())
Clear = Button(root, height=2,
               width=15,
               text="Clear",
               command=clearToTextInput)
l.pack()
inputtxt.pack()
Display.pack()
Output.pack()
Clear.pack()
mainloop()
