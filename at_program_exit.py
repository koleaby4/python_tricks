from atexit import register

def log_exit_message():
    print("atexit explicitly registered func: logging final messages...")

@register
def close_connections():
    print("atexit registered with decorator: closing open connections...")


register(log_exit_message)

if __name__ == '__main__':
    print("----\ndoing some work...")
    print("final explicit line of code\n----")
