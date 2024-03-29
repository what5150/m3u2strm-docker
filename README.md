# Thanks to hooray4me!
## m3u2strm-docker

m3u2strm-docker is a fork of hooray4me's python script (https://github.com/hooray4me/m3u2strm) that is used to consume the VOD (video on demand) tv shows, movies and events from an apollogroup.tv subscription and make it into libraries useable by emby. It has been modified to run in a docker container. **Python-3.8** docker image was used for the build.

**Pre-reqs:**
1. Docker...

**Setup:**
1. `git clone https://github.com/what5150/m3u2strm-docker.git`
2. `cd m3u2strm-docker`
2. Create directories for the containers persistent "media" data. 
   1. `mkdir -p media/tvshows media/movies media/events`
4. If you want to keep logs, create a folder to mount for persistent storage logs:/app/logs
5. Depending on how you setup docker you may need to adjust permissions for the folders you created.
6. Create a file to contain your environment variables 
7. `nano .env`
   1. ```
      provider=apollo
      user=YOURUSERNAME
      pw=YOURPASSWORD
      # funct options - all, events, movies, tv
      funct=all
      tvlistend=28
      eventlistend=12
      ```

**Run:**
1. `docker build -t m3u2strm-d .`
1. `docker run -v ./media:/media -v ./logs:/app/logs --env-file ./.env --name m3u2strm-d m3u2strm-d`

**Running after initial run:**
1. After the initial run the container is already created. All that is needed is to start it.
2. Run once a day (or less)
2. `docker start m3u2strm-d`

**CRON setup (after initial run)**
1. You may have to use root's crontab depending on how your docker was installed/setup
2. `crontab -e`
   1. or `sudo crontab -e` if root is needed
2. `0 0 * * * docker start m3u2strm-docker`

**Installation and setup:**
1. Clone this repo (requires git to be installed). We clone to the root.

In emby, create a tvshows and movies library that points to these paths.

