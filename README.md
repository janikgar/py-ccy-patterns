# Python Concurrency Patterns
This project demonstrates different concurrency patterns in Python, based on https://realpython.com/python-concurrency/.
## Requirements
- Python 3.x
- Requests library
  - `pip install requests`

To install requirements:
```
$ pip install -r requirements.txt
```

## Basic Script `basic.py`
The basic script runs the same two GET requests 80 times each.

## Threaded `threaded.py`
Designed specifically for I/O blocking jobs, this script performs the same requests in a multi-threaded fashion.

## Multiprocess `multi.py`
This script performs the same task utilizing as many cores as are available on the host processor.

## TODO: CPU Load
In the first revision, no provision is made for CPU blocking jobs.