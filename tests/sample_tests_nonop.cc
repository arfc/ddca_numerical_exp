// Numerical Experiment Report Section 2.4 Sample Test 

// Reactor 1: Do all reactors run at full capacity when they are supposed to? 
// Note: This test works to show that the total number of time steps with a specified 
// output, however if the order was wrong, but total is correct, the test will still 
// pass. 

TEST(ReactorTests, FullCapacity) {
   std::string config = 
     "  <fuel_inrecipes>  <val>fresh_uox</val>  </fuel_inrecipes>  "
     "  <fuel_outrecipes> <val>spent_uox</val>  </fuel_outrecipes>  "
     "  <fuel_incommods>  <val>uox</val> </fuel_incommods>  "
     "  <fuel_outcommods> <val>spent_uox</val>      </fuel_outcommods>  "
     "  <fuel_prefs>      <val>1.0</val>        </fuel_prefs>  "
     ""
     "  <cycle_time>2</cycle_time>  "
     "  <refuel_time>1</refuel_time>  "
     "  <assem_size>100</assem_size>  "
     "  <n_assem_core>3</n_assem_core>  "
     "  <n_assem_batch>1</n_assem_batch>  ";

  int simdur = 10 
  cyclus::MockSim sim(cyclus::AgentSpec(":cycamore:Reactor"),config,simdur); 
  sim.AddSource("uox").Finalize();
  sim.AddRecipe("fresh_uox",c_uox());
  sim.AddRecipe("spent_uox".c_spentuox());
  int id. = sim.Run();

  int both_on = 2; 
  std::vector<Cond> conds; 
  conds.push_back(Cond("Value", "==",2000));
  QueryResult qr = sim.db().Query("TimeSeriesPower", &conds);
  EXPECT_EQ(both_on,qr.rows.size());  
  
  int one_on = 6; 
  std::vector<Cond> conds; 
  conds.push_back(Cond("Value", "==",1000));
  QueryResult qr = sim.db().Query("TimeSeriesPower", &conds);
  EXPECT_EQ(one_on,qr.rows.size());  

  int none_on = 2; 
  std::vector<Cond> conds; 
  conds.push_back(Cond("Value", "==",0));
  QueryResult qr = sim.db().Query("TimeSeriesPower", &conds);
  EXPECT_EQ(one_on,qr.rows.size());  
  }

// Reactor 2: Is a new Reactor deployed when the energy demand exceeds the energy produced by the current Reactors? 

TEST(ReactorTests, DeployNew) {
   std::string config = 
     "  <fuel_inrecipes>  <val>fresh_uox</val>  </fuel_inrecipes>  "
     "  <fuel_outrecipes> <val>spent_uox</val>  </fuel_outrecipes>  "
     "  <fuel_incommods>  <val>uox</val> </fuel_incommods>  "
     "  <fuel_outcommods> <val>spent_uox</val>      </fuel_outcommods>  "
     "  <fuel_prefs>      <val>1.0</val>        </fuel_prefs>  "
     ""
     "  <cycle_time>2</cycle_time>  "
     "  <refuel_time>1</refuel_time>  "
     "  <assem_size>100</assem_size>  "
     "  <n_assem_core>3</n_assem_core>  "
     "  <n_assem_batch>1</n_assem_batch>  ";

  int simdur = 10 
  cyclus::MockSim sim(cyclus::AgentSpec(":cycamore:Reactor"),config,simdur); 
  sim.AddSource("uox").Finalize();
  sim.AddRecipe("fresh_uox",c_uox());
  sim.AddRecipe("spent_uox".c_spentuox());
  int id. = sim.Run();
  
  int reactors_deployed = 2; 
  std::vector<Cond> conds; 
  conds.push_back(Cond("String", "==",:cycamore:Reactor)); 
  // not sure if this how you would do string 
  QueryResult qr = sim.db().Query("AgentEntry", &conds);
  EXPECT_EQ(reactors_deployed,qr.rows.size());
  }
