#### Model API for presentation purposes
The model is deployed at: `https://model-rest-api.onrender.com`
Available endpoints:
- `/info` - GET request. The request will return the model input information as well as the link to the dataset.
- `/model/predict` - POST request with a JSON body containing the input data for the model. The model will return the prediction. The parameter could also be a list of inputs. The endpoint will return a list of predictions.
- `/model/sample/?num=<int>` - GET request. The request will return a sample of the dataset with the number of samples specified in the query parameter `num` (default num=1).