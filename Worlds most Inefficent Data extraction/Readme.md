# Filter Excel with data:

This scirpt is what I call the worlds most inefficent system for extracting data from excel.
# Working
This script allows us to take google adwords SEO csv file and append all entries to a table in mysql, Then this scripts takes out targeted/filtered data from that csv and places it in an csv file so we can work with it a little more.

The reason why I call it worlds most inefficent because it requires us to manually remove many things from csv file and takes a lot of time to append data to mysql. Also this script can easily be created using pandas with least effort but I didn't knew pandas when i created this.

Apart from that its good.

# Usage
columns allowed:
Keyword, Avg_monthly_searches, Competiton

remove anything else from the top even the headers named keyword, avg_monthly searchs, comptetion etc.

also look out for any avg monthly searches section cells which do not contain any value whatsoever, fill those cell with 0 and save the file.

