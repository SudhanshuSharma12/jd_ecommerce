from django import template
from creative.models import Order

register = template.Library()

@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user,ordered=False)
        if qs.exists():
            print(qs[0])
            return qs[0].items.count()
        return 0

# @register.inclusion_tag('product.html')
# def any_function():
#     variable = Review.objects.filter(title)
#     return {'variable': variable}