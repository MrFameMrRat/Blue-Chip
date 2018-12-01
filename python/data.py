"""data collect"""
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import pandas_datareader as pdr
import datetime
import statistics

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

def main():
    """main function"""
    apple, hp, intel, microsoft, google = data_collect()
    data = [apple[1:], hp[1:], intel[1:], microsoft[1:], google[1:]]
    part3(data)


def part1(data):
    """analysis by closing price"""
    apple = pdr.get_data_yahoo("AAPL", start = datetime.datetime(2018, 5, 20)\
        , end = datetime.datetime ( 2018, 11, 20))
    hp = pdr.get_data_yahoo("HPQ", start = datetime.datetime(2018, 5, 20)\
        , end = datetime.datetime ( 2018, 11, 20))
    intel = pdr.get_data_yahoo("INTC", start = datetime.datetime(2018, 5, 20)\
        , end = datetime.datetime ( 2018, 11, 20))
    microsoft = pdr.get_data_yahoo("MSFT", start = datetime.datetime(2018, 5, 20)\
        , end = datetime.datetime ( 2018, 11, 20))
    google = pdr.get_data_yahoo("GOOG", start = datetime.datetime(2018, 5, 20)\
        , end = datetime.datetime ( 2018, 11, 20))

    apple.plot(y='Close')
    hp.plot(y='Close')
    intel.plot(y='Close')
    microsoft.plot(y='Close')
    google.plot(y='Close')
    plt.show()

def bar_data_part1_2(index, data, more_previous, less_previous, high_avg, below_avg, mean):
    """collect data for bar"""
    present_data = 0
    for i in data[index]:
        if present_data <= float(i[4]):
            more_previous[index] += 1
        else:
            less_previous[index] += 1
        present_data = float(i[4])

        if mean <= float(i[4]):
            high_avg[index] += 1
        else:
            below_avg[index] += 1
    return more_previous, less_previous, high_avg, below_avg

def part1_2(data):
    """analysis closing average x 128 days"""
    x_axis = [i for i in range(len(data[0]))]
    y_apple, y_hp, y_intel, y_microsoft, y_google = [], [], [], [], []
    for j in range(len(data[0])):
        y_apple.append(float(data[0][j][4]))
        y_hp.append(float(data[1][j][4]))
        y_intel.append(float(data[2][j][4]))
        y_microsoft.append(float(data[3][j][4]))
        y_google.append(float(data[4][j][4]))

    mean1 = sum(y_apple)/128
    mean2 = sum(y_hp)/128
    mean3 = sum(y_intel)/128
    mean4 = sum(y_microsoft)/128
    mean5 = sum(y_google)/128

    high_avg, below_avg = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
    more_previous, less_previous =[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]


    more_previous, less_previous, high_avg, below_avg = \
    bar_data_part1_2(0, data, more_previous, less_previous, high_avg, below_avg, mean1)
    more_previous, less_previous, high_avg, below_avg = \
    bar_data_part1_2(1, data, more_previous, less_previous, high_avg, below_avg, mean2)
    more_previous, less_previous, high_avg, below_avg = \
    bar_data_part1_2(2, data, more_previous, less_previous, high_avg, below_avg, mean3)
    more_previous, less_previous, high_avg, below_avg = \
    bar_data_part1_2(3, data, more_previous, less_previous, high_avg, below_avg, mean4)
    more_previous, less_previous, high_avg, below_avg = \
    bar_data_part1_2(4, data, more_previous, less_previous, high_avg, below_avg, mean5)


    x_list = np.arange(1,18) 
    x_list = np.array([10, 30, 50, 70, 90])
    plt.figure(figsize=[20,20])
    plt.title("Compare stcok up-down and stock high-below their average.\nDate: 20/5/2018 - 20/11/2018.")
    range_x = ["AAPL", "HPQ", "INTC", "MSFT", "GOOG"]
    plt.ylabel("Amout (times)")
    plt.xlabel("Sample stcok Co.")
    plt.xticks(x_list, range_x)
    plt.bar(x_list - 4, more_previous, color="blue", width=3, align="center", label="upper from yesterday.")
    plt.bar(x_list - 1, less_previous, color="red", width=3, align="center", label="lower from yesterday.")
    plt.bar(x_list + 2, high_avg, color="green", width=3, align="center", label="higher average.")
    plt.bar(x_list + 5, below_avg, color="orange", width=3, align="center", label="belowe average.")
    plt.legend()

    fig_apple = plt.figure()
    fig_hp = plt.figure()
    fig_intel = plt.figure()
    fig_microsof = plt.figure()
    fig_google = plt.figure()

    ax1 = fig_apple.gca()
    ax1.set_title("AAPL closing price.\nDate: 20/5/2018 - 20/11/2018. [128 days]")
    ax1.set_ylabel("closing price.(Dollar)")
    ax1.set_xlabel("Days [0-127]")
    ax1.axhline(mean1, linestyle="--", label="mean", color="black")
    ax1.plot(x_axis, y_apple, color="red", label="closing price")
    ax1.legend()

    ax2 = fig_hp.gca()
    ax2.set_title("HPQ closing price.\nDate: 20/5/2018 - 20/11/2018. [128 days]")
    ax2.set_ylabel("closing price.(Dollar)")
    ax2.set_xlabel("Days [0-127]")
    ax2.axhline(mean2, linestyle="--", label="mean", color="black")
    ax2.plot(x_axis, y_hp, color="orange", label="closing price")
    ax2.legend()

    ax3 = fig_intel.gca()
    ax3.set_title("INTC closing price.\nDate: 20/5/2018 - 20/11/2018. [128 days]")
    ax3.set_ylabel("closing price.(Dollar)")
    ax3.set_xlabel("Days [0-127]")
    ax3.axhline(mean3, linestyle="--", label="mean", color="black")
    ax3.plot(x_axis, y_intel, color="green", label="closing price")
    ax3.legend()

    ax4 = fig_microsof.gca()
    ax4.set_title("MSFT closing price.\nDate: 20/5/2018 - 20/11/2018. [128 days]")
    ax4.set_ylabel("closing price.(Dollar)")
    ax4.set_xlabel("Days [0-127]")
    ax4.axhline(mean4, linestyle="--", label="mean", color="black")
    ax4.plot(x_axis, y_microsoft, color="blue", label="closing price")
    ax4.legend()

    ax5 = fig_google.gca()
    ax5.set_title("GOOG closing price.\nDate: 20/5/2018 - 20/11/2018. [128 days]")
    ax5.set_ylabel("closing price.(Dollar)")
    ax5.set_xlabel("Days [0-127]")
    ax5.axhline(mean5, linestyle="--", label="mean", color="black")
    ax5.plot(x_axis, y_google, color="purple", label="closing price")
    ax5.legend()

    plt.show()


