import http.client, urllib.parse, json

[] = []

key = {'Ocp-Apim-Subscription-Key': 'c6f6af859d0c402492f58afb53961511'} # says key is invalid!

# stationInput = input("Vul uw station's afkorting in: ")
def NS_API(stationInput):
    global afkStation
    #stationInput = stationInput.lower()
    try:
        conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
        conn.request("GET", "/public-reisinformatie/api/v2/stations", headers=key)

        response01 = conn.getresponse()
        responsetext01 = response01.read()
        data01 = json.loads(responsetext01)

        payloadObject01 = data01['payload']

        wteller = 0
        #print("Het werkt")

        for item in payloadObject01:
            #print("Het werkt2")
            #print(item)
            stationL = item['namen']['lang'] #.lowercase()
            #print(stationL)
            #print(stationInput)
            #stationK = item['namen']['kort'].lowercase()
            #stationM = item['namen']['middel'].lowercase()
            #if stationInput == stationL or stationInput == stationK or stationInput == stationM:
            if stationInput in stationL:
                afkStation = item['code']
                #return afkStation
                #print(afkStation)
            else:
                #wteller += 1
                print("Error! Dit is geen station")

        conn.close()
    except:
        print("Error01")

    params = urllib.parse.urlencode({
        'maxJourneys': '25',
        'station': afkStation })

    try:
        conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
        conn.request("GET", "/public-reisinformatie/api/v2/departures?" + params, headers=key)

        response = conn.getresponse()
        responsetext = response.read()
        data = json.loads(responsetext)

        payloadObject = data['payload']
        departuresList = payloadObject['departures']

        lstStations = []

        for departure in departuresList:
            lstStations.append({'time': departure['actualDateTime'], 'station': departure['direction'], 'spoor': departure['plannedTrack'], 'soort': departure["product"]["longCategoryName"] })
            #print(lstStations)
            #return departure['actualDateTime'], departure['direction']
            #print(departure['actualDateTime'], departure['direction'])
        for station in lstStations:
            station['time'] = station['time'][11:16]
            #print(station)

        conn.close()

        return lstStations
        #print(lstStations)

        #print(data)
    except Exception as e:
        print( "Error02")
        #print("Fout: ")   # {} {}".format(e.errno, e.strerror))

#stationInput = input("Vul uw station in: ")
#stationInput = "Augsburg"
#NS_API(stationInput)


