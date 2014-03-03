# Created to get data from file and turn
# it into a graph which is then outputed
# as a PDF file to be later use in report.

# Gets Data From File
date_file = read.table(file="date_data.txt", header=F, fill=T)
data = c(date_file)

# Saving the Pie Chat As a PDF
pdf("date_graph.pdf")
barplot(data[[2]], xlab="Date", ylab="Messages",
	main="Graph Showing Messages Over Time")
dev.off()
