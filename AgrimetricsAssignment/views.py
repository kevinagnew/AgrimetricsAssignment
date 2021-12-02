from django.shortcuts import render
from AgrimetricsAssignment.create_sandwich_order import CreateSandwich

# Accept sandwich orders
# List of tasks for giovanni


# Request for home_view
def home_view(request):
    return render(request, 'homepage.html')


# Navigate to sandwich order
def sandwich_order_view(request):
    return render(request, 'create_order.html')


# Request for create_sandwich_order_view
def create_sandwich_order_view(request):
    if (request.method == 'POST'):
        sandwich = {
            'name': request.POST.get('name'),
            'base': request.POST.get('base'),
            'meat_one': request.POST.get('meat_one'),
            'meat_two': request.POST.get('meat_two'),
            'cheese': request.POST.get('cheese'),
            'sauce': request.POST.get('sauce'),
            'salad': request.POST.get('salad'),
            'extra': request.POST.get('extra')
        }
        CreateSandwich.create_sandwich_order(request, sandwich)
    return render(request, 'homepage.html')


def sandwich_order_delete_view(request):
    CreateSandwich.delete_all_orders(request)
    return render(request, 'task_to_complete.html')


# Request for create_sandwich_order_view
def task_to_complete_view(request):
    orders = CreateSandwich.get_all_orders(request)
    tasks = CreateSandwich.get_schedule(request, orders)
    schedule = tasks[0]
    break_time = tasks[1]
    return render(request, 'task_to_complete.html', {'orders': orders,
                                                     'schedule': schedule,
                                                     'break_time': break_time})
