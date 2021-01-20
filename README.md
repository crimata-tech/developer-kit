# Developer Kit
Developer tools for writing Crimata apps

## Getting Started
```python
from develop import AppBare
```

The easiest way to create a Crimata app is by inheriting AppBare. As the name implies, AppBare is a bare application with all the boilerplate to get you started.

```python
class App(AppBare):
    def __init__(self, name):
        AppBare.__init__(self, “appname”)
```

From there, you can add methods to the class to create services. Each method will be treated as an endpoint in the Crimata System. An enpoint is like an service or an intent that the user can access. Below is an example endpoint for booking a plane ticket.

```python
    def bookplaneticket(self):
        name, email = self.fetch(("name", “email”))
```
