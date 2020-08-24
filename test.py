from basic_http.session import HttpSession

http_session = HttpSession(random_agent='opera', follow_redirects=True)
response = http_session.request('GET', 'http://google.ro')

requests_chain = http_session.get_requests_chain()
for request in requests_chain:
    print(request[0])
    print(request[1].get_header())
print(http_session)

response = http_session.request('GET', 'http://www.google.ro/search?q=masini')

requests_chain = http_session.get_requests_chain()
for request in requests_chain:
    print(request[0])
    print(request[1].get_header())
print(http_session)
