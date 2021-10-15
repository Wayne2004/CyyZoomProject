import tkinter as tk
import tkinter.font as tkfont
from tkinter import PhotoImage
import os,json
import joinmeet
import threading


#run task
def forthread():
    state.configure(text='𝒢𝑒𝓉𝓉𝒾𝓃𝑔 𝑅𝑒𝒶𝒹𝓎', fg='#6b5237')
    joinmeet.joinzoom(idsv.get(), PassSv.get(), timesv.get(), state)
def runtask():
    t = threading.Thread(target=forthread)
    t.start()

#setting up some files
def dumpfile(data,filename):
    with open(filename,'w') as f:
        json.dump(data,f,indent=4)
        f.close()

defaultjson = {
    "id":"",
    "password":"",
    "time":"00:00"
}
if os.path.exists('config.json'):
    with open('config.json','r') as f:
        config = json.load(f)
        f.close()
    nofile = False
else:
    dumpfile(defaultjson,'config.json')
    nofile = True


#setting some colors
mainbackground = '#dfb98a'
widgetbackground = '#ae8557'
textcolor = '#8a6030'


#root configuration
root = tk.Tk()
root.title('Little Wayne')
root.iconbitmap('image\\potato.ico')
root.configure(bg=mainbackground)

#loading some picture
bear1 = PhotoImage(file='image/bear1bg.png')
bear2 = PhotoImage(file='image/bear2bg.png')
lovebear2 = PhotoImage(file='image/lovebear2.png')
run = PhotoImage(file='image/run.png')

#set window sizes
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
root.maxsize(500,300)
root.minsize(500,300)
root.geometry(f'500x300+{int(screenwidth/2)-250}+{int(screenheight/2)-150}')

#callbacks
def identry(sv):
    if nofile:
        defaultjson["id"] = sv.get()
        dumpfile(defaultjson,'config.json')
    else:
        config["id"] = sv.get()
        dumpfile(config, 'config.json')
def passentry(sv):
    if nofile:
        defaultjson["password"] = sv.get()
        dumpfile(defaultjson, 'config.json')
    else:
        config["password"] = sv.get()
        dumpfile(config, 'config.json')
def time2entry(sv):
    if nofile:
        defaultjson["time"] = sv.get()
        dumpfile(defaultjson, 'config.json')
    else:
        config["time"] = sv.get()
        dumpfile(config, 'config.json')

#string vars for entry
idsv = tk.StringVar()
idsv.trace("w", lambda name, index, mode, sv=idsv: identry(sv))

PassSv = tk.StringVar()
PassSv.trace('w', lambda name,index,mode,sv=PassSv: passentry(sv))

timesv = tk.StringVar()
timesv.trace('w', lambda name,index,mode,sv=timesv: time2entry(sv))

#add a frame
frame = tk.Frame(root,
                 bg=mainbackground,
                 width=500,height=300)
frame.pack(fill='both')

#widgets
zoomidtext = tk.Label(frame,
                      text='𝒵𝑜𝑜𝓂 𝐼𝒟',
                      bg=mainbackground,fg=textcolor,
                      font=tkfont.Font(family='Andy',size=20))
zoomidtext.place(x=20,y=5)
zoomidentry = tk.Entry(frame,bd=0,
                       bg=widgetbackground,selectbackground=mainbackground,selectforeground=widgetbackground,
                       fg=mainbackground,insertbackground=mainbackground,
                       width=15,
                       textvariable=idsv,
                       font=tkfont.Font(family='Ink Free',size=15,weight='bold'))
zoomidentry.place(x=20,y=40)


zoompasstext = tk.Label(frame,
                      text='𝒵𝑜𝑜𝓂 𝒫𝒶𝓈𝓈𝓌𝑜𝓇𝒹',
                      bg=mainbackground,fg=textcolor,
                      font=tkfont.Font(family='Andy',size=20))
zoompasstext.place(x=20,y=70)
zoompassentry = tk.Entry(frame,bd=0,
                       bg=widgetbackground,selectbackground=mainbackground,selectforeground=widgetbackground,
                       fg=mainbackground,insertbackground=mainbackground,
                       width=15,
                       textvariable=PassSv,
                       font=tkfont.Font(family='Ink Free',size=15,weight='bold'))
zoompassentry.place(x=20,y=105)


timetext = tk.Label(frame,
                      text='𝒯𝒾𝓂𝑒',
                      bg=mainbackground,fg=textcolor,
                      font=tkfont.Font(family='Andy',size=20))
timetext.place(x=20,y=135)
timeentry = tk.Entry(frame,bd=0,
                       bg=widgetbackground,selectbackground=mainbackground,selectforeground=widgetbackground,
                       fg=mainbackground,insertbackground=mainbackground,
                       width=15,
                       textvariable=timesv,
                       font=tkfont.Font(family='Ink Free',size=15,weight='bold'))
timeentry.place(x=20,y=170)

if nofile:
    zoomidentry.insert('end',defaultjson["id"])
    zoompassentry.insert('end', defaultjson["password"])
    timeentry.insert('end', defaultjson["time"])
else:
    zoomidentry.insert('end', config["id"])
    zoompassentry.insert('end', config["password"])
    timeentry.insert('end', config["time"])

#status label
status = tk.Label(frame,text='𝒮𝓉𝒶𝓉𝓊𝓈',
                  bg=mainbackground, fg=textcolor,
                  font=tkfont.Font(family='Andy',size=15))
status.place(x=20,y=200)
dot = tk.Label(frame,text=':',
                  bg=mainbackground, fg=textcolor,
                  font=tkfont.Font(family='Andy',size=15))
dot.place(x=80,y=203)
state = tk.Label(frame,text='𝒪𝒻𝒻𝓁𝒾𝓃𝑒',
                  bg=mainbackground, fg=textcolor,
                  font=tkfont.Font(family='Andy',size=15))
state.place(x=95,y=200)


#buttons
buttonimage = tk.Button(frame,image=bear1,bg=mainbackground,bd=0,width=200,height=250)
buttonimage.place(x=240,y=70)

buttonimage2 = tk.Button(frame,image=bear2,bg=mainbackground,bd=0,width=90,height=100)
buttonimage2.place(x=240,y=15)

buttonimage3 = tk.Button(frame,image=lovebear2,bg=mainbackground,bd=0,width=90,height=100)
buttonimage3.place(x=390,y=10)

runbutton = tk.Button(frame,image=run,
                      bd=0,relief='sunken',bg=mainbackground,
                      activebackground=mainbackground,command=runtask)
runbutton.place(x=16,y=245)



root.mainloop()
