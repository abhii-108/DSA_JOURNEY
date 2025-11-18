import multiprocessing
import os 

def hello_from_process():
    print(f'Hello from child process {os.getpid()}')

if __name__ == '__main__':
    hello_process1 = multiprocessing.Process(target=hello_from_process)
    #hello_process2 = multiprocessing.Process(target=hello_from_process)

    hello_process1.start()
    #hello_process2.start()

    print(f'Hello from parent process {os.getpid()}')
    hello_process1.join()
    #hello_process2.join()