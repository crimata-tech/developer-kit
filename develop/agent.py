# develop/agent.py

import inspect

from .typs import P


class Agent:

    def fetch(self, entities, text=False):
        epic = inspect.stack()[1].function

        if type(entities) == str:
            entities = [entities]

        request = P(
            intent="fetch", 
            params={
                "entities": list(entities),
                "text": text
            },
            epic=epic
        )

        self.send_agent(request)
        
        # Wait for a fulfill intent to come in.
        request = self.__listen(epic)

        # Parse request
        response = self.__parse_request(request)

        return response

    def fetchone(self, entities, text=False):
        epic = inspect.stack()[1].function

        if type(entities) == str:
            entities = [entities]

        request = P(
            intent="fetchone", 
            params={
                "entities": list(entities),
                "text": text
            },
            epic=epic
        )

        self.send_agent(request)
        
        # Wait for a fulfill intent to come in.
        request = self.__listen(epic)

        # Parse request
        response = self.__parse_request(request)

        return response

    def fetchsubset(self, entities, text=False):
        epic = inspect.stack()[1].function

        if type(entities) == str:
            entities = [entities]

        request = P(
            intent="fetchsubset", 
            params={
                "entities": list(entities),
                "text": text
            },
            epic=epic
        )
        
        self.send_agent(request)
        
        # Wait for a fulfill intent to come in.
        request = self.__listen(epic)

        # Parse request
        response = self.__parse_request(request)

        return response

    def fetchany(self, text):
        epic = inspect.stack()[1].function

        request = P(
            intent="fetchany", 
            params={
                "text": text
            },
            epic=epic
        )

        self.send_agent(request)

        # Wait for a fulfill intent to come in.
        request = self.__listen(epic)

        response = self.__parse_request(request)

        return response
        
    def notify(self, text=False, params=False, end=False):
        epic = inspect.stack()[1].function

        request = P(
            intent="notify",
            params={
                "params": params,
                "text": text,
                "end": end
            },
            epic=epic
        )

        self.send_agent(request)

    def query(self, entity):
        epic = inspect.stack()[1].function

        request = P(
            intent="query", 
            params={"entity": entity},
            epic=epic
        
        )

        self.send_agent(request)

        # Wait for a fulfill intent to come in.
        request = self.__listen(epic)     

        # Parse request
        response = self.__parse_request(request)

        return response

    def alter(self, action, params):

        request = P(
            intent="alter", 
            params={
                "action": action,
                "params": params
            },
            epic=False
        )

        self.send_agent(request)

    def __listen(self, epic):
        while True:
            request = self.stm.get(epic)
            if request:
                self.stm.clear()
                break
        return request

    @staticmethod
    def __parse_request(request):

        values = [v for v in request.params.values()]

        response = tuple(values)
        if len(values) == 1:
            response = values[0]

        return response


