---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-send-extend-noti
title: 发送语音播报消息
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > 推送场景化消息 > 推送语音播报消息 > 发送语音播报消息
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:00+08:00
doc_updated_at: 2026-08-03
content_hash: sha256:9ab5d309ddc08706a60da6665978e51d05d0510b13a67f1d196432294d57e8ba
---

## 场景介绍

当用户终端收到您发送的语音播报消息时：

* 若您的应用进程不在前台，应用会拉起子进程，名为通知扩展进程，Push Kit会将消息内容传递给通知扩展进程，您可以在该进程中自行完成业务处理后，返回自定义消息内容，Push Kit将弹出通知提醒。您需要在10秒内返回消息内容，否则Push Kit将默认展示原有的消息内容。
* 若您的应用进程在前台，则不弹出通知提醒，您可以在应用进程中获取语音播报消息内容并自行完成业务处理。

## 约束与限制

推送语音播报消息能力支持Phone、Tablet、PC/2in1。并且从5.1.0(18)版本开始，新增支持Wearable设备；从6.1.0(23)版本开始，新增支持TV设备。

## 开通权益

推送语音播报消息需要申请推送语音播报消息权益，请参见[申请推送语音播报消息权益](push-apply-right.md#申请推送语音播报消息权益)。

## 频控规则

**调测阶段**，每个项目每日全网最多可推送1000条测试消息。发送测试消息需设置[testMessage](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)为true。

**正式发布阶段**，单设备单应用下每日推送消息总条数受[设备消息频控](../harmonyos-references/push-msg-freq-control.md#设备消息频控)限制，系统会根据使用场景和流量进行管控，不合理的使用场景系统会进行频控。

## 开发步骤

1. 参见指导[获取Push Token](push-get-token.md)。
2. 为确保应用可正常收到消息，建议应用发送通知前调用[requestEnableNotification](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagerrequestenablenotification10-1)()方法弹出提醒，告知用户需要允许接收通知消息。详情请参见Notification Kit-[请求通知授权](notification-enable.md)。
3. 应用服务端调用REST API推送消息，消息详情可参见[场景化消息API接口功能介绍](../harmonyos-references/push-scenariozed-api-intro.md)，请求示例如下：

   ```json5
   // Request URL
   POST "https://push-api.cloud.huawei.com/v3/[projectId]/messages:send"
    
   // Request Header
   Content-Type: application/json
   Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
   push-type: 2

   // Request Body
   {
     "payload": {
       "extraData": "{\"title\":\"replace title\",\"text\":\"replace text\"}",
       "notification": {
         "category": "PLAY_VOICE",
         "title": "通知标题",
         "body": "通知内容",
         "image":"https://lf*******246.png",
         "clickAction": {
           "actionType": 0
         },
         "notifyId": 12345
       }
     },
     "target": {
       "token": ["MAMzLg**********lPW"]
     },
     "pushOptions": {
       "testMessage": true,
       "ttl": 86400
     }
   }
   ```

   * [projectId]：项目ID，登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”，在该页面获取。
   * Authorization：JWT格式字符串，可参见[Authorization](../harmonyos-references/push-scenariozed-api-request-struct.md#request-header)获取。
   * push-type：2，表示语音播报场景。
   * category：消息自分类类别，当前支持设置为PLAY\_VOICE。
   * actionType：0表示点击消息打开应用首页。
   * token：Push Token，可参见[获取Push Token](push-get-token.md)获取。
   * extraData：语音播报场景可携带的额外数据，字符串类型。详情参见[ExtensionPayload 语音播报消息](../harmonyos-references/push-scenariozed-api-request-param.md#extensionpayload-语音播报消息)。extraData数据获取请参考[示例代码](https://gitcode.com/HarmonyOS_Samples/push-kit-sample-code-clientdemo-arkts/blob/master/entry/src/main/ets/abilities/PushMessageAbility.ets)。
   * testMessage：（选填）测试消息标识，true表示测试消息。每个项目每天限制发送1000条测试消息，单次推送可发送Token数不超过10个。详情请参见[testMessage](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)。
   * ttl：（选填）消息缓存时间，详见[ttl](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)。
   * notifyId：（选填）自定义消息标识字段。不携带或者设置-1时，Push Kit自动为每条消息生成一个唯一标识；不同的通知消息可以拥有相同的notifyId，实现新消息覆盖旧消息功能。仅支持数字，范围 [0, 2147483647]，若要**用于消息撤回则必填**。详情请参见[notifyId](../harmonyos-references/push-scenariozed-api-request-param.md#notification)。
   * image：（选填）通知右侧大图标URL，URL使用的协议必须是HTTPS协议。

   **说明** 

   Push Kit禁止推送包含敏感信息的图片。
4. 应用服务端调用REST API推送消息后，若应用进程在后台，Push Kit会将通知消息内容传递给通知扩展进程，并返回特定的消息内容（例如title、body等）后，通知栏将弹出通知提醒。实现步骤如下：

   在项目工程的**src/main/module.json5**文件的**extensionAbilities**模块中配置RemoteNotificationExtAbility的**type**和**actions**信息（**定义该type和actions的ExtensionAbility有且只能有一个，配置如下，若同时添加uris参数，则uris内容需为空**）：

   ```json5
   "extensionAbilities": [
     // ...
     {
       "name": "RemoteNotificationExtAbility",
       "type": "remoteNotification",
       "srcEntry": "./ets/entryability/RemoteNotificationExtAbility.ets",
       "description": "RemoteNotificationExtAbility test",
       "exported": false,
       "skills": [
         // 新增一个独立的skill对象，配置actions参数
         {
           "actions": [
             "action.hms.push.extension.remotenotification"
           ]
         }
       ]
     }
     // ...
   ]
   ```

   * type：固定值为**remoteNotification**，表示通知扩展的ExtensionAbility类型。
   * actions：固定值为**action.hms.push.extension.remotenotification**，用于接收语音播报消息。

   在您的工程内创建一个ExtensionAbility类型的组件并且继承[RemoteNotificationExtensionAbility](../harmonyos-references/push-remote-notification-extension-ability.md)，完成[onReceiveMessage](../harmonyos-references/push-remote-notification-extension-ability.md#onreceivemessage)()方法的覆写，在此方法中进行数据接收及业务处理。代码示例如下：

   ```typescript
   import { pushCommon, RemoteNotificationExtensionAbility } from '@kit.PushKit';
   import { image } from '@kit.ImageKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { resourceManager } from '@kit.LocalizationKit';
   import { common } from '@kit.AbilityKit';

   const DOMAIN = 0x0000;

   export default class RemoteNotificationExtAbility extends RemoteNotificationExtensionAbility {
     async onReceiveMessage(): Promise<pushCommon.RemoteNotificationContent> {
       hilog.info(DOMAIN, 'testTag', 'RemoteNotificationExtAbility onReceiveMessage, remoteNotificationInfo');

       // 通过图片解码参数创建PixelMap对象
       const resourceMgr: resourceManager.ResourceManager = (this.context as common.UIExtensionContext).resourceManager;
       let fileData: Uint8Array = new Uint8Array(0);
       try {
         fileData = await resourceMgr.getMediaContent($r('app.media.startIcon').id);
       } catch (e) {
         hilog.error(DOMAIN, 'testTag', 'Failed to get media content: %{public}d %{public}s', e.code, e.message);
       }
       const buffer = fileData.buffer;
       const imageSource: image.ImageSource = image.createImageSource(buffer as ArrayBuffer);
       const pixelMap: image.PixelMap = await imageSource.createPixelMap();
       if (pixelMap) {
         pixelMap.getImageInfo((err, imageInfo) => {
           if (imageInfo) {
             hilog.info(DOMAIN, 'testTag', `imageInfo ${imageInfo.size.width} * ${imageInfo.size.height}`);
           } else {
             hilog.error(DOMAIN, 'testTag', `Failed to obtain the image information.code is ${err.code}, message is ${err.message}`);
           }
         });
       }

       // 应用自行实现语音播报的逻辑
       this.textToSpeech();

       // 扩展消息实际展示内容
       return {
         title: 'Default replace title.',
         text: 'Default replace text.',
         badgeNumber: 1,
         setBadgeNumber: 2,
         overlayIcon: pixelMap,
         wantAgent: {
           abilityName: 'DemoAbility',
           parameters: {
             key: 'Default value'
           }
         }
       }
     }

     textToSpeech(): void {
       // 实现语音播报的逻辑
     }

     onDestroy(): void {
       hilog.info(DOMAIN, 'testTag', 'RemoteNotificationExtAbility onDestroy.');
     }
   }
   ```

   * 函数的返回值用于替换最终展示在终端的通知，title和text代表您要展示的通知标题与通知内容。
   * badgeNumber字段为展示通知时**增加**的角标数量，setBadgeNumber字段为展示通知时**显示**的角标数量，两者同时返回时，setBadgeNumber优先于badgeNumber。详情请参见[RemoteNotificationContent](../harmonyos-references/push-pushcommon.md#remotenotificationcontent)。
   * overlayIcon字段为展示通知时的叠加图标。详情请参见[RemoteNotificationContent](../harmonyos-references/push-pushcommon.md#remotenotificationcontent)。
   * wantAgent.abilityName字段为需要替换的点击拉起的落地页abilityName（例如DemoAbility），DemoAbility需要您自行适配开发。详情请参见[RemoteWantAgent](../harmonyos-references/push-pushcommon.md#remotewantagent)。
   * wantAgent.parameters字段表示传递给应用的数据。详情请参见[RemoteWantAgent](../harmonyos-references/push-pushcommon.md#remotewantagent)。

     **说明** 

     语音播报的功能可在代码示例中的textToSpeech()方法中实现。

     您可参考以下3种Kit能力实现语音播报：

     + 文本转语音 [Core Speech Kit（基础语音服务）](texttospeech-guide.md)。
     + 媒体服务 [Media Kit（媒体服务）](media-kit-intro.md)。
     + 音频播放 [Audio Kit（音频服务）](audio-playback-overview.md)。
5. 应用服务端调用REST API推送消息后，若应用进程在前台，通知栏将不会弹出通知提醒。实现步骤如下：

   在项目模块的**src/main/module.json5**文件的abilities模块中（以PushMessageAbility为例）配置skills标签的actions属性内容为**action.ohos.push.listener**（有且只能有一个ability定义该action，**若同时添加uris参数，则uris内容需为空**）：

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

   在客户端项目中现有的UIAbility类的onCreate()中（以PushMessageAbility为例），通过[receiveMessage](../harmonyos-references/push-pushservice.md#pushservicereceivemessage)()方法传入[PushType](../harmonyos-references/push-pushservice.md#pushservicepushtype)为"IM"获取语音播报消息，用于应用在前台时接收语音播报消息，示例代码如下：

   导入pushService模块及相关公共模块:

   ```typescript
   import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   import { pushService } from '@kit.PushKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```

   调用receiveMessage接口接收Push场景化消息：

   ```typescript
   const DOMAIN = 0x0000;

   export default class PushMessageAbility extends UIAbility {
     onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       // ...
       try {
         pushService.receiveMessage('IM', this, (payload) => {
           hilog.info(DOMAIN, 'testTag', '%{public}s', 'receive message for IM type');

           try {
             const data: string = payload?.data;
             // 处理数据
             hilog.info(DOMAIN, 'testTag', 'Succeeded in getting notification, data=%{public}s',
               JSON.stringify(JSON.parse(data)?.notification));
           } catch (err) {
             const e: BusinessError = err as BusinessError;
             hilog.error(DOMAIN, 'testTag', 'Failed to process data: %{public}d %{public}s', e.code, e.message);
           }
         });
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Succeeded in registering IM message');
       } catch (err) {
         const e: BusinessError = err as BusinessError;
         hilog.error(DOMAIN, 'testTag', 'Failed to register IM message: %{public}d %{public}s', e.code, e.message);
       }
     }
     // ...
   }
   ```
