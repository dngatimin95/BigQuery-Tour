"""
The code below creates a table that finds the nearest port given a coordinates
with provisions, water, fuel and diesel from the geo_international_ports dataset
and stores it within a dataset. A dataset foodpanda_project is created if the
specified dataset does not exist within the project folder 'bigquery-tour'.
"""

import os
from google.cloud import bigquery
from google.cloud.exceptions import NotFound

# Set up environment variable to the path of JSON file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "bigquery-tour-635ad9479312.json"

# Create new Google BigQuery client using Cloud Platform project default
client = bigquery.Client()

# Reference to project id and new or existing dataset
project_id = "bigquery-tour"
dataset_id = "tour-dataset"
full_dataset_id = "{}.{}".format(project_id, dataset_id)

# Check to see if dataset already exists within project, if not then create new BigQuery dataset
try:
    dataset = client.get_dataset(full_dataset_id)
    print("Dataset {} exists".format(full_dataset_id))
except NotFound:
    print("Dataset {} not found, creating new dataset".format(full_dataset_id))
    db = bigquery.Dataset(full_dataset_id)
    dataset = client.create_dataset(db)

# Reference to new table for storing query results
table_id = dataset.table("distress_call_port")

# Configure query job and set destination as new table mentioned above
job_config = bigquery.QueryJobConfig(destination = table_id)

# Query to find the nearest port given a coordinates with provisions, water, fuel and diesel
query = """
    SELECT country, port_name, port_latitude, port_longitude
    FROM bigquery-public-data.geo_international_ports.world_port_index
    WHERE provisions = TRUE AND water = TRUE AND fuel_oil = TRUE AND diesel = TRUE
    ORDER BY ST_DISTANCE(port_geom, ST_GEOGPOINT(-38.706256, 32.610982))
    LIMIT 1"""

# Run query and wait for it to finish
query_job = client.query(query, job_config = job_config)
query_job.result()
print("Query results loaded onto table {}".format(table_id))
