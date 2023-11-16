from unittest import TestCase, main

from WorkshopDictionary.hashtable import HashTable


class TestHashTable(TestCase):
    def setUp(self):
        self.table = HashTable()

    def test_init(self):
        self.assertEqual(4, self.table.max_length)
        self.assertEqual([None, None, None, None], self.table._HashTable__keys)
        self.assertEqual([None, None, None, None], self.table._HashTable__values)

    def test_set_items_if_key_does_not_exist(self):
        self.assertNotIn("test", self.table._HashTable__keys)
        self.assertNotIn(8, self.table._HashTable__values)

        self.table["test"] = 8

        self.assertIn("test", self.table._HashTable__keys)
        self.assertIn(8, self.table._HashTable__values)

    def test_set_items_if_key_does_exist(self):
        self.table["test"] = 8
        self.assertIn("test", self.table._HashTable__keys)
        self.assertIn(8, self.table._HashTable__values)
        self.assertNotIn("exist key", self.table._HashTable__values)

        self.table["test"] = "exist key"
        self.assertIn("exist key", self.table._HashTable__values)

    def test_set_items_when_reach_end_of_list(self):
        self.table["c"] = "test"
        self.assertIn("c", self.table._HashTable__keys)
        self.assertIn("test", self.table._HashTable__values)

        self.table["d"] = "check"
        self.assertIn("d", self.table._HashTable__keys)
        self.assertIn("check", self.table._HashTable__values)

    def test_set_items_when_reach_last_index(self):
        self.assertNotIn("c", self.table._HashTable__keys)
        self.assertNotIn("test", self.table._HashTable__values)
        self.assertNotIn("d", self.table._HashTable__keys)
        self.assertNotIn("check", self.table._HashTable__values)
        self.assertNotIn("e", self.table._HashTable__keys)
        self.assertNotIn("Peter", self.table._HashTable__values)
        self.assertNotIn("f", self.table._HashTable__keys)
        self.assertNotIn(9, self.table._HashTable__values)
        self.assertNotIn("g", self.table._HashTable__keys)
        self.assertNotIn("extended", self.table._HashTable__values)
        self.table["c"] = "test"
        self.table["d"] = "check"
        self.table["e"] = "Peter"
        self.table["f"] = 9
        self.table["g"] = "extended"
        self.assertIn("c", self.table._HashTable__keys)
        self.assertIn("test", self.table._HashTable__values)
        self.assertIn("d", self.table._HashTable__keys)
        self.assertIn("check", self.table._HashTable__values)
        self.assertIn("e", self.table._HashTable__keys)
        self.assertIn("Peter", self.table._HashTable__values)
        self.assertIn("f", self.table._HashTable__keys)
        self.assertIn(9, self.table._HashTable__values)
        self.assertIn("g", self.table._HashTable__keys)
        self.assertIn("extended", self.table._HashTable__values)

    def test_resize(self):
        self.assertEqual(4, self.table.max_length)
        self.table["c"] = "test"
        self.table["d"] = "check"
        self.table["e"] = "Peter"
        self.table["f"] = 9
        self.table["g"] = "extended"
        self.assertEqual(8, self.table.max_length)

    def test_dict_len(self):
        self.table["c"] = "test"
        self.table["d"] = "check"
        self.table["e"] = "Peter"
        self.assertEqual(3, len(self.table))

    def test_dict_repr(self):
        self.table["c"] = "test"
        self.table["d"] = "check"
        self.table["e"] = "Peter"
        self.assertEqual('{"d": "check", "e": "Peter", "c": "test"}', repr(self.table))

    def test_get_existing_item(self):
        self.table["c"] = "test"
        self.assertIn("c", self.table._HashTable__keys)
        self.assertIn("test", self.table._HashTable__values)
        self.assertEqual("test", self.table.get("c"))

    def test_get_item_not_existing_item(self):
        self.table["c"] = "test"
        self.assertNotIn("d", self.table._HashTable__keys)
        self.assertNotIn("check", self.table._HashTable__values)
        with self.assertRaises(KeyError) as ex:
            self.table["d"]
        self.assertEqual("'No such key'", str(ex.exception))

    def test_get_not_existing_item(self):
        self.table["c"] = "test"
        self.assertNotIn("d", self.table._HashTable__keys)
        self.assertNotIn("check", self.table._HashTable__values)
        self.assertEqual(None, self.table.get("d"))

    def test_add_method(self):
        self.assertNotIn("test", self.table._HashTable__keys)
        self.assertNotIn(8, self.table._HashTable__values)

        self.table["test"] = 8

        self.assertIn("test", self.table._HashTable__keys)
        self.assertIn(8, self.table._HashTable__values)

    def test_keys_method(self):
        self.assertNotIn("c", self.table._HashTable__keys)
        self.assertNotIn("test", self.table._HashTable__values)
        self.assertNotIn("d", self.table._HashTable__keys)
        self.assertNotIn("check", self.table._HashTable__values)
        self.table["c"] = "test"
        self.table["d"] = "check"
        self.assertEqual(["d", "c"], self.table.keys())

    def test_values_method(self):
        self.assertNotIn("c", self.table._HashTable__keys)
        self.assertNotIn("test", self.table._HashTable__values)
        self.assertNotIn("d", self.table._HashTable__keys)
        self.assertNotIn("check", self.table._HashTable__values)
        self.table["c"] = "test"
        self.table["d"] = "check"
        self.assertEqual(["check", "test"], self.table.values())

    def test_items_method(self):
        self.assertNotIn("c", self.table._HashTable__keys)
        self.assertNotIn("test", self.table._HashTable__values)
        self.assertNotIn("d", self.table._HashTable__keys)
        self.assertNotIn("check", self.table._HashTable__values)
        self.table["c"] = "test"
        self.table["d"] = "check"

        self.assertEqual([("d", "check"), ("c", "test")], self.table.item())

    def test_pop_method_existing_key(self):
        self.assertNotIn("c", self.table._HashTable__keys)
        self.assertNotIn("test", self.table._HashTable__values)
        self.assertNotIn("d", self.table._HashTable__keys)
        self.assertNotIn("check", self.table._HashTable__values)
        self.table["c"] = "test"
        self.table["d"] = "check"
        self.table.pop("d")
        self.assertNotIn("d", self.table._HashTable__keys)
        self.assertNotIn("check", self.table._HashTable__values)

    def test_pop_method_not_existing_key(self):
        self.assertNotIn("a", self.table._HashTable__keys)
        with self.assertRaises(KeyError) as ex:
            self.table.pop("a")
        self.assertEqual("'Invalid key'", str(ex.exception))

    def test_copy_method(self):
        self.assertNotIn("c", self.table._HashTable__keys)
        self.assertNotIn("test", self.table._HashTable__values)
        self.assertNotIn("d", self.table._HashTable__keys)
        self.assertNotIn("check", self.table._HashTable__values)
        self.table["c"] = "test"
        self.table["d"] = "check"
        test_table = self.table.copy()
        self.assertEqual('{"d": "check", "c": "test"}', repr(test_table))

    def test_clear_method(self):
        self.assertNotIn("c", self.table._HashTable__keys)
        self.assertNotIn("test", self.table._HashTable__values)
        self.assertNotIn("d", self.table._HashTable__keys)
        self.assertNotIn("check", self.table._HashTable__values)
        self.table["c"] = "test"
        self.table["d"] = "check"
        self.assertIn("c", self.table._HashTable__keys)
        self.assertIn("test", self.table._HashTable__values)
        self.assertIn("d", self.table._HashTable__keys)
        self.assertIn("check", self.table._HashTable__values)
        self.table.clear()
        self.assertEqual("{}", repr(self.table))




if __name__ == "__main__":
    main()
