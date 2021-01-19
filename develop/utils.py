# develop/utils.py

from uuid import uuid4
from nameparser import HumanName
from difflib import get_close_matches

from .typs import Contact


def create_contact(crimata_id="", name=""):

    # Parse name 
    p = HumanName(name)

    # Add name attributes to contact.
    contact = Contact(crimata_id=crimata_id,
                      title=p.title,
                      first=p.first,
                      middle=p.middle,
                      last=p.last,
                      suffix=p.suffix,
                      nickname=p.nickname,
                      contact_id=str(uuid4()))

    return contact

# Must pass in either name or Crimata ID.
def search_contacts(contacts, name=False, crimata_id=False):

    if crimata_id:
        return search_contacts_by_id(crimata_id, contacts)

    return search_contacts_by_name(name, contacts)

def search_contacts_by_name(name, contacts):
    names = [v.full for v in contacts.values()]

    target = get_close_matches(name, names, cutoff=0.5)

    if not target:
        return False

    for v in contacts.values():
        if v.full == target[0]:
            return v

def search_contacts_by_id(crimata_id, contacts):
    target = False
    for v in contacts.values():
        if v.crimata_id == crimata_id:
            target = v

    return target
