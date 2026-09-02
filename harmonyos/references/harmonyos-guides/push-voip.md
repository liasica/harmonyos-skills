---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-voip
title: 推送应用内通话消息
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > 推送场景化消息 > 推送应用内通话消息
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:00+08:00
doc_updated_at: 2026-08-03
content_hash: sha256:98e74dcd313d3815172f4ef35f0e9f00b72d0412cbf0c4ac510362eb957f5569
---

## 场景介绍

应用内通话消息，支持应用实现网络音视频通话的能力。当终端处于锁屏或解锁两种不同状态时，Push Kit将分别进行以下处理：

* 终端处于锁屏状态时，可在锁屏上点击接听或拒绝按钮。锁屏状态下**只支持接听语音**。
* 终端处于解锁状态时，网络音视频通话呼叫消息显性展示于横幅，支持用户接听视频或语音。

接听视频时会拉起应用内的接听界面。接通后，可以正常挂断（主动挂断/被动挂断）应用内通话消息。

应用内通话消息样式可参考如下示例，真实样式请以实际效果为准：

| 锁屏 | 来电横幅 |
| --- | --- |
|  |  |

**说明** 

* 应用内通话消息的问题场景请参见[指导](push-faq-7.md)。
* 应用内通话消息的pushOptions.[ttl](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)建议设置为**30~60秒**。

## 约束与限制

推送应用内通话消息能力支持Phone、Tablet设备，并且从6.1.0(23)版本开始，新增支持儿童智能表。

## 开通权益

