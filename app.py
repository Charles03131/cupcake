"""Flask app for Cupcakes"""

from flask import Flask,request,jsonify,render_template
from flask_cors import CORS

from models import db, connect_db, Cupcake


app=Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI']="postgresql:///cupcakes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_ECHO']=True
app.config['SECRET_KEY'] = 'secretsecret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


with app.app_context():
    connect_db(app)
    db.create_all()

@app.route("/")
def home():
    """render homepage"""
    cupcakes=Cupcake.query.all()
    return render_template("home.html",cupcakes=cupcakes)

@app.route("/api/cupcakes",methods=["GET"])
def show_cupcakes():
    """show list of cupcakes (returns json data of cupcake object"""

    cupcakes=[cupcake.serialize() for cupcake in Cupcake.query.all()]
    
    return jsonify(cupcakes=cupcakes)


@app.route("/api/cupcakes",methods=['POST'])
def add_cupcake():
  

    new_cupcake=Cupcake(id=request.json['id'],flavor=request.json['flavor'],size=request.json['size'],rating=request.json['rating'],image=request.json['image'])
                   
    with app.app_context():
        db.session.add(new_cupcake)
        db.session.commit()

        return(jsonify(new_cupcake=new_cupcake.serialize()),201)


@app.route('/api/cupcakes/<int:cupcake_id>')
def get_info(cupcake_id):
    cupcake=Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<int:cupcake_id>',methods=["PATCH","GET"])
def update_cupcake(cupcake_id):

    cupcakes=Cupcake.query.get_or_404(cupcake_id)
    
   #cupcakes.id=request.json['id'],
    cupcakes.flavor=request.json['flavor'],
    cupcakes.size=request.json['size'],
    cupcakes.rating=request.json['rating'],
    cupcakes.image=request.json['image']

    with app.app_context():
        db.session.commit()
    
        return jsonify(cupcakes=cupcakes.serialize())



@app.route('/api/cupcakes/<int:cupcake_id>',methods=["DELETE"])
def delete_cupcake(cupcake_id):
    cupcake=Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="deleted")




#git remote add origin git@github.com:Charles03131/24.3-Restful-JSON-API.git