from tkinter import *

from main import PasswordGengrator
from tkinter import messagebox
from PIL import ImageTk, Image
import threading, pickle, os, sys

python_dir = sys.executable

file_path = os.path.dirname(os.path.realpath(__file__))
Basic_File_exits_2 = os.path.isfile(f"{file_path}\\Data\\index.pak")
index = 0
# Done
root = Tk()
p1 = PhotoImage(file=f"{file_path}\Images\logo.png")
root.iconphoto(True, p1)
remove_list = []


if Basic_File_exits_2 == False:
    try:
        os.system("taskkill /im cmd.exe /f")
    except Exception as e:
        pass
    root.title("PassGen - Create/Secure Passwords ")
    root.resizable(False, False)
    root.geometry("1366x768")
    root.config(bg="white")

    def Typing_Effect_Cursor(
        root, words, sec1, sec_between, sec2, Deleting_effect, text_var, text_label
    ):
        for i, j in enumerate(words):
            root.after(sec1)
            text_var.set(f"{words[0:int(i)+1]+'|'}")
            text_label.update()
        root.after(sec_between)
        index = 1
        if Deleting_effect == True:
            for i in reversed(range(len(words))):
                root.after(sec2)
                text_var.set(f"{words[0:int(i)]+'| '}")
                text_label.update()

    app_title_dat = StringVar()
    app_title = Label(
        textvariable=app_title_dat,
        pady=10,
        font="Sublime 15 bold",
        bg="white",
        fg="#2b2b2b",
    )
    remove_list.append(app_title)
    app_title.pack(pady=300)
    sub_title_var = StringVar()
    sub_title = Label(
        textvariable=sub_title_var,
        font="Sublime 8 italic bold",
        fg="#9e9e9e",
        bg="white",
    )
    remove_list.append(sub_title)
    sub_title.place(x=595, y=360)

    def startup1():
        words = "PassGen"
        app_title.config(font="Times 35 bold", fg="#2b2b2b")
        Typing_Effect_Cursor(root, words, 70, 0, 30, False, app_title_dat, app_title)
        canvas = Canvas(root, height=136, width=136, bg="white", borderwidth=0)
        canvas.place(x=775, y=280)
        remove_list.append(canvas)
        canvas.create_rectangle(0, 0, 130, 130, outline="white", fill="#959595")
        canvas.create_rectangle(8, 8, 136, 136, outline="#959595", fill="#2b2b2b")
        canvas.create_rectangle(20, 60, 125, 90, outline="white", fill="white")
        canvas.create_rectangle(25, 65, 120, 85, outline="#959595", fill="#2b2b2b")
        canvas.create_text(
            75, 82, text="* * * *", fill="white", font=("Helvetica 20 bold")
        )

    def startup2():
        words = "Create/Secure Your Passwords!"
        Typing_Effect_Cursor(root, words, 10, 1500, 5, True, sub_title_var, sub_title)
        for i in remove_list:
            i.destroy()
        root.resizable(True, True)
        root.state("normal")
        root.after(1000)
        root.geometry("700x500")
        root.resizable(False, False)
        Home_Screen()

    def startup():
        threading.Thread(target=startup2).start()
        startup1()

    for i in range(0, 3):
        words = PasswordGengrator()
        word = words.random_password(14)
        if i == 2:
            word = words.custom_password("Welcome To PassGen")
        Typing_Effect_Cursor(root, word, 30, 1000, 10, True, app_title_dat, app_title)
    startup()
# Done
# =============================Home Screen=================================

Create_new_password_img_main = Image.open(rf"{file_path}\Images\Button.png")


def round_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [
        x1 + radius,
        y1,
        x1 + radius,
        y1,
        x2 - radius,
        y1,
        x2 - radius,
        y1,
        x2,
        y1,
        x2,
        y1 + radius,
        x2,
        y1 + radius,
        x2,
        y2 - radius,
        x2,
        y2 - radius,
        x2,
        y2,
        x2 - radius,
        y2,
        x2 - radius,
        y2,
        x1 + radius,
        y2,
        x1 + radius,
        y2,
        x1,
        y2,
        x1,
        y2 - radius,
        x1,
        y2 - radius,
        x1,
        y1 + radius,
        x1,
        y1 + radius,
        x1,
        y1,
    ]
    return canvas.create_polygon(points, **kwargs, smooth=True)