推送应用内通话消息需要申请场景化消息权益，请参见[申请推送应用内通话消息权益](push-apply-right.md#申请推送应用内通话消息权益)。

## 频控规则

**调测阶段**，每个项目每日全网最多可推送1000条测试消息。发送测试消息需设置[testMessage](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)为true。

**正式发布阶段**，单设备单应用下每日推送消息总条数受[设备消息频控](../harmonyos-references/push-msg-freq-control.md#设备消息频控)限制，系统会根据使用场景和流量进行管控，不合理的使用场景系统会进行频控。

## 开发步骤

1. 参见指导[获取Push Token](push-get-token.md)。
2. 在您的工程内创建一个UIAbility类型的组件，如VoIPUIAbility.ets（在项目工程的**src/main/ets/entryability**目录下），负责处理应用内通话消息的主流程，并完成[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)()、[onWindowStageCreate](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)()、[onDestroy](../harmonyos-references/js-apis-app-ability-uiability.md#ondestroy)()方法的覆写，代码示例如下：

   ```typescript
   import { UIAbility } from '@kit.AbilityKit';
   import { pushService } from '@kit.PushKit';
   import { window } from '@kit.ArkUI';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { VoipCallService } from '../service/VoipCallService';
   import { BusinessError } from '@kit.BasicServicesKit';

   const DOMAIN = 0x0000;

   export default class VoIPUIAbility extends UIAbility {
     onCreate(): void {
       hilog.info(DOMAIN, 'testTag', 'VoIPUIAbility onCreate');

       try {
         pushService.receiveMessage('VoIP', this, async (data) => {
           // 处理应用内通话消息数据
           try {
             await VoipCallService.processVoIPMainMsg(data.data, this.context);
           } catch (error) {
             hilog.error(DOMAIN, 'testTag', 'Failed to process VoIP message: %{public}d %{public}s', error.code,
               error.message);
           }
         });
       } catch (e) {
         hilog.error(DOMAIN, 'testTag', `Failed to register VoIP, error: ${e.code}, ${e.message}.`);
       }
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       hilog.info(DOMAIN, 'testTag', 'VoIPUIAbility onWindowStageCreate.');

       windowStage.loadContent('pages/CalleePage').catch((err: BusinessError) => {
         hilog.error(DOMAIN, 'testTag', `Failed to load content, error: ${err.code}, ${err.message}.`);
       });
     }

     onDestroy(): void {
       hilog.info(DOMAIN, 'testTag', 'VoIPUIAbility onDestroy');
     }
   }
   ```

   VoipCallService.ets（在项目工程的**src/main/ets/service**目录下），处理应用内通话消息，代码示例如下：

   ```typescript
   import { voipCall } from '@kit.CallServiceKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { common } from '@kit.AbilityKit';
   import { image } from '@kit.ImageKit';
   import { resourceManager } from '@kit.LocalizationKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   export interface VoipScene {
     scene: string;
   }

   export interface Content {
     data: string;
     header: string;
     callId: string;
   }

   const DOMAIN = 0x0000;

   export class VoipCallService {
     private static callId: string | undefined;

     public static async processVoIPMainMsg(data: string,
       context: common.UIAbilityContext): Promise<void> {
       hilog.info(DOMAIN, 'testTag', `Process VoIP message: ${data}`);

       let content: Content;
       let scene: VoipScene;
       let callId: string;

       try {
         content = JSON.parse(data);
         scene = JSON.parse(content.data);
         callId = content.callId;
         if (!callId) {
           hilog.error(DOMAIN, 'testTag', 'CallId is null');
         }
         VoipCallService.callId = callId;
       } catch (e) {
         let err: BusinessError = e as BusinessError;
         hilog.error(DOMAIN, 'testTag', 'Failed to parse VoIP message data: %{public}d %{public}s', err.code, err.message);
         return;
       }

       try {
         // 注册voipCallUiEvent事件
         voipCall.on('voipCallUiEvent', async (event) => {
           hilog.info(DOMAIN, 'testTag', `Process voip call ui event: ${JSON.stringify(event)}.`);

           await VoipCallService.processVoipCallEvent(event.voipCallUiEvent);
         });
       } catch (err) {
         let e: BusinessError = err as BusinessError;
         hilog.error(DOMAIN, 'testTag', 'Failed to register event: %{public}d %{public}s', e.code, e.message);
       }

       const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
       let fileData: Uint8Array = new Uint8Array(0);
       try {
         // example.png表示用户头像，取值为“/resources/rawfile”路径下的文件名
         fileData = await resourceMgr.getRawFileContent('example.png');
       } catch (e) {
         hilog.error(DOMAIN, 'testTag', 'Failed to get raw file: %{public}d %{public}s', e.code, e.message);
       }
       const buffer = fileData.buffer;
       const imageSource: image.ImageSource = image.createImageSource(buffer);
       const pixelMap: image.PixelMap = await imageSource.createPixelMap();
       if (pixelMap) {
         pixelMap.getImageInfo((err, imageInfo) => {
           if (imageInfo) {
             hilog.info(DOMAIN, 'testTag',
               `User profile imageInfo: ${imageInfo.size.width} * ${imageInfo.size.height}.`);
           } else {
             hilog.error(DOMAIN, 'testTag', `Failed to obtain the image information.code is ${err.code}, message is ${err.message}`);
           }
         });
       }

       // 构造上报来电的参数。注意，voipCallType.scene为您自定义的场景类型字段，从云侧推送消息时，请注意与端侧取值保持一致
       let call: voipCall.VoipCallAttribute = {
         callId: callId,
         voipCallType: scene?.scene === 'video' ? voipCall.VoipCallType.VOIP_CALL_VIDEO :
           voipCall.VoipCallType.VOIP_CALL_VOICE,
         userName: 'push',
         userProfile: pixelMap,
         abilityName: 'VoIPUIAbility',
         voipCallState: voipCall.VoipCallState.VOIP_CALL_STATE_RINGING
       };

       try {
         // 上报来电
         let error = await voipCall.reportIncomingCall(call);
         hilog.info(DOMAIN, 'testTag', `ReportIncomingCall result: ${error}.`);
       } catch (err) {
         let e: BusinessError = err as BusinessError;
         hilog.error(DOMAIN, 'testTag', 'Failed to report incoming call: %{public}d %{public}s', e.code, e.message);
       }

       // ...应用播放振动和铃声
     }

     public static async processVoipCallEvent(event: voipCall.VoipCallUiEvent) {
       try {
         switch (event) {
           case voipCall.VoipCallUiEvent.VOIP_CALL_EVENT_VOICE_ANSWER:
           case voipCall.VoipCallUiEvent.VOIP_CALL_EVENT_VIDEO_ANSWER:
             // 立即向Call Service Kit上报answered状态
             await voipCall.reportCallStateChange(VoipCallService.callId,
               voipCall.VoipCallState.VOIP_CALL_STATE_ANSWERED);

             // ...在应用内完成接听

             // 应用内接听后，向Call Service Kit上报active状态
             await voipCall.reportCallStateChange(VoipCallService.callId,
               voipCall.VoipCallState.VOIP_CALL_STATE_ACTIVE);
             break;
           case voipCall.VoipCallUiEvent.VOIP_CALL_EVENT_REJECT:
           case voipCall.VoipCallUiEvent.VOIP_CALL_EVENT_HANGUP:
             // ...应用内完成挂断

             // 向Call Service Kit上报通话状态
             await voipCall.reportCallStateChange(VoipCallService.callId,
               voipCall.VoipCallState.VOIP_CALL_STATE_DISCONNECTED);
             break;
           default: {
             break;
           }
         }
       } catch (err) {
         let e: BusinessError = err as BusinessError;
         hilog.error(DOMAIN, 'testTag', 'Failed to report call state change: %{public}d %{public}s', e.code, e.message);
       }
     }

     public static close(): void {
       hilog.info(DOMAIN, 'testTag', 'Close VoIP');

       VoipCallService.processVoipCallEvent(voipCall.VoipCallUiEvent.VOIP_CALL_EVENT_HANGUP);
       try {
         voipCall.off('voipCallUiEvent');
       } catch (err) {
         let e: BusinessError = err as BusinessError;
         hilog.error(DOMAIN, 'testTag', 'Failed to unregister event: %{public}d %{public}s', e.code, e.message);
       }
     }
   }
   ```

   **说明** 

   需要在项目工程的src/main/resources/rawfile目录下添加example.png，表示来电时的用户头像。

   * UIAbility.onCreate是同步接口，不支持异步回调，需要在onCreate生命周期的入口，完成[pushService.receiveMessage](../harmonyos-references/push-pushservice.md#pushservicereceivemessage)()注册，并且保证在注册前没有等待异步方法执行的调用。
   * 在[receiveMessage](../harmonyos-references/push-pushservice.md#pushservicereceivemessage)()回调中接收应用内通话消息，建议应用提前和服务器建连，用户点击接听后可以立即进行通话，并调用[voipCall.on](../harmonyos-references/call-voipcall.md#voipcallonvoipcalluievent)接口注册监听通话状态回调。用户点击接听或者拒绝接听之后，系统会通过应用注册的事件监听通话状态回调结果。
   * 应用需要在10秒内调用[voipCall.reportIncomingCall](../harmonyos-references/call-voipcall.md#voipcallreportincomingcall)接口上报通话来电状态，调用完成之后，系统会弹出应用内通话横幅通知。[voipCall.reportIncomingCall](../harmonyos-references/call-voipcall.md#voipcallreportincomingcall)()**接口入参中的callId需要使用receiveMessage()回调中的callId**。
   * 如果应用来电消息建立失败，需要调用[voipCall.reportIncomingCallError](../harmonyos-references/call-voipcall.md#voipcallreportincomingcallerror)()通知来电消息建立失败。如果应用在前台，通过自己的网络连接接收到来电消息，调用[voipCall.reportIncomingCall](../harmonyos-references/call-voipcall.md#voipcallreportincomingcall)接口上报了通话来电状态，后面才收到Push推送的应用内通话消息，在该消息处理中需要调用[voipCall.reportIncomingCallError](../harmonyos-references/call-voipcall.md#voipcallreportincomingcallerror)()上报[应用线路忙](../harmonyos-references/call-voipcall.md#voipcallfailurecause)。
   * 应用内通话主要有三种回调状态，分别为：接听状态、拒绝状态和挂断状态。
     + 在接听状态回调中，应用在建立连接成功之后，需要调用[voipCall.reportCallStateChange](../harmonyos-references/call-voipcall.md#voipcallreportcallstatechange)接口上报通话激活状态。
     + 在拒绝接听状态回调中，应用断开和服务器的连接之后，需要调用[voipCall.reportCallStateChange](../harmonyos-references/call-voipcall.md#voipcallreportcallstatechange)接口上报通话断开状态。
     + 在应用进行应用内通话的同时，若运营商来电，会弹出运营商来电接听界面，用户点击接听运营商来电之后，会回调应用内通话挂断状态，在回调方法中应用需要自行断开和服务器的连接，并调用[voipCall.reportCallStateChange](../harmonyos-references/call-voipcall.md#voipcallreportcallstatechange)接口上报通话断开状态。
   * 有关应用内通话回调状态的更多信息，详情请参见[Call Service Kit简介](call-introduction.md)。
   * 应用上报通话来电状态之后，可以调用[vibrator.startVibration](../harmonyos-references/js-apis-vibrator.md#vibratorstartvibration9-1)触发振动，有关振动的更多详情，请参见[Sensor Service Kit简介](sensorservice-kit-intro.md)。可以使用AVPlayer播放应用铃声，音频流建议设置为铃声，usage设置为STREAM\_USAGE\_RINGTONE，效果为开始响铃，播放的音乐会暂停播放。同时推荐使用AudioSession管理音频焦点，可以保证接听过程中、通话过程中都保持音频焦点，详情请参见[Audio Kit简介](audio-kit-intro.md)。
   * 进行音视频通话时，若您的应用处于OVERHEATED场景（设备发热严重或负载较重，Level=4），请降低码率和帧率，或关闭视频流降级为音频。相关说明请参见Basic Services Kit（基础服务）提供的接口[getLevel](../harmonyos-references/js-apis-resourceschedule-systemload.md#systemloadgetlevel)()。
3. 在项目工程的 **src/main/ets/pages**目录添加：视频接听页面CalleePage.ets，代码示例如下：

   ```typescript
   import CallComponent from '../component/CallComponent';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const DOMAIN = 0x0000;

   @Entry
   @Component
   struct CalleePage {
     @StorageLink('close') @Watch('close') end: boolean | undefined = undefined;

     aboutToAppear() {
       hilog.info(DOMAIN, 'testTag', 'CalleePage aboutToAppear');

       this.end = false;
     }

     private close() {
       if (this.end) {
         hilog.info(DOMAIN, 'testTag', 'CalleePage close');

         this.getUIContext().getRouter().back(); // 此处仅为示例（跳转返回），请根据实际情况设定路由
       }
     }

     aboutToDisappear() {
       hilog.info(DOMAIN, 'testTag', 'CalleePage aboutToDisappear');
     }

     build() {
       Column() {
         CallComponent({})
       }
     }
   }
   ```

   CallComponent.ets（在项目工程的**src/main/ets/component**目录下），代码示例如下：

   ```typescript
   import { VoipCallService } from '../service/VoipCallService';
   import { voipCall } from '@kit.CallServiceKit';

   @Component
   export default struct CallComponent {
     @StorageLink('close') end: boolean | undefined = undefined;

     build() {
       Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.SpaceBetween }) {
         Row() {
         }
         .width('100%')
         .justifyContent(FlexAlign.Center)

         Row({ space: 30 }) {

           Column() {
             Button()
               .width(80)
               .height(80)
               .backgroundColor(Color.Green)
               .onClick(() => {
                 VoipCallService.processVoipCallEvent(voipCall.VoipCallUiEvent.VOIP_CALL_EVENT_VIDEO_ANSWER);
               })

             Text('Answer').fontColor(Color.White).padding({ top: 5 })
           }

           Column() {
             Button()
               .width(80)
               .height(80)
               .backgroundColor(Color.Red)
               .onClick(() => {
                 this.end = true;
                 VoipCallService.close();
               })

             Text('Hang Up').fontColor(Color.White).padding({ top: 5 })
           }

         }
         .width('100%')
         .justifyContent(FlexAlign.Center)
       }
       .padding('30 10')
       .backgroundColor(Color.Black)
     }
   }
   ```

   在项目工程的 src/main/resources/base/profile/main\_pages.json添加page目录，示例如下：

   ```json
   {
     "src": [
       "pages/Index",
       "pages/CalleePage"
     ]
   }
   ```

   **说明** 

   示例代码提供的页面效果仅供开发参考，不代表最终效果。
4. 在项目工程的 **src/main/module.json5** 文件的**abilities**模块中配置VoIPUIAbility的 **actions** 信息。

   ```json5
   "abilities": [
     // ...
     {
       "name": "VoIPUIAbility",
       "srcEntry": "./ets/entryability/VoIPUIAbility.ets",
       "launchType": "singleton",
       "description": "$string:module_desc",
       "startWindowIcon": "$media:startIcon",
       "startWindowBackground": "$color:start_window_background",
       "exported": false,
       "skills": [
         // 保持现有skill对象不变
         // 新增一个独立的skill对象，配置actions参数为action.ohos.push.listener，有且只能有一个ability定义该action
         {
           "actions": [
             "action.ohos.push.listener"
           ]
         }
       ]
     }
     // ...
   ]
   ```

   * actions：内容为**action.ohos.push.listener**，有且只能有一个ability定义该action，**若同时添加uris参数，则uris内容需为空**。
5. 应用服务端调用REST API推送消息，消息详情可参见[场景化消息API接口功能介绍](../harmonyos-references/push-scenariozed-api-intro.md)。

### 应用内通话消息

1. 如果您需要呼叫，应用服务器可以调用REST API推送应用内通话消息，请求示例如下：

   ```json5
   // Request URL
   POST "https://push-api.cloud.huawei.com/v3/[projectId]/messages:send"

   // Request Header
   Content-Type: application/json
   Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
   push-type: 10

   // Request Body
   {
     "pushOptions": {
       "ttl": 30
     },
     "payload": {
       "extraData": "{\"scene\": \"voice\"}"
     },
     "target": {
       "token": ["MAMzLg**********aZW"]
     }
   }
   ```

   * [projectId]：项目ID，登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”，在该页面获取。
   * Authorization：JWT格式字符串，可参见[基于服务账号生成鉴权令牌](push-jwt-token.md)进行获取。
   * push-type：10表示应用内通话消息场景。
   * token：Push Token，可参见[获取Push Token](push-get-token.md)章节获取。
   * extraData：携带的额外数据，字符串类型。详情参见[VoIPCallPayload 应用内通话消息](../harmonyos-references/push-scenariozed-api-request-param.md#voipcallpayload-应用内通话消息)中extraData参数用法。extraData数据获取请参考[示例代码](https://gitcode.com/harmonyos_samples/push-kit-sample-code-clientdemo-arkts/blob/master/entry/src/main/ets/abilities/PushMessageAbility.ets)。
   * ttl：消息缓存时间，建议设置为30~60秒，详见pushOptions.[ttl](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)。

**说明** 

* 应用内通话消息只能用于音视频通话场景唤醒应用，完成呼叫，不要通过此种类型消息来挂断来电或者和应用通信，应用应该使用自己建立的网络连接和应用通信。相比应用服务器推送Push消息，使用现有的网络连接和应用通信通常会更快，在网络不佳的情况下，推送的Push消息可能无法到达应用。
* 应用无论是否在前台，自己的网络连接存在时，建议您通过Push推送应用内通话消息，再通过自己的网络连接发送通话消息，保证该呼叫能够到达应用。

### 未接来电通知

1. 如果您需要给被叫方发送未接来电通知，应用服务器可以调用REST API推送[通知消息](push-send-alert.md)。以通知消息为例，请求示例如下：

   ```json5
   // Request URL
   POST "https://push-api.cloud.huawei.com/v3/[projectId]/messages:send"
      
   // Request Header
   Content-Type: application/json
   Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
   push-type: 0
      
   // Request Body
   {
     "pushOptions": {
       "ttl":86400
     },
     "payload": {
       "notification": {
         "category": "MISS_CALL",
         "title": "通知标题",
         "body": "通知内容",
         "clickAction": {
           "actionType": 0
         },
         "appMessageId": "12345"
       }
      },
      "target": {
        "token": ["MAMzLg**********aZW"]
      }
    }
   ```

   * push-type：0表示通知消息场景。
   * category：消息自分类类别，设置为MISS\_CALL，请参见[参数说明](../harmonyos-references/push-scenariozed-api-request-param.md#notification)，发送消息前请确保您已[申请通知消息自分类权益](push-apply-right.md#申请通知消息自分类权益)。
   * appMessageId：应用消息的唯一标识。主叫挂断，被叫方VoIP应用在前台时应用可以通过调用[Notification Kit（用户通知服务）](notification-overview.md)发送未接来电通知。被叫方VoIP应用在后台时，可以通过Push推送未接来电通知。应用可能存在前后台状态判断不准确，同一电话会产生两条未接来电，建议您通过Notification Kit和Push Kit推送的未接来电通知使用相同的appMessageId，系统会进行通知去重。
   * 其他参数说明可参见[通知消息请求体参数说明](../harmonyos-references/push-scenariozed-api-request-param.md#alertpayload-通知消息)。
