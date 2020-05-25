import msprime
import time
import math

#####################################################################
# -- Simple simulation, no mutations --
#####################################################################

# Simulate 5 individuals with Ne = 1000
tree_sequence = msprime.simulate(sample_size=6, Ne=1000)
tree = tree_sequence.first()
print(tree.draw(format="unicode"))

#####################################################################
# -- Add mutations --
#####################################################################

# Simulate
# With recombination --> multiple trees, time it
startR = time.time()
tree_sequenceR = msprime.simulate(sample_size=10, Ne=1000, length=10e8, mutation_rate=1e-8,
                                 recombination_rate=1e-8, random_seed = 65)
endR = time.time()
print(endR - startR)
tree_sequenceR.num_trees

# Without recombination --> one tree, time it
start = time.time()
tree_sequence = msprime.simulate(sample_size=10, Ne=1000, length=10e8, mutation_rate=1e-8,
                                 random_seed = 65)
end = time.time()
print(end - start)
tree_sequence.num_trees
type(tree_sequence)

# Obtain the first tree
tree = tree_sequenceR.first()
help(tree)
# Draw the tree
print(tree.draw(format="unicode"))
# print(tree.__doc__) = help(tree)
type(tree)

tree = tree_sequence.first()
# Obtain number of variants
help(site)
len([x.site.id for x in tree_sequence.variants()])
# Obtain number of sites
tree_sequence.num_sites
# Obtain number of mutations
tree_sequence.num_mutations
# Mutations at the first site
[x.mutations for x in tree.sites()][0]
[x.position for x in tree.sites()][0]
[x.mutations for x in tree.sites()][26]
[x.mutations for x in tree.sites()][50000]
# Obtain number of individuals
tree_sequence.num_individuals

# TABLES (TableCollection)
print(tree_sequence.tables.nodes)
print(tree_sequence.tables.sites)
print(tree_sequence.tables.mutations)
print(tree_sequence.tables.individuals)
print(tree_sequence.tables.edges)
print(tree_sequence.tables.populations)
print(tree_sequence.tables.provenances)

# Get variants
# See the first variant
[(variant.site.id, variant.alleles, variant.genotypes) for variant in tree_sequence.variants()][0]
#
tree = tree_sequence.first()
site = tree.sites()
for site in tree.sites():
    for mutation in site.mutations:
        print("Site: {}, mutation: {}.".format(site.position, mutation.node))

# Get genotypes
geno = tree_sequence.genotype_matrix()
geno.shape


#####################################################################
# -- Add demographic event --
#####################################################################
bottle_neck1 = 1000
bottle_neck2 = 2000
generation_time = 25
gTime = bottle_neck1 / generation_time
gTime1 = bottle_neck2 / generation_time

############# Population configuration - NO GROWTH RATE ###################
# This is optional when you have only one population
population_configuration = [msprime.PopulationConfiguration(sample_size = 1000,
                                                            initial_size = 20000)]

#Population expansion
# First a "smaller" time!!!
demographic_events = [
   msprime.PopulationParametersChange(time = gTime, initial_size = 1000),
   msprime.PopulationParametersChange(time = gTime1, initial_size = 100)
]

history = msprime.DemographyDebugger(population_configurations = population_configuration,
                           demographic_events = demographic_events, model = "dtwf")
history.print_history()
history.coalescence_rate_trajectory()
history.epoch_times
history.population_size_history
history.population_size_trajectory(steps = [0, 1, 10, 40, 41, 42, 43, 44, 100, 200, 1000, 10000])


############# Population configuration - GROWTH RATE ###################
# current size = 1,000;
# bottle neck 100 years ago, size = 100
# before bottle neck size = 10,000 (constant)
sample_size = 10e6
initial_size = 1000
back100_size = 100
historical_size = 10000
growth_rate = math.log( initial_size / back100_size) /100
#back100 = math.exp(growth_rate * 100) / initial_size
bottle_neck = 2500
generation_time = 25
gTime = bottle_neck / generation_time

population_configuration = [msprime.PopulationConfiguration(sample_size = sample_size,
                                                            initial_size = initial_size,
                                                            growth_rate = growth_rate)]
demographic_events = [
   msprime.PopulationParametersChange(time = gTime, initial_size = historical_size, growth_rate = 0)
]

history = msprime.DemographyDebugger(population_configurations = population_configuration,
                           demographic_events = demographic_events, model = "dtwf")
history.print_history() ###???
history.coalescence_rate_trajectory()
history.epoch_times
history.population_size_history
history.population_size_trajectory(steps = [0, 1, 10, 40, 41, 42, 43, 44, 100, 200, 1000, 10000])


############## Run simulation ##########################3
pop = msprime.simulate(length = 10e08, mutation_rate=1e-8, recombination_rate=1e-8, random_seed = 8465, Ne = 200,
                       population_configurations = population_configuration, demographic_events = demographic_events)
pop.num_trees
pop.num_samples
pop.num_sites
pop.num_mutations