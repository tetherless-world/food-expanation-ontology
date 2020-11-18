from owlready2 import *


'''
first path works,
	just included it as a reference
second path doen't work - throws variable referenced before assignment error
	I suspect it might have to do with the fact that eo has not been load yet, 
	but I can't verify since eo also doesn't load
third path also doesn't work - throws a parsing error
	its say that there is a trple parsing error, but if that is the case I'm not 
	sure how the ontology could be working in other softwares.

'''

path = 'http://purl.org/heals/food'
# path = "file:///mnt/c/Users/Ishita Padhiar/Documents/Research2020/food-expanation-ontology.github.io/ontologies/feo.owl"
# path = 'http://purl.org/heals/eo'


onto = get_ontology(path).load()

'''
ontoTemp = get_ontology(path)
print(type(ontoTemp))
print(ontoTemp)
onto = ontoTemp.load()
'''
print("Ontology Loaded")


print(onto)
sync_reasoner_pellet(infer_property_values = True, infer_data_property_values = True)

onto_inferred = get_ontology("http://inferrences/")
onto_inferred.save("./infered_triples_1.rdf", format="rdfxml")
