import React,{useState, useEffect} from 'react'
import Graph3 from '../components/Plotv3'
import { useParams } from 'react-router-dom'
import Loader from '../components/Loader'

function PlotScreen3() {
  const {gage} = useParams();
  return (
    
    <div>
      <Loader />
      <Graph3 gage={gage}/>
      <Graph3 gage={'temp_40_avg'}/>

    </div>
  )

}

export default PlotScreen3
