from time import sleep
import time

def ft_progress(lst) :
    now = time.time()

    for i in range(len(lst)) :
        percent = i * 100 // len(lst)
        estimatedTime = (time.time() - now) / (percent+ 1) * 100
        progress_bar = "=" * ((percent // 2) + 1)
        print(f"ETA: {(estimatedTime ):>5.2f}s [ {percent+1:>3}%][{progress_bar:<50}] {i+1}/{len(lst)} | elapsed time {(time.time() - now) % 60 :0.2f}s", end = "\r")
        yield i

if __name__ == "__main__" :
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)