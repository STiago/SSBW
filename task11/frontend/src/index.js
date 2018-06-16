import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './index.css';
import registerServiceWorker from './registerServiceWorker';
import { BrowserRouter} from 'react-router-dom';

import  { Provider } from 'react-redux';
import { createStore } from 'redux';
import MyCombRed from './reducers';

var store = createStore (MyCombRed);

ReactDOM.render(
 <Provider store={store}>
	<BrowserRouter>
		<App />
	</BrowserRouter>
	</Provider>
, document.getElementById('root'))
registerServiceWorker()



