import React, { Component } from 'react';
import Head from 'next/head'
import Link from 'next/link'
import '../styles/styles.sass'

export default  class Layout extends Component {

  componentDidMount() {
    console.log(this.props)
  }
  render(){
    const {children} = this.props
    return (
      <div>
        <Head>
          <title>Diputados</title>
          <meta name="viewport" content="initial-scale=1.0, width=device-width" />
        </Head>

        <header>
          <nav className="navbar" role="navigation" aria-label="main navigation">
            <div className="navbar-brand">
              <a className="navbar-item">
                Diputado
              </a>
              <a id="burger"
                role="button" className="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbarmenu">
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
              </a>
            </div>
            {/* <div id="navbarmenu" className="navbar-menu">
              <div className="navbar-start">
                <Link prefetch href="/">
                  <a className="navbar-item">Home</a>
                </Link>
                <Link prefetch href="/elsewhere">
                  <a className="navbar-item">Elsewhere</a>
                </Link>
              </div>
              <div className="navbar-end">
                <div className="navbar-item">
                  <div className="buttons">
                    <a onClick={() => alert('You clicked the button!')} className="button is-primary">Click</a>
                  </div>
                </div>
              </div>
            </div> */}
          </nav>
        </header>
        <div className="container">
          {children}
        </div>
        {/* <footer className="footer">
        <div className="content has-text-centered">
          <span>Diputaditos</span>
        </div>
      </footer> */}
      </div> 
    )
  }
}