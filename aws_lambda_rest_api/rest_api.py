DEFAULT_DETAIL_KEY = 'id'


class RestApi:
    detail_key = DEFAULT_DETAIL_KEY

    def list(self, event, context):
        raise AttributeError()

    def retrieve(self, event, context):
        raise AttributeError()

    def create(self, event, context):
        raise AttributeError()

    def update(self, event, context):
        raise AttributeError()

    def patial_update(self, event, context):
        raise AttributeError()

    def destory(self, event, context):
        raise AttributeError()

    def default(self, event, context):
        raise AttributeError()

    @property
    def detail_methods(self):
        return {
            'get': self.retrieve,
            'put': self.update,
            'patch': self.patial_update,
            'delete': self.destory,
        }

    @property
    def list_methods(self):
        return {
            'get': self.list,
            'post': self.create,
        }

    def get_method(self, http_method: str, is_detail: bool):
        return self.detail_methods.get(str, self.default) if is_detail else self.list_methods.get(str, self.default)

    def create_handler(self):

        def handler(event, context):
            http_method = event['httpMethod']
            is_detail = event['pathParameters'].get(self.detail_key) != None
            rest_function = self.get_method(http_method, is_detail)
            return rest_function(event, context)

        return handler
