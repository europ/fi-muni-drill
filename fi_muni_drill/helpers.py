from django import template  

@register.inclusion_tag('templates/question.html')
def task(q):
    return q.task  