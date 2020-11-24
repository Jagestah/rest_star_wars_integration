# rest_star_wars_integration

This is a service that you can call and pass it yaml to get sweet sweet star wars information

## Getting Started

### Prerequisites

Must have [Python](https://www.python.org/) version 2.7.0

***Note: If you want to run this in python 3+ you must add parameters around the print statements    : C***
</br>
</br>

### Installing

Clone the repo

```
git clone https://gitlab.com/anon-alangford/rest_star_wars_integration.git

```
Or if you are cool, with ssh

```
git clone git@gitlab.com:anon-alangford/rest_star_wars_integration.git

```

Then navigate into the repo and run

```  pip install -r requirements.txt ```


</br>
</br>

## Development

Run

``` python ./main.py ```


This will kick off the flask server on port 5000 and start to accept requests.


</br>
</br>


## Hitting The Endpoints

This service has two endpoints.

### Path: ***/api/health***   Methods: ***GET***, ***POST***    Returns: ***Json***
When called this will send back a 200 response with a string that has a value of "alive"

### Path: ***/api/json***   Methods: ***GET***, ***POST***    Returns: ***Json***
When called with a get request the application will scan it's local directory and find any yaml file, if formatted correctly it will send requests to the star wars api and return a json response to you with information about sweet sweet star wars.

When called with a post you must send a yaml file as a data-binary object and it will make a request to the star wars api and return a json object with star wars information based on the yaml request you sent.

``` curl -XPOST --data-binary @./input.yaml http://localhost:5000/api/json ```

An example on how the yaml should be formatted can be found [here](https://gitlab.com/anon-alangford/rest_star_wars_integration/-/blob/master/input.yaml)

In both GET and POST it will write a json file named swapi-output.json locally which you can view.


</br>
</br>

## Linting The Project

Navigate into the repo and then run 

``` pip install pylint ```

And then run

``` python -m pylint ./*.py ```

**Please Lint Before Commit!**


</br>
</br>

## Running The Tests

Tests are ran with pytest, To start the tests navigate into the root repo directory and run

``` pip install pytest ```

And then run


 ``` python -m pytest ./main_test.py ```


</br>
</br>

## Running in Kubernetes
First you need a local Kubernetes cluster installed or have a remote one set up to deploy to.

I used [minikube](https://minikube.sigs.k8s.io/docs/start/) to test this deployment out locally.

Make sure [Helm](https://helm.sh/) is installed

Once you are ready to deploy navigate into the rest-star-wars folder and run 

```  helm install rest-star-wars . ```

Once deployed it will spit out commands that you can copy and paste into your console that will forward your local port of 8080 to the clusters port which is defaulted to 5000 and should give you a url that you can go to call the service.
```http://localhost:8080/api/health```

</br>
</br>

## Deployment
When a merge request gets created, the pipeline will kick off on Gitlab.

The pipeline will test and lint the project as well as as lint the helm template and show you the changes it would make if it were to deploy.

The pipeline will then build the image and once merged to master or when a tag gets created it will deploy the image to a public docker repository. (If less frugal I would push this to AWS ECR or a private repo where we wouldn't get rate limited on subsequent calls to pull down the image when deploying. Also I would have helm deploy this to an EKS cluster.)

This application is meant to be deployed to a Kubernetes cluster using helm.



</br>
</br>

## Built With

* [Python v2.7.0](https://www.python.org/) - The language used
* [Kubernetes](https://youtu.be/QxvmO-QlxJQ?t=43) - The container orchestration tool
* [Helm](https://helm.sh/) - The Kubernetes package management tool


</br>
</br>

## Authors

* **Alan G Ford** - *inital work* - [Gitlab Link](https://gitlab.com/anon-alangford)

See also the list of [contributors](https://www.youtube.com/watch?v=oHg5SJYRHA0) who participated in this project