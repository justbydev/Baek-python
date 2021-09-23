import json
import requests

BASE_URL="https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
AUTH_TOKEN="deb0468c620ec8e3b1faa1d3db34d2e6"

def start_api(number):
    headers={'Content-Type':'application/json', 'X-Auth-ToKen':AUTH_TOKEN}
    data={'problem': number}
    res=requests.post(BASE_URL+'/start', data=json.dumps(data), headers=headers)
    return res.json()

def location_api(AUTH_KEY):
    headers={'Content-Type':'application/json', 'Authorization':AUTH_KEY}
    res=requests.get(BASE_URL+'/locations', headers=headers)
    response=res.json()['locations']
    return response

def truck_api(AUTH_KEY):
    headers={'Content-Type':'application/json', 'Authorization':AUTH_KEY}
    res=requests.get(BASE_URL+'/trucks', headers=headers)
    response=res.json()['trucks']
    return response

def score_api(AUTH_KEY):
    headers={'Content-Type':'application/json', 'Authorization':AUTH_KEY}
    res=requests.get(BASE_URL+'/score', headers=headers)
    return res.json()['score']
def simulate_api(AUTH_KEY, commands):
    headers={'Content-Type':'application/json', 'Authorization':AUTH_KEY}
    data={'commands':commands}
    res=requests.put(BASE_URL+'/simulate', data=json.dumps(data), headers=headers)
    return res.json()

