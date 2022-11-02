import numpy as np  
import json
import pickle
import config
from sklearn.preprocessing import MinMaxScaler

class DibetesPrediction():
    def __init__(self,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
        self.Glucose = Glucose
        self.BloodPressure = BloodPressure
        self.SkinThickness = SkinThickness
        self.Insulin = Insulin
        self.BMI = BMI
        self.DiabetesPedigreeFunction = DiabetesPedigreeFunction
        self.Age = Age



    def load_model(self):
        with open (config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)


    def get_predict(self):

        self.load_model()

        test_array = np.zeros(len(self.json_data['columns']))

        test_array[0] = self.Glucose
        test_array[1] = self.BloodPressure
        test_array[2] = self.SkinThickness
        test_array[3] = self.Insulin
        test_array[4] = self.BMI
        test_array[5] = self.DiabetesPedigreeFunction
        test_array[6] = self.Age

        print("test_array:",test_array) # 9 values
        normal_scaler = MinMaxScaler()
        array3 = normal_scaler.fit_transform([test_array.reshape(-1,1)][0])
        predicted = self.model.predict([array3.reshape(1,-1)][0])
        return predicted[0]


if __name__ == "__main__":
			

    Glucose  = 150
    BloodPressure  = 76
    SkinThickness  = 23 
    Insulin = 180
    BMI = 26.2
    DiabetesPedigreeFunction = 0.171
    Age = 21


    dib = DibetesPrediction(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    dib.get_predict()