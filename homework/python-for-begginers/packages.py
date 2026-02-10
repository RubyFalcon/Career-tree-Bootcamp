# Packages: python package holds multiple related python modules into a directory, we call it a package
# We will make one called ecommerce
# To make a directory into a package, need to add __init__.py
# We then define our modules inside our package
# Cannot import modules directly, must import package 
from ecommerce import shipping
from ecommerce.shipping import calculate_shipping
shipping.calculate_shipping()

calculate_shipping()