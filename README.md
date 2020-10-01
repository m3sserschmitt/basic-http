# basic-http

basic-http is a python package for requesting web resources.

# Getting started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

`Python >= 3.6`

### Installing

Install the package from Python Package Index using command:

`pip3 install basic-http`

### Basic usage:

Request a web page and print response:

```
import basic_http

http_session = basic_http.session.HttpSession()
response = http_session.request('GET', 'https://google.ro')

print(response)
```

In case of multiple requests (http redirects), you can see
the requests chain:

```
# get the entire requests chain
requests_chain = http_session.get_requests_chain()

for request in requests_chain:
    print(request[0])  # print request 
    print(request[1])  # print http response
```

You can set a custom http header:

```
my_header = {
    'new_header': 'header_value',
    # add as many headers as you like
}

response = http_session.request('GET', 'https://google.ro/', header=my_header)
```

If you don't want to follow http redirects, or disable cookies:

```
http_session = basic_http.session.HttpSession(follow_redirects=False, cookies_enabled=False)
```

### Session details:

Print session details:

```
http_session = http_session = basic_http.session.HttpSession()
http_session.request('GET', 'https://google.ro/')

print(http_session)
```

### Using a proxy:

basic-http also has proxy support:

```
http_session = session.HttpSession()
http_session.set_proxy('proxy_address_here')
```

## Authors

* **Romulus-Emanuel Ruja <<romulus-emanuel.ruja@tutanota.com>>**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.