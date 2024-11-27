from http.server import BaseHTTPRequestHandler, HTTPServer


hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """Метод для обработки входящих GET-запросов"""

        path = self.path

        if path == "/css/bootstrap.min.css":
            path = "../css/bootstrap.min.css"
            type_header = "text/css"
        elif path == "/js/bootstrap.bundle.min.js":
            path = "../js/bootstrap.bundle.min.js"
            type_header = "text/javascript"

        else:

            path = "../html/contacts.html"
            type_header = "text/html"

        self.send_response(200)
        self.send_header("Content-type", type_header)
        self.end_headers()
        with open(path) as file:
            content = file.read()
            self.wfile.write(bytes(content, "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass





    webServer.server_close()
    print("Server stopped.")