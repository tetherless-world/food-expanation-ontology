from owlready2 import *
import time

'''
this file contains all the information for how to run the owlready2 with the pellet reasoner

first run the "runReasoner" function in order do the initial reasoning for the file.  

next run the "finishManualreasoning" funtion in order to do the manual part of the reasoning,
which is adding URIs to each of the entities.

last the 'runQueries' function runs queries on the reasoned ontology.

'''

# the inferred ontology in owlready2 does not include the original ontology URIs so it is 
# necessary to add them in order to queris later
def replaceFormating(line):
	old = "rdf:resource=\""
	new = "rdf:resource=\"http://purl.org/heals/food-explanation-ontology/"
	line =line.replace(old, new)

	old = "rdf:about=\""
	new = "rdf:about=\"http://purl.org/heals/food-explanation-ontology/"
	line =line.replace(old, new)

	old = "file:///mnt/c/Users/Ishita Padhiar/Documents/Research2020/"
	new = "http://purl.org/heals/food-explanation-ontology/"
	line =line.replace(old, new)

	old = "http://purl.org/heals/food-explanation-ontology/http://purl.org/heals/food"
	new = "http://purl.org/heals/food"
	line =line.replace(old, new)

	old = "http://purl.org/heals/food-explanation-ontology/http://www.omg.org/techprocess/ab/SpecificationMetadata"
	new = "http://www.omg.org/techprocess/ab/SpecificationMetadata"
	line =line.replace(old, new)

	old = "http://purl.org/heals/food-explanation-ontology/http://www.w3.org/2004/02/skos/core"
	new = "http://www.w3.org/2004/02/skos/core"
	line =line.replace(old, new)

	old = "http://purl.org/heals/food-explanation-ontology/https://purl.org/heals/eo/1.0.0"
	new = "https://purl.org/heals/eo/1.0.0"
	line =line.replace(old, new)

	old = "http://purl.org/heals/food-explanation-ontology/http://semanticscience.org/ontology/sio.owl"
	new = "http://semanticscience.org/ontology/sio.owl"
	line =line.replace(old, new)

	old = "http://purl.org/heals/food-explanation-ontology/https://raw.githubusercontent.com/tetherless-world/explanations-ontology/master/Ontologies/explanations-pattern-ontology.owl"
	new = "https://raw.githubusercontent.com/tetherless-world/explanations-ontology/master/Ontologies/explanations-pattern-ontology.owl"
	line =line.replace(old, new)

	old = "http://purl.org/heals/food-explanation-ontology/http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl"
	new = "http://www.ontologydesignpatterns.org/schemas/cpannotationschema.owl"
	line =line.replace(old, new)

	old = "http://purl.org/heals/food-explanation-ontology/https://www.w3.org/ns/prov-o.owl"
	new = "https://www.w3.org/ns/prov-o.owl"
	line =line.replace(old, new)

	old = "https://purl.org/heals/eo/1.0.0"
	new = "https://raw.githubusercontent.com/tetherless-world/explanation-ontology/master/Ontologies/explanation-ontology.owl"
	line =line.replace(old, new)

	old = "http://purl.org/heals/food-explanation-ontology/https://purl.org/heals/eo#"
	new = "https://purl.org/heals/eo#"
	line =line.replace(old, new)

	return line

# here we run the reasoners
def runReasoner(path):
	# laoding the ontology
	onto = World()
	print("Loading Ontology")
	onto.get_ontology(path).load()
	print("Ontology Loaded")

	# reasoning over the ontology, with pellet
	start = time.time()
	print("Running Pellet")
	sync_reasoner_pellet(onto, infer_property_values=True, infer_data_property_values=True)
	print("Inferred File")
	end = time.time()
	print("Time taken:", end- start)

	onto.save(file = "./infered_triples_1.rdf", format = "rdfxml")

	# here we finish the reasoning process manually and add superclasses to instances
	# we repeat until all the ancestors have been inferred
	onto2 = get_ontology("./infered_triples_1.rdf").load()

	classesInferred = True
	run = 0
	while classesInferred:
		classesInferred = False
		print(run)
		run += 1
		for c in onto2.classes():
			for i in c.instances(): 
				try:
					ancestors = list(set(i.INDIRECT_is_a))
				except AttributeError:
					continue
				for a in ancestors:
					if not (a == owl.Thing) and not(a == i) and not (type(a) == owlready2.class_construct.And ) and a not in i.is_a:
						i.is_a.append(a)
						print("instance", i, "added ancestor", a)
						classesInferred = True


	onto2.save(file = "./infered_triples_1.rdf", format = "rdfxml")


# this the function that adds the URIs to the inferred ontology
def finishManualReasoning():
	file = open("./infered_triples_1.rdf", 'r')
	line = file.read()
	file.close()

	line = replaceFormating(line)

	file = open("./infered_triples_2.rdf", 'w')
	file.write(line)
	file.close()

	print("formatting done")



#this is the function that runs any queries that the user might care about
def runQueries(path2, qtypes):

	inferred = World()
	print("Loading Ontology")
	inferred.get_ontology(path2).load()
	print("Ontology Loaded")

	graph = inferred.as_rdflib_graph()
	r = ""
	for q in qtypes:
		fname = "./queries/"+ q+ ".txt"
		file = open(fname, 'r')
		query = file.read()
		print(q.title(),"Results")
		r = list(graph.query(query))
		file.close()

		print(r)
		print()



# path = "file:///mnt/c/Users/Ishita Padhiar/Documents/Research2020/food-expanation-ontology.github.io/ontologies/feordf.rdf/"
# runReasoner(path)

#finishManualReasoning()

qTypes = ["contextual", "contrastive", "counterfactual", "statistical"]
path2 = "./infered_triples_2.rdf"
runQueries(path2, qTypes)




