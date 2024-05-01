# stat405project

**Files Description:**

build_data.sh: Bash script that sets up the environment, downloads and processes the data, runs the analysis script, and cleans up the workspace.

build_data.sub: HTCondor submission file that configures the job's resources and execution environment.

analyze_data.py: Python script that performs the data analysis (ensure this script is properly configured to handle the input data format and desired analysis).

kaggle.json: Contains Kaggle API credentials.


**Steps to Run the Job:**

**Prepare Your Workspace:**
Ensure you have the build_data.sh, build_data.sub, analyze_data.py, and kaggle.json files in your working directory on the HTCondor submission node (e.g., learn.chtc.wisc.edu).

Submit the Job:
Open a terminal on the HTCondor submission node.
Navigate to the directory containing your files.
Submit the job to HTCondor by running the following command:
bash

**condor_submit build_data.sub**

This command will queue your job for execution according to the resources specified in build_data.sub.

Monitor the Job:
You can monitor the status of your job using:
bash

**condor_q**

To get more detailed information about your job's status, use:
bash

condor_q -better-analyze <job_id>

Replace <job_id> with the actual job ID provided when you submitted the job.

Review Output and Logs:
Once the job completes, output and error logs specified in build_data.sub (download_data.out and download_data.err) will contain information about the job's execution and any issues encountered.

If configured in your analyze_data.py, the output results (analysis.csv or similar) should be in the same directory or specified output location.

Cleanup
The script build_data.sh is designed to remove all intermediate files after the job completes. Ensure this behavior aligns with your data management policies and adjust if necessary.



**Cluster Analysis:**
The cluster column categorizes movies into groups based on their similarities in rating, release year, and runtime, helping identify patterns or groupings that may not be immediately obvious.

Regression Prediction: The predicted_cluster provides an estimation of the cluster group for each movie based on the linear regression model, offering insights into how well the model predicts or fits the data based on the input features.


The analysis_results.csv file captures detailed analysis of movie data through both clustering and regression models, reflecting various aspects of movies released between 2018 and 2023. Here's an elaboration of what the contents mean:

**rating:** The viewer ratings for the movies, scaled typically from 1 to 5. Higher ratings generally indicate better viewer reception.
date: The release year of each movie. This dataset includes movies from the years 2018 to 2023.

**runtime:** The length of each movie in minutes. It shows a range in this dataset from as short as 82 minutes to as long as 129 minutes.

**cluster:** Derived from a KMeans clustering process, this column classifies movies into groups (clusters) based on similarities in their ratings, release years, and runtimes. Here, all example movies fall into cluster '0', suggesting they are similar according to the clustering model's criteria, possibly indicating a particular type or genre of movies that share these attributes.


**predicted_cluster:** The predicted cluster labels based on a linear regression model. These values are continuous due to the nature of regression models, which predict a numeric output. The predicted values are quite close to zero (since they've been trained to predict the cluster which is a discrete label), and these can be interpreted as the model's confidence or proximity to the cluster center defined by the clustering algorithm. For example, a predicted cluster value close to 0 (like 0.039) suggests a strong fit or closeness to cluster '0'.

**Insights from the Output** (NEEDS TO BE UPDATED)
The clustering suggests a significant grouping or similarity in the movie attributes within cluster '0'. This could be explored further to understand common themes, genres, or other characteristics that might be influencing this clustering.
The regression model's outputs indicate how closely each movie aligns with the characteristics of its cluster. Movies with predicted cluster values close to 0 fit well within their assigned cluster based on the model's training.
