
rank_dict = {}

def good(res,countr,indicate):
    if(res >= 90):
        rank_dict[(countr), (indicate)] = 10
    elif(res >= 80 and res < 90):
        rank_dict[(countr), (indicate)] = 9
    elif(res >= 70 and res < 80):
        rank_dict[(countr), (indicate)] = 8
    elif(res >= 60 and res < 70):
        rank_dict[(countr), (indicate)] = 7
    elif(res >= 50 and res < 60):
        rank_dict[(countr), (indicate)] = 6
    elif(res >= 40 and res < 50):
        rank_dict[(countr), (indicate)] = 5
    elif(res >= 30 and res < 40):
        rank_dict[(countr), (indicate)] = 4
    elif(res >= 20 and res < 30):
        rank_dict[(countr), (indicate)] = 3
    elif(res >= 10 and res < 20):
        rank_dict[(countr), (indicate)] = 2
    elif(res >= 0 and res < 10):
        rank_dict[(countr), (indicate)] = 1
    elif(res<0):
        rank_dict[(countr), (indicate)] = 0


def bad(res,countr,indicate):
    if(res >= 90):
        rank_dict[(countr), (indicate)] = 1
    elif(res >= 80 and res < 90):
        rank_dict[(countr), (indicate)] = 2
    elif(res >= 70 and res < 80):
        rank_dict[(countr), (indicate)] = 3
    elif(res >= 60 and res < 70):
        rank_dict[(countr), (indicate)] = 4
    elif(res >= 50 and res < 60):
        rank_dict[(countr), (indicate)] = 5
    elif(res >= 40 and res < 50):
        rank_dict[(countr), (indicate)] = 6
    elif(res >= 30 and res < 40):
        rank_dict[(countr), (indicate)] = 7
    elif(res >= 20 and res < 30):
        rank_dict[(countr), (indicate)] = 8
    elif(res >= 10 and res < 20):
        rank_dict[(countr), (indicate)] = 9
    elif(res >= 0 and res < 10):
        rank_dict[(countr), (indicate)] = 10
    elif(res<0):
        rank_dict[(countr), (indicate)] = 10


def Rank_Sort(total_rank_Dict,country):
    counter=1
    for k,v in sorted(total_rank_Dict.items(), key=lambda p:p[1],reverse=True):
        if(k==country):
            print("World_Rank Of ",k,":",counter)
            print("Overall Value =",int(v))
        counter+=1



def Rank_Top10(total_rank_Dict):
    counter= 1
    for k,v in sorted(total_rank_Dict.items(), key=lambda p:p[1],reverse=True):
        
        print("World_Rank Of ",k,":",counter)
        print("Overall Value =",int(v))
        if(counter == 10):
            break
        else:    
            counter += 1