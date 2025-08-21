---

layout: home
---

{% assign book_items = site.book %}
<script id="random-content-data" type="application/json">
[
  {% for item in book_items %}
    {
      "title": {{ item.title | jsonify }},
      "url": {{ item.url | jsonify }},
      "content": {{ item.content | strip_newlines | jsonify }}
    }{% if forloop.last == false %},{% endif %}
  {% endfor %}
]
</script>

# A random page from William Campbell's book

<div id="random-content"></div>

<script>
document.addEventListener("DOMContentLoaded", function() {
  var data = JSON.parse(document.getElementById('random-content-data').textContent);
  if (data.length > 0) {
    var randomItem = data[Math.floor(Math.random() * data.length)];
    var html = '<h2><a href="' + '{{ site.baseurl }}' + randomItem.url + '">' + randomItem.title + '</a></h2>';
    html += '<div>' + randomItem.content + '</div>';
    document.getElementById('random-content').innerHTML = html;
  }
});
</script>

<!-- {% for collection in site.collections %}
  {% unless collection.label == "posts" %}
  <p>
    <a href="{{ collection.label | prepend: '/' | append: '/' }}">
      {{ collection.title | default: collection.label }}
    </a>
  </p>
  {% endunless %}
{% endfor %} -->
