### X. Create simple and well-organized data file system (or "code base")

mkdir sf_for_beh_ss
touch README.md requirements.txt LICENSE.txt
mkdir code data docs results  

### X. Use virtual environments
python --version
virtualenv --version
virtualenv sf_for_beh_ss_env
source sf_for_beh_env/bin/activate
pip list
pip install numpy pandas scikit-learn matplotlib
