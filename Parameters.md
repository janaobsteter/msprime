
# PopulationConfiguration

* sample_size: number of sampled monoploid genomes
* Ne: effective (diploid) population size (default = 1)
* length: length of simulated region in bases (cannot be used with recombination_map)
        * . (So, although we recommend setting the units of length to be analogous to “bases”, events can occur at fractional positions.)
* recombination_rate: per base per generation
* recombination_map
* mutation_rate: The rate of infinite sites mutations per unit of sequence length per generation. (default = no mutations)
    * only binary(0,1) alphabet, mutate() for more control
* population configuration <list>: sampling configuration, relative sites nad growth rates (for subpopulations!)
* demographic events <list>:
    * PopulationParametersChange:
        * time: length of time AGO when event occured
        * initial_size: absolute diploid size of the population before demographic event
        * growth rate: new per-generation growth rate
        * population: ID of the population (if None = all population)
    * MigrationRateChange
    * MassMigration
    * SimulationModelChange
        * time
        * model: new simulation model to use
    * CensusEvent: adds node to each branch of every tree at a given time during the simulation

* samples <list>: specifying the location and time of all samples (population, time) pair. Cannot be used with sample_size.
* num_replicates
* from_ts: initialise the simulation from root sehments
* start_time: initial simulation time
* end_time: terminate simulation
* record_full_arg: record all intermediate nodes (default = False)
* model:
    * Coalescent and approximations
        * StandardCoalescent: Hudson's algorithm
        * SmcApprocCoalescent: McVean and Cardin
        * SmcPrimerApproxCoalescent: Marjoram and Wall
    * Discrete time Wright-Fischer
        * DiscreteTimeWrightFischer
