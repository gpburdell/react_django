import React from 'react'
import { Navbar, Nav, Container, Row } from 'react-bootstrap'
import {LinkContainer} from 'react-router-bootstrap'

function Header() {
  return (
    <header>
      <Navbar bg="dark" variant='dark' expand="lg" collapseOnSelect>
      <Container>
        <LinkContainer to='/'>
          <Navbar.Brand href="/">WJE Analytics</Navbar.Brand>
        </LinkContainer>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="mr-left">
          <LinkContainer to='/cart'>
            <Nav.Link><i className='fas fa-shopping-cart'></i>Test1</Nav.Link>
            </LinkContainer>
            <LinkContainer to='/login'>
            <Nav.Link><i className='fas fa-user'></i>Login</Nav.Link>
            </LinkContainer>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
    </header>
  )
}

export default Header
