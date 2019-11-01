### X. Create simple and well-organized data file system (or "code base")

mkdir sf_for_beh_ss  
touch README.md requirements.txt LICENSE.txt  
mkdir code data docs results  
touch ./code/cool_script.ipynb ./code/helper_script.py
touch ./docs/brilliant-manuscript.pdf
touch ./results/fake-plot.jpg

### X. Use virtual environments
python --version
virtualenv --version
virtualenv sf_for_beh_ss_env
source sf_for_beh_env/bin/activate
pip list
pip install numpy pandas scikit-learn matplotlib

### X. Use version control systems
git status
git init
git add .
git commit -m "First commit"
git remote add origin remote repository URL# Sets the new remote
git remote -v
git push origin master

### X. Eight simple principles to write better code
