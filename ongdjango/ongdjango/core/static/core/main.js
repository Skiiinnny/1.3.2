

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
$(document).ready(function () {
    $('#btn-limpiar').click( function () {
        $('#form').load('core/contactos.html #form');
        return false;
    });

});


