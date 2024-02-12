import io
import requests
from google.cloud import storage
import itertools

services = ["green"]
years = ["2022"]
months = list(i for i in range(1, 13))

bucket_name = "lively-citizen-412110-terra-bucket-homework-3"

# Create a client
gcs_client = storage.Client()

# Get the bucket
bucket = gcs_client.get_bucket(bucket_name)

for service, year, month in itertools.product(services, years, months):
    month_str = f"{month:02d}"
    file_name = f"{service}_tripdata_{year}-{month_str}.parquet"
    request_url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{file_name}"
    object_key = f"{service}/{year}/{file_name}"

    print(f"Processing {file_name}...")

    try:
        # Fetch the Parquet file
        response = requests.get(request_url, stream=True)
        response.raise_for_status()

        # Ensure we're streaming the content
        response.raw.decode_content = True

        # Upload the file to GCS
        blob = bucket.blob(object_key)
        # Use io.BufferedReader to wrap the raw stream for compatibility
        blob.upload_from_file(io.BufferedReader(response.raw))
        print(f"Successfully uploaded {file_name} to {object_key} in GCS.")


    except requests.HTTPError as e:
        print(f"HTTP Error for {file_name}: {e}")
    except Exception as e:
        print(f"Error processing {file_name}: {e}")
