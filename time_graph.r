# Created to get data from file and turn
# it into a graph which is then outputed
# as a PDF file to be later use in report.

# Gets Data From File
time_file = read.table(file="time_data.txt", header=F, fill=T)
data = c(time_file)

# Saving the Pie Chat As a PDF
pdf("time_graph.pdf")
barplot(data[[2]], names.arg=data[[3]], xlab="Time Split By Hour", ylab="Messages",
	main="Graph Showing Total Messages Sent at a Given Time")
abline(v = (seq(0, 1800, 75)), col="lightgray", lty="dotted")
dev.off()

# Heatmap sensitivity
# pdf("time_bar.pdf")
# barplot(height=data[[2]], xlab="Time Split By Hour", ylab="Messages",
# 	main="Graph Showing Total Messages Sent at a Given Time")
# dev.off()
