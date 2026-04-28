---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-voip
title: 推送应用内通话消息
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > 推送场景化消息 > 推送应用内通话消息
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:07c9304547faf94c7f36668dbc25df8707be32dc0dbebfe7ca9eb56cd2849c66
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

说明

* 应用内通话消息的问题场景请参见[指导](push-faq-7.md)。
* 应用内通话消息的pushOptions.[ttl](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)建议设置为**30~60秒**。

## 约束与限制

应用内通话消息支持Phone、Tablet设备，并且从6.1.0(23)版本开始，新增支持Lite Wearable设备。

## 开通权益

推送应用内通话消息需要申请场景化消息权益，请参见[申请推送应用内通话消息权益](push-apply-right.md#申请推送应用内通话消息权益)。

## 频控规则

**调测阶段**，每个项目每日全网最多可推送1000条测试消息。发送测试消息需设置[testMessage](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)为true。

**正式发布阶段**，单设备单应用下每日推送消息总条数受[设备消息频控](../harmonyos-references/push-msg-freq-control.md#设备消息频控)限制，系统会根据现网使用场景和流量进行管控，不合理的使用场景系统会进行频控。

## 开发步骤

1. 参见指导[获取Push Token](push-get-token.md)。
2. 在您的工程内创建一个UIAbility类型的组件，如VoIPUIAbility.ets（在项目工程的**src/main/ets/entryability**目录下），负责处理应用内通话消息的主流程，并完成[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)()、[onWindowStageCreate](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)()、[onDestroy](../harmonyos-references/js-apis-app-ability-uiability.md#ondestroy)()方法的覆写，代码示例如下：

   ```
   1. // 文件路径: src/main/ets/entryability/VoIPUIAbility.ets
   2. import { UIAbility } from '@kit.AbilityKit';
   3. import { pushService } from '@kit.PushKit';
   4. import { window } from '@kit.ArkUI';
   5. import { hilog } from '@kit.PerformanceAnalysisKit';
   6. import { VoipCallService } from '../service/VoipCallService';
   7. import { BusinessError } from '@kit.BasicServicesKit';

   9. export default class VoIPUIAbility extends UIAbility {
   10. onCreate(): void {
   11. hilog.info(0x0000, 'testTag', `VoIPUIAbility onCreate`);

   13. try {
   14. pushService.receiveMessage('VoIP', this, async (data) => {
   15. // process message，并建议对Callback进行try-catch
   16. try {
   17. await VoipCallService.processVoIPMainMsg(data.data, this.context);
   18. } catch (error) {
   19. hilog.error(0x0000, 'testTag', 'Failed to process VoIP message: %{public}d %{public}s',
   20. error.code,
   21. error.message);
   22. }
   23. });
   24. } catch (e) {
   25. hilog.error(0x0000, 'testTag', `Failed to register VOIP, error: ${e.code}, ${e.message}.`);
   26. }
   27. }

   29. onWindowStageCreate(windowStage: window.WindowStage): void {
   30. hilog.info(0x0000, 'testTag', `VoIPUIAbility onWindowStageCreate`);

   32. windowStage.loadContent('pages/CalleePage').catch((err: BusinessError) => {
   33. hilog.error(0x0000, 'testTag', `Failed to load content, error: ${err.code}, ${err.message}.`);
   34. });
   35. }

   37. onDestroy(): void {
   38. hilog.info(0x0000, 'testTag', 'VoIPUIAbility onDestroy');
   39. }
   40. }
   ```

   VoipCallService.ets（在项目工程的**src/main/ets/service**目录下），处理应用内通话消息，代码示例如下：

   ```
   1. // 文件路径: src/main/ets/service/VoipCallService.ets
   2. import { voipCall } from '@kit.CallServiceKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. import { common } from '@kit.AbilityKit';
   5. import { image } from '@kit.ImageKit';
   6. import { resourceManager } from '@kit.LocalizationKit';
   7. import { BusinessError } from '@kit.BasicServicesKit';

   9. export interface VoipScene {
   10. scene: string;
   11. }

   13. export interface Content {
   14. data: string;
   15. header: string;
   16. callId: string;
   17. }

   19. export class VoipCallService {
   20. private static callId: string | undefined;

   22. public static async processVoIPMainMsg(data: string,
   23. context: common.UIAbilityContext): Promise<void> {
   24. hilog.info(0x0000, 'testTag', `Process VoIP message: ${data}`);

   26. let content: Content = JSON.parse(data);
   27. let scene: VoipScene = JSON.parse(content.data);
   28. let callId: string = content.callId;
   29. if (!callId) {
   30. hilog.error(0x0000, 'testTag', `CallId is null`);
   31. }
   32. VoipCallService.callId = callId;

   34. try {
   35. // 注册voipCallUiEvent事件
   36. voipCall.on('voipCallUiEvent', async (event) => {
   37. hilog.info(0x0000, 'testTag', `Process voip call ui event: ${JSON.stringify(event)}.`);

   39. await VoipCallService.processVoipCallEvent(event.voipCallUiEvent);
   40. });
   41. } catch (err) {
   42. let e: BusinessError = err as BusinessError;
   43. hilog.error(0x0000, 'testTag', 'Failed to register event: %{public}d %{public}s', e.code, e.message);
   44. }

   46. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
   47. // example.png表示用户头像，取值为“/resources/rawfile”路径下的文件名
   48. let fileData: Uint8Array = new Uint8Array(0);
   49. try {
   50. fileData = await resourceMgr.getRawFileContent('example.png');
   51. } catch (e) {
   52. hilog.error(0x0000, 'testTag', 'Failed to get raw file: %{public}d %{public}s', e.code, e.message);
   53. }
   54. const buffer = fileData.buffer;
   55. const imageSource: image.ImageSource = image.createImageSource(buffer);
   56. const pixelMap: image.PixelMap = await imageSource.createPixelMap();
   57. if (pixelMap) {
   58. pixelMap.getImageInfo((err, imageInfo) => {
   59. if (imageInfo) {
   60. hilog.info(0x0000, 'testTag',
   61. `User profile imageInfo: ${imageInfo.size.width} * ${imageInfo.size.height}.`);
   62. }
   63. });
   64. }

   66. // 构造上报来电的参数。注意，voipCallType.scene为您自定义的场景类型字段，从云侧推送消息时，请注意与端侧取值保持一致
   67. let call: voipCall.VoipCallAttribute = {
   68. callId: callId,
   69. voipCallType: scene?.scene === 'video' ? voipCall.VoipCallType.VOIP_CALL_VIDEO :
   70. voipCall.VoipCallType.VOIP_CALL_VOICE,
   71. userName: 'push',
   72. userProfile: pixelMap,
   73. abilityName: 'VoIPUIAbility',
   74. voipCallState: voipCall.VoipCallState.VOIP_CALL_STATE_RINGING
   75. };

   77. try {
   78. // 上报来电
   79. let error = await voipCall.reportIncomingCall(call);
   80. hilog.info(0x0000, 'testTag', `ReportIncomingCall result: ${error}.`);
   81. } catch (err) {
   82. let e: BusinessError = err as BusinessError;
   83. hilog.error(0x0000, 'testTag', 'Failed to report incoming call: %{public}d %{public}s', e.code, e.message);
   84. }

   86. // ...应用播放振动和铃声
   87. }

   89. public static async processVoipCallEvent(event: voipCall.VoipCallUiEvent) {
   90. try {
   91. switch (event) {
   92. case voipCall.VoipCallUiEvent.VOIP_CALL_EVENT_VOICE_ANSWER:
   93. case voipCall.VoipCallUiEvent.VOIP_CALL_EVENT_VIDEO_ANSWER:
   94. // 立即向Call Service Kit上报answered状态
   95. await voipCall.reportCallStateChange(VoipCallService.callId,
   96. voipCall.VoipCallState.VOIP_CALL_STATE_ANSWERED);

   98. // ...在应用内完成接听

   100. // 应用内接听后，向Call Service Kit上报active状态
   101. await voipCall.reportCallStateChange(VoipCallService.callId,
   102. voipCall.VoipCallState.VOIP_CALL_STATE_ACTIVE);
   103. break;
   104. case voipCall.VoipCallUiEvent.VOIP_CALL_EVENT_REJECT:
   105. case voipCall.VoipCallUiEvent.VOIP_CALL_EVENT_HANGUP:
   106. // ...应用内完成挂断

   108. // 向Call Service Kit上报通话状态
   109. await voipCall.reportCallStateChange(VoipCallService.callId,
   110. voipCall.VoipCallState.VOIP_CALL_STATE_DISCONNECTED);
   111. break;
   112. default: {
   113. break;
   114. }
   115. }
   116. } catch (err) {
   117. let e: BusinessError = err as BusinessError;
   118. hilog.error(0x0000, 'testTag', 'Failed to report call state change: %{public}d %{public}s', e.code, e.message);
   119. }
   120. }

   122. public static close(): void {
   123. hilog.info(0x0000, 'testTag', `Close VoIP`);

   125. VoipCallService.processVoipCallEvent(voipCall.VoipCallUiEvent.VOIP_CALL_EVENT_HANGUP);
   126. try {
   127. voipCall.off('voipCallUiEvent');
   128. } catch (err) {
   129. let e: BusinessError = err as BusinessError;
   130. hilog.error(0x0000, 'testTag', 'Failed to unregister event: %{public}d %{public}s', e.code, e.message);
   131. }
   132. }
   133. }
   ```

   说明

   需要在项目工程的src/main/resources/rawfile目录下添加example.png，表示来电时的用户头像。

   * UIAbility.onCreate是同步接口，不支持异步回调，需要在onCreate生命周期的入口，完成[pushService.receiveMessage](../harmonyos-references/push-pushservice.md#pushservicereceivemessage)()注册，并且保证在注册前没有等待异步方法执行的调用。
   * 在[receiveMessage](../harmonyos-references/push-pushservice.md#pushservicereceivemessage)()回调中接收应用内通话消息，建议应用提前和服务器建连，用户点击接听后可以立即进行通话，并调用[voipCall.on](../harmonyos-references/call-voipcall.md#voipcallonvoipcalluievent)()接口注册监听通话状态回调。用户点击接听或者拒绝接听之后，系统会通过应用注册的事件监听通话状态回调结果。
   * 应用需要在10秒内调用[voipCall.reportIncomingCall](../harmonyos-references/call-voipcall.md#voipcallreportincomingcall)()接口上报通话来电状态，调用完成之后，系统会弹出应用内通话横幅通知。[voipCall.reportIncomingCall](../harmonyos-references/call-voipcall.md#voipcallreportincomingcall)()**接口入参中的callId需要使用receiveMessage()回调中的callId**。
   * 如果应用来电消息建立失败，需要调用[voipCall.reportIncomingCallError](../harmonyos-references/call-voipcall.md#voipcallreportincomingcallerror)()通知来电消息建立失败。如果应用在前台，通过自己的网络连接接收到来电消息，调用[voipCall.reportIncomingCall](../harmonyos-references/call-voipcall.md#voipcallreportincomingcall)()接口上报了通话来电状态，后面才收到Push推送的应用内通话消息，在该消息处理中需要调用[voipCall.reportIncomingCallError](../harmonyos-references/call-voipcall.md#voipcallreportincomingcallerror)()上报[应用线路忙](../harmonyos-references/call-voipcall.md#voipcallfailurecause)。
   * 应用内通话主要有三种回调状态，分别为：接听状态、拒绝状态和挂断状态。
     + 在接听状态回调中，应用在建立连接成功之后，需要调用[voipCall.reportCallStateChange](../harmonyos-references/call-voipcall.md#section491515915329)()接口上报通话激活状态。
     + 在拒绝接听状态回调中，应用断开和服务器的连接之后，需要调用[voipCall.reportCallStateChange](../harmonyos-references/call-voipcall.md#section491515915329)()接口上报通话断开状态。
     + 在应用进行应用内通话的同时，若运营商来电，会弹出运营商来电接听界面，用户点击接听运营商来电之后，会回调应用内通话挂断状态，在回调方法中应用需要自行断开和服务器的连接，并调用[voipCall.reportCallStateChange](../harmonyos-references/call-voipcall.md#section491515915329)()接口上报通话断开状态。
   * 有关应用内通话回调状态的更多信息，详情请参见[Call Service Kit简介](call-introduction.md)。
   * 应用上报通话来电状态之后，可以调用[vibrator.startVibration](../harmonyos-references/js-apis-vibrator.md#vibratorstartvibration9-1)触发振动，有关振动的更多详情，请参见[Sensor Service Kit简介](sensorservice-kit-intro.md)。可以使用AVPlayer播放应用铃声，音频流建议设置为铃声，usage设置为STREAM\_USAGE\_RINGTONE，效果为开始响铃，播放的音乐会暂停播放。同时推荐使用AudioSession管理音频焦点，可以保证接听过程中、通话过程中都保持音频焦点，详情请参见[Audio Kit简介](audio-kit-intro.md)。
   * 进行音视频通话时，若您的应用处于Overhead场景（设备发热严重或负载较重，Level=4），请降低码率和帧率，或关闭视频流降级为音频。相关说明请参见Basic Services Kit（基础服务）提供的接口[getLevel](../harmonyos-references/js-apis-resourceschedule-systemload.md#systemloadgetlevel)()。
3. 在项目工程的 **src/main/ets/pages**目录添加：视频接听页面CalleePage.ets，代码示例如下：

   ```
   1. // 文件路径: src/main/ets/pages/CalleePage.ets
   2. import CallComponent from '../component/CallComponent';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';

   5. @Entry
   6. @Component
   7. struct CalleePage {
   8. @StorageLink('close') @Watch('close') end: boolean | undefined = undefined;

   10. aboutToAppear() {
   11. hilog.info(0x0000, 'testTag', `CalleePage aboutToAppear`);

   13. this.end = false;
   14. }

   16. private close() {
   17. if (this.end) {
   18. hilog.info(0x0000, 'testTag', `CalleePage close`);

   20. this.getUIContext().getRouter().back(); // 此处仅为示例（跳转返回），请根据实际情况设定路由
   21. }
   22. }

   24. aboutToDisappear() {
   25. hilog.info(0x0000, 'testTag', `CalleePage aboutToDisappear`);
   26. }

   28. build() {
   29. Column() {
   30. CallComponent({})
   31. }
   32. }
   33. }
   ```

   CallComponent.ets（在项目工程的**src/main/ets/component**目录下），代码示例如下：

   ```
   1. // 文件路径: src/main/ets/component/CallComponent.ets
   2. import { VoipCallService } from '../service/VoipCallService';
   3. import { voipCall } from '@kit.CallServiceKit';

   5. @Component
   6. export default struct CallComponent {
   7. @StorageLink('close') end: boolean | undefined = undefined;

   9. build() {
   10. Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.SpaceBetween }) {
   11. Row() {
   12. }
   13. .width('100%')
   14. .justifyContent(FlexAlign.Center)

   16. Row({ space: 30 }) {

   18. Column() {
   19. Button()
   20. .width(80)
   21. .height(80)
   22. .backgroundColor(Color.Green)
   23. .onClick(() => {
   24. VoipCallService.processVoipCallEvent(voipCall.VoipCallUiEvent.VOIP_CALL_EVENT_VIDEO_ANSWER);
   25. })

   27. Text('Answer').fontColor(Color.White).padding({ top: 5 })
   28. }

   30. Column() {
   31. Button()
   32. .width(80)
   33. .height(80)
   34. .backgroundColor(Color.Red)
   35. .onClick(() => {
   36. this.end = true;
   37. VoipCallService.close();
   38. })

   40. Text('Hang Up').fontColor(Color.White).padding({ top: 5 })
   41. }

   43. }
   44. .width('100%')
   45. .justifyContent(FlexAlign.Center)
   46. }
   47. .padding('30 10')
   48. .backgroundColor(Color.Black)
   49. }
   50. }
   ```

   在项目工程的 src/main/resources/base/profile/main\_pages.json添加page目录，示例如下：

   ```
   1. {
   2. "src": [
   3. "pages/Index",
   4. "pages/CalleePage"
   5. ]
   6. }
   ```

   说明

   示例代码提供的页面效果仅供开发参考，不代表最终效果。
4. 在项目工程的 **src/main/module.json5** 文件的**abilities**模块中配置VoIPUIAbility的 **actions** 信息。

   ```
   1. "abilities": [
   2. {
   3. "name": "VoIPUIAbility",
   4. "srcEntry": "./ets/entryability/VoIPUIAbility.ets",
   5. "launchType": "singleton",
   6. "description": "VoIPUIAbility test",
   7. "startWindowIcon": "$media:startIcon",
   8. "startWindowBackground": "$color:start_window_background",
   9. "exported": false,
   10. "skills": [
   11. // 保持现有skill对象不变
   12. // 新增一个独立的skill对象，配置actions参数
   13. {
   14. "actions": ["action.ohos.push.listener"]
   15. }
   16. ]
   17. }
   18. ]
   ```

   * actions：内容为**action.ohos.push.listener**，有且只能有一个ability定义该action，**若同时添加uris参数，则uris内容需为空**。
5. 应用服务端调用REST API推送消息，消息详情可参见[场景化消息API接口功能介绍](../harmonyos-references/push-scenariozed-api-intro.md)。

### 应用内通话消息

1. 如果您需要呼叫，应用服务器可以调用REST API推送应用内通话消息，请求示例如下：

   ```
   1. // Request URL
   2. POST "https://push-api.cloud.huawei.com/v3/[projectId]/messages:send"

   4. // Request Header
   5. Content-Type: application/json
   6. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
   7. push-type: 10

   9. // Request Body
   10. {
   11. "pushOptions": {
   12. "ttl": 30
   13. },
   14. "payload": {
   15. "extraData": "{\"scene\": \"voice\"}"
   16. },
   17. "target": {
   18. "token": ["MAMzLg**********aZW"]
   19. }
   20. }
   ```

   * [projectId]：项目ID，登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”，在该页面获取。
   * Authorization：JWT格式字符串，可参见[基于服务账号生成鉴权令牌](push-jwt-token.md)进行获取。
   * push-type：10表示应用内通话消息场景。
   * token：Push Token，可参见[获取Push Token](push-get-token.md)章节获取。
   * extraData：携带的额外数据，字符串类型。详情参见[VoIPCallPayload 应用内通话消息](../harmonyos-references/push-scenariozed-api-request-param.md#voipcallpayload-应用内通话消息)中extraData参数用法。extraData数据获取请参考[示例代码](https://gitcode.com/harmonyos_samples/push-kit-sample-code-clientdemo-arkts/blob/master/entry/src/main/ets/service/VoipCallService.ets)。
   * ttl：消息缓存时间，建议设置为30~60秒，详见pushOptions.[ttl](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)。

说明

* 应用内通话消息只能用于音视频通话场景唤醒应用，完成呼叫，不要通过此种类型消息来挂断来电或者和应用通信，应用应该使用自己建立的网络连接和应用通信。相比应用服务器推送Push消息，使用现有的网络连接和应用通信通常会更快，在网络不佳的情况下，推送的Push消息可能无法到达应用。
* 应用无论是否在前台，自己的网络连接存在时，建议您通过Push推送应用内通话消息，再通过自己的网络连接发送通话消息，保证该呼叫能够到达应用。

### 未接来电通知

1. 如果您需要给被叫方发送未接来电通知，应用服务器可以调用REST API推送[通知消息](push-send-alert.md)。以通知消息为例，请求示例如下：

   ```
   1. // Request URL
   2. POST "https://push-api.cloud.huawei.com/v3/[projectId]/messages:send"

   4. // Request Header
   5. Content-Type: application/json
   6. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
   7. push-type: 0

   9. // Request Body
   10. {
   11. "pushOptions": {
   12. "ttl":86400
   13. },
   14. "payload": {
   15. "notification": {
   16. "category": "MISS_CALL",
   17. "title": "通知标题",
   18. "body": "通知内容",
   19. "clickAction": {
   20. "actionType": 0
   21. },
   22. "appMessageId": "12345"
   23. }
   24. },
   25. "target": {
   26. "token": ["MAMzLg**********aZW"]
   27. }
   28. }
   ```

   * push-type：0表示通知消息场景。
   * category：消息自分类类别，设置为MISS\_CALL，请参见[参数说明](../harmonyos-references/push-scenariozed-api-request-param.md#notification)，发送消息前请确保您已[申请通知消息自分类权益](push-apply-right.md#申请通知消息自分类权益)。
   * appMessageId：应用消息的唯一标识。被叫挂断，被叫方VoIP应用在前台时应用可以通过调用[Notification Kit（用户通知服务）](notification-overview.md)发送未接来电通知。被叫方VoIP应用在后台时，可以通过Push推送未接来电通知。应用可能存在前后台状态判断不准确，同一电话会产生两条未接来电，建议您通过Notification Kit和Push Kit推送的未接来电通知使用相同的appMessageId，系统会进行通知去重。
   * 其他参数说明可参见[通知消息请求体参数说明](../harmonyos-references/push-scenariozed-api-request-param.md#alertpayload-通知消息)。
