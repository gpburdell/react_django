import React, { useState } from 'react';
import Plot from 'react-plotly.js';



class Graph2  extends React.Component {
  constructor(props) {
    super(props);
    
    this.state = {gage: '',data: [], layout: {}, frames: [], config: {}};
  }
  

  async reload () {
      
      // let url = 'http://localhost:8000/api/csi'
      // console.log(this.props.gage)

      //URL URL
      let url = 'http://localhost:8000/api/nyc/onegage/'+this.props.gage
      console.log(this.state.gage)
      console.log('inside....')
      const res = await fetch(url);
      const info = await res.json();
      console.log(info)
      this.setState({
        x: info.x,
        y: info.y,
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
            x: this.state.x,
            y: this.state.y,
            type: 'scatter',
            // mode: 'points-lines',
            marker: {color: 'red'},
          mode: 'line',
          name: 'laser18'
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



export default Graph2 