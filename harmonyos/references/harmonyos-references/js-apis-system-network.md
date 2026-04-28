---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-network
title: @system.network (网络状态)
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > 已停止维护的接口 > @system.network (网络状态)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:42+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:92ee584756272853d6daa93aa53963037e07fef43b111aed365bf999ed822f8d
---

说明

* 本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 从API Version 8 开始，该接口不再维护，推荐使用新接口['@ohos.net.connection'](js-apis-net-connection.md)。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import network from '@system.network';
```

## 权限列表

PhonePC/2in1TabletTVWearable

ohos.permission.GET\_WIFI\_INFO

ohos.permission.GET\_NETWORK\_INFO

## network.getType3+

PhonePC/2in1TabletTVWearable

getType(options?: {

success?: (data: NetworkResponse) => void;

fail?: (data: any, code: number) => void;

complete?: () => void;

}): void

获取当前设备的网络类型。

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | Function | 否 | 接口调用成功的回调函数，返回值为[NetworkResponse](js-apis-system-network.md#networkresponse3)。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

fail返回值：

| 错误码 | 说明 |
| --- | --- |
| 602 | 当前权限未声明。 |

**示例：**

```
1. export default class Network {
2. getType() {
3. network.getType({
4. success: (data) => {
5. console.info('success get network type:' + data.type);
6. }
7. });
8. }
9. }
```

## network.subscribe3+

PhonePC/2in1TabletTVWearable

subscribe(options?:{

success?: (data: NetworkResponse) => void;

fail?: (data: any, code: number) => void;

}): void

订阅当前设备的网络连接状态。如果多次调用，会覆盖前一次调用。

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | Function | 否 | 网络发生变化的回调函数。返回值为[NetworkResponse](js-apis-system-network.md#networkresponse3)。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |

fail返回值：

| 错误码 | 说明 |
| --- | --- |
| 602 | 当前权限未声明。 |
| 200 | 订阅失败。 |

**示例：**

```
1. export default class Network {
2. subscribe() {
3. network.subscribe({
4. success: (data) => {
5. console.info('success get network type:' + data.type);
6. }
7. });
8. }
9. }
```

## network.unsubscribe3+

PhonePC/2in1TabletTVWearable

unsubscribe(): void

取消订阅设备的网络连接状态。

**系统能力：** SystemCapability.Communication.NetManager.Core

**示例：**

```
1. import network from '@system.network';

3. network.unsubscribe();
```

## NetworkResponse3+

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Communication.NetManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| metered | boolean | 否 | 是 | 是否按照流量计费。true：按照流量计费；false：不按照流量计费。 |
| type | string | 否 | 否 | 网络类型，可能的值有2g，3g，4g，5g，wifi，none等。 |
