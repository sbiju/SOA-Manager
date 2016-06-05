from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        regex=r'^oa-order/add/$',
        view= views.OrderCreateView.as_view(),
        name='oa-order-add'
     ),
     url(
        regex=r'^oa-order/$',
        view= views.OrderListView.as_view(),
        name='oa-order-list'
     ),

    # url(
    #     regex=r'^oa-order/detail/(?P<pk>[-\w]+)/$',
    #     view= views.OrderInstanceView.as_view(),
    #     name='oa-order-details'
    #  ),

    url(
        regex=r'^oa-order/(?P<pk>[-\w]+)/$',
        view= views.OrderDetailView.as_view(),
        name='oa-order-detail'
     ),
]
