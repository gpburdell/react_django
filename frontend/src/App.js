import { Container } from 'react-bootstrap';
import { BrowserRouter as Router, Route } from 'react-router-dom'
import Footer from './components/Footer';
import Header from './components/Header';

import HomeScreen from './screens/HomeScreen'
import ProductScreen from './screens/ProductScreen'

import LoginScreen from './screens/LoginScreen'

import PlotScreen from './screens/PlotScreen'
import PlotScreen2 from './screens/PlotScreen2'
import PlotScreen_ny17 from './screens/PlotScreen_ny17'

function App() {
  return (
    <Router>
      <Header />
      <main className='py-3'>
        <Container>

          <Route path='/' component={HomeScreen} exact />
          <Route path='/product/:id' component={ProductScreen} />
          <Route path='/login' component={LoginScreen} />
          <Route path='/plot/' component={PlotScreen}  />

          <Route path='/plot2/:gage' component={PlotScreen2}  />
          <Route path='/plotny17/' component={PlotScreen_ny17} exact />

        </Container>
      </main>
      <Footer />
    </Router>
  )
}

export default App;
