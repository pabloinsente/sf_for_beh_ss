# Introducing software development best practices for research in the behavioral and social sciences

**Author**: Pablo Caceres  
**Contact**: pcaceres@wisc.edu  

Research in the behavioral and social sciences (B&SS) is **increasingly relying on complex computational procedures**. Nonetheless, researchers in the B&SS usually have **little formal training** in data management and software development strategies for scientific computing. This situation limits researchers ability to produce data processing pipelines that are **reproducible, reusable, reliable, maintainable, extensible, and shareable** with the wider scientific community. Introducing a **set of simple strategies and techniques in data management and software development** can significantly help to alleviate this situation and improve the long-term sustainability of research that relies on heavy computation.

In this talk, I provide a **few simple strategies and techniques** that require relatively **low effort** in exchange of **high impact** on improving researchers computational workflows. I also provide a **minimal example** illustrating the application of this simple principles in a data analysis pipeline.

# Getting started

To obtain the files locally  

```Git
git clone https://github.com/pabloinsente/sf_for_beh_ss.git
```

To run the examples, you'd need python >= 3.6.X installed in a **Linux/Mac machine**.

For **Windows users**, there are two ways to make the code work:

- Installing [**cygwin**](https://www.cygwin.com/) and running everything from the cygwin console
- Installing the **Ubuntu distribution** in the [Windows subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

Check your python3 installation by typing this in the command line:

```Python
python3 --version
```  

If you have python version <=3.5, go and install a [newer version](https://www.python.org/downloads/).


**Pro tip**: managing multiple versions of python may be messy. One way of managing this properly, is to use [pyenv](https://github.com/pyenv/pyenv). Here is an [excellent tutorial](https://realpython.com/intro-to-pyenv/) about installing and using pyenv in multiple OS.

# Usage

The slides are provided in the ```/docs``` directory. Python scripts and jupyter notebooks are provided in the ```/code``` directory. The step by step instructions are next in this document.

# Tutorial Instructions

## 1. Create a simple and well-organized data file system

In the social sciences, it is common to find code repositories where everything is dump into the same directory: data, code, charts, manuscripts, etc. I've done this multiple times in the past and I regret it. There are many ways in which you can organize your projects. We will generate repository structure based on common conventions around software development. We'll use the command line to populate our project.

**Pro tip**: using the command line may be confusing and unpleasant for some people. You can make your experience better by installing a different terminal in your system. Alternative terminals add multiple capabilities like autocomplete, coloring, easy copy-pase, multiple terminals in the same window, and more. Here a few options:

- Linux: [Tilix](https://gnunn1.github.io/tilix-web/)
- MacOS: [iterm2](https://iterm2.com/index.html)
- Windows: [cmder](https://cmder.net//)

**About learning to use the terminal/shell**: learning bash is beyond the scope of this tutorial. There are many good resources out there to learn bash and the command line (see [here](https://github.com/awesome-lists/awesome-bash)), but the trick is just using it as much as you can for your day-to-day tasks (ang googling alot). There a few commands what we will use a lot worth mentioning:

- `cd`: change directory
- `mkdir`: make a directory
- `ls`: list files
- `touch`: create files
- `rm`: remove files and directories

### 1.1 Create project directory

We'll start by creating a project directory

```Bash
mkdir my_awesome_project
cd my_awesome_project
```

### 1.2 Create the repo documentation files

At the root of your project, it's usually expected to have at least three elements:

- **README.MD**: this is like the abstract of a paper plus instructions about usage
- **requirements.txt**: to indicate the required package dependencies. More about this later.
- **LICENSE.txt**: to inform potential users about the usability of your code.  

```Bash
touch README.md requirements.txt LICENSE.txt
```  

### 1.3 Create the main folders

It is good idea to separate every element of your project into distinc sub-directories

```Bash
mkdir src data docs results tests
```  

We will add some fillers files in the meantime:

```bash
touch ./src/eda.py ./src/stats.py
touch ./src/ml.py ./src/nn.py
touch .src/eda.ipynb .src/helper.py
touch ./data/fake_data.csv
touch ./docs/code_notes.md
touch ./results/fake_plot.jpg
touch ./tests/test_my_code.py
```

**Note**: GitHub will not upload directories if they are empty. Hence, we created some empty files. More on this later.

## 2. Use virtual environments

Virtual environments are a way to isolate the software requirements for your project. In brief, they say: **"use this version of python, and these versions of these packages, and here is where you can find them"**.

Using virtual environments is a good idea because they **avoid interference between the dependencies of multiple projects** living in your system. They also **avoid altering dependencies of your system installation** of python. Finally, they also **facilitate reproducibility** of your projects by locking them to specific packages versions.

There are multiple options to create virtual environments in python. We will use [**venv**](https://docs.python.org/3/library/venv.html) because of its simplicity and comes by default in python 3.

### 2.1 Create virtual environment

```Python
python3 -m venv venv
```

### 2.2 Activate virtual environment

```Python
source venv/bin/activate
```

### 2.3 Verify venv activation

```Python
which python
```

The output should point to your current directory. It should look similar to:

```Bash
/home/yourname/Desktop/my_awesome_project/venv/bin/python
```

As long as your venv is active, python will go to that directory to search for dependencies 

### 2.4 Check current packages

```Python
pip3 list
```  

The output should look similar to this:

| Package    | Version |
|------------|---------|
| pip        | 19.2.3  |
| setuptools | 41.2.0  |

If you see more packages, your pip3 installation it is not pointing to the venv directory.

Once we have the venv **activated** (this is easy to forget), we can safely install dependecies using pip3.

### 2.5 Installing packages

One way to install packages is to simply type `pip3 name-package`. A better way, is to specify the package name and version in the **requirements.txt** file. Open the file in vscode by typing `code requirements.txt`, and copy-paste:

```Python
altair==3.3.0
jupyterlab==1.2.4
numpy==1.17.4
pandas==0.25.3
scikit-learn==0.21.3
scipy==1.3.3
statsmodels==0.10.2
tensorflow==2.0.0
wandb==0.8.19
```

Save the file and install the dependencies by running:

```Python
pip install - r requirements.txt
```

You can check the installation by:

```Python
pip list
```

To **deactivate** the environment

```Python
deactivate
```

Or simply close your terminal

If you want to **delete the environment** run

```Bash
rm -rf venv/
```

## 3. Use version control systems

Version control systems are tools for **managing and tracking code changes over time in a semi-automated manner**. If you have ever created something like:

```Python
my_analysis_script.py
my_analysis_script_final.py
my_analysis_script_final_FINAL.py
my_analysis_script_final_FINAL_FOR_REAL.py
my_analysis_script_2.py
my_analysis_script_2_this_is_the_last_one.py
...
```

You may need to use version control. There are many version control systems around, but git and GitHub are the more popular ones.

**What is git**: git is the actual version control software managing, tracking, and logging your code in your machine. Technically, it can be used locally in your machine.

**What is GitHub**: GitHub is a hosting service for git. Basically, it allows to save everything related to your project in the cloud instead of your own machine. It is so well integrated with git, that are easy to confuse.

Learning git may take a while. Fortunatelly, there are relative few commands needed to track your project effectively with git. The rest can be googled. Chances are that someone else ran into the same problem.


### 3.1 Check git installation

```git
git --version
```

If you need to install git, got to [this link](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and follow installation instructions for your system

### 3.2 Check the git status

Run this in the root of your project directory

```git
git status
```

### 3.3 Initialize git tracking

```git
git init
```

### 3.4 Create .gitignore file

```git
touch .gitignore
```

The .gitignore file tells to git: **"DON'T track this files, please"**. Whatever you put in there, would not appear in GitHub later.

**Pro tip**: adding exceptions to .gitignore may be repetitive. You can use [this webpage](https://www.gitignore.io/) to automatically generate .gitignore files based on the software you are using.

### 3.5 Add files to local repository

This stages the files to be committed. This is how we tell git: "prepare this files to be commited". The '-A' in this case stands for "all changes"

```git
git add -A
```

### 3.6 Commit files

Commit prepares the added files to be pushed to the remote repository
This is how we tell git: "save this changes to send them to GitHub later"

```git
git commit -m "First commit"
```

### 3.7 Creating a remote repository

In order to push our files to our remote repository, we need to create one in the first place.

Go to [https://github.com/](https://github.com/) and create a new **empty repository** (don't add README). Then copy the remote repository URL

### 3.8 Connect with the remote repository

To connect our local repository with our remote one, run this replacing **GITHUB_URL** with your remote URL

```git
git remote add origin remote repository GITHUB_URL
```

### 3.9 Check new remote

```git
git remote -v
```

### 3.10 Push local changes to remote repository

Now we are ready to push our changes into GitHub (our remote bucket for git and our code)

```git
git push origin master
```

If you go to your GitHub repo, you will the see the added changes.

## 4. Example 1: Writing a basic reproducible script

We have accomplished three things:

- A project structure
- An isolated virtual environment to manage our dependencies
- A version control system to track our progress

Now we need some code that processes data in automated and reproducible fashion. We will walk through the `eda.ipynb` and `stats.py` files to see an example of how this may work. You just need to copy-past them from the workshp repo into your own `/src` directory.

## 5. Example 2: Set up machine learning experiment tracking

Machine learning usually entails many rounds of iterating over different hyper-parameters, architechtures, data partitions, etc. This makes really hard to keep track of your experiments and metrics over time, which may hinder reproducibility. Several tools has been created recentrly to tackle this issue. In this case, we will use [Weight & Biases](https://www.wandb.com/) to showcase a very simple example of how this might work.

### 5.1 To install Weight and Biases

```Python
pip install wandb
```

### 5.2 To sing up or login to an existing account

```Python
wandb login
```

This should prompt you to create a new account if you don't have one already. Otherwise, it will ask you to login. Follow the instructions and past the API key to the console and you are ready to roll.

Since we don't have time to write a ML pipeline, we will use scripts provided in the `/src` folder of the workshop repo, and add some code to those scripts to make things work. This files can be found in the `/src` directory.

Further instructions about this section are provided in the `ml.py` and `nn.py` scripts. This files can be found in the `/src` directory. You just need to copy-past them into your own `/src` directory.

## 6.0 Testing your code

Code testing is an uncommon, yet very important part of writing software for scientific computing in a reliable and reprodicible fashion. There are multiple framewokrs in the python ecosystem for this. We will use `pytest`, because its simplicity and popularity.

### 6.1 To install pytest run

```Python
pip install pytest
```

### 6.2 Check pytest installation

```Python
pytest --version
```

Again, you just need to copy-paste the `test_my_code.py` file into the `\tests` directory of your project.

`pytest` works by searching for files that have **test_something.py** or **something_test.py** (note the **test** keyword), and running any function or method beginning with **test**

To run the unit test go to the `test\` directory and run

```Python
pytest
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
