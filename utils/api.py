# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '5/29/14'


from libs.apiclient import HTTPSAPIClient

HTTPSAPIClient.install_pem('/opt/ca/client.pem')
apicall = HTTPSAPIClient()
