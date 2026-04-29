---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-send-extend-noti
title: 发送语音播报消息
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > 推送场景化消息 > 推送语音播报消息 > 发送语音播报消息
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:55+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:0a592373f4e85203f0d86cb469055a142b57c45ee8f47c995a35018870cd43ae
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

**正式发布阶段**，单设备单应用下每日推送消息总条数受[设备消息频控](../harmonyos-references/push-msg-freq-control.md#设备消息频控)限制，系统会根据现网使用场景和流量进行管控，不合理的使用场景系统会进行频控。

## 开发步骤

1. 参见指导[获取Push Token](push-get-token.md)。
2. 为确保应用可正常收到消息，建议应用发送通知前调用[requestEnableNotification](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagerrequestenablenotification10-1)()方法弹出提醒，告知用户需要允许接收通知消息。详情请参见Notification Kit-[请求通知授权](notification-enable.md)。
3. 应用服务端调用REST API推送消息，消息详情可参见[场景化消息API接口功能介绍](../harmonyos-references/push-scenariozed-api-intro.md)，请求示例如下：

   ```
   1. // Request URL
   2. POST "https://push-api.cloud.huawei.com/v3/[projectId]/messages:send"

   4. // Request Header
   5. Content-Type: application/json
   6. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
   7. push-type: 2

   9. // Request Body
   10. {
   11. "payload": {
   12. "extraData": "{\"title\":\"replace title\",\"text\":\"replace text\"}",
   13. "notification": {
   14. "category": "PLAY_VOICE",
   15. "title": "通知标题",
   16. "body": "通知内容",
   17. "clickAction": {
   18. "actionType": 0
   19. },
   20. "notifyId": 12345
   21. }
   22. },
   23. "target": {
   24. "token": ["MAMzLg**********lPW"]
   25. },
   26. "pushOptions": {
   27. "testMessage": true,
   28. "ttl": 86400
   29. }
   30. }
   ```

   * [projectId]：项目ID，登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”，在该页面获取。
   * Authorization：JWT格式字符串，可参见[Authorization](../harmonyos-references/push-scenariozed-api-request-struct.md#request-header)获取。
   * push-type：2，表示语音播报场景。
   * category：消息自分类类别，当前支持设置为PLAY\_VOICE。
   * actionType：0表示点击消息打开应用首页。
   * token：Push Token，可参见[获取Push Token](push-get-token.md)获取。
   * extraData：语音播报场景可携带的额外数据，字符串类型。详情参见[ExtensionPayload 语音播报消息](../harmonyos-references/push-scenariozed-api-request-param.md#extensionpayload-语音播报消息)。extraData数据获取请参考[示例代码](https://gitcode.com/HarmonyOS_Samples/push-kit-sample-code-clientdemo-arkts/blob/master/entry/src/main/ets/entryability/RemoteNotificationExtAbility.ets)。
   * testMessage：（选填）测试消息标识，true表示测试消息。每个项目每天限制发送1000条测试消息，单次推送可发送Token数不超过10个。详情请参见[testMessage](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)。
   * ttl：（选填）消息缓存时间，详见[ttl](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)。
   * notifyId：（选填）自定义消息标识字段。不携带或者设置-1时，Push Kit自动为每条消息生成一个唯一标识；不同的通知消息可以拥有相同的notifyId，实现新消息覆盖旧消息功能。仅支持数字，范围 [0, 2147483647]，若要**用于消息撤回则必填**。详情请参见[notifyId](../harmonyos-references/push-scenariozed-api-request-param.md#notification)。
   * image：（选填）通知右侧大图标URL，URL使用的协议必须是HTTPS协议。

   说明

   Push Kit禁止推送包含敏感信息的图片。
4. 应用服务端调用REST API推送消息后，若应用进程在后台，Push Kit会将通知消息内容传递给通知扩展进程，并返回特定的消息内容（例如title、body等）后，通知栏将弹出通知提醒。实现步骤如下：

   在项目工程的**src/main/module.json5**文件的**extensionAbilities**模块中配置RemoteNotificationExtAbility的**type**和**actions**信息（**定义该type和actions的ExtensionAbility有且只能有一个，配置如下，若同时添加uris参数，则uris内容需为空**）：

   ```
   1. "extensionAbilities": [
   2. {
   3. "name": "RemoteNotificationExtAbility",
   4. "type": "remoteNotification",
   5. "srcEntry": "./ets/entryability/RemoteNotificationExtAbility.ets",
   6. "description": "RemoteNotificationExtAbility test",
   7. "exported": false,
   8. "skills": [
   9. // 新增一个独立的skill对象，配置actions参数
   10. {
   11. "actions": ["action.hms.push.extension.remotenotification"]
   12. }
   13. ]
   14. }
   15. ]
   ```

   * type：固定值为**remoteNotification**，表示通知扩展的ExtensionAbility类型。
   * actions：固定值为**action.hms.push.extension.remotenotification**，用于接收语音播报消息。

   在您的工程内创建一个ExtensionAbility类型的组件并且继承[RemoteNotificationExtensionAbility](../harmonyos-references/push-remote-notification-extension-ability.md)，完成[onReceiveMessage](../harmonyos-references/push-remote-notification-extension-ability.md#onreceivemessage)()方法的覆写，在此方法中进行数据接收及业务处理。代码示例如下：

   ```
   1. // 文件路径: src/main/ets/entryability/RemoteNotificationExtAbility.ets
   2. import { pushCommon, RemoteNotificationExtensionAbility } from '@kit.PushKit';
   3. import { image } from '@kit.ImageKit';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';
   5. import { resourceManager } from '@kit.LocalizationKit';
   6. import { common } from '@kit.AbilityKit';

   8. export default class RemoteNotificationExtAbility extends RemoteNotificationExtensionAbility {
   9. async onReceiveMessage(remoteNotificationInfo: pushCommon.RemoteNotificationInfo): Promise<pushCommon.RemoteNotificationContent> {
   10. hilog.info(0x0000, 'testTag', 'RemoteNotificationExtAbility onReceiveMessage, remoteNotificationInfo');

   12. // Read the pixel map object
   13. const resourceMgr: resourceManager.ResourceManager = (this.context as common.UIExtensionContext).resourceManager;
   14. let fileData: Uint8Array = new Uint8Array(0);
   15. try {
   16. fileData = await resourceMgr.getMediaContent($r('app.media.startIcon').id);
   17. } catch (e) {
   18. hilog.error(0x0000, 'testTag', 'Failed to get media content: %{public}d %{public}s', e.code, e.message);
   19. }
   20. const buffer = fileData.buffer;
   21. const imageSource: image.ImageSource = image.createImageSource(buffer as ArrayBuffer);
   22. const pixelMap: image.PixelMap = await imageSource.createPixelMap();
   23. if (pixelMap) {
   24. pixelMap.getImageInfo((err, imageInfo) => {
   25. if (imageInfo) {
   26. hilog.info(0x0000, 'testTag', `imageInfo ${imageInfo.size.width} * ${imageInfo.size.height}`);
   27. }
   28. });
   29. }

   31. // 应用自行实现语音播报的逻辑
   32. this.textToSpeech();

   34. // Return the display message content.
   35. return {
   36. title: 'Default replace title.',
   37. text: 'Default replace text.',
   38. badgeNumber: 1,
   39. setBadgeNumber: 2,
   40. overlayIcon: pixelMap,
   41. wantAgent: {
   42. abilityName: 'DemoAbility',
   43. parameters: {
   44. key: 'Default value'
   45. }
   46. }
   47. }
   48. }

   50. textToSpeech(): void {
   51. // Perform the text-to-speech task.
   52. }

   54. onDestroy(): void {
   55. hilog.info(0x0000, 'testTag', 'RemoteNotificationExtAbility onDestroy.');
   56. }
   57. }
   ```

   * 函数的返回值用于替换最终展示在终端的通知，title和text代表您要展示的通知标题与通知内容。
   * badgeNumber字段为展示通知时**增加**的角标数量，setBadgeNumber字段为展示通知时**显示**的角标数量，两者同时返回时，setBadgeNumber优先于badgeNumber。详情请参见[RemoteNotificationContent](../harmonyos-references/push-pushcommon.md#remotenotificationcontent)。
   * overlayIcon字段为展示通知时的叠加图标。详情请参见[RemoteNotificationContent](../harmonyos-references/push-pushcommon.md#remotenotificationcontent)。
   * wantAgent.abilityName字段为需要替换的点击拉起的落地页abilityName（例如DemoAbility），DemoAbility需要您自行适配开发。详情请参见[RemoteWantAgent](../harmonyos-references/push-pushcommon.md#remotewantagent)。
   * wantAgent.parameters字段表示传递给应用的数据。详情请参见[RemoteWantAgent](../harmonyos-references/push-pushcommon.md#remotewantagent)。

     说明

     语音播报的功能可在代码示例中的textToSpeech()方法中实现。

     您可参考以下3种Kit能力实现语音播报：

     + 文本转语音 [Core Speech Kit（基础语音服务）](texttospeech-guide.md)。
     + 媒体服务 [Media Kit（媒体服务）](media-kit-intro.md)。
     + 音频播放 [Audio Kit（音频服务）](audio-playback-overview.md)。
5. 应用服务端调用REST API推送消息后，若应用进程在前台，通知栏将不会弹出通知提醒。实现步骤如下：

   在项目模块的**src/main/module.json5**文件的abilities模块中（以PushMessageAbility为例）配置skills标签的actions属性内容为**action.ohos.push.listener**（有且只能有一个ability定义该action，**若同时添加uris参数，则uris内容需为空**）：

   ```
   1. {
   2. "name": "PushMessageAbility",
   3. "srcEntry": "./ets/abilities/PushMessageAbility.ets",
   4. "launchType": "singleton",
   5. "startWindowIcon": "$media:startIcon",
   6. "startWindowBackground": "$color:start_window_background",
   7. "exported": false,
   8. "skills": [
   9. // 保持现有skill对象不变
   10. {
   11. "actions": [
   12. "com.app.action"
   13. ]
   14. },
   15. // 新增一个独立的skill对象，配置actions参数
   16. {
   17. "actions": [
   18. "action.ohos.push.listener"
   19. ]
   20. }
   21. ]
   22. }
   ```

   在客户端项目中现有的UIAbility类的onCreate()中（以PushMessageAbility为例），通过[receiveMessage](../harmonyos-references/push-pushservice.md#pushservicereceivemessage)()方法传入[PushType](../harmonyos-references/push-pushservice.md#pushservicepushtype)为"IM"获取语音播报消息，用于应用在前台时接收语音播报消息，示例代码如下：

   ```
   1. // 文件路径: src/main/ets/abilities/PushMessageAbility.ets
   2. import { UIAbility } from '@kit.AbilityKit';
   3. import { pushService } from '@kit.PushKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   5. import { hilog } from '@kit.PerformanceAnalysisKit';

   7. /**
   8. * 此处以PushMessageAbility为例，用于应用在前台时接收语音播报消息
   9. */
   10. export default class PushMessageAbility extends UIAbility {
   11. onCreate(): void {
   12. try {
   13. // receiveMessage中的参数固定为IM
   14. pushService.receiveMessage('IM', this, (payload) => {
   15. try {
   16. // 获取服务端传递的数据
   17. const data: string = payload.data;
   18. // TODO：业务自行处理
   19. hilog.info(0x0000, 'testTag', 'Succeeded in getting notification,data=%{public}s',
   20. JSON.stringify(JSON.parse(data)?.notification));
   21. } catch (e) {
   22. let errRes: BusinessError = e as BusinessError;
   23. hilog.error(0x0000, 'testTag', 'Failed to process data: %{public}d %{public}s',
   24. errRes.code, errRes.message);
   25. }
   26. });
   27. } catch (err) {
   28. let e: BusinessError = err as BusinessError;
   29. hilog.error(0x0000, 'testTag', 'Failed to get message: %{public}d %{public}s', e.code,
   30. e.message);
   31. }
   32. }
   33. }
   ```
