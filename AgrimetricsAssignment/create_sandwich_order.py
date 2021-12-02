from AgrimetricsAssignment.models import CreateSandwichOrder
from time import strftime
from time import gmtime


class CreateSandwich:

    def create_sandwich_order(self, sandwich):

        new_sandwich = CreateSandwichOrder(name=sandwich.get('name'),
                                           base=sandwich.get('base'),
                                           meat_one=sandwich.get('meat_one'),
                                           meat_two=sandwich.get('meat_two'),
                                           cheese=sandwich.get('cheese'),
                                           sauce=sandwich.get('sauce'),
                                           salad=True,
                                           extra=sandwich.get('extra'))
        new_sandwich.save()


    def get_all_orders(self):
        orders = CreateSandwichOrder.objects.all()
        return orders


    def get_schedule(self, orders):
        # Sandwich take 3.5 minutes to completely finish, sandwiches are made and served in sequential order
        count = 0
        result = []
        for order in orders:
            name = order.name
            ticket = order.id
            start_time = 0
            serve_time = 0
            if count == 0:
                start_time = strftime("%H:%M:%S", gmtime(0))
                serve_time = strftime("%H:%M:%S", gmtime(150))
            elif count != 0:
                start_time = strftime("%H:%M:%S", gmtime(count * 210))
                serve_time = strftime("%H:%M:%S", gmtime((count * 210) + 150))

            schedule = {'start_time': start_time,
                        'serve_time': serve_time,
                        'name': name,
                        'ticket': ticket}
            result.append(schedule)
            count += 1
        break_time = strftime("%H:%M:%S", gmtime(count * 210))

        time_make_sandwiches_in_seconds = len(orders) * 150
        serve_and_payment_in_seconds = len(orders) * 60

        return result, break_time


    def delete_all_orders(self):
        CreateSandwichOrder.objects.all().delete()
        return
