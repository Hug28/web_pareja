from flask import Flask,render_template,redirect,url_for,request
from db.get_connect import get_conn

app=Flask(__name__)

@app.route("/")
def index():
    return redirect("/index")


#MOSTRAR DATOS DE LA BD
@app.route("/index")
def home():
    conn=get_conn()
    cur=conn.cursor()
    cur.execute("SELECT * FROM pareja")
    resultado=cur.fetchall()
    return render_template("home.html",resultado=resultado)



#INSERTAR DATOS EN LA BD
@app.route("/formulario" ,methods=["POST"])
def formulario():
    if request.method=="POST":
        nombre=request.form["nombre"]
        texto=request.form["texto"]

        try:
            conn=get_conn()
            cur=conn.cursor()
            cur.execute("INSERT INTO pareja(name,recuerdo) VALUES (%s,%s)",(nombre,texto))
            conn.commit()
            return redirect("/")
        except Exception as e:
            print(e)
            return "Ocurrio un error para insertar datos"


#ELIMINAR UN REGISTRO DE LA BD
@app.route("/eliminar/<int:id>")
def eliminar(id):
    try:
        conn=get_conn()
        cur=conn.cursor()
        cur.execute("DELETE  FROM pareja WHERE id=%s",(id,))
        conn.commit()
        return redirect("/")
    except Exception as e:
        print (e)
        return ("Ocurrio un error en la eliminacion.")

#EDITAR
@app.route("/editar/<int:id>")
def editar(id):
    try:
        conn=get_conn()
        cur=conn.cursor()
        cur.execute("SELECT * FROM pareja WHERE id=%s",(id,))
        resu=cur.fetchone()
        return render_template("editar.html",resu=resu)
    except Exception as e:
        print(e)
        return "Ocurrio un error editando los datos"

@app.route("/formulario/editar/<int:id>",methods=["POST"])
def editar1(id):
    if request.method=="POST":
        nombre=request.form["nombre"]
        texto=request.form["texto"]
        try:
            conn=get_conn()
            cur=conn.cursor()
            cur.execute("update pareja SET name=%s,recuerdo=%s  WHERE id=%s",(nombre,texto,id),)
            conn.commit()
            return redirect("/")
        except Exception as e:
            print (e)
            return ("Ocurrio un error en la eliminacion.")