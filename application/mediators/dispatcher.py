class Dispatcher:
    def __init__(self):
        self._handlers = {}

    def register(self, request_type, handler):
        self._handlers[request_type] = handler

    async def dispatch(self, request):
        handler = self._handlers[type(request)]
        return await handler.handle(request)
