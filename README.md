# Reproducibility Arno-Jeremy

## Introduction

The goal of this project is to reproduce experiments this article https://blog.mathieuacher.com/FootballAnalysis-xG-COVIDHome/ in order to analyse if playing at home in football is an advantage especially the effects of Covid on it. Our goal during reproduction was to scrap data of five football leagues and then reproduce all of the graphs using the same metrics to compare the results. We also add recent years which is a factor of relicability to have more information on data before and after Covid pandemic. 

## Reproducibility

### How to Reproduce the Results
1. **Requirements**  
   For this project, we have used : 
    - Python 3.12.4
    - pandas
    - matplotlib
    - BeautifulSoup / requests
    - numpy
    - scipy

The data have been scrapped on https://understat.com/. BeautifulSoup and requests were used to scrap data. pandas and matplotlib were used to reorganise data and print it using graphs.

2. **Setting Up the Environment && Reproducing Results**  
   - Both Dockerfiles are setting up the environment and also reproducing results
   - Provide instructions for using the Dockerfile to create a reproducible environment:  
     ```bash
     docker build -t reproducible-project .
     docker run -v ./output:/app/output reproducible-project
     ```
  
   - Instructions for using the second Dockerfile with other study:
     - The terminal must be in Other_leagues
     ```bash
     docker build -t reproducible-other-study .
     docker run -v ./output:/app/output reproducible-other-study
     ```

   - Results of both studies can then be seen in the html file of their output folder (`analysis_results.html`), 
     Opening it will show all code and output produced by the original notebook

4. **Automation (Bonus)**  
   - Explain the included GitHub Action that produces or analyzes data automatically.  
    
### Encountered Issues and Improvements

The hardest part was to find where data can be scrapped on understat. At the beginning, we didn't scrap the appropriate field to compute graphs of the paper.

For all graphs of the study, we didn't encounter any issue except for the last one.

The last one was about the Mann–Whitney U test to assess differences between seasons on the xPoints metric.
After implementing this test, we found exactly twice the results of the paper. For example, Bundesliga 2014-2015 was 0,231377 on the paper and 0.462894 with our programm. We conclude that the difference between these two experiments was an update in the spicy library. 

In addition, the wilco-xG and wilco-xG-pvalue columns have errors. All the values are the same.

### Is the Original Study Reproducible?

We succeded to reproduce all the graphs of the study except some graphic points that doesn't change the final result. As said before, metrics like wilco-xG and wilco-xG-pvalue were not provided. Then we calculate our own and it confirms the actual tendance that playing at home is still an advantage after the Covid.

JEREMY : parler des résultats pour voir si ça confirme bien l'avantage ou non de jouer à domicile

- Summarize the success or failure of reproducing the study.
- Include supporting evidence, such as comparison tables, plots, or metrics.

## Replicability

### Variability Factors
- **List of Factors**: Identify all potential sources of variability (e.g., dataset splits, random seeds, hardware).  
  Example table:
  | Variability Factor | Possible Values     | Relevance                                   |
  |--------------------|---------------------|--------------------------------------------|
  | Random Seed        | [0, 42, 123]       | Impacts consistency of random processes    |
  | Hardware           | CPU, GPU (NVIDIA)  | May affect computation time and results    |
  | Dataset Version    | v1.0, v1.1         | Ensures comparability across experiments   |

- **Constraints Across Factors**:  
  - Document any constraints or interdependencies among variability factors.  
    For example:
    - Random Seed must align with dataset splits for consistent results.
    - Hardware constraints may limit the choice of GPU-based factors.

- **Exploring Variability Factors via CLI (Bonus)**  
   - Provide instructions to use the command-line interface (CLI) to explore variability factors and their combinations:  
     ```bash
     python explore_variability.py --random-seed 42 --hardware GPU --dataset-version v1.1
     ```
   - Describe the functionality and parameters of the CLI:
     - `--random-seed`: Specify the random seed to use.
     - `--hardware`: Choose between CPU or GPU.
     - `--dataset-version`: Select the dataset version.


### Replication Execution
1. **Instructions**  
   - Provide detailed steps or commands for running the replication(s):  
     ```bash
     bash scripts/replicate_experiment.sh
     ```

2. **Presentation and Analysis of Results**  
   - Include results in text, tables, or figures.
   - Analyze and compare with the original study's findings.

### Does It Confirm the Original Study?
- Summarize the extent to which the replication supports the original study’s conclusions.
- Highlight similarities and differences, if any.

## Conclusion
- Recap findings from the reproducibility and replicability sections.
- Discuss limitations of your
