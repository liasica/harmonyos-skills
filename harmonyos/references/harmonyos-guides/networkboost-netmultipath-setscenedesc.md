---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-netmultipath-setscenedesc
title: 业务场景设置
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > 连接迁移（多网并发） > 业务场景设置
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e4b3c370b2f3f70ddf414cb032bef55fdda3741d641a0337c49a96f3bd4c7ff2
---

## 场景介绍

应用在请求多网并发之前，通过设置业务场景，可以帮助系统进行多网并发管控和业务时长分析。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/networkboost-netboost.md#netboostsetscenedesc)。

| 接口名 | 描述 |
| --- | --- |
| setSceneDesc(sceneDesc : SceneDesc): void | 设置业务场景。 |

## 开发步骤

1. 导入Network Boost Kit模块。

   ```
   1. import { netBoost } from '@kit.NetworkBoostKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 设置业务场景。

   ```
   1. try {
   2. let sceneDesc : netBoost.SceneDesc = {
   3. scene : 'realtimeVoice',
   4. sceneEvent : netBoost.SceneEvent.SCENE_EVENT_ENTER
   5. }
   6. netBoost.setSceneDesc(sceneDesc);
   7. } catch (err) {
   8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   9. }
   ```
