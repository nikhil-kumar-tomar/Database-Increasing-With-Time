# Filter Excel with data:
This script is what I call the world's most inefficient system for extracting data from Excel.
# Working
This script allows us to take Google Ads SEO CSV file and append all entries to a table in MySQL. 
Then this scripts takes out targeted/filtered data from that CSV file and places it in a new CSV file, so we can work with it a little more.

The reason I call it world's most inefficient because it requires us to manually remove many things from CSV file and takes a lot of time to append data to MySQL. Also, this script can easily be created using pandas with the least effort, but I didn't know pandas when I created this.

Apart from that, it's good.

# Usage
columns allowed: Keyword, Avg_monthly_searches, Competition

Remove anything else from the top even the headers named keyword, avg monthly searches, completion etc.

Also look out for any avg monthly searches section cells which do not contain any value whatsoever, fill those cells with 0 (this can be easily done using pandas as well) and save the file.