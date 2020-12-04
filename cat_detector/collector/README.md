# collector

A module built with `python`, [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [SQLAlchemy](https://docs.sqlalchemy.org/en/13/) and ran originally on an [AWS EC2](https://aws.amazon.com/ec2/) instance that accepts pictures sent by an authenticated client (through Basic-AUTH) and exposes information about the provided content

To detect the presence of a cat in an uploaded photo, the collector module uses [AWS Rekognition](https://aws.amazon.com/rekognition/) 

The extracted information is stored in an [AWS RDS](https://aws.amazon.com/rds/) MySQL instance  

The first photo containing a cat that was detected during a meal is stored in an [AWS S3](https://aws.amazon.com/s3/) bucket

The `AWS` resources that were used are part of the [AWS Free Tier](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc)

#
## Structure
- `app.py` - a `Flask` application exposing multiple HTTP endpoints
    - `/collect` - accepts a photo in base64 format and tries to detect a cat, storing information regarding its presence
    - `/data?days=10` - returns the number of meals/day for the last *10 days*
    - `/detail?day=3&month=12&year=2020` - returns the number of meals/hour for a specific day
    - `/pictures` - returns the last `n` pictures stored in the `S3` bucket
- `config.yaml` - a file containing AWS credentials in a `YAML` format
- `config.py` - a loader that reads the `config.yaml` content and caches it
- `db.py` - database connection and configuration
- `event.py` - database model declaration
- `observer.py` - a class that handles object detection and interacts with other `AWS` resources
- `requirements.txt` - a file containing dependencies declaration

#
## Deployment
1. Install [python 3+](https://www.python.org/downloads/)
    - `pip` and `virtualenv` should also be installed - on Windows they should be installed by default, on Linux-based systems you may have to install them separately

2. Create a virtual environment to avoid polluting the global packages
    - `python3 -m venv sandbox --clear`

3. Activate the virtual environment
    - Windows: `sandbox/Scripts/activate`
    - Linux: `source sandbox/bin/activate`

4. Install the dependencies
    - `pip install -r requirements.txt`

5. Fill the `config.yaml` file with adequate inputs

6. Run the application
    - `flask run`
    - if you want to deploy it for real, you can use something like [uWSGI](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04)