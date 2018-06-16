// components/Todas.js
import React, { Component } from 'react'
import Recipe from './Recipe'

class Todas extends Component {
  constructor(props) {
    super(props)
    this.state = {
      recipes: []
     }
  }

componentDidMount() {
  fetch('https://localhost/recipes_dashboard/api/recipe/?format=json')
    .then(res => { return res.json()})
    .then(data => {
      console.log(data)
      this.setState({recipes:data})
    }).catch(error => {
      console.log(error)
    })

  }

  render() {
    // re-renderiza al cambiar el state
    return (
      <div>
        All our recipes: <br />
        {this.state.recipes.map(recipe => {
          return (
            <Recipe recipe={recipe} />
          )
        })
      }
      </div>
    )
  }

}

export default Todas
