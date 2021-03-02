---
layout: default
title: Food Explanation Ontology
---

[About](#ontologyabout) | [Access Links](#ontologylinks) | [Ontology Metadata](#ontologymetadata) 

<article class="mb-5" id="ontology">
<content>
  
  
<h2 id="ontologyabout">Food Explanation Ontology</h2>
  <p class="message">Ontology has been cleared for release and is made available as an open-source resource under the <a href="https://www.apache.org/licenses/LICENSE-2.0">Apache 2.0 license</a></p>
  <p> 
  We  can  view  classes  in  our  system  from  two  different lenses. First, we want to be able to model them as components of explanations, and second, as elements of the question and system. Additionally,  the  parameters  within  the  users’  questions, and  the  characteristics  associated  with  these  parameters,  can be described in the context of food (the domain of application) and  user  and  system  semantics. We accomplish these goals as in FEO, we use a system of subclasses and subproperties to classify and reason over instances.
</p>
 
  
 <img src ="../images/characteristics.png" style="width:70%; height:700%">  
 <caption>Fig. 1: This diagram provides an insight into the subclass structure. We split characteristics into a couple sections the Parameter, System, and the User. The next level of subcharacteristics takes us to the food domain. Here we can see different subclasses of food characteristics, such as Liked Foods, Allergies, Seasonality, and Location. Restrictions in the on these classes along with reasoning allows instances to infered into these categories.</caption>  
 
 <img src ="../images/properties.png" style="width:100%; height:100%">  
 <caption>Fig. 2: The property structure similarly has subproperties. We characterize properties as supporting and opposing and also as types of characteristics. We also define inverse of as a type of property, in order to save time on duplication of data. </caption>
 
 <img src ="../images/contextualModel1.png" style="width:70%; height:70%">  
 <caption>Fig. 3: This is a model of what the process to get the answer to the first competency question. Her we illustrate how these modeling choices work together to help us solve our competency questions. The image details how the ontology appears (after reasoning) with the classes necessary to answer the first competency question. The light blue boxes illustrate the relationships between instances and the dark blue boxes contain classes and their pertinent restrictions. </caption>  
  
  <h3 id="ontologylinks">Ontology Links</h3>
  <ul>
  <li>Ontology documentation generated using the <a href="https://github.com/dgarijo/Widoco">Widoco</a> tool can be browsed at: <a href="https://tetherless-world.github.io/food-explanation-ontology/WidocoDocumentation/doc/index-en.html">https://tetherless-world.github.io/food-explanation-ontology/WidocoDocumentation/doc/index-en.html</a></li>
  <li>Ontology can be accessed from <a href="https://purl.org/heals/food-explanation-ontology/">https://purl.org/heals/food-explanation-ontology/</a></li>
  <li class="note">We are aware of issues with the PURL service at the moment, if there are issues, please use the <a href="https://github.com/tetherless-world/food-explanation-ontology">github link</a> instead.  </li>
  </ul>
  
  <article class="mb-5" id="ontologymetadata">
  <content>
    <h3>Ontology Metadata</h3>
    <p>Metadata that would be useful to navigate our <a href="#resources">resources</a>, i.e., ontology, modeling snippets and SPARQL queries. The content below can also be viewed by inspecting our explanation ontology in an ontology editor, like, <a href="https://protege.stanford.edu/products.php#desktop-protege">Protege 5.5.0</a>.
    
  <h4> Ontology Prefixes </h4>
  <table style="width:100%">
    <tr>
    <th>Prefix</th>
    <th>Links</th> 
  </tr>
  <tr>
    <td>rdf</td>
    <td><a href="http://www.w3.org/1999/02/22-rdf-syntax-ns">Resource Description Framework</a></td> 
  </tr>
  <tr>
    <td>rdfs</td>
    <td><a href="http://www.w3.org/2000/01/rdf-schema"> RDF Schema</a> </td> 
  </tr>
  <tr>
    <td>owl</td>
    <td><a href="http://www.w3.org/2002/07/owl#">Web Ontology Language </a> </td> 
  </tr>
    <tr>
    <td> xsd</td>
    <td> <a href="http://www.w3.org/2001/XMLSchema#"></a> XML Schema Definition</td> 
  </tr>
    <tr>
    <td>dct</td>
    <td> <a href="http://purl.org/dc/terms/">Dublin Core Term</a> </td> 
  </tr>
   <tr>
    <td>skos</td>
    <td> <a href="http://www.w3.org/2004/02/skos/core#"></a>  Simple Knowledge Organization System</td> 
  </tr>
    <tr>
    <td>eo</td>
    <td> <a href="https://purl.org/heals/eo#"> Explanation Ontology</a> </td> 
  </tr> 
     <tr>
    <td>feo</td>
    <td> <a href="https://purl.org/heals/food-explanation-ontology/"> Food Explanation Ontology</a> </td> 
  </tr> 
     <tr>
    <td>food</td>
    <td> <a href="https://purl.org/heals/food/"> What To Make Ontology</a> </td> 
  </tr> 
    <tr>
    <td>sio</td>
    <td> <a href="http://semanticscience.org/resource/">SemanticScience Integrated Ontology</a> </td> 
  </tr>
  <tr>
    <td>ep</td>
    <td> <a href="https://raw.githubusercontent.com/tetherless-world/explanation-ontology/master/Ontologies/explanations-pattern-ontology.owl#">Explanations Pattern Ontology</a> </td>
    <!--Note to self update this to the dedalo upon consulting with Ilaria-->
  </tr>
  <tr>
    <td>ep</td>
    <td> <a href="https://www.w3.org/TR/prov-o/">Provenance Ontology</a> </td> 
  </tr>
     <tr>
    <td>obo</td>
    <td> <a href="http://purl.obolibrary.org/obo/">OBO Foundry</a> </td> 
  </tr>
    
</table>
