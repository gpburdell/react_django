import { Container } from 'react-bootstrap';
import { BrowserRouter as Router, Route } from 'react-router-dom'
import Footer from './components/Footer';
import Header from './components/Header';

import HomeScreen from './screens/HomeScreen'
import ProductScreen from './screens/ProductScreen'

import LoginScreen from './screens/LoginScreen'
import RegisterScreen from './screens/RegisterScreen'

import PlotScreen from './screens/PlotScreen'
import PlotScreen2 from './screens/PlotScreen2'
import PlotScreen3 from './screens/PlotScreen3'
import PlotScreen_ny17 from './screens/PlotScreen_ny17'
import PlotScreen_lulling from './screens/PlotScreen_lulling'
import PlotScreen_danz from './screens/PlotScreen_danz';

function App() {
  return (
    <Router>
      <Header />
      <main className='py-3'>
        <Container>

          <Route path='/' component={PlotScreen_lulling} exact />
          <Route path='/product/:id' component={ProductScreen} />
          <Route path='/login' component={LoginScreen} />
          <Route path='/register' component={RegisterScreen} />

          
          <Route path='/plot/' component={PlotScreen}  />

          <Route path='/plot2/:gage' component={PlotScreen2}  />
          <Route path='/plot3/' component={PlotScreen3}  />
          <Route path='/luling/' component={PlotScreen_lulling}  />
          <Route path='/danziger/' component={PlotScreen_danz}  />
          <Route path='/plotny17/' component={PlotScreen_ny17} exact />

        </Container>
      </main>
      <Footer />
    </Router>
  )
}

export default App;
