# Dungeons of Garmage
The project was deployed at the following link - [Dungeons of Garmage]()

Developed by: Jhoan Trujillo

## Introduction 
**"Dungeons of Garmage"** is a choose-your-own-adventure game that transports players to a fictional dungeon in a strange fantasy land. Players become immersed in a sense of dread and adventure, and are provided with the ability to choose their own path in the game. The idea is for players to select between various choices presented by the game, leading to different endings based on their decisions.

## Table of Content
1. Project Goals
  - User Goals 
  - Site Owner Goals
2. User Experience
  - Target Audience
  - User Stories
  - Players
3. Design
  - Design Choices
  - Technologies use 
  - Code Design Choices
4. deployment
  - Version Control
  - Heroku Deployment
5. Credits

## 1.Project Goals

### User Goals
As a user I expect: 

- **Immersive Experience**: A storytelling adventure that allows me to immerse myself in the world of Garmage, providing challenges and consequences for my choices, adding weight to my gameplay.
- **User-Friendly Interface**: An easily navigable game with intuitive controls. The language used should be clear and understandable, and information displays should be concise and straightforward
- **Quick Gameplay Sessions**: I anticipate being able to pick up and play the game in short, concise sessions, that allow me to .

### Site Owner's Objectives
As the site owner, my goal is to offer players an engaging and captivating gaming experience by: 

- Delivering a well-formatted, easily readable dialogue to help users immerse themselves in the story. 
- Clear and concise choices to ensure an enjoyable experience and experience, that still holds the player choices into account. 
- The grammar and language used will be accessible, and the story will be rich and diverse, with differet ways to end the game.

[Back to table of content](#table-of-content)

## User Experience

### Target Audience
The target audience for the budget tracker application includes a diverse range of individuals who are interested in managing their personal finances more effectively.

### User Stories
Here are the Users stories which can also be found here on the project Kanban board:

### Players
- **As a user** I can pick the game for a quick run, whenever I have a couple of minutes.
- **As a user** I can make choices that will hold weight on the game narrative.
- **As a user** I can register my username, password, and keep track of my global score.
- **As a user** I can leave the game at any time.
- **As a user** I can experience different outcomes based on my choices in any given game run.
- **As a user** I want the formatting of the text to provide key insight into any game event.

## 3. Design

### Design Choices
This project was design to work with terminal, as such, the choice of style was limited, but I used the Rich a python module to provide as much context in the events of the game via text formatting. That way I can share a feeling with the player by using text formatting alone.

## 4. Deployment

### Version Control
For version control I used github and the best practices highlited by [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) 
to improve the readability of the comments. Sadly, the new convention was adopted half-way thought the project, but they are kept consistent afterwards. 

The workflow follow to upload the project to github was simple. Just using the commands: 

- git add - To stage the changes.
- git commit -m "<\type>[optional scope]: <\description>" - To add a message and commit the changes to be pushed.
- git push - Lastly, push command to send the changes to our github repo. 

### Heroku
Heroku, is the **PaaS** (Platform as a service) of choice for this project. To deploy the project below 

- In the top-right corner of the Heroku Dashboard, Click **New > Create new app**.
- Select an unique app name (It must be unique to be deployed) > choose the closest region to your location (EU or USA), and select **Create App**.
- In our new app, Go over **Settings > on Config Var, click reveal config var > set the value of KEY to PORT, and the value to 8000 then select add**.
- Then below in **Add buildpack** button.
- The order of the buildpacks is important, select **Python first**, then **Node.js**. (if they are not in this order, you can drag them to rearrange them)
- Important: Heroku needs two additional files in order to deploy properly.

  - requirements.txt
  - Procfile

Lastly, you can install this project's requirements by using: pip3 install -r requirements.txt. If you have your own packages that have been installed, then the requirements file needs updated using: pip3 freeze --local > requirements.txt

The **Procfile** can be created with the following command: echo web: node index.js > Procfile

## 5. Credits 

## Resources

### Modules
Below you can find all the external modules use in the project.

- [Rich - a Python library for rich text and beautiful formatting in the terminal](https://github.com/Textualize/rich)
- The following [stackoverflow code](https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing) was used for the slow_print function.
- [Pipreqs](https://pypi.org/project/pipreqs/) was used to create a requirement file that uses local file modules to create the requirements.txt file. 
- [ASCII TODAY](https://ascii.today/) - is a fast title generator that converts text to ASCII 