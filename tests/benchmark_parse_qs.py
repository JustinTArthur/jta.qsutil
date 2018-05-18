from urllib.parse import parse_qs as stdlib_parse_qs
from jta.qsutil.parse import parse_qs as jtaqsutil_parse_qs
from querystring import parse_qs as querystring_parse_qs
from querystring_parser.parser import parse as qs_parser_parse

from tabulate import tabulate
from timeit import timeit

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

parser_tests = (
    ("urllib.parse", "stdlib_parse_qs(qs, keep_blank_values=True)"),
    ("jta.qsutil", "jtaqsutil_parse_qs(qs, keep_blank_values=True)"),
    ("querystring", "querystring_parse_qs(qs)"),
    ("querystring_parser", "qs_parser_parse(qs)")
)

for qs in sample_querystrings:
    results = []
    for test_name, test in parser_tests:
        try:
            result = eval(test)
            result_time = timeit(test, globals=globals())
        except Exception as e:
            result = str(e)
            result_time = None
        row = (test_name, result, result_time)
        results.append(row)

    print(tabulate(results, headers=('', qs, '')))
    print('\n')
