from jta.qsutil.parse import parse_qs as jtaqsutil_parse_qs
from querystring import parse_qs as querystring_parse_qs
from querystring_parser.parser import parse as qs_parser_parse
from tabulate import tabulate
from timeit import timeit
import sys
import warnings

warnings.simplefilter('ignore')

sample_querystrings = (
    (
        'key1=val1&key2=val2&key3[a][b][c]=val3&key3[a][b][c]=val4'
        '&key4&key3[a][b][d]=val5&key5[]=val6'
    ),
    'key1=val1&key2=val2',
    'key1=val1&key1=val2',
    'singleSymbol',
    'singleValArray[]=val1',
    'key1[]=val1&key1[]=val2',
    'key1[a][b][c]=val1',
    'key1[a][b][c]=val1&key1[a][b][d]=val2',
    'key1[a][b][]=val1',
)

parser_tests = [
    ('urlparser or urllib.parse', 'stdlib_parse_qs(qs, keep_blank_values=True)'),
    ('jta.qsutil', 'jtaqsutil_parse_qs(qs, keep_blank_values=True)'),
    ('querystring', 'querystring_parse_qs(qs)'),
    ('querystring_parser', 'qs_parser_parse(qs)'),
]

try:
    from urllib.parse import parse_qs as stdlib_parse_qs
except ImportError:
    try:
        from urlparse.urlparse import parse_qs as stdlib_parse_qs
    except ImportError:
        from cgi import parse_qs as stdlib_parse_qs

try:
    from django.conf import settings
    settings.configure()
    from django.http.request import QueryDict as DjQueryDict
except ImportError:
    pass
else:
    parser_tests.append(('Django QueryDict', 'DjQueryDict(qs)'))

py_ver = int(sys.version[0])

for qs in sample_querystrings:
    results = []
    for test_name, test in parser_tests:
        try:
            result = '`{}`'.format(eval(test))
            if py_ver > 2:
                result_time = timeit(test, globals=globals())
            else:
                result_time = timeit(test, 'from __main__ import *')
        except Exception as e:
            result = str(e)
            result_time = None
        row = (test_name, result, result_time)
        results.append(row)

    print('## `{}`'.format(qs))
    print(
        tabulate(
            results,
            headers=(
                'Library',
                'Python {} Result'.format(py_ver),
                'Python {} Time'.format(py_ver)
            ),
            tablefmt='pipe')
    )
    print('\n')
