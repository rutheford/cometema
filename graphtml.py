# -*- coding: utf-8 -*-

# Creates the graph page
def write_page(graph, filename='graph.html'):
    f = open(filename, 'w')

    f.write(r"""<!DOCTYPE html>
    <html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Sugestões de tema XXX COMECON</title>

      <script type="text/javascript" src="http://visjs.org/dist/vis.js"></script>
      <link href="http://visjs.org/dist/vis-network.min.css" rel="stylesheet" type="text/css">

      <style type="text/css">
        #mynetwork {
          width: 100%;
          height: 95vh;
        }
      </style>
    </head>
    <body>

    <div id="mynetwork"><div class="vis-network" tabindex="900" style="position: relative; overflow: hidden; touch-action: pan-y; user-select: none; -webkit-user-drag: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); width: 100%; height: 100%;"><canvas style="position: relative; touch-action: none; user-select: none; -webkit-user-drag: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); width: 100%; height: 100%;" width="600" height="400"></canvas></div></div>

    <script type="text/javascript">
      // create an array with nodes


      var nodes = new vis.DataSet([""")

    for n in graph.nodes(data='name'):
        f.write("    {id: %d, label: '%s'},\n" % n)

    f.write("""  ]);

      // create an array with edges
      var edges = new vis.DataSet([""")

    for e in graph.edges:
        f.write('    {from: %d, to: %d},\n' % e)

    f.write("""  ]);

      // create a network
      var container = document.getElementById("mynetwork");
      var data = {
        nodes: nodes,
        edges: edges
      };
      var options = {
        nodes: {
          shape: 'dot',
          size: 10,
        },
        layout: {
          improvedLayout: true
        },
      };
      var network = new vis.Network(container, data, options);

    </script>




    </body></html>
    """)

    return f.close()

# Creates the set page
def create_set_page(graph, filename='set_page.html'):
    f = open(filename, 'w')

    f.write("""<!DOCTYPE html>
    <html>
    <head>
        <title></title>
    </head>
    <body>
        <div>""")

    for n in graph.nodes(data='name'):
        f.write('<button type="button" onclick="addText(\'%d\')">%s (%d)</button>' % (n[0], n[1], n[0]))

    f.write("""	</div>
        <div><textarea id="from" rows="1" cols="50"></textarea></div>
        <div><textarea id="alltext" rows="20" cols="50"></textarea></div>
    <script type="text/javascript">
        function addText(text){
            document.getElementById("alltext").value += "    {from: " + document.getElementById("from").value + ", to: " + text + "},\n";
        }
    </script>
    </body>
    </html>""")

    f.close()