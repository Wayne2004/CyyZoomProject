import pyautogui,os,time,keyboard,schedule


def find_joinbutton():
    try:
        joinbutton = pyautogui.locateOnScreen('image/jointest.png', confidence=.6)
        x = joinbutton[0]
        y = joinbutton[1]
        pyautogui.moveTo(x + 30, y + 30)
        pyautogui.leftClick()
    except:
        find_joinbutton()
def findjoinmeetingheader(idleh):
    try:
        header = pyautogui.locateOnScreen('image/entry.png',confidence=0.6)
        pyautogui.moveTo(header[0]+150,header[1]+75)
        keyboard.write(idleh)
    except:
        findjoinmeetingheader(idleh)
def clickjoinmeeting():
    try:
        joinbutton = pyautogui.locateOnScreen('image/join.png',confidence=0.8)
        pyautogui.moveTo(joinbutton[0],joinbutton[1]+20)
        pyautogui.leftClick()
    except:
        clickjoinmeeting()
def findpasswordheader(password):
    try:
        pyautogui.locateOnScreen('image/passheader.png',confidence=0.6)
        keyboard.write(password)
    except:
        findpasswordheader(password)
def clickjoinmeeting2():
    global status
    try:
        joinbutton = pyautogui.locateOnScreen('image/join.png', confidence=0.8)
        pyautogui.moveTo(joinbutton[0], joinbutton[1] + 20)
        pyautogui.leftClick()
        status.configure(text='π₯ππΎπππΉ πππππΎππ β', fg='#52fc03')
    except:
        clickjoinmeeting2()


#try to join zoom
def joinzoom(id,password,times,status):
    #startzoomapp
    os.system("open /Applications/zoom.us.app")
    time.sleep(1)

    status.configure(text='πΏππΈπΆππΎππ π£', fg='#6b5237')
    find_joinbutton()
    status.configure(text='πΏππΈπΆπππΉ β', fg='#52fc03')

    time.sleep(0.4)

    status.configure(text='πΈππππ πΌπΉ', fg='#6b5237')
    findjoinmeetingheader(id)
    status.configure(text='πΌπΉ πΈππππππΉ β', fg='#52fc03')

    time.sleep(0.4)

    status.configure(text='πππΎπΈππΎππ π΅πππππ', fg='#6b5237')
    clickjoinmeeting()
    status.configure(text='π΅πππππ πππΎπΈπππΉ β', fg='#52fc03')

    time.sleep(0.4)

    status.configure(text='πΈπππππΎππ π«πΆππππππΉ', fg='#6b5237')
    findpasswordheader(password)
    status.configure(text='π«πΆππππππΉ πΈππππππΉ β', fg='#52fc03')

    status.configure(text='π²πΆπΎππΎππ π―πΎππ', fg='#6b5237')
    schedule.every().day.at(times).do(clickjoinmeeting2)
    while True:
        schedule.run_pending()
        time.sleep(1)



