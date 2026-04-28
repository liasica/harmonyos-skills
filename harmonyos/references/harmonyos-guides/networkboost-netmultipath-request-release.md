---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-netmultipath-request-release
title: 多网发起和释放
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > 连接迁移（多网并发） > 多网发起和释放
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dc9219bf6b65f5c085c19e0d255ea02362c156469d82ead7fa35f0502d137266
---

## 场景介绍

应用可根据自身业务的需要，以及系统的建议来发起多网络加速的请求，并在使用结束后及时释放。支持WiFi和蜂窝并发以及主卡和副卡并发，不支持开发者指定并发组合，并发组合由系统决定。

说明

* 主卡和副卡并发需要开启智能切换上网卡开关，并依赖主卡和副卡驻留网络的频点，若不满足并发条件（例如主副卡插入同运营商卡场景），多网发起会失败。
* 受限于硬件，部分设备不支持双卡场景下的多网并发，开发者可通过错误码进行排查。
* 如果要使用的传输协议接口不支持指定网络，则新发起的网络无法使用。如[HTTP](http-request.md)当前只支持默认网络传输，不支持指定网络，所以无法使用。

## 开发前准备

多网发起需要开启网络加速开关，操作路径为：设置->移动网络->网络加速->允许使用移动数据加速网络，如果没有该开关，说明您当前的设备/ROM不支持多网并发能力。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/networkboost-nethandover.md#nethandoverrequestmultipath)。

| 接口名 | 描述 |
| --- | --- |
| requestMultiPath(callback: Callback<MultiPathRequestResult>): void | 发起多网请求。 |
| releaseMultiPath(): void | 释放多网。 |

## 开发步骤

1. 导入Network Boost Kit模块。

   ```
   1. import { netHandover } from '@kit.NetworkBoostKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 发起多网请求，同步监听多网状态可以获取多网的状态信息。

   ```
   1. try {
   2. netHandover.requestMultiPath((data: netHandover.MultiPathRequestResult) => {
   3. console.info(` requestMultiPath result:` + JSON.stringify(data));
   4. });
   5. } catch (err) {
   6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   7. }
   ```
3. 当应用业务流程结束，通过releaseMultiPath接口释放多网。

   ```
   1. try {
   2. netHandover.releaseMultiPath();
   3. } catch (err) {
   4. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   5. }
   ```
