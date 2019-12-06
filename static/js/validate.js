function ValidarDatos(){
    if(document.form_misperris.selectregion.value==0){
        alert("Debe seleccionar región.");
    }

    if(document.form_misperris.selectciudad.value==0){
        alert("Debe seleccionar ciudad.");
    }

    if(document.form_misperris.selectvivienda.value==0){
        alert("Debe seleccionar tipo de vivienda.");
    }
    var d = new Date(document.form_misperris.fecha.value);

    if(d.getFullYear()>2001){
        alert("Año de nacimiento debe ser anterior a 2001.");
    }

    var texto = document.form_misperris.correo.value;
        var regex = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;
        
        if (!regex.test(texto)) {
            alert("Correo invalido");
        } else {
          alert("ok");
        }
}

function SoloNumeros(evt){
    if(window.event){//asignamos el valor de la tecla a keynum
    keynum = evt.keyCode; //IE
    }
    else{
    keynum = evt.which; //FF
    } 
    //comprobamos si se encuentra en el rango numérico y que teclas no recibirá.
    if((keynum > 47 && keynum < 58) || keynum == 8 || keynum == 13 || keynum == 6 ){
    return true;
    }
    else{
        alert('Campo solo de numeros.');
    return false;
    }
}

function soloLetras(e) {
    key = e.keyCode || e.which;
    tecla = String.fromCharCode(key).toString();
    letras = " áéíóúabcdefghijklmnñopqrstuvwxyzÁÉÍÓÚABCDEFGHIJKLMNÑOPQRSTUVWXYZ";//Se define todo el abecedario que se quiere que se muestre.
    especiales = [8, 37, 39, 46, 6]; //Es la validación del KeyCodes, que teclas recibe el campo de texto.

    tecla_especial = false
    for(var i in especiales) {
        if(key == especiales[i]) {
            tecla_especial = true;
            break;
        }
    }

    if(letras.indexOf(tecla) == -1 && !tecla_especial){
       alert('Campo solo de letras.');
        return false;
    }
}

function soloK(e) {
    key = e.keyCode || e.which;
    tecla = String.fromCharCode(key).toString();
    letras = "kK1234567890-";//Se define todo el abecedario que se quiere que se muestre.
    especiales = [8, 37, 39, 46, 6]; //Es la validación del KeyCodes, que teclas recibe el campo de texto.

    tecla_especial = false
    for(var i in especiales) {
        if(key == especiales[i]) {
            tecla_especial = true;
            break;
        }
    }

    if(letras.indexOf(tecla) == -1 && !tecla_especial){
       alert('Solo letra K.');
        return false;
    }
}
