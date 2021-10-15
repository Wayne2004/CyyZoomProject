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
        status.configure(text='𝒥𝑜𝒾𝓃𝑒𝒹 𝑀𝑒𝑒𝓉𝒾𝓃𝑔 ✔', fg='#52fc03')
    except:
        clickjoinmeeting2()


#try to join zoom
def joinzoom(id,password,times,status):
    #startzoomapp
    os.system("open /Applications/zoom.us.app")
    time.sleep(1)

    status.configure(text='𝐿𝑜𝒸𝒶𝓉𝒾𝓃𝑔 𝟣', fg='#6b5237')
    find_joinbutton()
    status.configure(text='𝐿𝑜𝒸𝒶𝓉𝑒𝒹 ✔', fg='#52fc03')

    time.sleep(0.4)

    status.configure(text='𝐸𝓃𝓉𝑒𝓇 𝐼𝒹', fg='#6b5237')
    findjoinmeetingheader(id)
    status.configure(text='𝐼𝒹 𝐸𝓃𝓉𝑒𝓇𝑒𝒹 ✔', fg='#52fc03')

    time.sleep(0.4)

    status.configure(text='𝒞𝓁𝒾𝒸𝓀𝒾𝓃𝑔 𝐵𝓊𝓉𝓉𝑜𝓃', fg='#6b5237')
    clickjoinmeeting()
    status.configure(text='𝐵𝓊𝓉𝓉𝑜𝓃 𝒞𝓁𝒾𝒸𝓀𝑒𝒹 ✔', fg='#52fc03')

    time.sleep(0.4)

    status.configure(text='𝐸𝓃𝓉𝑒𝓇𝒾𝓃𝑔 𝒫𝒶𝓈𝓈𝓌𝑜𝓇𝒹', fg='#6b5237')
    findpasswordheader(password)
    status.configure(text='𝒫𝒶𝓈𝓈𝓌𝑜𝓇𝒹 𝐸𝓃𝓉𝑒𝓇𝑒𝒹 ✔', fg='#52fc03')

    status.configure(text='𝒲𝒶𝒾𝓉𝒾𝓃𝑔 𝒯𝒾𝓂𝑒', fg='#6b5237')
    schedule.every().day.at(times).do(clickjoinmeeting2)
    while True:
        schedule.run_pending()
        time.sleep(1)



