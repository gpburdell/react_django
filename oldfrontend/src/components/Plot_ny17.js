import React, { useState } from 'react';
import Plot from 'react-plotly.js';


class Graph extends React.Component {
  state = {};
  

  async reload () {
      // let url = 'http://localhost:8000/api/ny17'
      let url = 'http://localhost:8000/api/nyc/api/ny17'
      const res = await fetch(url);
      const info = await res.json();
      console.log(info)
      this.setState({
        tmStamp: info.amStamp,
        laser_18_avg: info.laser_18_avg,
      });
      
  }

  async componentDidMount() {
      this.reload();
  }

  render() {
    return (
        <Plot
        data={[
          {
            x: this.state.tmStamp,
            y: this.state.laser_18_avg,
            type: 'scatter',
            mode: 'points-lines',
            marker: {color: 'red'},
          },
        ]}
        layout={ {width: 800, height: 480, title: 'Laser plot'} }
      />

    );
  }
}

export default Graph 