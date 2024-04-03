from django import template
from eduprod.models import BOXES, Card

register = template.Library()
#Creates an instance of Django's Library class to register custom template tags.


@register.inclusion_tag("eduprod/box_links.html")
#Decorator used to register a template tag named boxes_as_links and specify the template (eduprod/box_links.html) to render the tag.
def boxes_as_links():
    boxes = []
    for box_num in BOXES:
        card_count = Card.objects.filter(box=box_num).count()
        boxes.append({"number": box_num, "card_count": card_count})

    return {"boxes": boxes}

#this code defines a custom template tag that generates navigation links to boxes/categories of flashcards. The tag retrieves the number of cards associated with each box and passes this information to a template for rendering.