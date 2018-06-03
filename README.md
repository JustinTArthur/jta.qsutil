# jta.qsutil - Complex URL Query String Processing
## Background
The specs that define the makeup of URLs are very flexible when it
comes to what makes up the query string portion (the part after the `?`). Many
web services take the initial recommendation of using `key=value` pairs to
another level by allowing complex structures to be represented for a
sacrifice in parsing performance.

The goals of this project are:
* Be able to process sequence and sub-mapping hints in URL query string keys.
* Only shape values into sequences if there are multiple occurrences of the same
 key or the key contains a sequence hint.
* Remain standards-compliant with URI and URL RFC specs.
* Provide an API similar to Python 3's standard urllib.
* Be Python 2 and 3 compatible without relying on a compatibility library.


## Installation
```bash
pip install jta.qsutil
```

## Parsing
This library processes query strings, looking for hints of deeper structure.
It's designed to use the same square-bracket hints that Ruby on Rails and
Express use. The library will also only portray items as sequences if more than
one value has been supplied or a hint has been given.

### Single Strings or Sequences
```python
from jta.qsutil.parse import parse_qs

parse_qs('a=this&b=that&a=another')
# {'a': ['this', 'another'], b: 'that'}
```

This differs from the parsing behavior of the Python standard library as well as
the Flask and Django projects, which use homogeneous dicts of
`{key: sequence_of_values, …}`. Parsing into such a form is generally faster,
but some consider it less readable.


### Sequence Hints
```python
parse_qs('a[]=this&a[]=that')
# {'a': ['this', 'that']}

parse_qs('singleItemSequence[]=this')
# {'singleItemSequence': ['this']}
```

### Sub-Mapping Hints
```python
parse_qs('a[b]=this')
# {'a': {'b': 'this'}}
    
parse_qs('a[b]=this&a[b]=that')
# {'a': {'b': ['this', 'that']}}
```

### Empty Items
```python
parse_qs('a', keep_blank_values=True)
# {'a': ''}
```

## Compared to Other Python Querystring Parsing Libs
Comparison with other libraries can be achieved with the source repo's
`tests/benchmark_parse_qs.py` script.
[Some benchmark results are available in the wiki.](https://github.com/JustinTArthur/jta.qsutil/wiki/Benchmarks)

### [urllib.parse](https://docs.python.org/3/library/urllib.parse.html)
Python standard library API for basic querystring parsing. Does not process
sequence or sub-mapping hints. Is fast. Used by this project.

### [querystring](https://pypi.org/project/querystring/)
Python port of node.js' querystring module. Faster than jta.qsutil.parse,
but doesn't interpret sequence or sub-mapping hints. Doesn't work in Python 3.

### [querystring-parser](https://github.com/bernii/querystring-parser)
Parser that understands sub-mapping hints but not `[]` sequence hints. Doesn't
handle single/blank values.

### [Django QueryDict](https://docs.djangoproject.com/en/2.0/ref/request-response/#querydict-objects)
Robust handling of many edge scenarios like user agent quirks. Slow. Doesn't
process sequence or sub-mapping hints.
