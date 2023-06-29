from django.shortcuts import render

# Create your views here.
import joblib
model=joblib.load('./saved_models/model.joblib')
def predict(request):
    return render(request, 'main.html')
def forminfo(request):
    sepal_length=request.GET['sepal_length']
    sepal_width=request.GET['sepal_width']
    petal_length=request.GET['petal_length']
    petal_width=request.GET['petal_width']
    y_pred=model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
    if y_pred[0]==0:
        y_pred='setosa'
    elif y_pred[0]==1:
        y_pred='versicolor'
    else:
        y_pred='viriginica'
    return render(request,'result.html',{'result':y_pred})