import os
path = 'C:/Users/Divyansh/Downloads/MDisPredic/MultiHealthPrediction/diabetes_model.sav'
if os.path.exists(path):
    print("File exists")
else:
    print("File does not exist")
