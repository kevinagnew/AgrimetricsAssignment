from AgrimetricsAssignment.models import CreateSandwichOrder
from time import strftime
from time import gmtime


class CreateSandwich:

    # Create sandwich record and add it to the database
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

    # Return all current orders in the database
    def get_all_orders(self):
        orders = CreateSandwichOrder.objects.all()
        return orders

    # Create a sequential schedule for Giovanni - break is only taken when no orders are left
    def get_schedule(self, orders):
        # Sandwich take 3.5 minutes to completely finish, sandwiches are made and served in sequential order
        # Current time of when an order is place can be taken into consideration and added to the database for accurate timings
        count = 0
        result = []
        for order in orders:
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
                        'name': order.name,
                        'ticket': order.id}
            result.append(schedule)
            count += 1
        # A break time can be implemented based on whether Giovanni takes a break every hour, two hours etc
        # The implement break time is assuming Giovanni only makes 4 - 5 sandwiches at any given time period
        break_time = strftime("%H:%M:%S", gmtime(count * 210))
        return result, break_time

    # Delete all order from the database
    def delete_all_orders(self):
        CreateSandwichOrder.objects.all().delete()
        return
