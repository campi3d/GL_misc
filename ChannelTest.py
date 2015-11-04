import mari

NEW_CHANNEL = None

def getNodeFromSignal(Node):
    ''' THe new Channel Node that is created '''
    global NEW_CHANNEL
    NEW_CHANNEL = Node

def findChannel(uuid):
    ''' Returns a channel object based on an input uuid'''
    curGeo = mari.current.geo()
    channelList = curGeo.channelList()

    for channel in channelList:
        if channel.uuid() == uuid:
            return channel
            break


size_dict = {256:mari.ImageSet.SIZE_256,
             512:mari.ImageSet.SIZE_512,
             1024:mari.ImageSet.SIZE_1024,
             2048:mari.ImageSet.SIZE_2048,
             4096:mari.ImageSet.SIZE_4096,
             8192:mari.ImageSet.SIZE_8192,
             16384:mari.ImageSet.SIZE_16384,
             32768:mari.ImageSet.SIZE_32768
            }

# Current Scene Data
current_channel = mari.current.channel()
current_channel_UUID = current_channel.uuid()
current_geo = mari.geo.current()
current_graph = current_geo.nodeGraph()
nodelist = current_graph.nodeList()
channel_node = None
node_id = -1

# searching for channel node
for node in nodelist:
    node_id += 1
    if node.uuid() == current_channel_UUID:
        channel_node = node
        break

# Saving what is attached to the Channel
channel_input = channel_node.inputNode('Input')

# writing a duplicate of the channel node
channel_node_ls = (nodelist[node_id],)
stringFromNode = current_graph.nodesToString(channel_node_ls)

#hooking up to a signal first so I can find the node I am about to create
# Hopefully this can be removed in a future version of Mari.
mari.utils.connect(mari.nodes.nodeCreated,getNodeFromSignal)
current_graph.nodesFromString(stringFromNode)
mari.utils.disconnect(mari.nodes.nodeCreated,getNodeFromSignal)

# Finding Channel corresponding to new Channel node
channel_obj = findChannel(NEW_CHANNEL.uuid())

# sampling newly created temp channel
index_ls = []
size_var = mari.ImageSet.SIZE_256


# Resizing new Channel to target resolution dependency
for patch in mari.geo.current().patchList():
    index = patch.uvIndex()
    index_ls = [index,]
    height = channel_obj.width(index)

    height /= 2
    if height < 256:
        height = 256
    if height > 32768:
        height = 32768
    size_var = size_dict[height]

    channel_obj.resize(size_var,index_ls)

NEW_CHANNEL.setInputNode('Input',channel_input)