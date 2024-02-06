## 1.1.1 Introduction to Google Cloud Platform

<iframe width="560" height="315" src="https://www.youtube.com/embed/18jIzE41fJ4?si=rj3_gEuUqHqTU77-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

- Cloud computing services offered by Google
- Includes a range of hosted services for compute, storage and application development that run on Google hardware
- Same hardware and infrastructure that Google uses internally for its end-user products, such as Google Search, Gmail, file storage, and YouTube
- It has a LOT of services! - explore later

TODO:
- [ ] Explore the services offered by GCP
- [ ] Take a google cloud mini-course
- [ ] Add the data to be used in this course to bucket


## 1.2.1 Introduction to Docker

<iframe width="560" height="315" src="https://www.youtube.com/embed/EYNwNlOrpr0?si=9ZNehA6bRrrQSXK2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

- For the error I got wile trying to run Dcker without sudo:
    The error message you're seeing is due to a lack of permissions when trying to connect to the Docker daemon socket. This is a common issue when the current user doesn't have the necessary rights to execute Docker commands.

    The Docker daemon socket is a Unix socket used by Docker to communicate with the Docker daemon, which is responsible for building, running, and managing Docker containers. The error message indicates that the current user doesn't have the necessary permissions to communicate with this socket.

    To fix this issue, you can either run the Docker command as a superuser using `sudo`:

    ```bash
    sudo docker run hello-world
    ```

    Or, you can add the current user to the `docker` group, which has the necessary permissions to communicate with the Docker daemon socket:

    ```bash
    sudo usermod -aG docker $USER
    ```

    After running this command, you'll need to log out and log back in for the changes to take effect.

- A daemon is a type of program in Unix and Unix-like operating systems that runs in the background, rather than under the direct control of a user. They are usually initiated as background processes. In the context of Docker, the Docker daemon is a service that runs in the background on your host operating system and manages everything required to run and interact with Docker containers.


## 1.3.1 Terraform

<iframe width="560" height="315" src="https://www.youtube.com/embed/s2bOYDCKl_M?si=bS-nKBlkAHfFTD5G" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Terraform is an open-source Infrastructure as Code (IaC) software tool created by HashiCorp. It allows developers to define and provide data center infrastructure using a declarative configuration language. This means you describe your desired state of infrastructure, and Terraform will figure out how to achieve that state. 

Terraform can manage a wide variety of service providers as well as custom in-house solutions. It provides a unified view of all resources and services and an elegant way to create, change, and improve infrastructure with ease. It's widely used in automating and managing infrastructure for cloud platforms like AWS, Google Cloud, Azure, and many others.



