import main

yaml = "---\ninput:\n  - type: people\n    id: 1\n    infoRequest:\n      - name\n      - films\n      - gender\n      - starships\n      - url\n "

req = {
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
    assert main.read_yaml_stream(yaml) == expected

def test_send_request():
    expected = {
        "gender": "hermaphrodite",
        "mass": "1,358",
        "name": "Jabba Desilijic Tiure",
        "species": ["http://swapi.dev/api/species/5/"],
        "url": "http://swapi.dev/api/people/16/"
    }
    assert main.send_request(req) == expected

def test_parse_results():
    obj =  {
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

