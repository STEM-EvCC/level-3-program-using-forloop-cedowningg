mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

totalMission = 0
for number in mission_names:
    totalMission = totalMission + 1
print("Total number of missions:" ,totalMission)

counter = 0
for number in mission_success:
    if number == True:
        counter = counter + 1
print ("Number of successful missions", counter)

sucessRate = counter/totalMission * 100
print (f"Sucess rate: {sucessRate:.2f}%")

for number in mission_years:
    if number < 2012:
        print("Missions launched before the year 2000:")
        print (mission_names[mission_years.index(number)])