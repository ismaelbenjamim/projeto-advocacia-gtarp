from django import template

register = template.Library()


def getnamefield(value):
    try:
        return str(value.__class__.__name__)
    except:
        return None


register.filter('getnamefield', getnamefield)
