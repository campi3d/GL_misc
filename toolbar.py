import mari
import PySide.QtGui as QtGui


# Variables need to be declared as globals or else the scoping
# doesn't work due to a PySide Bug
g_paintBuffer = mari.canvases.paintBuffer()
g_buffer_size_label = None
g_buffer_size = None
g_halve_size = None
g_double_size = None
g_buffer_depth_label = None
g_buffer_depth = None
g_buffer_clamp = None
g_buffer_sync = None
g_mirror_x = None
g_mirror_y = None


class paintBufferToolbar(object):
    "Adds new items to the TransformPaint Tool Properties Toolbar"
    def __init__(self, parent=None):

        #  Global Vars. Need to use Globals because Objects are being destroyed otherwise
        global g_paintBuffer
        global g_buffer_size_label
        global g_buffer_size
        global g_halve_size
        global g_double_size
        global g_buffer_depth_label
        global g_buffer_depth
        global g_buffer_clamp
        global g_buffer_sync
        global g_mirror_x
        global g_mirror_y


        # Create Widgets

        g_buffer_size_label = QtGui.QLabel("  Resolution ")
        g_buffer_size = QtGui.QComboBox()

        # determine allowed resolutions
        for resolution in g_paintBuffer.supportedResolutions():
            size = resolution.width()
            g_buffer_size.addItem(str(size) + ' x ' + str(size), resolution)

        g_halve_size = QtGui.QPushButton("Halve")
        g_double_size = QtGui.QPushButton("Double")

        g_buffer_depth_label = QtGui.QLabel("  Depth ")
        g_buffer_depth = QtGui.QComboBox()
        g_buffer_depth.addItem("8 Bit (Byte)", mari.PaintBuffer.BufferDepth.DEPTH_BYTE)
        g_buffer_depth.addItem("16 Bit (Half)", mari.PaintBuffer.BufferDepth.DEPTH_HALF)
        g_buffer_depth.addItem("32 Bit (Float)", mari.PaintBuffer.BufferDepth.DEPTH_FLOAT)
        g_buffer_clamp = QtGui.QCheckBox('Clamp')
        g_buffer_sync = QtGui.QCheckBox('Link Depth to Paint Target')

        g_mirror_x = QtGui.QPushButton("Mirror X")
        g_mirror_y = QtGui.QPushButton("Mirror Y")


        # set currents for widgets from active Paintbuffer
        self._setBufferResolution()
        self._setBufferDepth()
        self._setBufferClamp()

        # Add to Toolbar
        toolbar = mari.app.findToolBar('Tool Properties')

        toolbar.setLocked(False)
        toolbar.addWidget(g_buffer_size_label)
        toolbar.addWidget(g_buffer_size)
        toolbar.addWidget(g_halve_size)
        toolbar.addWidget(g_double_size)
        toolbar.addSeparator()
        toolbar.addSeparator()
        toolbar.addWidget(g_buffer_depth_label)
        toolbar.addWidget(g_buffer_depth)
        toolbar.addSeparator()
        toolbar.addWidget(g_buffer_clamp)
        toolbar.addWidget(g_buffer_sync)
        toolbar.addSeparator()
        toolbar.addSeparator()
        toolbar.addWidget(g_mirror_x)
        toolbar.addWidget(g_mirror_y)
        toolbar.setLocked(True)

        # connect to signals so widgets change when settings are changed in Painting Palette
        #  1 - Signals from Painting Palette to Toolbar
        mari.utils.connect(g_paintBuffer.resolutionChanged, lambda: self._setBufferResolution())
        mari.utils.connect(g_paintBuffer.depthChanged, lambda: self._setBufferDepth())
        #  2 - Signals from Toolbar to Painting Palette



    def _setBufferResolution(self):
        ''' Reads the current Buffer resolution and sets the Toolbar Dropdown accordingly '''
        if not self._checkTool():
            return
        else:
            global g_buffer_size
            global g_paintBuffer
            cur_buffer_res = g_paintBuffer.resolution().width()
            g_buffer_size.setCurrentIndex( g_buffer_size.findText( str(cur_buffer_res) + ' x ' + str(cur_buffer_res) ) )


    def _setBufferDepth(self):
        ''' Reads the current Buffer depth and sets the Toolbar Dropdown accordingly '''
        if not self._checkTool():
            return
        else:
            global g_buffer_depth
            global g_paintBuffer
            cur_buffer_depth =  g_paintBuffer.depth()
            g_buffer_depth.setCurrentIndex( g_buffer_depth.findData( cur_buffer_depth))

    def _setBufferClamp(self):
        ''' Reads the current Buffer clamp settings and sets the Toolbar Chckbox accordingly '''
        global g_buffer_clamp
        global g_paintBuffer
        cur_buffer_clamp = g_paintBuffer.clampColors()
        g_buffer_clamp.setChecked(cur_buffer_clamp)

    def _checkTool(self):
        ''' Checks if the current Tool is the right tool '''
        if mari.tools.currentTool().name() == 'Transform Paint':
            return True
        else:
            return False


bufferAction = mari.actions.get('/Mari/Tools/General/Transform Paint')
mari.utils.connect(bufferAction.triggered, paintBufferToolbar)