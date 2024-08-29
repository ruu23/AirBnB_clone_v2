#!/usr/bin/python3

import unittest
from unittest.mock import patch
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_init(self):
        instance = BaseModel()
        self.assertIsNotNone(instance.id)
        self.assertTrue(isinstance(instance.id, str))
        self.assertTrue(isinstance(instance.created_at, datetime))
        self.assertTrue(isinstance(instance.update_at, datetime))
        self.assertAlmostEqual(instance.created_at.timestamp(), datetime.now().timestamp(), delta=1)
        self.assertAlmostEqual(instance.update_at.timestamp(), datetime.now().timestamp(), delta=1)

    def test_save(self):
        instance = BaseModel()
        old_updated_at = instance.update_at
        instance.save()
        self.assertNotEqual(old_updated_at, instance.update_at)
        self.assertAlmostEqual(instance.update_at.timestamp(), datetime.now().timestamp(), delta=1)

    def test_to_dict(self):
        instance = BaseModel()
        instance_dict = instance.to_dict()

        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertEqual(instance_dict['id'], instance.id)
        self.assertTrue("created_at" in instance_dict)
        self.assertTrue("update_at" in instance_dict)

        try:
            datetime.strptime(instance_dict["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            datetime.strptime(instance_dict["update_at"], "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            self.fail("Incorrect date format in to_dict output")

    def test_str_method(self):
        instance = BaseModel()
        expected_str_format = "[BaseModel] ({}) {}".format(instance.id, instance.__dict__)
        self.assertEqual(str(instance), expected_str_format)

    @patch("models.base_model.datetime")
    def test_mocked_time_in_init(self, mocked_datetime):
        mocked_datetime.now.return_value = datetime(2020, 1, 1)
        instance = BaseModel()
        self.assertEqual(instance.created_at, datetime(2020, 1, 1))
        self.assertEqual(instance.update_at, datetime(2020, 1, 1))

if __name__ == '__main__':
    unittest.main()

