---
sidebar_position: 1
---
# Best Practices for Collaborative Python Development 
<hr></hr>

## Develop in a Virtual Environment

Using a virtual environment in Python is simple and ensures that there won't be any conflicts between a previously installed version of a library and that which you are running. It functionally allows you to pretend that you're running a clean Python3 installation with just the packages you need in that particular instance.
Furthermore, It also provides the advantage that you can provide a `requirements.txt` file, which gives an easy method to share the necessary file versions that work together and solves a great proportion of "It works on my machine issues"

Another consideration I would recommend is the use of [`pyenv`](https://github.com/pyenv/pyenv/tree/master) ([windows version here](https://github.com/pyenv-win/pyenv-win)). This is a tool that grants you the ability to swap in python versions / interpreters in the same way we might swap around versions of python libraries. If a tool is running on a specific old version of python3 and is broken in new versions, it is worth considering using this to manage it. Especially with the quality of life features provided by being able to to set specific versions to specific folders / projects. 

The temptation may exist to download this via PIP (or whatever package manager) but I can't stress what a bootstrapping nightmare it is to have a package manager tied to a python version in charge of a python version manager and so on. do yourself a favour and keep pyenv as the overseer of its python versions. 
Same is especially true as conda does provide similiar functionality in that you can configure venvs with particular python versions, but again, bootstrapping hell

With that out of the way, let's examine Virtual environments:

## 1. PIP

> Do you install your packages by running `pip install {packagename}`?  
> Read this bit 

First things first, we want to ensure that python is in your shell's path. to do so simply open a terminal and type:  
`python`  
If this results in output that shows the current python version and and interpreter (denoted by the `>>>` prompt ) you should be good to go.  
If not, ask an LLM chatbot to walk you through it with your particular OS / terminal info. 

### Creating a venv:
In your terminal navigate to the folder your project (or projects if they're related and going to share packages) is located and type  
`python -m venv .venv`

This tells python to use the venv module to create a folder named `.venv` that contains the python bin info and will be where all of your installed libraries are contained. You can technically name it whatever you like, but in this case its convention, and .venv is already included in the gitignore. 
Since our collaborators probably wont be using the exact same python binary, we dont want to force them to download personalized junk. What we do want to do, is to provide them with a list of things they need to make our application / jupyter notebook to work like it does on our machine. 

### Entering a venv:
If you've just create the venv from above, you can activate it by typing:

1. UNIX (MAC / Linux)
    1. Bash / zsh: `source .venv/bin/activate`
    2. fish: `source .venv/bin/activate.fsh`
    3. csh/tcsh: `source .venv/bin/activate.csh`
2. Windows: 
    1. Powershell: `.venv\Scripts\Activate.ps1`
    2. cmd (in current year?): `.venv\Scripts\Activate.bat`

You'll know it was a success if in your terminal it shows up with (.venv) before the prompt.

### Logging your packages:
Now download all your packages and when you've got everything your jupyter notebook or python script requires, run   
`pip freeze > requirements.txt`  
This will output all of the packages in this venv and write them to a file named `requirements.txt`

### Installing someone elses venv
Then, all anyone needs to do to get a working build of your code on their machine, should be to download the repo, navigate to the project folder, make their own venv and run:
`pip install -r requirements.txt`
or failing that:
`python -m pip install -r requirements.txt`



## 2. Conda
> Do you install your packages by running `Conda install {packagename}`?  
> or just downloaded Anaconda for a unit ages ago and have everything already?  
> Read this bit 

Assuming you ran the anaconda installer with default settings, conda should be on your system's PATH.
This can be tested by opening a terminal and running `conda`.

You should get some version info. if you get a file not found error, ask an LLM chatbot to walk you through it with your particular OS / terminal info.

### Creating a venv:

In your terminal navigate to the folder your project (or projects if they're related and going to share packages) is located and type  
`conda create -n .venv`

This will create a hidden folder in that directory named `.venv` that contains the python and conda bin info and will be where all of your installed libraries are contained.  You can technically name it whatever you like, but in this case its convention, and .venv is already included in the gitignore. 

You can also specify python version by appending the `version=x.x` as well as initialize the venv with any packages you know you'll want by appending the package names to the end of the command

Since our collaborators probably wont be using the exact same python binary, we dont want to force them to download personalized junk. What we do want to do, is to provide them with a list of things they need to make our application / jupyter notebook to work like it does on our machine. 

### Logging your packages:
Now download all your packages and when you've got everything your jupyter notebook or python script requires, run   
`conda list -e > requirements.txt`  
This will output all of the packages in this venv and write them to a file named `requirements.txt`

### Installing someone elses venv
Then, all anyone needs to do to get a working build of your code on their machine, should be to download the repo, navigate to the project folder, make their own venv and run:
`conda create -n .venv --file requirements.txt`


:::info
**Document Creation:** 5 September 2024. **Last Edited:** 5 September 2024. **Authors:** Lachlan Costigan
:::

