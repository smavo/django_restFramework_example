
from django.http import JsonResponse
from .models import Employee


def employeeView(request):

    # emp = {
    #     'id': 100057596,
    #     'name': 'Smavodev',
    #     'sal': 100000000
    # }
    # return JsonResponse(emp)

    data = Employee.objects.all();
    response = {'employees': list(data.values('id', 'name', 'sal'))}

    return JsonResponse(response)
