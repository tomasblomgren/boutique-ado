from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'there is nothing in your bag at the moment')
        return redirect(reverse('products'))
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_secret_key': pk_test_51MUSoCEjEMHluTxVKcQRL8hlSlzdoqDZr3eLTj8txmslvIsiUlh5GI8ZuuAXlc24iI1FAPkr21i9RwjLxu6yFgz300C0BnMtqe,
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
