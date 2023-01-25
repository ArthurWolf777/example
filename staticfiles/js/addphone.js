
const phoneform = document.querySelector('.phone_form');
let counter = 0; // variable contadora
let stop = false;

const canvas = document.getElementById('add_phone_here');
const buttonadd = document.getElementById('add-phone');




document.getElementById('add-phone').addEventListener('click', e => {
    if (counter == 0){
        phoneform.classList.remove('not_visible');
        console.info(counter, "primer elemento agregado");
        counter ++;
    }else{
        if (!stop) {
            phoneform.classList.remove('not_visible');
            const structure_phone_form = phoneform.outerHTML;
            const create_form = document.createElement('div');
            create_form.innerHTML = structure_phone_form;
            create_form.setAttribute("id", counter);

            canvas.append(create_form);

            buttonadd.classList.remove('new-contact-li');
            buttonadd.classList.add('disabled-button');

            stop = true;
            counter= 2;
            console.info(counter, "ultimo elemento agregado");


        } else {
            console.log("Maximo de elementos agregados");
            console.info(counter, "Es el número máximo de formularios por evento")
        }
    }

    let removeButtons = document.querySelectorAll('.remove-phone');

    removeButtons.forEach(button => {
        button.addEventListener('click', e => {
            

            if (counter == 1 && !stop) {

                phoneform.classList.add('not_visible');
                buttonadd.classList.remove('disabled-button');
                buttonadd.classList.add('new-contact-li');
                counter = 0;
                console.log('Pirmera opción de eliminar')

            }else if(stop && counter == 2){

                let lastForm = document.getElementById('1');
                lastForm.remove();
                buttonadd.classList.remove('disabled-button');
                buttonadd.classList.add('new-contact-li');

                console.log('Segunda opción de eliminar')
                stop = false;
                counter = 2;
            
            }else if(counter == 2 && !stop){
                counter = 1;
            }
        });
    });
});




//getElementById('remove-phone')