<p align="center">
  <a href="" rel="noopener">
 <img width=497px height=127px src="https://www.businesswatcher.hu/wp-content/uploads/2020/06/Business-Watcher-Logo-vol.1.-ENG.png" alt="Project Title"></a>
</p>

<h3 align="center">Solution of Python Weekend Entry Task (2022)</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Purpose of current project is to get attendance to "Kiwi.com Python Weekend" in 2022 march 4-6.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

Project focuses on develop a search script runable on terminal (without GUI) due to requirements (raised in https://github.com/kiwicom/python-weekend-entry-task).

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites

At least Python 3.8.10 be installed on your computer.

```
Please visit python.org and download it via the link below.
https://www.python.org/downloads/

```

Only the standard libraries are necessary to execute the script, no need 3rd party packages, notebooks, specialized distros (Conda) etc.
The code should run as is, no environment setup is required.




### Installing <a name="installing"></a>



Extract the received ZIP file in case of getting it via email or downloading it from git repo in that format.
Using (Ubuntu) Linux OS, such as:

```bash
unzip flight_search-master.zip
```


Extract the received ZIP file in case of using Windows OS command line:

```
tar -xf flight_search-master.zip
```


You have to get the following directory structure within flight_search-master folder:
```bash
├── example
│   ├── example0.csv
│   ├── example1.csv
│   ├── example2.csv
│   └── example3.csv
├── modules
│   ├── data_validation.py
│   ├── flights.py
│   └── __init__.py
├── README.md
├── solution.py
```
`example/*.csv`:
 * Input files for testing purpose

`solution.py`:
  * It gets the parameters (mandatory & optionals - see in further subchapters below) from console and includes the execution function of the search-engine module, so called  `flights`. It calls `search function` from  `flights` module and validate the parameters got from terminal.
  If any of the mandatory or optional parameters is wrong the following error message retruns, without keep running:
```bash
# ERROR MESSAGE
One of the arguments is invalid!!
```

`modules/flights.py`:

  - It contains those functions which are necessary to derive proper search result(s):
  * set_result     --> writes the result set into `json_data.json` and to the terminal with the number of flights found.
  * get_traveltime --> converts string timestamp into ISO format and returns how much time the travel take.
  * get_overlay    --> calculates time between flight changes
  * read_csv       --> read csv input file and validate input data records according to definitions in `modules/data_validation.py`
  * get_flights    --> based on search parameters, this function is the core-engine of the task. It calls `get_traveltime` and `get_overlay`   
                      functions.
  * search         --> calles direct or indirect way every function in this module by splitting the return and non-return searches.


`modules/data_validation.py`:

- Functions of current module go through the atributes in input file and flag if any error would be detected:
* flight_no_checker --> returns error message if fligh number is not equal to 5 (supposing according to - example - input files this is the standard length) or its characters massed up.
```bash
# ERROR MESSAGE
  Input file contains invalid flight number such as '[FLIGHT_NO]'!
```
* geo_checkor --> validates if airport codes correctness. If airport code is not 3 character long and it is not string following error message returns:
```bash
# ERROR MESSAGE
'[GEO_CODE]' is not a valid geo code to '[ARRIVAL / DEPARTURE]' airport. Please fix adequate field of input file!
```
* timestamp_checker --> handles error of incorrect format of timestamp regarding arrival / departure time
```bash
# ERROR MESSAGE
Sorry but date format of '[ARRIVAL / DEPARTURE TIMESTAMP]' is unacceptable in the field '[ARRIVAL / DEPARTURE TIME COLUMN]' of input file: '[VALUE ERROR MESSAGE]'
```
* integer_checker --> returns error message if called column of input file contains data type apart of integer. It validates string representation of integers.
```bash
# ERROR MESSAGE
[NUMBER] is not a number in '[COLUMNNAME]' field. Please fix adequate field of input file!
```
* float_checker --> regarding float number validation and error handling
```bash
# ERROR MESSAGE
'[NUMBER]' is not a number. Please fix adequate field of input file!
```



## 🎈 Usage <a name="usage"></a>

Step into the folder where `solution.py` script is:


List of mandatory arguments of the solution python module:
| Argument name | type    | Description              | Notes |
|---------------|---------|---------------------------------------------------------------------------------------------------------------------|---------- |
| `filepath`    | string  | filepath of csv file, which has proper structure with all necessary input data (see an example file attached)       | Mandatory |
| `origin`      | string  | Origin (departure) site where You would like to travel from | Mandatory |
| `destination` | string  | Destination (arrival) site where You would like to travel to | Mandatory |


### 1. Execution
If you just want to run a search on airports code without any additional filter, run the following command:
```bash
    python -m solution  example/example3.csv BPZ WTN
```

There are two other optional argument which can be used to tune up Your search:
| Argument name | type    | Description              | Notes                        |
|---------------|---------|--------------------------|------------------------------|
| `bags`        | integer | Number of requested bags | Optional (defaults to 0)     |
| `return`      | boolean | Is it a return flight?   | Optional (defaults to false) |



### 2. Execution
  a) scenario, if you want to search for flights which allow at least one lagguage to take.
  **NOTE:** Changing flights take a look at what is the maxium number of bag can be taken because of "bag allowance". It can reduce your results.
    (e.g. your 1st flight allows 2 bags, but changing to the 2nd one it just allows 1)

  ```bash
    python -m solution  example/example3.csv BPZ WTN --bags=1
    
    #OR
    python -m solution  example/example3.csv BPZ WTN -b 1
  ```

  b) scenario, if you want to search return flights as well with one lagguage. 
