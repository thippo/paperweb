# -*- coding:utf-8 -*-

from jinja2 import Template

def alert_div(colour, message):
    template = Template('''<div class="alert alert-{{ colour }}" style="margin-top:-15px;"><a href="#" class="close" data-dismiss="alert">&times;</a><p class="text-center"><strong>{{ message }}</strong></div>''')
    return template.render(colour=colour, message=message)

def jj2papers(who, paper_items):
    template = Template('''
{% for i in range(paper_items|length) %}
        <div class="panel panel-default">
                <div class="panel-heading">
                        <h4 class="panel-title">
                                <a data-toggle="collapse" data-parent="#accordion" href="#collapse{{ i }}">
                        &lt{{ paper_items[i]['ENTRYTYPE'] }}&gt<strong> {{ paper_items[i]['title'] }}</strong>
                                </a>
                        </h4>
                </div>
                <div id="collapse{{ i }}" class="panel-collapse collapse in">
                        <div class="panel-body">
                        <p class="text-success">{{ paper_items[i]['author'] }}</p>
<blockquote>
                        <p class="text-primary">{{ paper_items[i]['description'] }}</p>
</blockquote>
        <br>
<div class="pull-left">
<p><span class="glyphicon glyphicon-tag">{% for x in paper_items[i]['tags'] %} {{ x }}{% endfor %}</span></p>
</div>
<div class="pull-right">
        <a href="/showpaper/{{ who }}/{{ paper_items[i]['_id'] }}" data-toggle="tooltip" title="文献详情" class="text-danger" target=_blank>
          <span class="glyphicon glyphicon-file" ></span>
        </a>
        <a href="/editpaper/{{ who }}/{{ paper_items[i]['_id'] }}" data-toggle="tooltip" title="编辑文献" class="text-primary">
          <span class="glyphicon glyphicon-pencil"></span>
        </a>
{% if paper_items[i]['pdfweb'] %}
        <a href="{{  paper_items[i]['pdfweb'] }}" data-toggle="tooltip" title="外部PDF文件" class="text-success" target=_blank>
          <span class="glyphicon glyphicon-cloud"></span>
        </a>
{% endif %}
{% if paper_items[i]['pdfupload'] %}
        <a href="/static/papers/{{  paper_items[i]['pdfupload'] }}.pdf" data-toggl="tooltip" title="本地PDF文件" class="text-info" target=_blank>
          <span class="glyphicon glyphicon-paperclip"></span>
        </a>
{% endif %}
        <a href='/downloadbibtex/{{ who }}/{{ paper_items[i]['_id'] }}' data-toggle="tooltip" title="下载BibTex文件" class="text-warning">
          <span class="glyphicon glyphicon-save"></span>
        </a>
        <a href="/deletepaper/{{ who }}/{{ paper_items[i]['_id'] }}/{{ tag_now }}" data-toggle="tooltip" title="删除文献" class="text-danger">
          <span class="glyphicon glyphicon-trash" Onclick="return confirm('请确认是否删除')"></span>
        </a>
</div>
                        </div>
                </div>
        </div>
{% endfor %}
''')
    return template.render(who=who, paper_items=paper_items)
