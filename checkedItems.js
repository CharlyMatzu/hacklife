Abrimos consola de navegador:

	Control + Mayus + J ó K




============================
ITESCA
============================
El formulario esta dentro de un "IFRAME", ya que no conocemos su nombre hay que accerder mediante "window.frame[0]", y al ser el primero y unico IFRAME obtenemos los que buscamos. Estando dentro del IFRAME, obtenemos los elementos por "Etiqueta" especificando el tipo "input" de la siguiente forma:

	document.getElementsByTagName("input");

Obtendremos un Array, de este hacemos un ciclo comparando por su valor ("A", "B", "C" o "D") y su atributo "checked" lo ponemos en "true"

	var elementos = window.frames[0].document.getElementsByTagName("input");
	for( var i=0; i<elementos.length; i++){ 
	     if ( elementos[i].value == "A" ) {
 		elementos[i].checked = true;
	     };
	};

Hacemos que el boton haga clic
	document.getElementsById("enviar").click();


============================
ITSON
============================

divCompetencia1 (id)
	|
	--- table
		|
		--- select (tagName)
			|
			---Values: 

boton enviar ---> id = btnSiguiente


document.getElementById("divCompetencia1");
document.getElementsByTagName("select");

selectedIndex 


var elementos = document.getElementsByTagName("select");
for( var i=0; i<elementos.length; i++){ 
     elementos[i].selectedIndex = 6;
};


var elementos = document.getElementsByTagName("select"); for(var i=0; i<elementos.length; i++){ elementos[i].selectedIndex = 6; document.getElementById("btnSiguiente");}	