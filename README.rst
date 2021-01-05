Kock bacillus
=============
The Koch bacillus (Mycobacterium tuberculosis) is an aerobic bacillus associated with tuberculosis disease.
For more information, you can visit the following link:
 `wikipedia link <https://en.wikipedia.org/wiki/Mycobacterium_tuberculosis>`

Koch_bacillus is a Python package built to explore the analytic information of genetic Koch bacillus information.
The Open Reading Frame (aka ORF) are a nucleotide sequence needed to codify a protein.
Bacillus gen has a multiples ORF.

Dates
-----
The dates are extracted from the "UCI Machine Learning" and they have the datalog format.
 `UCI link <https://archive.ics.uci.edu/ml/datasets/m.+Tuberculosis+Genes>`

- tb_funtions.pl: This file contains general information about genes and its functionals classes.
- tb_data_XX.pl: This collection has a genetic detail from genes.
     In this package only need the ORF relations, "tb_to_tb_evalue" attribute.

Package structure
-----------------
The package has the following structure:

| Koch_bacillus |              |           | (main folder)                             |
|---------------|--------------|-----------|-------------------------------------------|
| - Data        |              |           | (Data folder with tb_functions.pl file)   |
|               | -- orfs      |           | (Data subfolder with tb_data_XX.pl files) |
| - Doc         |              |           | (document adictional folder)              |
| - Koch        |              |           | (main folder with python files)           |
|               | -- drawing   |           | (python file with drawing functions)      |
|               | -- Orf       |           | (Analytic Kock bacillus python files)     |
|               |              | --- tests | (Analytic test files)                     |
|               | -- readwrite |           | (read and writes methods implemented)     |
|               |              | --- tests | (read and write test files)               |
| - Test        |              |           | (main test folder)                        |
| - venv        |              |           | (library root)                            |

Execution
=========
Execute the main.py file.

Test
====
All the python files have a main process which is able to test the different functions.
Furthermore, test processes have been implemented in the test folders.
For executing the main test process run "test_kock.py" from Test folder.

Graphics
========
 - 1.1.  Número de ORFs por clase.
Because there are too many numbers of output results (class_Id), it is shown the top 10 with a vertical bar graph.

 - 2.1.  Número de clases con descripción "protein" y uno o más ORF.
In that case, the selected graph is a horizontal bar graph because it has only one measure and it's possible to show the indicator.

 - 2.2.  Promedio de ORFs cuya descripción contiene la palabra "hydro" y es de una longitud de 13.
The same case as the previous question.

 - 3. Número de clases por dimensión.
We have eight results to be showed. In that case, a vertical bar can show the results correctly.


