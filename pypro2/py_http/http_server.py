# Web server : 클라이언트와 통신이 가능
# CGI (Common Gateway Interface)
# : 웹서버와 외부 프로그램 사이에서 정보를 주고 받는 방법이나 규약. 대화형 웹 페이지 작성 가능.
# : DB 자료 처리, form tag를 사용한 자료 전송 가능 

from http.server import HTTPServer, CGIHTTPRequestHandler

PORT = 8888

class Handler(CGIHTTPRequestHandler):   # java에 servlet 같은 활동을 할 수 있다.
    cgi_directories = ['/cgi-bin']      # python 파일은 설정 경로에 저장
    
serv = HTTPServer(('127.0.0.1', PORT), Handler)

print('웹 서비스 시작 ...')

serv.serve_forever()
