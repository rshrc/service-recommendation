from django.shortcuts import render

# from ml_code.ml_process import server_predictor
from recommend.forms import GetRecommendationForm


def operate_function(product_detail):
    back_camera = product_detail.back_camera
    front_camera = product_detail.front_camera
    resolution_1 = product_detail.resolution_1
    resolution_2 = product_detail.resolution_2
    screen_size = product_detail.screen_size
    battery = product_detail.battery
    price = product_detail.price
    pre_release_demand = product_detail.pre_release_demand
    # sales = product_detail.sales
    # quarter = product_detail.quarter
    # cluster_assigned, predicted_sales = server_predictor.get_prediction(back_camera, front_camera, resolution_1,
    #                                                                    resolution_2, screen_size,
    #                                                                    battery, price, pre_release_demand
    #                                                                    )
    # return cluster_assigned[0], int(predicted_sales[0])


def recommend_view(request):
    """
    View to take the data from the user and process year
    """
    customer_data_filled = False
    cluster_assigned = 0
    predicted_sales = 0
    if request.method == 'POST':
        get_recommendation_form = GetRecommendationForm(data=request.POST)
        if get_recommendation_form.is_valid():
            product_detail = get_recommendation_form.save()
            customer_data_filled = True
            print(product_detail)
            # cluster_assigned, predicted_sales = operate_function(product_detail)
            # print("Cluster Assigned : {}".format(cluster_assigned))
            product_detail.save()
    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        get_recommendation_form = GetRecommendationForm()
    return render(request, 'cart/recommendation.html',
                  {'get_recommendation_form': get_recommendation_form, 'customer_data_filled': customer_data_filled, 'cluster_assigned': cluster_assigned,
                   'predicted_sales': predicted_sales})
