from twisted.internet import reactor
from twisted.internet.interfaces import IAddress
from twisted.internet.protocol import Protocol
from twisted.internet.protocol import ClientFactory as ClFactory
from twisted.internet.endpoints import TCP4ClientEndpoint


class Client(Protocol):
    def __init__(self):
        reactor.callInThread(self.send_data)

    def dataReceived(self, data: bytes) -> None:
        data = data.decode('utf-8')
        print(data)

    def send_data(self) -> None:
        while True:
            self.transport.write(input().encode('utf-8'))


class ClientFactory(ClFactory):
    def buildProtocol(self, addr: IAddress) -> Client:
        return Client()

if __name__ == '__main__':
    endpoind = TCP4ClientEndpoint(reactor, 'localhost', port=2000)
    endpoind.connect(ClientFactory())
    reactor.run()

