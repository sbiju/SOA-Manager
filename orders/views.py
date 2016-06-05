from django.shortcuts import render
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView, FormMixin
from django.views.generic import DetailView
from django.views.generic import ListView
from braces.views import LoginRequiredMixin
from .models import Order
from .forms import OrderForm


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/order_form.html'
    success_url = 'orders/oa-order'

    def get_success_url(self):
        return reverse_lazy('orders:oa-order-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(OrderCreateView, self).form_valid(form)


class OrderDetailView(LoginRequiredMixin, DetailView):
    queryset = Order.objects.all()
    template_name = 'order/order_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(OrderDetailView, self).get_context_data(*args,**kwargs)
        return context


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order/order_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(OrderListView, self).get_context_data(*args,**kwargs)
        return context


# class OrderInstanceView(DetailView):
#     queryset = Order.objects.all()[:0]
#     template_name = 'order/order_detail.html'

