from time import perf_counter


class Timer:
    """Timer class for timing code execution"""

    def __init__(self):
        self.start_time: float | None = None
        self.end_time: float | None = None
        self.elapsed_time: float | None = None

    @property
    def elapsed(self) -> float:
        return (
            self.elapsed_time or (perf_counter() - self.start_time)
            if self.start_time
            else 0.0
        )

    def start(self) -> float:
        self.start_time = perf_counter()
        return self.start_time

    def stop(self) -> float:
        self.end_time = perf_counter()
        if self.start_time is not None:
            self.elapsed_time = self.end_time - self.start_time
        return self.end_time

    def __enter__(self):
        self.start_time = perf_counter()
        return self

    def __exit__(self, *args):
        self.end_time = perf_counter()
        if self.start_time is not None:
            self.elapsed_time = self.end_time - self.start_time
