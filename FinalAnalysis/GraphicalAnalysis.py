#AK_FileAnalysisData
#AK_FileAnalysisGraph
#AK_FileSizeAnalysis
#AK_MaskConversion
#AK_HighContrastEffect

import os

os.system("python FinalAnalysis/FixResolution.py")
os.system("python FinalAnalysis/CreateMask.py")
os.system("python FinalAnalysis/FileAnalysisData.py")
os.system("python FinalAnalysis/FileAnalysisGraph.py")

print("Done!")