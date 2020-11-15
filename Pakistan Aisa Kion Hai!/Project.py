import csv
import matplotlib.pyplot as plt
import functions

with open('C:/Users/Muhammad Ali Raza/Desktop/AoA/Gapminder.csv', 'r') as myFile:
    data = list(csv.reader(myFile, delimiter=','))


def dataTypeConversion(rawList, dataType):
    convertedList = []
    previousValue = 0
    for item in rawList:
        if item != '':
            convertedList.append(dataType(item))
            previousValue = dataType(item)
        else:
            
            convertedList.append(previousValue)
    return convertedList



def fetchIndices(data, columnIndex, searchItem):
    listRowIndices = []

    for i in range(len(data)):
        if data[i][columnIndex] == searchItem:
            listRowIndices.append(i)

    return listRowIndices


def fetchColumnData(data, columnIndex, hasHeader):
    listData = []

    for i in range(len(data)):
        listData.append(data[i][columnIndex])
    if hasHeader:
        return listData[1:]
    else:
        return listData




def fetchData(data, columnIndex, listRowIndices):
    listDataValues = []

    for i in range(len(listRowIndices)):
        listDataValues.append(data[listRowIndices[i]][columnIndex])
    return listDataValues




paksitanIndices = fetchIndices(data, 0, 'Pakistan')
years = dataTypeConversion(fetchData(data, 4, paksitanIndices), int)

countries = set(fetchColumnData(data, 0, True))
indicators = data[0][6:]  
country = list(countries)
countriesDict = {}
for countryName in countries:
    countryIndices = fetchIndices(data, 0, countryName)
    for indicatorName in indicators:
        countriesDict[(countryName, indicatorName)] = dataTypeConversion(
            fetchData(data, data[0].index(indicatorName), countryIndices), float)

# print(len(countriesDict))
# print(len(indicators))
# list_sum = []
# countries = set(fetchColumnData(data, 0, True))
# indicators = data[0][6:]
# country = list(countries)
# #countries ko set data type sy list data typpe main convert kia hy
max_dict={}
for i in indicators:
    max=0
    for j in countries:
        value = (sum(
            countriesDict[(j), (i)])/len(years))
        if(max<value):
            max=value
    max_dict[(i)]=max



rank_dict={}


#rank ka main function
for country_name in countries:
    for indicator in indicators:
        obj_value =value = (sum(
            countriesDict[(country_name), (indicator)])/len(years)) 
        res = float((obj_value/float(max_dict[(indicator)])*101))
        if indicator in ( "Urbanpopulationgrowth", "Trafficdeaths", "Suicideage15to29", "Residentialelectricityuseperperson", "Ratioofgirlstoboysinprimaryandsecondaryeducation", "Poverty", "Populationdensity","YearlyCO2emission", "Populationtotal", "Populationgrowth", "  Oilconsumptionperperson", "Murderedwomen", "Murderedmen","Murder", "Longtermunemploymentrate", "Literacyrateyouthtotal", "Inflation", "Infantmortality", "Imports", "EnergyUsePerPerson", "CO2Emissions", "ChildrenPerWoman"):
            res=res-10
            rank_dict[(country_name), (indicator)]=res
            #bad_indicators(res,rank_by_indicator,country_name,indicator)

        else:
            rank_dict[(country_name), (indicator)]=res
            #good_indicators(res,rank_by_indicator,country_name,indicator)


#total rank country wise
total_rank_Dict={}
for i in countries:
    total=0
    for j in indicators:
        total += rank_dict[(i),(j)]
    total_rank_Dict[(i)]=total

#sb counteries ka rank
# count=0
# for k,v in sorted(country_rank_dict.items(), key=lambda p:p[1],reverse=True):
    
#     print("World_Rank Of",k,":",count)
#     print("Rank_Value =",v)
#     count+=1


good_indicator={}
bad_indicator={}
def ranking (country_name , condition):    
    for indi in indicators:
        value=rank_dict[(country_name),(indi)]
        #print(rank_dict[(country_name), (indi)])
        if indi in ("Taxrevenue","YearlyCO2emission","CO2Emissions", "Urbanpopulationgrowth", "Trafficdeaths", "Suicideage15to29", "Residentialelectricityuseperperson", "Ratioofgirlstoboysinprimaryandsecondaryeducation", "Poverty", "Populationdensity", "Populationtotal", "Populationgrowth", "  Oilconsumptionperperson", "Murderedwomen", "Murderedmen","Murder", "Longtermunemploymentrate", "Literacyrateyouthtotal", "Inflation", "Infantmortality", "Imports", "EnergyUsePerPerson", "CO2Emissions", "ChildrenPerWoman"):
            if (value >= 70):
            #print(country_name,":",indi,":",rank_by_indicator[(country_name),(indi)])
                bad_indicator[(country_name),(indi)]='Best'   #bad indicators me best ka mtlb bilkul nai paya jata...mtln k bhot acha in other words
            elif(value >= 40 and value < 70):
                bad_indicator[(country_name),(indi)]='Average' 
            elif(value >= 10 and value < 40):
                bad_indicator[(country_name),(indi)]='Bad'
            elif(value < 10 ):
                bad_indicator[(country_name),(indi)]='Worst'    
        else:
            if (value >= 30 ):
            #print(country_name,":",indi,":",rank_by_indicator[(country_name),(indi)])
                good_indicator[(country_name),(indi)]='Bad'
            elif(value >= 0 and value < 30):
                good_indicator[(country_name),(indi)]='Average'
            elif(value >= -100 and value < 0):
                good_indicator[(country_name),(indi)]='Good'
            elif(value >= -221 and value < -100 ):
                good_indicator[(country_name),(indi)]='Best'


    if(condition=="Good" or condition=="good"):
        print('--------------------------')
        print("Good Indicator's Condition")  
        print("_________________________")
        print("                         ")

        for k,v in good_indicator.items():
            print(k,v)
    elif(condition=="Bad" or condition=="bad"):
        print('-------------------------')
        print("Bad Indicator's Condition")  
        print("_________________________")
        print("                         ")

        for k,v in bad_indicator.items():
            print(k, v)

    else:
        print("--------------------------")
        print('No Condition was Entered!')


