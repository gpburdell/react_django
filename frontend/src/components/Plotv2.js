import React, { useState } from 'react';
import Plot from 'react-plotly.js';


class Graph  extends React.Component {
  constructor(props) {
    super(props);
    const gage = ''
    this.state = {data: [], layout: {}, frames: [], config: {}};
  }
  

  async reload () {
      // let url = 'http://localhost:8000/api/csi'
      const gage ='laser_18_avg'
      let url = '/api/ny17gage/'+gage
      const res = await fetch(url);
      const info = await res.json();
      console.log(info)
      this.setState({
        tmstamp: info.tmstamp,
        gage: info.gage,
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
            x: this.state.tmstamp,
            y: this.state.gage,
            type: 'scatter',
            // mode: 'points-lines',
            marker: {color: 'red'},
          mode: 'line',
          name: 'temperature'
          },

        ]}
        layout={ {

          // to highlight the timestamp we use shapes and create a rectangular
      
          
          height: 500,
          width: 1000
      }
       }


      />

    );
  }
}

export default Graph 