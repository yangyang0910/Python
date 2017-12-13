# ATM + 购物车项目简介

## ATM项目具体功能
![ATM项目流程图](https://github.com/yangyang0910/Python/blob/master/%E6%A8%A1%E5%9D%97%E4%BA%8C/homework/ATMofCart/imgs/ATM.png?raw=true)

## Cart项目具体功能
![ATM项目流程图](https://github.com/yangyang0910/Python/blob/master/%E6%A8%A1%E5%9D%97%E4%BA%8C/homework/ATMofCart/imgs/Cart.png?raw=true)

## 日志
- error.log：记录错误日志
- Finance.log：记录金融方面的操作
- All.log：所有操作日志记录

## 登录功能
- 成功则记录session, 否则不作操作


## 账户信息表

- 用户表
```json
{
  "root" : {
    "userid" : "2015001",
    "username" : "root",
    "password" : "root",
    "balance": 5000,
    "status" : "0(正常)|1(冻结)|2(未知状态)"
  }
}
```

- 订单流水表
```json
{
  "123456789":{
    "userid" : "2015001",
    "operation" : "取现(0)|还款(1)|转账(2)",
    "money" : 500,
    "touser" : "root",
    "status" : "0(未成功)|1(成功)|2(未知错误)",
    "createtime" : "1452000000",
    "updatetime" : "1452000000"
  }
}
```