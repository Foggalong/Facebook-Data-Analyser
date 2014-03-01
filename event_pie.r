# Created to get data from file and turn
# it into a pie chat which is then outputed
# as a PDF file to be later use in report.

# Gets Data From File
event_file = read.table(file="event_data.txt", header=F)
outcomes = table(c(event_file))

# Creates a simple pie chart
slices = c(outcomes["Attending"], outcomes["Declined"], outcomes["NoReply"], outcomes["Maybe"])
labels = c("Attending", "Declined", "NoReply", "Maybe")
pie(slices, labels = labels, main = "Pie Chart of Event Responses")
