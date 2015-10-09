import mari
import PySide.QtGui as QtGui

buffer_size_label = QtGui.QLabel("  Resolution ")

buffer_size = QtGui.QComboBox()
buffer_size.addItem("256 x 256", 256)
buffer_size.addItem("512 x 512", 512)
buffer_size.addItem("1024 x 1024", 1024)
buffer_size.addItem("2048 x 2048", 2048)
buffer_size.addItem("4096 x 4096", 4096)
buffer_size.addItem("8192 x 8192", 8192)
buffer_size.addItem("16384 x 16384", 16384)
buffer_size.addItem("32768 x 32768", 32768)

halve_size = QtGui.QPushButton("Halve")
double_size = QtGui.QPushButton("Double")


buffer_depth_label = QtGui.QLabel("  Depth ")

buffer_depth = QtGui.QComboBox()
buffer_depth.addItem("8 Bit (Byte)", 8)
buffer_depth.addItem("16 Bit (Half)", 16)
buffer_depth.addItem("32 Bit (Float)", 32)

buffer_clamp = QtGui.QCheckBox('Clamp')

buffer_sync = QtGui.QCheckBox('Link Depth to Paint Target')



mirror_x = QtGui.QPushButton("Mirror X")
mirror_y = QtGui.QPushButton("Mirror Y")

toolbar = mari.app.findToolBar('Tool Properties')

toolbar.setLocked(False)
toolbar.addWidget(buffer_size_label)
toolbar.addWidget(buffer_size)
toolbar.addWidget(halve_size)
toolbar.addWidget(double_size)
toolbar.addSeparator()
toolbar.addSeparator()
toolbar.addWidget(buffer_depth_label)
toolbar.addWidget(buffer_depth)
toolbar.addSeparator()
toolbar.addWidget(buffer_clamp)
toolbar.addWidget(buffer_sync)
toolbar.addSeparator()
toolbar.addSeparator()
toolbar.addWidget(mirror_x)
toolbar.addWidget(mirror_y)
toolbar.setLocked(True)