---
layout: default
image: /assets/images/hackers-2.jpg
---


## Links to class GitHub repos


<table class="table table-sm table-striped table-hover table-bordered" style="font-size: 14px">
  <caption>Class GitHub repos by username</caption>
  <thead class="thead-dark">
    <tr>   
      <th scope="col">Username</th>
      <th scope="col">Project title</th>
      <th scope="col">Project repo</th>
  </tr>
  </thead>
  <tbody>
    {% for row in site.data.usernames %}
    <tr>
      <th scope="col">{{ row["Username"] }}</th>
      <!-- <th scope="col">{{ row["Project"] }}</th> -->
      <th scope="col"><a href="https://github.com/{{ row['Username'] }}/{{ row['Project'] }}">{{ row["Project"] }}</a></th>      
      <th scope="col"><a href="https://github.com/{{ row['Username'] }}">https://github.com/{{ row['Username'] }}</a></th>
    </tr>
    {% endfor %}
  </tbody>
</table>
