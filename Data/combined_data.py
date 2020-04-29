import pandas as pd
import csv
import matplotlib.pyplot as plt


def main():
    xlsfiles = ['jan17.xls','feb17.xls','mar17.xls','apr17.xls','may17.xls','jun17.xls','jul17.xls','aug17.xls','sep17.xls','oct17.xls','nov17.xls','dec17.xls']
    csvfiles = ['jan17.csv','feb17.csv','mar17.csv','apr17.csv','may17.csv','jun17.csv','jul17.csv','aug17.csv','sep17.csv','oct17.csv','nov17.csv','dec17.csv']
    All_offenses = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(len(xlsfiles)):
        current_month = All_offenses[i]
        plotoffensive(csvfiles[i],current_month,i)
    Theftval = []
    Assaultval = []
    Burglaryval = []
    Robberyval = []
    for x in range(12):
        months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        Theftval.append(All_offenses[x][0])
        Assaultval.append(All_offenses[x][1])
        Burglaryval.append(All_offenses[x][2])
        Robberyval.append(All_offenses[x][3])
    Theft(Theftval, months)
    Assault(Assaultval, months)
    Burglary(Burglaryval, months)
    Robbery(Robberyval, months)


        

'''        currentFile = pd.read_csv('./csvfiles/{}'.format(csvfiles[i]))
        dframe = pd.DataFrame(currentFile)
        current_month = All_offenses[i]
        Offenses(current_month, dframe)
        print()
        plotname = All_offenses_plots[i]
        OffensePlots(current_month, OffenseTypes, plotname)
    
    currentFile = pd.read_csv('./csvfiles/jan17.csv')
    dframe = pd.DataFrame(currentFile)
    Jan_Offenses= [0,0,0,0,0]
    Offenses(Jan_Offenses, dframe)
    OffenseTypes = ['Theft', 'Assault', 'burglary', 'Robbery', 'Auto Theft']
    Jan = 'JanuaryOffenses'
    OffensePlots(Jan_Offenses, OffenseTypes, Jan)

    print(dframe.columns)'''





    

#counting all the how many times each offense was committed
def Offenses(types, data):
    for i in data.index:
        if 'Theft' in data['Offense Type'][i]:
            types[0] += 1
        if (data['Offense Type'][i] == 'Aggravated Assault') and ('Street' in str(data['Premise'][i]) or 'Parking' in str(data['Premise'][i]) or 'Driveway' in str(data['Premise'][i])):
            types[1] += 1
        if data['Offense Type'][i] == 'Burglary':
            types[2] +=1
        if data['Offense Type'][i] == 'Robbery':
            types[3] += 1
    return types


def OffensePlots(values, types, month):
    plt.plot(types, values)
    plt.ylabel('Quantities')
    plt.xlabel('Types of crimes')
    plt.savefig('./offenseplots/{}'.format(month))
    plt.close()


def plotoffensive(filename,month,i):
    plots = ['JanOffenses','FebOffenses','MarOffenses','AprOffenses','MayOffenses','JunOffenses','JulOffenses','AugOffenses','SepOffenses','OctOffenses','NovOffenses','DecOffenses']
    types = ['Theft', 'Assault', 'burglary', 'Robbery']
    currentFile = pd.read_csv('./csvfiles/{}'.format(filename))
    dframe = pd.DataFrame(currentFile)    
    Offenses(month, dframe)      
    OffensePlots(month, types, plots[i])

def Theft(month, values):
    plt.plot(values, month)
    plt.ylabel('Theft Values')
    plt.xlabel('Month')
    plt.title('Number of theft crimes committed each month')
    plt.savefig('./offenseplots/Theft')
    plt.close()
def Assault(month, values):
    plt.plot(values, month)
    plt.ylabel('Assault Values')
    plt.xlabel('Month')
    plt.title('Number of assault crimes committed each month')
    plt.savefig('./offenseplots/Assault')
    plt.close()
def Burglary(month, values):
    plt.plot(values, month)
    plt.ylabel('Burglary Values')
    plt.xlabel('Month')
    plt.title('Number of burglary crimes committed each month')
    plt.savefig('./offenseplots/Burglary')
    plt.close()
def Robbery(month, values):
    plt.plot(values, month)
    plt.ylabel('Robbery Values')
    plt.xlabel('Month')
    plt.title('Number of robbery crimes committed each month')
    plt.savefig('./offenseplots/Robbery')
    plt.close()



if __name__ == '__main__': main()