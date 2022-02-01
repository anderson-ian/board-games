#set parameters for download
$ProgressPreference = 'SilentlyContinue'

# download the details data
Invoke-Webrequest -Uri https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-01-25/details.csv -OutFile ..\data\01_raw\details.csv

# download the ratings data
Invoke-Webrequest -Uri https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-01-25/ratings.csv -OutFile ..\data\01_raw\ratings.csv