# ML web app with Streamlit example: decision tree classifier diabetes prediction

## Introduction

This repository contains the minimum requirements to get a web application up and running using the model trained in one of our prior projects. The model deployed will be the diabetes prediction decision tree classifier. I have set-up much of the nit-picky configuration for you, but it is up to you to build the heart of the app and get it deployed to Render.

The project consists of three main parts:

1. **Model inference function**: This portion takes data from users and sends it to the model for prediction. It then sends back the prediction.
2. **Streamlit**: Streamlit is a framework to build and run web applications in python.
4. **Render**: Render is the cloud hosting service we will use to actually run our application. This allows us to have a public URL where the application can be accessed.

## Render set-up

Once you have your app running in a codespace with no errors, it is time to deploy to Render. Go to [render.com](https://render.com/) and click 'Get started for free'. The site will ask for an email address and password and then send you a conformation link. After clicking the link, you are asked to fill out some basic profile details and finally taken to the 'service type' page on the Render Dashboard page.

1. Choose 'New web service' from the service type dashboard tab.
2. On the Configure tab, select 'Public Git Repository' and past the link to your project repo.
3. Click 'Connect'

Add the following settings:

1. Name: whatever you want
2. Project: don't need to add to a project for minimal deployment
3. Language: Python 3
4. Branch: main
5. Region: Ohio (US east)
6. Root directory: src
7. pip install -r ../requirements.txt
8. gunicorn app:app

Only real gotcha here is the root directory - setting it to src means that Render will run all commands from there. This is what we want since our app lives in src. But since the requirements file is in the project home (i.e. one directory above src) we need to make sure we get the path right while pip installing.

After that set the instance type to free, and you can leave everything else alone. Click 'Deploy Web Service'! You should see the requirements.txt being installed in the log terminal and then gunicorn starting. If there were no problems, you can now access your web app at the URL provided at the top of the page, under the project name and GitHub repo link.
