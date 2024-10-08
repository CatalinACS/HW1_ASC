"""
This module represents the Producer.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

from threading import Thread
from time import sleep


class Producer(Thread):
    """
    Class that represents a producer.
    """

    def __init__(self, products, marketplace, republish_wait_time, **kwargs):
        """
        Constructor.

        @type products: List()
        @param products: a list of products that the producer will produce

        @type marketplace: Marketplace
        @param marketplace: a reference to the marketplace

        @type republish_wait_time: Time
        @param republish_wait_time: the number of seconds that a producer must
        wait until the marketplace becomes available

        @type kwargs:
        @param kwargs: other arguments that are passed to the Thread's __init__()
        """
        Thread.__init__(self, **kwargs)
        self.products = products
        self.marketplace = marketplace
        self.republish_wait_time = republish_wait_time
        self.prod_id = marketplace.register_producer()

    def run(self):
        """
        Takes a product from the list and then publishes it in the Marketplace.
        If the operation fails, the producer sleeps 'republish_wait_time' seconds.
        If the operation succeeds, the producers sleeps 'wait_time' seconds.
        'wait_time' is a time associated with the current product.
        """
        while 1:
            for product, quantity, wait_time in self.products:
                cnt = quantity
                while cnt > 0:
                    result = self.marketplace.publish(self.prod_id, product)
                    if not result:
                        sleep(self.republish_wait_time)
                    else:
                        sleep(wait_time)
                        cnt -= 1
