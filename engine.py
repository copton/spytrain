#!/usr/bin/python

from gui import Gui
from random import Random
from string import join

class Engine:
    alphas = ["a", "a1", "a1A", "a1A!"]
    alpha = 0
    training = 0
    ready = 0
    def __init__(self):
        self.option = "amount"
        self.options = {"amount":(5,0), "uptime":(20,0), "delay":(20,0), "alphas":self.alphas[self.alpha]}
        self.gui = Gui(self.key_event_handler)

	apply(self.gui.display_option, (), self.options)

        self.rnd = Random()
        
    def run(self):
        self.gui.run()

    def train(self):
	if self.training:
	   return
	self.training = 1
        self.ready = 0
        self.user_input = []
        
        self.passw = []
        i = 0
        var = self.options["amount"][1] 
        len = self.options["amount"][0] + self.rnd.randint(-1*var, var)
        if len < 1:
            len = 1
        while i < len:
            char = self.rnd.randint(33,126)
            if self.alpha!=3:
                if char in range(33,48) or char in range(58,65) or char in range(91,97) or char in range(123,127):  # special characters
                    continue
            if self.alpha!=2:
                if char in range(65,91): #A-Z
                    continue
            if self.alpha!=1:
                if char in range(48,58): #0-9
                    continue
            if not self.alpha in range(4):
                raise "train: illigal value for alpha: %d" %self.alpha

            self.passw.append(chr(char))
            i += 1

        self.callback(0,0)

    def callback(self, *args):
        if args[1] == 0:
            if args[0] < self.passw.__len__():
                self.gui.display_passw(self.passw, args[0], args[0]+1)
                upt, var = self.options["uptime"]
                total = upt + self.rnd.randint(-1*var, var)
                self.gui.tk_callback(total*10, self.callback, args[0], 1)
            else:    
                self.ready = 1
        else:
            self.gui.display_passw(self.passw,0,0)
            delay, var = self.options["delay"]
            total = delay + self.rnd.randint(-1*var, var)
            self.gui.tk_callback(total*10, self.callback, args[0]+1, 0)

    def user_completed(self):
        mistakes = self.passw.__len__() - self.user_input.__len__()
        for i in range(self.user_input.__len__()):
             if self.passw.__len__() <= i:
                 mistakes += 1
             else:
                if ord(self.user_input[i])!= ord(self.passw[i]):
                    mistakes += 1

        user = join(self.user_input,"")
        pw = join(self.passw, "")
        show = join((pw, user, str(mistakes)))
        self.gui.display_passw(show, 0, show.__len__())
        self.gui.newline()
        self.training = 0
        self.ready = 0
            
    def key_event_handler(self, event):
        k = event.keysym
        if k in ("F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "Up", "Down", "Left", "Right"):
            self.handle_options(k)
        else:
            self.handle_user_input(k)
        
    def handle_options(self, k):
        if k == "F2":
            self.option = "amount"
        elif k == "F3":
            self.option = "uptime"
        elif k == "F4":
            self.option = "delay"
	elif k == "F5":
	    self.option = "alphas"
        elif k in ("Up", "Down", "Left", "Right"):
	    if self.option in ("amount", "uptime", "delay"):
                a,b = self.options[self.option]
                if (k=="Up"):
                    a = a + 1
                elif (k=="Down"):
                    if (a>1):
                        a = a - 1
                elif (k=="Right"):
                     b = b + 1
                elif (k=="Left"):
                    if (b>0):
                        b = b - 1
                self.options[self.option] = (a,b)
	    elif self.option == "alphas":
               if (k=="Up"):
		   if self.alpha < self.alphas.__len__() - 1:
                       self.alpha += 1
               elif (k=="Down"):
		   if self.alpha > 0:
		       self.alpha -= 1
               self.options[self.option] = self.alphas[self.alpha]

            apply(self.gui.display_option,(),{self.option:self.options[self.option]})
        else:
            pass

    def handle_user_input(self, k):
     	if k == "Escape":
	    self.gui.quit()
	elif k == "Return":
            if self.training == 0:
                self.train()
            if self.ready == 1:
                self.user_completed()
        elif k == "BackSpace":
            if self.training == 1:
		self.user_input=[]
                self.callback(0,0)
        elif k in ("Shift_R", "Shift_L", "Tab", "Next", "Prior", "Control_L", "Control_R", "CapsLock", "Alt_L", "Alt_R", "Mode_switch", "Menu", "SuperL", "Delete", "Insert", "Print"):
            pass
        else:
            if self.ready:
                self.user_input.append(k)

if __name__ == '__main__':
    engine = Engine()
    engine.run()
else:
    print "Module engine loaded"

