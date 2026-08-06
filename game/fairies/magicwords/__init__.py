"""
The magic words the Flash client's LiveMod console can send.

`registry` holds the dispatch table and the context object every handler is
given; `commands` is the package of handlers, importing which is what fills the
table in. FairiesMagicWordManagerAI is the only caller -- it authorizes the
sender and then hands the command string here.
"""
