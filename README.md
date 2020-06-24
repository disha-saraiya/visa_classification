# H1-B Visa Classification using Support Vector Machines

_This project is part of the coursework for CS6220 Data Mining at Northeastern Univeristy, Seattle._

H1B Visas are a category of employment based, non-immigrant visas for temporary foreign workers in the USA. The selection process for these visas is often based on a lottery system, which can make the prediction of status confusing and tedious. 
This project aims at predicting the probability of acceptance or denial of an applicant's LCA (Labour Condition Application) depending upon various important aspects such as: 
* Applicant's current employer
* Current worksite address (State, City)
* Current prevailing wage (average salary)
* Current employment status (Full time/Part time)
* Current Job Title (Based on USCIS SOC names)

With this prediction, we hope to help both candidates and employers with an accurate assessment of what to expect during and after the application process.  

### Working 
To test the project, please follow these steps: 
* Clone/download the repository to your local machine
* Change directory to `dockerized_service`
* To run the app, type on your terminal : `python h1b_lca_classification_api.py`

### Jupyter Notebook Description
 * `data_visualization.ipynb` : This notebook contains various kinds of data visualization and exploration using the dataset. This was done in order to understand the data better, to see the most dominant features while also recognizing features that were extra or very high in number. This later helped in data preprocessing for feature reduction and extraction. 
 * `data_classification.ipynb` : This notebook contains data preprocessing and training/testing the dataset using Support Vector Classification. It also includes the results and classification matrix. 

### About the project
* Created by : Disha Saraiya, Ganga Hosmani 
* Algorithm : Support Vector Classification (SVC) from `sklearn.svm.SVC()`
* Dataset : [Kaggle H1B Dataset](https://www.kaggle.com/nsharan/h-1b-visa) 
* Frontend on: [SwaggerUI](https://swagger.io/tools/swagger-ui/)

### References 
* [Datacamp | Deepak Jhanji's Article](https://www.datacamp.com/community/tutorials/predicting-H-1B-visa-status-python)

* Data Understanding 
    * [Understanding what LCA is](https://redbus2us.com/what-is-h1b-lca-why-file-it-salary-processing-times-dol/) 
    * [Data Visualization](http://rstudio-pubs-static.s3.amazonaws.com/291447_c33c1030b1214189bc05c95d0231c9da.html)
    * [Similar Article](https://codeburst.io/the-h-1b-an-analysis-of-american-companies-requests-for-external-labour-2f9fc718613b)
* Data Visualization
    * [Managing a highly imbalanced dataset](https://towardsdatascience.com/what-to-do-when-your-classification-dataset-is-imbalanced-6af031b12a36)
    * [USCIS's SOC Classification Guideline](https://www.bls.gov/soc/2018/soc_2018_class_prin_cod_guide.pdf)
    * [Determining the correct prevailing wage level](https://www.usavisanow.com/how-to-determine-the-correct-prevailing-wage-level-for-perm-and-h-1b-petitions/)
    * [Foreign Labour Certification Data Center](https://www.flcdatacenter.com/)
    

_For any other questions/queries, please reach out to me on [LinkedIn](https://www.linkedin.com/in/dishasaraiya/) or  [Gmail](mailto:saraiya.disha18@gmail.com). Thanks for stopping by!_
