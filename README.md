# Json Flattener

## Overview

This JSON Flattener transforms a potentially branched and deep JSON structure object into a flattened one.


## Getting Started

#### Prerequisites

 - Python3
 - Pytest

Open a terminal and `Git clone` this repository to your machine

```bash
https://github.com/99rafa/JsonFlattener

```

#### Running

Open a terminal in the JsonFlattener directory and run, for example

```bash
cat <inputFile>.json | python3 JsonFlattener.py

```
where <inputFile>.json is the name of file that contains the JSON object.

A prompt will appear

```bash

Check the file 'out.json' to get the flattened JSON version.

```

The `out.json` file is where the flattened JSON object is stored.


To run the tests, run

```bash

pytest JsonFlattener.py

```

which will run the 3 unit tests produced, each one of them with one of the input files included in the `example` folder.


## Observations

Challenge Duration: 2 hours

Done by: Rafael Alexandre
