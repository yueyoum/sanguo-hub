# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/21/14'


from core.purchase import Purchase, PRODUCTS
from utils.decorate import proto_return

from libs import pack_msg
from protomsg import GetProductsResponse, BuyVerityResponse

@proto_return
def get_products(request):
    response = GetProductsResponse()
    response.ret = 0
    for k, v in PRODUCTS.iteritems():
        p = response.products.add()
        p.id = k
        p.name = v['name']
        p.des = v['des']

    return pack_msg(response)


@proto_return
def verify(request):
    req = request._proto

    p = Purchase(req.char_id)
    error_code, product_id, add_sycee = p.verify(req.receipt)
    response = BuyVerityResponse()
    response.ret = error_code
    if error_code:
        return pack_msg(response)

    name = PRODUCTS[product_id]['name']
    response.name = name
    response.add_sycee = add_sycee
    return pack_msg(response)
