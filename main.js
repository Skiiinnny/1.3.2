
function capturarDatos (){
    var campoRut = document.getElementById("identificador").value;
    
    return campoRut;

}
var datos =  capturarDatos();
console.log(datos);
// $("#formulario").submit(function () {  
//     if($("#nombre").val().length < 1) {  
//         alert("El nombre es obligatorio");  
//         return false;  
//     }  
//     return false;  
// });  