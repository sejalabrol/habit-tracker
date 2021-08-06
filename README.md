# Habit Tracker
A Python script using [Pixela](https://pixe.la/) to generate a graph to store the progress of any habit, goal etc

## Screenshot
![ss](https://user-images.githubusercontent.com/87208681/128559855-b1c982be-cce5-469e-ba07-0b7415bf5c7e.png)

## API
[Pixela](https://pixe.la/)

## Environment Variables
To run this project, you will need to add the following environment variables to your .env file

`PIXELA_TOKEN` `PIXELA_USERNAME` `GRAPH_ID`

Refer to the [env template](https://github.com/sejalabrol/habit-tracker/blob/main/.env.template)

## Run Locally
Clone the project
```bash
  git clone https://github.com/sejalabrol/habit-tracker
```
Go to the project directory
```bash
  cd habit-tracker
```
Create a .env file and enter environment variables
```bash
  cp .env.template .env
```
[Create a virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment) (optional but recommended) 
```bash
  python -m venv venv
  source venv/Scripts/activate
```
Install dependencies
```bash
  pip install -r requirements.txt
```
Run the project
```bash
  python main.py
```
