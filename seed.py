"""Seed the database using the ORM only — no SQL anywhere.

Run with:  pipenv run python seed.py
"""
from app import create_app, db
from app.models import User, Post

app = create_app("development")

with app.app_context():
    # wipe previous seed data so the script is safe to re-run
    Post.query.delete()
    User.query.delete()
    db.session.commit()

    ian = User(
        username="ian",
        email="ian@iancreative.co.ke",
        bio="Founder, IAN Creative. Frontend dev, part-time jetski philosopher.",
    )
    ian.password = "correct-horse-battery"

    wanjiku = User(
        username="wanjiku",
        email="wanjiku@example.com",
        bio="Backend engineer. Believes every bug is a feature with bad PR.",
    )
    wanjiku.password = "s3cure-enough!"

    otieno = User(
        username="otieno",
        email="otieno@example.com",
        bio="Data nerd. Will normalize your tables and your expectations.",
    )
    otieno.password = "third-normal-form"

    posts = [
        Post(title="Why Flask factories beat one-file apps", body="Once you have blueprints, config classes and extensions, create_app() keeps the wiring in one place and makes testing trivial.", author=ian),
        Post(title="Shipping MKONO", body="Built a hand-gesture showreel with Three.js and MediaPipe. The webcam is the mouse now.", author=ian),
        Post(title="Migrations are save points", body="Every flask db migrate is a checkpoint you can roll back to. Treat your schema like code, because it is.", author=wanjiku),
        Post(title="back_populates vs backref", body="back_populates is explicit on both sides, so future-you can read either model and see the whole relationship.", author=wanjiku),
        Post(title="Indexes are not free", body="They speed up reads and slow down writes. Index what you filter by, not everything you can see.", author=otieno),
    ]

    db.session.add_all([ian, wanjiku, otieno, *posts])
    db.session.commit()

    print(f"Seeded {User.query.count()} users and {Post.query.count()} posts.")
