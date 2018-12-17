import time
from concurrent import futures
from xfacter import xfacter_pb2
from xfacter import xfacter_pb2_grpc
import facter
import grpc

__version__ = "0.0.1"
__description__ = "facter without border"
__url__ = "https://github.com/neofob/xfacter.git"
__title__ = "xfacter"
__author__ = "tuan t. pham"
__license__ = "MIT"
__copyright__ = "(c) 2018 tuan t. pham"

# TODO: Add healthcheck

GRPC_BIND_ADDRESS = '0.0.0.0'
GRPC_PORT = '50051'
HOUR = 60 * 60


class XFacterServicer(xfacter_pb2_grpc.XFacterServicer):
    fact = None

    def __init__(self):
        self.facter = facter.Facter()
        self.facter.build_cache()

    def HasCache(self, request, context):
        return xfacter_pb2.ResponseHasCache(value=self.facter.has_cache())

    def GetMethod(self):
        pass


def serve():
    print("Entering %s serve" % __file__)
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    xfacter_pb2_grpc.add_XFacterServicer_to_server(XFacterServicer(), grpc_server)
    grpc_server.add_insecure_port(GRPC_BIND_ADDRESS + ':' + GRPC_PORT)
    grpc_server.start()

    try:
        while True:
            time.sleep(HOUR)
    except KeyboardInterrupt:
        grpc_server.stop(grace=1.0)

if __name__ == '__main__':
    serve()
