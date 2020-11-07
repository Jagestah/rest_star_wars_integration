"""This module will test the functions in the main.py"""
import main

YAML = """
---input:
  - type: people
    id: 1
    infoRequest:
      - name
      - films
      - gender
      - starships
      - url
 """

REQ = {
    "type": "people",
    "id": 16,
    "infoRequest": [
        "name",
        "mass",
        "gender",
        "species",
        "url"
    ]
}

def test_read_yaml():
    """Tests the read_yaml function in the main.py"""
    expected = [{
        'films': [
            'http://swapi.dev/api/films/1/',
            'http://swapi.dev/api/films/2/',
            'http://swapi.dev/api/films/3/',
            'http://swapi.dev/api/films/6/'
        ],
        'gender': 'male',
        'name': 'Luke Skywalker',
        'starships': [
            'http://swapi.dev/api/starships/12/',
            'http://swapi.dev/api/starships/22/'
            ],
        'url': 'http://swapi.dev/api/people/1/'
    }]
    assert main.read_yaml_stream(YAML) == expected

def test_send_request():
    """Tests the send_request function in the main.py"""
    expected = {
        "gender": "hermaphrodite",
        "mass": "1,358",
        "name": "Jabba Desilijic Tiure",
        "species": ["http://swapi.dev/api/species/5/"],
        "url": "http://swapi.dev/api/people/16/"
    }
    assert main.send_request(REQ) == expected

def test_parse_results():
    """Tests the parse_results function in the main.py"""

    obj = {
        "films": [
            "http://swapi.dev/api/films/1/",
            "http://swapi.dev/api/films/2/",
            "http://swapi.dev/api/films/3/",
            "http://swapi.dev/api/films/6/"
        ],
        "gender": "male",
        "name": "Luke Skywalker",
        "starships": [
            "http://swapi.dev/api/starships/12/",
            "http://swapi.dev/api/starships/22/"
        ],
        "url": "http://swapi.dev/api/people/1/"
    }
    info = ["name", "gender", "url"]
    expected = {
        "gender": "male",
        "name": "Luke Skywalker",
        "url": "http://swapi.dev/api/people/1/"
    }
    assert main.parse_results(obj, info) == expected
