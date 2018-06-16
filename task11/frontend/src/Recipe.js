// components/Recipe.js
import React, { Component } from 'react'

import { connect } from 'react-redux'
import { Eliminar } from './actions'

class Recipe extends Component {

	handleBorrar(id) {
	   this.props.EliminaRecipe(id) // subscrita como props
	}

	render() {

	var recipe = this.props.recipe   // props desde el componente de arriba
	return(
	   <div key={recipe.id}>
	      <h3>{recipe.name}</h3>
	      <img src={"https://localhost/recipes_dashboard/get_recipe_image/" + recipe.id} width="400" height="300" alt="Image"/>
	      <p>ID: {recipe.id}</p>
		  <p>Tags: {recipe.tags}</p>
		  <button onClik={()=>this.handleBorrar(recipe.id)}>Delete</button>
	      <hr/>
	   </div>
	  )
	}
}

// Apply actions js
function mapDispatchToProps(dispatch) {
	return {
		EliminaRecipe: (id) => {dispatch(Eliminar(id))},
   }
}

// recibir cambios en el componente en props.id_deleted
function mapStateToProps(state) {
  return {
	  id_deleted: state.MyReducer.id_deleted,
  }
}

export default connect (
  mapStateToProps,
  mapDispatchToProps
)(Recipe)

//export default Recipe
