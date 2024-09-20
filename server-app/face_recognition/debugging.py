import tensorflow as tf

# Load the graph
with tf.compat.v1.gfile.GFile('EDSR_x3.pb', 'rb') as f:
    graph_def = tf.compat.v1.GraphDef()
    graph_def.ParseFromString(f.read())

# Summarize the graph
with tf.Graph().as_default() as graph:
    tf.import_graph_def(graph_def, name='')
    for op in graph.get_operations():
        print(op.name, op.type)
