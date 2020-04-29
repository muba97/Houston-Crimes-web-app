import pandas as pd
import csv
import googlemaps


def main():
    months = ['Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    csvfiles = ['feb.csv','mar.csv','apr.csv','may.csv','jun.csv','jul.csv','aug.csv','sep.csv','oct.csv','nov.csv','dec.csv']
    for i in range(len(months)):
        addresses(months[i],csvfiles[i])


def Premises(month, data):
    
    temp = 0
    lat = []
    lon = []
    errors = 0

    gmaps_key = googlemaps.Client(key = "AIzaSyDLWtHbC8AHB45-DImFqtwed0lbQtWAOmw")
    
    for i in data.index:
        
        temp += 1
        Type = str(data['Address'][i])
        
        geocode_result =gmaps_key.geocode(Type)
        
        try:
            lat.append (geocode_result[0]['geometry']['location']['lat'])
            lon.append (geocode_result[0]['geometry']['location']['lng'])
        except:
            errors += 1
        if temp >= 20:
            break
        
        print(temp)
       
    
    df = pd.DataFrame([lat,lon], index = ['Latitude','Longtitude']).T
    df.to_csv(r'./coordinates/{}'.format(month), index = None, header= True)
    df = pd.DataFrame(lat, columns = ['Latitude'])
    df.to_csv(r'./latitude', index = False, header= True)
    df = pd.DataFrame(lon, columns = ['Longtitude'])
    df.to_csv(r'./longtitude', index = False, header= True)
    print(temp)



def addresses(months,csvfiles):
    currentFile = pd.read_csv('./address/{}'.format(months))
    
    dframe = pd.DataFrame(currentFile)
    Premises(csvfiles,dframe)      

if __name__ == '__main__': main()