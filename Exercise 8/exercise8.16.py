#1
import exercise8_15_modul 

unprinted_designs = ['phone case', 'robot pendant']
completed_models = []
exercise8_15_modul.print_models(unprinted_designs, completed_models)

#2
from exercise8_15_modul import print_models

unprinted_designs = ['phone case', 'robot pendant']
completed_models = []
print_models(unprinted_designs, completed_models)

#3
from exercise8_15_modul import print_models as pm

unprinted_designs = ['phone case', 'robot pendant']
completed_models = []
pm(unprinted_designs, completed_models)


#4
import exercise8_15_modul as pf

unprinted_designs = ['phone case', 'robot pendant']
completed_models = []
pf.print_models(unprinted_designs, completed_models)

#5
from exercise8_15_modul import *

unprinted_designs = ['phone case', 'robot pendant']
completed_models = []
print_models(unprinted_designs, completed_models)