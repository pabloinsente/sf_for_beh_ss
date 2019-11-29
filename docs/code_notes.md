## Create simple and well-organized data file system (or "code base")

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

## Use virtual environments
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
pip freeze > requirements.txt```
- To deactivate the environment:
```
deactivate
```

- If you want to delete the environment run
```
rm -rf env/
```

## Use version control systems
- Check git installation:
```
git --version
```
- If you need to install git, got to [this link](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)and follow installation instructions for your system
- Then, inside your project directory, check the git status:
```
git status```
- Initialize git repository and tracking:
````
git init
```
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
- Add the URL for the remore repository to your local repository:
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
## Eight simple principles to write better code
