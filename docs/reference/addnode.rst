Adding a node to pycrunchbase
=============================

If CrunchBase adds a new Node, we can add it to pycrunchbase as such:

1. Make a new file under `resource/` with the name `<node>.py`, rerplacing `<node>` with the name of the node.

2. Write a test file for this node in `tests/` called `test_<node>.py`.

3. Add a method on :class:`CrunchBase` with the name `<node>` as the public api to access this node.

4. Ensure that all imports are working fine, this includes adding the node to `resource/__init__.py`, `pycrunchbase/__init__.py`.

5. Add a test case to `test_pycrunchbase.py` to test the public api for the new node.
