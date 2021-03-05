from flask import Flask, render_template
from data.db_session import *
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route("/")
def index():
	db_sess = create_session()
	jobs = db_sess.query(Jobs, User)
	jobs = jobs.join(User, Jobs.team_leader == User.id)
	jobs = jobs.all()
	return render_template("index.html", jobs=jobs)

def main():
	global_init("db/mars_explorer.db")
	app.run()

if __name__ == '__main__':
	main()
