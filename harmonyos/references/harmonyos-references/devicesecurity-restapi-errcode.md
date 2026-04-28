---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-restapi-errcode
title: REST API错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:07:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:14df4610cfb731e51cb80b89452388d9d41fc270ebd99aeb3b30e0dd7274710b
---

说明

以下仅介绍云服务特有错误码及原因分析。

## InvalidBundleName

**错误信息**

```
1. {
2. "errorCodes": "InvalidBundleName"
3. }
```

**错误描述**

bundleName缺失或不合法。

**可能原因**

1、请求header中缺少bundleName。

2、请求header中的bundleName和调用getDeviceToken接口应用的bundleName不一致。

**处理步骤**

1、检查请求header中是否携带了bundleName。

2、需要开发者自行检查header和getDeviceToken接口应用的bundleName是否一致。

## InvalidDeviceToken

**错误信息**

```
1. {
2. "errorCodes": "InvalidDeviceToken"
3. }
```

**错误描述**

deviceToken缺失或不合法。

**可能原因**

请求参数中deviceToken字段缺失或者传特殊字符。

**处理步骤**

检查请求参数中deviceToken字段是否缺失或者传参中是否存在特殊字符。

## DeviceTokenExpired

**错误信息**

```
1. {
2. "errorCodes": "DeviceTokenExpired"
3. }
```

**错误描述**

deviceToken过期。

**可能原因**

请求参数中deviceToken已过期。

**处理步骤**

deviceToken有效期为1小时，重新生成token后尝试即可。

## InvalidTimeStamp

**错误信息**

```
1. {
2. "errorCodes": "InvalidTimeStamp"
3. }
```

**错误描述**

timeStamp缺失或不合法。

**可能原因**

请求参数中timeStamp字段缺失或者参数非法（非long型字段）。

**处理步骤**

检查请求参数中timeStamp字段是否缺失或者传参中是否合法。

## NotFound

**错误信息**

```
1. {
2. "errorCodes": "NotFound"
3. }
```

**错误描述**

未找到设备的标记记录（设备身份验证成功，该设备未被标记过）。

**可能原因**

标记在服务侧不存在。

**处理步骤**

1、先调用更新标记后再次查询该标记即可。

2、切换mode枚举后再尝试（枚举是1或2）。

## InvalidMode

**错误信息**

```
1. {
2. "errorCodes": "InvalidMode"
3. }
```

**错误描述**

mode不合法。

**可能原因**

请求参数中mode字段枚举不正确，具体枚举查看接口字段枚举详情。

**处理步骤**

检查请求参数中mode字段枚举是否正确，是否与接口规定符合。

## InvalidBits

**错误信息**

```
1. {
2. "errorCodes": "InvalidBits"
3. }
```

**错误描述**

bit值缺失或不合法。

**可能原因**

请求参数中bit字段缺失或者传参非Boolean类型。

**处理步骤**

检查请求参数中bit字段是否缺失且传参类型是否是Boolean（true OR false）。

## InternalServerError

**错误信息**

```
1. {
2. "errorCodes": "InternalServerError"
3. }
```

**错误描述**

服务器内部错误。

**可能原因**

服务器内部处理异常。

**处理步骤**

如果您出现服务器内部错误码，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)申请帮助。
