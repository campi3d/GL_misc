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
g_flip_x = None
g_flip_y = None

g_depth_var_dict = {'8 Bit (Byte)': mari.PaintBuffer.BufferDepth.DEPTH_BYTE ,
                    '16 Bit (Half)': mari.PaintBuffer.BufferDepth.DEPTH_HALF ,
                    '32 Bit (Float)': mari.PaintBuffer.BufferDepth.DEPTH_FLOAT
                    }

USER_ROLE = 34


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
        global g_flip_x
        global g_flip_y


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

        g_flip_x = QtGui.QPushButton("Flip X")
        g_flip_y = QtGui.QPushButton("Flip Y")


        # set currents for widgets from active Paintbuffer
        self._setBufferResolutionItem()
        self._setBufferDepthItem()
        self._setBufferClampItem()

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
        toolbar.addWidget(g_flip_x)
        toolbar.addWidget(g_flip_y)
        toolbar.setLocked(True)

        # connect to signals so widgets change when settings are changed in Painting Palette
        #  1 - Signals from Painting Palette to Toolbar
        mari.utils.connect(g_paintBuffer.resolutionChanged, lambda: self._setBufferResolutionItem())
        mari.utils.connect(g_paintBuffer.depthChanged, lambda: self._setBufferDepthItem())
        #  2 - Signals from Toolbar to Painting Palette
        mari.utils.connect(g_buffer_size.currentIndexChanged, lambda: self._changeBufferResolution())
        mari.utils.connect(g_buffer_depth.currentIndexChanged, lambda: self._changeBufferDepth())
        mari.utils.connect(g_buffer_clamp.stateChanged, lambda: self._changeBufferClamp())
        mari.utils.connect(g_double_size.clicked, lambda: self._doubleRes())
        mari.utils.connect(g_halve_size.clicked, lambda: self._halveRes())
        mari.utils.connect(g_flip_x.clicked, lambda: self._flipX())
        mari.utils.connect(g_flip_y.clicked, lambda: self._flipY())



    def _checkTool(self):
        ''' Checks if the current Tool is the right tool '''
        if mari.tools.currentTool().name() == 'Transform Paint':
            return True
        else:
            return False

    def _setBufferResolutionItem(self):
        ''' Reads the current Buffer resolution and sets the Toolbar Dropdown accordingly '''
        if not self._checkTool():
            return
        else:
            global g_buffer_size
            global g_paintBuffer
            cur_buffer_res = g_paintBuffer.resolution().width()
            g_buffer_size.setCurrentIndex( g_buffer_size.findText( str(cur_buffer_res) + ' x ' + str(cur_buffer_res) ) )


    def _setBufferDepthItem(self):
        ''' Reads the current Buffer depth and sets the Toolbar Dropdown accordingly '''
        if not self._checkTool():
            return
        else:
            global g_buffer_depth
            global g_paintBuffer
            cur_buffer_depth =  g_paintBuffer.depth()
            g_buffer_depth.setCurrentIndex( g_buffer_depth.findData( cur_buffer_depth))

    def _setBufferClampItem(self):
        ''' Reads the current Buffer clamp settings and sets the Toolbar Chckbox accordingly '''
        global g_buffer_clamp
        global g_paintBuffer
        cur_buffer_clamp = g_paintBuffer.clampColors()
        g_buffer_clamp.setChecked(cur_buffer_clamp)


    def _changeBufferResolution(self):
        '''Changes the Paint Buffer Resolution'''
        global g_buffer_size
        global g_paintBuffer
        index = g_buffer_size.currentIndex()
        data = g_buffer_size.itemData(index)
        g_paintBuffer.setResolution(data)


    def _changeBufferDepth(self):
        '''Changes the Paint Buffer Depth'''
        global g_buffer_depth
        global g_paintBuffer
        global g_depth_var_dict
        index = g_buffer_depth.currentIndex()
        data = g_buffer_depth.itemText(index)
        depth = g_depth_var_dict[data]
        g_paintBuffer.setDepth(depth)

    def _changeBufferClamp(self):
        '''Changes the Paint Buffer Clamping'''
        global g_buffer_clamp
        global g_paintBuffer
        checkedState = g_buffer_clamp.isChecked()
        g_paintBuffer.setClampColors(checkedState)

    def _doubleRes(self):
        ''' Doubles the Size of the paintBuffer Res'''
        global g_paintBuffer
        global g_buffer_size
        cur_buffer_res = g_paintBuffer.resolution().width()
        cur_buffer_res *= 2
        if cur_buffer_res > 32768:
            cur_buffer_res = 32768
        g_buffer_size.setCurrentIndex( g_buffer_size.findText( str(cur_buffer_res) + ' x ' + str(cur_buffer_res) ) )

    def _halveRes(self):
        ''' Doubles the Size of the paintBuffer Res'''
        global g_paintBuffer
        global g_buffer_size
        cur_buffer_res = g_paintBuffer.resolution().width()
        cur_buffer_res /= 2
        if cur_buffer_res < 256:
            cur_buffer_res = 256
        g_buffer_size.setCurrentIndex( g_buffer_size.findText( str(cur_buffer_res) + ' x ' + str(cur_buffer_res) ) )


    def _flipX(self):
        ''' Flips the Buffer horizontally'''
        global g_paintBuffer
        scale = g_paintBuffer.scale()
        scale_x = g_paintBuffer.scale().width() * (-1.0)
        scale.setWidth(scale_x)
        g_paintBuffer.setScale(scale)

    def _flipY(self):
        ''' Flips the Buffer horizontally'''
        global g_paintBuffer
        scale = g_paintBuffer.scale()
        scale_y = g_paintBuffer.scale().height() * (-1.0)
        scale.setHeight(scale_y)
        g_paintBuffer.setScale(scale)



bufferAction = mari.actions.get('/Mari/Tools/General/Transform Paint')
mari.utils.connect(bufferAction.triggered, paintBufferToolbar)