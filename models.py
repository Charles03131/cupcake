"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy(session_options={"expire_on_commit": False})

DEFAULT_IMG = "https://tinyurl.com/demo-cupcake"

class Cupcake(db.Model):
    """cupcakes to get"""
    __tablename__="cupcakes"

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    flavor=db.Column(db.Text, nullable=False)
    size=db.Column(db.Text,nullable=False)
    rating=db.Column(db.Float,nullable=False)
    image=db.Column(db.Text,nullable=False,default=DEFAULT_IMG)


    def serialize(self):
        """Serialize a cupcake SQLAlchemy obj to dictionary."""

        return {
            "id":self.id,
            "flavor":self.flavor,
            "size":self.size,
            "rating":self.rating,
            "image":self.image
        }

def connect_db(app):
    with app.app_context():
        db.app=app
        db.init_app(app)


