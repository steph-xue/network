from datetime import datetime, timezone

from django.core.management.base import BaseCommand

from network.models import Dislike, Follow, Like, Post, User

# Usernames and emails for all demo accounts
DEMO_USERS = {
    "Steph": "steph@mail.com",
    "Alysha": "alysha@mail.com",
    "Cayden": "cayden@mail.com",
    "Michelle": "michelle@mail.com",
}

# Shared login password for all the demo accounts above
DEMO_PASSWORD = "password123"

# Each entry creates one post for the given author, along with the reactions
# it received from other demo users, ordered from the oldest post to the newest
DEMO_POSTS = [
    {
        "author": "Michelle",
        "content": "Hello there!",
        "posted_at": "2024-05-31 21:34:07",
        "likes": ["Steph", "Alysha", "Cayden"],
        "dislikes": [],
    },
    {
        "author": "Alysha",
        "content": "I just adopted a new cat today! She is so cute!",
        "posted_at": "2024-05-31 21:34:52",
        "likes": ["Michelle"],
        "dislikes": [],
    },
    {
        "author": "Cayden",
        "content": "Check out my new vlog if you're looking for some good tips on productivity! youtu.be/aZOrmt7DVk0",
        "posted_at": "2024-05-31 21:42:00",
        "likes": ["Steph", "Alysha"],
        "dislikes": [],
    },
    {
        "author": "Steph",
        "content": "Starting my day off with a matcha latte! Excited to relax this weekend and unwind with a book!",
        "posted_at": "2024-05-31 21:44:42",
        "likes": [],
        "dislikes": ["Cayden"],
    },
    {
        "author": "Michelle",
        "content": "This week has been very productive but I am so glad it is finally Friday! How's your week going?",
        "posted_at": "2024-05-31 21:46:25",
        "likes": ["Alysha"],
        "dislikes": ["Steph"],
    },
    {
        "author": "Cayden",
        "content": "A love a combination of notion, google calendar, and pen and paper :)",
        "posted_at": "2024-05-31 21:47:08",
        "likes": ["Michelle"],
        "dislikes": ["Steph"],
    },
    {
        "author": "Alysha",
        "content": "My cat has been the sweetest, she loves to cuddle and nap in the sun!",
        "posted_at": "2024-05-31 21:47:44",
        "likes": ["Steph", "Cayden"],
        "dislikes": [],
    },
    {
        "author": "Steph",
        "content": "Cherishing every moment with my wonderful friends and family!",
        "posted_at": "2024-05-31 21:48:34",
        "likes": ["Michelle"],
        "dislikes": ["Alysha"],
    },
    {
        "author": "Michelle",
        "content": "A clean space helps to form a clean mind!",
        "posted_at": "2024-05-31 21:49:14",
        "likes": [],
        "dislikes": ["Steph"],
    },
    {
        "author": "Cayden",
        "content": "What is your favourite productivity tool to use?",
        "posted_at": "2024-05-31 21:50:00",
        "likes": ["Steph", "Alysha"],
        "dislikes": [],
    },
    {
        "author": "Steph",
        "content": "Looking for some cozy inspo and tips on how to improve productivity!",
        "posted_at": "2024-05-31 21:52:07",
        "likes": ["Michelle", "Cayden"],
        "dislikes": [],
    },
    {
        "author": "Steph",
        "content": "Working on prioritizing authenticity, happiness and fulfillment over perfection:)",
        "posted_at": "2024-05-31 21:52:34",
        "likes": [],
        "dislikes": ["Michelle", "Alysha"],
    },
    {
        "author": "Michelle",
        "content": "Just got a new wide screen curved monitor for my desk setup, excited to decorate my new office!",
        "posted_at": "2024-05-31 21:53:36",
        "likes": ["Steph", "Alysha", "Cayden"],
        "dislikes": [],
    },
    {
        "author": "Cayden",
        "content": "Check out my new vlog if you're looking for some good tips on productivity! youtu.be/aZOrmt7DVk0",
        "posted_at": "2024-05-31 21:54:49",
        "likes": [],
        "dislikes": [],
    },
    {
        "author": "Michelle",
        "content": "This week has been very productive but I am so glad it is finally Friday! How's your week going?",
        "posted_at": "2024-05-31 21:55:03",
        "likes": ["Steph", "Alysha"],
        "dislikes": [],
    },
    {
        "author": "Steph",
        "content": "Starting my day off with a matcha latte! Excited to relax this weekend and unwind with a book!",
        "posted_at": "2024-05-31 21:55:17",
        "likes": [],
        "dislikes": ["Michelle", "Cayden"],
    },
    {
        "author": "Alysha",
        "content": "Have been buying my new cat all sorts of new toys and snacks, she seems to love them all!",
        "posted_at": "2024-05-31 21:56:15",
        "likes": ["Steph", "Michelle", "Cayden"],
        "dislikes": [],
    },
    {
        "author": "Cayden",
        "content": "A love a combination of notion, google calendar, and pen and paper :)",
        "posted_at": "2024-05-31 21:56:32",
        "likes": [],
        "dislikes": ["Steph"],
    },
    {
        "author": "Steph",
        "content": "Cherishing every moment with my wonderful friends and family!",
        "posted_at": "2024-05-31 21:56:55",
        "likes": [],
        "dislikes": ["Michelle"],
    },
    {
        "author": "Cayden",
        "content": "What is your favourite productivity tool to use?",
        "posted_at": "2024-05-31 21:57:11",
        "likes": ["Michelle", "Steph"],
        "dislikes": ["Alysha"],
    },
    {
        "author": "Michelle",
        "content": "A clean space helps to form a clean mind!",
        "posted_at": "2024-05-31 21:57:26",
        "likes": ["Alysha", "Cayden"],
        "dislikes": [],
    },
]