def part2(data):
    """analysis by volume"""
    y_apple = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    x_list = np.arange(1,10)
    for i in data[0]:
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
    plt.xlabel("volume sold. [10 million unit.]", fontsize=10)
    plt.xticks(x_list, range_x)
    plt.bar(x_list,y_apple, color="red")


    y_hp = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    x_list2 = np.arange(1,10)
    for i in data[1]:
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
    for i in data[2]:
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
    for i in data[3]:
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
    plt.show()

    y_google = [0, 0, 0, 0, 0, 0, 0, 0]
    x_list5 = np.arange(1,9)
    for i in data[4]:
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

    x = [0, 0, 0, 0, 0]

    for i in range(len(apple)):
        x[0] += int(apple[i][6])
        x[1] += int(hp[i][6])
        x[2] += int(intel[i][6])
        x[3] += int(microsoft[i][6])
        x[4] += int(google[i][6])
    labels = ["AAPL", "HPQ", "INTC", "MSFT", "GOOG"]
    plt.figure(figsize=[7,7])
    plt.pie(x,autopct='%d%%', counterclock=0, startangle=90, labels=labels)

def part3(data):
    """pair trade HPQ and INTC"""

    x_axis = [i for i in range(len(data[0]))]
    y_hp, y_intel = [], []
    y_diff = []
    for j in range(len(data[0])):
        y_hp.append(float(data[1][j][5]))
        y_intel.append(float(data[2][j][5]))
        y_diff.append(float(data[2][j][5]) - float(data[1][j][5]))

    ax1 = plt.gca()
    ax1.set_title("HPQ and INTC adj. close price.\nDate: 20/5/2018 - 20/11/2018. [128 days]")
    ax1.set_ylabel("Adj. close price.(Dollar)")
    ax1.set_xlabel("Days [0-127]")
    ax1.plot(x_axis, y_hp, color="orange", label="HPQ")
    ax1.plot(x_axis, y_intel, color="green", label="INTC")
    ax1.legend(loc=0)
    ax2 = ax1.twinx()
    ax2.set_ylabel("Difference between INTC and HPQ.")
    ax2.plot(x_axis, y_diff, color="black", label="difference")
    ax2.legend(loc=5)

    plt.show()

    y_diff_float = []
    for i in y_diff:
        y_diff_float.append(i)
    for i in range(len(y_diff)):
        y_diff[i] = int(y_diff[i])

    x_list = np.arange(19,34)
    y_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in y_diff:
        y_list[i - 19] += 1


    plt.title("Amout of difference.")
    plt.ylabel("Amout")
    plt.xlabel("Difference")
    plt.bar(x_list, y_list, color="purple", width=1)
    plt.show()


    mean = int(statistics.mean(y_diff))
    std = int(statistics.pstdev(y_diff))
    print(mean, std)

    ax3 = plt.gca()
    ax3.set_title("Adj close difference between INTC and HPQ")
    ax3.set_ylabel("difference")
    ax3.set_xlabel("Days [0-127]")
    ax3.axhline(mean, linestyle="--", label="mean [24]", color="green")
    ax3.axhline(mean + std, linestyle="--", label="std +1 [27]", color="red")
    ax3.axhline(mean - std, linestyle="--", label="std -1 [21]", color="blue")
    ax3.plot(x_axis, y_diff_float, color="purple", label="difference")
    ax3.legend()
    plt.show()

main()
