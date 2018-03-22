# Project Skeleton
Skeleton for a DRF/React/Docker project.

# Set up
Replace {project_name} with your project name:
```git clone https://github.com/tonypedraza/project-skeleton.git {project_name}```

Change the nginx and django container names to reflect the project name (instead of alloy)

If you haven't installed docker:

Install docker: https://www.docker.com/community-edition

Install docker-compose: https://docs.docker.com/compose/install/ 
(Note that the Docker for Mac and Docker for Windows installations already include docker-compose.)

Run ```make startdocker```

The site should be running at http://127.0.0.1:8000/
