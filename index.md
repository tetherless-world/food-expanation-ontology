---
layout: default
title: Food Explanation Ontology: Semantic Modeling of Food Recommendation Explanations
---

[Abstract](#abstract) | [Resources](#resources) | [Tools Used](#toolsused) 

<h1 class="page-title" style="text-transform:uppercase;" id="header">FOOD EXPLANTION ONTOLOGY: A SEMANTIC MODELING OF FOOD RECOMMENDATION EXPLANTIONS</h1>
<!--<h3 style="color:dimgrey;">Shruthi Chari<sup>1</sup>, Oshani Seneviratne<sup>1</sup>, Daniel M. Gruen<sup>2</sup>, Morgan Foreman<sup>2</sup>, Deborah L. McGuinness<sup>1</sup>, Amar K. Das<sup>2</sup></h3>
<h3><a href="https://www.rpi.edu/"><sup>1</sup>Rensselaer Polytechnic Institute</a> | <a href="https://www.research.ibm.com/labs/cambridge/"><sup>2</sup>IBM Research, Cambridge</a></h3>-->
<p class="message">A website to navigate resources open-sourced via the associated DECOR 2020 submission. Use the side navigation panel to explore different sections of the website and click on an add symbol for more navigation options under some sections.</p>

<!-- <table>
  <tbody>
    <tr>
      <td><a href="#abstract">Abstract</a></td>
    </tr>
  </tbody>
</table> -->

<hr>
<article class="mb-5" id="abstract">
<content>
  
  
<h2>Abstract</h2>
  <p>With the increased use of AI methods to provide recommendations in the health, and specifically, food space, there is also an increased need for explainability of those recommendations. Such explanations would benefit users of recommendation systems by empowering them with a justification for following the system's suggestions. We present the Food Explanation Ontology (FEO) that provides a formalism for generating explanations to users for food-related recommendations. FEO creates a semantic modeling for food recommendations, using concepts from the explanation domain to create intelligent responses to user questions about food recommendations they receive from AI systems such as personalized knowledge base question answering systems. FEO uses a modular, extensible structure that lends itself to a variety of explanations while still preserving important semantic details to accurately represent food recommendations.</p>
 </content>
 
 <hr/>
 <article class="mb-5" id="resources">
<content>
<h2>List of Resources </h2>
<ul>
 <table style="width:100%">
    <tr>
    <th>Resources</th>
    <th>Links</th> 
  </tr>
   <tr>
    <td>Protocol Guidance on Usage of Ontology</td>
    <td><a href="protocol">Protocol</a> </td> 
  </tr>
  <tr>
    <td>Ontology</td>
    <td><a href="ontology">Food Explanation Ontology</a> </td> 
  </tr>
  <tr>
    <td>Explanation Types</td>
    <td><a href="modeling#explanationtypes">Modeling</a> </td> 
  </tr>
    <!--<tr>
    <td> </td>
    <td> (b) <a href="./application.html">Faceted Browser</a> </td> 
  </tr>-->
    <tr>
    <td>Clincal Example</td>
    <td><a href="clinicalexample">Example of a Contrastive Explanation</a> </td> 
  </tr>
   <tr>
    <td>Competency Questions </td>
    <td><a href="competencyquestions#sparql">SPARQL Queries</a> </td> 
  </tr>
   <tr>
    <td>Tools Used </td>
    <td><a href="index#toolsused">References to tools used</a> </td> 
  </tr>
</table>
  
 </ul>
 </content>
 
 <hr/>
 
 <article class="mb-5" id="toolsused">
<content>
  
  
<h2>Tools Used during Development</h2>
  <ul>
  <li>Ontology Editor: <a href="https://protege.stanford.edu/products.php#desktop-protege">Protege 5.5.0</a></li>
  <li>Conceptual Diagram created using <a href="https://www.omnigroup.com/omnigraffle/">Omnigraffle</a></li>
  <li>Ontology documentation tool, <a href="https://github.com/dgarijo/Widoco">Widoco</a></li>
  <li>RDF Visualization generated with <a href="http://jimmccusker.github.io/rdfviewer/">RDFViewer</a></li>
  </ul>
  </content>
  <!--<iframe src="https://tetherless-world.github.io/explanation-ontology/WidocoDocumentation/index-en.html" style="width:100%;"/>-->
 
  <!--<article class="mb-5" id="publications">
<content>
  <h2>Publications</h2>
  <ul>
    <li>Explanation Ontology: A Model of Explanations for User-Centered AI; Shruthi Chari , Oshani Seneviratne , Daniel M. Gruen ,  Morgan A. Foreman , Amar K. Das, Deborah L. McGuinness; Resource Track,19th International Semantic Web Conference 2020</li>
    <li>Explanation Ontology in Action: A Clinical Use-Case; Shruthi Chari , Oshani Seneviratne , Daniel M. Gruen ,  Morgan A. Foreman , Amar K. Das, Deborah L. McGuinness; Posters and Demo Track,19th International Semantic Web Conference 2020</li>
  </ul>
  </content>-->
<!-- 
<div class="posts">
  {% for post in paginator.posts %}
  <div class="post">
    <h1 class="post-title">
      <a href="{{ post.url }}">
        {{ post.title }}
      </a>
    </h1>

    <span class="post-date">{{ post.date | date_to_string }}</span>

    {{ post.content }}
  </div>
  {% endfor %}
</div>

<div class="pagination">
  {% if paginator.next_page %}
    <a class="pagination-item older" href="{{ site.baseurl }}page{{paginator.next_page}}">Older</a>
  {% else %}
    <span class="pagination-item older">Older</span>
  {% endif %}
  {% if paginator.previous_page %}
    {% if paginator.page == 2 %}
      <a class="pagination-item newer" href="{{ site.baseurl }}">Newer</a>
    {% else %}
      <a class="pagination-item newer" href="{{ site.baseurl }}page{{paginator.previous_page}}">Newer</a>
    {% endif %}
  {% else %}
    <span class="pagination-item newer">Newer</span>
  {% endif %}
</div> -->
