from config import load_vars
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

env_vars = load_vars()

connection_url = 'mysql+pymysql://{}:{}@{}'.format(
    env_vars['AWS_RDS_USER'], env_vars['AWS_RDS_PASSWORD'], env_vars['AWS_RDS_URL'])

engine = create_engine(connection_url)
Session = sessionmaker(bind=engine)
Base = declarative_base()