- **NOTE:** Take into account overlay limitations are also used in case of return flights and the lagguage limitation as well.

```bash
  python -m solution  example/example3.csv BPZ WTN --bags=1 --return

  #OR
  python -m solution  example/example3.csv BPZ WTN -b 1 -r
```

After running the parameterized module, **`the search result will be printed to console and saved in json_data.json file in the current`** directory.
Providing `bags` with greater than 0 value, it will be utilized in case of flight changes, so it has to be less than or equal to smaller bag allowance limitation.
Providing `return`  argument, the result set will include the "ways there" and "return journeys" as well.



```bash
python -m solution example/example0.csv WIW ECV --bags=1 --return
```

RESULT SET is a json-compatible structured list of trips `sorted by total_price` (ascending order alias cheapest is first):
```json
[
    {
        "flights": [
            {
                "flight_no": "ZH151",
                "origin": "WIW",
                "destination": "ECV",
                "departure": "2021-09-01T07:25:00",
                "arrival": "2021-09-01T12:35:00",
                "base_price": "245.0",
                "bag_price": "12",
                "bags_allowed": "2"
            }
        ],
        "bags_allowed": "2",
        "bags_count": 1,
        "destination": "ECV",
        "origin": "WIW",
        "total_price": 257.0,
        "travel_time": "5:10:00"
    },
    {
        "flights": [
            {
                "flight_no": "ZH151",
                "origin": "WIW",
                "destination": "ECV",
                "departure": "2021-09-02T07:25:00",
                "arrival": "2021-09-02T12:35:00",
                "base_price": "245.0",
                "bag_price": "12",
                "bags_allowed": "2"
            }
        ],
        "bags_allowed": "2",
        "bags_count": 1,
        "destination": "ECV",
        "origin": "WIW",
        "total_price": 257.0,
        "travel_time": "5:10:00"
    },
    {
        "flights": [
            {
                "flight_no": "ZH151",
                "origin": "WIW",
                "destination": "ECV",
                "departure": "2021-09-06T07:25:00",
                "arrival": "2021-09-06T12:35:00",
                "base_price": "245.0",
                "bag_price": "12",
                "bags_allowed": "2"
            }
        ],
        "bags_allowed": "2",
        "bags_count": 1,
        "destination": "ECV",
        "origin": "WIW",
        "total_price": 257.0,
        "travel_time": "5:10:00"
    },
    {
        "flights": [
            {
                "flight_no": "ZH151",
                "origin": "WIW",
                "destination": "ECV",
                "departure": "2021-09-11T07:25:00",
                "arrival": "2021-09-11T12:35:00",
                "base_price": "245.0",
                "bag_price": "12",
                "bags_allowed": "2"
            }
        ],
        "bags_allowed": "2",
        "bags_count": 1,
        "destination": "ECV",
        "origin": "WIW",
        "total_price": 257.0,
        "travel_time": "5:10:00"
    },
    {
        "flights": [
            {
                "flight_no": "ZH151",
                "origin": "ECV",
                "destination": "WIW",
                "departure": "2021-09-01T15:35:00",
                "arrival": "2021-09-01T20:45:00",
                "base_price": "245.0",
                "bag_price": "12",
                "bags_allowed": "2"
            }
        ],
        "bags_allowed": "2",
        "bags_count": 1,
        "destination": "WIW",
        "origin": "ECV",
        "total_price": 257.0,
        "travel_time": "5:10:00"
    },
    {
        "flights": [
            {
                "flight_no": "ZH151",
                "origin": "ECV",
                "destination": "WIW",
                "departure": "2021-09-02T15:35:00",
                "arrival": "2021-09-02T20:45:00",
                "base_price": "245.0",
                "bag_price": "12",
                "bags_allowed": "2"
            }
        ],
        "bags_allowed": "2",
        "bags_count": 1,
        "destination": "WIW",
        "origin": "ECV",
        "total_price": 257.0,
        "travel_time": "5:10:00"
    },
    {
        "flights": [
            {
                "flight_no": "ZH151",
                "origin": "ECV",
                "destination": "WIW",
                "departure": "2021-09-06T15:35:00",
                "arrival": "2021-09-06T20:45:00",
                "base_price": "245.0",
                "bag_price": "12",
                "bags_allowed": "2"
            }
        ],
        "bags_allowed": "2",
        "bags_count": 1,
        "destination": "WIW",
        "origin": "ECV",
        "total_price": 257.0,
        "travel_time": "5:10:00"
    },
    {
        "flights": [
            {
                "flight_no": "ZH151",
                "origin": "ECV",
                "destination": "WIW",
                "departure": "2021-09-11T15:35:00",
                "arrival": "2021-09-11T20:45:00",
                "base_price": "245.0",
                "bag_price": "12",
                "bags_allowed": "2"
            }
        ],
        "bags_allowed": "2",
        "bags_count": 1,
        "destination": "WIW",
        "origin": "ECV",
        "total_price": 257.0,
        "travel_time": "5:10:00"
    }
]
```
<br>
<br /> 

## ⛏️ Built Using <a name = "built_using"></a>

- Ubuntu 20.04 LTS
- Python 3.8
- CSV file storage


## ✍️ Authors <a name = "authors"></a>

- [@stnorbi](https://github.com/stnorbi/flight_search) - Initial work
- [@BusinessWatcher](https://businesswatcher.hu/en) - Blog

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

 - https://www.kiwi.com/hu/
