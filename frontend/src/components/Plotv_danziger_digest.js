import React, { useState } from 'react';
import Plot from 'react-plotly.js';



class Graph_Danziger_Digest  extends React.Component {
  constructor(props) {
    super(props);
    
    this.state = {gagelist: {},dateRange: [], table: '', data: [], layout: {}, frames: [], config: {}};
    
  }
  
  async reload () {
      // let url = 'http://localhost:8000/api/csi'
      // console.log(this.props.gage)
      
      //URL URL
      
      // let url = 'http://localhost:8000/api/lulling/gage/'
      let url = 'http://10.2.3.115:8000' +'/api/danziger/getCurrentData/'
      console.log('inside reload')
      

      // const res = await fetch(url);
      // 
      const response = await fetch(url);

      const info = await response.json();
      console.log(info)
      this.setState({
        data: info.data,
        layout: info.layout
      });

    //   const addFeedback = async (newFeedback) => {
    //     const response = await fetch('/feedback',{
    //         method:'POST',
    //         headers: {
    //             'Content-Type': 'application/json'
    //         },
    //         body: JSON.stringify(newFeedback)
    //     })
    //     const data = await response.json()

    //     setFeedback([data, ...feedback])
    // }
      
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

export default Graph_Danziger_Digest