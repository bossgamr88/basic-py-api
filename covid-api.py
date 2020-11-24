import requests
r = requests.get('https://covid19.th-stat.com/api/open/today')
# print(r.json())
print("UpdateDate : ", r.json()['UpdateDate'])
print("Confirmed : ", r.json()['Confirmed'])
print("NewConfirmed : ", r.json()['NewConfirmed'])
print("NewDeaths : ", r.json()['NewDeaths'])

msg = "UpdateDate : " + str(r.json()['UpdateDate'])
msg2 = "Confirmed : " + str(r.json()['Confirmed'])
msg3 = "NewConfirmed : " + str(r.json()['NewConfirmed'])
msg4 = "NewDeaths : " + str(r.json()['NewDeaths'])

