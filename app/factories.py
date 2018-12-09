# import factory
# from faker import Factory, internet

# from django.contrib.auth.models import User
# from django.utils import timezone
# from collection.models import Post, Comment, Vote

# faker = Factory.create()


# class UserFactory(factory.DjangoModelFactory):
#     class Meta:
#         model = User

#     username = factory.LazyAttribute(lambda _: faker.name())
#     email = factory.LazyAttribute(lambda _: faker.email())
#     password = factory.LazyAttribute(lambda _: faker.password())


# class PostFactory(factory.DjangoModelFactory):
#     class Meta:
#         model = Post

#     title = factory.LazyAttribute(lambda _: faker.text())
#     author = factory.SubFactory(UserFactory)
#     text=factory.LazyAttribute(lambda _: faker.text())
#     url = factory.LazyAttribute(lambda _: faker.internet.url())

# class CommentFactory(factory.DjangoModelFactory):
#     class Meta:
#         model = Comment

#     post = factory.SubFactory(PostFactory)
#     user = factory.SubFactory(UserFactory)
#     contents = factory.LazyAttribute(lambda _: faker.text())

# class VoteFactory(factory.DjangoModelFactory):
#     class Meta:
#         model = Vote

#     post = factory.SubFactory(PostFactory)
#     user = factory.SubFactory(UserFactory)
