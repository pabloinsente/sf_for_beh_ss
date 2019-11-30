# Introducing software development best practices for the behavioral and social sciences

**Author**: Pablo Caceres  
**Contact**: pcaceres@wisc.edu  

Research in the behavioral and social sciences (B&SS) is **increasingly relying on complex computational procedures**. Nonetheless, researchers in the B&SS usually have **little formal training** in data management and software development best practices for scientific computing. This situation limits researchers ability to produce data processing pipelines that are **reproducible, reusable, reliable, maintainable, extensible, and shareable** with the wider scientific community. Introducing a **set of simple principles in data management and software development** may significantly help to alleviate this situation and improve the long-term sustainability of research in the social sciences that relies on heavy computation.


In this talk I provide a **few simple principles** that require relatively **low effort** in exchange of **high impact** on improving researchers computational workflows. I also provide a **minimal example** illustrating the application of this simple principles in a data analysis pipeline.

## Getting started

To obtain the files locally:  
```
git clone https://github.com/pabloinsente/sf_for_beh_ss.git
```

To set up your system to run the examples, you need python 3.6.X installed in a Linux/Mac machine. Then install dependencies by running:

```
cd sf_for_beh_ss
pip install -r requirements.txt
```

## Usage

The slides are provided in the ```/docs``` directory. Python scripts and jupyter notebooks are provided in the ```/code``` directory

## Turorial Instructions:

### Create simple and well-organized data file system

- Create project directory:
```
mkdir my_awesome_project
cd my_awesome_project
```
- Create repo documentation files:
```
touch README.md requirements.txt LICENSE.txt
```  
- Create main folders:
```
mkdir code data docs results
```  
- Create scripts fillers:
```
touch ./code/cool_script.ipynb
touch ./code/helper_script.py
```
- Create file fillers:
```
touch ./docs/brilliant-manuscript.pdf
touch ./results/fake-plot.png
```

### Use virtual environments
- Check python installation and version:
```
python --version
```
- We need Python 3.6 installed. If you don't have it, go to [this link](https://www.python.org/downloads/) and look for version 3.6.9 and follow the installation instructions.
- Create virtual environment:
```
python3 -m venv env
```
- Activate virtual environment:
```
source env/bin/activate
```
- Chec venv creation:
```
which python
```
- Check current packages:
```
pip3 list
```  
- Install some packages:
```
pip3 install numpy pandas altair jupyterlab watermark scikit-learn
```
- Create requirements file with current dependencies:
```
pip freeze > requirements.txt
```
- To deactivate the environment:
```
deactivate
```
- If you want to delete the environment run
```
rm -rf env/
```

### Use version control systems
- Check git installation:
```
git --version
```
- If you need to install git, got to [this link](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)and follow installation instructions for your system
- Then, inside your project directory, check the git status:
```
git status
```
- Initialize git repository and tracking:
```
git init
````
- Create and add .gitignore file
```
touch .gitignore
```
- Add files to local repository. This stages the files to be committed:
```
git add .
```
- Commit staged files and prepares them to be pushed to the remote repository:
```
git commit -m "First commit"
```
- Go to [https://github.com/](https://github.com/) and create a new empty repository with the same name as your local repository. Then copy the remote repository URL
- Add the URL for the remote repository to your local repository:
```
git remote add origin remote repository GITHUB_URL#
```
- Check new remote:
```
git remote -v
```
- Push local changes to remote repository
```
git push origin master
```

### Set up machine learning experiment tracking
- To install Weight and Biases:
```
pip install wandb
```
- To sing up or login to an existing account:
```
wandb login
```
- Past the API key to the console and you are ready to roll
- Further wandb configuration is explained in the scripts

## License
[MIT](https://choosealicense.com/licenses/mit/)