# for i  in countries:
#     Rank_Sort(total_rank_Dict,i)

print('\t\t___________________________________________________\t\t')
print('\t\t|                                                 |\t\t')
print('\t\t|    Proj. By :  Muhammad Ali Raza                |\t\t')
print('\t\t|_________________________________________________|\t\t')

input("Press any Key To Continue! : ")
functions.Rank_Top10(total_rank_Dict)


print("Press key 'Y' if you Want to check Rank of another Country or Press 'Q' to Quit")
Option = input()
while(1):
    
   
    if (Option == 'Y' or Option == 'y' ):
        country_name=input('Enter The Country Name : ')
        print('                         ')

        print('_________________________')
        print('                         ')
        functions.Rank_Sort(total_rank_Dict,country_name)
        print('-------------------------')
        print('                         ')
        print("Press 'Q' to Terminate! Or Press 'Y' to check Again")
        Option = input()
    
    elif(Option == 'q' or Option == 'Q'):
        break
    else:
        break
print("Press Key 'I' to check the Condition of Indicators in Any Country Or press 'Q' to Exit")
con = input()
while(1):
    if(con == 'i' or con == 'I'):
        country_name = input('\tEnter Country Name !   : ' )
        condition =input('Enter The Type Of Indicator: Options Like:  "Bad" Or "Good"  :   ')
        print('---------------------------------')
        print('                                 ')
        ranking(country_name , condition)
        print("Press 'Q' To terminate Or Press 'I' To Continue1")
        con= input()
    elif(con=='q' or con=='Q'):
        break
    else:
        break







for indicator_name in indicators:
    plt.figure()
    if indicator_name in ("Taxrevenue","YearlyCO2emission", "Urbanpopulationgrowth", "Trafficdeaths", "Suicideage15to29", "Residentialelectricityuseperperson", "Ratioofgirlstoboysinprimaryandsecondaryeducation", "Poverty", "Populationdensity", "Populationtotal", "Populationgrowth", "Oilconsumptionperperson", "Murderedwomen", "Murderedmen","Murder", "Ratioofgirlstoboysinprimaryandsecondaryeducation","Longtermunemploymentrate", "Femalesaged25to54labourforceparticipationrate","Literacyrateyouthtotal", "Inflation", "Infantmortality", "Imports", "EnergyUsePerPerson", "CO2Emissions", "ChildrenPerWoman"):
        plt.plot([-100,101],[0,rank_dict[(
            'Pakistan', indicator_name)]], 'green', label="Pakistan")
        plt.plot([-100,101],[0,rank_dict[(
            'India', indicator_name)]], 'red', label="India")
        plt.plot([-100,101],[0,rank_dict[(
            'United States of America', indicator_name)]], 'blue', label="USA")
        plt.plot([-100,101],[0,rank_dict[(
            'China', indicator_name)]], 'black', label="China")
        plt.plot([-100,101],[0,rank_dict[(
            'Somalia', indicator_name)]], 'orange', label="Somalia")
        plt.plot([-100,101],[0,rank_dict[(
            'Bangladesh', indicator_name)]], 'yellow', label="Bangladesh")
        plt.plot([-100,101],[0,rank_dict[(
            'United Kingdom', indicator_name)]], 'cyan', label="UK")
        plt.plot([-100,101],[0,rank_dict[(
            'Norway', indicator_name)]], 'magenta', label="Norway")
        plt.title(indicator_name)
    else:
        plt.plot([-100,101],[0,rank_dict[(
            'Pakistan', indicator_name)]], 'green', label="Pakistan")
        plt.plot([-100,101],[0,rank_dict[(
            'India', indicator_name)]], 'red', label="India")
        plt.plot([-100,101],[0,rank_dict[(
            'United States of America', indicator_name)]], 'blue', label="USA")
        plt.plot([-100,101],[0,rank_dict[(
            'China', indicator_name)]], 'black', label="China")
        plt.plot([-100,101],[0,rank_dict[(
            'Somalia', indicator_name)]], 'orange', label="Somalia")
        plt.plot([-100,101],[0,rank_dict[(
            'Bangladesh', indicator_name)]], 'yellow', label="Bangladesh")
        plt.plot([-100,101],[0,rank_dict[(
            'United Kingdom', indicator_name)]], 'cyan', label="UK")
        plt.plot([-100,101],[0,rank_dict[(
            'Norway', indicator_name)]], 'magenta', label="Norway")
        plt.title(indicator_name)
    plt.legend(loc="best")
plt.show()




