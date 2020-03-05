import okex.account_api as account
import okex.futures_api as future
import okex.lever_api as lever
import okex.spot_api as spot
import okex.swap_api as swap
import okex.index_api as index
import okex.option_api as option
import json
import logging
import datetime

log_format = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(filename='mylog-rest.json', filemode='a', format=log_format, level=logging.INFO)


def get_timestamp():
    now = datetime.datetime.now()
    t = now.isoformat("T", "milliseconds")
    return t + "Z"


time = get_timestamp()

if __name__ == '__main__':

    api_key = os.environ.get('api_key')
    secret_key = os.environ.get('secret_key')
    passphrase = os.environ.get('passphrase')

## swap api test
# 永续合约API
    swapAPI = swap.SwapAPI(api_key, secret_key, passphrase, False)
    # 所有合约持仓信息 （1次/10s）
    #result = swapAPI.get_position()
    # 单个合约持仓信息 （20次/2s）
    # result = swapAPI.get_specific_position('XRP-USD-SWAP')
    ## result = swapAPI.get_specific_position('BTC-USDT-SWAP')
    # 所有币种合约账户信息 （当用户没有持仓时，保证金率为10000）（1次/10s）
    # result = swapAPI.get_accounts()
    # 单个币种合约账户信息 （当用户没有持仓时，保证金率为10000）（20次/2s）
    # result = swapAPI.get_coin_account('LTC-USD-SWAP')
    # 获取某个合约的用户配置 （5次/2s）
    # result = swapAPI.get_settings('XRP-USD-SWAP')
    # 设定某个合约的杠杆 （5次/2s）
    # result = swapAPI.set_leverage('XRP-USD-SWAP', 10, 3)
    # 账单流水查询 （流水会分页，每页100条数据，并且按照时间倒序排序和存储，最新的排在最前面）（可查询最近7天的数据）（5次/2s）
    # result = swapAPI.get_ledger('BTC-USD-SWAP')
    # 下单 （40次/2s）
    result = swapAPI.take_order('BTC-USDT-SWAP', '1', '8795.0', '500', client_oid="", match_price='0')
    # 批量下单 （每个合约可批量下10个单）（20次/2s）
    # result = swapAPI.take_orders('XRP-USD-SWAP',  [
    #         {"client_oid": "a1211", "type": "1", "price": "0.1911", "size": "1"},
    #         {"client_oid": "b2323", "type": "1", "price": "0.1912", "size": "1"}
    #     ])
    # 撤单 （40次/2s）
    # result = swapAPI.revoke_order('XRP-USD-SWAP', '413371152692895744')
    # 批量撤单 （每个币对可批量撤10个单）（20次/2s）
    # result = swapAPI.revoke_orders('XRP-USD-SWAP', client_oids=['a1211', 'b2323'])
    # 获取所有订单列表 （可查询最近7天20000条数据，挂单可一直拿到，支持分页，分页返回结果最大为100条）（20次/2s）
    # result = swapAPI.get_order_list('XRP-USD-SWAP', '0')
    # 获取订单信息 （只能查询最近3个月的已成交和已撤销订单信息，已撤销的未成交单只保留2个小时）（40次/2s）
    # result = swapAPI.get_order_info('BTC-USD-SWAP', '2')
    # 获取成交明细 （能查询最近7天的数据）（20次/2s）
    # result = swapAPI.get_fills('XRP-USD-SWAP')
    # 获取合约挂单冻结数量 （5次/2s）
    # result = swapAPI.get_holds_amount('XRP-USD-SWAP')
    # 委托策略下单 （40次/2s）
    # result = swapAPI.take_order_algo('XRP-USD-SWAP', '1', '1', '1', trigger_price='0.2640', algo_price='0.2641')
    # 委托策略撤单 （每次最多可撤6（冰山/时间）/10（计划/跟踪）个）（20 次/2s）
    # result = swapAPI.cancel_algos('XRP-USD-SWAP', ['367645536490315776'], '1')
    # 获取委托单列表 （20次/2s）
    # result = swapAPI.get_order_algos('XRP-USD-SWAP', '1', algo_id='', status='2')
    # 获取账户手续费费率 （母账户下的子账户的费率和母账户一致。每天凌晨0点更新一次）（1次/10s）
    # result = swapAPI.get_trade_fee()
    # 公共-获取合约信息 （20次/2s）
    # result = swapAPI.get_instruments()
    # 公共-获取深度数据 （20次/2s）
    # result = swapAPI.get_depth('BTC-USD-SWAP', '30')
    # 公共-获取全部ticker信息 （20次/2s）
    # result = swapAPI.get_ticker()
    # 公共-获取某个ticker信息 （20次/2s）
    # result = swapAPI.get_specific_ticker('BTC-USD-SWAP')
    # 公共-获取成交数据 （能查询最近300条数据）（20次/2s）
    # result = swapAPI.get_trades('XRP-USD-SWAP')
    # 公共-获取K线数据 （最多可获取最近1440条）（20次/2s）
    # result = swapAPI.get_kline('BTC-USDT-SWAP', '1800')
    # print(len(result))
    # 公共-获取指数信息 （20次/2s）
    # result = swapAPI.get_index('BTC-USD-SWAP')
    # 公共-获取法币汇率 （20次/2s）
    # result = swapAPI.get_rate()
    # 公共-获取平台总持仓量 （20次/2s）
    # result = swapAPI.get_holds('XRP-USD-SWAP')
    # 公共-获取当前限价 （20次/2s）
    # result = swapAPI.get_limit('XRP-USD-SWAP')
    # 公共-获取强平单 （20次/2s）
    # result = swapAPI.get_liquidation('XRP-USD-SWAP', '1')
    # 公共-获取合约资金费率 （20次/2s）
    # result = swapAPI.get_funding_time('XRP-USD-SWAP')
    # 公共-获取合约标记价格 （20次/2s）
    # result = swapAPI.get_mark_price('XRP-USD-SWAP')
    # 公共-获取合约历史资金费率 （能查询最近7天的数据）（20次/2s）
    # result = swapAPI.get_historical_funding_rate('XRP-USD-SWAP')

    # print(time + json.dumps(result))
    # logging.info("result:" + json.dumps(result))

# index api test
# 指数API
    indexAPI = index.IndexAPI(api_key, secret_key, passphrase, False)
    # 公共-获取指数成分 （20次/2s）
    #result = indexAPI.get_index_constituents('BTC-USD')

    print(time + json.dumps(result))
    logging.info("result:" + json.dumps(result))
