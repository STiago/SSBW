// components/Recipe.js
import React, { Component } from 'react'
import logo from './logo.svg';
import './App.css';

class Recipe extends Component {

	render() {

	var recipe = this.props.recipe   // props desde el componente de arriba
	return(
	   <div key={recipe.id}>
	      <h3>{recipe.name}</h3>
	      <img src={"https://localhost/recipes_dashboard/imagen_de/" + recipe.id} alt=""/>
	      {recipe.id},{" "}, {recipe.tags}
	      <hr />
	   </div>
	  )
	}
}

export default Recipe
