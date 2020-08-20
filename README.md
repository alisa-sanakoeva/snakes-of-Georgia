# Snakes Flask Server [demo]
Flask Web Server for project "Snakes of Georgia"

## Documentation
This is a database to contain data about snakes that are native to Georgia

**Methods**:

GET : _/snakes_

GET : _/snakes/<string:species>_

POST : _/snakes/<string:species>_

`latin_name` type: string

`location` type: string

`date` type: string

PUT : _/snakes/<string:species>_

`latin_name` type: string

`location` type: string

`date` type: string

DELETE : _/snakes/<string:species>_

POST : _/registration_

`username` type: string

`password` type: string

DELETE : _/registration_

`username` type: string

`password` type: string
