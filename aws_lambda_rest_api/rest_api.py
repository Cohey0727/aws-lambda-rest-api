DEFAULT_DETAIL_KEY = 'id'


class RestApi:
    detail_key = DEFAULT_DETAIL_KEY
    default_headers = {}

    def list(self, event, context):
        raise AttributeError('list method does not be implemented')

    def retrieve(self, event, context):
        raise AttributeError('retrieve method does not be implemented')

    def create(self, event, context):
        raise AttributeError('create method does not be implemented')

    def update(self, event, context):
        raise AttributeError('update method does not be implemented')

    def patial_update(self, event, context):
        raise AttributeError('patial_update method does not be implemented')

    def destroy(self, event, context):
        raise AttributeError('destory method does not be implemented')

    def default(self, event, context):
        raise AttributeError('default method does not be implemented')

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
        http_method = http_method.lower()
        return self.detail_methods.get(http_method, self.default) if is_detail else self.list_methods.get(http_method, self.default)

    def decorate_response(self, response: dict):
        if response.get('headers') == None:
            response['headers'] = self.default_headers

    def create_handler(self):

        def handler(event, context):
            http_method = event['httpMethod']
            path_parameters = event.get('pathParameters', {}) or {}
            is_detail = path_parameters.get(self.detail_key) != None
            rest_function = self.get_method(http_method, is_detail)
            response = rest_function(event, context)
            self.decorate_response(response)
            return response

        return handler
