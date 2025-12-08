import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        print(f"Execution took {self.end - self.start:.2f} seconds")

with Timer():
    for i in range(1000000):
        pass
