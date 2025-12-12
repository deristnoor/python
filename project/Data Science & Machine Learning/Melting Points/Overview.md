# Melting Points Prediction Challange from Kaggle Competition

## Background
Predicting the melting point of organic molecules is a long-standing challenge in chemistry and chemical engineering. Melting point is critical for drug design, material selection, and process safety, yet experimental measurements are often costly, time-consuming, or unavailable.

## Goals
Build ML Model with low Mean Absolute Error (MAE) score on test-set that predict melting point for organic compounds given molecular descriptors

## Data Description

Data Description
- Total compounds: 3328
- Train: 2662 (80%)
- Test: 666 (20%)

Files
- train.csv : Features + target (Tm)
- test.csv : Features only, no target
- sample_submission.csv : Template with columns [id,Tm]

Columns
- id : unique ID
- SMILES : molecular string
- Group 1..N : descriptor features
- Tm : melting point (K) [train only]

## Data Approach
With the help from Perplexity.ai, the list of the most important parameters affecting the melting points of organic molecules, from most to least influential as follow:
1. Intermolecular force strength
2. Molecular symmetry and packing efficiency
3. Presence of functional groups
4. Molecular size and surface area
5. Molecular Shape (Branched and Linear)

With the present of the functional groups in the dataset, we can add 4 more feature that affecting the melting points using RDKit package.

## Method


## Results
Catboost Regressor with Hyperparameter tuning can predict the melting points with MAE score 30.11. Then, we compare prediction on the test data with external data. In total, we have 476 entry that have the same molecular string in both data. Using the same method of scoring, the prediction MAE score is 28.5.

