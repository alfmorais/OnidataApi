import json


def response_body_replace(items):
    """Replace sensitive fields in response to vcr cassettes"""

    def before_record_response(response):
        try:
            body = json.loads(response["body"]["string"])
        except (json.decoder.JSONDecodeError, UnicodeDecodeError):
            return response

        if type(body) is list:
            body_without_sensitive_data = list(
                map(lambda i: _parse_list(i, items), body)
            )
        else:
            body_without_sensitive_data = _replace_values(body, items)

        response["body"]["string"] = json.dumps(body_without_sensitive_data).encode(
            "utf-8"
        )  # noqa E501

        return response

    return before_record_response


def _parse_list(index, items):
    if type(index) is not dict:
        return index
    return _replace_values(index, items)


def _replace_values(body, items):
    for key, value in body.items():
        if type(value) is dict:
            _replace_values(body[key], items)
        if key in items:
            body[key] = items[key]
    return body
