from flask import Flask,render_template,request
import os

app=Flask(__name__)

dictionary={
    1:"one_mv.mp3",
    2:"two_mv.mp3",
    3:"three_mv.mp3",
    4:"four_mv.mp3",
    5:"five_mv.mp3",
    6:"six_mv.mp3",
    7:"seven_mv.mp3",
    8:"eight_mv.mp3",
    9:"nine_mv.mp3",
    10:"ten_mv.mp3",
    11:"eleven_mv.mp3",
    12:"twelve_mv.mp3",
    13:"thirteen_mv.mp3",
    14:"fourteen_mv.mp3",
    15:"fifteen_mv.mp3",
    16:"sixteen_mv.mp3",
    17:"seventeen_mv.mp3",
    18:"eightteen_mv.mp3",
    19:"nineteen_mv.mp3",
    20:"twenty_mv.mp3",

    30:"thirty_mv.mp3",
    40:"forty_mv.mp3",
    50:"fifty_mv.mp3",
    60:"sixty_mv.mp3",
    70:"seventy_mv.mp3",
    80:"eighty_mv.mp3",
    90:"ninety_mv.mp3",
    100:"hundred_mv.mp3",
    1000:"thousand_mv.mp3",
    "lakh":"lakh_mv.mp3",
    "rus":"rupees_mv.mp3"
}

@app.route('/')
def home():
    return render_template("index.html",send_list=[])

@app.route('/voice',methods=['GET','POST'])
def voice():
    send_list=[]
    stack_money=[]

    if request.method=="POST":
        money=request.form["input_money"]
        
        for x in money[::-1]:
            stack_money.append(int(x))
        print(stack_money)

        while len(stack_money)>0:
            index_val=len(stack_money)-1
            val=stack_money.pop()


            if index_val==0:
                if val!=0:
                    send_list.append(dictionary[val])
                send_list.append(dictionary["rus"])
            elif index_val==1:
                if val!=0:
                    if val==1:
                        val2=stack_money.pop()
                        val=val*10+val2
                        send_list.append(dictionary[val])
                        send_list.append(dictionary["rus"])
                    else:
                        val = val*10
                        send_list.append(dictionary[val])
            elif index_val==2:
                if val!=0:
                    send_list.append(dictionary[val])
                    send_list.append(dictionary[100])
            elif index_val==3:
                if val!=0:
                    send_list.append(dictionary[val])
                    send_list.append(dictionary[1000])
            elif index_val==4:
                if val!=0:
                    if val==1:
                        val2=stack_money.pop()
                        val=val*10+val2
                        send_list.append(dictionary[val])
                        send_list.append(dictionary[1000])
                    else:
                        val=val*10
                        send_list.append(dictionary[val])
            elif index_val==5:
                if val!=0:
                    send_list.append(dictionary[val])
                    send_list.append(dictionary["lakh"])
            elif index_val==6:
                if val!=0:
                    if val==1:
                        val2=stack_money.pop()
                        val=val*10+val2
                        send_list.append(dictionary[val])
                        send_list.append(dictionary["lakh"])
                    else:
                        val=val*10
                        send_list.append(dictionary[val])

    return render_template("index.html",send_list=send_list,money=money)
            

if __name__=="__main__":
    app.run(host='0.0.0.0',port=int(os.environ.get("PORT",5000)))
