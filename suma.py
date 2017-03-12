#!/usr/bin/python3

#Sofia Lopez

class Sum:
    def parse(self, request, rest):
        return rest

    def process(self, parsedRequest):
        try:
        	sum1 = parsedRequest[1]
        	sum2 = parsedRequest[2]
        	total = int(sum1) + int(sum2)
        return ("200 OK", "<html><body><p>El resultado es: " + str(total) + "<p></body></html>")