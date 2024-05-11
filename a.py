import tkinter as tk
import time


from main import PasswordGengrator
from PIL import ImageTk, Image
import threading, pickle, os, sys

python_dir = sys.executable

file_path = os.path.dirname(os.path.realpath(__file__))
Basic_File_exits_2 = os.path.isfile(f"{file_path}\\Data\\index.pak")
index = 0


class Commons:
    def Typing_Effect_Cursor(
        self,
        root,
        words,
        text_var,
        text_label,
        write_delay,
        sec_between,
        delete_delay,
        Deleting_effect=False,
    ):
        """Use's Label and textvariables to create a Typing effect and cursor effect"""

        for i, j in enumerate(words):
            root.after(write_delay)
            text_var.set(f"{words[0:int(i)+1]+'|'}")
            text_label.update()
        root.after(sec_between)
        index = 1
        if Deleting_effect == True:
            for i in reversed(range(len(words))):
                root.after(delete_delay)
                text_var.set(f"{words[0:int(i)]+'| '}")
                text_label.update()

    def Logo(self, master_root, Effect=False, FramePlace_parameter=None, sublogo=False):
        """Create's the PassGen Logo Using Label and Canvas"""

        words = ("PassGen", "Create/Secure Your Passwords!")

        main_frame = tk.Frame(master_root, height=150, width=600, bg="white")
        if Effect:
            main_frame.place(FramePlace_parameter)

        Logo_var = tk.StringVar()
        Logo_label = tk.Label(
            main_frame,
            bg="white",
            font="Times 35 bold",
            fg="#2b2b2b",
            textvariable=Logo_var,
        )
        Logo_label.place(relx=0.4, rely=0.5, anchor="center")

        if Effect:
            self.Typing_Effect_Cursor(
                self=self,
                root=master_root,
                words=words[0],
                write_delay=70,
                sec_between=0,
                delete_delay=30,
                Deleting_effect=False,
                text_var=Logo_var,
                text_label=Logo_label,
            )
        else:
            Logo_var.set(words[0])

        canvas = tk.Canvas(main_frame, height=136, width=136, bg="white", borderwidth=0)
        canvas.place(relx=0.68, rely=0.5, anchor="center")
        canvas.create_rectangle(0, 0, 130, 130, outline="white", fill="#959595")
        canvas.create_rectangle(8, 8, 136, 136, outline="#959595", fill="#2b2b2b")
        canvas.create_rectangle(20, 60, 125, 90, outline="white", fill="white")
        canvas.create_rectangle(25, 65, 120, 85, outline="#959595", fill="#2b2b2b")
        canvas.create_text(
            75, 82, text="* * * *", fill="white", font=("Helvetica 20 bold")
        )
        if sublogo:
            subintro_var = tk.StringVar()
            subintro_label = tk.Label(
                main_frame,
                textvariable=subintro_var,
                font="Sublime 8 italic bold",
                fg="#9e9e9e",
                bg="white",
            )
            subintro_label.place(relx=0.4, rely=0.8, anchor="center")
            if Effect:
                self.Typing_Effect_Cursor(
                    self=self,
                    root=master_root,
                    words=words[1],
                    write_delay=10,
                    sec_between=1500,
                    delete_delay=5,
                    Deleting_effect=False,
                    text_var=subintro_var,
                    text_label=subintro_label,
                )
            else:
                subintro_var.set(words[1])
        if not Effect:
            return main_frame

    @staticmethod
    def Delete_Page(root):
        """Delete's all the children of the master root"""

        for i in root.winfo_children():
            i.destroy()


class StartUp:
    """Creates widgets required during startup"""

    def __init__(self, root, mgr=1):
        self.root = root
        super().__init__()
        self.passgen, self.commons = PasswordGengrator(), Commons

        ### Title bar
        # Title icon
        p1 = tk.PhotoImage(file=f"{file_path}\Images\logo.png")
        self.root.iconphoto(True, p1)

        self.root.title("PassGen - Create/Secure Passwords ")
        self.root.resizable(False, False)
        self.root.geometry("700x500")
        self.root.config(bg="white")

        self.Intro_var = tk.StringVar()
        if mgr:
            self.main()

    def Intro_Random(self):
        self.Intro_label = tk.Label(
            self.root,
            textvariable=self.Intro_var,
            pady=10,
            font="Sublime 15 bold",
            bg="white",
            fg="#2b2b2b",
        )
        self.Intro_label.place(relx=0.5, rely=0.5, anchor="center")

        for i in range(0, 3):
            word = self.passgen.random_password(14)
            if i == 2:
                word = self.passgen.custom_password("Welcome To PassGen")

            self.commons.Typing_Effect_Cursor(
                self=self.commons,
                root=self.root,
                words=word,
                write_delay=30,
                sec_between=1000,
                delete_delay=10,
                Deleting_effect=True,
                text_var=self.Intro_var,
                text_label=self.Intro_label,
            )

    def Intro_Title(self):

        self.Intro_label.destroy()

        self.commons.Logo(
            self=self.commons,
            master_root=self.root,
            Effect=True,
            FramePlace_parameter={"relx": 0.5, "rely": 0.5, "anchor": "center"},
            sublogo=True,
        )

    def main(self):
        self.Intro_Random()
        self.root.after(500)
        self.Intro_Title()
        self.root.after(200)
        self.commons.Delete_Page(root=self.root)


