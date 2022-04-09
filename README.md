# Cloud Computing Mini Project, Group 44

This repo contains the mini project for group 44 for the Queen Mary Computing and Information Systems MSc Cloud Computing module.

We used Lab 5 from the QMUL cloud computing module [1] as the basis for our application, which will allow users to get and post information about music and artists.

# How to run app

- Clone this repo onto GCP VM instance (see lab notes for creating VM instance)
- Open terminal on your instance (see lab notes for how)
- Use the following commands to install docker:
  - `sudo apt update`
  - `sudo apt install docker.io`
- From terminal go to the app folder:
  - `cd cloud_computing_coursework_g44/app`
- Build:
  - `sudo docker build . -t music_app`
- Run:
  - `sudo docker run -p 80:80 music_app`
- Test it works by going to the IP address of your VM instance, add :80 (for the port), you should see a page saying 'Welcome to music finder!'
- If you now add `/records/all_bands/` to the URL you should see '["Radiohead","Portishead"]'

# External API
- We've implemented a call to the iTunes API which will return a URL to a video by the users chosen band. The way to make the call is as follows
  - `<GCLOUD_EXT_IP>:80/records/video/<BAND_NAME>`
  - e.g. http://35.234.153.246:80/records/video/portishead would get a link to an iTunes video by Portishead if your GCloud external ip were 35.234.153.246

# References

[1] Lab 5, QMUL cloud computing module: https://qmplus.qmul.ac.uk/mod/folder/view.php?id=1889568
