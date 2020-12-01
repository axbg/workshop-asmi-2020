from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import load_vars

env_vars = load_vars()

engine = create_engine('mysql+pymysql://{}:{}@{}'.format(env_vars['AWS_RDS_USER'], env_vars['AWS_RDS_PASSWORD'], env_vars['AWS_RDS_URL']))

Session = sessionmaker(bind = engine)

Base = declarative_base()