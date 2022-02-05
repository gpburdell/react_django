import React, { useState } from 'react';
import Plot from 'react-plotly.js';


class Graph  extends React.Component {
  state = {};
  

  async reload () {
      // let url = 'http://localhost:8000/api/csi'
      let url = '/api/csi'
      const res = await fetch(url);
      const info = await res.json();
      console.log(info)
      this.setState({
        tmstamp: info.tmstamp,
        measure_avg: info.measure_avg,
      });
      
  }

  async componentDidMount() {
      this.reload();
  }

  render() {
    return (
        <Plot
        data={[
          // {
          //   x: this.state.tmstamp,
          //   y: this.state.measure_avg,
          //   type: 'scatter',
          //   mode: 'points-lines',
          //   marker: {color: 'red'},
          // },
          {
            x: ['2015-02-01', '2015-02-02', '2015-02-03', '2015-02-04', '2015-02-05',
                '2015-02-06', '2015-02-07', '2015-02-08', '2015-02-09', '2015-02-10',
                '2015-02-11', '2015-02-12', '2015-02-13', '2015-02-14', '2015-02-15',
                '2015-02-16', '2015-02-17', '2015-02-18', '2015-02-19', '2015-02-20',
                '2015-02-21', '2015-02-22', '2015-02-23', '2015-02-24', '2015-02-25',
                '2015-02-26', '2015-02-27', '2015-02-28'],
            y: [-14, -17, -8, -4, -7, -10, -12, -14, -12, -7, -11, -7, -18, -14, -14,
                -16, -13, -7, -8, -14, -8, -3, -9, -9, -4, -13, -9, -6],
            mode: 'line',
            name: 'temperature'
          }
        ]}
        layout={ {

          // to highlight the timestamp we use shapes and create a rectangular
      
          shapes: [
              // 1st highlight during Feb 4 - Feb 6
              {
                  type: 'rect',
                  // x-reference is assigned to the x-values
                  xref: 'x',
                  // y-reference is assigned to the plot paper [0,1]
                  yref: 'paper',
                  x0: '2015-02-04',
                  y0: 0,
                  x1: '2015-02-06',
                  y1: 1,
                  fillcolor: 'rgb(76, 76, 161)',
                  opacity: 0.2,
                  line: {
                      width: 0
                  }
              },
      
              // 2nd highlight during Feb 20 - Feb 23
              
              {
                  type: 'rect',
                  xref: 'x',
                  yref: 'paper',
                  x0: '2015-02-20',
                  y0: 0,
                  x1: '2015-02-22',
                  y1: 1,
                  fillcolor: 'rgb(76, 76, 161)',
                  opacity: 0.2,
                  line: {
                      width: 0
                  }
              }
          ],
          height: 500,
          width: 1000
      }
       }


      />

    );
  }
}

export default Graph 