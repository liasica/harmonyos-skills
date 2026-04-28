---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-reporthandovermode
title: 迁移模式设置
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > 连接迁移（多网切换） > 迁移模式设置
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f553934b59a8108f409452ac4d5b5a09a64ffaf042118338479a7c6e460d4f8a
---

## 场景介绍

应用可通过该接口变更连接迁移模式，包括委托模式由系统发起连接迁移，和自主模式由应用发起连接迁移。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/networkboost-nethandover.md#nethandoversethandovermode)。

| 接口名 | 描述 |
| --- | --- |
| setHandoverMode(mode: HandoverMode): void | 应用设置迁移模式，默认为委托模式。 |

## 开发步骤

1. 导入Network Boost Kit模块。

   ```
   1. import { netHandover} from '@kit.NetworkBoostKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用setHandoverMode接口，设置为自主模式，禁止系统发起连接迁移。

   ```
   1. try{
   2. let mode: netHandover.HandoverMode = netHandover.HandoverMode.DISCRETION;
   3. netHandover.setHandoverMode(mode);
   4. } catch (err) {
   5. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   6. }
   ```
