import React,{useState, useEffect} from 'react'
import Graph2 from '../components/Plotv2'
import { useParams } from 'react-router-dom'


function PlotScreen2() {
  const {gage} = useParams();
  return (
    
    <div>
      <h1>Latest products</h1>
      <Graph2 gage={gage}/>
      <Graph2 gage={'temp_40_avg'}/>
    </div>
  )

}

export default PlotScreen2
