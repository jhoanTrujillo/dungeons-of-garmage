# Dungeons of Garmage
The project was deployed at the following link - [Dungeons of Garmage]()

Developed by: Jhoan Trujillo

## Introduction 

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
  - Technologies Use
  - Features
  - Code Design Choices
4. Deployment
  - Version Control
  - Heroku Deployment
5. Credits

## 1.Project Goals

### User Goals
As a user I expect: 

- **Immersive Experience**: A storytelling adventure that allows me to immerse myself in the world of Garmage, providing challenges and consequences for my choices, adding weight to my gameplay.
- **User-Friendly Interface**: An easily navigable game with intuitive controls. The language used should be clear and understandable, and information displays should be concise and straightforward
- **Quick Gameplay Sessions**: I anticipate being able to pick up and play the game in short, concise sessions, that allow me to.

[Back to table of content](#table-of-content)

### Site Owner's Objectives
As the site owner, my goal is to offer players an engaging and captivating gaming experience by: 

- Delivering a well-formatted, easily readable dialogue to help users immerse themselves in the story. 
- Clear and concise choices to ensure an enjoyable experience and experience, that still holds the player choices into account. 
- The grammar and language used will be accessible, and the story will be rich and diverse, with differet ways to end the game.

[Back to table of content](#table-of-content)

## User Experience

### Target Audience
The target audience for the budget tracker application includes a diverse range of individuals who are interested in managing their personal finances more effectively.

[Back to table of content](#table-of-content)

### Players
- **As a user** I can pick the game for a quick run, whenever I have a couple of minutes.
- **As a user** I can make choices that will hold weight on the game narrative.
- **As a user** I can register my username, password, and keep track of my global score.
- **As a user** I can leave the game at any time.
- **As a user** I can experience different outcomes based on my choices in any given game run.
- **As a user** I want the formatting of the text to provide key insight into any game event.

[Back to table of content](#table-of-content)

## 3. Design

### Design Choices
This project was design to work with terminal, as such, the choice of style was limited, but I used the Rich a python module to provide as much context in the events of the game via text formatting. That way I can share a feeling with the player by using text formatting alone.

[Back to table of content](#table-of-content)

### Techonologies Used
This project uses the following tech stack:

- Python
  - Main programming language used for the project 
- JS (Node.js)
  - Code created by code institute to run terminal in site. 
- HTML
- Github
- Vscode
- Git
  - For version control.

[Back to table of content](#table-of-content)

### Features
The initial draft of the game started with a couple of choices when it came from game features. I would like to provide some more context into those features below:

- Events - All the events use the same class named Event() which looks for text, an array of options, and if the event has a special category
that way the event parser can apply the logic to the event appropriately.
- Routes: Routes are simple, they are split between two to keep the story moving and avoid choice paralyzis.
- Battle: The battle when over a couple of ideas in the whiteboard. Firstly, it was intended to provide the player with choices to fight, but then I realized that would take away from the narrative, so I added a quick resolution to combat which autoplays and provide an outcome. The latest version only allows for text to be displayed, and for the damage to be auto calculated.
- Item interactions: Items are simply added to an array and then the utility file has the event_handler function which checks the type of event and handles the logic needed to make the event act as expected.

[Back to table of content](#table-of-content)

### Flowchart of behavior

Please see the flowchart in the link below to better understand the behaviour of the program:

- [Flowchart](https://github.com/jhoanTrujillo/dungeons-of-garmage-pp3/blob/6fbfcdfe96ccbd21f08b4a6dd462c9e8e1b73720/repo_images/flowchart.png)

[Back to table of content](#table-of-content)

## 4. Deployment

### Version Control
For version control I used github and the best practices highlited by [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) 
to improve the readability of the comments. Sadly, the new convention was adopted half-way thought the project, but they are kept consistent afterwards. 

The workflow follow to upload the project to github was simple. Just using the commands: 

- git add - To stage the changes.
- git commit -m "`<\type>[optional scope]: <\description>`" - To add a message and commit the changes to be pushed.
- git push - Lastly, push command to send the changes to our github repo. 

[Back to table of content](#table-of-content)

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

Lastly, you can install this project's requirements by using: `pip3 install -r requirements.txt`. If you have your own packages that have been installed, then the requirements file needs updated using: `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command: `echo web: node index.js > Procfile`

[Back to table of content](#table-of-content)

### Testing 

For testing purposes I used the following: 

- Python linter provided by code institute [pep8 checker](https://pep8ci.herokuapp.com/#), the checks to the run, utility, choices, and character .py files are properly execute and compliant with python's standards. 

[Back to table of content](#table-of-content)

### Bugs

At the moment, the majority of the issues I would like to fix are style related, and possibly built a solution to be able to use the styling of the print imported from the rich module, and slow_printing at the same time. Other than that, I believe everything else seems in order. 

> Note: I troubleshoot and tested extensibely to make sure the main mechanics and progression of story wasn't bugged down by anything. But then again I added several routes which I might not have experience myself in the story. 

[Back to table of content](#table-of-content)

## 5. Credits 

## Resources
This are the resources I used externally from other sites such as stack overflow, ASCII TODAY, pipreqs:

- The following [stackoverflow code](https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing) was used for the slow_print function.
- [Pipreqs](https://pypi.org/project/pipreqs/) was used to create a requirement file that uses local file modules to create the requirements.txt file. 
- [ASCII TODAY](https://ascii.today/) - is a fast title generator that converts text to ASCII 
- [diagrams.net](https://app.diagrams.net/) - free diagram maker tool

### Modules
Below you can find all the external modules use in the project.

- [Rich - a Python library for rich text and beautiful formatting in the terminal](https://github.com/Textualize/rich)
