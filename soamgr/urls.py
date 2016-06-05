from django.conf.urls import url

from . import views



urlpatterns = [
    url(
        regex=r'^adviser/$',
        view=views.Adviser_BaseView.as_view(),
        name='adviser_base'
    ),
    url(
        regex=r'^oa-create/$',
        view=views.Oa_CreateView.as_view(),
        name='oa_create'
    ),    
    url(
        regex=r'^oa-update/(?P<pk>\d+)/$',
        view=views.Oa_UpdateView.as_view(),
        name='oa_update'
    ),
    url(
        regex=r'^adviser/soa-review/(?P<pk>\d+)/$',
        view=views.Adviser_ReviewSoa.as_view(),
        name='adviser_reviewsoa'
    ),
    url(
        regex=r'^qpp-admin/review-soa/(?P<pk>\d+)/$',
        view=views.Adviser_ReviewSoa.as_view(),
        name='qppadmin_reviewsoa'
    ),
    url(
        regex=r'^qpp-admin/$',
        view=views.QppAdmin_Base.as_view(),
        name='qppadmin_base'
    ),
    url(
        regex=r'^qpp-admin/soa-settings/$',
        view=views.QppAdmin_SoaSettings.as_view(),
        name='qppadmin_soasettings'
    ),
    url(
        regex=r'^qpp-admin/soatype-create/$',
        view=views.QppAdmin_SoaTypeCreateView.as_view(),
        name='qppadmin_soatype_create'
    ),
    url(
        regex=r'^qpp-admin/soatype-update/(?P<pk>\d+)$',
        view=views.QppAdmin_SoaTypeUpdateView.as_view(),
        name='qppadmin_soatype_update'
    ),
    url(
        regex=r'^qpp-admin/order-approval/(?P<pk>\d+)/$',
        view=views.QppAdmin_OaApproval.as_view(),
        name='qppadmin_orderapproval'
    ),
    url(
        regex=r'^paraplanner/$',
        view=views.Paraplanner_BaseView.as_view(),
        name='paraplanner_base'
    ),
    url(
        regex=r'^paraplanner/claim-job/(?P<pk>\d+)/$',
        view=views.Paraplanner_ClaimJob.as_view(),
        name='paraplanner_claimjob'
    ),
]
