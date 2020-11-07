
import glob
import json
import os
import requests
import yaml
from flask import Flask, request

# setting a base url for the stars api
BASE_URL = 'https://swapi.dev/api'
# pulling in the current working directory
WORKING_DIR = os.path.dirname(os.path.realpath(__file__))



# initalizing the flask APP
APP = Flask(__name__)

# This function will take in a single yaml file and return a list of dictionaries from the star wars api
def read_yaml_stream(stream):
    data = []
    try:
        safe_yaml = yaml.safe_load(stream)
        for _, dictionary in safe_yaml.items():
            for req in dictionary:
                try:
                    response = send_request(req)
                    data.append(response)
                except Exception as err:
                    print(err)
    except yaml.YAMLError as exc:
        print('{} yaml is not well formatted'.format(exc))
    return data


# This function will call out to the startwars api with the specific parameters
def send_request(obj):
    url = '{}/{}/{}'.format(BASE_URL, obj["type"], obj["id"])
    response = requests.get(url)
    json_response = response.json()
    if response.ok:
        parsed_results = parse_results(json_response, obj["infoRequest"])
        return parsed_results
    else:
        print ('The url: {} returned a {} error code'.format(url, response.status_code))



# This function will pull the objects out of the returned dictionary
def parse_results(obj, info):
    parsed_obj = {}
    for i in info:
        parsed_obj['{}'.format(i)] = obj[i]
    return parsed_obj



@APP.route('/api/health', methods=['GET'])
def heatlh():
    return "alive"
# This route will allow to read in the local .yaml files and return a json list
# containing objects of information on the star wars characters
# you can also send a post request to this route using a yaml file as the data-binary
# and it will write to the local json file and also return a json list
# containing objects of information on the star wars characters 
@APP.route('/api/yaml', methods=['GET', 'POST'])
def run():
    data = []
    if request.method == "POST":
        try:
            req_dict = request.form.to_dict()
            first_pos = list(req_dict.keys())[0]
            response = read_yaml_stream(first_pos)
            with open('{}/swapi-output.json'.format(WORKING_DIR), 'w') as f:
                f.write('{}'.format(json.dumps(response, indent=4, sort_keys=True)))
            return json.dumps(response, indent=4)
        except Exception as err:
            print(err)
    else: 
        files = glob.glob('{}/*.yaml'.format(WORKING_DIR))
        for yaml_file in files:
            with open(yaml_file, 'r') as stream:
                response = read_yaml_stream(stream)
                data.append(response)
        flat_list = [item for sublist in data for item in sublist]
        with open('{}/swapi-output.json'.format(WORKING_DIR), 'w') as f:
            f.write('{}'.format(json.dumps(flat_list, indent=4, sort_keys=True)))
        return json.dumps(flat_list, indent=4)


if __name__ == "__main__":
    APP.run(host='0.0.0.0')
