// src/actions.js
export const ELIMINAR = 'ELIMINAR'

export const Eliminar = (id) => {    // arrow function
	return {
		type: ELIMINAR,                // obligatorio
		id                             // por id:id (del ES6), info adicional
	}
}
		  
