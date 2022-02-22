import React from 'react'
import Graph_danziger_TS from '../components/Plotv_danziger'

function PlotScreen_danz() {
  return (
    <div>
      <h1>Danziger Digest</h1>

      <Graph_danziger_TS gagelist= {{"primary" : [ "lse_ultra_in_med","tse_ultra_in_med"] ,"secondary" : [ "temp_ambient_avg"]}} dateRange={{"dateRange" : [ '2022-02-07 00:00:00', '2022-02-15 00:00:00'] }} table={'Dan602'} />

      <Graph_danziger_TS gagelist= {{"primary" : [ "vse_med"] ,"secondary" : [ "temp_ambient_avg"]}} dateRange={{"dateRange" : [ '2022-02-07 00:00:00', '2022-02-15 00:00:00'] }} table={'Dan602'} />

      <Graph_danziger_TS gagelist= {{"primary" : [ "vne_med"] ,"secondary" : [ "se_shoe_avg"]}} dateRange={{"dateRange" : [ '2022-02-07 00:00:00', '2022-02-15 00:00:00'] }} table={'Dan502'} />
    </div>
  )


}

export default PlotScreen_danz
