---
image: /assets/images/hackers-panel.png
title: "project-planning-2"
layout: default
---

<style>
h3 {
    margin-top: 30px
}
pre {
    line-height: 1.5em;
}
pre code {
    font-size: 0.9em;
}
</style>



## Project ideas
If you are still unsure of a project idea here are some project types to 
condider:

- A tool for automating (or making easier) a type of data analysis (command-line).
- A tool for teaching/outreach (e.g., mobile or web app).
- A tool for visualizing a specific type of data (plotting module).
- A new module/extension of an existing library (e.g., toytree.pcm).
- A REST API: make a dataset publicy accessible and begin to build code around it.


### Getting started (planning)
We are at the stage now of beginning to plan our projects. There's no better 
way to get started then to actually do it. You are free to continue to evolve
to your project ideas over the next few weeks, so do not feel concerned if the
idea you come up with today is not fully satisfying. We will have plenty of 
time to think it over, and to get feedback from me and your peers. To get
started:

1. Create a new GitHub repo and *for now* name it **project**, and initialize it with a README.
2. Using markdown create an outline of your project idea in the README file. 
Make a level-3 header section for the following topics and writing a 
desription in each of your current project plans.
	- Description of project goal: (e.g., the program will accomplish goal x.)
	- Description of the code: (e.g., what packages you will use, or classes you will create.)
	- Description of the data: (e.g., it will analyze CSV data input by the user.)
	- Description or demonstration of user interaction: (e.g., see example below.)

See [https://github.com/hackers-test/program](https://github.com/hackers-test/program)
for an example from the class test student.


### Project resources
Over the next few weeks we will continue to explore many third-party Python
libraries in more detail. By exploring the capabilities of these tools you 
may become inspired with new ideas for how you could implement them in your
program. Below I list a few example libraries and ideas for how you could
implement a custom program using these tools:


- [scikit-learn](https://scikit-learn.org/stable/): 
develop a domain-specific machine-learning wrapper. The 
scikit-learn library has great tutorials, and is an expansive toolkit for 
performing statistical analyses. If you have a problem or dataset well 
suited for a particular type of analysis (e.g., PCA) you can create a 
wrapper that takes this data as input, analyses it, and generates nicely 
formatted results. A pipeline basically. (But try to go beyond a single 
simple analysis like a PCA -- how can you generate something really useful?)

- [bokeh](https://docs.bokeh.org/en/latest/index.html): 
bokeh is a javascript-based plotting library (for the web) but 
with a Python syntax. Use it to make an interactive dashboard deployed to 
your website.

- [pymc3](https://docs.pymc.io/): 
Bayesian statistic inference software with many good tutorials. 
It takes a fair bit of studying and testing to develop and fit an appropriate
model. It can be very useful to develop a program that is domain-specific 
(e.g., specialized for a specific data type, like bird songs) and which can
format the data appropriately, define good priors, run the inference, and 
return nicely formatted results.

- [tensorflow](https://www.tensorflow.org/tutorials): 
Powerful machine learning library with many good tutorials. 
Similar examples to the pymc3 description above, but implementing a 
machine learning analysis that you could learn from the tensorflow tutorials.
Here there are many great examples, including interesting topics like
image classification.

- geospatial data analysis: Use [geopandas](https://geopandas.org/), 
[folium](https://python-visualization.github.io/folium/), or 
[google-earth-engine](https://developers.google.com/earth-engine/guides/python_install)
Python API to download, analyze, and visualize data. This should be more 
involved than simple tutorials for plotting points on a map. Develop the tool
for a domain-specific purpose (e.g., extracts bird observation data from 
database x, filters for birds of type y, and analyzes for overlap with 
layers of treecover, temperature, agriculture, etc.). 

- [fastAPI](https://fastapi.tiangolo.com/) 
(or flask): Develop a REST API that makes a large database 
searchable based on its label, metadata, or properties, and accessible and 
from a server address/URL (e.g., https://api.yourname.github.io/bird-data/). 
Your whole community can then access and analyze the data.
This could be species occurrence records (like GBIF), or bird song recordings
searched by date or location, or images of flowers, or data from some 
public database that is currently poorly available that you want to make 
more easily available (if allowed).
You could then also work on an analysis or visualization package for this 
specific type of data.

- [streamlit](https://docs.streamlit.io/en/stable/index.html):
Develop a webapp for visualizing results from interactive toggles that
run embedded Python code.

- [kivy](https://kivy.org/#gallery): 
create a graphical user interface for desktop or mobile app. 
There are a few packages for doing this in Python, but many "front-end"
development (user interactions design) is done in other languages like java
or javascript. But, kivy is a pretty cool app for designing a user interface
in Python that can work on android or osx. Run any Python program and 
display its results nicely, or even design a game.



## Project complexity and planning

Below I list ideas for several projects, ranging from relatively simple to 
very complex. You have 1.5 months from now to complete your programs, and 
for most of the remainder of class we will spend time in class sharing updates
on our programs, discussing them, and contributing to each others programs.
Try to set yourself a reasonable goal, *but* keep in mind also that you do 
need to have a completed project at the end of class. Just a working 
prototype. You can continue to develop it after class.


### Beginner
- Write a Python wrapper around an existing command-line tool that you can call
using `subprocess` such that the program can now be called from Python. 

- Write a conversion tool. It takes as input data of type X (e.g., a PDF) 
and performs some function operations on it and returns as a result some
data of type Y (text extracted and re-formatted from the PDF).


### Intermediate

- Create a pipeline tool that calls several programs using subprocess and
passes the results from one to the next to perform a complex task.

- Create a tool to search a public API (e.g., GBIF) for data based on a 
set of user arguments and perform a domain-specific type of analysis on
these data (e.g., tells you how many mammal species have occurrence records
within a given area.)


### Advanced

- Create a biology-related game/learning app:
	- write functions to perform some biologically relevant operation.
	- develop a mobile phone interface w/ kivy.
	- or as a simple web app using streamlit.

- Develop a domain-specific image analysis tool. 
	- Input is the path to a folder full of image files.
	- Write a class to extract data from images using scikit-image or openCV:
		- object detection (e.g., is a cat or not a cat)
		- edge detection (extract shape, size, density of x from images)
		- quantify interactions (distance between x and y)
		- etc.
	- Statistical analysis of data (pandas, scipy, etc):
		- fit a logistic regression
		- cluster images by similarity in extracted data/features
		- etc.

- Develop a domain-specific statistical analysis tool
	- Input is a CSV or data that can be converted to arrays.
	- Write a class object to fit a model using Bayesian or ML inference according to
	a tutorial in the pymc3 or tensorflow, etc. documentation. 
		- Format input data appropriately.
		- Develop model for domain-specific data.
		- Find reasonable priors for this type of data.
		- Create custom plots and tables of results.

- Develop a simulation tool:
	- Conceive a generative model to produce a type of data.
	- Implement generative data model using e.g., numpy.random with input arguments.
	- Develop an API and/or CLI interface.
	- Show that some inference tool can fit the simulated data to the 
	generative model (correctly infer parameters of the model).


### Assessement
None.  
Visit links to many of the packages above and explore their documentation 
and consider if you might incorporate any of these into your project proposal.
