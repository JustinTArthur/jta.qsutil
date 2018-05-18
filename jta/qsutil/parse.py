import re

try:
    from urllib.parse import parse_qsl
except ImportError:
    try:
        from urlparse.urlparse import parse_qsl
    except ImportError:
        from cgi import parse_qsl
    pass_new_params = False
else:
    pass_new_params = True


NAME_PATTERN = r'([^[\]]+)(?:((?:\[[^[\]]+\])+)?(\[\])?)?$'
PATH_ELEMENTS_PATTERN = r'(?:\[(.+?)\])'
PAIR_DELIMITER = r'&|;'
PAIR_PATTERN = r'([^&;]+)(?:=([^&;]+))?'

_match_name_format = re.compile(NAME_PATTERN).match
_parse_path_elements = re.compile(PATH_ELEMENTS_PATTERN).findall
_split_pairs = re.compile(PAIR_DELIMITER).split
_find_pairs = re.compile(PAIR_PATTERN).findall


def parse_qs(qs, keep_blank_values=False, strict_parsing=False,
             encoding='utf-8', errors='replace'):
    result = {}
    if pass_new_params:
        pairs = parse_qsl(qs, keep_blank_values, strict_parsing,
                          encoding=encoding, errors=errors)
    else:
        pairs = parse_qsl(qs, keep_blank_values, strict_parsing)

    for name, value in pairs:
        name_match = _match_name_format(name)
        if not name_match:
            raise ValueError(
                'Query string attribute in unknown format: %s' % name
            )
        base_name, path_elements, array_hint = name_match.groups()

        if path_elements:
            path_elements = _parse_path_elements(path_elements)
            path = result.setdefault(base_name, {})
            for path_element in path_elements[:-1]:
                path = path.setdefault(path_element, {})
            final_element = path_elements[-1]
        else:
            path = result
            final_element = base_name

        if not isinstance(path, dict):
            raise ValueError(
                "Mismatched type of string and mapping at %s" % name
            )

        if final_element in path:
            existing_value = path[final_element]
            if isinstance(existing_value, list):
                existing_value.append(value)
            else:
                path[final_element] = [existing_value, value]
        else:
            path[final_element] = [value] if array_hint else value

    return result


def parse_qsl(qs, keep_blank_values=False, strict_parsing=False,
              encoding='utf-8', errors='replace'):
    """Parse a query given as a string argument.

        Arguments:

        qs: percent-encoded query string to be parsed

        keep_blank_values: flag indicating whether blank values in
            percent-encoded queries should be treated as blank strings.
            A true value indicates that blanks should be retained as blank
            strings.  The default false value indicates that blank values
            are to be ignored and treated as if they were  not included.

        strict_parsing: flag indicating what to do with parsing errors. If
            false (the default), errors are silently ignored. If true,
            errors raise a ValueError exception.

        encoding and errors: specify how to decode percent-encoded sequences
            into Unicode characters, as accepted by the bytes.decode() method.

        Returns a list, as G-d intended.
    """
    qs, _coerce_result = _coerce_args(qs)
    result = []
    new_result = result.append
    for pair_match in _find_pairs(qs):
        name, value = pair_match.groups()
        if not name and not strict_parsing:
            continue
        if len(nv) != 2:
            if strict_parsing:
                raise ValueError("bad query field: %r" % (pair_match.group(0),))
            # Handle case of a control-name with no equal sign
            if keep_blank_values:
                nv.append('')
            else:
                continue
        if len(nv[1]) or keep_blank_values:
            name = nv[0].replace('+', ' ')
            name = unquote(name, encoding=encoding, errors=errors)
            name = _coerce_result(name)
            value = nv[1].replace('+', ' ')
            value = unquote(value, encoding=encoding, errors=errors)
            value = _coerce_result(value)
            new_result((name, value))
    return r