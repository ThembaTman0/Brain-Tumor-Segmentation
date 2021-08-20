# Brain-Tumor-Segmentation

Medical imaging refers to a set of technologies designed to generate visual representations of the internal aspects of the human body in a non-invasive way. Medical imaging is intended to reveal internal organs that are hidden by skin and bones to analyze for abnormalities and diagnose and treat disease. The purpose of the project is to develop an automated supervised learning tumor diagnosis system that indicates whether a given brain MRI image represents a patient with tumor. Detailed log can be found in the report.

<!-- ![Alt text](https://raw.githubusercontent.com/Motaung08/Brain-Tumor-Segmentation/main/results/Ex1_brainTumor.jpg)
![Alt text](https://raw.githubusercontent.com/Motaung08/Brain-Tumor-Segmentation/main/results/ex1_NoBrainTumor.jpg) -->

### Supervised learning paradigms used
- k Nearest Neighbours
- Logistic Regression (gradient descent and genetic algorithm learning)


### Model performance
Logistic regression is the best performing model with a peak accuracy of 96%. Below is it's confusion matrix.

![Alt text](https://raw.githubusercontent.com/Motaung08/Brain-Tumor-Segmentation/main/results/LR_cm.png)

### kNN
kNN confusion matrix.

![kNN text](https://raw.githubusercontent.com/Motaung08/Brain-Tumor-Segmentation/main/results/knn_cunfusion_matrix.png)


### Logistic regression (full batch)
![LR fullbatch](https://github.com/Motaung08/Brain-Tumor-Segmentation/blob/main/results/full_batch.png)

### Logistic regression (genetic algorithm)
![LR GA](https://raw.githubusercontent.com/Motaung08/Brain-Tumor-Segmentation/main/results/Genetic_alg.png)

### Logistic regression (particle swamp optimization)
![LR pso](https://raw.githubusercontent.com/Motaung08/Brain-Tumor-Segmentation/main/results/pso_alg.png)
