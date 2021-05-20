# BigQuery_Tour

This repo contains multiple scripts which queries results from the geo_international_ports dataset and stores it in a table within my own dataset under the bigquery-trial project on Google Cloud Platform. There are scripts for each individual questions. Since most of the code in the three scripts are similar, I could create a function and pass different table names and SQL query into the function to simplify things but having three seperate files follows the guidelines set by the question and is easier to understand.

1. The first script `nearest_ports.py` queries a table that finds the 5 nearest ports to Singapore's JURONG ISLAND port.
2. The second script `number_of_ports.py` queries a table that finds the country that has the largest number of ports with a cargo wharf.
3. The final script, `distress_call_port.py` creates a table that finds the nearest port given a coordinates with provisions, water, fuel and diesel.

To use this repo, first download the files and ensure that the correct packages are installed (google-cloud/google-cloud-bigquery). Then just run the scripts (e.g. `python nearest_ports.py`) and it should create the tables under the 'bigquery-trial' project folder under the bigquery-tour dataset! 
