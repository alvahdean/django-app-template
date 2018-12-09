#from django.test import TestCase

# from collection.factories import (
#     UserFactory,
#     PostFactory,
#     VoteFactory,
#     CommentFactory,
# )


# class ApileSeedTests(TestCase):
#     def setUp(self):
#         self.author = UserFactory()
#         self.post = PostFactory(author=self.author)
#         self.url = self.reverse('library:book_borrow_list',
#                                 user_id=self.user.id)

#     def seed_data(self):
#         user_count=User.objects.all().Count()
#         books = BookFactory.create_batch(5, library=self.library)

#         for book in books:
#             BookBorrowFactory(user=self.user, book=book)

#         response = self.get(self.url)

#         self.assertEqual(200, response.status_code)
#         for book in books:
#             self.assertContains(response, book.title)

#     def test_with_several_books_borrowed_by_one_user(self):
#         books = BookFactory.create_batch(5, library=self.library)

#         for book in books:
#             BookBorrowFactory(user=self.user, book=book)

#         response = self.get(self.url)

#         self.assertEqual(200, response.status_code)
#         for book in books:
#             self.assertContains(response, book.title)

#     def test_with_several_books_borrowed_by_one_user_and_another_user(self):
#         another_user = UserFactory()

#         user1_books = BookFactory.create_batch(5, library=self.library)
#         user2_books = BookFactory.create_batch(5, library=self.library)

#         for book in user1_books:
#             BookBorrowFactory(user=self.user, book=book)

#         for book in user2_books:
#             BookBorrowFactory(user=another_user, book=book)

#         response = self.get(self.url)

#         self.assertEqual(200, response.status_code)
#         for book in user1_books:
#             self.assertContains(response, book.title)
#         for book in user2_books:
#             self.assertNotContains(response, book.title)
