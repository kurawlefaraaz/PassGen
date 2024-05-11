from os import error
import os, random, pickle, string as str_mod, secrets

dir_path = os.path.dirname(os.path.realpath(__file__))  # to take File path`


class PasswordGengrator:
    def __init__(self):
        self.char = str_mod.ascii_letters

        self.nums = str_mod.digits

        self.special = str_mod.punctuation

        self.all_char = self.char + self.nums + self.special

    def random_password(self, pass_len):
        pass_len = int(pass_len)

        password = "".join(secrets.choice(list(self.all_char)) for i in range(pass_len))
        return password

    def custom_password(self, password):
        words_replace = (
            ("s", "$"),
            ("S", "$"),
            ("and", "&"),
            ("a", "@"),
            ("A", "@"),
            ("o", "0"),
            ("O", "0"),
            (" ", "_"),
        )

        for a, b in words_replace:
            password = password.replace(a, b)

        return password


class Encrypt(PasswordGengrator):
    def save_encrpt(self, list_name):
        encryption = (f"'{self.all_char[j]}':'{i}'" for i, j in enumerate(list_name))

        return encryption

    def complexifier():
        try:
            with open(rf"{dir_path}\Data\Pydat.pgdt", "w") as dat:
                dat.write("")
                rangeing = random.randint(0, 30)
                name = ["Pydat", "lan", "Base_dat", "execute"]
                ext = ["dat", "pak", "imp", "dt", "pgdt"]
                for i in range(rangeing):
                    rangeing2 = random.randint(0, 4)
                    with open(
                        rf"{dir_path}\Data\{name[rangeing2]}{i}.{ext[rangeing2]}",
                        "w",
                    ) as dat:
                        dat.write("")
        except:
            pass

    def __init__(self, password, website, id, save=False):
        Basic_File_exits = os.path.isfile(f"{dir_path}\\Data\\Base_dat.dat")

        if Basic_File_exits == True:
            Basic_File_exits_1 = os.path.isfile(f"{dir_path}\\Data\\Pydat.pgdt")
            if Basic_File_exits_1 == False:
                self.complexifier()

            with open(f"{dir_path}\\Data\\Base_dat.dat", "rb") as decryption:
                encryption_vals = pickle.load(decryption)
            encrypt_list = []

            # Replaces
            password = password.replace("\n", "")
            website = website.replace("\n", "")
            id = id.replace("\n", "")
            password = password.replace(":", "")
            website = website.replace(":", "")
            website = website.replace("https//", "")
            id = id.replace(":", "")

            for i in encryption_vals:
                i = i.replace("'", "")
                i = i.split(":")
                encrypt_list.append(i)
            password_en = ""
            encrypt_dict = {a: b for a, b in encrypt_list}

            for i in password:
                a = encrypt_dict[i]
                password_en += a
            id_en = ""
            for i in id:
                a = encrypt_dict[i]
                id_en += a
            web_en = ""
            for i in website:
                a = encrypt_dict[i]
                web_en += a
            if save == True:
                with open(rf"{dir_path}\Data\Pydat.pgdt", "a") as dat:
                    dat.write(f"{web_en}|{id_en}|{password_en}next")
            else:
                return [password_en, web_en, id_en]
        else:
            pswd = [self.random_password(5) for i in range(len(self.all_char))]
            encryptions = self.save_encrpt(pswd)

            with open(f"{dir_path}\\Data\\Base_dat.dat", "wb") as dat:
                pickle.dump(encryptions, dat)
            Encrypt(password, website, id, save=True)


class Decrypt:
    def __init__(self, website, id, password):
        with open(f"{dir_path}\\Data\\Base_dat.dat", "rb") as decryption:
            decryption_vals = pickle.load(decryption)

        decryption_vals = tuple(decryption_vals)
        encrypt_dict = {}
        encrypt_list = []

        for i in decryption_vals:
            i = i.replace("'", "")
            i = i.split(":")
            encrypt_list.append(i)

        for a, b in encrypt_list:
            encrypt_dict[a] = b
        indexes = []
        for a, b in encrypt_list:
            b = encrypt_dict[a]
            indexes.append(b)
        for i in indexes:
            if i in password:
                key_list = list(encrypt_dict.keys())
                val_list = list(encrypt_dict.values())
                ind = val_list.index(i)
                password = password.replace(i, key_list[ind])
        for i in indexes:
            if i in website:
                key_list = list(encrypt_dict.keys())
                val_list = list(encrypt_dict.values())
                ind = val_list.index(i)
                website = website.replace(i, key_list[ind])
        for i in indexes:
            if i in id:
                key_list = list(encrypt_dict.keys())
                val_list = list(encrypt_dict.values())
                ind = val_list.index(i)
                id = id.replace(i, key_list[ind])
        return [website, id, password]


if __name__ == "__main__":
    pass
