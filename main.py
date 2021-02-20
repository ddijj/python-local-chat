import sys
import time
from datetime import datetime

print("Copyright (c) 2020 ddijj")
print("python-local-chat")

sere=1
sure=["log.txt","log-2.txt"]
chat =[]
l=[]
ban =[]
name = input("名前を入力：")
with open('user.txt','r',encoding = "utf_8") as f1:
    user = [s.strip() for s in f1.readlines()]
with open('pass.txt','r',encoding = "utf_8") as f1:
    passe = [s.strip() for s in f1.readlines()]
with open('ban.txt','r',encoding = "utf_8") as f1:
    ban = [s.strip() for s in f1.readlines()]
if name in user:
    pase = input("パスワードを入力:")
    if pase == passe[user.index(name)] and not name in ban:
        print("system:ログイン成功")
    else: 
       sys.exit()
else:
    with open('user.txt', 'a',encoding = "utf_8") as f:
         f.write(name+"\n")
    pase = input("パスワードを設定:")
    with open('pass.txt', 'a',encoding = "utf_8") as f:
         f.write(pase+"\n")
print("<会話ログ>")
with open(sure[sere],'r',encoding = "utf_8") as f1:
    l = [s.strip() for s in f1.readlines()]
    s_n= '\n'.join(l)
    print(s_n)
while(1==1):
    c = input("文章を入力：")
    if c == "/dl":
        with open(sure[sere],'r',encoding = "utf_8") as f1:
            l = [s.strip() for s in f1.readlines()]
            s_n= '\n'.join(l)
            print(s_n)
    elif c == "/help":
        print("コマンド一覧"+"\n")
        print("/dl...保存されているログを読み込み"+"\n")
        print("/user...ユーザーの一覧を表示"+"\n")
        print("/out...チャットを停止"+"\n")
        print("/channel...チャンネルの切替")
    elif c=="/book":
        print("0...メインのチャンネル")
        print("1...サブののチャンネル")
    elif c == "/out":
        sys.exit()
    elif c == "/user":
        with open(sure[sere],'r',encoding = "utf_8") as f1:
            user = [s.strip() for s in f1.readlines()]
            s_n= '\n'.join(user)
            print(s_n)
    elif c == "/dh" and name=="ddijj":
        pase = input("パスワードを入力:")
        if pase == "pass":
            with open(sure[sere], 'w',encoding = "utf_8") as f:
                f.write("system:管理者が削除しました"+"\n")
        else:
            print("system:ログインに失敗しました")
    elif c== "/ban" and name == "ddijj":
        pase = input("パスワードを入力:")
        if pase == "pass":
            gg = input("ban者を入力>")
            with open('ban.txt', 'w') as f:
                f.writelines(gg)
    elif c=="/channel":
        sere = int(input("チャンネル番号を入力>"))
        with open(sure[sere],'r',encoding = "utf_8") as f1:
            l = [s.strip() for s in f1.readlines()]
            s_n= '\n'.join(l)
            print(s_n)
    else:              
        chat.append(c)
        l.append(name+":"+c)
        with open(sure[sere], 'a',encoding = "utf_8") as f:
            f.write(name+":"+c+"\n")
        with open(sure[sere],'r',encoding = "utf_8") as f1:
            l = [s.strip() for s in f1.readlines()]
            s_n= '\n'.join(l)
            print(s_n)
        time.sleep(0.5)
