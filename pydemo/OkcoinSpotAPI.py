#!/usr/bin/python
# -*- coding: utf-8 -*-
#用于访问OKCOIN 现货REST API
from __future__ import absolute_import
from HttpMD5Util import buildMySign,httpGet,httpPost

class OKCoinSpot(object):

    def __init__(self,url,apikey,secretkey):
        self.__url = url
        self.__apikey = apikey
        self.__secretkey = secretkey

    #获取OKCOIN现货行情信息
    def ticker(self,symbol = u''):
        TICKER_RESOURCE = u"/api/v1/ticker.do"
        params=u''
        if symbol:
            params = u'symbol=%(symbol)s' %{u'symbol':symbol}
        return httpGet(self.__url,TICKER_RESOURCE,params)

    #获取OKCOIN现货市场深度信息
    def depth(self,symbol = u''):
        DEPTH_RESOURCE = u"/api/v1/depth.do"
        params=u''
        if symbol:
            params = u'symbol=%(symbol)s' %{u'symbol':symbol}
        return httpGet(self.__url,DEPTH_RESOURCE,params) 

    #获取OKCOIN现货历史交易信息
    def trades(self,symbol = u''):
        TRADES_RESOURCE = u"/api/v1/trades.do"
        params=u''
        if symbol:
            params = u'symbol=%(symbol)s' %{u'symbol':symbol}
        return httpGet(self.__url,TRADES_RESOURCE,params)
    
    #获取用户现货账户信息
    def userinfo(self):
        USERINFO_RESOURCE = u"/api/v1/userinfo.do"
        params ={}
        params[u'api_key'] = self.__apikey
        params[u'sign'] = buildMySign(params,self.__secretkey)
        return httpPost(self.__url,USERINFO_RESOURCE,params)

    #现货交易
    def trade(self,symbol,tradeType,price=u'',amount=u''):
        TRADE_RESOURCE = u"/api/v1/trade.do"
        params = {
            u'api_key':self.__apikey,
            u'symbol':symbol,
            u'type':tradeType
        }
        if price:
            params[u'price'] = price
        if amount:
            params[u'amount'] = amount
            
        params[u'sign'] = buildMySign(params,self.__secretkey)
        return httpPost(self.__url,TRADE_RESOURCE,params)

    #现货批量下单
    def batchTrade(self,symbol,tradeType,orders_data):
        BATCH_TRADE_RESOURCE = u"/api/v1/batch_trade.do"
        params = {
            u'api_key':self.__apikey,
            u'symbol':symbol,
            u'type':tradeType,
            u'orders_data':orders_data
        }
        params[u'sign'] = buildMySign(params,self.__secretkey)
        return httpPost(self.__url,BATCH_TRADE_RESOURCE,params)

    #现货取消订单
    def cancelOrder(self,symbol,orderId):
        CANCEL_ORDER_RESOURCE = u"/api/v1/cancel_order.do"
        params = {
             u'api_key':self.__apikey,
             u'symbol':symbol,
             u'order_id':orderId
        }
        params[u'sign'] = buildMySign(params,self.__secretkey)
        return httpPost(self.__url,CANCEL_ORDER_RESOURCE,params)

    #现货订单信息查询
    def orderinfo(self,symbol,orderId):
         ORDER_INFO_RESOURCE = u"/api/v1/order_info.do"
         params = {
             u'api_key':self.__apikey,
             u'symbol':symbol,
             u'order_id':orderId
         }
         params[u'sign'] = buildMySign(params,self.__secretkey)
         return httpPost(self.__url,ORDER_INFO_RESOURCE,params)

    #现货批量订单信息查询
    def ordersinfo(self,symbol,orderId,tradeType):
         ORDERS_INFO_RESOURCE = u"/api/v1/orders_info.do"
         params = {
             u'api_key':self.__apikey,
             u'symbol':symbol,
             u'order_id':orderId,
             u'type':tradeType
         }
         params[u'sign'] = buildMySign(params,self.__secretkey)
         return httpPost(self.__url,ORDERS_INFO_RESOURCE,params)

    #现货获得历史订单信息
    def orderHistory(self,symbol,status,currentPage,pageLength):
           ORDER_HISTORY_RESOURCE = u"/api/v1/order_history.do"
           params = {
              u'api_key':self.__apikey,
              u'symbol':symbol,
              u'status':status,
              u'current_page':currentPage,
              u'page_length':pageLength
           }
           params[u'sign'] = buildMySign(params,self.__secretkey)
           return httpPost(self.__url,ORDER_HISTORY_RESOURCE,params)















    
