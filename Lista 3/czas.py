from timeit import default_timer as timer
def czas(f, *args):
    start = timer()
    f(*args)
    return (timer() - start)
