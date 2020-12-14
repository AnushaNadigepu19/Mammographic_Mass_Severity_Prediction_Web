from django.shortcuts import render
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#Home page view


def home(request):
    return render(request, 'index.html')


# custom method for generating predictions
def getPredictions(birads_assessment, age, shape, margin, density):
    import pickle
    model = pickle.load(open(os.path.join(BASE_DIR, "Mammographic_Mass_Severity_Prediction_Web\ModelFiles\model.pkl"), 'rb'))
    prediction = model.predict([[birads_assessment, age, shape, margin, density]])

    if prediction == 0:
        return "begnin"
    elif prediction == 1:
        return "malignant"
    else:
        return "error"


# our result page view
def result(request):
    birads_assessment = int(request.GET['birads_assessment'])
    age = int(request.GET['age'])
    shape = int(request.GET['shape'])
    margin = int(request.GET['margin'])
    density = int(request.GET['density'])

    result = getPredictions(birads_assessment, age, shape, margin, density)

    return render(request, 'result.html', {'result': result})
