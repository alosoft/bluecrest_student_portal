from django.views.generic import ListView
from students import models


# Create your views here.
class Index(ListView):
    model = models.Record
    template_name = 'students/index.html'


# def index(request):
#     data = models.Record.objects.all()
#
#     form = forms.SearchForm()
#     # if request.method == 'GET':
#     data_query = request.GET.get('query', None)
#     print(data_query)
#     if data_query:
#         search_results = data.filter(
#             Q(program__icontains=data_query) |
#             Q(semester__icontains=data_query)
#         )
#         record_list = {
#             'record_list': search_results,
#         }
#         return render(request, 'students/index.html', context=record_list)
#
#     return render(request, 'students/index.html', {'form': form})
