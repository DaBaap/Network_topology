$(document).ready(function() {

    $('#search').on('keypress', function(e) {
        if (e.which == 13) { 
            var nodeValue = $('#search').val();
            get_network_graph(nodeValue)
        }
    });

    $('.loadGraph').on('click', function() {
        var nodeValue = $(this).val();
        get_network_graph(nodeValue)

    });
        
    function get_network_graph(node_value) {
        console.log("asdasd")

        $.ajax({
            url: '/get_graph/',
            type: 'GET',
            data: { 'node': node_value },
            dataType: 'json',
            success: function(data) {
                var nodes = new vis.DataSet(data.nodes);
                var edgesData = data.edgesData;
                var shortestPath = data.shortestPath;
                var secondShortestPath = data.secondShortestPath;

                $('#node_name').html('<h3>'+data.node_name+'</h3>');


                edgesData.forEach(function(edge) {
                    if (isEdgeInPath(edge, shortestPath)) {
                        edge.color = {color:'blue', highlight:'blue'};
                    } else if (isEdgeInPath(edge, secondShortestPath)) {
                        edge.color = {color:'grey', highlight:'grey', dashes: [5,5]};
                        edge.dashes = true;
                    }
                });

                var edges = new vis.DataSet(edgesData);

                var container = document.getElementById('mynetwork');
                var data = {
                    nodes: nodes,
                    edges: edges
                };
                var options = {
                    nodes: {
                        shape: 'dot',
                        size: 30,
                        font: {
                            size: 12
                        }
                    },
                    edges: {
                        width: 2
                    },
                    physics: {
                        stabilization: false,
                        barnesHut: {
                            gravitationalConstant: -30000
                        },
                        springLength: 150,
                        springConstant: 0.05
                    }
                };

                var network = new vis.Network(container, data, options);
            }
        });
    }
});
function isEdgeInPath(edge, path) {
    for (var i = 0; i < path.length - 1; i++) {
        if ((edge.from === path[i] && edge.to === path[i + 1]) || 
            (edge.from === path[i + 1] && edge.to === path[i])) {
            return true;
        }
    }
    return false;
}
