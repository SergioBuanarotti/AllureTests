from enum import Enum


class GlobalErrorMessages(Enum):

    WRONG_STATUS_CODE = "Status code is not equal to expected."
    WRONG_ELEMENT_COUNT = "Count of elements is not equal to expected."
    MISSING_HEADER = "Expected header absent in the response."
