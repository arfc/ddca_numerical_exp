# ddca_numerical_exp
Numerical Experiment for CYCLUS Demand-Driven Deployment 

hi The repository is part of an effort to add demand-driven deployment
capabilities into the [CYCLUS](github.com/cyclus/cyclus) framework.
PI: Kathryn Huff

## Assume the algorithm is an INSTITUTION.

## GIVEN:
    all prototype definitions and parameters
        - reprocessing capacity of one facility
        - reprocessing efficiency
        - reactor specifications
        - enrichment capacity / tails assay
        - spent / fresh fuel compositions

### Non-optimizing
- If it `predicts' the fuel demand correctly ( given the past, )
- Does all the reactors run? (timeseriespower =! 0 if not in refueling)
- Does it deploy facilities when it sees we need more capacity? 
- Does it track demand?

### Deterministic-Optimizing
- Are the constraints met?
- The objective function is maximized?
- Same result every time?

### Commodity Flow
Power / Advanced Reactor Deployment -> mox_fuel (fuel for advanced reactors) -> spent fuel (Pu / Fissile) -> Reprocessing Capacity
-> uox -> uox fabrication capacity -> uox enrichment capacity -> natural u

### Example Objective Function
2% nuclear electricity generation annually, starting from x 
P = x*(1.02)^(t/12)
