from functools import singledispatch

@singledispatch
def process_args(arg):
    raise NotImplementedError(f"Functionality for processing type `{arg.__class__.__name__}` has not been implemented")

@process_args.register
def _(arg: int):
    print("processing INT argument...")

@process_args.register
def _(arg: str):
    print("processing STR argument...")

@process_args.register
def _(arg: list):
    print("processing LIST argument...")

class A:
    pass

if __name__ == '__main__':
    process_args("hello, there)")
    process_args(42)
    process_args(['a', 'list'])
    process_args(A())
