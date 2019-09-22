import random
"""
dict_sample key値:入力値,value値:じゃんけんの手
string_value(string) ユーザのじゃんけんの手
value(int) ユーザのじゃんけんの手
evalue(int) 相手のじゃんけんの手
"""
def Battle(value,evalue):

    if (value == 0 and evalue == 1) or (value == 1 and evalue == 2) or (value == 2 and evalue == 0):
        print("あなたの勝ちです")
    elif value == evalue:
        print("あいこです")
    else:
        print("あなたの負けです")

def main():

    dict_sample = {
        0 : "グー",
        1 : "チョキ",
        2 : "パー",
    }

    while(1):
        print("じゃんけんゲームです 0:グー,1:チョキ,2:パー,4:やめる")
        string_value = input()
        value = (int)(string_value)
        if value == 4:
            print("ゲームをやめます")
            break
        evalue =random.randint(0,2)
        print("自分の手は",dict_sample[value],"です")
        print("相手の手は",dict_sample[evalue],"です")
        Battle(value,evalue)

if __name__ == "__main__":
    main()
