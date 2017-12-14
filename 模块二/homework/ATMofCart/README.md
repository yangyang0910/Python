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
- 退出登录删除session


## 账户信息表

- 用户表
```json
{
  "root" : {
    "userid" : "2015001",
    "username" : "root",
    "password" : "root",
    "balance": 5000,
    "status" : "0(正常)|1(冻结)|2(未知状态)",
    "userstatus" : "0(正常)|1(软删除)",
    "loginstatus" : "0(正在登录)|1(下线)",
    "jurisdiction" : "0(超级权限)|1(高级权限)|2(初级权限)"
  }
}
```

- 用户状态表
```json
{
  "root":{
    "status" : "sessiodId"
  }
}
```

- 订单流水表
```json
{
  "123456789":{
    "userid" : "2015001", // 用户ID
    "operation" : "取现(0)|还款(1)|转账(2)", // 操作方式
    "money" : 500,  // 操作金额
    "touser" : "root", // 操作对象
    "status" : "0(操作中)|1(成功)|2(未知错误)", // 操作状态
    "createdtime" : "1452000000", // 创建时间
    "updatedtime" : "1452000000"  // 修改时间
    "deletedtime" : "1452000000"  // 删除时间
  }
}
```


- sessionId表
```json
{
  "username" : "sessionID", 
  "root" : "a371f8775da8d33ada110c2af75a351d782f9da5" 
}
```


- session记录表
```json
{
  "12f95bb180732f456147270c869934adcd16797d": 
  {
    "user": "admin", // 用户名
    "expiryTime": 3600, // 过期时间
    "expiry": true, // 是否过期
    "createTime": 1513154308.3949254 // session创建时间
  }
}

```

- cookie 记录
```json
{
    "cookie": "cookieId", 
    "sessionid": "sessionId", 
    "times": 3600, // 有效期 
    "status": "true|flase", // 状态
    "createtime": 1513167260.2514932 // 创建时间
}
```