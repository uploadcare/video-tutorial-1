import SimpleHTTPServer
import BaseHTTPServer
import urlparse


class HTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_POST(self):
        """Serve a POST request."""
        # Extract and print the contents of the POST
        length = int(self.headers['Content-Length'])
        post_data = urlparse.parse_qs(self.rfile.read(length).decode('utf-8'))
        if post_data:
            print 'POST DATA:'
        for key, value in post_data.iteritems():
            print "    %s=%s" % (key, value)
        return self.do_GET()


def test(HandlerClass=HTTPRequestHandler,
         ServerClass=BaseHTTPServer.HTTPServer):
    BaseHTTPServer.test(HandlerClass, ServerClass)


if __name__ == '__main__':
    test()
