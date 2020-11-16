# Food Explanation Ontology
Ontology for generating Food Related Explanations

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
