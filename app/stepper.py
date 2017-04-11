import cherrypy

@cherrypy.expose
class Stepper(object):
    def POST(self):
        print("stepper post")
    def GET(self):
        print("stepper get")
    def PUT(self):
        print("stepper put")
    def DELETE(self):
        print("stepper delete")
