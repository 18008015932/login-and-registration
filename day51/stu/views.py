from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from stu.models import Student, StudentInfo
from uauth.models import Users

def index(request):

    if request.method == 'GET':
        # 获取所有学生信息
        # ticket = request.COOKIES.get('ticket')
        # if not ticket:
        #     return HttpResponseRedirect('/uauth/login/')
        # if Users.objects.filter(u_ticket=ticket).exists():
        #     stuinfos = StudentInfo.objects.all()
        #     return render(request, 'index.html', {'stuinfos': stuinfos})
        # else:
        #     return HttpResponseRedirect('/uauth/login/')
        stuinfos = StudentInfo.objects.all()
        return render(request,'index.html',{'stuinfos':stuinfos})


def addStu(request):

    if request.method == 'GET':

        return  render(request, 'addStu.html')

    if request.method == 'POST':
        # 跳转到学习详情方法中去
        name = request.POST.get('name')
        tel = request.POST.get('tel')

        stu = Student.objects.create(s_name=name, s_tel=tel)

        return HttpResponseRedirect(
            reverse('s:addinfo', kwargs={'stu_id': stu.id})
        )


def addStuInfo(request, stu_id):

    if request.method == 'GET':

        return render(request, 'addStuInfo.html', {'stu_id':stu_id})

    if request.method == 'POST':

        stu_id = request.POST.get('stu_id')
        addr = request.POST.get('addr')

        # 添加头像图片
        img = request.FILES.get('img')

        StudentInfo.objects.create(i_addr=addr, s_id=stu_id, i_image=img)

        return HttpResponseRedirect('/stu/index/')


def stuPage(request):

    if request.method == 'GET':
        page_id = request.GET.get('page_id',1) # 如果没有取到page_id，则默认为1
        stus = Student.objects.all()
        paginator = Paginator(stus,3)
        page = paginator.page(int(page_id))
        return render(request,'index_page.html',{'stus':page})