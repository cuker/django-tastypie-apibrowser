from django.views.generic import TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

class StaffTemplateView(TemplateView):
    template_name="apibrowser/index.html"

    @method_decorator(staff_member_required)
    def dispatch(self,request,*args,**kwargs):
        return super(StaffTemplateView,self).dispatch(request,*args,**kwargs)


