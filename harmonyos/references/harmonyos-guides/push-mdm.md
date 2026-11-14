---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-mdm
title: 推送MDM消息
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > 推送场景化消息 > 推送MDM消息
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:29+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:5bb2c3ed760756e8c46db8040b069f6fc4ed433b5e775675bd81c8adbfac6630
---

从API版本26.0.1开始，推送服务新增支持推送MDM消息能力。

## 场景介绍

MDM（Mobile Device Management）消息用于设备管理场景，支持向终端设备下发管理指令。MDM应用在后台时仍能接收MDM消息，可以确保设备管理员或企业IT部门在任何情况下都能及时下发/收到携带指令的MDM消息，比如设备异常、安全策略更新或远程操作指令。

## 约束与限制

推送MDM消息能力支持Phone、Tablet、PC/2in1。

## 开通权益

推送MDM消息需要申请推送MDM消息权益，请参见[申请推送MDM消息权益](push-apply-right.md#申请推送mdm消息权益)。

## 频控规则

**调测阶段**，每个项目每日全网最多可推送1000条测试消息。发送测试消息需设置[testMessage](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)为true。

**正式发布阶段**，单设备单应用下每日推送消息总条数受[设备消息频控](../harmonyos-references/push-msg-freq-control.md#设备消息频控)限制，系统会根据使用场景和流量进行管控，不合理的使用场景系统会进行频控。

## 开发步骤

1. 参见指导[获取Push Token](push-get-token.md)，使用token推送MDM消息。
2. 在项目中现有的UIAbility类（以PushMessageAbility为例）的onCreate中，调用[receiveMessage](../harmonyos-references/push-pushservice.md#pushservicereceivemessage)方法接收MDM消息。MDM消息与后台消息共用同一个回调入口，类型参数均为'BACKGROUND'；当data.type为'MDM'时，该消息即为MDM消息。仅能使用UIAbility接收MDM消息。

   ```typescript
   import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   import { pushCommon, pushService } from '@kit.PushKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   // ...

   const DOMAIN = 0x0000;

   export default class PushMessageAbility extends UIAbility {
     onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
     // ...
       try {
         pushService.receiveMessage('BACKGROUND', this, (data: pushCommon.PushPayload) => {
           // process message
           try {
             if (data.type === 'MDM') {
               hilog.info(DOMAIN, 'testTag', 'Receive MDM message : %{public}s', JSON.stringify(data));
               // 处理MDM消息
               // ...
             }
           } catch (e) {
             let errRes: BusinessError = e as BusinessError;
             hilog.error(DOMAIN, 'testTag', 'Failed to process data: %{public}d %{public}s', errRes.code, errRes.message);
           }
         });
       } catch (err) {
         let e: BusinessError = err as BusinessError;
         hilog.error(DOMAIN, 'testTag', 'Failed to get background message: %{public}d %{public}s', e.code, e.message);
       }
       // ...
     }
   }
   ```
3. 在项目工程src/main/module.json5文件的abilities模块**skills**标签中配置**actions**内容为**action.ohos.push.listener**（有且只能有一个ability定义该action，**若同时添加uris参数，则uris内容需为空**）。

   ```json5
   {
     "name": "PushMessageAbility",
     "srcEntry": "./ets/abilities/PushMessageAbility.ets",
     "description": "$string:PushMessageAbility_desc",
     "icon": "$media:layered_image",
     "label": "$string:PushMessageAbility_label",
     "startWindowIcon": "$media:startIcon",
     "startWindowBackground": "$color:start_window_background",
     "launchType": "singleton",
     "exported": false,
     "skills": [
       // 保持现有skill对象不变
       {
         "actions": [
           "com.app.action"
         ]
       },
       // 新增一个独立的skill对象，配置actions参数
       {
         "actions": [
           "action.ohos.push.listener"
         ]
       }
     ]
     // ...
   }
   ```
4. 应用服务端调用REST API推送MDM消息，消息详情可参见[场景化消息API接口功能介绍](../harmonyos-references/push-scenariozed-api-intro.md)，请求示例如下。

   ```json5
   // Request URL
   POST "https://push-api.cloud.huawei.com/v3/[projectId]/messages:send"

   // Request Header
   Content-Type: application/json
   Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
   push-type: 11

   // Request Body
   {
     "payload": {
       "data": "携带的MDM管理指令数据"
     },
     "target": {
       "token": ["MAMzLg**********lPW"]
     }
   }
   ```

   * [projectId]：项目ID，登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”，在该页面获取。
   * Authorization：JWT格式字符串，可参见[Authorization](../harmonyos-references/push-scenariozed-api-request-struct.md#request-header)获取。
   * push-type：11表示MDM消息场景。
   * token：Push Token，可参见[获取Push Token](push-get-token.md)获取。
   * data：携带的MDM管理指令数据，字符串类型。详情请参见[data](../harmonyos-references/push-scenariozed-api-request-param.md#mdmpayload-mdm消息)。

   消息下发后会直接拉起应用并将数据传递，您可以在[receiveMessage](../harmonyos-references/push-pushservice.md#pushservicereceivemessage)()方法中获取消息数据。
