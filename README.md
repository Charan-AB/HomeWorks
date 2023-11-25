credentials_info contains details regarding the connection to gcp cloud
data_api_to_gcp is for extracting the data from the api and then storing it in a gcp bucket (data lake)
data_transform is to pre process the data, performing dimensional data modeling, writing transformed data into the gcp bucket
data_to_postgres_gcp is to read the transformed data from gcp and then load it into the postgres database in gcp
