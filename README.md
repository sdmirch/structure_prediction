## tl;dr
Allen Institute for Cell Science’s imaging pipeline could affect the structure and nucleus of the cell depending on the protein being imaged. I used various models to determine if the protein being imaged was predictable if only features related to structure and nucleus were used (meaning no data about the protein itself). Proteins were predictable using this limited data, which means that there are likely batch effects within the imaging pipeline.

## Intro:
The Allen Institute for Cell Science’s pipeline relies identical processing for all cells to ensure reproducibility. Understanding batch effects in the imaging pipeline can help understand whether processes within the pipeline are affecting image results. Imaging cells may change features related to the structure and nucleus of the cell, which are both measured and derived. To test whether the type of protein imaged can affect these measurements, we can attempt to predict the protein being imaged using only features related to the cell structure and nucleus (and removing features related to the protein). If prediction of the protein is possible, that may indicate batch effects within the pipeline, which of course we want to avoid. The features that are correlated with the protein being imaged are clues to the cause of the batch effects occurring.

## Data Preparation:
Before prediction can take place, the dataset containing the cell imaging features and protein labels must be cleaned. All features related to the protein imaged are removed from the data set. The protein name is the only column that is retained as a label for the classification step. Then, NaNs are removed or replaced. If NaNs are present in the majority of all columns in a row, then the row is removed; this is the case in 175 rows. If NaNs are present in a small subset of rows, then the value is imputed based on the distribution of values for a given feature. This methodology is applied to the “feat_nuc_obj_mean_edge_len” and the “feat_nuc_obj_std_edge_len” features, and the mean of each feature is used as the imputation value.

## Modeling:
After feature reduction and imputation, different classification models are trained using the full feature set, to determine whether prediction is possible. A logistic regression, a random forest, and gradient boosted classifiers (sklearn and xgboost implementations) are trained by minimizing cross-entropy loss. They are compared with a model that will randomly guess the label of the protein with probability equal to the distribution of the given protein label in the data set. The trained classifiers achieve similar cross entropy losses, and all are more predictive than random chance, as shown in the overall precision and recall values shown following classification reports.

Gradient Boosting (left) and Random Guessing (right) Classification Reports:

![XGBoostClassificationReport](/img/XGBoostClassificationReport)![RandomGuessClassificationReport](/img/RandomGuessClassificationReport.png)

To confirm that prediction is possible, a distribution of the accuracy for the random guess model by guessing the labels for the data 10,000 times is plotted below in red; the blue line shows the accuracy of the logistic regression. The difference between the random guess and the accuracy of the logistic regression is statistically significant.



## Evaluation:
Now that it can be shown with confidence that prediction is possible, inference based on the feature importances and coefficients from the trained models can provide insight into which features aid in the protein structure prediction. The feature importances from the xgboost gradient boosted classifier, which achieved the lowest cross entropy loss, are shown below.


The first three top features importances are used to understand clusters of protein structures; the two scatter plots show that the first few features do not show easily understandable or interpretable clusters of proteins, even though they provide the most information about the labels.


Logistic regression modeling techniques are selected for further analysis due to their interpretability. Eleven one-versus-all logistic regression models are trained so that structure-specific coefficients can be analyzed; the positive label is a specific protein structure, and the negative label is given to the remaining 10 structures. The two features with the largest resulting coefficients are used in scatter plots to show clusters of red positive labels on top of the black negative labels. The coefficients with the highest values may indicate a cluster of ZO1 in the two dimensions shown, but often, the first two coefficients are insufficient to demonstrate a noticeable clustering for Beta Actin and ST6GAL1.



## Conclusions:
Prediction of proteins was possible indicating batch effects in the imaging pipeline are likely affecting the structure and nucleus of the cell.
