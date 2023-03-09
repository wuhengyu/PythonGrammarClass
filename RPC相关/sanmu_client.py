# -*- coding: utf-8 -*-
# Time    : 2023/3/9 18:41
# Author  : Walter
# File    : sanmu_client.py
# License : (C)Copyright Walter
# Version : 1.0
# Desc    :

import grpc

import sanmu_pb2
import sanmu_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = sanmu_pb2_grpc.SanmuStub(channel)
        request = sanmu_pb2.Request(a=2, b=3)
        response = stub.add(request)
        print(f"Response received: {response.c}")
    print("Sanmu client received: " + str(response.c))


if __name__ == "__main__":
    run()
