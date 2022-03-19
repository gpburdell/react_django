import React,{useState, useEffect} from 'react'
import Graph3 from '../components/Plotv3'
import { useParams } from 'react-router-dom'
import Loader from '../components/Loader'

function PlotScreen3() {
  // const {gagelist} = useParams();
  return (
    
    
    <div>
      <Loader />
      <Graph3 gagelist= {{"primary" : [ "laser_18_avg", "laser_19_avg"] ,"secondary" : [ "temp_40_avg"]}} dateRange={{"dateRange" : [ '2022-01-01 00:00:00', '2022-02-16 00:00:00'] }}/>
      {/* <Graph3 gagelist={['temp_40_avg']}/> */}

    </div>
  )

}

export default PlotScreen3
