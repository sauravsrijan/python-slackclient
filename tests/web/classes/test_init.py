import unittest

from slack.web.classes import extract_json
from slack.web.classes.objects import PlainTextObject, MarkdownTextObject


class TestInit(unittest.TestCase):
    def test_from_list_of_json_objects(self):
        json_objects = [
            PlainTextObject(text="foo"),
            MarkdownTextObject(text="bar"),
        ]
        output = extract_json(json_objects)
        expected = {"result": [
            {"type": "plain_text", "text": "foo", "emoji": True},
            {"type": "mrkdwn", "text": "bar", "verbatim": False},
        ]}
        self.assertDictEqual(expected, {"result": output})

    def test_from_single_json_object(self):
        single_json_object = PlainTextObject(text="foo")
        output = extract_json(single_json_object)
        expected = {"result": {"type": "plain_text", "text": "foo", "emoji": True}}
        self.assertDictEqual(expected, {"result": output})
