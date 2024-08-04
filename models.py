import mongoengine as me

class Author(me.Document):
    fullname = me.StringField(required=True)
    born_date = me.StringField()
    born_location = me.StringField()
    description = me.StringField()

class Quote(me.Document):
    tags = me.ListField(me.StringField())
    author = me.ReferenceField(Author, required=True)
    quote = me.StringField(required=True)
