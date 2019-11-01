# Introducing software development best practices for the behavioral and social sciences

## Keep in mind:

- I'm not a software engineer and I don't have a CS degree
- This is not about the best way of writing code
- This is not about the best programming language for the B&SS
- This is not about the best statistical procedures or machine learning approaches
- This is not about deploying data pipelines in production systems

## Keep in mind

- This is about what I believe are good software engineering practices for scientific computing in the B&SS  
- This is more useful for projects that do not require large scale computing (HTC, HPC, Hadoop, Spark, cloud computing, etc.). Roughly ~10 to 1 million of rows.
- This is about simple architectural principles that allow creating data projects which are:

  - Reproducible
  - Reusable
  - Reliable
  - Maintainable
  - Scalable
  - Shareable

## Keep in mind:

I'm coming from my personal experience analyzing data and writing code for research in sociology, public policy/economics, cognitive neuroscience and psychology in the past ~8 years (since 2011).

- SPSS and Excel for 4 years
- STATA and MATLAB for 2 years
- Python and R for 2.5 years

## Recommended good enough practices

### X. Use free and open-source software (FOSS):
- Python, R, Scala, SQL, Julia, Bash, etc. instead of SPSS, STATA, MATLAB, SAS, etc.
- Otherwise, reproducibility, reusability, and shareability, are not possible
- Far more people use FOSS than proprietary software

### X. Create simple and well-organized data file system (or "code base")
  - Separate scripts/programs from data and results
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
- For Python virtualenv or conda environment; for R conda environment

### X. Use version control systems
- Git, Mercurial, or SVN
- Push changes frequently
- Use branches for experimentation
- Use a third backup (safe) backup system with continuous sync (Box, Dropbox, Drive, Mega, etc.)

### 3. Use version control systems
- Optimized for plain text. Not that good for tabular data, docx, or PDFs.
- Bad for "large" files (limited to 100 megabytes per file in GitHub).
- If files are too large: zip the files (OK solution). Read data from the web (Better solution)
- Raw should not change, and therefore, should not require version tracking
- Keep minimal notes/log of major changes

## Documentation:
	- README.md
  - LICENSE.txt
	- requirements.txt
	- to-do.txt

### X. Modularization

- DRY


- Explicit is better than implicit

- Consistent and transparent naming

- Iterate and re-run

- Avoid Premature Optimization



- Testing

- Refactoring

- Code reviews (when possible)
Use well-tested and properly supported software libraries
Maintain your raw-data (single authoritative version of your data)
	- Readable and consistent naming
	- Use unique and consistent identifiers
	- Add dates
	- Keep a data schema / metadata
	- Keep multiple copies of the file
	- When possible, avoid saving multiple versions of the data, let the computer 				automate  building clean data on the fly* / Some (cite) prefer to create intermediate data products. I don't like it, because they incentive to skip previous steps (i.e., not-rerun and test) in the script. For instance, if you change a dependency (upgrade a library to a newer version) part of your pipeline may go untested. BUT, if you are working with very large files and doing way to many pre-processing you may consider to use a different approach.
	- Use open non-proprietary formats (CSV, JSON, XML etc)
