import pandas as pd
import csv
import matplotlib.pyplot as plt


def main():
    xlsfiles = ['jan17.xls','feb17.xls','mar17.xls','apr17.xls','may17.xls','jun17.xls','jul17.xls','aug17.xls','sep17.xls','oct17.xls','nov17.xls','dec17.xls']
    csvfiles = ['jan17.csv','feb17.csv','mar17.csv','apr17.csv','may17.csv','jun17.csv','jul17.csv','aug17.csv','sep17.csv','oct17.csv','nov17.csv','dec17.csv']
    All_premises = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(len(xlsfiles)):
        current_month = All_premises[i]
        plotpremises(csvfiles[i],current_month,i)

    
    for x in range(12):
        months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        Streetval.append(All_premises[x][0])
        Commercialval.append(All_premises[x][1])
        Residentialval.append(All_premises[x][2])
        otherval.append(All_premises[x][3])
    Street(Streetval, months)
    Commercial(Commercialval, months)
    Residential(Residentialval, months)
    Other(otherval, months)


    

#counting all the how many times each offense was committed
def Premises(types, data):
    for i in data.index:
    
        if 'Street' in str(data['Premise'][i]) or 'Parking' in str(data['Premise'][i]) or 'Driveway' in str(data['Premise'][i]):
            types[0] += 1
        elif 'Store' in str(data['Premise'][i]) or "Shop" in str(data['Premise'][i]) or 'Bar' in str(data['Premise'][i]):
            types[1] += 1
        elif 'House' in str(data['Premise'][i]) or "Apartment" in str(data['Premise'][i]) or 'Hotel' in str(data['Premise'][i]):
            types[2] +=1
        else:
            types[3] +=1
    return types


def PremisesPlots(values, types, month):
    plt.plot(types, values)
    plt.ylabel('Quantities')
    plt.xlabel('Types of crimes')
    plt.savefig('./Premisesplots/{}'.format(month))
    plt.close()


def plotpremises(filename,month,i):
    plots = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    currentFile = pd.read_csv('./csvfiles/{}'.format(filename))
    dframe = pd.DataFrame(currentFile)
    Premises(month, dframe)      
    PremisesPlots(month, types, plots[i])

def Street(month, values):
    plt.plot(values, month)
    plt.ylabel('Street Values')
    plt.xlabel('Month')
    plt.title('Number of street crimes committed each month')
    plt.savefig('./Premisesplots/Street')
    plt.close()
def Commercial(month, values):
    plt.plot(values, month)
    plt.ylabel('Commercial Values')
    plt.xlabel('Month')
    plt.title('Number of commercial crimes committed each month')
    plt.savefig('./Premisesplots/Commercial')
    plt.close()
def Residential(month, values):
    plt.plot(values, month)
    plt.ylabel('Residential Values')
    plt.xlabel('Month')
    plt.title('Number of residential crimes committed each month')
    plt.savefig('./Premisesplots/Residential')
    plt.close()
def Other(month, values):
    plt.plot(values, month)
    plt.ylabel('Other Values')
    plt.xlabel('Month')
    plt.title('Number of others crimes committed each month')
    plt.savefig('./Premisesplots/Others')
    plt.close()



if __name__ == '__main__': main()