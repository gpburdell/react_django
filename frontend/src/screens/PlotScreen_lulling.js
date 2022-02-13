import React,{useState, useEffect} from 'react'
import Graph_lulling_TS from '../components/Plotv_lulling1'
import { useParams } from 'react-router-dom'
import Loader from '../components/Loader'

function PlotScreen_lulling() {
  // const {gagelist} = useParams();
  return (
    
    <div>
      <h1>Lulling Raw Plots</h1>
      <h3>Lulling Logger1</h3>
      <Loader />
      <Graph_lulling_TS gagelist= {{"primary" : [ "vr1000_s_1", "vr1000_s_2"] ,"secondary" : [ "sys1_temp_c_s"]}} dateRange={{"dateRange" : [ '2022-02-10 00:00:00', '2022-02-14 00:00:00'] }} table={'L1'} />
      <Graph_lulling_TS gagelist= {{"primary" : [ "vr1000_e_1", "vr1000_e_2"] ,"secondary" : [ "sys1_temp_c_s"]}} dateRange={{"dateRange" : [ '2022-02-10 00:00:00', '2022-02-14 00:00:00'] }} table={'L1'} />


      <Graph_lulling_TS gagelist= {{"primary" : [ "vr1000_s_1", "vr1000_s_2","vr1000_c_3","vr1000_c_4"] ,"secondary" : [ "sys1_temp_c_s"]}} dateRange={{"dateRange" : [ '2022-02-10 00:00:00', '2022-02-14 00:00:00'] }} table={'L1'} />

      <Graph_lulling_TS gagelist= {{"primary" : [ "sys1_loc2_strain_s", "sys1_loc1_strain_e","sys1_loc2_strain_e","sys1_loc1_strain_c1"] ,"secondary" : [ "sys1_temp_c_s"]}} dateRange={{"dateRange" : [ '2022-02-10 00:00:00', '2022-02-14 00:00:00'] }} table={'L1'} />

      <p>Note this plot is temps, but I have report as displacement, jut need to update customization of naming</p>
      <Graph_lulling_TS gagelist= {{"primary" : [ "sys1_temp_c_s", "sys1_temp_c_e","sys1_temp_c_c1","sys1_temp_c_c2"] ,"secondary" : [ "sys1_temp_c_s"]}} dateRange={{"dateRange" : [ '2022-02-10 00:00:00', '2022-02-14 00:00:00'] }} table={'L1'} />

      <h3>Lulling Logger2</h3>

      <Graph_lulling_TS gagelist= {{"primary" : [ "vr1000_s_1", "vr1000_s_2"] ,"secondary" : [ "sys2_temp_c_s"]}} dateRange={{"dateRange" : [ '2022-02-10 00:00:00', '2022-02-14 00:00:00'] }} table={'L2'} />
      <Graph_lulling_TS gagelist= {{"primary" : [ "vr1000_e_1", "vr1000_e_2"] ,"secondary" : [ "sys2_temp_c_s"]}} dateRange={{"dateRange" : [ '2022-02-10 00:00:00', '2022-02-14 00:00:00'] }} table={'L2'} />


      <Graph_lulling_TS gagelist= {{"primary" : [ "vr1000_c_1", "vr1000_c_2","vr1000_c_3","vr1000_c_4"] ,"secondary" : [ "sys2_temp_c_s"]}} dateRange={{"dateRange" : [ '2022-02-10 00:00:00', '2022-02-14 00:00:00'] }} table={'L2'} />

      <Graph_lulling_TS gagelist= {{"primary" : [ "sys2_loc1_strain_c1", "sys2_loc1_strain_c2","sys2_loc2_strain_c1","sys2_loc2_strain_c2"] ,"secondary" : [ "sys2_temp_c_s"]}} dateRange={{"dateRange" : [ '2022-02-10 00:00:00', '2022-02-14 00:00:00'] }} table={'L2'} />

      <p>Note this plot is temps, but I have report as displacement, jut need to update customization of naming</p>
      <Graph_lulling_TS gagelist= {{"primary" : [ "sys2_temp_c_s", "sys2_temp_c_e","sys2_temp_c_c1","sys2_temp_c_c1"] ,"secondary" : [ "sys2_temp_c_s"]}} dateRange={{"dateRange" : [ '2022-02-10 00:00:00', '2022-02-14 00:00:00'] }} table={'L2'} />

      <h3>Lulling Logger3</h3>

      <Graph_lulling_TS gagelist= {{"primary" : [ "vr1000_s_1", "vr1000_s_2"] ,"secondary" : [ "sys3_temp_c_s"]}} dateRange={{"dateRange" : [ '2022-02-10 00:00:00', '2022-02-14 00:00:00'] }} table={'L3'} />

      <Graph_lulling_TS gagelist= {{"primary" : [ "vr1000_e_1", "vr1000_e_2"] ,"secondary" : [ "sys3_temp_c_s"]}} dateRange={{"dateRange" : [ '2022-02-10 00:00:00', '2022-02-14 00:00:00'] }} table={'L3'} />


      <Graph_lulling_TS gagelist= {{"primary" : [ "vr1000_c_1", "vr1000_c_2","vr1000_c_3","vr1000_c_4"] ,"secondary" : [ "sys3_temp_c_s"]}} dateRange={{"dateRange" : [ '2022-02-10 00:00:00', '2022-02-14 00:00:00'] }} table={'L3'} />

      <Graph_lulling_TS gagelist= {{"primary" : [ "sys3_loc2_strain_s", "sys3_loc1_strain_e","sys3_loc2_strain_e","sys3_loc1_strain_c1","sys3_loc3_strain_s"] ,"secondary" : [ "sys3_temp_c_s"]}} dateRange={{"dateRange" : [ '2022-02-10 00:00:00', '2022-02-14 00:00:00'] }} table={'L3'} />

      <p>Note this plot is temps, but I have report as displacement, jut need to update customization of naming</p>
      <Graph_lulling_TS gagelist= {{"primary" : [ "sys3_temp_c_s", "sys3_temp_c_e","sys3_temp_c_c1","sys3_temp_c_c2"] ,"secondary" : [ "sys3_temp_c_s"]}} dateRange={{"dateRange" : [ '2022-02-10 00:00:00', '2022-02-14 00:00:00'] }} table={'L3'} />
 

    </div>
  )

}

export default PlotScreen_lulling
