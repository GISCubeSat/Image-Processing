#AK_FileAnalysisData
#AK_FileAnalysisGraph
#AK_FileSizeAnalysis
#AK_MaskConversion
#AK_HighContrastEffect

import os

os.system("python AK_FixResolution.py")
os.system("python AK_MaskConversion.py")
os.system("python AK_FileAnalysisData.py")
os.system("python AK_FileAnalysisGraph.py")

print("Done!")