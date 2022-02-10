import React,{useState, useEffect} from 'react'
import Graph3 from '../components/Plotv3'
import { useParams } from 'react-router-dom'


function PlotScreen3() {
  const {gage} = useParams();
  return (
    
    <div>
      <h1>Latest products</h1>
      <Graph3 gage={gage}/>

    </div>
  )

}

export default PlotScreen3
