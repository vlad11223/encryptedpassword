from cryptography.fernet import  Fernet
'''
def write_key():
    key= Fernet.generate_key()
    with open ("key.key","wb") as key_file:
        key_file.write(key)
'''
def load_key():
    file = open("key.key","rb")
    key=file.read()
    file.close()
    print("Loaded Key:", key)
    return key


key=load_key()
fer=Fernet(key)

def view():
    with open('passwords,txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            decrypted_pass = fer.decrypt(passw.encode()).decode()
            print("utilizator:", user, "| parola:", decrypted_pass)


def add():
    name=input(' nume utilizator')
    pwd=input ("parola:")
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()
    print("Encrypted Password:", encrypted_pwd)
    with open ('passwords,txt','a') as f:
        f.write(name + "|" + encrypted_pwd + "\n")

while True:
    mode=input ("vrei sa adaugi o noua parola la cele deja salvate(view,add) sau q sa iesi)")
    if mode =="q":
        break
    if mode =="view":
        view()
    elif mode=="add":
        add()
    else:
        print("invalid")
        continue

