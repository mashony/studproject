from django.db import connection
from django.template import Template, Context

class SQLLogMiddleware(object):
    def process_response ( self, request, response ):
        time = 0.0
        for q in connection.queries:
            time += float(q['time'])
        t = Template('''
            <p><em>Total query count:</em> {{ count }}<br/>
            <em>Total execution time:</em> {{ time }}</p>
            <ul class="sqllog">
                {% for sql in sqllog %}
                    <li>{{ sql.time }}: {{ sql.sql }}</li>
                {% endfor %}
            </ul>
        ''')
        content = t.render(Context({'sqllog':connection.queries,
                                'count':len(connection.queries),
                                'time':time})).encode('utf-8')
        response.content = response.content.replace('</body>',
            content + '</body>')
        return response