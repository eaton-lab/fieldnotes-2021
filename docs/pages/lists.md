---
layout: default
image: /assets/images/hackers-1.jpg
---

<style>

tr {
  line-height: 1rem;
}

</style>

### Genomes

<table class="table table-sm table-striped table-hover table-bordered" style="font-size: 14px">
  <!-- <caption>Class GitHub repos by username</caption> -->
  <thead class="thead-dark">
    <tr>   
      <th scope="col">#</th>
      <th scope="col">Species</th>      
      <th scope="col">County</th>
      <th scope="col">Sites</th>
      <th scope="col">Day</th>      
  </tr>
  </thead>
  <tbody>
    {% for row in site.data.genomes %}
    <tr>
      <th scope="col">{{ forloop.index }}</th>    	
      <th scope="col">{{ row["Species"] }}</th>
      <th scope="col">{{ row["County"] }}</th>
      <th scope="col">{{ row["Sites"] }}</th>
      <th scope="col">{{ row["Day"] }}</th>      
    </tr>
    {% endfor %}
  </tbody>
</table>


### Transcriptomes

<table class="table table-sm table-striped table-hover table-bordered" style="font-size: 14px">
  <!-- <caption>Class GitHub repos by username</caption> -->
  <thead class="thead-dark">
    <tr>   
      <th scope="col">#</th>
      <th scope="col">Species</th>      
      <th scope="col">County</th>
      <th scope="col">Sites</th>
      <th scope="col">Day</th>      
  </tr>
  </thead>
  <tbody>
    {% for row in site.data.transcriptomes %}
    <tr>
      <th scope="col">{{ forloop.index }}</th>    	
      <th scope="col">{{ row["Species"] }}</th>
      <th scope="col">{{ row["County"] }}</th>
      <th scope="col">{{ row["Sites"] }}</th>
      <th scope="col">{{ row["Day"] }}</th>      
    </tr>
    {% endfor %}
  </tbody>
</table>