# Seeds the database with demo users, posts, follows, likes, and dislikes
class Command(BaseCommand):
    help = "Seeds the database with demo users, posts, follows, likes, and dislikes for local development/testing."

    # Adds the --flush flag for clearing existing demo data before reseeding
    def add_arguments(self, parser):
        parser.add_argument(
            "--flush",
            action="store_true",
            help="Delete existing demo posts (from the demo users) before reseeding.",
        )

    # Creates the demo users, has every demo user follow every other demo user,
    # then seeds their posts, likes, and dislikes unless they already exist
    def handle(self, *args, **options):
        users = {}
        for username, email in DEMO_USERS.items():
            user, created = User.objects.get_or_create(
                username=username, defaults={"email": email}
            )
            if created:
                user.set_password(DEMO_PASSWORD)
                user.save()
                self.stdout.write(f"Created user {username}")
            users[username] = user

        for follower in users.values():
            for following in users.values():
                if follower != following:
                    Follow.objects.get_or_create(
                        user_follower=follower, user_following=following
                    )

        if options["flush"]:
            deleted, _ = Post.objects.filter(user__in=users.values()).delete()
            self.stdout.write(f"Deleted {deleted} existing demo post(s) and their reactions")

        if Post.objects.filter(user__in=users.values()).exists():
            self.stdout.write(
                self.style.WARNING(
                    "Demo posts already exist, skipping. Re-run with --flush to reseed."
                )
            )
        else:
            for entry in DEMO_POSTS:
                post = Post.objects.create(
                    user=users[entry["author"]], content=entry["content"]
                )
                post.date_time = datetime.strptime(
                    entry["posted_at"], "%Y-%m-%d %H:%M:%S"
                ).replace(tzinfo=timezone.utc)
                post.save()

                for username in entry["likes"]:
                    Like.objects.create(user=users[username], post=post)
                for username in entry["dislikes"]:
                    Dislike.objects.create(user=users[username], post=post)

            self.stdout.write(f"Created {len(DEMO_POSTS)} demo post(s)")

        self.stdout.write(self.style.SUCCESS("Done."))
        self.stdout.write(f"Demo accounts (password: {DEMO_PASSWORD}):")
        for username in DEMO_USERS:
            self.stdout.write(f"  {username}")
