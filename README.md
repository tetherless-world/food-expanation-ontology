# Food Explanation Ontology
Ontology for generating Food Related Explanations

## Setup

* Prepare the virtual environment

```
python -m pip install virtualenv
python -m virtualenv env --python=python3
source env/bin/activate
python -m pip install -r requirements.txt
```

* Run the code

```
python src/runfeo.py
```

## Competency Questions

1. **Contextual** - "Why should I eat Butternut Squash Soup?"

```
prefix feo: <http://purl.org/heals/food-explanation-ontology/>

SELECT DISTINCT ?characteristic ?classes
WHERE{
  ?question feo:hasParameter ?parameter .
  ?parameter feo:hasCharacteristic ?characteristic .
  ?characteristic feo:isInternal False .
  ?systemChar a feo:SystemCharacteristic .
  ?userChar a feo:UserCharacteristic .
  filter ( ?characteristic = ?systemChar || ?characteristic = ?userChar ) .
  ?characteristic a ?classes .
  ?classes rdfs:subClassOf feo:Characteristic .
}
```

2. **Counterfactual** - "Why should I eat Butternut Squash Soup over a Strawberry Tart"

```
PREFIX feo: <http://purl.org/heals/food-explanation-ontology/>
PREFIX food: <http://purl.org/heals/food/>
PREFIX eo: <http://purl.org/heals/eo#>

Select DISTINCT ?factType ?factA ?foilType ?foilB
Where{
  ?question feo:hasPrimaryParameter ?parameterA .
  ?question feo:hasSecondaryParameter ?parameterB .

  ?parameterA feo:hasCharacteristic ?factA .
  ?factA a <https://purl.org/heals/eo#Fact>.
  ?factA a ?factType .
  ?factType (rdfs:subClassOf+) feo:Characteristic .
  
  ?parameterB feo:hasCharacteristic ?foilB .
  ?foilB a <https://purl.org/heals/eo#Foil> .
  ?foilB a ?foilType.
  ?foilType (rdfs:subClassOf+) feo:Characteristic .
}
```

3. **Contrastive** - "What if it was Spring?"

```
PREFIX feo: <http://purl.org/heals/food-explanation-ontology/>
PREFIX food: <http://purl.org/heals/food/>
SELECT Distinct ?parameter ?outputs
WHERE{
feo:WhatIfItWereSpring  feo:hasParameter ?parameter .
?parameter feo:isCharacteristicOf ?outputs .
?outputs a food:Food .
}
```
