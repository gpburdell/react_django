import React, { useState } from 'react';
import Plot from 'react-plotly.js';



class Graph3  extends React.Component {
  constructor(props) {
    super(props);
    
    this.state = {gage: '',data: [], layout: {}, frames: [], config: {}};
  }
  
  async reload () {
      // let url = 'http://localhost:8000/api/csi'
      // console.log(this.props.gage)

      //URL URL
      let url = 'http://localhost:8000/api/nyc/gage/'+this.props.gage
      console.log(this.state.gage)
      const res = await fetch(url);
      const info = await res.json();
      console.log(info)
      this.setState({
        data: info.data,
        layout: info.layout
      });
      
  }

  async componentDidMount() {
      this.reload();
  }

  render() {
    return (
        <Plot
        data= {this.state.data }
        layout={ this.state.layout}

      />

    );
  }
}

export default Graph3