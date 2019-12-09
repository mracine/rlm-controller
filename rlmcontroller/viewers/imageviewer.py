from socket import AF_UNIX, SOCK_STREAM, socket

class ImageViewer():

    def __init__(self):
        self.sock = socket(AF_UNIX, SOCK_STREAM, 0)
        self.current = None
        pass

    def display(self, resource, config={}):
        # TODO: what should we return here?
        pass

#    def __del__(self):
#        pass

