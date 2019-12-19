from mongoengine import Document, EmbeddedDocument, fields


class SpotAvailableHours(EmbeddedDocument):

    DAY_CHOICES = (
        ('m', 'monday'),
        ('t', 'tuesday'),
        ('w', 'wednesday'),
        ('th', 'thursday'),
        ('f', 'friday'),
        ('sa', 'saturday'),
        ('su', 'sunday'),
    )

    day = fields.StringField(max_length=3, choices=DAY_CHOICES)
    start_time = fields.StringField(required=True)
    end_time = fields.StringField(required=True)


class Spot(Document):
    name = fields.StringField(required=True)
    location = fields.PointField(auto_index=True)
    hours = fields.ListField(fields.EmbeddedDocumentField(SpotAvailableHours))