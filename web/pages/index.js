import React, { Component } from 'react'
import queryString from 'query-string'
import Layout from '../components/layout'
import axios from 'axios'
import ReactPaginate from 'react-paginate'
import Router from 'next/router';
export default class PageHome extends Component {

  constructor(props) {
    super(props)
    this.state = {
      query: {
        search: '',
        page: 1
      },
      total: null,
      diputados: []
    }
  }
  getData() {
    const url = 'http://localhost:8000/api/diputados/'
    const { query } = this.state
    axios.get(url, {
      params: {
        ...query
      }
    }).then(({ data }) => {
      Router.push({
        pathname: '/',
        query
      });
      this.setState({ diputados: data.results, total: data.count })
    })
  }
  search = () => {
    this.getData()
  }

  componentDidMount() {
    this.getData()
  }
  changePage = (event) => {
    const { selected } = event
    this.setState({
      query:{
        ...this.state.query,
        page:selected+1
      }
    }, ()=> {
        this.getData()
    })
  }
  render() {
    const { diputados, total, query: { search, page} } = this.state
    return (
      <Layout>
        <nav className="level">

          <div className="level-left">
            <div className="level-item">
              <p className="subtitle is-5"><strong>{total}</strong></p>
            </div>
            <div className="level-item">
              <div className="field has-addons">
                <p className="control">
                  <input className="input" value={search} onKeyPress={event => {
                    if (event.key === 'Enter') {
                      this.search()
                    }
                  }} onChange={e => this.setState({ query: { search: e.target.value } })} type="text" placeholder="Ingresa Nombre, Email" />
                </p>
                <p className="control">
                  <button onClick={() => this.search()} className="button">Buscar</button>
                </p>
              </div>
            </div>
          </div>
          <div className="level-right">
            <p className="level-item"><strong>All</strong></p>
            <p className="level-item"><a>Diputados</a></p>
            <p className="level-item"><a>Senadores</a></p>
          </div>
        </nav>
        <nav className="level">
          <div className="level-item has-text-centered">
            <div>
              <p className="heading">Diputados</p>
              <p className="title">3,456</p>
            </div>
          </div>
          <div className="level-item has-text-centered">
            <div>
              <p className="heading">Senadores</p>
              <p className="title">123</p>
            </div>
          </div>
          <div className="level-item has-text-centered">
            <div>
              <p className="heading">Propuestas</p>
              <p className="title">456K</p>
            </div>
          </div>
          <div className="level-item has-text-centered">
            <div>
              <p className="heading">Iniciativas</p>
              <p className="title">789</p>
            </div>
          </div>
        </nav>
        <table className="table is-fullwidth is-striped">
          <thead>
            <tr>
              <th></th>
              <th>Nombre</th>
              <th>Email</th>
              <th>Distrito / Circunscripción</th>
              <th>Entidad</th>
              <th>Partido</th>
            </tr>
          </thead>
          <tbody>
            {diputados &&
              diputados.map(diputado => (
                <tr key={diputado.id}>
                  <td>
                    <img width="40" style={{ borderRadius: '50%'}}src={diputado.image} />
                  </td>
                  <td>{diputado.name}</td>
                  <td>{diputado.email}</td>
                  <td>{diputado.distrit}</td>
                  <td>{diputado.entidad.name}</td>
                  <td><img width="35" src={diputado.partido.image} alt={diputado.partido.name}/></td>
                </tr>
              ))
            }
          </tbody>
        </table>
        <div className="columns">
          <div className="column is-half is-offset-one-quarter">
            <ReactPaginate
              pageCount={total / 10}
              previousLabel="Anterior"
              nextLabel="Siguiente"
              containerClassName="pagination is-centered"
              pageLinkClassName="pagination-link"
              activeLinkClassName="is-current"
              onPageChange={event => this.changePage(event)}
            />

          </div>

        </div>
      </Layout>
    )
  }

}