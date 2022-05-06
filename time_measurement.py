import time
 
def measurement(*f):
    start_time = time.perf_counter()    
    print(*f)
    end_time = time.perf_counter()
    
    elapsed_time = end_time - start_time
    print(elapsed_time)