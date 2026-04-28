---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ion-subscriber-extension-ability-development-steps
title: 通知订阅扩展能力开发步骤
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 通知订阅扩展能力 > 通知订阅扩展能力开发步骤
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:de8862c89dbe7c2e11379e3b05887c9ae1b5ba4bf816a15e398eb73c915942db
---

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [onDestroy(): void](../harmonyos-references/js-apis-notificationsubscriberextensionability.md#ondestroy) | 通知订阅扩展被销毁时的回调。 |
| [onReceiveMessage(notificationInfo: NotificationInfo): void](../harmonyos-references/js-apis-notificationsubscriberextensionability.md#onreceivemessage) | 收到通知时的回调。 |
| [onCancelMessages(hashCodes: Array<string>): void](../harmonyos-references/js-apis-notificationsubscriberextensionability.md#oncancelmessages) | 取消通知时的回调。 |

## 前提条件

申请[ohos.permission.SUBSCRIBE\_NOTIFICATION](restricted-permissions.md#ohospermissionsubscribe_notification)权限。

## 开发步骤

开发者在实现[NotificationSubscriberExtensionAbility](../harmonyos-references/js-apis-notificationsubscriberextensionability.md)提供方时，需在[DevEco Studio](ide-tools-overview.md)工程中新建一个NotificationSubscriberExtensionAbility。具体步骤如下。

1. 在entry/src/main/ets/创建目录extensionability。
2. 在entry/src/main/ets/extensionability目录下创建NotificationSubscriberExtAbility.ets，其内容如下。

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';
   2. import { notificationExtensionSubscription, NotificationSubscriberExtensionAbility } from '@kit.NotificationKit';
   3. // ...

   5. const DOMAIN = 0x0000;
   6. // ...
   7. export class NotificationSubscriberExtAbility extends NotificationSubscriberExtensionAbility {
   8. // ...
   9. onDestroy(): void {
   10. hilog.info(DOMAIN, 'testTag', 'onDestroy');
   11. // ...
   12. }
   13. // ...
   14. onReceiveMessage(notificationInfo: notificationExtensionSubscription.NotificationInfo): void {
   15. hilog.info(DOMAIN, 'testTag', `on receive message ${JSON.stringify(notificationInfo)}`)
   16. // ...
   17. }
   18. // ...
   19. onCancelMessages(hashCodes: Array<string>): void {
   20. hilog.info(DOMAIN, 'testTag', `on cancel message ${JSON.stringify(hashCodes)}`)
   21. // ...
   22. }
   23. // ...
   24. }
   ```

   [NotificationSubscriberExtAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/ThirdpartyWerableDemo/entry/src/main/ets/extensionability/NotificationSubscriberExtAbility.ets#L17-L237)
3. 使用[蓝牙模块](connectivity-kit-intro.md#蓝牙简介)接口与穿戴设备配对（蓝牙处于配对状态）并获取地址，然后通过[subscribe](../harmonyos-references/js-apis-notificationextensionsubscription.md#notificationextensionsubscriptionsubscribe)/[unsubscribe](../harmonyos-references/js-apis-notificationextensionsubscription.md#notificationextensionsubscriptionunsubscribe)接口订阅或取消订阅通知。
4. 实现[NotificationSubscriberExtensionAbility](../harmonyos-references/js-apis-notificationsubscriberextensionability.md)后，还需要在合适的时机调用[openSubscriptionSettings](../harmonyos-references/js-apis-notificationextensionsubscription.md#notificationextensionsubscriptionopensubscriptionsettings)接口，打开通知扩展订阅设置页面，引导用户授予获取本机通知的权限，该页面以半模态弹窗显示。建议在设备管理页面提供一个通知授权的按钮，用户点击按钮则调用[openSubscriptionSettings](../harmonyos-references/js-apis-notificationextensionsubscription.md#notificationextensionsubscriptionopensubscriptionsettings)接口。
5. 在应用的module.json5文件中配置extensionAbilities。

   ```
   1. {
   2. "name": "NotificationSubscriberExtAbility",
   3. "srcEntry": "./ets/extensionability/NotificationSubscriberExtAbility.ets",
   4. "type": "notificationSubscriber",
   5. "description": "$string:NotificationSubscriberExtAbility_desc",
   6. "icon": "$media:layered_image",
   7. "label": "$string:NotificationSubscriberExtAbility_label",
   8. "exported": true
   9. }
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/ThirdpartyWerableDemo/entry/src/main/module.json5#L63-L73)
6. 在应用的string.json文件中添加

   ```
   1. {
   2. "name": "NotificationSubscriberExtAbility_desc",
   3. "value": "description"
   4. },
   5. {
   6. "name": "NotificationSubscriberExtAbility_label",
   7. "value": "ThirdPartyWearableApp"
   8. }
   ```

## 传统蓝牙连接示例

1. 示例仅为传统蓝牙连接示例，开发者也可选用低功耗蓝牙连接方式。
2. 用户收到消息后，假如蓝牙连接是无效的，则建立蓝牙连接。
3. 假如蓝牙连接已经存在，则直接使用这个连接发送消息。
4. 如果使用该连接发送消息失败，则重新建立连接，如果连接能建立成功则发送消息。
5. 需要申请权限ohos.permission.ACCESS\_BLUETOOTH。如何配置和申请权限，具体操作请参考[声明权限](declare-permissions.md)和[向用户申请授权](request-user-authorization.md)。

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';
   2. import { notificationExtensionSubscription, NotificationSubscriberExtensionAbility } from '@kit.NotificationKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { socket } from '@kit.ConnectivityKit'
   5. import { util } from '@kit.ArkTS';

   7. const DOMAIN = 0x0000;
   8. class TransferInfo {
   9. public type: string = ''
   10. public info: notificationExtensionSubscription.NotificationInfo | undefined
   11. public cancelHashCodes: Array<string> | undefined
   12. }
   13. // Spp means Serial Port Profile
   14. class SppClientManager {
   15. private clientNumber: number = -1;
   16. private peerDevice: string = '';

   18. constructor(peerDevice: string) {
   19. this.peerDevice = peerDevice
   20. }

   22. public isConnect(): boolean {
   23. return this.clientNumber !== -1;
   24. }

   26. public async startConnect(): Promise<boolean> {
   27. let option: socket.SppOptions = {
   28. uuid: '00009999-0000-1000-8000-00805F9B34FB',
   29. secure: false,
   30. type: socket.SppType.SPP_RFCOMM
   31. };
   32. socket.sppConnect(this.peerDevice, option, (err: BusinessError, num: number) => {
   33. if (err) {
   34. hilog.error(DOMAIN, 'testTag', `cpp connect failed, errCode: ${err.code}, errMessage: ${err.message}`);
   35. } else {
   36. hilog.info(DOMAIN, 'testTag', `spp connect success clientNumber: ${num}`);
   37. this.clientNumber = num;
   38. }
   39. });
   40. return true
   41. }

   43. private sendData(jsonStr: string) {
   44. if (!this.isConnect()) {
   45. hilog.error(DOMAIN, 'testTag', `server is not connected`);
   46. return;
   47. }
   48. if (!jsonStr) {
   49. hilog.error(DOMAIN, 'testTag', 'json is empty');
   50. return;
   51. }
   52. hilog.info(DOMAIN, 'testTag', `prepare sending data to client ${this.clientNumber}`);
   53. const textEncoder:util.TextEncoder = new util.TextEncoder();
   54. const uint8Array: Uint8Array = textEncoder.encodeInto(jsonStr);
   55. const arrayBuffer = uint8Array.buffer;

   57. socket.sppWrite(this.clientNumber, arrayBuffer);
   58. hilog.info(DOMAIN, 'testTag', `sending success size: ${arrayBuffer.byteLength} bytes, data: ${jsonStr}`);
   59. }

   61. public sendNotificationData(notificationInfo: notificationExtensionSubscription.NotificationInfo) {
   62. let info: TransferInfo = {
   63. type: 'publish',
   64. info: notificationInfo,
   65. cancelHashCodes: undefined
   66. };

   68. let jsonStr = JSON.stringify(info);
   69. this.sendData(jsonStr);
   70. }

   72. public sendCancelNotificationData(cancelHashCodes: Array<string>) {
   73. let info: TransferInfo = {
   74. type: 'cancel',
   75. cancelHashCodes: cancelHashCodes,
   76. info: undefined
   77. };

   79. let jsonStr = JSON.stringify(info);
   80. this.sendData(jsonStr);
   81. }

   83. public read = (dataBuffer: ArrayBuffer) => {
   84. let data = new Uint8Array(dataBuffer);
   85. hilog.info(DOMAIN, 'testTag', `client data: ${JSON.stringify(data)}`);
   86. };

   88. public stopConnect() {
   89. hilog.info(DOMAIN, 'testTag', `closeSppClient ${this.clientNumber}`);
   90. try {
   91. socket.off('sppRead', this.clientNumber, this.read);
   92. } catch (err) {
   93. hilog.error(DOMAIN, 'testTag', `off sppRead errCode: ${err.code}, errMessage: ${err.message}`);
   94. }
   95. try {
   96. socket.sppCloseClientSocket(this.clientNumber);
   97. this.clientNumber = -1;
   98. } catch (err) {
   99. hilog.error(DOMAIN, 'testTag', `stopConnect errCode: ${err.code}, errMessage: ${err.message}`);
   100. }
   101. }
   102. }

   104. // export SppClientManager;
   105. export class NotificationSubscriberExtAbility extends NotificationSubscriberExtensionAbility {
   106. private sppClientManager: SppClientManager | undefined;
   107. onDestroy(): void {
   108. hilog.info(DOMAIN, 'testTag', 'onDestroy');
   109. this.sppClientManager!.stopConnect();
   110. }
   111. // Called back when a notification is published.
   112. onReceiveMessage(notificationInfo: notificationExtensionSubscription.NotificationInfo): void {
   113. hilog.info(DOMAIN, 'testTag', `on receive message ${JSON.stringify(notificationInfo)}`)
   114. notificationExtensionSubscription.getSubscribeInfo()
   115. .then(async (info) => {
   116. if (this.sppClientManager == undefined) {
   117. this.sppClientManager = new SppClientManager(info[0].addr);
   118. }
   119. if (this.sppClientManager.isConnect()) {
   120. this.sendPublishWithRetry(notificationInfo);
   121. } else {
   122. try {
   123. await this.sppClientManager.startConnect().then(() => {
   124. hilog.info(DOMAIN, 'testTag', `startConnect success`);
   125. });
   126. } catch (err) {
   127. hilog.error(DOMAIN, 'testTag', `Failed to start connect: ${JSON.stringify(err)}`);
   128. }
   129. setTimeout(() => {
   130. this.sendPublishWithRetry(notificationInfo);
   131. }, 3000)
   132. }
   133. }).catch((err: BusinessError) => {
   134. hilog.error(DOMAIN, 'testTag',
   135. `notificationExtensionSubscription failed, errCode ${err.code}, errorMessage ${err.message}`);
   136. });
   137. }
   138. // Sends a publish notification and retries once upon failure.
   139. private async sendPublishWithRetry(notificationInfo: notificationExtensionSubscription.NotificationInfo) {
   140. try {
   141. this.sppClientManager!.sendNotificationData(notificationInfo);
   142. } catch (err) {
   143. hilog.error(DOMAIN, 'testTag', `send failed, errCode ${err.code}, errorMessage ${err.message}, and retry one times`);
   144. try {
   145. await this.sppClientManager!.startConnect().then(() => {
   146. hilog.info(DOMAIN, 'testTag', `startConnect success`);
   147. });
   148. } catch (err) {
   149. hilog.error(DOMAIN, 'testTag', `Failed to start connect: ${JSON.stringify(err)}`);
   150. }
   151. setTimeout(() => {
   152. this.sppClientManager!.sendNotificationData(notificationInfo);
   153. }, 3000);
   154. }
   155. }

   157. // Called back when notifications are cancelled.
   158. onCancelMessages(hashCodes: Array<string>): void {
   159. hilog.info(DOMAIN, 'testTag', `on cancel message ${JSON.stringify(hashCodes)}`)
   160. notificationExtensionSubscription.getSubscribeInfo()
   161. .then(async (info) => {
   162. if (this.sppClientManager == undefined) {
   163. this.sppClientManager = new SppClientManager(info[0].addr);
   164. }
   165. if (this.sppClientManager.isConnect()) {
   166. this.sendCancelWithRetry(hashCodes);
   167. } else {
   168. try {
   169. await this.sppClientManager.startConnect().then(() => {
   170. hilog.info(DOMAIN, 'testTag', `startConnect success`);
   171. });
   172. } catch (err) {
   173. hilog.error(DOMAIN, 'testTag', `Failed to start connect: ${JSON.stringify(err)}`);
   174. }
   175. setTimeout(() => {
   176. this.sendCancelWithRetry(hashCodes);
   177. }, 3000)
   178. }
   179. }).catch((err: BusinessError) => {
   180. hilog.error(DOMAIN, 'testTag', `notificationExtensionSubscription failed, errCode ${err.code}, errorMessage ${err.message}`);
   181. });
   182. }
   183. // Retries a cancel operation if it fails.
   184. private async sendCancelWithRetry(hashCodes: string[]) {
   185. try {
   186. this.sppClientManager!.sendCancelNotificationData(hashCodes);
   187. } catch (err) {
   188. hilog.error(DOMAIN, 'testTag', `send failed, errCode ${err.code}, errorMessage ${err.message}, and retry one times`);
   189. try {
   190. await this.sppClientManager!.startConnect().then(() => {
   191. hilog.info(DOMAIN, 'testTag', `startConnect success`);
   192. });
   193. } catch (err) {
   194. hilog.error(DOMAIN, 'testTag', `Failed to start connect: ${JSON.stringify(err)}`);
   195. }
   196. setTimeout(() => {
   197. this.sppClientManager!.sendCancelNotificationData(hashCodes);
   198. }, 3000);
   199. }
   200. }
   201. }
   ```

   [NotificationSubscriberExtAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Notification-Kit/ThirdpartyWerableDemo/entry/src/main/ets/extensionability/NotificationSubscriberExtAbility.ets#L16-L238)

注意：请勿频繁建立连接，可能会影响功能。
