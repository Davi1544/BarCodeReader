# Method Decorators

class Log:
    path = "log.txt"
    f = open(path, "a")

    def log(func : object) -> object:
        
        def wrapper(*args, **kwargs):
            Log.f.write(f"Calling funcion {func.__name__}\n")
            value = func(*args, **kwargs)
            return value
        return wrapper