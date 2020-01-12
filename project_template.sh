# make a directory to host your project
mkdir my_awesome_project
# navigate into your project directory
cd my_awesome_project
# add documentation
touch README.md requirements.txt
# make directories
mkdir src data docs results tests
# file fillers
touch ./src/eda.py ./src/eda.ipynb
touch ./src/stats_example.py ./src/stats_refactor.py stats_helper.py
touch ./src/ml.py ./src/nn.py
touch ./src/__init__.py
touch ./data/fake_data.csv
touch ./docs/code_notes.md
touch ./results/fake_plot.jpg
touch ./tests/test_my_code.py

# create virtual environment
python3 -m venv venv
# activate venv
source venv/bin/activate
# upgrade pip
pip install --upgrade pip
# install requirements
pip install -r requirements.txt



