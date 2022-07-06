
# Final Task In Docker

Create a Python Web APP using FLASK that:  
● Presents the Current BitCoin Price (LIVE)  
● Stores the price in a Redis Database  
● Presents the Average Price for the last 10 minutes (LIVE) 

## Run Locally

Clone the project

```bash
  git clone https://github.com/mohamadassi173/Docker-Final-Task.git
```

Go to the project directory

```bash
  cd Docker-Final-Task
```

Build

```bash
  docker compose up
```

Run

```bash
  http://127.0.0.1:8000/
```


https://user-images.githubusercontent.com/57872327/177614184-d023bf0b-a810-4b07-ad04-acc38f23e515.mp4



## DockerHub

Run the image from DockerHub

```bash
  docker pull mohamadassi173/bitcoin-flask
  docker run -d -p 8000:5000 mohamadassi173/bitcoin-flask:latest
```
<img width="932" alt="image" src="https://user-images.githubusercontent.com/57872327/177643708-e471383c-7a00-4601-9f9b-4986d45e87ad.png">

## Jenkins 
CI/CD that creates and pushes the generated Web application Docker image to Docker Hub  
<img width="662" alt="image" src="https://user-images.githubusercontent.com/57872327/177614069-498a87bc-2dd5-4874-a033-b08495668615.png">

## Author

- [@Mohamad Assi](https://github.com/mohamadassi173)

