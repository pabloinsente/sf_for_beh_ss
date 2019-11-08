# Introducing software development best practices for the behavioral and social sciences

## Keep in mind:

- I'm not a software engineer and I don't have a CS degree
- This is not about the best way of writing code
- This is not about the best programming language for the B&SS
- This is not about the best statistical procedures or machine learning approaches
- This is not about deploying data pipelines in production systems
- This is about what I believe are good software engineering practices for scientific computing in the B&SS  
- This is more useful for projects that do not require large scale computing (HTC, HPC, Hadoop, Spark, cloud computing, etc.). Roughly ~10 to 1 million of rows.
- This is about simple architectural principles that allow creating data projects which are:
  - Reproducible
  - Reusable
  - Reliable
  - Maintainable
  - Scalable
  - Shareable
- I'm coming from my personal experience analyzing data and writing code for research in sociology, public policy/economics, cognitive neuroscience and psychology in the past ~8 years (since ~2011):
  - SPSS and Excel for 4 years
  - STATA and MATLAB for 2 years
  - Python and R for 2.5 years

## Recommended best practices

### X. Use free and open-source software (FOSS)
- Python, R, Scala, SQL, Julia, Bash, etc. instead of SPSS, STATA, MATLAB, SAS, etc.
- Otherwise, reproducibility, reusability, and shareability, are not possible
- Far more people use FOSS than proprietary software
- Proprietary software is not accessible in lower income countries
- FOSS is the present AND the future of data science ecosystems
All new statistics and machine learning are created in FOSS


### X. Create simple and well-organized data file system ("code base")
- Separate code from data and results
- Add a README.md file
- Add a LICENSE .txt
- Add a requirements.txt file
- For instance:

```
|--\my_awesome_project
|  |README.md
|  |LICENSE.txt
|  |requirements.txt
|  |--\code
|  |  |--cool-script.py
|  |  |--helper-script.py
|  |--\data
|  |  |--fantastic-data.csv
|  |  |--fantastic-data_schema.csv
|  |--\docs
|  |  |--brilliant-manuscript.pdf
|  |--\results
|  |  |--fig-1.tiff
|  |  |--fig-2.tiff
|  |  |--table-1.tiff
|  |  |--table-2.tiff
```

### X. Use virtual environments
- Virtual environments create an isolated environment for your project
- For Python virtualenv or conda environment
- For R conda environment

### X. Use version control systems
- Git, Mercurial, or SVN
- Push changes frequently
- Use branches for experimentation
- Use a third backup (safe) backup system with continuous sync (Box, Dropbox, Drive, Mega, etc.)
- Optimized for plain text. Not that good for tabular data, docx, or PDFs.
- Bad for "large" files (limited to 100 megabytes per file in GitHub).
- If files are too large: zip the files (OK solution). Read data from the web (Better solution)
- Raw should not change, and therefore, should not require version tracking
- Keep minimal notes/log of major changes

### X. Add and maintain documentation
- README.md
- LICENSE.txt
- requirements.txt
- to-do.txt
-Push frequently to maintain snapshots of your projects at different timepoints

### X. Maintain your raw-data (single authoritative version of your data)

- Readable and consistent naming
- Use unique and consistent identifiers
- Add dates
- Keep a data schema / metadata
- Keep multiple copies of the file
- When possible, avoid saving multiple versions of the data, let the computer automate  building clean data on the fly* / Some (cite) prefer to create intermediate data products. I don't like it, because they incentive to skip previous steps (i.e., not-rerun and test) in the script. For instance, if you change a dependency (upgrade a library to a newer version) part of your pipeline may go untested. BUT, if you are working with very large files and doing way to many pre-processing you may consider to use a different approach.
- Use open non-proprietary formats (CSV, JSON, XML etc)

### X. Use well-tested and properly supported software libraries

- Review what are the most popular libraries in your field
- When possible, resist using tools that other people in your group uses just for the sake of group conformity
- Popular libraries:
  - Thoroughly tested (less bugs),
  - Optimized for performance
  - Are safer,
  - Better documentation
  - Better on-line support (i.e., Stack Overflow)
  - Better and tutorials
  - Are more likely to be maintained long-term
- Python: pandas, numpy, scikit-learn, matplotlib, seaborn, Tensorflow, Keras, Pythorch, XGBoost, statsmodels, etc.
- R: ggplot2, dplyr, data.table, glm,  prophet, lme4, glmnet, etc.
- Check GitHub activity and downloads as a guide

### X. Eight simple principles to write better code

1. Write modular code
2. Explicit is better than implicit
3. Write DRY code
4. Consistent and transparent naming
5. Iterate and re-run
6. Refactor code
7. Avoid Premature Optimization
8. Test code for critical issues

### X. If doing ML: use a experiment tracking system

Machine learning is iterative and experimental
Tracking progress and changes is hard and messy
Reproducibility in ML is a problem
Options: Weights and Biases for Deep Learning; MlFlow for ML in general

### X. Do code reviews (when possible)
- Code reviews are critical for:
  - Finding bugs
  - Improve code readability
  - Improve code performance
  - Improve documentation
  - Sharing your progress and knowledge with your group

### X. Resources to learn:

- Version control:
  - Pro Git Book: https://git-scm.com/book/en/v2
  - Pro Git Videos: https://git-scm.com/videos

  - Articles:
