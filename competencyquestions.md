---
layout: default
title: Competency Questions
---
[Questions](#competencyquestions) | [SPARQL Queries](#sparql) 

<article class="mb-5" id="competencyquestions">
<content>
  
  
<h2>Example of Competency Questions</h2>
  <p>We have crafted a set of competency questions which showcase how our explanation ontology can be useful to provide system designers the support they seek when planning to include different explanation types into the system and while deciding what explanation would be best suited for the user's question in real-time given the system's capabilities. We first present a table of our competency question list with the setting they correspond to and answers, and, we then present SPARQL query implementations for these questions.</p>
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
    <td><a href="#question2">(Q2).</a> Why should I eat Butternut Squash Soup over a Strawberry Tart?</td>
    <td>Butternut Squash Soup is better than a Strawberry Tart because Butternut Squash Soup is currently in season, and you are allergic to Strawberry Tarts. </td>
  </tr>
  <tr>
    <td>Counterfactual</td>
    <td><a href="#question2">(Q3).</a>What if I was pregnant?</td>
    <td> If you were you would be forbidden from eating sushi. </td>
  </tr>

</tbody>
</table>





<h3 id="sparql">SPARQL Queries</h3>
<ol>
  <li id="question1"><strong>Why should I eat Cauliflower Potato Curry?</strong>
  <ul type = "circle">
    <li> <strong>Query:</strong> <br/>
      <pre>
prefix feo: <http://purl.org/heals/food-explanation-ontology/>
PREFIX eo: <http://purl.org/heals/eo#>

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
  <li id="question2"><strong>Why should I eat Butternut Squash Soup over a Strawberry Tart?</strong>
  <ul type = "circle">
    <li> <strong>Query:</strong> <br/>
      <pre>
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
    <td>Strawberry</td>
  </tr>
</tbody>
</table>
  </li>
  </ul>
  </li>
}
   <li id="question3"><strong>  What if I was pregnant?</strong>
  <ul type = "circle">
    <li> <strong>Query:</strong> <br/>
      <pre>
PREFIX feo: <http://purl.org/heals/food-explanation-ontology/>
PREFIX food: <http://purl.org/heals/food/>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT Distinct ?parameter ?prop ?outputs
WHERE{
  feo:WhatIfIWasPregnant  feo:hasParameter ?parameter .
  ?parameter ?prop  ?outputs .
  ?prop rdfs:subPropertyOf feo:isCharacteristicOf.
  ?outputs a food:Food .
      </pre></li>
      <li><strong>Answer</strong> <br/>
  <table>
<thead>
  <tr>
    <th>Parameter</th>
    <th>Property</th>
    <th>Outputs</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Pregnancy Diet</td>
    <td>forbids</td>
    <td>Sushi</td>
  </tr>
</tbody>
</table>
  </li>
  </ul>
  </li>
</ol>
  </content>
