from flask import render_template, request, Response



class HomeController():
    def __init__(self, server):
        self.server = server
        self.group = "Home"

    def index(self):

        return render_template('/home/index.html')
