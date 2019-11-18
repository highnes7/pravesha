from django.conf.urls import url
from basic_app import views

# SET THE NAMESPACE!
app_name = 'basic_app'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^food_pref_updt/$',views.food_pref_updt,name='food_pref_updt'),
    url(r'^participate/$',views.participate,name='participate'),
    url(r'^departicipate/$',views.departicipate,name='departicipate'),
    url(r'^user/$',views.user,name='user'),
    url(r'^user_login/coordinator/$',views.coordinator,name='coordinator'),
    url(r'^adminpanel/$',views.adminpanel,name='adminpanel'),
    url(r'^pp_report/$',views.pp_report,name='pp_report'),
    url(r'^bat_report/$',views.bat_report,name='bat_report'),
    url(r'^tq_report/$',views.tq_report,name='tq_report'),
    url(r'^adzpreloaded_report/$',views.adzpreloaded_report,name='adzpreloaded_report'),
    url(r'^aio_report/$',views.aio_report,name='aio_report'),
    url(r'^typist_report/$',views.typist_report,name='typist_report'),
    url(r'^showyourtalent_report/$',views.showyourtalent_report,name='showyourtalent_report'),
    url(r'^mod_report/$',views.mod_report,name='mod_report'),
    url(r'^treasurehunt_report/$',views.treasurehunt_report,name='treasurehunt_report'),
    url(r'^cs_pp/$',views.cs_pp,name='cs_pp'),
    url(r'^registrationdesk/',views.registrationdesk,name='registrationdesk'),
    url(r'^paymentupdate/',views.paymentupdate,name='paymentupdate'),
    url(r'^pp_winners/',views.pp_winners,name='pp_winners'),
    url(r'^cs_bat/',views.cs_bat,name='cs_bat'),
    url(r'^bat_winners/',views.bat_winners,name='bat_winners'),
    url(r'^cs_tq/',views.cs_tq,name='cs_tq'),
    url(r'^tq_winners/',views.tq_winners,name='tq_winners'),
    url(r'^cs_ar/',views.cs_ar,name='cs_ar'),
    url(r'^ar_winners/',views.ar_winners,name='ar_winners'),
    url(r'^cs_aio/',views.cs_aio,name='cs_aio'),
    url(r'^aio_winners/',views.aio_winners,name='aio_winners'),
    url(r'^ty_winners/',views.ty_winners,name='ty_winners'),
    url(r'^cs_ty/',views.cs_ty,name='cs_ty'),
    url(r'^cs_syt/',views.cs_syt,name='cs_syt'),
    url(r'^syt_winners/',views.syt_winners,name='syt_winners'),
    url(r'^mod_winners/',views.mod_winners,name='mod_winners'),
    url(r'^cs_mod/',views.cs_mod,name='cs_mod'),
    url(r'^cs_th/',views.cs_th,name='cs_th'),
    url(r'^th_winners/',views.th_winners,name='th_winners'),
    url(r'^cs_pubg/',views.cs_pubg,name='cs_pubg'),
    url(r'^pubg_winners/',views.pubg_winners,name='pubg_winners'),
    url(r'^pdf/',views.Pdf,name='Pdf'),
    url(r'^certificate_report/',views.certificate_report,name='certificate_report')
]


