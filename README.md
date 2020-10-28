# Introduction

Need to see which roll numbers belong to which people in the
pdf which can be downloaded from ERP for internships/
placements?

You are at the right place.


## Installation

Make sure you have Java Development Kit (SE Edition) installed since
we use `tabula` to read pdfs which in return depends on Java.

Setup virtual environment in Python3 using:

```
virtualenv -p python3 .venv/
```

Activate it in a shell using:
```
source .venv/bin/activate
```

**Install Dependencies**

```
pip install tabula-py
```

## Usage

```
python main.py <filename>
```

For testing on sample file ([test.pdf](test.pdf)):

```
python main.py test.pdf
```