def start_one():
    response=start_api(1)
    auth_key=response['auth_key']
    time=response['time']
    status="ready"
    while True:
        if status=="finished":
            break
        jsonarray=location_api(auth_key)
        smallboard_list=[]
        for list in jsonarray:
            count=list['located_bikes_count']
            smallboard_list.append(count)
        trucks=truck_api(auth_key)
        commands=[]
        for i in range(5):
            each_truck={}
            each_truck['truck_id']=i
            each_truck['command']=[0]
            commands.append(each_truck)
        if time==0:
            for i in range(1, 5):
                for j in range(i):
                    commands[i]['command'].append(2)
        else:
            #0번 트럭
            locate=trucks[0]['location_id']
            bike=trucks[0]['loaded_bikes_count']
            if locate==4:
                if smallboard_list[locate]==0 and bike!=0:
                    commands[0]['command'].append(6)
                    bike-=1
                commands[0]['command'].append(3)
                locate-=1
                for i in range(4):
                    if locate==0:
                        if smallboard_list[locate]==0 and bike!=0:
                            commands[0]['command'].append(6)
                            bike-=1
                        break
                    if smallboard_list[locate]>=2 and bike<20:
                        commands[0]['command'].append(5)
                        bike+=1
                    elif smallboard_list[locate]==0 and bike!=0:
                        commands[0]['command'].append(6)
                        bike-=1
                    locate-=1
                    commands[0]['command'].append(3)
            elif locate==0:
                if smallboard_list[locate]==0 and bike!=0:
                    commands[0]['command'].append(6)
                    bike-=1
                commands[0]['command'].append(1)
                locate-=1
                for i in range(4):
                    if locate==4:
                        if smallboard_list[locate]==0 and bike!=0:
                            commands[0]['command'].append(6)
                        break
                    if smallboard_list[locate]>=2 and bike<20:
                        commands[0]['command'].append(5)
                        bike+=1
                    elif smallboard_list[locate]==0 and bike!=0:
                        commands[0]['command'].append(6)
                        bike-=1
                    locate+=1
                    commands[0]['command'].append(1)
            #1번 트럭
            locate=trucks[1]['location_id']
            bike=trucks[1]['loaded_bikes_count']
            if locate==9:
                if smallboard_list[locate]==0 and bike!=0:
                    commands[1]['command'].append(6)
                    bike-=1
                commands[1]['command'].append(3)
                locate-=1
                for i in range(4):
                    if locate==5:
                        if smallboard_list[locate]==0 and bike!=0:
                            commands[1]['command'].append(6)
                        break
                    if smallboard_list[locate]>=2 and bike<20:
                        commands[1]['command'].append(5)
                        bike+=1
                    elif smallboard_list[locate]==0 and bike!=0:
                        commands[1]['command'].append(6)
                        bike-=1
                    locate-=1
                    commands[1]['command'].append(3)
            elif locate==5:
                if smallboard_list[locate]==0 and bike!=0:
                    commands[1]['command'].append(6)
                    bike-=1
                commands[1]['command'].append(1)
                locate-=1
                for i in range(4):
                    if locate==9:
                        if smallboard_list[locate]==0 and bike!=0:
                            commands[1]['command'].append(6)
                        break
                    if smallboard_list[locate]>=2 and bike<20:
                        commands[1]['command'].append(5)
                        bike+=1
                    elif smallboard_list[locate]==0 and bike!=0:
                        commands[1]['command'].append(6)
                        bike-=1
                    locate+=1
                    commands[1]['command'].append(1)
            #2번 트럭
            locate=trucks[2]['location_id']
            bike=trucks[2]['loaded_bikes_count']
            if locate==14:
                if smallboard_list[locate]==0 and bike!=0:
                    commands[2]['command'].append(6)
                    bike-=1
                commands[2]['command'].append(3)
                locate-=1
                for i in range(4):
                    if locate==10:
                        if smallboard_list[locate]==0 and bike!=0:
                            commands[2]['command'].append(6)
                        break
                    if smallboard_list[locate]>=2 and bike<20:
                        commands[2]['command'].append(5)
                        bike+=1
                    elif smallboard_list[locate]==0 and bike!=0:
                        commands[2]['command'].append(6)
                        bike-=1
                    locate-=1
                    commands[2]['command'].append(3)
            elif locate==10:
                if smallboard_list[locate]==0 and bike!=0:
                    commands[2]['command'].append(6)
                    bike-=1
                commands[2]['command'].append(1)
                locate-=1
                for i in range(4):
                    if locate==14:
                        if smallboard_list[locate]==0 and bike!=0:
                            commands[2]['command'].append(6)
                        break
                    if smallboard_list[locate]>=2 and bike<20:
                        commands[2]['command'].append(5)
                        bike+=1
                    elif smallboard_list[locate]==0 and bike!=0:
                        commands[2]['command'].append(6)
                        bike-=1
                    locate+=1
                    commands[2]['command'].append(1)
            #3번 트럭
            locate=trucks[3]['location_id']
            bike=trucks[3]['loaded_bikes_count']
            if locate==19:
                if smallboard_list[locate]==0 and bike!=0:
                    commands[3]['command'].append(6)
                    bike-=1
                commands[3]['command'].append(3)
                locate-=1
                for i in range(4):
                    if locate==15:
                        if smallboard_list[locate]==0 and bike!=0:
                            commands[3]['command'].append(6)
                            bike-=1
                        break
                    if smallboard_list[locate]>=2 and bike<20:
                        commands[3]['command'].append(5)
                        bike+=1
                    elif smallboard_list[locate]==0 and bike!=0:
                        commands[3]['command'].append(6)
                        bike-=1
                    locate-=1
                    commands[3]['command'].append(3)
            elif locate==15:
                if smallboard_list[locate]==0 and bike!=0:
                    commands[3]['command'].append(6)
                    bike-=1
                commands[3]['command'].append(1)
                locate-=1
                for i in range(4):
                    if locate==19:
                        if smallboard_list[locate]==0 and bike!=0:
                            commands[3]['command'].append(6)
                        break
                    if smallboard_list[locate]>=2 and bike<20:
                        commands[3]['command'].append(5)
                        bike+=1
                    elif smallboard_list[locate]==0 and bike!=0:
                        commands[3]['command'].append(6)
                        bike-=1
                    locate+=1
                    commands[3]['command'].append(1)
            #4번 트럭
            locate=trucks[4]['location_id']
            bike=trucks[4]['loaded_bikes_count']
            if locate==24:
                if smallboard_list[locate]==0 and bike!=0:
                    commands[4]['command'].append(6)
                    bike-=1
                commands[4]['command'].append(3)
                locate-=1
                for i in range(4):
                    if locate==20:
                        if smallboard_list[locate]==0 and bike!=0:
                            commands[4]['command'].append(6)
                            bike-=1
                        break
                    if smallboard_list[locate]>=2 and bike<20:
                        commands[4]['command'].append(5)
                        bike+=1
                    elif smallboard_list[locate]==0 and bike!=0:
                        commands[4]['command'].append(6)
                        bike-=1
                    locate-=1
                    commands[4]['command'].append(3)
            elif locate==20:
                if smallboard_list[locate]==0 and bike!=0:
                    commands[4]['command'].append(6)
                    bike-=1
                commands[3]['command'].append(1)
                locate-=1
                for i in range(4):
                    if locate==24:
                        if smallboard_list[locate]==0 and bike!=0:
                            commands[4]['command'].append(6)
                        break
                    if smallboard_list[locate]>=2 and bike<20:
                        commands[4]['command'].append(5)
                        bike+=1
                    elif smallboard_list[locate]==0 and bike!=0:
                        commands[4]['command'].append(6)
                        bike-=1
                    locate+=1
                    commands[4]['command'].append(1)
        simulate_response=simulate_api(auth_key, commands)
        time=simulate_response['time']
        status=simulate_response['status']
    print(score_api(auth_key))
def start_two():
    response=start_api(1)
    auth_key=response['auth_key']
    status="ready"
    while True:
        if status=="finished":
            break
        jsonarray=location_api(auth_key)
        smallboard_list=[]
        for list in jsonarray:
            count=list['located_bikes_count']
            smallboard_list.append(count)
        trucks=truck_api(auth_key)
        commands=[]
        for i in range(5):
            each_truck={}
            each_truck['truck_id']=i
            each_truck['command']=[0]
            commands.append(each_truck)
        simulate_response=simulate_api(auth_key, commands)
        status=simulate_response['status']
    print(score_api(auth_key))

#start_one()
start_two()