from classes import webserver
from flask import Flask

class Main:
    def run(self):
        app = Flask(__name__)
        app.add_url_rule("/api/get/<list_ids>", view_func=webserver.serveRequests.as_view("get_data_api"))
        app.run()


if __name__ == "__main__":
    main = Main()
    main.run()