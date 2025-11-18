import threading 
import time 
import requests

def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    
    print(f'fib({number}) is {fib(number)}')
        

def fibo_with_threads():
    t1 = threading.Thread(target = print_fib, args=(40,))
    t2 = threading.Thread(target = print_fib, args=(41,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

start_thread=time.time()

#fibo_with_threads()

end_thread=time.time()

print(f'Thread took {end_thread - start_thread:.2f} seconds ')

print('-' * 100)



def read_example() -> None:
    response = requests.get('https://www.example.com')
    print(response.status_code)


sync_start = time.time()

read_example()
read_example()

sync_end = time.time()
print(f'Running synchronously took {sync_end - sync_start:.4f} seconds.')
print('-' * 100)

def read_example() -> None:
    response = requests.get('https://www.example.com')
    print(response.status_code)

thread1 = threading.Thread(target = read_example)
thread2 = threading.Thread(target = read_example)

thread_start = time.time()
thread1.start()
thread2.start()

print('All threads are running..!!')

thread1.join()
thread2.join()

thread_end = time.time()

print(f'Running synchronously took {thread_end - thread_start:.4f} seconds.')
