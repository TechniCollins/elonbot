**NOTE:** This project began as a fork of [elonbot](https://github.com/vslaykovsky/elonbot/blob/master/elonbot.py), but is now a web app with an almost entirely different purpose. It now serves a wider audience - individuals who want to keep track of what specific twitter accounts publish and invoke APIs based on keyword and timing.

## Running the app for the first time

1. ssh into the server.

2. Clone the project; https://github.com/shome/elonbot.git

3. `cd elonbot`

4. `nano .env` then add environment variables

5. `sudo docker-compose up --build -d`

6. `sudo docker-compose exec web python manage.py migrate`

7. (V1 only) Go to the UI and add the user id you want to follow

8. Start the streaming script with one of the following commands depending on whether you are running v1 or v2;

**API Version 1**

`sudo docker-compose exec web python manage.py run_stream --use-image-signal > /home/ubuntu/logs.log 2>&1 &`

**API Version 2**

`sudo docker-compose exec web python manage.py run_stream --user=username --use-image-signal > /home/ubuntu/logs.log 2>&1 &`


## Changing filter stream

This has to be done every time you want to change the user to follow. For V1, ensure you change the user ID from the user interface first.

1. ssh into the server

2. If a stream is already running, disconnect by killing the process running it. You can find the process id by running `ps aux | grep run_stream`. Then `sudo kill -9 <pid>`

3. Finally, run the appropriate (as discussed above)


**NOTE:** All the `docker-compose` commands have to be run in the project's root directory, `elonbot/`, where the compose file is located.


