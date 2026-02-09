Petri Net Concurrency Simulator                                                                                                   
                                                                                                                                    
  Project Description                                                                                                               
                                                                                                                                    
  A Python-based CPU instruction pipeline simulator that uses Petri net modeling to demonstrate concurrency concepts. The simulator 
  models instruction flow through various pipeline stages over clock cycles, visualizing how data moves through a CPU architecture. 
                                                                                                                                    
  Pipeline Components (Places):                                                                                                     
  - INM - Instruction Memory                                                                                                        
  - INB - Instruction Buffer                                                                                                        
  - RGF - Register File                                                                                                             
  - AIB - ALU Input Buffer                                                                                                          
  - LIB - Load Input Buffer                                                                                                         
  - ADB - Address Data Buffer                                                                                                       
  - REB - Result Buffer                                                                                                             
  - DAM - Data Memory                                                                                                               
                                                                                                                                    
  Transitions:                                                                                                                      
  - DECODE - Fetch instructions from memory                                                                                         
  - ISSUE1/ISSUE2 - Route operations to execution units                                                                             
  - ALU - Execute arithmetic operations (AND, SUB, ADD, OR)                                                                         
  - ADDR - Calculate memory addresses                                                                                               
  - LOAD - Retrieve data from memory                                                                                                
  - WRITE - Update registers with results                                                                                           
                                                                                                                                    
  Screenshots                                                                                                                       
                                                                                                                                    
  Coming soon                                                                                                                       
                                                                                                                                    
  How to Run It                                                                                                                     
                                                                                                                                    
  Prerequisites                                                                                                                     
                                                                                                                                    
  - Python 3.x                                                                                                                      
                                                                                                                                    
  Configuration                                                                                                                     
                                                                                                                                    
  Provide input data in the following files:                                                                                        
  - instructions.txt - CPU instructions to execute                                                                                  
  - registers.txt - Initial register values                                                                                         
  - datamemory.txt - Initial data memory state                                                                                      
                                                                                                                                    
  Usage                                                                                                                             
                                                                                                                                    
  python script.py                                                                                                                  
                                                                                                                                    
  The simulator will execute the pipeline over multiple clock cycles, displaying the state of each component after each cycle.      
                                                                                                                                    
  Technologies Used                                                                                                                 
                                                                                                                                    
  - Python                                                                                                                          
                                                                                                                                    
  What I Learned                                                                                                                    
                                                                                                                                    
  - Simulating Hardware in Software - Modeling physical CPU components and their interactions programmatically, understanding how   
  instruction pipelines process data through discrete stages                                                                        
  - State Machine Design - Implementing a token-based state system where data flows between places via transitions, tracking state  
  changes across clock cycles                                                                                                       
  - Concurrency Concepts - Applying Petri net theory with tokens (data units), places (pipeline stages), and transitions            
  (operations) to model parallel execution paths in a single cycle program                       
