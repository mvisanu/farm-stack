Now,  the prerequisites to follow along is to have the basic understanding of the following  :

1- HTTP request methods
2- Async/Await Syntax
3- Python language in general and FASTAPI in particular
4- JavaScript ES6 and React JS basics
5- Database systems, and specially NOSQL
6- Fundamentals of MongoDB
7- How client talks to the server ( Axios / HTTP methods )


We have also created a CRUD Application, where you will understand :
How to connect FastAPI - where your server side code lives - with mongoDB database. 
And together we can connect the backend to the frontend where React can send and receive HTTP requests to and from the server.

requirements.txt
fastapi == 0.65.1
uvicorn == 0.14.0
motor == 2.4.0

pip install pipenv

activate by
pipenv shell

--run app server
uvicorn main:app --reload

--create-react-app
npx create-react-app frontend

--to run
npm start

npm install axios bootstrap