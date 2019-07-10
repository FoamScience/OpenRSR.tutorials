#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
fiveSpot06OpenFOAM = FindSource('fiveSpot06.OpenFOAM')

# set active source
SetActiveSource(fiveSpot06OpenFOAM)

# get color transfer function/color map for 'Sw'
swLUT = GetColorTransferFunction('Sw')
swLUT.LockDataRange = 0
swLUT.InterpretValuesAsCategories = 0
swLUT.ShowCategoricalColorsinDataRangeOnly = 0
swLUT.RescaleOnVisibilityChange = 0
swLUT.EnableOpacityMapping = 0
swLUT.RGBPoints = [0.160099998116493, 0.0, 0.0, 1.0, 0.783000111579895, 1.0, 0.0, 0.0]
swLUT.UseLogScale = 0
swLUT.ColorSpace = 'HSV'
swLUT.UseBelowRangeColor = 0
swLUT.BelowRangeColor = [0.0, 0.0, 0.0]
swLUT.UseAboveRangeColor = 0
swLUT.AboveRangeColor = [1.0, 1.0, 1.0]
swLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
swLUT.Discretize = 1
swLUT.NumberOfTableValues = 256
swLUT.ScalarRangeInitialized = 1.0
swLUT.HSVWrap = 0
swLUT.VectorComponent = 0
swLUT.VectorMode = 'Magnitude'
swLUT.AllowDuplicateScalars = 1
swLUT.Annotations = ['0', '0', '1', '1', '3', '3', '', '']
swLUT.ActiveAnnotatedValues = []
swLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]

# get opacity transfer function/opacity map for 'Sw'
swPWF = GetOpacityTransferFunction('Sw')
swPWF.Points = [0.160099998116493, 0.0, 0.5, 0.0, 0.783000111579895, 1.0, 0.5, 0.0]
swPWF.AllowDuplicateScalars = 1
swPWF.ScalarRangeInitialized = 1

# find source
annotateTimeFilter1 = FindSource('AnnotateTimeFilter1')

# set active source
SetActiveSource(annotateTimeFilter1)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [633, 518]

# export view
ExportView('/home/elwardi/gitea-repositories/elwardi/reservoir-simulator.git/tutorials/impesFoam/TanejaDr/fiveSpot06/time01.pdf', view=renderView1, Plottitle='ParaView GL2PS Export',
    Compressoutputfile=0,
    Drawbackground=1,
    Cullhiddenprimitives=1,
    Linewidthscalingfactor=0.714,
    Pointsizescalingfactor=0.714,
    GL2PSdepthsortmethod='Simple sorting (fast, good)',
    Rasterize3Dgeometry=1,
    Dontrasterizecubeaxes=1,
    Rendertextaspaths=1)

# get animation scene
animationScene1 = GetAnimationScene()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

# export view
ExportView('/home/elwardi/gitea-repositories/elwardi/reservoir-simulator.git/tutorials/impesFoam/TanejaDr/fiveSpot06/time07.pdf', view=renderView1, Plottitle='ParaView GL2PS Export',
    Compressoutputfile=0,
    Drawbackground=1,
    Cullhiddenprimitives=1,
    Linewidthscalingfactor=0.714,
    Pointsizescalingfactor=0.714,
    GL2PSdepthsortmethod='Simple sorting (fast, good)',
    Rasterize3Dgeometry=1,
    Dontrasterizecubeaxes=1,
    Rendertextaspaths=1)

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToPrevious()

animationScene1.GoToPrevious()

animationScene1.GoToPrevious()

animationScene1.GoToPrevious()

animationScene1.GoToPrevious()

# export view
ExportView('/home/elwardi/gitea-repositories/elwardi/reservoir-simulator.git/tutorials/impesFoam/TanejaDr/fiveSpot06/time10.pdf', view=renderView1, Plottitle='ParaView GL2PS Export',
    Compressoutputfile=0,
    Drawbackground=1,
    Cullhiddenprimitives=1,
    Linewidthscalingfactor=0.714,
    Pointsizescalingfactor=0.714,
    GL2PSdepthsortmethod='Simple sorting (fast, good)',
    Rasterize3Dgeometry=1,
    Dontrasterizecubeaxes=1,
    Rendertextaspaths=1)

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToPrevious()

# export view
ExportView('/home/elwardi/gitea-repositories/elwardi/reservoir-simulator.git/tutorials/impesFoam/TanejaDr/fiveSpot06/time14.pdf', view=renderView1, Plottitle='ParaView GL2PS Export',
    Compressoutputfile=0,
    Drawbackground=1,
    Cullhiddenprimitives=1,
    Linewidthscalingfactor=0.714,
    Pointsizescalingfactor=0.714,
    GL2PSdepthsortmethod='Simple sorting (fast, good)',
    Rasterize3Dgeometry=1,
    Dontrasterizecubeaxes=1,
    Rendertextaspaths=1)

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

# export view
ExportView('/home/elwardi/gitea-repositories/elwardi/reservoir-simulator.git/tutorials/impesFoam/TanejaDr/fiveSpot06/time21.pdf', view=renderView1, Plottitle='ParaView GL2PS Export',
    Compressoutputfile=0,
    Drawbackground=1,
    Cullhiddenprimitives=1,
    Linewidthscalingfactor=0.714,
    Pointsizescalingfactor=0.714,
    GL2PSdepthsortmethod='Simple sorting (fast, good)',
    Rasterize3Dgeometry=1,
    Dontrasterizecubeaxes=1,
    Rendertextaspaths=1)

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

animationScene1.GoToNext()

# export view
ExportView('/home/elwardi/gitea-repositories/elwardi/reservoir-simulator.git/tutorials/impesFoam/TanejaDr/fiveSpot06/time25.pdf', view=renderView1, Plottitle='ParaView GL2PS Export',
    Compressoutputfile=0,
    Drawbackground=1,
    Cullhiddenprimitives=1,
    Linewidthscalingfactor=0.714,
    Pointsizescalingfactor=0.714,
    GL2PSdepthsortmethod='Simple sorting (fast, good)',
    Rasterize3Dgeometry=1,
    Dontrasterizecubeaxes=1,
    Rendertextaspaths=1)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [2.18416821200034, 9.28271490100149, 273.711910798532]
renderView1.CameraFocalPoint = [2.18416821200034, 9.28271490100149, 0.5]
renderView1.CameraParallelScale = 70.7124458635112

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
exit()
