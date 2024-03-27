# Match Predictor Project

## Project Overview
The Match Predictor is designed to forecast football match outcomes using advanced data analysis and machine learning techniques. This innovative application combines various predictive models to ensure accurate and reliable predictions.

## Predictive Models
The backend features a suite of predictors, including:
- Alphabet Model
- Gaussian Naive Bayes
- Points
- Offense Simulator (Fast)
- Offense Simulator
- Full Simulator
- Linear Regression

These models are tested and evaluated for accuracy, utilizing a unittest framework. 

## Testing Methodology
All predictors undergo testing to evaluate their performance.

## Running the code

## Backend

1.  Run tests
    ```shell
    make backend/test

1.  Run model measurement tests
    ```shell
    make backend/measure
    ```

1.  Run server
    ```shell
    make backend/run
    ```

1.  Run an accuracy report
    ```shell
    make backend/report
    ```

## Frontend

1.  Run tests
    ```shell
    make frontend/test
    ```

1.  Run server
    ```shell
    make frontend/run
    ```

## Integration tests

1.  Run tests
    ```shell
    make integration/test
    ```

1.  Interactive mode
    ```shell
    make integration/run
    ```