def logo():
    app_title = Label(
        root, text="PassGen|", pady=20, font="Times 25 bold", bg="white", fg="#2b2b2b"
    )
    app_title.place(x=250, y=0)
    canvas_title = Canvas(
        root, height=70, width=70, bg="white", borderwidth=0, relief=FLAT
    )
    canvas_title.place(x=380, y=10)
    canvas_title.create_rectangle(0, 0, 64, 64, outline="white", fill="#959595")
    canvas_title.create_rectangle(8, 8, 70, 70, outline="#959595", fill="#2b2b2b")
    canvas_title.create_rectangle(20, 30, 60, 50, outline="white", fill="white")
    canvas_title.create_rectangle(23, 33, 57, 47, outline="#959595", fill="#2b2b2b")
    canvas_title.create_text(
        41, 43, text="* * * *", fill="white", font=("Helvetica 10 bold")
    )


HOME_IMG = Create_new_password_img_main.resize((50, 20), Image.ANTIALIAS)
HOME_IMG = ImageTk.PhotoImage(HOME_IMG)


def home():
    try:
        root.destroy()
    finally:
        with open(rf"{file_path}\Data\index.pak", "w") as dataas:
            dataaas = dataas.write("0")
        os.system(rf'"{file_path}\\PassGen.exe"')
        os.system("taskkill /im cmd.exe /t /f")


