from enums.GlobalEnums import GlobalErrorMessages


class Response:

    def __init__(self, response):
        self.response = response

    def check_status_code(self, expected_code):
        assert self.response.status_code == expected_code, GlobalErrorMessages.WRONG_STATUS_CODE.value

    def validate_body(self, schema):
        pass

    def validate_headers(self, schema):
        pass

    def check_headers(self, expected_header):
        assert expected_header in self.response.headers, GlobalErrorMessages.MISSING_HEADER.value




