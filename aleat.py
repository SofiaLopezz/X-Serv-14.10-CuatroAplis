#!/usr/bin/python3

#Sofia Lopez

class Hello:
    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        return ("200 OK", "<html><body><h1>" + "Dumb application just saying 'It works!'" +"</h1><p>App id: Hola<p></body></html>")