# Developer Kit
Developer tools for writing Crimata apps.

**This is mainly for internal use (not third party development) at the moment.

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

## Example

From there, you can add methods to the class to create services. Each method will be treated as an intent in the Crimata System. Let's write a service for booking a plane ticket.

```python
    def bookplaneticket(self):
        name, email = self.fetch(("name", “email”))
        # do something with entities
```

Let's assume we are an airline and our booking backend needs a name and an email to verify the person. To fetch these entities, we simply call fetch() and pass in what we need. Crimata likley knows the name and email of it's client already. Therefore, it doesn't even have to ask them. Crimata will automatically return those entities. But if it didn't, Crimata will automatically generate envoking text to fetch the entities. It would generate something like "What is your name and email for booking the ticket?" I'll explain more later.

```python
        date = self.fetch(“date”)
        location = self.fetch(“location”, text=“Where do you want to go?”)
```

Next, we fetch a date and location for travel. Notice we can also pass in our own envoking text if we feel that we need more detail.

```python
        # Our airline specific code -------------
        ticket = search_ticket_db(date, location)
        
        # “Does 3:00PM on June 14th work?”
        response = format_ticket_response(ticket)
        # ---------------------------------------
        
        if self.fetch(“polar”, text=response):
            self.book_ticket(ticket)
```

We use the informating we've fetched to search our tickets database for what is available. We find a match and can ask the client to comfirm by fetching a polar entity (yes or no). If the client affirms, we book the ticket.

```python
        self.notify(f"The ticket is booked.", end=True)
```

Finally, we use notify() to send a notification to the client letting them know the ticket is booked. Set end=True to let Crimata know the service is complete.

## Next Steps

Our Api is in the early stages. If your find this intriguing, please don't hesitate to reach out. Currently, our team must be in the loop for any new service added to the platform to ensure everything works well and the intent (along with it's training phrases) is logged into the system.
