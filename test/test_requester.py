from unittest import TestCase

from Requester import request_stock


class TestRequester(TestCase):
    request_stock("nothing", "MSFT")
    pass
