from __future__ import print_function

import grpc

import calculator_pb2
import calculator_pb2_grpc


def run():
    file = open("output.txt","w+")
    a = 5
    b = 10
    file.write("Request send to server: param1: {0},param2: {1} \n".format(a,b))
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Add(calculator_pb2.AddRequest(param1=a,param2=b))
    file.write("Response received from server: {0}\n".format(response.addResult))
    file.close()

if __name__ == '__main__':
    run()
