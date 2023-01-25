from django.db import models

# Create your models here.


###### ITERACIÓN DE LISTA DE ESTADOS, PARA INDEXAR CADA UNO ########
def all_states():
    states_list = ['SELECCIONAR', 'Aguascalientes', 'Baja California', 'Baja California Sur', 'Campeche', 'Coahuila', 'Colima', 'Chiapas', 'Chihuahua',  'Ciudad de México', 'Durango', 'Guanajuato', 'Guerrero', 'Hidalgo', 'Jalisco', 'México', 'Michoacán', 'Morelos', 'Nayarit', 'Nuevo León', 'Oaxaca', 'Puebla', 'Querétaro', 'Quintana Roo', 'San Luis Potosí', 'Sinaloa', 'Sonora', 'Tabasco', 'Tamaulipas', 'Tlaxcala', 'Veracruz', 'Yucatán', 'Zacatecas']
    index_list = range(len(states_list))
    state_index_list = list(zip(index_list, states_list))
    return state_index_list

states = all_states()

##### TIPOS DE TELÉFONO #########
phones_types = [
    (0, 'Móvil'),
    (1, 'Casa') 
]


####### MODELO CONTACTOS 
class Contact(models.Model):
    name = models.CharField(max_length=60)
    lastname = models.CharField(max_length=120)
    photo = models.ImageField(default='null')
    birthday = models.DateField()
    updated_at = models.DateTimeField(auto_now_add=True)

########## MODELO DIRECCIÓN RELACIÓN 1:N
class Address(models.Model):
    street = models.CharField(max_length=255)
    exterior_number = models.CharField(max_length=10)
    internal_number = models.CharField(max_length=10)
    neighborhood = models.CharField(max_length=255)
    municipality = models.CharField(max_length=255)
    state = models.IntegerField(choices=states, default=0)
    references = models.TextField()
    contact = models.ForeignKey(Contact, null=False, on_delete=models.CASCADE)

############### MODELO TELÉFONO RELACIÓN 1:N
class Phone(models.Model):
    contact = models.ForeignKey(Contact, null=False, related_name='Phones' ,on_delete=models.CASCADE)
    phone_type_options = models.CharField(max_length=10, choices=phones_types, default=0)
    alias = models.CharField(max_length=255)
    number = models.CharField(max_length=50)
