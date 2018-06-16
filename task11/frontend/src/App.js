// components/App.js
import React, { Component } from 'react'
import {Route} from 'react-router-dom'
import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
  } from 'reactstrap'

import Todas from './Todas'
import logo from './logo.svg';
import './App.css';
import { connect } from 'react-redux'


class App extends Component {
  constructor(props) {
	   super(props)
	   this.state = {
	      isOpen: false  // para navbar
	    }
  }

	toggle = () => {
	   this.setState({
	     isOpen: !this.state.isOpen  // de navbar
	   })
  }
  

	 render() {
	   return (            // código JSX
		  <div className="App">
		    <div className="App-header">
		      <img src={logo} className="App-logo" alt="logo" />
		      <h2>My Recipes Instagram</h2>
		    </div>
		    <div>
			   <Navbar color="light" light expand="md">
				 <NavbarBrand href="/"> Click to hide the pictures</NavbarBrand>
			     <NavbarToggler onClick={this.toggle} />
			     <Collapse isOpen={this.state.isOpen} navbar>
			       <Nav className="ml-auto" navbar>
			         <NavItem>
			           <NavLink href="/all_recipes">Click to show all the pictures</NavLink>
			         </NavItem>
					 <NavItem>
			   			Picture ID: {this.props.id_deleted} 
			 		 </NavItem>
			       </Nav>
			     </Collapse>
			   </Navbar>
			 <Route path="/all_recipes" component={Todas}/>
			 </div>
		  </div>
	   )
	 }
}

// Aplicar actions
function mapDispatchToProps(dispatch) {
   return { }
}

// Recibir cambios en el componente en props.id_deleted
function mapStateToProps(state) {
   return {
      id_deleted: state.MyReducer.id_deleted
   }
}

export default connect (
   mapStateToProps,
   mapDispatchToProps
)(App)
//export default App
