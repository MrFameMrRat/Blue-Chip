"""data collect"""
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

def data_collect():
    """convert all data into list"""
    file = open("AAPL.csv", "r")
    data = csv.reader(file)
    apple = [row for row in data]

    file = open("HPQ.csv", "r")
    data = csv.reader(file)
    hp = [row for row in data]

    file = open("INTC.csv", "r")
    data = csv.reader(file)
    intel = [row for row in data]

    file = open("MSFT.csv", "r")
    data = csv.reader(file)
    microsoft = [row for row in data]

    file = open("GOOG.csv", "r")
    data = csv.reader(file)
    google = [row for row in data]

    return apple, hp, intel, microsoft, google
def part2(apple, hp, intel, microsoft, google):
    """analysis by volume"""
    """
    y_apple = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    x_list = np.arange(1,10)
    for i in apple:
        if i[6] != "Volume":
            if 10000 <= int(i[6])/1000 < 20000:
                y_apple[0] += 1
            elif int(i[6])/1000 < 30000:
                y_apple[1] += 1
            elif int(i[6])/1000 < 40000:
                y_apple[2] += 1
            elif int(i[6])/1000 < 50000:
                y_apple[3] += 1
            elif int(i[6])/1000 < 60000:
                y_apple[4] += 1
            elif int(i[6])/1000 < 70000:
                y_apple[5] += 1
            elif int(i[6])/1000 < 80000:
                y_apple[6] += 1
            elif int(i[6])/1000 < 90000:
                y_apple[7] += 1
            else:
                y_apple[8] += 1
    plt.title("APPLE volume sold out.\nDate: 20/5/2018 - 20/11/2018", fontsize=15)
    range_x = ['1-2','2-3','3-4','4-5','5-6', "6-7", "7-8","8-9", "9-10"]
    plt.ylabel("Amout of volume.", fontsize=17)
    plt.xlabel("volume sold. [10 million unit.]", fontsize=17)
    plt.xticks(x_list, range_x)
    plt.bar(x_list,y_apple, color="red")

    y_hp = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    x_list2 = np.arange(1,10)
    for i in hp:
        if i[6] != "Volume":
            if 30000 <= int(i[6])/100 < 50000:
                y_hp[0] += 1
            elif int(i[6])/100 < 70000:
                y_hp[1] += 1
            elif int(i[6])/100 < 90000:
                y_hp[2] += 1
            elif int(i[6])/100 < 110000:
                y_hp[3] += 1
            elif int(i[6])/100 < 130000:
                y_hp[4] += 1
            elif int(i[6])/100 < 150000:
                y_hp[5] += 1
            elif int(i[6])/100 < 170000:
                y_hp[6] += 1
            elif int(i[6])/100 < 190000:
                y_hp[7] += 1
            else:
                y_hp[8] += 1
    plt.title("HP volume sold out.\nDate: 20/5/2018 - 20/11/2018", fontsize=15)
    range_x = ['3-5','5-7','7-9','9-11','11-13', "13-15", "15-17","17-19", "19-21"]
    plt.ylabel("Amout of volume.", fontsize=17)
    plt.xlabel("volume sold. [1 million unit.]", fontsize=17)
    plt.xticks(x_list2, range_x)
    plt.bar(x_list2, y_hp, color="orange")

    y_intel = [0, 0, 0, 0, 0, 0]
    x_list3 = np.arange(1,7)
    for i in intel:
        if i[6] != "Volume":
            if 10000 <= int(i[6])/1000 < 20000:
                y_intel[0] += 1
            elif int(i[6])/1000 < 30000:
                y_intel[1] += 1
            elif int(i[6])/1000 < 40000:
                y_intel[2] += 1
            elif int(i[6])/1000 < 50000:
                y_intel[3] += 1
            elif int(i[6])/1000 < 60000:
                y_intel[4] += 1
            else:
                y_intel[5] += 1
    plt.title("Intel volume sold out.\nDate: 20/5/2018 - 20/11/2018", fontsize=15)
    range_x = ['1-2','2-3','3-4','4-5','5-6', "6-7"]
    plt.ylabel("Amout of volume.", fontsize=17)
    plt.xlabel("volume sold. [10 million unit.]", fontsize=17)
    plt.xticks(x_list3, range_x)
    plt.bar(x_list3, y_intel, color="green")

    y_microsoft = [0, 0, 0, 0, 0, 0]
    x_list4 = np.arange(1,7)
    for i in intel:
        if i[6] != "Volume":
            if 10000 <= int(i[6])/1000 < 20000:
                y_microsoft[0] += 1
            elif int(i[6])/1000 < 30000:
                y_microsoft[1] += 1
            elif int(i[6])/1000 < 40000:
                y_microsoft[2] += 1
            elif int(i[6])/1000 < 50000:
                y_microsoft[3] += 1
            elif int(i[6])/1000 < 60000:
                y_microsoft[4] += 1
            else:
                y_microsoft[5] += 1

    plt.title("MICROSOFT volume sold out.\nDate: 20/5/2018 - 20/11/2018", fontsize=15)
    range_x = ['1-2','2-3','3-4','4-5','5-6', "6-7"]
    plt.ylabel("Amout of volume.", fontsize=17)
    plt.xlabel("volume sold. [10 million unit.]", fontsize=17)
    plt.xticks(x_list4, range_x)
    plt.bar(x_list4, y_microsoft, color="blue")

    y_google = [0, 0, 0, 0, 0, 0, 0, 0]
    x_list5 = np.arange(1,9)
    for i in google:
        if i[6] != "Volume":
            if 5000 <= int(i[6])/100 < 10000:
                y_google[0] += 1
            elif int(i[6])/100 < 15000:
                y_google[1] += 1
            elif int(i[6])/100 < 20000:
                y_google[2] += 1
            elif int(i[6])/100 < 25000:
                y_google[3] += 1
            elif int(i[6])/100 < 30000:
                y_google[4] += 1
            elif int(i[6])/100 < 35000:
                y_google[5] += 1
            elif int(i[6])/100 < 40000:
                y_google[6] += 1
            else:
                y_google[7] += 1

    plt.title("GOOGLE volume sold out.\nDate: 20/5/2018 - 20/11/2018", fontsize=15)
    range_x = ['0.5-1.0','1-1.5','1.5-2.0','2.0-2.5','2.5-3.0', "3.0-3.5", "3.5-4.0", "4.0-4.5"]
    plt.ylabel("Amout of volume.", fontsize=17)
    plt.xlabel("volume sold. [1 million unit.]", fontsize=17)
    plt.xticks(x_list5, range_x)
    plt.bar(x_list5, y_google, color="purple")
    """
    x = [0, 0, 0, 0, 0]

    for i in range(len(apple)):
        if i != 0:
            x[0] += int(apple[i][6])
            x[1] += int(hp[i][6])
            x[2] += int(intel[i][6])
            x[3] += int(microsoft[i][6])
            x[4] += int(google[i][6])
    labels = ["AAPL", "HPQ", "INTC", "MSFT", "GOOG"]
    plt.figure(figsize=[7,7])
    plt.pie(x,autopct='%d%%', counterclock=0, startangle=90, labels=labels)
    plt.show()
def main():
    """main func"""
    apple, hp, intel, microsoft, google = data_collect()
    part2(apple, hp, intel, microsoft, google)

main()

