---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-fetch
title: @system.fetch (数据请求)
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > 已停止维护的接口 > @system.fetch (数据请求)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d0723ef4c5a93cbe5561cffa56c6fd8be7a656b1ff67067136502879e2714f46
---

说明

* 从API Version 6开始，该接口不再维护，推荐使用新接口[@ohos.net.http](js-apis-http.md)。
* 本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import fetch from '@system.fetch';
```

## fetch.fetch3+

PhonePC/2in1TabletTVWearable

fetch(options:{

url: string;

data?: string | object;

header?: Object;

method?: string;

responseType?: string;

success?: (data: FetchResponse) => void;

fail?: (data: any, code: number) => void;

complete?: () => void;

} ): void

通过网络获取数据。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 资源地址。 |
| data | string | Object | 否 | 请求的参数，可选类型是字符串或者json对象。详见表 data与Content-Type关系。 |
| header | Object | 否 | 设置请求的header。 |
| method | string | 否 | 请求方法默认为GET，可选值为：OPTIONS、GET、HEAD、POST、PUT、DELETE、TRACE。 |
| responseType | string | 否 | 默认会根据服务器返回header中的Content-Type确定返回类型，支持文本和json格式。详见success返回值。 |
| success | Function | 否 | 接口调用成功的回调函数，返回值为[FetchResponse](js-apis-system-fetch.md#fetchresponse3)。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

**表1** data与Content-Type关系

| data | Content-Type | 说明 |
| --- | --- | --- |
| string | 不设置 | Content-Type默认为 text/plain，data值作为请求的body。 |
| string | 任意 Type | data值作为请求的body。 |
| Object | 不设置 | Content-Type默认为application/x-www-form-urlencoded，data按照资源地址规则进行encode拼接作为请求的body。 |
| Object | application/x-www-form-urlencoded | data按照资源地址规则进行encode拼接作为请求的body。 |

## FetchResponse3+

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 否 | 表示服务器的状态code。 |
| data | string | Object | 否 | 否 | 返回数据类型由responseType确定，详见表 responseType与success中data关系。 |
| headers | Object | 否 | 否 | 表示服务器response的所有header。 |

**表2** responseType与success中data关系

| responseType | data | 说明 |
| --- | --- | --- |
| 无 | string | 服务器返回的header中的type如果是text/\*或application/json、application/javascript、application/xml，值为文本内容。 |
| text | string | 返回文本内容。 |
| json | Object | 返回json格式的对象。 |

**示例：**

```
1. export default {
2. data: {
3. responseData: 'NA',
4. url: "test_url",
5. },
6. fetch: function () {
7. var that = this;
8. fetch.fetch({
9. url: that.url,
10. success: function(response) {
11. console.info("fetch success");
12. that.responseData = JSON.stringify(response);
13. },
14. fail: function() {
15. console.info("fetch fail");
16. }
17. });
18. }
19. }
```

说明

默认支持https，如果要支持http，需要在config.json里增加network标签，属性标识 "cleartextTraffic": true。即：

```
1. {
2. "deviceConfig": {
3. "default": {
4. "network": {
5. "cleartextTraffic": true
6. }
7. ... // 用户的其它配置信息
8. }
9. }
10. ... // 用户的其它配置信息
11. }
```
