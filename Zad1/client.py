from suds.client import Client
#hello_client = Client('http://192.168.56.103:8000/?wsdl')
hello_client = Client('http://localhost:8000/?wsdl')
print hello_client.service.say_hello("Dave", 5)
