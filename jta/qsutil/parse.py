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

_match_name_format = re.compile(NAME_PATTERN).match
_parse_path_elements = re.compile(PATH_ELEMENTS_PATTERN).findall


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
