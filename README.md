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
- Test it works by going to the IP address of your VM instance, you should see a page saying 'Welcome to music finder!'
- If you now add `/records/all_bands/` to the URL you should see '["Radiohead","Portishead"]'
- Try `<ext_ip>/records/video/Radiohead` and you should get a link to an itunes video by radiohead

# References

[1] Lab 5, QMUL cloud computing module: https://qmplus.qmul.ac.uk/mod/folder/view.php?id=1889568
