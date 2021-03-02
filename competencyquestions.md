---
layout: default
title: Competency Questions
---
[Questions](#competencyquestions) | [SPARQL Queries](#sparql) 

<article class="mb-5" id="competencyquestions">
<content>
  
  
<h2>Competency Questions</h2>
  <table>
<thead>
  <tr>
    <th>Setting</th>
    <th>Example Competency Question</th>
    <th>Candidate Answer</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Contextual</td>
    <td><a href="#question1">(Q1).</a> Why should I eat Cauliflower Potato Curry?</td>
    <td>Cauliflower Potato Curry uses ingredient Cauliflower,  which is available in the current season. </td>
  </tr>
  <tr>
    <td>Contrastive</td>
    <td><a href="#question2">(Q2).</a> Why should I eat Butternut Squash Soup over a Broccoli Cheddar Soup?</td>
    <td>Butternut Squash Soup is better than a Broccoli Cheddar Soup because Butternut Squash Soup is currently in season, and you are allergic to Broccoli Cheddar Soup. </td>
  </tr>
  <tr>
    <td>Counterfactual</td>
    <td><a href="#question3">(Q3).</a>What if I was pregnant?</td>
    <td> If  you  were  pregnant,  you  would  beforbidden from eating sushi. You would be suggested toeat Spinach Frittata. </td>
  </tr>
  <tr>
    <td>Statistical</td>
    <td><a href="#question4">(Q4).</a>Why should I follow a low calorie diet?</td>
    <td> 66.67% percent of people how followed a low calorie diet lost weight, which is one of your goals.</td>
  </tr>

</tbody>
</table>





<h3 id="sparql">SPARQL Queries</h3>
<ol>
  <li id="question1"><strong>Why should I eat Cauliflower Potato Curry?</strong>
  <ul type = "circle">
    <li> <strong>Query:</strong> <br/>
      <pre>
PREFIX feo: <http://purl.org/heals/food-explanation-ontology/>
PREFIX eo: <http://purl.org/heals/eo#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?characteristic ?classes
WHERE{
  ?WhyEatCauliflowerPotatoCurry feo:hasParameter ?parameter .
  ?parameter feo:hasCharacteristic ?characteristic .
  ?characteristic feo:isInternal False .
  ?systemChar a feo:SystemCharacteristic .
  ?userChar a feo:UserCharacteristic .
  filter ( ?characteristic = ?systemChar || ?characteristic = ?userChar ) .
  ?characteristic a ?classes .
  ?classes rdfs:subClassOf feo:Characteristic .
  Filter Not Exists{?classes rdfs:subClassOf <https://purl.org/heals/eo#knowledge> }.
}
      </pre></li>
      <li><strong>Answer</strong> <br/>
  <table>
<thead>
  <tr>
    <th>Characteristic</th>
    <th>Classes</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Autumn</td>
    <td>SeasonCharacteristic</td>
  </tr>
</tbody>
</table>
  </li>
  </ul>
  </li>
  <li id="question2"><strong>Why should I eat Butternut Squash Soup over a Broccoli Cheddar Soup?</strong>
  <ul type = "circle">
    <li> <strong>Query:</strong> <br/>
      <pre>
PREFIX food: <http://purl.org/heals/food/>
PREFIX eo: <http://purl.org/heals/eo#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

Select DISTINCT ?factType ?factA ?foilType ?foilB
Where{
  ?question feo:hasPrimaryParameter ?parameterA .
  ?question feo:hasSecondaryParameter ?parameterB .

  ?parameterA feo:hasCharacteristic ?factA .
  ?factA a <https://purl.org/heals/eo#Fact>.
  ?factA a ?factType .
  ?factType (rdfs:subClassOf+) feo:Characteristic .
  Filter Not Exists{?factType rdfs:subClassOf <https://purl.org/heals/eo#knowledge> }.
  Filter Not Exists{?s rdfs:subClassOf ?factType}.
  
  ?parameterB feo:hasCharacteristic ?foilB .
  ?foilB a <https://purl.org/heals/eo#Foil> .
  ?foilB a ?foilType.
  ?foilType (rdfs:subClassOf+) feo:Characteristic .
  Filter Not Exists{?foilType rdfs:subClassOf <https://purl.org/heals/eo#knowledge> }.
  Filter Not Exists{?t rdfs:subClassOf ?foilType}.

}
      </pre></li>
      <li><strong>Answer</strong> <br/>
    <table>
<thead>
  <tr>
    <th>FactType</th>
    <th>FactA</th>
    <th>FoilType</th>
    <th>FoilB</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>SeasonCharacteristic</td>
    <td>Autumn</td>
    <td>AllergicFoodCharacteristic</td>
    <td>Broccoli</td>
  </tr>
</tbody>
</table>
  </li>
  </ul>
  </li>

   <li id="question3"><strong>  What if I was pregnant?</strong>
  <ul type = "circle">
    <li> <strong>Query:</strong> <br/>
      <pre>
PREFIX feo: <http://purl.org/heals/food-explanation-ontology/>
PREFIX food: <http://purl.org/heals/food/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT Distinct ?property ?ingredient ?outputs
WHERE{
  feo:WhatIfIWasPregnant  feo:hasParameter ?parameter .
  ?parameter ?property  ?ingredient .
  ?property rdfs:subPropertyOf feo:isCharacteristicOf.
  ?ingredient a food:Food .
  OPTIONAL { ?ingredient feo:isIngredientOf ?outputs.}
}
  <table>
<thead>
  <tr>
    <th>Property</th>
    <th>Base Food</th>
    <th>Inherited Foods</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>recommends</td>
    <td>Spinach</td>
    <td>Spinach Frittata</td>
  </tr>
    <tr>
    <td>forbids</td>
    <td>Sushi</td>
    <td></td>
  </tr>
</tbody>
</table>
  </li>
  </ul>
  </li>
</ol>
  </content>
