import React, { useState } from 'react';
import Plot from 'react-plotly.js';



class Graph3  extends React.Component {
  constructor(props) {
    super(props);
    
    this.state = {gagelist: {},dateRange: [], data: [], layout: {}, frames: [], config: {}};
    
  }
  
  async reload () {
      // let url = 'http://localhost:8000/api/csi'
      // console.log(this.props.gage)
      
      //URL URL
      // let url = 'http://localhost:8000/api/nyc/gage/'+this.props.gage
      let url = 'http://localhost:8000/api/nyc/gage/'
      console.log('inside reload')
      console.log(this.props.gagelist)
      let date="2022-01-01 00:00:00"
      // const res = await fetch(url);
      // 
      const response = await fetch(url,{
            method:'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            
            body: JSON.stringify({'gagelist': this.props.gagelist, 'dateRange':this.props.dateRange})
        })
      console.log(this.state.gagelist)
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

export default Graph3