def Home_Screen():
    try:
        os.system("taskkill /im cmd.exe /f")
    except Exception as e:
        pass
    global drop_down_list, remove_list_Drop, drop_list_save_password, remove_list_save
    root.config(bg="white")
    root.resizable(True, True)
    root.state("normal")
    root.after(1000)
    root.geometry("700x500")
    root.resizable(False, False)

    Create_new_password_img = Create_new_password_img_main.resize(
        (200, 40), Image.ANTIALIAS
    )
    Create_new_password_img = ImageTk.PhotoImage(Create_new_password_img)
    drop_down_list = []
    remove_list_Drop = []
    drop_list_save_password = []
    remove_list_save = []

    def Create_new_password():
        global drop_down_list, remove_list_Drop
        Gen_pass_img = Image.open(rf"{file_path}\\Images\Button.png ")
        Gen_pass_img = Gen_pass_img.resize((150, 30), Image.ANTIALIAS)
        Gen_pass_img = ImageTk.PhotoImage(Gen_pass_img)
        if len(drop_down_list) == 0:
            Create_new_password_btn.config(text="Create Password   ⮝")
            Saved_Passwords_btn.place(x=248, y=300)
            drop_down_list.append("0")
            canvas_Create_password = Canvas(
                root,
                height=70,
                width=142,
                bg="#2b2b2b",
                borderwidth=0,
                bd=0,
                highlightthickness=0,
            )
            remove_list_Drop.append(canvas_Create_password)
            remove_list.append(canvas_Create_password)
            canvas_Create_password.place(x=308, y=230)
            canvas_Create_password.create_rectangle(
                0, 0, 145, 75, outline="#2b2b2b", fill="#2b2b2b"
            )
            Genrate_password = Button(
                canvas_Create_password,
                text="Generate Password",
                bg="#434343",
                font="Times 12 bold",
                borderwidth=0,
                fg="white",
                command=GeneratePassword,
            )
            Genrate_password.place(x=1, y=12)
            remove_list.append(Genrate_password)
            Secure_Your_password = Button(
                canvas_Create_password,
                text="Secure Password",
                bg="#525252",
                font="Times 13 bold",
                justify=LEFT,
                borderwidth=0,
                fg="white",
                padx=5,
                command=Secure_password,
            )
            remove_list.append(Secure_Your_password)
            Secure_Your_password.place(x=1, y=42)
        else:
            for i in remove_list_Drop:
                i.destroy()

            Create_new_password_btn.config(text="Create Password   ⮟")
            Saved_Passwords_btn.place(x=248, y=250)
            drop_down_list = []

    def GeneratePassword():
        for i in remove_list:
            i.destroy()
        GenPass_img = Create_new_password_img_main.resize((170, 37), Image.ANTIALIAS)
        GenPass_img = ImageTk.PhotoImage(GenPass_img)

        def password():
            global your_password_secure
            lenth = lenth_of_password.get()
            Password.delete("1.0", "end")
            your_password_secure = PasswordGengrator.random_password(root, lenth)
            Password.insert(0.0, your_password_secure)
            root.update()

        def copy():
            global wanna_save_btn
            root.clipboard_clear()
            root.clipboard_append(Password.get("1.0", END))
            messagebox.showinfo(
                "PassGen - Create/Secure Passwords",
                f"""Password "{Password.get("1.0",END)}" Copied to Clipboard!""",
            )
            wanna_save_btn = Button(
                text="Wanna Save? ⮟",
                command=Save_Password,
                compound=CENTER,
                image=GenPass_img,
                font="times 10 bold",
                bg="white",
                fg="white",
                borderwidth=0,
            )
            wanna_save_btn.place(x=300, y=270)

        def Save_Password():
            global drop_list_save_password, remove_list_save

            def save_button():
                from main import Save

                password = Password.get("0.0", END)
                website = website_text.get("1.0", END)
                id = id_text.get("1.0", END)
                allowed_char = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,1,2,3,4,5,6,7,8,9,0,!,@,#,$,%,^,&,*,(,),_,+,=,."
                allowed_char_1 = allowed_char.split(",")
                check = f'{Password.get("0.0",END)}{website_text.get("1.0",END)}{id_text.get("1.0",END)}'
                check = check.replace("\n", "")
                for i in check:
                    if i not in allowed_char_1:
                        messagebox.showerror(
                            "PassGen - Create/Secure Passwords",
                            f"""Invaild Character! "{i}" \n Allowed Characters are: {allowed_char}""",
                        )
                        GeneratePassword()
                        break
                    else:
                        pass

                if id == "" or "example_faraaz":
                    id = "Unknown"
                Save.encrypt(website=website, password=password, id=id, save=True)
                messagebox.showinfo(
                    "PassGen - Create/Secure Passwords", f"""Data Saved Successfully!"""
                )
                Save_Password()

            if len(drop_list_save_password) == 0:
                Save_btn_img = Create_new_password_img_main.resize(
                    (85, 25), Image.ANTIALIAS
                )
                Save_btn_img = ImageTk.PhotoImage(Save_btn_img)
                wanna_save_btn.config(text="Wanna Save? ⮝")
                drop_list_save_password.append("0")
                canvas_Save_password = Canvas(
                    root,
                    height=100,
                    width=300,
                    bg="white",
                    borderwidth=0,
                    bd=0,
                    highlightthickness=0,
                )
                canvas_Save_password.place(x=200, y=320)
                remove_list_save.append(canvas_Save_password)
                my_rectangle = round_rectangle(
                    canvas_Save_password, 0, 0, 300, 100, radius=40, fill="#eeeded"
                )
                website_label = Label(
                    canvas_Save_password,
                    text="Website: ",
                    bg="#eeeded",
                    font="times 15 bold",
                    fg="#2b2b2b",
                )
                website_label.place(x=10, y=10)
                website_text = Text(
                    canvas_Save_password,
                    bg="#4c4c4c",
                    fg="white",
                    height=1,
                    width=20,
                    font="times 12",
                    borderwidth=2,
                    relief=RIDGE,
                )
                website_text.place(x=100, y=10)
                website_text.insert("1.0", "example.com")
                id_label = Label(
                    canvas_Save_password,
                    text="Site Id: ",
                    bg="#eeeded",
                    font="times 12 bold",
                    fg="#2b2b2b",
                )
                id_text = Text(
                    canvas_Save_password,
                    bg="#cbcbcb",
                    fg="#4c4c4c",
                    height=1,
                    width=26,
                    font="times 10",
                    borderwidth=2,
                    relief=RIDGE,
                )
                id_text.insert("1.0", "example_faraaz")
                id_text.place(x=100, y=45)
                id_label.place(x=37, y=43)
                Save_btn = Button(
                    canvas_Save_password,
                    text="Save Password",
                    bg="#eeeded",
                    fg="white",
                    image=Save_btn_img,
                    borderwidth=0,
                    compound="center",
                    font="Times 8 bold",
                    command=save_button,
                )
                Save_btn.image = Save_btn_img
                Save_btn.place(x=110, y=70)

            else:
                wanna_save_btn.config(text="Wanna Save? ⮟")
                for i in remove_list_save:
                    i.destroy()
                drop_list_save_password = []

        Generate = Button(
            text="Generate Password |",
            command=password,
            compound=CENTER,
            image=GenPass_img,
            font="times 10 bold",
            bg="white",
            fg="white",
            borderwidth=0,
        )
        Generate.image = GenPass_img
        Generate.place(x=70, y=168)
        GenPass_img = Create_new_password_img_main.resize((100, 37), Image.ANTIALIAS)
        GenPass_img = ImageTk.PhotoImage(GenPass_img)
        copy_text = Button(
            text="  Copy",
            command=copy,
            compound=CENTER,
            image=GenPass_img,
            font="times 15 bold",
            bg="white",
            fg="white",
            borderwidth=0,
        )

        copy_text.image = GenPass_img
        copy_text.place(x=530, y=168)
        border_color = Frame(root, background="white")
        lenth_of_password = Scale(
            border_color,
            from_=8,
            to=100,
            orient="horizontal",
            bg="white",
            borderwidth=0,
        )
        Password = Text(
            border_color,
            bg="#4c4c4c",
            fg="white",
            height=1,
            width=23,
            font="times 20",
            borderwidth=2,
            relief=RIDGE,
        )
        border_color.place(x=220, y=170)
        Password.pack()
        lenth_of_password.pack(side=BOTTOM, fill=X)

    def Secure_password():
        for i in remove_list:
            i.destroy()
        GenPass_img = Create_new_password_img_main.resize((170, 37), Image.ANTIALIAS)
        GenPass_img = ImageTk.PhotoImage(GenPass_img)

        def password():
            global your_password_secure
            password = Password.get("0.0", END)
            your_password_secure = PasswordGengrator.custom_password(root, password)
            Password.insert(0.0, your_password_secure)
            root.update()

        def copy():
            global wanna_save_btn
            root.clipboard_clear()
            root.clipboard_append(Password.get("1.0", END))
            messagebox.showinfo(
                "PassGen - Create/Secure Passwords",
                f"""Password "{Password.get("1.0",END)}" Copied to Clipboard!""",
            )
            wanna_save_btn = Button(
                text="Wanna Save? ⮟",
                command=Save_Password,
                compound=CENTER,
                image=GenPass_img,
                font="times 10 bold",
                bg="white",
                fg="white",
                borderwidth=0,
            )
            wanna_save_btn.place(x=263, y=270)

        def Save_Password():
            global drop_list_save_password, remove_list_save, remove_list

            def save_button():
                from main import Save

                password = Password.get("0.0", END)
                password = password.replace(" ", "")
                website = website_text.get("1.0", END)
                id = id_text.get("1.0", END)
                allowed_char = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,1,2,3,4,5,6,7,8,9,0,!,@,#,$,%,^,&,*,(,),_,+,=,."
                allowed_char_1 = allowed_char.split(",")
                check = f'{Password.get("0.0",END)}{website_text.get("1.0",END)}{id_text.get("1.0",END)}'
                check = check.replace("\n", "")
                for i in check:
                    if i not in allowed_char_1:
                        messagebox.showerror(
                            "PassGen - Create/Secure Passwords",
                            f"""Invaild Character! "{i}" \n Allowed Characters are: {allowed_char}""",
                        )
                        return
                        break
                    else:
                        pass
                if id == "" or "example_faraaz":
                    id = "Unknown"
                Save.encrypt(website=website, password=password, id=id, save=True)
                messagebox.showinfo(
                    "PassGen - Create/Secure Passwords", f"""Data Saved Successfully!"""
                )
                home()

            if len(drop_list_save_password) == 0:
                Save_btn_img = Create_new_password_img_main.resize(
                    (85, 25), Image.ANTIALIAS
                )
                Save_btn_img = ImageTk.PhotoImage(Save_btn_img)
                wanna_save_btn.config(text="Wanna Save? ⮝")
                drop_list_save_password.append("0")
                canvas_Save_password = Canvas(
                    root,
                    height=100,
                    width=300,
                    bg="white",
                    borderwidth=0,
                    bd=0,
                    highlightthickness=0,
                )
                canvas_Save_password.place(x=200, y=320)
                remove_list_save.append(canvas_Save_password)
                my_rectangle = round_rectangle(
                    canvas_Save_password, 0, 0, 300, 100, radius=40, fill="#eeeded"
                )
                website_label = Label(
                    canvas_Save_password,
                    text="Website: ",
                    bg="#eeeded",
                    font="times 15 bold",
                    fg="#2b2b2b",
                )
                website_label.place(x=10, y=10)
                website_text = Text(
                    canvas_Save_password,
                    bg="#4c4c4c",
                    fg="white",
                    height=1,
                    width=20,
                    font="times 12",
                    borderwidth=2,
                    relief=RIDGE,
                )
                website_text.place(x=100, y=10)
                website_text.insert("1.0", "https://example.com")
                id_label = Label(
                    canvas_Save_password,
                    text="Site Id: ",
                    bg="#eeeded",
                    font="times 12 bold",
                    fg="#2b2b2b",
                )
                id_text = Text(
                    canvas_Save_password,
                    bg="#cbcbcb",
                    fg="#4c4c4c",
                    height=1,
                    width=26,
                    font="times 10",
                    borderwidth=2,
                    relief=RIDGE,
                )
                id_text.insert("1.0", "example_faraaz")
                id_text.place(x=100, y=45)
                id_label.place(x=37, y=43)
                Save_btn = Button(
                    canvas_Save_password,
                    text="Save Password",
                    bg="#eeeded",
                    fg="white",
                    image=Save_btn_img,
                    borderwidth=0,
                    compound="center",
                    font="Times 8 bold",
                    command=save_button,
                )
                Save_btn.image = Save_btn_img
                Save_btn.place(x=110, y=70)

            else:
                wanna_save_btn.config(text="Wanna Save? ⮟")
                for i in remove_list_save:
                    i.destroy()
                drop_list_save_password = []

        Secure = Button(
            text="Secure Password |",
            command=password,
            compound=CENTER,
            image=GenPass_img,
            font="times 10 bold",
            bg="white",
            fg="white",
            borderwidth=0,
        )
        Secure.image = GenPass_img
        Secure.place(x=70, y=168)
        SecPass_img = Create_new_password_img_main.resize((100, 37), Image.ANTIALIAS)
        SecPass_img = ImageTk.PhotoImage(SecPass_img)
        copy_text = Button(
            text="  Copy",
            command=copy,
            compound=CENTER,
            image=SecPass_img,
            font="times 15 bold",
            bg="white",
            fg="white",
            borderwidth=0,
        )

        copy_text.image = SecPass_img
        copy_text.place(x=530, y=168)
        border_color = Frame(root, background="white")
        Password = Text(
            border_color,
            bg="#4c4c4c",
            fg="white",
            height=1,
            width=23,
            font="times 20",
            borderwidth=2,
            relief=RIDGE,
        )
        Password.insert("0.0", "Insert a Password")
        border_color.place(x=220, y=170)
        Password.pack()

    logo()

    Create_new_password_btn = Button(
        text="Create Password   ⮟",
        bg="white",
        fg="white",
        image=Create_new_password_img,
        borderwidth=0,
        compound="center",
        font="Times 15 bold",
        command=Create_new_password,
    )
    remove_list.append(Create_new_password_btn)
    Create_new_password_btn.image = Create_new_password_img
    Create_new_password_btn.pack(side=TOP, pady=200)

    Saved_Passwords_btn = Button(
        text="Saved Password",
        bg="white",
        fg="white",
        image=Create_new_password_img,
        borderwidth=0,
        compound="center",
        font="Times 15 bold",
        command=Saved_Password,
    )
    remove_list.append(Saved_Passwords_btn)
    Saved_Passwords_btn.place(x=248, y=250)

    home_btn = Button(
        text="ᐊ HOME",
        bg="white",
        fg="#2b2b2b",
        borderwidth=0,
        font="Times 10 bold",
        command=home,
    ).place(x=1, y=10)


