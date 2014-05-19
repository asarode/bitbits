from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from models import Items
from forms import Units
from random import randint
import requests
import json
from decimal import Decimal
import json as simplejson

def update(request):
    random_index = randint(0, Items.objects.count() - 1)
    random_item = Items.objects.all()[random_index]

    BTC = calcBTC(random_item.price)
    mBTC = float(calcBTC(random_item.price)) * 1000


    return HttpResponse('{"item_name": "%s", "item_USD": "%s", "imgfile": "%s", "item_BTC": "%s", "item_mBTC": "%s"}' % (random_item.name, random_item.price, random_item.imgfile, BTC, mBTC))

def calcBTC(item_price):
    rate = requests.get("https://coinbase.com/api/v1/prices/spot_rate").json()
    BTC = '%0.3f' % (item_price/Decimal(rate["amount"]))

    return BTC

def home(request):

    random_index = randint(0, Items.objects.count() - 1)
    random_item = Items.objects.all()[random_index]

    BTC = calcBTC(random_item.price)
    mBTC = float(calcBTC(random_item.price)) * 1000
    
    price = {'BTC': BTC, 'mBTC': mBTC}

    form = Units()

    return render(request, 'index.html', { 'item': random_item, 'form': form, 'price': price })