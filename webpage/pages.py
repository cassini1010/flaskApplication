from flask import Blueprint, render_template
bp = Blueprint('pages', __name__)


@bp.route("/")
def home():
    return render_template(r'pages/home.html')

@bp.route("/about")
def about():
    return render_template(r'pages/about.html')