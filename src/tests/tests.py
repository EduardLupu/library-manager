import unittest
from src.domain.container import Container
from src.utility.functions import filter_container, gnome_sort


class TestContainer(unittest.TestCase):
    def setUp(self) -> None:
        self.test = Container([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def tearDown(self) -> None:
        pass

    def test_init__no_parameter__success(self):
        self.test = Container()
        self.assertEqual(len(self.test), 0)

    def test_init__list_parameter__success(self):
        self.test = Container([2, 2, 2])
        self.assertEqual(len(self.test), 3)

    def test_len__success(self):
        self.assertEqual(len(self.test), 10)

    def test_setitem__valid_integers__success(self):
        self.test[9] = 5
        self.assertEqual(self.test[9], 5)

    def test_setitem__invalid_key__throw_exception(self):
        with self.assertRaises(IndexError):
            self.test[11] = 5

    def test_getitem__valid_key__success(self):
        item = self.test.__getitem__(5)
        self.assertEqual(item, 6)

    def test_getitem__invalid_key__throw_exception(self):
        with self.assertRaises(IndexError):
            item = self.test.__getitem__(11)

    def test_delitem__valid_key__success(self):
        self.test.__delitem__(4)
        self.assertEqual(len(self.test), 9)

    def test_delitem__invalid_key__throw_exception(self):
        with self.assertRaises(IndexError):
            self.test.__delitem__(11)

    def test_iter__success(self):
        self.test.__iter__()
        self.assertEqual(next(self.test), 1)

    def test_next__success(self):
        self.test.__iter__()
        item = next(self.test)
        self.assertEqual(1, item)

    def test_next__throw_exception_if_out_of_range(self):
        self.test = Container()
        self.test.__iter__()
        with self.assertRaises(StopIteration):
            item = next(self.test)

    def test_append__item__success(self):
        self.test.append(100)
        self.assertEqual(100, self.test[-1])

    def test_remove__item__success(self):
        self.test.remove(4)
        self.assertEqual(len(self.test), 9)

    def test_reverse__item__success(self):
        auxiliary = self.test
        self.test.reverse()
        self.assertEqual(self.test, auxiliary)


class TestGnomeSort(unittest.TestCase):
    def setUp(self) -> None:
        self.test = Container([5, 5, 2, 7, 8, 1, 2, 9, 10, 53, 11])

    def tearDown(self) -> None:
        pass

    def test_gnome_sort_ascending__integers_container__success(self):
        list = [5, 5, 2, 7, 8, 1, 2, 9, 10, 53, 11]
        gnome_sort(self.test, lambda x, y: x >= y)
        list.sort()
        self.test.__iter__()
        for element in range(len(list)):
            self.assertEqual(list[element], self.test[element])

    def test_gnome_sort_descending__integers_container__success(self):
        list = [5, 5, 2, 7, 8, 1, 2, 9, 10, 53, 11]
        gnome_sort(self.test, lambda x, y: x >= y, True)
        list.sort(reverse=True)
        self.test.__iter__()
        for element in range(len(list)):
            self.assertEqual(list[element], self.test[element])


class TestFilterContainer(unittest.TestCase):
    def setUp(self) -> None:
        self.test = Container([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def tearDown(self) -> None:
        pass

    def test_filter_container__integers_container__succes(self):
        self.test = filter_container(self.test, lambda x: x != 1)
        self.assertEqual(len(self.test), 9)


if __name__ == '__main__':
    unittest.main()
