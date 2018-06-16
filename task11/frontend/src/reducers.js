// src/reducers.js
import { combineReducers } from 'redux'

import { ELIMINAR } from './actions'

const initialState = {
	id_deleted: ''
}

const MyReducer  = (state=initialState, action) => {

	switch (action.type) {

 	  	case ELIMINAR:       // (... ES6 spread operator)
 			return {...state, id_deleted: action.id}

		default:
	   		return state
	}
}

const MyCombRed = combineReducers({
	MyReducer
})

export default MyCombRed
