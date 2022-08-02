from app.models import db, User, Post, comments


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        full_name='Demo User', email='demo@aa.io', username='Demo',  profile_pic= '',password='password')
    marnie = User(
        username='marnie', email='marnie@aa.io', password='password')
    bobbie = User(
        username='bobbie', email='bobbie@aa.io', password='password')

    post1 = Post( img_url="https://houseofyumm.com/wp-content/uploads/2021/01/Birria-de-Res-9.jpg", caption="Had these delicious birria tacos at Los 2 Brothers. Defititely recommend!", user_id=1)
    post2 = Post( img_url="https://preview.redd.it/zg28x4wewll11.jpg?auto=webp&s=22dbcb27dfa245c9c4a40e814870cdc529701dee", caption="Amazing night out at Sushi Saito. It was incredible watching Chef Takashi Saito prepare our courses in front of us!", user_id= 2)
    post3 = Post( img_url="https://static.wixstatic.com/media/5eff48_3a2809aa29a246c1a46a7dad27028386~mv2.jpg/v1/fit/w_960%2Ch_960%2Cal_c%2Cq_80/file.jpg", caption="Breakfast in Egypt", user_id= 3)

    comment1 = Comment(comment_text="Those tacos are so good!", user_id=2, post_id=1)
    comment2 = Comment(comment_text="How long to get a reservation? I heard it was over two years!!", user_id=1, post_id=2)
    comment3 = Comment(comment_text="Where is this?", user_id=1, post_id=3)

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    db.session.add(comment1)
    db.session.add(comment2)
    db.session.add(comment3)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()