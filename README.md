[![codecov](https://codecov.io/gh/natan-dias/personal-kb-api/graph/badge.svg?token=J54LT6XYZ2)](https://codecov.io/gh/natan-dias/personal-kb-api)<img alt="Python" src="https://img.shields.io/badge/-python-F7B93E?style=flat-square&logo=python&logoColor=white" /><img alt="Flask" src="https://img.shields.io/badge/-Flask-000?style=flat-square&logo=flask&logoColor=white" />

# Personal Knowledge Base Simple API

## The Goal! :tada:

I have a bad memory :sweat_smile: ! So, in order to deal with that and work with IT, I like to spend some time wrinting useful commands and doing a lot of practice with lab environments and even here, in this repository, because I belive in "learning by doing" style. 

But over more than 15 years working with that, I believe I have now an issue to find commands using my knowledge base. Of course, today we have a LOT of great IA tools and good search engines to help us with that, but I really like to have my own custom database, with commands that make sense for me or have some kind of useful tip that I need in my day-to-day work.

## The issue :scream:

Like I said, over the year I basically store a lot of commands in small and simple `.md` files, which was good but now I have hundreds of files with a lot of information and very painful to search. I could use IA, but why not get this opportunity to learn something :smile:.

## The task :muscle:

My goal was to leave from basic `.md`files to something more structured and maybe easier to search and edit. 

Before:

<img src="pictures/old-text-knowledge-base.png" width="100%"/>

After:

<img src="pictures/sql-visualization.png" width="100%"/>

Postmand Visualization:

<img src="pictures/postman-visualization.png" width="100%"/>

### Python :snake:

To achieve that, I have started to write a small API and use flask to be able to perform some requests, add commands, categories and edit them. In order to have a persistent data, of course, store that in a database.

As a DevOps engineer with a more infrastrucure than coding background, it was a good opportunity to increase my Python skills and also to learn more about how to create a REST API using this programming language. 

So the result is what you can find in this repository :blush:

## Instalation

There is still a lot of things to do here, but for now the installation is quite simple.

### Prerequisites

- Python 3.10 or higher
- PIP 24.0 or higher

### Requirements

Just install them using:

> pip install -r requirements.txt

### Running

> python main.py

This will start a Flask app in localhost which can also be accessible via browser, looking for the `healthcheck` page.

<img src="pictures/healthcheck.png" width="100%"/>

## API Documentation

Please check the full [API documentation HERE](./API-documentation.md).

## Next Steps

- Dockerize app
- Migrate to Postgres
- Kubernetes Deployment
