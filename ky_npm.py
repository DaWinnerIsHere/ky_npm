import numpy

class UnauthorizedAPIKey(Exception):
    def __init__(self, message="Invalid API key."):
        self.message = message
        super().__init__(self.message)

class UnauthorizedAPIBot(Exception):
    def __init__(self, message="Invalid API bot."):
        self.message = message
        super().__init__(self.message)

class UnknownError(Exception):
    def __init__(self, message="Unknown error, contact DaWinnerIsHere#1264."):
        self.message = message
        super().__init__(self.message)

class UnknownRequest(Exception):
    def __init__(self, message="Unknown request."):
        self.message = message
        super().__init__(self.message)

class InvalidBodyForm(Exception):
    def __init__(self, message="Invalid body form."):
        self.message = message
        super().__init__(self.message)

class InvalidObjectType(Exception):
    def __init__(self, message="Invalid object type."):
        self.message = message
        super().__init__(self.message)

class UnsupportedFileExt(Exception):
    def __init__(self, message="File extension is not supported."):
        self.message = message
        super().__init__(self.message)

class UnknownFile(Exception):
    def __init__(self, message="File could not be found in the database."):
        self.message = message
        super().__init__(self.message)

class RateLimit(Exception):
    def __init__(self, message="You have hit the rate limit."):
        self.message = message
        super().__init__(self.message)

class InsufficientArguments(Exception):
    def __init__(self, message="Insufficient arugments."):
        self.message = message
        super().__init__(self.message)

class RequestSender():
    def __init__(self,key):
        self.key = key

    request_base = '{\"h\":{\"key\":\"*1\"},\"d\":{\"rq\":\"*2\"}}'
    request_id = '{\"h\":{\"key\":\"*1\"},\"d\":{\"rq\":\"*2\",\"id\":*3}}'
    request_file = '{\"h\":{\"key\":\"*1\"},\"d\":{\"rq\":\"*2\",\"file\":\"*3\"}}'

    def rq(self,request=None,type='base',id=None,file=None):
        if request == None:
            raise InsufficientArguments
        if type == 'base':
            body = request_base
        elif type == 'id':
            body = request_id
        elif type == 'file':
            body = request_file
        else:
            raise InvalidBodyForm
        body.replace('*1',key)
        if request == None:
            raise UnknownRequest
        body.replace('*2',request)
        if type == 'id':
            if id == None:
                raise InsufficientArguments
            if isinstance(id,int) != True:
                raise InvalidObjectType
        if type == 'file':
            if file == None:
                raise InsufficientArguments
            if isinstance(file,str) != True:
                raise InvalidObjectType
        return body
