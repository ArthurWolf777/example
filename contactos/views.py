from django.shortcuts import render, HttpResponse, redirect
from contactos.models import Contact, Address, Phone
from .forms import states_options, phone_form
from datetime import datetime

# #TEST FULL STACK DEV #########################################

state_select =  states_options()
phoneform = phone_form


#PANTALLA 0002 INDEX ############################
def index(request):
    contactos = Contact.objects.order_by('name')
    return render(request, 'index.html', {
        'contactos': contactos
    })



#PANTALLA 0003 NUEVO CONTACTO #########################################
def new_contact(request):
    

    if request.method == 'POST':
        
        birthday_string = request.POST['birthday']
        birthday_datetime = datetime.strptime(birthday_string, "%Y-%m-%d")

        name = request.POST['name']
        lastname = request.POST['lastname']
        photo = request.POST['photo']
        birthday = birthday_datetime

        contact = Contact(
            name = name,
            lastname = lastname,
            photo = photo,
            birthday = birthday,
        )

        contact.save()

        return redirect('index')
    else:
        return render(request, 'newcontact.html')


#PANTALLA 0004 EDITAR CONTACTO #########################################
def edit_contact(request, id):
    
    contact_id = Contact.objects.get(pk=id)

    contact_id.name
    contact_id.lastname
    contact_id.photo
    contact_id.birthday
    primary_key = contact_id.id
    update = contact_id.updated_at


    if request.method == 'POST':

        Phoneform = phone_form(request.POST)
        
        if Phoneform.is_valid():

            phone_type_options = request.POST['types']
            alias = request.POST['alias']
            number = request.POST['number']
            contact_id = contact_id.id
            
            
            phone = Phone(
                phone_type_options = phone_type_options,
                alias = alias,
                number = number,
                contact_id = contact_id

            )

            phone.save()

            return redirect('edit_contact', print('telefono actualizado'))

        


    try:
        Phones_list = Phone.objects.filter(contact_id=contact_id)
        

    except Phone.DoesNotExist:
        
        Phones_list = None

        
    return render(request, 'editcontact.html', 
                {'savedname' : contact_id.name,
                'lastname' : contact_id.lastname,
                'update' : update,
                'contact_id' : primary_key,
                'state_select' : state_select,
                'phoneform' : phoneform,
                'Phone_list' : Phones_list
                })


#FUNCIÓN BORRAR CONTACTO, BORRA LOS DATOS DE RELACIPON EN CASCADA #########################################
def delete_contact(request, id):

    contact = Contact.objects.get(pk=id)

    contact.delete()

    return redirect('index')


#FUNCIÓN EDITAR INFORMACIÓN DE CONTACTO #########################################
def edit_name(request, id):
            if request.method == 'POST':

                contact_id = Contact.objects.get(pk=id)


                birthday_string = request.POST['birthday']
                birthday_datetime = datetime.strptime(birthday_string, "%Y-%m-%d")

                contact_id.name = request.POST['name']
                contact_id.lastname = request.POST['lastname']
                contact_id.photo = request.POST['photo']
                contact_id.birthday = birthday_datetime

                contact_id.save()

                primary_key = contact_id.id

                update = contact_id.updated_at
                
            return redirect('index')



#FUNCIÓN EDITAR DIRECCIÓN DEL CONTACTO, RELACIÓN 1:1 #########################################

def edit_adress(request, id):
            if request.method == 'POST':

                contact_id = Contact.objects.get(pk=id)

                street = request.POST['street']
                exterior_number = request.POST['exterior_number']
                internal_number = request.POST['internal_number']
                neighborhood = request.POST['neighborhood']
                municipality = request.POST['municipality']
                state = request.POST['states']
                references = request.POST['references']

                address = Address(
                    street = street,
                    exterior_number = exterior_number,
                    internal_number = internal_number,
                    neighborhood = neighborhood,
                    municipality = municipality,
                    state = state,
                    references = references,
                    contact_id = contact_id.id
                )

                address.save()
                update = contact_id.updated_at

            return redirect('index')


#FUNCIÓN ELIMINAR TELEFONO #########################################

def delete_phone(request, id):

    Phone_to_delete = Phone.objects.get(pk=id)
    Phone_to_delete.delete()

    return redirect('index')


#VISTA DE PRUEBAS PARA FRONTEND #########################################

def test_code(request):
    
    phoneform = phone_form

    return render(request, 'test.html', {'phoneform' : phoneform})