#!/usr/bin/python
# -*- coding: utf-8 -*-
#用于访问OKCOIN 期货REST API
from __future__ import absolute_import
from HttpMD5Util import buildMySign,httpGet,httpPost

class OKCoinFuture(object):

    def __init__(self,url,apikey,secretkey):
        self.__url = url
        self.__apikey = apikey
        self.__secretkey = secretkey

    #OKCOIN期货行情信息
    def future_ticker(self,symbol,contractType):
        FUTURE_TICKER_RESOURCE = u"/api/v1/future_ticker.do"
        params = u''
        if symbol:
            params += u'&symbol=' + symbol if params else u'symbol=' +symbol
        if contractType:
            params += u'&contract_type=' + contractType if params else u'contract_type=' +symbol
        return httpGet(self.__url,FUTURE_TICKER_RESOURCE,params)

    #OKCoin期货市场深度信息
    def future_depth(self,symbol,contractType,size): 
        FUTURE_DEPTH_RESOURCE = u"/api/v1/future_depth.do"
        params = u''
        if symbol:
            params += u'&symbol=' + symbol if params else u'symbol=' +symbol
        if contractType:
            params += u'&contract_type=' + contractType if params else u'contract_type=' +symbol
        if size:
            params += u'&size=' + size if params else u'size=' + size
        return httpGet(self.__url,FUTURE_DEPTH_RESOURCE,params)

    #OKCoin期货交易记录信息
    def future_trades(self,symbol,contractType):
        FUTURE_TRADES_RESOURCE = u"/api/v1/future_trades.do"
        params = u''
        if symbol:
            params += u'&symbol=' + symbol if params else u'symbol=' +symbol
        if contractType:
            params += u'&contract_type=' + contractType if params else u'contract_type=' +symbol
        return httpGet(self.__url,FUTURE_TRADES_RESOURCE,params)

    #OKCoin期货指数
    def future_index(self,symbol):
        FUTURE_INDEX = u"/api/v1/future_index.do"
        params=u''
        if symbol:
            params = u'symbol=' +symbol
        return httpGet(self.__url,FUTURE_INDEX,params)

    #获取美元人民币汇率
    def exchange_rate(self):
        EXCHANGE_RATE = u"/api/v1/exchange_rate.do"
        return httpGet(self.__url,EXCHANGE_RATE,u'')

    #获取预估交割价
    def future_estimated_price(self,symbol):
        FUTURE_ESTIMATED_PRICE = u"/api/v1/future_estimated_price.do"
        params=u''
        if symbol:
            params = u'symbol=' +symbol
        return httpGet(self.__url,FUTURE_ESTIMATED_PRICE,params)

    #期货全仓账户信息
    def future_userinfo(self):
        FUTURE_USERINFO = u"/api/v1/future_userinfo.do?"
        params ={}
        params[u'api_key'] = self.__apikey
        params[u'sign'] = buildMySign(params,self.__secretkey)
        return httpPost(self.__url,FUTURE_USERINFO,params)

    #期货全仓持仓信息
    def future_position(self,symbol,contractType):
        FUTURE_POSITION = u"/api/v1/future_position.do?"
        params = {
            u'api_key':self.__apikey,
            u'symbol':symbol,
            u'contract_type':contractType
        }
        params[u'sign'] = buildMySign(params,self.__secretkey)
        return httpPost(self.__url,FUTURE_POSITION,params)

    #期货下单
    def future_trade(self,symbol,contractType,price=u'',amount=u'',tradeType=u'',matchPrice=u'',leverRate=u''):
        FUTURE_TRADE = u"/api/v1/future_trade.do?"
        params = {
            u'api_key':self.__apikey,
            u'symbol':symbol,
            u'contract_type':contractType,
            u'amount':amount,
            u'type':tradeType,
            u'match_price':matchPrice,
            u'lever_rate':leverRate
        }
        if price:
            params[u'price'] = price
        params[u'sign'] = buildMySign(params,self.__secretkey)
        return httpPost(self.__url,FUTURE_TRADE,params)

    #期货批量下单
    def future_batchTrade(self,symbol,contractType,orders_data,leverRate):
        FUTURE_BATCH_TRADE = u"/api/v1/future_batch_trade.do?"
        params = {
            u'api_key':self.__apikey,
            u'symbol':symbol,
            u'contract_type':contractType,
            u'orders_data':orders_data,
            u'lever_rate':leverRate
        }
        params[u'sign'] = buildMySign(params,self.__secretkey)
        return httpPost(self.__url,FUTURE_BATCH_TRADE,params)

    #期货取消订单
    def future_cancel(self,symbol,contractType,orderId):
        FUTURE_CANCEL = u"/api/v1/future_cancel.do?"
        params = {
            u'api_key':self.__apikey,
            u'symbol':symbol,
            u'contract_type':contractType,
            u'order_id':orderId
        }
        params[u'sign'] = buildMySign(params,self.__secretkey)
        return httpPost(self.__url,FUTURE_CANCEL,params)

    #期货获取订单信息
    def future_orderinfo(self,symbol,contractType,orderId,status,currentPage,pageLength):
        FUTURE_ORDERINFO = u"/api/v1/future_order_info.do?"
        params = {
            u'api_key':self.__apikey,
            u'symbol':symbol,
            u'contract_type':contractType,
            u'order_id':orderId,
            u'status':status,
            u'current_page':currentPage,
            u'page_length':pageLength
        }
        params[u'sign'] = buildMySign(params,self.__secretkey)
        return httpPost(self.__url,FUTURE_ORDERINFO,params)

    #期货逐仓账户信息
    def future_userinfo_4fix(self):
        FUTURE_INFO_4FIX = u"/api/v1/future_userinfo_4fix.do?"
        params = {u'api_key':self.__apikey}
        params[u'sign'] = buildMySign(params,self.__secretkey)
        return httpPost(self.__url,FUTURE_INFO_4FIX,params)

    #期货逐仓持仓信息
    def future_position_4fix(self,symbol,contractType,type1):
        FUTURE_POSITION_4FIX = u"/api/v1/future_position_4fix.do?"
        params = {
            u'api_key':self.__apikey,
            u'symbol':symbol,
            u'contract_type':contractType,
            u'type':type1
        }
        params[u'sign'] = buildMySign(params,self.__secretkey)
        return httpPost(self.__url,FUTURE_POSITION_4FIX,params)







    
