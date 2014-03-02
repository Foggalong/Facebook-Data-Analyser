#!/usr/bin/python3

# Opening Facebook data files
with open('friends.htm', 'r') as file:
	friend_file = [line.strip() for line in file][0]
with open('events.htm', 'r') as file:
	event_file = [line.strip() for line in file][0]
with open('messages.htm', 'r') as file:
	messages_file_line_list = [line.strip() for line in file]
with open('pokes.htm', 'r') as file:
	poke_file = [line.strip() for line in file][0]


###########################################################################
"""Counts the number of messages"""
###########################################################################

# Counts the number of messages
messages_count = 0
for line in messages_file_line_list:
	messages_count += line.count('UTC')
print("Number of messages:", messages_count)



###########################################################################
"""Counts the number of conversation threads"""
###########################################################################

# Counts the number of different conversation threads
thread_count = 0
for line in messages_file_line_list:
	thread_count += line.count('<div class="thread">')
print("Number of conversations:", thread_count)



###########################################################################
"""Messages Over Time Analysis"""
###########################################################################

# Creates list of all times
times_list = []
for line in messages_file_line_list:
	span_split_line = line.split("span")
	for string in span_split_line:
		if '"meta">' in string:
			times_list.append(string.split('"meta">')[1].split('</')[0])

# Creates a list of dates
date_list = []
for time in times_list:
	if time.split(" at ")[0] in date_list:
		pass
	else: date_list.append(time.split(" at ")[0])

# Creates ISO date list
iso_date_list = []
months = {"january":"01", "february":"02", "march":"03", "april":"04",
		"may":"05", "june":"06", "july":"07", "august":"08",
		"september":"09", "october":"10", "november":"11", "december":"12"}
for date in date_list:
	iso_date = []
	# Finds Year
	iso_date.append(date.split(" ")[3])
	# Finds Month
	month = date.split(" ")[2].lower()
	iso_date.append(months[month])
	# Finds Date
	if int(date.split(" ")[1]) < 10:
		iso_date.append("0"+date.split(" ")[1])
	else:
		iso_date.append(date.split(" ")[1])
	# Adds to main list
	if "".join(iso_date) in iso_date_list:
		pass
	else:
		iso_date_list.append("".join(iso_date))

# Counts how many messages per day
date_count_list = [0 for item in date_list]
for time in times_list:
	date_count_list[date_list.index(time.split(" at ")[0])] += 1

unique_date_list = []
for date in iso_date_list:
	if date in unique_date_list:
		pass
	else:
		unique_date_list.append(date)

unique_date_list = sorted(unique_date_list, key=int)
unique_date_count_list = [0 for item in unique_date_list]

for date in iso_date_list:
	unique_date_count_list[unique_date_list.index(date)] += date_count_list[iso_date_list.index(date)]

target = open('date_data.txt', 'w')
target.truncate()
for date in unique_date_list:
	target.write("%s  %s \n" % (date, unique_date_count_list[unique_date_list.index(date)]))
target.close()
print("Created message date data")

# Checks all messages counted - I lose 4 messages
count_check = 0
for item in unique_date_count_list:
	count_check += int(item)
print("Actual messages:", count_check)



###########################################################################
"""Message at Time Analysis"""
###########################################################################

# Makes use of times_list and date_count_list created previously

# Creates list of all times
all_times = []
for hour in range(0,24):
	for mins in range(0,60):
			hourv, minv = "", ""
			if hour < 10:
					hourv = "0"+str(hour)
			else:
					hourv = hour
			if mins < 10:
					minv = "0"+str(mins)
			else:
					minv = mins
			all_times.append(str(hourv)+str(minv))

# Creates a list of dates
time_list = []
for time in times_list:
	time_list.append(time.split(" at ")[1].split(" ")[0].replace(":",""))

unique_time_list = []
for time in time_list:
	if time in unique_time_list:
		pass
	else:
		unique_time_list.append(time)

unique_time_list = sorted(unique_time_list, key=int)
unique_time_count_list = [0 for item in unique_time_list]

for time in time_list:
	unique_time_count_list[unique_time_list.index(time)] += 1

# TEST
all_unique_time_list = []
all_unique_time_count_list = []
never_messaged_times =[]
# binary_message_list = [] for heatmapping
for time in all_times:
	all_unique_time_list.append(time)
	if time in unique_time_list:
		all_unique_time_count_list.append(unique_time_count_list[unique_time_list.index(time)])
		# binary_message_list.append(1) for heatmapping
	else:
		time_parts = list(str(time))
		time_parts.insert(2,":")
		time = "".join(time_parts)
		never_messaged_times.append(time)
		all_unique_time_count_list.append(0)
		# binary_message_list.append(0) for heat mapping
print("Never sent a message at the following %d times: %s" % (len(never_messaged_times), ", ".join(never_messaged_times)))
# TEST