def Saved_Password():
    from main import Save

    Basic_File_exits = os.path.isfile(f"{file_path}\\Data\\lan.pak")
    for i in remove_list:
        i.destroy()

    def confirmed():
        from main import Save

        for i in remove_list:
            i.destroy()
        # delete_img=Image.open(r".\Images\delete.png")
        # delete_img=delete_img.resize((30,40),Image.ANTIALIAS)
        # delete_img=ImageTk.PhotoImage(delete_img)
        try:
            with open(rf"{file_path}\Data\Pydat.pgdt", "r") as datas:
                data = datas.read()
            data = data.split("next")
            if "" in data:
                a = data.index("")
                del data[a]
            decrypted = []
            for i in data:
                j = i.split("|")
                k = Save.decrypt(website=j[0], id=j[1], password=j[2])
                decrypted.append(k)
        except:
            data = []
        container = Frame(root)
        canvas = Canvas(container, height=1000, bg="white", highlightthickness=0)
        scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas)
        scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        y1 = 125
        y2 = 250
        decrypted_keys_store = {}
        try:
            for n, i in enumerate(decrypted):
                for num, j in enumerate(i):
                    if num == 0:
                        decrypted_keys_store[f"Website[{n}]"] = j
                    elif num == 1:
                        decrypted_keys_store[f"Site_ID[{n}]"] = j
                    elif num == 2:
                        decrypted_keys_store[f"Password[{n}]"] = j
        except:
            pass
        if len(data) == 0:
            round_rectangle(canvas, 53, y1, 630, y2, radius=20, fill="#eeeded")
            label = Label(
                text="There seems no Saved data to read,\nPlease add Passwords from the Generate or Secure Password Tab.",
                font="times 15 bold italic",
                fg="#2b2b2b",
                bg="#eeeded",
            )
            label.place(x=65, y=y1 + 25)
        else:
            for i in range(len(data)):
                # delete_btn= Button(canvas, text = f"{i}", anchor = W,image=delete_img,borderwidth=0,bg="#eeeded",highlightbackground="white",command=deleting)
                # ab.append(delete_btn)
                # delete_btn.image=delete_img
                # delete_btn.configure(activebackground = "#eeeded", relief = FLAT)
                # button1_window = canvas.create_window(590, y1+75, anchor=NW, window=delete_btn)

                round_rectangle(canvas, 53, y1, 630, y2, radius=20, fill="#eeeded")
                website_name_label = canvas.create_text(
                    100 + 20,
                    y1 + 25,
                    text="Website: ",
                    font="times 17 bold",
                    fill="#2b2b2b",
                )
                website_data = Text(
                    canvas,
                    bg="#4c4c4c",
                    fg="white",
                    height=1,
                    width=15,
                    font="times 15",
                    borderwidth=2,
                    relief=RIDGE,
                )

                website_data.insert("0.0", decrypted_keys_store[f"Website[{i}]"])
                website_data.config(state=DISABLED)
                canvas.create_window(250, y1 + 27, window=website_data)

                site_id = canvas.create_text(
                    400, y1 + 25, text="Site ID: ", font="times 17 bold", fill="#2b2b2b"
                )
                site_id = Text(
                    canvas,
                    bg="#4c4c4c",
                    fg="white",
                    height=1,
                    width=15,
                    font="times 15",
                    borderwidth=2,
                    relief=RIDGE,
                )
                site_id.insert("0.0", decrypted_keys_store[f"Site_ID[{i}]"])
                site_id.config(state=DISABLED)
                canvas.create_window(530, y1 + 27, window=site_id)

                password_label = canvas.create_text(
                    120,
                    y1 + 73,
                    text="Password: ",
                    font="times 15 bold",
                    fill="#2b2b2b",
                )
                password = Text(
                    canvas,
                    bg="#4c4c4c",
                    fg="white",
                    height=1,
                    width=15,
                    font="times 15 bold",
                    borderwidth=2,
                    relief=RIDGE,
                )
                password.insert("0.0", decrypted_keys_store[f"Password[{i}]"])
                password.config(state=DISABLED)
                canvas.create_window(250, y1 + 75, window=password)

                y1 += 150
                y2 += 150
        BG = Label(
            root,
            text="",
            pady=22,
            padx=340,
            font="Times 25 bold",
            bg="white",
            fg="#2b2b2b",
        )
        BG.place(x=0, y=0)
        logo()
        home_btn = Button(
            text="ᐊ HOME",
            bg="white",
            fg="#2b2b2b",
            borderwidth=0,
            font="Times 10 bold",
            command=home,
        ).place(x=1, y=10)
        canvas.configure(scrollregion=canvas.bbox("all"))
        scrollbar.pack(side="right", fill="y")
        container.pack(fill="both")
        canvas.pack(fill="both", expand=True)

    if Basic_File_exits == False:
        canvas = Canvas(root, bg="white", highlightthickness=0, height=1000)
        remove_list.append(canvas)

        def save_btn():
            password_1 = text1.get(0.0, END)
            yesorno = messagebox.askokcancel(
                "PassGen - Create/Secure Passwords ",
                f"Confirm Your Password: {password_1}",
            )
            if yesorno == True:
                en = Save.encrypt(password_1, "none", "none", save=False)
                with open(rf"{file_path}\Data\lan.pak", "w") as dat:
                    dat.write(en[0])
                home()
            else:
                pass

        round_rectangle(canvas, 70, 180, 633, 380, radius=20, fill="#eeeded")
        text1 = Text(
            root, width=7, height=1, font="sublime 100 bold", bg="#eeeded", relief=FLAT
        )
        text1.place(x=90, y=202)
        remove_list.append(text1)
        labeling = canvas.create_text(
            370, 190, text="Enter a Password:", font="Times 20 bold"
        )
        text1.focus_set()
        canvas.pack(fill="both")
        logo()
        wanna_save_btn = Button(
            text="Save",
            font="times 10 bold",
            bg="#cdcdcd",
            fg="BLACK",
            relief=SUNKEN,
            command=save_btn,
        )
        wanna_save_btn.place(x=570, y=185)
        remove_list.append(wanna_save_btn)
    else:
        with open(rf"{file_path}\Data\lan.pak", "r") as datas:
            data = datas.read()
        canvas = Canvas(root, bg="white", highlightthickness=0, height=1000)
        remove_list.append(canvas)
        password_confirm = Save.decrypt("none", "none", password=data)

        def confirming():
            password_no = text1.get("0.0", END)
            password_no = password_no.replace("\n", "")
            if password_confirm[2] == password_no:
                confirmed()
            else:
                messagebox.showerror(
                    "PassGen - Create/Secure Passwords ",
                    "Password Mismatch, Please Enter the correct Password!",
                )

        round_rectangle(canvas, 70, 180, 633, 380, radius=20, fill="#eeeded")
        text1 = Text(
            root, width=7, height=1, font="sublime 100 bold", bg="#eeeded", relief=FLAT
        )
        text1.place(x=90, y=202)
        remove_list.append(text1)
        labeling = canvas.create_text(
            370, 190, text="Password Please:", font="Times 20 bold"
        )
        text1.focus_set()
        canvas.pack(fill="both")
        logo()
        confirm = Button(
            text="Enter",
            font="times 10 bold",
            bg="#cdcdcd",
            fg="BLACK",
            relief=SUNKEN,
            command=confirming,
        )
        remove_list.append(confirm)
        confirm.place(x=570, y=185)


try:
    if Basic_File_exits_2 == True:
        Home_Screen()
        os.remove(f"{file_path}\\Data\\index.pak")
finally:
    pass
    # if Basic_File_exits_2==True:
    #     Home_Screen()
    #     os.remove(f"{file_path}\\Data\\index.pak")


root.mainloop()
