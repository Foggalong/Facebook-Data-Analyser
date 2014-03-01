# Created to get data from file and turn
# it into a pie chat which is then outputed
# as a PDF file to be later use in report.

# Gets Data From File
event_file = read.table(file="event_data.txt", header=F)
outcomes = table(c(event_file))

# Creates a simple pie chart
slices = c(outcomes["Attending"], outcomes["Declined"], outcomes["NoReply"], outcomes["Maybe"])
labels = c("Attending", "Declined", "No Reply", "Maybe")
percentages = round(slices/sum(slices)*100, digits = 1)
labels = paste(labels, ": ", round(slices),"\n   (",percentages,"%)",sep="")
colours = c("#9EF0A4", "#E86D6D", "#BDBDBD", "#F5E487")
pie(slices, labels = labels, col = colours, main = "Pie Chart of Event Responses")
