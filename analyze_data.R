args <- commandArgs(trailingOnly = TRUE)
data_path <- args[1]

# Load the data
data <- read.csv(data_path)

# Perform your analysis
# For example, a summary of ratings
summary_stats <- summary(data$rating)
print(summary_stats)

# Save results to a file or for further processing
write.csv(data, file = 'processed_data_R.csv')
