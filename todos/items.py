from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from todos.database import get_db

bp = Blueprint("items", __name__)

@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        user = request.form.get("user", "Anonymous").strip()
        item = request.form.get("item", "").strip()
        priority = request.form.get("priority", "Medium")
        
        error = None
        
        if not item:
            error = "Item description is required."
        elif len(item) > 500:
            error = "Item description is too long (max 500 characters)."
        
        if priority not in ["Low", "Medium", "High"]:
            error = "Invalid priority value."
        
        if error is None:
            db = get_db()
            db.execute(
                "INSERT INTO items (user, item, priority) VALUES (?,?,?)",
                (user, item, priority),
            )
            db.commit()
            flash("Item added successfully!", "success")
            return redirect(url_for("items.items"))
        
        flash(error, "error")
        
    return render_template("items/create.html")

@bp.route("/items")
def items():
    db = get_db()
    items = db.execute(
        "SELECT user, item, priority, created FROM items ORDER BY created DESC"
    ).fetchall()
    return render_template("items/items.html", items=items)