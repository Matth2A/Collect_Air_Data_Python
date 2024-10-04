# Collect Air Data Python

---
## Table of Contents
- [Introduction](#Introduction)
- [Installation](#Installation)

---
## Introduction

This repository has for goal to collect air data from several sources. At the moment, the program is able to collect data from 2 sources:
- [Air Quality Open Data Platform](https://aqicn.org/data-platform/covid19/ro/)
- [Europe Environment Agency](https://www.eea.europa.eu/en/datahub/datahubitem-view/778ef9f5-6293-4846-badd-56a29c70880d)


It's composed of three main files:
- `program.py`: The main file that runs the program
- `dowloadFile.py`: The file that contains the class that downloads the data from the API and automatically change the format of the data
- `api_Data.py`: The file that contains the class that retrieves the data from the API


## Installation

This project has been conceived in `python 3.11`. 

To run it, you need to dowload theses libraries:

- `pandas`
- `pyarrow`
- `fastparquet`
- `request`

You can do this by running the following command:

```bash
pip install -r requirements.txt
```