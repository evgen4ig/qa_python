from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    def setUp(self):
        self.books_collector = BooksCollector()

    import unittest
    from main import BooksCollector

    class TestBooksCollector(unittest.TestCase):
        def setUp(self):
            self.books_collector = BooksCollector()

        def test_add_new_book(self):
            self.books_collector.add_new_book("Harry Potter")
            self.assertIn("Harry Potter", self.books_collector.books_genre)


        def test_get_book_genre(self):
            self.books_collector.add_new_book("Harry Potter")
            self.books_collector.set_book_genre("Harry Potter", "Фантастика")
            self.assertEqual(self.books_collector.get_book_genre("Harry Potter"), "Фантастика")



        def test_get_books_with_specific_genre(self):
            self.books_collector.add_new_book("Harry Potter")
            self.books_collector.set_book_genre("Harry Potter", "Фантастика")
            self.books_collector.add_new_book("Властелин колец")
            self.books_collector.set_book_genre("Властелин колец", "Фантастика")
            self.books_collector.add_new_book("Шерлок Холмс")
            self.books_collector.set_book_genre("Шерлок Холмс", "Детективы")
            self.assertCountEqual(
                self.books_collector.get_books_with_specific_genre("Фантастика"),
                ["Harry Potter", "Властелин колец"]
            )

        def test_get_book_genre_when_book_exists(self):
            # Добавляем книгу с жанром
            self.books_collector.add_new_book("Harry Potter")
            self.books_collector.set_book_genre("Harry Potter", "Фантастика")
            self.assertEqual(self.books_collector.get_book_genre("Harry Potter"), "Фантастика")

        def test_get_book_genre_when_book_does_not_exist(self):
            # Проверяем, что функция возвращает None, если книга не найдена
            self.assertIsNone(self.books_collector.get_book_genre("Unknown Book"))
        def test_get_books_genre(self):
            self.books_collector.add_new_book("Harry Potter")
            self.books_collector.set_book_genre("Harry Potter", "Фантастика")
            self.books_collector.add_new_book("Властелин колец")
            self.books_collector.set_book_genre("Властелин колец", "Фантастика")
            self.books_collector.add_new_book("Шерлок Холмс")
            self.books_collector.set_book_genre("Шерлок Холмс", "Детективы")
            actual_genres = self.books_collector.get_books_genre()
            expected_genres = {
                "Harry Potter": "Фантастика",
                "Властелин колец": "Фантастика",
                "Шерлок Холмс": "Детективы"
            }
            self.assertDictEqual(actual_genres, expected_genres)

        def test_get_books_for_children(self):

            books_for_children = self.books_collector.get_books_for_children()

            # Проверка, что в списке только книги без возрастных ограничений
            self.assertFalse(
                any(book in books_for_children for book in ["Harry Potter", "Властелин колец", "Шерлок Холмс"]))

        def test_add_new_book(self):
            """Проверка добавления новой книги в коллекцию."""
            self.books_collector.add_new_book('Новая книга')
            self.assertIn('Новая книга', self.books_collector.books_genre)

        def test_delete_book_from_favorites(self):
            self.books_collector.add_book_in_favorites("Harry Potter")
            self.books_collector.delete_book_from_favorites("Harry Potter")
            self.assertFalse(self.books_collector.favorites)

        def test_get_list_of_favorites_books_empty(self):
            """Проверка, что список избранных книг пуст после создания объекта."""
            self.assertEqual(self.books_collector.get_list_of_favorites_books(), [])


    if __name__ == '__main__':
        unittest.main()
