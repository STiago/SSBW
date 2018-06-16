// components/Recipe.js
import React, { Component } from 'react'

class Recipe extends Component {

	render() {

	var recipe = this.props.recipe   // props desde el componente de arriba
	return(
	   <div key={recipe.id}>
	      <h3>{recipe.name}</h3>
	      <img src={"https://localhost/recipes_dashboard/get_recipe_image/" + recipe.id} width="400" height="300" alt="Image"/>
	      <p>ID: {recipe.id}</p>
		  <p>Tags: {recipe.tags}</p>
	      <hr/>
	   </div>
	  )
	}
}

export default Recipe
