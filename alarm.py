import time, winsound

def main():
    global maininp
    maininp = input("Hours mins or sec").lower()
    timelist = ("hours","mins" ,"sec")
    if maininp in timelist:
        times(maininp)
    else:
        print("try again")
        main()


def times(userinp):
    if userinp == "hours":
        timewanted = int(input("how many hour: "))
        waitingtime= (timewanted*60)*60
        alarm(waitingtime)

    elif userinp == "mins":
        timewanted = int(input("how many mins: "))
        waitingtime= timewanted*60
        alarm(waitingtime)

    elif userinp == "sec":
        timewanted = int(input("how many sec: "))
        waitingtime= timewanted
        alarm(timewanted)

def alarm(thetime):
    if maininp == "hours":
        s = str((thetime/60)/60)
        items = s.split(".")
        if thetime ==1:
            print(f"Your alarm is set for {int((thetime/60)/60)} Hour")
            time.sleep(thetime)
            sound()
        elif thetime != 1:
            print(f"Your alarm is set for {int((thetime/60)/60)} Hours")
            time.sleep(thetime)
            sound()

    elif maininp == "mins":
        test = float((thetime / 60))
        twodp = float("{:.2f}".format(test))
        s = str(twodp)
        items = s.split(".")
        if test >60:
            print(f"Your alarm is set for {items[0]} Hours and {items[1]} mins")
            time.sleep(thetime)
            sound()

        else:
            print(f"Your alarm is set for {int(thetime/60)} mins")
            time.sleep(thetime)
            sound()
    elif maininp == "sec":
        print(f"Your alarm is set for {thetime} seconds")
        time.sleep(thetime)
        sound()



def sound():
    for i in range(2):
        for j in range (3):
            winsound.MessageBeep(-1)
            time.sleep(0.3)
        time.sleep(1)


main()    
