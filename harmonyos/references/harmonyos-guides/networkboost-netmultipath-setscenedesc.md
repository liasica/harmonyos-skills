---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-netmultipath-setscenedesc
title: 业务场景设置
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > 连接迁移（多网并发） > 业务场景设置
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:afd6e7e1dfcc552ba584428534f15a02efb34f2760dc4be5b73710d3a3e3a4d3
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

   ```typescript
   import { netBoost } from '@kit.NetworkBoostKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 设置业务场景。

   ```typescript
   try {
     let sceneDesc : netBoost.SceneDesc = {
       // scene: 'realtimeVoice' 表示实时语音业务场景，可通过业务需求配置; sceneEvent: SCENE_EVENT_ENTER 表示进入场景事件
       scene : 'realtimeVoice',
       sceneEvent : netBoost.SceneEvent.SCENE_EVENT_ENTER
     }
     netBoost.setSceneDesc(sceneDesc);
   } catch (err) {
     console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   }
   ```
