from django import template

register = template.Library()  # если мы не зарегестрируем наши фильтры, то django никогда не узнает где именно их искать и фильтры потеряются :(

censor_words = [
    'мат1',
    'мат2',
    'мат3',
]

@register.filter(name='censor')  # регистрируем наш фильтр под именем censor, чтоб django понимал, что это именно фильтр, а не простая функция

def censor(value):
    # фильтр заменяет слова из стоп-листа на '***'
    for sw in censor_words:
        value = value.lower().replace(sw.lower(), '***')
    return value


