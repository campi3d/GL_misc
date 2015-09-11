sets = mari.menus.sets()

for item in sets:
    roots = mari.menus.roots(item)

    for root in roots:
        submenus = mari.menus.submenus(item,root)

        try:
            actions = mari.menus.actions(item,root)
        except:
            pass
        for action in actions:
            print item + '/' +root + '/' + action.name()

        for sub in submenus:

            try:
                actions = mari.menus.actions(item,root,sub)
            except:
                pass
            for action in actions:
                print item + '/' +root + '/' + sub + action.name()


Canvas/Context/&Object Mode
Canvas/Context/&Patch Mode
Canvas/Context/&Face Mode
Canvas/Context/Create Patch Selection Set
Canvas/Context/Create Selection Group
Canvas/Context/Export &FlattenedExport Current &Channel Flattened
Canvas/Context/Export &FlattenedExport &All Channels Flattened
Canvas/Context/Export &FlattenedExport Everything &Flattened
Canvas/Context/&ExportExport Current &Channel
Canvas/Context/&ExportExport &All Channels
Canvas/Context/&ExportExport &Everything
Canvas/Context/&ImportImport into Layer &Stack
Canvas/Context/&ImportImport into &New Channel
Canvas/Context/VisibilityHide &Unselected
Canvas/Context/VisibilityHide &Selected
Canvas/Context/VisibilityShow Se&lected
Canvas/Context/VisibilityShow &All
Canvas/Context/VisibilityShow Entire Object
Canvas/Context/VisibilityIsolate Selection
Canvas/Context/SelectionSelect &All
Canvas/Context/SelectionSelect &None
Canvas/Context/SelectionSelect &Invert
Canvas/Context/SelectionSelect &Visible
Canvas/Context/LockingLock &Unselected
Canvas/Context/LockingLock &Selected
Canvas/Context/LockingUnlock S&elected
Canvas/Context/LockingLock &All
Canvas/Context/LockingUnlock A&ll
Canvas/Context/LockingUnlock Entire Object
MainWindow/&Camera/View All
MainWindow/&Camera/&Load Camera
MainWindow/&Camera/Quick Project Front
MainWindow/&Camera/Quick Project Through
MainWindow/&Camera/Quick Unproject
MainWindow/&Camera/Quick Projection Settings
MainWindow/&Camera/Camera Left
MainWindow/&Camera/Camera Right
MainWindow/&Camera/Camera Top
MainWindow/&Camera/Camera Bottom
MainWindow/&Camera/Camera Front
MainWindow/&Camera/Camera Rear
MainWindow/&Camera/Reset Camera
MainWindow/&Camera/Quick Unproject Channel
MainWindow/&Camera/Quick Unproject Layer
MainWindow/&Channels/Add Channel
MainWindow/&Channels/Channel &Presets
MainWindow/&Channels/Remove Channel
MainWindow/&Channels/Convert Channel
MainWindow/&Channels/Flatten
MainWindow/&Channels/Cut
MainWindow/&Channels/Copy
MainWindow/&Channels/Paste
MainWindow/&Channels/&Lock Channel
MainWindow/&Channels/&UnLock Channel
MainWindow/&Channels/Lock &All Channels
MainWindow/&Channels/U&nlock All Channels
MainWindow/&Channels/Next Channel
MainWindow/&Channels/Previous Channel
MainWindow/&Channels/Transfer
MainWindow/&Channels/Duplicate && Flatten
MainWindow/&Channels/Duplicate
MainWindow/&Channels/Export &FlattenedExport Current &Channel Flattened
MainWindow/&Channels/Export &FlattenedExport &All Channels Flattened
MainWindow/&Channels/Export &FlattenedExport Everything &Flattened
MainWindow/&Channels/Export &FlattenedExport Custom Channel Selection
MainWindow/&Channels/&ExportExport Current &Channel
MainWindow/&Channels/&ExportExport &All Channels
MainWindow/&Channels/&ExportExport &Everything
MainWindow/&Channels/&ExportExport Custom Channel Selection
MainWindow/&Channels/Resi&ze256 x 256
MainWindow/&Channels/Resi&ze512 x 512
MainWindow/&Channels/Resi&ze1024 x 1024
MainWindow/&Channels/Resi&ze2048 x 2048
MainWindow/&Channels/Resi&ze4096 x 4096
MainWindow/&Channels/Resi&ze8192 x 8192
MainWindow/&Channels/Resi&ze16384 x 16384
MainWindow/&Channels/Resi&ze32768 x 32768
MainWindow/&Channels/Resi&zeSave Channel Resolution
MainWindow/&Channels/Resi&zeLoad Channel Resolution
MainWindow/&Channels/&ImportImport into Layer &Stack
MainWindow/&Channels/&ImportImport into &New Channel
MainWindow/&Channels/&SnapshotsSnapshot &All Channels
MainWindow/&Channels/&SnapshotsSnapshot &Current Channel
MainWindow/&Channels/&Snapshots&Manage Snapshots
MainWindow/&Channels/&Snapshots&Delete All Snapshots
MainWindow/&Edit/&Undo
MainWindow/&Edit/&Redo
MainWindow/&Edit/&Preferences
MainWindow/&Edit/&Toolbars
MainWindow/&Edit/&Shortcuts
MainWindow/&Edit/&HUD Manager
MainWindow/&File/&New
MainWindow/&File/&Rename
MainWindow/&File/S&ettings
MainWindow/&File/&Save
MainWindow/&File/&Close
MainWindow/&File/&Quit
MainWindow/&File/Project Paths
MainWindow/&File/Open&1. SphereSet_SphereA
MainWindow/&File/Session&Export Session
MainWindow/&File/Session&Import Session
MainWindow/&File/SessionImport &Channels
MainWindow/&File/SessionImport &Shaders
MainWindow/&Help/Create Example Project
MainWindow/&Help/&About
MainWindow/&Help/Getting Started
MainWindow/&Help/User Guide
MainWindow/&Help/Reference Guide
MainWindow/&Help/&Release Notes
MainWindow/&Help/&Training and Tutorials
MainWindow/&Help/Extension Pack Online Help
MainWindow/&Help/&SDK&API Overview
MainWindow/&Help/&SDKCustom Shader API
MainWindow/&Layers/Add New Layer
MainWindow/&Layers/Cut
MainWindow/&Layers/Copy
MainWindow/&Layers/Paste
MainWindow/&Layers/Remove Layers
MainWindow/&Layers/Merge Layers
MainWindow/&Layers/Add Empty Layer Group
MainWindow/&Layers/Group Layers
MainWindow/&Layers/Flatten Layer Group
MainWindow/&Layers/Transfer
MainWindow/&Layers/Add Channel Layer
MainWindow/&Layers/Clone && Merge Layers
MainWindow/&Layers/Convert To Paintable
MainWindow/&Layers/Add Procedural LayerBasic
MainWindow/&Layers/Add Procedural LayerEnvironment
MainWindow/&Layers/Add Procedural LayerGeometry
MainWindow/&Layers/Add Procedural LayerProcedural
MainWindow/&Layers/Export &FlattenedExport &Selected Layers Flattened
MainWindow/&Layers/Export &FlattenedExport &All Layers Flattened
MainWindow/&Layers/Secondary AdjustmentRemove Secondary Adjustment
MainWindow/&Layers/&ExportExport &Selected Layers
MainWindow/&Layers/&ExportExport &All Layers
MainWindow/&Layers/&ExportExport Selected Masks
MainWindow/&Layers/&ExportExport All Masks
MainWindow/&Layers/SharingShare Layer
MainWindow/&Layers/SharingUnshare Layer
MainWindow/&Layers/SharingShare Layers As Channel
MainWindow/&Layers/SharingMake Shared Channel Current
MainWindow/&Layers/&ImportImport into &Layer
MainWindow/&Layers/&ImportImport into Layer &Stack
MainWindow/&Layers/Visibility + LockToggle Selected Visibility
MainWindow/&Layers/Visibility + LockToggle Unselected Visibility
MainWindow/&Layers/Visibility + LockToggle Selected Lock
MainWindow/&Layers/Visibility + LockToggle Unselected Lock
MainWindow/&Layers/Add Adjustment LayerBrightness
MainWindow/&Layers/Add Adjustment LayerBrightness Lookup
MainWindow/&Layers/Add Adjustment LayerClamp
MainWindow/&Layers/Add Adjustment LayerColor Balance
MainWindow/&Layers/Add Adjustment LayerColor Lookup
MainWindow/&Layers/Add Adjustment LayerColor Switch
MainWindow/&Layers/Add Adjustment LayerColor To Mask
MainWindow/&Layers/Add Adjustment LayerContrast
MainWindow/&Layers/Add Adjustment LayerCopy Channel
MainWindow/&Layers/Add Adjustment LayerFalloff Curve
MainWindow/&Layers/Add Adjustment LayerFlow
MainWindow/&Layers/Add Adjustment LayerGamma
MainWindow/&Layers/Add Adjustment LayerGrade
MainWindow/&Layers/Add Adjustment LayerHSL
MainWindow/&Layers/Add Adjustment LayerHSV
MainWindow/&Layers/Add Adjustment LayerHeight As Normal
MainWindow/&Layers/Add Adjustment LayerHue Shift
MainWindow/&Layers/Add Adjustment LayerInvert
MainWindow/&Layers/Add Adjustment LayerLevels
MainWindow/&Layers/Add Adjustment LayerLinear To Log
MainWindow/&Layers/Add Adjustment LayerLog To Linear
MainWindow/&Layers/Add Adjustment LayerLuminosity
MainWindow/&Layers/Add Adjustment LayerPremultiply Alpha
MainWindow/&Layers/Add Adjustment LayerSaturation
MainWindow/&Layers/Add Adjustment LayerScale
MainWindow/&Layers/Add Adjustment LayerSet Value
MainWindow/&Layers/Add Adjustment LayerShuffle
MainWindow/&Layers/Add Adjustment LayerTangent To Screen
MainWindow/&Layers/Add Adjustment LayerTangent To World
MainWindow/&Layers/Add Adjustment LayerWorld To Tangent
MainWindow/&Layers/Add Adjustment LayersRGB2Linear
MainWindow/&Layers/Add Adjustment LayerCustom
MainWindow/&Layers/Adjustment StackBake Adjustment Stack
MainWindow/&Layers/Adjustment StackRemove Adjustment Stack
MainWindow/&Layers/Adjustment StackEnable Adjustment Stack
MainWindow/&Layers/Adjustment StackDisable Adjustment Stack
MainWindow/&Layers/CachingCache Layers
MainWindow/&Layers/CachingCache Up To Here
MainWindow/&Layers/CachingUncache Layers
MainWindow/&Layers/CachingUncache Up To Here
MainWindow/&Layers/Layer MaskBake Mask
MainWindow/&Layers/Layer MaskRemove Mask
MainWindow/&Layers/Layer MaskCut
MainWindow/&Layers/Layer MaskCopy
MainWindow/&Layers/Layer MaskPaste
MainWindow/&Layers/Layer MaskMake Mask Stack
MainWindow/&Layers/Layer MaskFlatten Mask Stack
MainWindow/&Layers/Layer MaskEnable Mask
MainWindow/&Layers/Layer MaskDisable Mask
MainWindow/&Nuke/&Launch Nuke
MainWindow/&Nuke/&Import Projection
MainWindow/&Nuke/&Help
MainWindow/&Nuke/&ExportProjection &Texture
MainWindow/&Nuke/&Export&Unique Projection Texture
MainWindow/&Nuke/&ExportUV Texture(s) (&All Channels)
MainWindow/&Nuke/&ExportUV Texture(s) (&Current Channel)
MainWindow/&Nuke/&ExportCurrent &View
MainWindow/&Nuke/&ExportCurrent &Projector
MainWindow/&Nuke/&ExportAll Pro&jectors
MainWindow/&Nuke/&SendProjection &Texture
MainWindow/&Nuke/&Send&Unique Projection Texture
MainWindow/&Nuke/&SendUV Texture(s) (&All Channels)
MainWindow/&Nuke/&SendUV Texture(s) (&Current Channel)
MainWindow/&Nuke/&SendCurrent &View
MainWindow/&Nuke/&SendCurrent &Projector
MainWindow/&Nuke/&SendAll Pro&jectors
MainWindow/&Objects/&Add Object
MainWindow/&Objects/Add Locator
MainWindow/&Objects/Reset Object Transform
MainWindow/&Objects/&Remove Object
MainWindow/&Objects/&Ambient Occlusion
MainWindow/&Objects/&Subdivide
MainWindow/&Objects/Export Object
MainWindow/&Objects/Export UV Mask
MainWindow/&Objects/GenerateGaussian Blur
MainWindow/&Objects/GenerateDisplacement
MainWindow/&Objects/GenerateHeight
MainWindow/&Objects/DuplicateObject Only
MainWindow/&Objects/DuplicateObject And Shader Network
MainWindow/&Objects/SubdivisionSet all to Highest Level
MainWindow/&Objects/SubdivisionSet all to Lowest Level
MainWindow/&Objects/SubdivisionSet all Visible to Highest Level
MainWindow/&Objects/SubdivisionSet all Visible to Lowest Level
MainWindow/&Painting/&Clear Painting
MainWindow/&Painting/Toggle Mask Preview
MainWindow/&Painting/&Bake
MainWindow/&Painting/B&ake and Clear
MainWindow/&Painting/&Save Painting
MainWindow/&Painting/&Load Painting
MainWindow/&Selection/&Object Mode
MainWindow/&Selection/&Patch Mode
MainWindow/&Selection/&Face Mode
MainWindow/&Selection/Hide &Unselected
MainWindow/&Selection/Hide &Selected
MainWindow/&Selection/Show Se&lected
MainWindow/&Selection/Show &All
MainWindow/&Selection/Show Entire Object
MainWindow/&Selection/Select &All
MainWindow/&Selection/Select &None
MainWindow/&Selection/Select &Invert
MainWindow/&Selection/Select &Visible
MainWindow/&Selection/Lock &Unselected
MainWindow/&Selection/Lock &Selected
MainWindow/&Selection/Unlock S&elected
MainWindow/&Selection/Lock &All
MainWindow/&Selection/Unlock A&ll
MainWindow/&Selection/Unlock Entire Object
MainWindow/&Selection/Isolate Selection
MainWindow/&Tools/P&lugins
MainWindow/&Tools/&Import Brushes
MainWindow/&Tools/&License
MainWindow/&Tools/Shader Console
MainWindow/&View/&Display Properties
MainWindow/&View/&Save Layout
MainWindow/&View/&Load Layout
MainWindow/&View/&Default Layout
MainWindow/&View/&Take Screenshot
MainWindow/&View/S&creenshot Settings
MainWindow/&View/Toggle Palettes Visibility
MainWindow/&View/Fu&ll Screen
MainWindow/&View/Screenshot All Channels
MainWindow/&View/&PalettesPatches
MainWindow/&View/&PalettesObjects
MainWindow/&View/&PalettesLights
MainWindow/&View/&PalettesProjectors
MainWindow/&View/&PalettesSelection Groups
MainWindow/&View/&PalettesColor Manager
MainWindow/&View/&PalettesImage Manager
MainWindow/&View/&PalettesHistory View
MainWindow/&View/&PalettesBrush Editor
MainWindow/&View/&PalettesPlay Controls
MainWindow/&View/&PalettesPython Console
MainWindow/&View/&PalettesShaders
MainWindow/&View/&PalettesChannels
MainWindow/&View/&PalettesLayers
MainWindow/&View/&PalettesNode Graph
MainWindow/&View/&PalettesNode Properties
MainWindow/&View/&PalettesPixelAnalyzer
MainWindow/&View/&PalettesColors
MainWindow/&View/&PalettesTool Properties
MainWindow/&View/&PalettesPainting
MainWindow/&View/&PalettesProjection
MainWindow/&View/&PalettesShelf
MainWindow/&View/&PalettesSnapshots
MainWindow/&View/&PalettesModo Render
MainWindow/F&ilters/&Invert
MainWindow/F&ilters/&Luminosity
MainWindow/F&ilters/&Gamma
MainWindow/F&ilters/&sRGB To Linear
MainWindow/F&ilters/&Hue
MainWindow/F&ilters/&Brightness
MainWindow/F&ilters/&Contrast
MainWindow/F&ilters/&Clamp
MainWindow/F&ilters/&Levels
MainWindow/F&ilters/&Color Curves
MainWindow/F&ilters/&Color Switches
MainWindow/F&ilters/&Tone Mapping
MainWindow/F&ilters/&Copy Channel
MainWindow/F&ilters/&Premultiply Alpha
MainWindow/F&ilters/&Edge Detect
MainWindow/F&ilters/&Emboss
MainWindow/F&ilters/&Sharpen
MainWindow/F&ilters/&High Pass
MainWindow/F&ilters/&Color Correction
MainWindow/F&ilters/&Add Noise
MainWindow/F&ilters/&Blur&Blur
MainWindow/F&ilters/&Blur&Soften
MainWindow/F&ilters/&Blur&Gaussian
MainWindow/P&atches/Extract &Selected
MainWindow/P&atches/Select &Range
MainWindow/P&atches/&Copy Indexes to Clipboard
MainWindow/P&atches/Quick &Paste
MainWindow/P&atches/Quick &Copy
MainWindow/P&atches/&Copy Textures
MainWindow/P&atches/UV &Mask to Image Manager
MainWindow/P&atches/UV Wireframe to Image Manager
MainWindow/P&atches/&Bleed Patch Edges
MainWindow/P&atches/Patch to Image Manager
MainWindow/P&atches/&FillB&lack
MainWindow/P&atches/&Fill&Gray
MainWindow/P&atches/&Fill&White
MainWindow/P&atches/&Fill&Foreground
MainWindow/P&atches/&Fill&Background
MainWindow/P&atches/&Fill&Transparent
MainWindow/P&atches/&Fill&UV Mask
MainWindow/P&atches/&Fill&Wireframe
MainWindow/P&atches/&MirrorMirror &Left to Right
MainWindow/P&atches/&MirrorMirror &Right to Left
MainWindow/P&atches/&MirrorMirror &Top to Bottom
MainWindow/P&atches/&MirrorMirror &Bottom to Top
MainWindow/P&atches/&TransformFlip &Vertical
MainWindow/P&atches/&TransformFlip &Horizontal
MainWindow/P&atches/&Transform&Rotate 90 CCW
MainWindow/P&atches/&TransformRotate 90 &CW
MainWindow/P&atches/&TransformRotate &180
MainWindow/P&atches/&LinkLin&k Selected Patch Images
MainWindow/P&atches/&LinkUnli&nk Selected Patch Images
MainWindow/P&atches/&Link&Select Linked Patch Images
MainWindow/P&atches/&LinkUnlink &All Linked Patch Images
MainWindow/P&atches/Resi&ze Selected256 x 256
MainWindow/P&atches/Resi&ze Selected512 x 512
MainWindow/P&atches/Resi&ze Selected1024 x 1024
MainWindow/P&atches/Resi&ze Selected2048 x 2048
MainWindow/P&atches/Resi&ze Selected4096 x 4096
MainWindow/P&atches/Resi&ze Selected8192 x 8192
MainWindow/P&atches/Resi&ze Selected16384 x 16384
MainWindow/P&atches/Resi&ze Selected32768 x 32768
MainWindow/P&atches/Resi&ze SelectedHalve Size
MainWindow/P&atches/Resi&ze SelectedDouble Size
MainWindow/P&ython/&Documentation
MainWindow/P&ython/&Readme
MainWindow/P&ython/Show &Console
MainWindow/P&ython/&ExamplesOpen Examples &Folder
MainWindow/P&ython/&ExamplesBake on New Layer
MainWindow/P&ython/&ExamplesMake Tools Menu
MainWindow/P&ython/&Examples&Asset Management
MainWindow/P&ython/&ExamplesCommand Port
MainWindow/P&ython/&ExamplesCreate Blacksmith Project
MainWindow/P&ython/&ExamplesCreate Project
MainWindow/P&ython/&ExamplesCreate Project And Import
MainWindow/P&ython/&ExamplesExport Image Sets
MainWindow/P&ython/&ExamplesExport Shelf
MainWindow/P&ython/&Examples&Paint Buffer
MainWindow/P&ython/&ExamplesResource Info
MainWindow/P&ython/&Examples&Setup Vector Brush
MainWindow/P&ython/&ExamplesCreate Vector Channels
MainWindow/P&ython/&ExamplesExport for Maya
MainWindow/Pte&x/&Double Face Resolution
MainWindow/Pte&x/&Halve Face Resolution
MainWindow/Pte&x/&World Space Face Resolution
MainWindow/Pte&x/&Set Face Resolution
MainWindow/Pte&x/Fill Faces &Foreground
MainWindow/Pte&x/Fill Faces &Background
MainWindow/Scripts/ShadingPause Viewport Update
MainWindow/Scripts/Selection GroupsMaterialID from Selection Groups
MainWindow/Scripts/Image ManagerExport Selection
MainWindow/Scripts/LayersAdd Channel Layer
MainWindow/Scripts/LayersClone && Merge Layers
MainWindow/Scripts/LayersConvert To Paintable
MainWindow/Scripts/ViewScreenshot All Channels
MainWindow/Scripts/ShadersSync Object Shaders
MainWindow/Scripts/CameraQuick Unproject Channel
MainWindow/Scripts/CameraQuick Unproject Layer
MainWindow/Scripts/PatchesPatch to Image Manager
MainWindow/Scripts/FileProject Paths
MainWindow/Scripts/ObjectsExport Object
MainWindow/Scripts/ObjectsExport UV Mask
MainWindow/Scripts/ChannelsDuplicate && Flatten
MainWindow/Scripts/ChannelsDuplicate
MainWindow/Scripts/SelectionIsolate Selection
MainWindow/Scripts/HelpExtension Pack Online Help
MainWindow/Sha&ding/Add New Shader
MainWindow/Sha&ding/Duplicate Shader
MainWindow/Sha&ding/Remove Shader
MainWindow/Sha&ding/&Flat
MainWindow/Sha&ding/&Basic
MainWindow/Sha&ding/F&ull
MainWindow/Sha&ding/Shadows
MainWindow/Sha&ding/Toggle &Wireframe
MainWindow/Sha&ding/Toggle &UvImage
MainWindow/Sha&ding/Toggle Whole Patch Project
MainWindow/Sha&ding/Pause Viewport Update
MainWindow/Sha&ding/Sync Object Shaders
MriBasicLight/CollectionContext/Disable Lights
MriBasicLight/CollectionContext/Enable Lights
MriBasicLight/CollectionContext/&Reset Lights
MriBasicLight/ItemContext/Disable Lights
MriBasicLight/ItemContext/Enable Lights
MriBasicLight/Panel/Disable Lights
MriBasicLight/Panel/Enable Lights
MriBasicLight/Panel/&Reset Lights
MriChannel/CollectionContext/&Add Channel
MriChannel/CollectionContext/Channel &Presets
MriChannel/ItemContext/Channel &Presets
MriChannel/ItemContext/Convert Channel
MriChannel/ItemContext/&Duplicate Channel
MriChannel/ItemContext/&Remove Channel
MriChannel/ItemContext/&Alpha To Mask
MriChannel/ItemContext/&Mask to Alpha
MriChannel/ItemContext/Snapshot &All Channels
MriChannel/ItemContext/Snapshot &Current Channel
MriChannel/ItemContext/&Manage Snapshots
MriChannel/ItemContext/&Lock Channel
MriChannel/ItemContext/&UnLock Channel
MriChannel/Panel/Snapshot &All Channels
MriChannel/Panel/Snapshot &Current Channel
MriChannel/Panel/&Manage Snapshots
MriChannel/Panel/Channel &Presets
MriChannel/Panel/&Add Channel
MriChannel/Panel/Convert Channel
MriChannel/Panel/&Remove Channel
MriEntity/ItemContext/Add Child Object
MriEntity/ItemContext/Add Child Locator
MriEntity/ItemContext/&Remove Object
MriFaceSelectionGroup/ItemContext/Select Selection Group
MriFaceSelectionGroup/ItemContext/Lock Selection Group
MriFaceSelectionGroup/ItemContext/Unlock Selection Group
MriFaceSelectionGroup/ItemContext/Hide Selection Group
MriFaceSelectionGroup/ItemContext/Show Selection Group
MriFaceSelectionGroup/ItemContext/Remove Selection Group
MriGeoEntity/CollectionContext/&Add Object
MriGeoEntity/CollectionContext/Add Locator
MriGeoEntity/ItemContext/&Add Version
MriGeoEntity/ItemContext/Rename Version
MriGeoEntity/ItemContext/&Remove Version
MriGeoEntity/ItemContext/&Remove Object
MriGeoEntity/ItemContext/Add Child Object
MriGeoEntity/ItemContext/Add Child Locator
MriGeoEntity/ItemContext/&Ambient Occlusion
MriGeoEntity/ItemContext/&Subdivide
MriGeoEntity/ItemContext/Export Object
MriGeoEntity/ItemContext/Export UV Mask
MriGeoEntity/ItemContext/GenerateGaussian Blur
MriGeoEntity/ItemContext/GenerateDisplacement
MriGeoEntity/ItemContext/GenerateHeight
MriGeoEntity/ItemContext/DuplicateObject Only
MriGeoEntity/ItemContext/DuplicateObject And Shader Network
MriGeoEntity/ItemContext/SubdivisionSet all to Highest Level
MriGeoEntity/ItemContext/SubdivisionSet all to Lowest Level
MriGeoEntity/ItemContext/SubdivisionSet all Visible to Highest Level
MriGeoEntity/ItemContext/SubdivisionSet all Visible to Lowest Level
MriGeoEntity/Panel/&Add Object
MriGeoEntity/Panel/Add Locator
MriGeoEntity/Panel/&Remove Object
MriGeoEntitySelectionGroup/ItemContext/Select Selection Group
MriGeoEntitySelectionGroup/ItemContext/Lock Selection Group
MriGeoEntitySelectionGroup/ItemContext/Unlock Selection Group
MriGeoEntitySelectionGroup/ItemContext/Hide Selection Group
MriGeoEntitySelectionGroup/ItemContext/Show Selection Group
MriGeoEntitySelectionGroup/ItemContext/Remove Selection Group
MriGeoLight/ItemContext/Move to Camera Position
MriGeoLight/Panel/Move to Camera Position
MriGeometrySelectionGroup/Panel/Create Selection Group
MriGeometrySelectionGroup/Panel/Remove Selection Group
MriGeometrySelectionGroup/Panel/Select Selection Group
MriGeometrySelectionGroup/Panel/Lock Selection Group
MriGeometrySelectionGroup/Panel/Unlock Selection Group
MriGeometrySelectionGroup/Panel/Hide Selection Group
MriGeometrySelectionGroup/Panel/Show Selection Group
MriGeometrySelectionGroup/Panel/MaterialID from Selection Groups
MriImageManager/ItemContext/Run Script
MriImageManager/ItemContext/Quick &Copy
MriImageManager/ItemContext/Export Selection
MriLayer/CollectionContext/&ExportExport &All Layers
MriLayer/CollectionContext/&ExportExport &All Layers Flattened
MriLayer/CollectionContext/&ExportExport All Masks
MriLayer/CollectionContext/&ImportImport into Layer &Stack
MriLayerShader/AddShader/Phong
MriLayerShader/AddShader/Cook Torrance
MriLayerShader/AddShader/Beckman
MriLayerShader/AddShader/Blinn
MriLayerShader/AddShader/Flat
MriLayerShader/AddShader/Unreal
MriLayerShader/AddShader/BRDF
MriLayerShader/AddShader/Standard Lighting
MriLayerShader/AddShader/AiStandard
MriLayerShader/AddShader/RedshiftArchitectural
MriLayerShader/AddShader/VRayMtl
MriLayerShader/AddShader/Layered
MriLayerShader/AddShader/Choose Diffuse And Specular
MriLayerShader/AddShader/Ward Isotropic
MriLayerShader/AddShader/Ward Anisotropic
MriLayerShader/AddShader/Mia Material BRDF
MriLayerShader/AddShader/Unreal Advanced
MriLayerShader/CollectionContext/Add New Shader
MriLayerShader/CollectionContext/Duplicate Shader
MriLayerShader/CollectionContext/Remove Shader
MriLayerShader/CollectionContext/Cut
MriLayerShader/CollectionContext/Copy
MriLayerShader/CollectionContext/Paste
MriLayerShader/CollectionContext/Sync Object Shaders
MriLayer_MriLayerShader/AddShader/Phong
MriLayer_MriLayerShader/AddShader/Cook Torrance
MriLayer_MriLayerShader/AddShader/Beckman
MriLayer_MriLayerShader/AddShader/Blinn
MriLayer_MriLayerShader/AddShader/Flat
MriLayer_MriLayerShader/AddShader/Unreal
MriLayer_MriLayerShader/AddShader/BRDF
MriLayer_MriLayerShader/AddShader/Standard Lighting
MriLayer_MriLayerShader/AddShader/AiStandard
MriLayer_MriLayerShader/AddShader/RedshiftArchitectural
MriLayer_MriLayerShader/AddShader/VRayMtl
MriLayer_MriLayerShader/AddShader/Choose Diffuse And Specular
MriLayer_MriLayerShader/AddShader/Ward Isotropic
MriLayer_MriLayerShader/AddShader/Ward Anisotropic
MriLayer_MriLayerShader/AddShader/Mia Material BRDF
MriLayer_MriLayerShader/AddShader/Unreal Advanced
MriLocatorEntity/ItemContext/Add Child Object
MriLocatorEntity/ItemContext/Add Child Locator
MriLocatorEntity/ItemContext/&Remove Object
MriPatchSelectionGroup/ItemContext/Select Selection Group
MriPatchSelectionGroup/ItemContext/Lock Selection Group
MriPatchSelectionGroup/ItemContext/Unlock Selection Group
MriPatchSelectionGroup/ItemContext/Hide Selection Group
MriPatchSelectionGroup/ItemContext/Show Selection Group
MriPatchSelectionGroup/ItemContext/Remove Selection Group
MriProject/ItemContext/&Add Channel
MriProjector/CollectionContext/&Load Projector
MriProjector/CollectionContext/&Create Projector
MriProjector/CollectionContext/Save &All Projectors
MriProjector/ItemContext/&Make Projector Current
MriProjector/ItemContext/&Update Transform From Paint Buffer
MriProjector/ItemContext/&Update Global Settings From Projector
MriProjector/ItemContext/&Update Only Masks From Projector
MriProjector/ItemContext/&Project
MriProjector/ItemContext/&Unproject
MriProjector/ItemContext/&Render Turntable
MriProjector/ItemContext/&Diagnostic Turntable
MriProjector/ItemContext/&Import Image
MriProjector/ItemContext/&Save Projector
MriProjector/ItemContext/Save &All Projectors
MriProjector/ItemContext/&Remove Projector
MriProjector/Panel/&Create Projector
MriProjector/Panel/&Save Projector
MriProjector/Panel/&Load Projector
MriProjector/Panel/&Remove Projector
MriShader/CollectionContext/&Open Shader Template
MriShader/ItemContext/&Duplicate Shader
MriShader/ItemContext/&Save Shader As Template
MriShader/ItemContext/&Bake Shader
MriShader/Panel/&Save Shader
MriShader/Panel/&Open Shader
MriShader/Panel/&Remove Shader
MriSurfaceShader/CollectionContext/Add SurfaceShader
MriSurfaceShader/CollectionContext/&Duplicate Shader
MriSurfaceShader/CollectionContext/Remove SurfaceShader
MriSurfaceShader/CollectionContext/&Load Shader
MriSurfaceShader/ItemContext/&Duplicate Shader
MriSurfaceShader/ItemContext/Remove SurfaceShader
MriSurfaceShader/ItemContext/&Save Shader
MriSurfaceShader/ItemContext/&Bake Shader
MriSurfaceShader/Panel/Add SurfaceShader
MriSurfaceShader/Panel/&Duplicate Shader
MriSurfaceShader/Panel/Remove SurfaceShader
MriSurfaceShader/Panel/&Load Shader
MriSurfaceShader/Panel/&Save Shader
MriUvPatch/CollectionContext/Select &All Patches
MriUvPatch/CollectionContext/Select &None Patches
MriUvPatch/CollectionContext/Select &Invert Patches
MriUvPatch/CollectionContext/Select &Visible Patches
MriUvPatch/CollectionContext/&Lock Selected Patches
MriUvPatch/CollectionContext/&Lock Unselected Patches
MriUvPatch/CollectionContext/&Unlock Selected Patches
MriUvPatch/CollectionContext/&Unlock Unselected Patches
MriUvPatch/CollectionContext/&Lock All Patches
MriUvPatch/CollectionContext/&Unlock All Patches
MriUvPatch/CollectionContext/UV &Mask to Image Manager
MriUvPatch/CollectionContext/&Bleed Patch Edges
MriUvPatch/CollectionContext/Hide &Unselected Patches
MriUvPatch/CollectionContext/Hide &Selected Patches
MriUvPatch/CollectionContext/Show &All Patches
MriUvPatch/CollectionContext/Show Se&lected Patches
MriUvPatch/CollectionContext/Show Unselecte&d Patches
MriUvPatch/CollectionContext/Lin&k Selected Patch Images
MriUvPatch/CollectionContext/Unli&nk Selected Patch Images
MriUvPatch/CollectionContext/&Select Linked Patch Images
MriUvPatch/CollectionContext/Unlink &All Linked Patch Images
MriUvPatch/CollectionContext/&Copy Indexes to Clipboard
MriUvPatch/ItemContext/Select &All Patches
MriUvPatch/ItemContext/Select &None Patches
MriUvPatch/ItemContext/Select &Invert Patches
MriUvPatch/ItemContext/Select &Visible Patches
MriUvPatch/ItemContext/&Lock Selected Patches
MriUvPatch/ItemContext/&Lock Unselected Patches
MriUvPatch/ItemContext/&Unlock Selected Patches
MriUvPatch/ItemContext/&Unlock Unselected Patches
MriUvPatch/ItemContext/&Lock All Patches
MriUvPatch/ItemContext/&Unlock All Patches
MriUvPatch/ItemContext/UV &Mask to Image Manager
MriUvPatch/ItemContext/&Bleed Patch Edges
MriUvPatch/ItemContext/Hide &Unselected Patches
MriUvPatch/ItemContext/Hide &Selected Patches
MriUvPatch/ItemContext/Show &All Patches
MriUvPatch/ItemContext/Show Se&lected Patches
MriUvPatch/ItemContext/Show Unselecte&d Patches
MriUvPatch/ItemContext/Lin&k Selected Patch Images
MriUvPatch/ItemContext/Unli&nk Selected Patch Images
MriUvPatch/ItemContext/&Select Linked Patch Images
MriUvPatch/ItemContext/Unlink &All Linked Patch Images
MriUvPatch/ItemContext/&Copy Indexes to Clipboard
MriUvPatch/ItemContext/Resi&ze Selected256 x 256
MriUvPatch/ItemContext/Resi&ze Selected512 x 512
MriUvPatch/ItemContext/Resi&ze Selected1024 x 1024
MriUvPatch/ItemContext/Resi&ze Selected2048 x 2048
MriUvPatch/ItemContext/Resi&ze Selected4096 x 4096
MriUvPatch/ItemContext/Resi&ze Selected8192 x 8192
MriUvPatch/ItemContext/Resi&ze Selected16384 x 16384
MriUvPatch/ItemContext/Resi&ze Selected32768 x 32768
MriUvPatch/ItemContext/Resi&ze SelectedHalve Size
MriUvPatch/ItemContext/Resi&ze SelectedDouble Size
MriUvPatch/Panel/Hide &Selected Patches
MriUvPatch/Panel/Show &All Patches
MriUvPatch/Panel/Select &All Patches
MriUvPatch/Panel/&Lock Selected Patches
MriUvPatch/Panel/&Unlock Selected Patches
MriUvPatch/Panel/Lin&k Selected Patch Images
MriUvPatch/Panel/Unli&nk Selected Patch Images
Shaders/Panel/Sync Object Shaders
