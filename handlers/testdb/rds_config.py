#config file containing credentials for RDS MySQL instance
import os

rds_host = os.getenv('RDS_HOST')
db_username = os.getenv('RDS_DB_USERNAME')
db_password = os.getenv('RDS_DB_PASSWORD')
db_name = os.getenv('RDS_DB_NAME')