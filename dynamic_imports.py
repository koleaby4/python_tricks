from importlib import import_module
import re

client_module_path = 'project.path.to.module'
module = import_module(client_module_path)
candidates = [s for s in dir(module) if re.match(r"\w+ClientContext$", s)]

assert (
    len(candidates) == 1
), f"Expected 1 subclass of ClientContext in {client_module_path=}, but found {candidates=}"

client_context_class = getattr(module, candidates[0])

if issubclass(client_context_class, ClientContext):
    instance = client_context_class()
    instance.do_stuff()
