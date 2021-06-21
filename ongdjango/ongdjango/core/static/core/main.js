

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        jQuery('#geo').html('La localización no se pudo conseguir.');
    }
}

function showPosition(position) {
    var latitud = position.coords.latitude;
    var longitud = position.coords.longitude;
    var linkAPI = 'http://api.weatherapi.com/v1/current.json?key=261a3397a09c419cb67155250211405&q=';
    var linkFinal = linkAPI + latitud + ',' + longitud;
    jQuery.getJSON(linkFinal,
        function (data) {

            jQuery('#geo2').html(data.location.name + ', ' + data.location.country + ': ' + data.current.temp_c + ' °C');

        });

}

jQuery(document).ready(function () {
    // getLocation();

    jQuery('#btnClima').click(function () {
        getLocation();
    });
});



// function checkRut(rut) {
//                     rut = String(rut);
//                     var valor = rut.replace(".", "").replace(".", "");
//                     valor = valor.replace("-", "");
//                     cuerpo = valor.slice(0, -1);
//                     dv = valor.slice(-1).toUpperCase();
//                     rut = cuerpo + "-" + dv;
//                     if (cuerpo.length < 7) {
//                         return false;
//                     }
//                     suma = 0;
//                     multiplo = 2;
//                     for (i = 1; i <= cuerpo.length; i++) {
//                         index = multiplo * valor.charAt(cuerpo.length - i);
//                         suma = suma + index;
//                         if (multiplo < 7) {
//                             multiplo = multiplo + 1;
//                         } else {
//                             multiplo = 2;
//                         }
//                     }
//                     dvEsperado = 11 - suma % 11;
//                     dv = dv == "K" ? 10 : dv;
//                     dv = dv == 0 ? 11 : dv;
//                     if (dvEsperado != dv) {
//                         return false;
//                     }
//                     return true;
//                 }
//         $(
//             function () {
//                 $.validator.addMethod("rut", function(value, element){
//                     return checkRut(value);
//                 });
//                 $("#sendbtn").on("click",
//                     function () {
//                         $("#form").validate(
//                             {
//                                 rules: {
//                                     nombre: { required: true },
//                                     correo: { required: true },
//                                     ciudad: { required: true },
//                                     comentario: { required: true },
//                                     rut: { required: true, rut: true}

//                                 },
//                                 messages: {
//                                     nombre: {
//                                         required: 'Ingrese el nombre'
//                                     },
//                                     correo: {
//                                         required: 'Ingrese un correo valido'
//                                     },
//                                     ciudad: {
//                                         required: 'Ingrese la ciudad'
//                                     },
//                                     comentario: {
//                                         required: 'Ingrese su comentario'
//                                     },
//                                     rut: {
//                                         required: 'Ingrese rut o numero de pasaporte valido',
//                                         rut: 'Rut no validado'
//                                     }

//                                 }
//                             }


//                         );

//                     }
//                 );
//             }

//         );


