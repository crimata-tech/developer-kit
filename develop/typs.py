# develop/typs.py

class P:

    def __init__(self, 
                 intent, 
                 params={}, 
                 epic=False, 
                 confidence=1.0):

        self.intent = intent #eg. launch, fetch, etc.
        self.params = params
        self.epic = epic #eg. editprofile

        self.confidence = confidence


class Profile:

    def __init__(self, 
                 crimata_id, 
                 title, 
                 first, 
                 middle, 
                 last, 
                 suffix, 
                 nickname):
    
        self.crimata_id = crimata_id

        # Name attributes
        self.title = title
        self.first = first
        self.middle = middle
        self.last = last
        self.suffix = suffix
        self.nickname = nickname
        self.full = first + " " + last if first else None


class Contact:

    def __init__(self, 
                 crimata_id, 
                 title, 
                 first, 
                 middle, 
                 last, 
                 suffix, 
                 nickname,
                 contact_id):
    
        self.crimata_id = crimata_id

        # Name attributes
        self.title = title
        self.first = first
        self.middle = middle
        self.last = last
        self.suffix = suffix
        self.nickname = nickname
        self.full = first + " " + last

        self.contact_id = contact_id