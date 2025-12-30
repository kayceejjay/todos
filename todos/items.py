from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    url_for,
)

from todos.database import get_db

bp = Blueprint("items", __name__)

@bp.route("/create", methods=("GET", "POST"))
def create():
    item = ""
    if request.method == "POST":
        user = request.form["user"] or "Anonymous"
        item = request.form["item"]
        priority = request.form["priority"]
        # return user
        # return item
        
    if item:
        db = get_db()
        db.execute(
            "INSERT INTO items (user, item, priority) VALUES (?,?,?)",
            (user, item),
        )
        db.commit()
        return redirect(url_for("items.items"))
        
    return render_template("items/create.html")

@bp.route("/items")
def items():
    db = get_db()
    items = db.execute(
        "SELECT user, item, created FROM items ORDER BY created DESC"
    ).fetchall()
    return render_template("items/items.html", items=items)
    
# Blueprint