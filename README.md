### Model API Documentation
#### Base URL: https://model-rest-api.onrender.com

#### Endpoints
1. `/info` - GET Request

- Description: Retrieves information about the model's expected input format and provides a link to the dataset.
- Response: JSON with input requirements and dataset link.

2. `/model/predict` - POST Request

- Description: Takes a JSON body with input data for the model and returns predictions. The request body can contain a single input or a list of inputs.
- Parameters: JSON body with model input(s).
- Response: list of predictions for each input / predicted value for a single input.

3. `/model/sample/?num=<int>`- GET Request

- Description: Returns a sample of the dataset, with the number of samples specified by the query parameter num.
- Parameters: num (integer, optional, default: 1) - The number of dataset samples to return.
- Response: JSON with the requested sample(s) from the dataset.