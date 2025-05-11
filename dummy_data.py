
import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
import random
from faker import Faker
from blog.models import Post,Category,Review
from django.contrib.auth.models import User




def seed_category(n):
    fake=Faker()
    for _ in range(n):
        Category.objects.create(
            name=fake.name()

        )

def seed_post(n):
    fake=Faker()
    images=['1.jpeg','2.jpeg','3.jpeg','4.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg']
    category=Category.objects.all()
    users=User.objects.all()
    for _ in range(n):
        Post.objects.create(
            user=users[random.randint(0,len(users)-1)],
            title=fake.name(),
            image=f'photo_post/{images[random.randint(0,8)]}',
            content=fake.text(max_nb_chars=4000),
            category=category[random.randint(0,len(category)-1)]


        )
def seed_review(n):
    users=User.objects.all()
    posts=Post.objects.all()
    fake=Faker()
    for _ in range(n):
        Review.objects.create(
            user=users[random.randint(0,len(users)-1)],
            post=posts[random.randint(0,len(posts)-1)],
            content=fake.text(max_nb_chars=1200),
            rate=random.randint(1,6)
        )
# seed_category(50)
# seed_post(250)
seed_review(150)

