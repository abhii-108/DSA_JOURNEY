import os 
import threading

print(f'python process is running with process id {os.getpid()}')

# total_thread = threading.active_count()  ## 1
# thread_name = threading.current_thread().name ## MainThread

# print(f'python is currently running {total_thread} threads')
# print(f'the current thread is {thread_name}') ## MainThread


def hello_from_thread():
    print(f'hello from thread {threading.current_thread()}')


hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()
total_threads = threading.active_count()
thread_name = threading.current_thread().name
print(f'Python is currently running {total_threads} thread(s)')
print(f'The current thread is {thread_name}')
hello_thread.join()