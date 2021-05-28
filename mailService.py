from datetime import datetime
import os
import time

clear = ("cls" if os.name == "nt" else "clear")


class MailService(object):
    def __init__(self, name: str):
        self.__name = name
        self.__members = [("example", "exm", "example@exm.com", "password")]
        self.__send_mails = []

    def __str__(self):
        return "Welcome " + self.__name

    def control(self, mail: str):
        for i in self.__members:
            if i[2] == mail:
                return False
        return True

    def sing_up(self, f_name: str, l_name: str, mail: str, password: str):
        if self.control(mail):
            print("\n You can use it")
            new_one = f_name, l_name, mail, password
            self.__members.append(new_one)
            print("Done !")
        else:
            print("This Email is Used")

    def password_control(self, mail: str, password: str):
        for i in self.__members:
            if i[2] == mail and i[3] == password:
                return True
        return False

    def sing_in(self, mail: str, password: str):
        if self.password_control(mail, password):
            print("loading...")
            time.sleep(2)
            print("Welcome : " + self.__name)
            time.sleep(1)
            self.user_menu(mail)
        else:
            print("Something Wrong")
            time.sleep(1)

    def user_menu(self, mail: str):
        while 1:
            os.system(clear)
            print("""
                  [1] : Send Mail
                  [2] : Mail Box
                  [0] : Sing Out
                  """)
            option = int(input("Your chose : "))
            if option == 1:
                self.send_mail(mail)
            elif option == 2:
                self.mail_box(mail)
            elif option == 0:
                break

    def send_mail(self, mail):
        title = input("Title : ")
        content = input("Content : ")
        receiver = input("Receiver : ")
        new_mail = Mail(mail, receiver, title, content)
        self.__send_mails.append(new_mail)
        time.sleep(1)
        print("Done")
        print("Redirecting to main menu")
        time.sleep(1)
        self.user_menu(mail)

    def mail_box(self, mail):
        is_mail = False
        for i in self.__send_mails:
            if i.get_receiver() == mail or i.get_sender() == mail:
                is_mail = True
                print(i)
        if not is_mail:
            print("Mail Box empty")
        input("Press Enter ")


class Mail:
    def __init__(self, from_who, to_who, title, message):
        self.__from_who = from_who
        self.__to_who = to_who
        self.__title = title
        self.__message = message
        self.__date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def get_receiver(self):
        return self.__to_who

    def get_sender(self):
        return self.__from_who

    def __str__(self):
        return """
        *************************************************
        Date     :   {}
        Sender   :   {}
        Receiver :   {}
        *************************************************
        
        Title    :   {}
        Message  :   {}""".format(self.__date, self.__from_who, self.__to_who, self.__title, self.__message)


email1 = MailService("Mail")
menu = """
        {title}
        
        [1] -> Take Mail
        [2] -> Sing In
        [0] -> Sing Out
       """.format(title=email1)

while True:
    try:
        os.system(clear)
        print(menu)
        user_input = int(input(" --> : "))
        if user_input == 1:
            u_f_name = input("First Name : ")
            u_l_name = input("Last Name  : ")
            u_mail = input("Create Mail  : ")
            u_password = input("Password : ")
            if u_f_name and u_l_name and u_mail and u_password:
                email1.sing_up(u_f_name, u_l_name, u_mail, u_password)
        elif user_input == 2:
            email1.sing_in(mail=input("Email : "), password=input("Password : "))
        elif user_input == 0:
            break
        else:
            raise ValueError("You can chose ony 1,2 or 0")

    except ValueError as e:
        print("not found")
        print("Oops! ", e.__class__)
