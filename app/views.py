from django.shortcuts import render
from django.http import JsonResponse
from . import predict 

def dumbanengue(request):
    if request.method == "GET":

        return render(request, 'index.html')


    if request.method == "POST":

        paramas = {}

        paramas['year'] = int(request.POST.get('year', 0))
        paramas['month'] = int(request.POST.get('month', 0))
        paramas['province'] = int(request.POST.get('province', 0))
        paramas['category'] = int(request.POST.get('category', 0))
        paramas['product'] = int(request.POST.get('product', 0))


        model = predict.get_model()

        feature_columns = predict.get_commodity_data(paramas)

        predicted_price = predict.predict_food_price(model, feature_columns)

        if predicted_price < 1:
            predicted_price = 'Currently Invaluable'
        else:
            predicted_price = f'{predicted_price:.2f} MZN'


        # return render(request, 'index.html', {'msg': predicted_price})
        return JsonResponse({'success': True, 'msg': predicted_price})
