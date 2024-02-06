variable "credentials" {
  description = "My Credentials"
  default     = "../keys/lively-citizen-412110-6cefac031360.json"
  #ex: if you have a directory where this file is called keys with your service account json file
  #saved there as my-creds.json you could use default = "./keys/my-creds.json"
}


variable "project" {
  description = "Project"
  default     = "lively-citizen-412110"
}

variable "region" {
  description = "Region"
  #Update the below to your desired region
  default = "europe-west3"
}

variable "location" {
  description = "Project Location"
  #Update the below to your desired location
  default = "EU"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  #Update the below to what you want your dataset to be called
  default = "demo_dataset_dezoomcamp"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  #Update the below to a unique bucket name
  default = "lively-citizen-412110-terra-bucket-mage"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
