import datetime as dt


def read(date):
    try:
        file = open(date + ".txt", "r")
        for i in file:
            print(i, end="")

    except Exception as e:
        print("File not found")
        print("Oops! ", e.__class__)
    finally:
        start()


def write(wrt):
    time = dt.datetime.now().strftime("%d-%m-%Y")
    file = open(time + ".txt", "a")
    file.write(wrt + "\n")


def start():
    menu = input("""
            ************
            Welcome :::
            Read     ---> 1
            Write    ---> 2
            Shutdown ---> 0
            ************             
           """)
    if menu == "1":
        day = input("Date : ")
        read(day)
    elif menu == "2":
        while True:
            daily = input("Start To Write (press + for shutdown) ")
            if daily == "+":
                start()
            write(daily)
    elif menu == "0":
        return
    else:
        print("Wrong Chose")


start()
