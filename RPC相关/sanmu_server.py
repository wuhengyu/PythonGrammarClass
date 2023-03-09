# -*- coding: utf-8 -*-
# Time    : 2023/3/9 14:05
# Author  : Walter
# File    : sanmu_server.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :
from concurrent import futures

import grpc

import sanmu_pb2
import sanmu_pb2_grpc


class Sanmu(sanmu_pb2_grpc.SanmuServicer):
    def add(self, request, context):
        a, b = request.a, request.b
        print(f"Received request: {a} + {b}")
        c = a + b
        return sanmu_pb2.Response(c=c)


def serve():
    # server = grpc.server(grpc.insecure_channel("[::]:50051"))
    # sanmu_pb2_grpc.add_SanmuServicer_to_server(Sanmu(), server)
    # print("Starting server. Listening on port 50051.")
    # server.start()
    # server.wait_for_termination()

    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sanmu_pb2_grpc.add_SanmuServicer_to_server(Sanmu(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
