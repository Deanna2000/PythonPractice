# Capture the start time and the event duration
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Calculate the duration of hours and minutes
remainingmins = (dura+mins)%60
print(remainingmins)
durahours = (dura+mins)//60

newhour = (hour + durahours)%24
newmins = remainingmins

print("End Time of the event: ", newhour, ":", newmins)

