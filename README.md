# Introducing software development practices and tools for research in the behavioral and social sciences

**Author**: Pablo Caceres  
**Contact**: pcaceres@wisc.edu  

Research in the behavioral and social sciences (B&SS) is **increasingly relying on complex computational procedures**. Nonetheless, researchers in the B&SS usually have **little formal training** in data management and software development strategies for scientific computing. This situation limits researchers ability to produce data processing pipelines that are **reproducible, reusable, reliable, maintainable, extensible, and shareable** with the wider scientific community. Introducing a **set of practices and tools from software development** can significantly help to alleviate this situation and improve the long-term sustainability of research that relies on heavy computation.

In this talk, I provide a **few simple practices and tools** that require relatively **low effort** in exchange of **high impact** on improving researchers computational workflows. I also provide a **minimal example** illustrating the application of this simple principles in a data analysis pipeline.

## Getting started

To obtain the files locally  

```Git
git clone https://github.com/pabloinsente/sf_for_beh_ss.git
```

To run the examples, you'd need python or 3.7 installed in a **Linux/Mac machine**.

For **Windows users**, there are two ways to make the code work:

- Installing [**cygwin**](https://www.cygwin.com/) and running everything from the cygwin console
- Installing the **Ubuntu distribution** in the [Windows subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

Check your python3 installation by typing this in the command line:

```Python
python3 --version
```  

If you have a different python version, go and install [python 3.7](https://www.python.org/downloads/). Look under the *"Looking for a specific release?"* section.

**Pro tip**: managing multiple versions of python may be messy. One solution is to use [pyenv](https://github.com/pyenv/pyenv). Here is an [excellent tutorial](https://realpython.com/intro-to-pyenv/) about installing and using pyenv in multiple OS.

## Usage

 Python scripts and jupyter notebooks are provided in the ```/src``` directory. The step by step instructions are next in this document.

## Tutorial Instructions

### 1.0 Create a simple and well-organized data file system

In the social sciences, it is common to find code repositories where everything is dump into the same directory: data, code, charts, manuscripts, etc. I've done this multiple times in the past and I regret it. There are many ways in which you can organize your projects. We'll generate a repository structure based on a few conventions around software development. We'll use the command line to populate our project.

**Note about the command line**: using the command line may be confusing. It can make you feel like you'd break your computer if you make a typo. You can make your experience better by installing an alternative terminal in your system. Alternative terminals add multiple capabilities like autocomplete, coloring, easy copy-pase, multiple terminals in the same window, and more. Here a few options:

- Linux: [Tilix](https://gnunn1.github.io/tilix-web/)
- MacOS: [iterm2](https://iterm2.com/index.html)
- Windows: [cmder](https://cmder.net//)

**About learning to use the terminal/shell**: learning bash is beyond the scope of this tutorial. There are many good resources out there to learn bash and the command line (see [here](https://github.com/awesome-lists/awesome-bash)), but the trick is just using it as much as you can for your day-to-day tasks (and googling). There a few commands what we will use worth mentioning:

- `cd`: change directory
- `mkdir`: make a directory
- `ls`: list files
- `touch`: create files
- `rm`: remove files
- `rm -r`: remove directories

#### 1.1 Create project directory

We'll start by creating a project directory

```Bash
mkdir my_awesome_project
cd my_awesome_project
```

#### 1.2 Create the repo documentation files

At the root of your project, it's usually expected to see at least three elements:

- **README.md**: this is like the abstract of a paper plus instructions about installation, and usage.
- **requirements.txt**: to indicate the required package dependencies (using pip). More about this later.
- **LICENSE.txt**: to inform potential users about the usability of your code. GitHub provides a guide about how to chose a License [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/licensing-a-repository), and how to add one [here](https://help.github.com/en/github/building-a-strong-community/adding-a-license-to-a-repository)

```Bash
touch README.md requirements.txt
```  

**README.md content**: creating readme files is repetitive. We will use [this website](https://www.makeareadme.com/) as a template to create our content. Once you're done, open the README.md and past the content.

```vscode
code README.md
```

#### 1.3 Create the main folders

It is good idea to separate every element of your project into sub-directories

```Bash
mkdir src data docs results tests
```  

We will add some fillers files to our directories in the meantime

```bash
touch ./src/eda.py ./src/eda.ipynb
touch ./src/stats_example.py ./src/stats_refactor.py stats_helper.py
touch ./src/ml.py ./src/nn.py
touch ./src/__init__.py
touch ./data/fake_data.csv
touch ./docs/code_notes.md
touch ./results/fake_plot.jpg
touch ./tests/test_my_code.py
```

**Note**: GitHub will not upload directories if they are empty. Hence, we created some empty files. More on this later.

### 2.0 Use virtual environments

Virtual environments are a way to isolate the software requirements for your project. In brief, they say: **"use this version of python, and these versions of these packages, and here is where you can find them"**.

Using virtual environments is a good idea because they **avoid interference between the dependencies of multiple projects** living in your system. They also **avoid altering dependencies of your system installation** of python. Finally, they also **facilitate reproducibility** of your projects by specifying the environment in which your code was run.

**Note about environments and dependencies**: other programming languages like R, Julia, etc., have their own solutions for environment isolation and dependency managment. Today's examples are based on python. If you need to use multiple programming languages, the best solution is to use Docker containers, in which you can "package" your whole software system: code, runtime, system tools, system libraries and settings, to be reproduced in another machine. Docker is beyond the scope of this tutorial. You can learn more [here](https://www.docker.com/resources/what-container), [here](https://www.youtube.com/watch?v=Q2u1wcfmlzw), and [here](https://www.youtube.com/watch?v=gBalsA-x300).

There are multiple options to create virtual environments in python. We'll use [**venv**](https://docs.python.org/3/library/venv.html) because of its simplicity and comes by default in python 3.

#### 2.1 Create virtual environment

Inside your project directory type

```Python
python3 -m venv venv
```

**Note**: if you're not sure where in your file system is your terminal, type 

```terminal
pwd
```

#### 2.2 Activate virtual environment

Creating your venv is the first step. To actually use it, you need to active it by running:

```Python
source venv/bin/activate
```

#### 2.3 Verify venv activation

As a sanity check:

```Python
which python
```

The output should point to your current directory. It should look similar to:

```Bash
/home/yourname/Desktop/my_awesome_project/venv/bin/python
```

As long as your venv is active, python will go to that directory to search for dependencies, and pip will install dependencies in there as well.

#### 2.4 Check installed packages

```Python
pip list
```  

The output should look similar to this (Version may vary):

| Package    | Version |
|------------|---------|
| pip        | 19.2.3  |
| setuptools | 41.2.0  |

If you see more packages, your pip installation it is not pointing to the `/venv` directory. Did you remmember to activate the environment?

Once we have the venv **activated** (this is easy to forget), we can safely install dependecies using pip.

#### 2.5 Installing packages

One way to install packages is to simply type `pip name-package`. A better way, is to specify the package name and version in the **requirements.txt** file. Open the file in vscode by typing `code requirements.txt`, and copy-paste:

```Python
altair==3.3.0
jupyterlab==1.2.4
numpy==1.17.4
pandas==0.25.3
scikit-learn==0.21.3
scipy==1.3.3
statsmodels==0.10.2
tensorflow==2.0.0
wandb==0.8.20
watermark==2.0.2
```

Before installing dependencies, check the pip version by

```bash
pip --version
```

If you see a version older than `19.2.3`, go an upgrade with

```bash
pip install --upgrade pip
```

Now you're ready to install the dependencies by running:

```Python
pip install -r requirements.txt
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

The main advantage of the requirements.txt file is that **allows other people to reproduce your dependencies**

### 3.0 Use version control systems

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

You may need to use version control. There are many version control systems around (Subversion, Mercurial, etc), but Git is the most popular by far.

**What is Git**: Git is the actual version control software managing, tracking, and logging your code in your machine. Git is commonly used along with GitHub as hosting service.

**What is GitHub**: GitHub is a hosting service for Git. Basically, it allows to save everything related to your project in the cloud instead of your own machine.

Learning git may take a while. Fortunatelly, there are relative few commands needed to track your project effectively. The rest can be googled as needed.

#### 3.1 Check git installation

```git
git --version
```

If you need to install Git, got to [this link](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and follow installation instructions for your system

#### 3.2 Check the git status

Run this in the root of your project directory

```git
git status
```

The output should look like this:

```console
fatal: not a git repository (or any parent up to mount point /)
```

This is fine. This means that Git has not initiated tracking in that directory.

#### 3.3 Initialize git tracking

```git
git init
```

This creates an empty Git repository or reinitialize an existing one. You will not see the repository because it is a .git directory (directories starting with a "." are hidden)

To confirm the initialization type

```git
git status
```

It should say something like this:

```git
On branch master

No commits yet
...
```

#### 3.4 Create .gitignore file

```git
touch .gitignore
```

The .gitignore file tells to git: **"DON'T track this files"**. Whatever you put in there, would not appear in GitHub later.

**Populating .gitignore**: adding files to be ignored to .gitignore may be repetitive. We'll use [this webpage](https://www.gitignore.io/) to automatically generate .gitignore files based on the dependencies we're using. Once in the page, ask for `python`, `jupyter`, and `venv` in the search bar.

#### 3.5 Add files to local repository

```git
git add -A
```

This stages the files to be committed. This is how we tell git: "prepare this files to be commited". The '-A' in this case stands for "all changes"

#### 3.6 Commit files

```git
git commit -m "First commit"
```

Commit prepares the added files to be pushed to the remote repository. This is how we tell git: **"save this changes locally, I'll send them to GitHub later"**. The "-m" flag (shor for --message) add a commentary to your commit. This is useful to record what changes you made to your code.

#### 3.7 Creating a remote repository

In order to push our files to our remote repository, we need to create one in the first place.

Go to [https://github.com/](https://github.com/) and create a new **empty repository** (don't add README). Then copy the remote repository URL

#### 3.8 Connect with the remote repository

To connect our local repository with our remote one, run this replacing **GITHUB_URL** with your remote URL

```git
git remote add origin remote repository GITHUB_URL
```

#### 3.9 Check new remote

```git
git remote -v
```

The output should look like:

```console
origin https://github.com/pabloinsente/sf_for_beh_ss.git (fetch)
origin https://github.com/pabloinsente/sf_for_beh_ss.git (push)
```

#### 3.10 Push local changes to remote repository

Now we are ready to push our changes to GitHub (our remote bucket for git and our code)

```git
git push origin master
```

This should prompt you enter your `username` and `password`.

**Note about connecting to GitHub**: If you push and fetch a lot, you may want to avoid typing your username and password every time by connecting to GitHub with SSH. [Here](https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh) is a GitHub guide about how to configure that.

If you go to your GitHub repo, you should see the added changes.

### 4.0 Example 1: Writing a basic reproducible script

We have accomplished three things:

1. A project structure
2. An isolated virtual environment to manage our dependencies
3. A version control system to track our progress

Now we need some **code that processes data in automated and reproducible fashion**. We will walk through the `eda.ipynb` and `stats_example.py` files to see an example of how this may work. You just need to copy-past them from the workshop repo `sf_for_beh_ss/src` into your own `my_awesome_project/src` directory. Remember also to copy-paste the `mental_health_tech_data.csv` from `sf_for_beh_ss/data` to your `my_awesome_project/data`

#### 4.1 Jupter Notebook (`eda.ipynb`) instructions

From the root of your repository run

```bash
cd src
jupyter lab eda.ipynb
```

This should open Jupyter Lab. Further instructions in the noteook

#### 4.2 Stats Example (`stats_example.py`)

From the root of your repository run

```bash
cd src
code stats_example.py stats_refactor.py stats_helper.py
```

Further instructions will be given in the workshop. Once you're done, run

```bash
stats_refactor.py # to print to the console
python stats_refactor.py > ../results/chi2.txt # to print to a .txt file
```

Now, you have a data analysis script that is:

- **reusable**: you can use parts of your code for further analysis and/or projects
- **maintainable**: easy to fix
- **extensible**: easy to add extra functionality
- **shareable**: others can clone my repo and run your script easily

### 5. Example 2: Set up machine learning experiment tracking

Machine learning usually entails many rounds of iterating over different hyper-parameters, architechtures, data partitions, etc. This makes really hard to keep track of your experiments and metrics over time, which may hinder reproducibility. Several tools has been created recentrly to tackle this issue. In this case, we will use [Weight & Biases](https://www.wandb.com/) to showcase a very simple example of how this might work.

#### 5.1 To install Weight and Biases

This should be installed already (if you pip installed the requirements.txt). Otherwise, it can be installed by

```Python
pip install wandb
```

#### 5.2 To sing up or login to an existing account

```Python
wandb login
```

This should prompt you to Log in. If you don't have an account, create one and Log in. Follow the instructions and past the key to the command line. If you did this right, you should see a `Successfully logged in to Weights & Biases!` message.

Since we don't have time to write a ML pipeline, we will use scripts provided in the `/src` folder of the workshop repo, and add some code to those scripts to make things work. Again, copy and paste `ml.py` and `nn.py` from `sf_for_beh_ss/src` into your own `my_awesome_project/src`. Then open the files in vscode.

```vscode
code ml.py nn.py
```

#### 5.3 Tracking configuration and metrics

Tracking configuration and metrics with wandb is done in 4 steps:

```Python
# Step 1: import wandb
import wandb

# Step 2: initialize wandb project tracking
wandb.init(project='my-awesome-project')

# Step 3: add tracking configuration
config = wandb.config # Config is a variable that holds and saves hyperparameters and inputs
config.epochs = 100
config.dropout = 0.2
...

# Step 4: tell wandb to log the config and matrrics
# For instance, at the end of a Keras model:
# fit the model
model.fit(X_train_transform,
          y_train,
          epochs=config.epochs,
          validation_data=(X_test_transform, y_test),
          callbacks=[WandbCallback()])
```

Weight & Biases support multiple python frameworks: Scikit-learn, Tensorflow, Keras, Pytorch, Fast.ai, and XGBoost. Each framework follows the same steps with minimal variations. See the [documentation](https://docs.wandb.com/library/frameworks) to learn more about this.

#### 5.4 Run the examples

To run the scikit-learn example

```Python
python ml.py
```

To run the keras example

```Python
python nn.py
```

If the scripts run successfully, wandb will generate a url where you can see the project data and metrics online.

### 6.0 Testing your code

Code testing is an uncommon, yet very important part of writing software for scientific computing in a reliable and reprodicible fashion. There are multiple frameworks in the python ecosystem for this. We will use `pytest`, because its simplicity and popularity.

#### 6.1 To install pytest run

This should be installed already (if you pip installed the requirements.txt). Otherwise, it can be installed by

```bash
pip install pytest
```

#### 6.2 Check pytest installation

```bash
pytest --version
```

Again, you just need to copy-paste the `test_my_code.py` file from `sf_for_beh_ss/tests` into your own `my_awesome_project/tests`

`pytest` works by searching for files that have **test_something.py** or **something_test.py** (note the **test** keyword), and running any function or method beginning with **test**

To run the unit test

```bash
cd /tests
pytest
```

The pytest output should output something like

```console
=========1 passed in 0.51s=========
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