time_labs=[]
for time in all_unique_time_list:
	if (list(str(time))[2]+list(str(time))[3] == "00") and (int(time)%3 == 0):
		time_parts = list(str(time))
		time_parts.insert(2, ":")
		time_labs.append("".join(time_parts))
	else:
		time_labs.append("")

target = open('time_data.txt', 'w')
target.truncate()
for x in range(0, len(all_unique_time_list)-1):
	time_parts = list(str(all_unique_time_list[x]))
	time_parts.insert(2,":")
	time = "".join(time_parts)
	target.write("%s  %s  %s \n" % (time, all_unique_time_count_list[x], time_labs[x])) # binary_message_list[x]
target.close()
print("Created message time data")



###########################################################################
"""Poke Analysis"""
###########################################################################

# Extracting List of Pokes
poke_list = []
poke_file_data = poke_file.split("Pokes")[len(poke_file.split("Pokes"))-1].split("<li>")
for item in poke_file_data:
	if "poked" in item:
		poke_list.append(item.replace('<div class="meta">', ', ').replace(' UTC+01</div></li>',''))
	else:
		pass

# Cleaning up data
last_item = poke_list[len(poke_list)-1]
poke_list.pop(len(poke_list)-1)
poke_list.append(last_item.split('</ul></div><div class="footer">')[0])
temp_list = []
for item in poke_list:
	temp_list.append(item.split('</div>')[0])
poke_list = temp_list
print("Number of pokes:", len(poke_list))



###########################################################################
"""Friends Analysis"""
###########################################################################

all_friend_data = friend_file.split('<h2>Friends</h2>')[len(friend_file.split('<h2>Friends</h2>'))-1]

# Current Friends
current_friend_data = all_friend_data.split('<h2>Sent Friend Requests</h2>')[0].split('<li>')
temp_list = []
for friend in current_friend_data:
	temp_list.append(friend.replace("</li>","").replace("</ul>",""))
temp_list.pop(0)
current_friend_data = temp_list
print("Number of current friends:", len(current_friend_data))

# Sent Friend Requests
sent_friend_data = all_friend_data.split('<h2>Sent Friend Requests</h2>')[1].split('<h2>Received Friend Requests</h2>')[0].split('<li>')
temp_list = []
for friend in sent_friend_data:
	temp_list.append(friend.replace("</li>","").replace("</ul>",""))
temp_list.pop(0)
sent_friend_data = temp_list
print("Number of sent friend requests:", len(sent_friend_data))

# Recieved Friend Requests
recieved_friend_data = all_friend_data.split('<h2>Received Friend Requests</h2>')[1].split('<h2>Removed Friends</h2>')[0].split('<li>')
temp_list = []
for friend in recieved_friend_data:
	temp_list.append(friend.replace("</li>","").replace("</ul>",""))
temp_list.pop(0)
recieved_friend_data = temp_list
print("Number of recieved friend requests:", len(recieved_friend_data))

# Removed Friends
removed_friend_data = all_friend_data.split('<h2>Removed Friends</h2>')[1].split('<li>')
temp_list = []
for friend in removed_friend_data:
	temp_list.append(friend.replace("</li>","").replace("</ul>",""))
temp_list.pop(0)
removed_friend_data = temp_list
last_item = removed_friend_data[len(removed_friend_data)-1].split('</div><div class="footer">')[0]
removed_friend_data.pop(len(removed_friend_data)-1)
removed_friend_data.append(last_item)
print("Number of removed friends:", len(removed_friend_data))



###########################################################################
"""Event Analysis"""
###########################################################################

event_data = event_file.split('<h2>Events</h2>')[len(event_file.split('<h2>Events</h2>'))-1].split('<li>')
event_data.pop(0)

temp_list = []
for event in event_data:
	temp_list.append(event.split('<p class="meta">'))
event_data = temp_list

temp_list = []
for event in event_data:
	temp_list.append([event[0]]+event[1].replace('</p></li>','').split('<br />'))
event_data = temp_list

last_item = [event_data[len(event_data)-1][0], event_data[len(event_data)-1][1], event_data[len(event_data)-1][2].split('</ul></div><div class="footer">')[0]]
event_data.pop(len(event_data)-1)
event_data.append(last_item)
print("Number of events:", len(event_data))

"""This code was designed to seperate out the event dates
but Facebook gives them in an inconsitent format so the
output was similarly inconsistent and difficult to use."""
# day_list = ["Monday,","Tuesday,","Wednesday,","Thursday,","Friday,","Saturday,","Sunday,"]
# for event in temp_list:
#	 for word in event.split(" "):
#		 if word in day_list:
#			 if event.split(" ").index(word)-1 == 0:
#				 print(event.split(event.split(" ")[event.split(" ").index(word)]))
#				 break
#			 else:
#				 print(event.split(event.split(" ")[event.split(" ").index(word)-1]))
#				 break

target = open('event_data.txt', 'w')
target.truncate()
for event in event_data:
	target.write("%s \n" % event[2].replace(" r","R"))
target.close()
