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
	     <div>
	       <Navbar color="light" light expand="md">
	         <NavbarBrand href="/"> My Recipes Instagram </NavbarBrand>
	         <NavbarToggler onClick={this.toggle} />
	         <Collapse isOpen={this.state.isOpen} navbar>
	           <Nav className="ml-auto" navbar>
	             <NavItem>
	               <NavLink href="/todas">All the pictures</NavLink>
	             </NavItem>
	           </Nav>
	         </Collapse>
	       </Navbar>
	     <Route path="/todas" component={Todas}/>
	     </div>
	   )
	 }
}
export default App