class Home:
    """Creates the widget in Main Page/Home"""

    def __init__(self, root):
        self.root = root
        self.commons = Commons()
        Button_image = Image.open(rf"{file_path}\Images\Button.png")
        Button_image_home = Button_image.resize((200, 40), Image.Resampling.LANCZOS)
        self.Button_image_home = ImageTk.PhotoImage(Button_image_home)

        self.GenratePassword = lambda: GeneratePassword(
            root=self.root, Button_image=Button_image
        )

        Logo = self.commons.Logo(
            master_root=self.root,
            Effect=False,
        )
        Logo.pack(side="top", anchor="center")

    def window(self):
        Generate_password_btn = tk.Button(
            self.root,
            text="Generate Password",
            bg="white",
            fg="white",
            image=self.Button_image_home,
            borderwidth=0,
            compound="center",
            font="Times 15 bold",
            command=self.GenratePassword,
        )
        Generate_password_btn.place(relx=0.5, rely=0.5, anchor="center")

        Secure_password_btn = tk.Button(
            self.root,
            text="Secure Password",
            bg="white",
            fg="white",
            image=self.Button_image_home,
            borderwidth=0,
            compound="center",
            font="Times 15 bold",
        )
        Secure_password_btn.place(relx=0.5, rely=0.6, anchor="center")

        Saved_Passwords_btn = tk.Button(
            self.root,
            text="Saved Password",
            bg="white",
            fg="white",
            image=self.Button_image_home,
            borderwidth=0,
            compound="center",
            font="Times 15 bold",
            command="Saved_Password",
        )
        Saved_Passwords_btn.place(relx=0.5, rely=0.7, anchor="center")

        # home_btn = Button(
        #     text="ᐊ HOME",
        #     bg="white",
        #     fg="#2b2b2b",
        #     borderwidth=0,
        #     font="Times 10 bold",
        #     command=home,
        # ).place(x=1, y=10)


'''
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

'''


class GeneratePassword(Commons):
    def __init__(self, root, Button_image):
        self.root = root
        self.Delete_Page(self.root)
        self.Button_image = Button_image
        Button_image_GenPass = Button_image.resize((200, 40), Image.Resampling.LANCZOS)
        self.Button_image_GenPass = ImageTk.PhotoImage(Button_image_GenPass)
        self.window()

    def window(self):
        Generate_btn = tk.Button(
            self.root,
            text="Generate Password |",
            command="password",
            compound="center",
            image=self.Button_image_GenPass,
            font="times 10 bold",
            bg="white",
            fg="white",
            borderwidth=0,
        )
        Generate_btn.image = self.Button_image_GenPass
        Generate_btn.place(x=65, y=168)

        CopyPass_img = self.Button_image.resize((100, 37), Image.Resampling.LANCZOS)
        CopyPass_img = ImageTk.PhotoImage(CopyPass_img)
        copy_text_btn = tk.Button(
            self.root,
            text="  Copy",
            command="copy",
            compound="center",
            image=CopyPass_img,
            font="times 15 bold",
            bg="white",
            fg="white",
            borderwidth=0,
        )
        copy_text_btn.image = CopyPass_img
        copy_text_btn.place(x=530, y=168)

        lenth_of_password = tk.Scale(
            self.root,
            from_=8,
            to=100,
            orient="horizontal",
            bg="white",
            borderwidth=0,
        )
        Password_input = tk.Text(
            self.root,
            bg="#4c4c4c",
            fg="white",
            height=1,
            width=23,
            font="times 20",
            borderwidth=2,
            relief="ridge",
        )
        Password_input.place(x=220, y=170)
        lenth_of_password.pack(side="bottom", fill="x", pady=50)


if __name__ == "__main__":
    root = tk.Tk()

    a = StartUp(root, mgr=0)

    b = Home(root=root)
    b.window()
    root.mainloop()
