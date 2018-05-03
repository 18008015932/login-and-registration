from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from stu import views
urlpatterns = [
    url(r'^index/',login_required(views.index)),
    url(r'^addstu/',login_required(views.addStu), name='add'),
    url(r'^stupage/',login_required(views.stuPage)),
    url(r'^addstuInfo/(?P<stu_id>\d+)/', login_required(views.addStuInfo), name='addinfo')
]