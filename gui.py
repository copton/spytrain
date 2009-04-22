from Tkinter import *
from string import join

class MyText(Text):
    def __init__(self, master, **kw):
        apply(Text.__init__,(self,master),kw)
        self["bg"] = "#000"
        self["fg"] = "#0f0"
        self["font"] = ("Helvetica", "13")
        self.bind("<Key>", lambda e: "break")
        self.bind("<Button-1>", lambda e: "break")
        self.bind("<Double-Button-1>", lambda e: "break")


class Gui:
    def __init__(self, event_handler):
        self.root = Tk()
        self.root.title("Spy Trainer")

        help_text = MyText(self.root)
        help_text.insert(INSERT, """Help:

<ESC> \t \t Exit
<Return> \t \t Start
<Backspace> \t Replay
<F1> \t \t Help
<F2> \t \t Edit Amount
<F3> \t \t Edit Uptime
<F4> \t \t Edit Delay
<F5> \t \t Edit Alphabet
<Up> \t \t Increase Value
<Down> \t \t Decrease Value
<Right> \t \t Increase Scattering
<Left> \t \t Decrease Scattering""")

        self.opt_text = MyText(self.root)
        self.opt_text.insert(INSERT, "Options:\n")
        self.opt_text.mark_set("amount", INSERT)
        self.opt_text.mark_gravity("amount", LEFT)
        self.opt_text.insert(INSERT, "\n")
        self.opt_text.mark_set("uptime", INSERT)
        self.opt_text.mark_gravity("uptime", LEFT)
        self.opt_text.insert(INSERT, "\n")
        self.opt_text.mark_set("delay", INSERT)
        self.opt_text.mark_gravity("delay", LEFT)
        self.opt_text.insert(INSERT, "\n")
	self.opt_text.mark_set("alphas", INSERT)
	self.opt_text.mark_gravity("alphas", LEFT)
	self.opt_text.insert(INSERT, "\n")


        self.main_text = MyText(self.root)
        self.main_text.mark_set("curline", INSERT)
        self.main_text.mark_gravity("curline", LEFT)
	self.main_text.insert(INSERT, "hello world")


        # slider = Scrollbar(self.root, orient=VERTICAL,command=self.scrtest)
        # self.main_text["yscrollcommand"]=slider.set

        help_text.grid(column=2, row=0,sticky=N+E+S+W)
        self.opt_text.grid(column=2,row=1, sticky=N+E+S+W)
	self.main_text.grid(column=0, row=0, rowspan=2)
        # slider.grid(column=1, row=0, rowspan=2, sticky=N+S)
        
        apply(self.main_text.config,(),{"height":40, "width":80})
        apply(help_text.config,(),{"height":20, "width":40})
        apply(self.opt_text.config,(),{"height":20, "width":40})
              
        self.root.bind("<Key>", event_handler)
    

    def run(self):
        self.root.mainloop()

    def quit(self):
	self.root.quit()

    def tk_callback(self, delay, callback, a, b):
        self.root.after(delay, callback, a, b)
        
    def option_string(self, option, options):
	if (options[1] == 0) :
	    return "%s: %d" % (option,options[0])
	else: 
            return join((option, " %d +/- %d" %options), ":")

    def display_option(self, **options):
	for option in options.keys():
	    if option in ("amount", "uptime", "delay"):
		self.opt_text.delete(option, "%s lineend" %option)
		self.opt_text.insert(option, self.option_string(option, options[option]))
	    elif option == "alphas":
	        self.opt_text.delete("alphas", "alphas lineend")
	        self.opt_text.insert("alphas", "Alphabeth: %s" %options[option])
            else:
                raise "illigal option %s" %k


    def display_passw(self, passw, disc, max):
        displ = []
        i=0
        for c in passw:
            if i == max:
                break
            if i<disc:
                displ.append(" ")
            else:
                displ.append(c)
            i += 1


        self.main_text.delete("curline", "curline lineend")
        self.main_text.insert("curline", join(displ))

    def newline(self):
        self.main_text.mark_unset("curline")
        self.main_text.insert(INSERT, "\n")
        self.main_text.mark_set("curline", INSERT)
        self.main_text.mark_gravity("curline", LEFT)
        self.main_text.see(INSERT)

    



