from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
import pandas as pd
import io
import matplotlib
matplotlib.use('Agg') # Matplotlib の backend を指定
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter

   
def index(request):

    

    return render(request, 'index.html', {
    "data":"これはデータ変数です"
    })

#png画像形式に変換数関数
def plt2png():
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=200)
    s = buf.getvalue()
    buf.close()
    return s

def view_plot1(request):
    # matplotを使って作図する

    # x = [1, 5, 9]
    # y = [4, 6, 8]
    # ax = plt.subplot()
    # ax.scatter(x, y)
    # png = plt2png()
    # plt.cla()

    df1 = pd.read_parquet("/Users/takatoshiinaoka/Desktop/django/dec_team_a/app/201807-043398656781-043398656781.parquet")
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    #print(df1)
    ret=df1["product_code"].value_counts()
    print(ret)
    ret.plot.bar()
    png = plt2png()
    plt.cla()

    response = HttpResponse(png, content_type='image/png')
    return response

    

    # response = HttpResponse(content_type="image/png")
    # Image.save(response, "PNG")
    # return response


def graph(request):
    return render(request, 'graph.html', {
    "data": "データ"
    })

def get_graph_data(request):
    allInoutData = [{"input":"I","total":1700},{"input":"o","total":1700}]
    return JsonResponse(list(allInoutData),safe=False)