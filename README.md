# BlogAi

A blog that's created by AI with openai API & vercel blog template.

Demo : https://blogai-five.vercel.app

<img width="1177" alt="main_page" src="https://github.com/yasarkaancan/aiblog/assets/66377701/d431f76c-17c8-4b62-98e8-a47ebb9a8c46">

<img width="1177" alt="post_page" src="https://github.com/yasarkaancan/aiblog/assets/66377701/71ce9276-005f-4f10-87c9-c76f904ec103">



## How it works ?

With the python openai library you can make API call's to the openai's ai models. In this project, with the davinci model we give the model the syntax and the topic (can be random) that we want and the ai and python take's the rest of the work.

## How to install & use ?

- Simply sign in to vercel & deploy the "Next.js Contentlayer Blog Starter" template and pull it to your computer.

- Then open a new directory on your computer and initialize the git and do the following :

`git init`

`git remote add origin https://YOUR_REPOSITORY_LINK.git`

`git pull origin main`

- Then inside the root folder of the blog template clone this repository

`git clone https://github.com/yasarkaancan/aiblog.git`

- Install the requirements from requirements.txt

`pip install -r requirements.txt`

- Edit the python script and enter your openai API key.

- Run the script with python.

`python content.py`

- Congrats ! You are ready to go !

- When you make update's and push it to github it will be automatically updated on the vercel. 

! You could use different blog's or different syntax but in that case you should delete the prompt and rewrite it yourself.
