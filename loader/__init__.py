__version__ = "5.0"


# for python 3.11
# https://t.me/UserGeSpam/548736
def fix_python311():
    from platform import python_version_tuple

    py_version = map(lambda i: int(i), python_version_tuple()[:2])
    if tuple(py_version) > (3, 9):
        # maintain the import order
        from collections.abc import MutableMapping
        from collections.abc import Container
        import collections

        setattr(collections, "MutableMapping", MutableMapping)
        setattr(collections, "Container", Container)


fix_python311()
