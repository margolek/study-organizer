from django.views.generic import TemplateView

class DefaultView(TemplateView):
	template_name = 'index.html'