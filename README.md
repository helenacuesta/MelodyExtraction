# Melody Extraction
This repository contains the code for a project on Melody Extraction for the Music Information Retrieval course from the master
in Sound and Music Computing at UPF (Barcelona). It is maintained by Joe Munday (joseph.munday01@estudiant.upf.edu) 
and Helena Cuesta (helena.cuesta01@estudiant.upf.edu). Feel free to contact us for any query/doubt/comment.

You can check how we are developing the project in the following blog: https://musicinformationretrieval.wordpress.com/category/audio-melody-extraction/
(check the tag *Audio Melody Extraction* for information only about this task), where we report on the steps and the procedure.

In this project we test two different melody extraction methods: MELODIA by Salamon & Gómez [1] and source/filter model 
by Durrieu et al. [2], using two existing datasets: Orchset [3] and MedleyDB [4].  

In this repository you will find the scripts that we have written for the whole project:  

1. **main** contains the whole commands sequence to perform all the experiments we've done: using both methods
for melody extraction in both datasets, and the evaluation of the results, which is done using the Python library
*mir_eval* [5]. This main script calls all the other ones.  

2. **melodia_melodyExtraction** and **melodia_evaluation** are the two scripts to extract the melody using MELODIA and 
evaluating the obtained results.  

3. **durrieu_melodyExtraction** and **durrieu_evaluation** are the two scripts to extract the melody using the source/filter
model and evaluating the obtained results.  

4. There are two more scripts, **txt2csv** and **averageResults**: the first one, as the name already suggests, converts txt
files into csv; the second one takes the evaluation results for the whole dataset and averages them to obtain a general
overview of the algorithms' performance.  

**References**

[1] J. Salamon and E. Gómez, “Melody Extraction from Polyphonic Music Signals using Pitch Contour Characteristics”, 
IEEE Transactions on Audio, Speech and Language Processing, 20(6):1759-1770, (2012).  

[2] J. L. Durrieu, G. Richard, B. David and C. Fevotte, “Source/Filter Model for Unsupervised Main Melody Extraction
From Polyphonic Audio Signals,” in IEEE Transactions on Audio, Speech, and Language Processing, vol. 18, no. 3, 
pp. 564-575, (2010).  

[3] Bosch, J., Marxer, R., Gomez, E., “Evaluation and Combination of Pitch Estimation Methods for Melody Extraction 
in Symphonic Classical Music”, Journal of New Music Research, (2016).  

[4] Bittner, R., Salamon, J., Tierney, M., Mauch, M., Cannam, C., & Bello, J. MedleyDB: A multitrack dataset for annotation 
– intensive mir research. International Society for Music Information Retrieval Conference, 155–160. (2014).  

[5] Colin Raffel, Brian McFee, Eric J. Humphrey, Justin Salamon, Oriol Nieto, Dawen Liang, and Daniel P. W. Ellis, 
“mir_eval: A Transparent Implementation of Common MIR Metrics”, Proceedings of the 15th International Conference on
Music Information Retrieval, (2014).
