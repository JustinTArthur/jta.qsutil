from jta.qsutil.parse import parse_qs


def test_natural_array():
    result = parse_qs('a[]=this&a[]=that')
    assert result == {'a': ['this', 'that']}


def test_array_brackets():
    result = parse_qs('a[]=this&a[]=that')
    assert result == {'a': ['this', 'that']}

    result = parse_qs('a[]=this&b=something&a[]=that')
    assert result == {'a': ['this', 'that'], 'b': 'something'}


def test_key_only_items():
    result = parse_qs('a', keep_blank_values=True)
    assert result == {'a': ''}


def test_single_array_item():
    result = parse_qs('a[]=this')
    assert result == {'a': ['this']}

    result = parse_qs('a=this')
    assert result == {'a': 'this'}


def test_associative_array_brackets():
    result = parse_qs('a[b]=this')
    assert result == {'a': {'b': 'this'}}

    result = parse_qs('a[b]=this&a[b]=that')
    assert result == {'a': {'b': ['this', 'that']}}
