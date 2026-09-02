---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-subscriber-extension-ability-development-steps
title: 通知订阅扩展能力开发步骤
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 通知订阅扩展能力 > 通知订阅扩展能力开发步骤
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:36e73d52e62ee1c57babc28fa140cdca852e307de5565d954c5efecb26f4e5db
---

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [onDestroy(): void](../harmonyos-references/js-apis-notificationsubscriberextensionability.md#ondestroy) | [通知订阅](notification-glossary.md#notification-subscription通知订阅)扩展被销毁时的回调。 |
| [onReceiveMessage(notificationInfo: NotificationInfo): void](../harmonyos-references/js-apis-notificationsubscriberextensionability.md#onreceivemessage) | 收到通知时的回调。 |
| [onCancelMessages(hashCodes: Array<string>): void](../harmonyos-references/js-apis-notificationsubscriberextensionability.md#oncancelmessages) | 取消通知时的回调。 |

## 前提条件

申请[ohos.permission.SUBSCRIBE\_NOTIFICATION](restricted-permissions.md#ohospermissionsubscribe_notification)权限。

## 开发步骤

开发者在实现[NotificationSubscriberExtensionAbility](../harmonyos-references/js-apis-notificationsubscriberextensionability.md)提供方时，需在[DevEco Studio](ide-tools-overview.md)工程中新建一个NotificationSubscriberExtensionAbility。具体步骤如下。

1. 在entry/src/main/ets/创建目录extensionability。
2. 在entry/src/main/ets/extensionability目录下创建NotificationSubscriberExtAbility.ets，其内容如下。

   ```typescript
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { notificationExtensionSubscription, NotificationSubscriberExtensionAbility } from '@kit.NotificationKit';
   // ...

   const DOMAIN = 0x0000;
   // ...
   export class NotificationSubscriberExtAbility extends NotificationSubscriberExtensionAbility {
     // ...
     onDestroy(): void {
       hilog.info(DOMAIN, 'testTag', 'onDestroy');
       // ...
     }
     // ...
     onReceiveMessage(notificationInfo: notificationExtensionSubscription.NotificationInfo): void {
       hilog.info(DOMAIN, 'testTag', `on receive message ${JSON.stringify(notificationInfo)}`)
       // ...
     }
     // ...
     onCancelMessages(hashCodes: Array<string>): void {
       hilog.info(DOMAIN, 'testTag', `on cancel message ${JSON.stringify(hashCodes)}`)
       // ...
     }
     // ...
   }
   ```
3. 使用[蓝牙模块](connectivity-kit-intro.md#蓝牙简介)接口与穿戴设备配对（蓝牙处于配对状态）并获取地址，然后通过[subscribe](../harmonyos-references/js-apis-notificationextensionsubscription.md#notificationextensionsubscriptionsubscribe)/[unsubscribe](../harmonyos-references/js-apis-notificationextensionsubscription.md#notificationextensionsubscriptionunsubscribe)接口订阅或取消订阅通知。
4. 实现[NotificationSubscriberExtensionAbility](../harmonyos-references/js-apis-notificationsubscriberextensionability.md)后，还需要在合适的时机调用[openSubscriptionSettingsWithResult](../harmonyos-references/js-apis-notificationextensionsubscription.md#notificationextensionsubscriptionopensubscriptionsettingswithresult)接口，打开通知扩展订阅设置页面，引导用户授予获取本机通知的权限，该页面以半模态弹窗显示，并在弹窗关闭时返回授权的结果。建议在设备管理页面提供一个[通知授权](notification-glossary.md#notification-authorization通知授权)的按钮，用户点击按钮则调用[openSubscriptionSettingsWithResult](../harmonyos-references/js-apis-notificationextensionsubscription.md#notificationextensionsubscriptionopensubscriptionsettingswithresult)接口。
5. 在应用的module.json5文件中配置extensionAbilities。

   ```json5
   {
     "name": "NotificationSubscriberExtAbility",
     "srcEntry": "./ets/extensionability/NotificationSubscriberExtAbility.ets",
     "type": "notificationSubscriber",
     "description": "$string:NotificationSubscriberExtAbility_desc",
     "icon": "$media:layered_image",
     "label": "$string:NotificationSubscriberExtAbility_label",
     "exported": true
   }
   ```
6. 在应用的string.json文件中添加

   ```json
   [
     {
       "name": "NotificationSubscriberExtAbility_desc",
       "value": "description"
     },
     {
       "name": "NotificationSubscriberExtAbility_label",
       "value": "ThirdPartyWearableApp"
     }
   ]
   ```
7. 示例仅为传统蓝牙连接示例，开发者也可选用低功耗蓝牙连接方式。
8. 用户收到消息后，如果蓝牙连接是无效的，则需建立蓝牙连接。
9. 假如蓝牙连接已经存在，则直接使用此连接发送消息。
10. 如果使用该蓝牙连接发送消息失败，则需要重新建立蓝牙连接，连接成功后即可发送消息。
11. 需要申请权限[ohos.permission.ACCESS\_BLUETOOTH](permissions-for-all-user.md#ohospermissionaccess_bluetooth)。如何配置和申请权限，具体操作请参考[声明权限](declare-permissions.md)和[向用户申请授权](request-user-authorization.md)。

    ```typescript
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { notificationExtensionSubscription, NotificationSubscriberExtensionAbility } from '@kit.NotificationKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { socket } from '@kit.ConnectivityKit'
    import { util } from '@kit.ArkTS';

    const DOMAIN = 0x0000;
    class TransferInfo {
      public type: string = ''
      public info: notificationExtensionSubscription.NotificationInfo | undefined
      public cancelHashCodes: Array<string> | undefined
    }
    // Spp means Serial Port Profile
    class SppClientManager {
      private clientNumber: number = -1;
      private peerDevice: string = '';
      private connectPromise: Promise<boolean> | null = null;

      constructor(peerDevice: string) {
        this.peerDevice = peerDevice
      }

      public isConnect(): boolean {
        return this.clientNumber !== -1;
      }

      public startConnect(): Promise<boolean> {
        if (this.isConnect()) {
          return Promise.resolve(true);
        }
        if (this.connectPromise) {
          return this.connectPromise;
        }
        this.connectPromise = new Promise((resolve) => {
          let option: socket.SppOptions = {
            uuid: '00009999-0000-1000-8000-00805F9B34FB', // UUID of the server to connect to, ensure server support
            secure: false,
            type: socket.SppType.SPP_RFCOMM
          };
          socket.sppConnect(this.peerDevice, option, (err: BusinessError, num: number) => {
            this.connectPromise = null;
            if (err) {
              hilog.error(DOMAIN, 'testTag', `cpp connect failed, errCode: ${err.code}, errMessage: ${err.message}`);
              resolve(false);
            } else {
              hilog.info(DOMAIN, 'testTag', `spp connect success clientNumber: ${num}`);
              this.clientNumber = num;
              socket.on('sppRead', this.clientNumber, this.read);
              resolve(true);
            }
          });
        });
        return this.connectPromise;
      }

      private sendData(jsonStr: string) {
        if (!this.isConnect()) {
          hilog.error(DOMAIN, 'testTag', `server is not connected`);
          return;
        }
        if (!jsonStr) {
          hilog.error(DOMAIN, 'testTag', 'json is empty');
          return;
        }
        hilog.info(DOMAIN, 'testTag', `prepare sending data to client ${this.clientNumber}`);
        const textEncoder:util.TextEncoder = new util.TextEncoder();
        const uint8Array: Uint8Array = textEncoder.encodeInto(jsonStr);
        const arrayBuffer = uint8Array.buffer;

        socket.sppWrite(this.clientNumber, arrayBuffer);
        hilog.info(DOMAIN, 'testTag', `sending success size: ${arrayBuffer.byteLength} bytes, data: ${jsonStr}`);
      }

      public sendNotificationData(notificationInfo: notificationExtensionSubscription.NotificationInfo) {
        let info: TransferInfo = {
          type: 'publish',
          info: notificationInfo,
          cancelHashCodes: undefined
        };

        let jsonStr = JSON.stringify(info);
        this.sendData(jsonStr);
      }

      public sendCancelNotificationData(cancelHashCodes: Array<string>) {
        let info: TransferInfo = {
          type: 'cancel',
          cancelHashCodes: cancelHashCodes,
          info: undefined
        };

        let jsonStr = JSON.stringify(info);
        this.sendData(jsonStr);
      }

      public read = (dataBuffer: ArrayBuffer) => {
        let data = new Uint8Array(dataBuffer);
        hilog.info(DOMAIN, 'testTag', `client data: ${JSON.stringify(data)}`);
      };

      public stopConnect() {
        hilog.info(DOMAIN, 'testTag', `closeSppClient ${this.clientNumber}`);
        this.connectPromise = null;
        try {
          socket.off('sppRead', this.clientNumber, this.read);
        } catch (err) {
          hilog.error(DOMAIN, 'testTag', `off sppRead errCode: ${err.code}, errMessage: ${err.message}`);
        }
        try {
          socket.sppCloseClientSocket(this.clientNumber);
        } catch (err) {
          hilog.error(DOMAIN, 'testTag', `stopConnect errCode: ${err.code}, errMessage: ${err.message}`);
        }
        this.clientNumber = -1;
      }
    }

    // export SppClientManager;
    export class NotificationSubscriberExtAbility extends NotificationSubscriberExtensionAbility {
      private sppClientManager: SppClientManager | undefined;
      onDestroy(): void {
        hilog.info(DOMAIN, 'testTag', 'onDestroy');
        this.sppClientManager?.stopConnect();
      }
      // Called back when a notification is published.
      onReceiveMessage(notificationInfo: notificationExtensionSubscription.NotificationInfo): void {
        hilog.info(DOMAIN, 'testTag', `on receive message ${JSON.stringify(notificationInfo)}`)
        notificationExtensionSubscription.getSubscribeInfo()
          .then(async (info) => {
            if (this.sppClientManager == undefined) {
              this.sppClientManager = new SppClientManager(info[0].addr);
            }
            if (this.sppClientManager.isConnect()) {
              this.sendPublishWithRetry(notificationInfo);
            } else {
              let connected = await this.sppClientManager.startConnect();
              if (connected) {
                this.sendPublishWithRetry(notificationInfo);
              } else {
                hilog.error(DOMAIN, 'testTag', `startConnect failed, skip send`);
              }
            }
          }).catch((err: BusinessError) => {
          hilog.error(DOMAIN, 'testTag',
            `notificationExtensionSubscription failed, errCode ${err.code}, errorMessage ${err.message}`);
        });
      }
      // Sends a publish notification and retries once upon failure.
      private async sendPublishWithRetry(notificationInfo: notificationExtensionSubscription.NotificationInfo) {
        try {
          this.sppClientManager!.sendNotificationData(notificationInfo);
        } catch (err) {
          hilog.error(DOMAIN, 'testTag', `send failed, errCode ${err.code}, errorMessage ${err.message}, and retry one times`);
          this.sppClientManager!.stopConnect();
          let connected = await this.sppClientManager!.startConnect();
          if (connected) {
            this.sppClientManager!.sendNotificationData(notificationInfo);
          } else {
            hilog.error(DOMAIN, 'testTag', `retry startConnect failed, skip send`);
          }
        }
      }

      // Called back when notifications are cancelled.
      onCancelMessages(hashCodes: Array<string>): void {
        hilog.info(DOMAIN, 'testTag', `on cancel message ${JSON.stringify(hashCodes)}`)
        notificationExtensionSubscription.getSubscribeInfo()
          .then(async (info) => {
            if (this.sppClientManager == undefined) {
              this.sppClientManager = new SppClientManager(info[0].addr);
            }
            if (this.sppClientManager.isConnect()) {
              this.sendCancelWithRetry(hashCodes);
            } else {
              let connected = await this.sppClientManager.startConnect();
              if (connected) {
                this.sendCancelWithRetry(hashCodes);
              } else {
                hilog.error(DOMAIN, 'testTag', `startConnect failed, skip send`);
              }
            }
          }).catch((err: BusinessError) => {
          hilog.error(DOMAIN, 'testTag', `notificationExtensionSubscription failed, errCode ${err.code}, errorMessage ${err.message}`);
        });
      }
      // Retries a cancel operation if it fails.
      private async sendCancelWithRetry(hashCodes: string[]) {
        try {
          this.sppClientManager!.sendCancelNotificationData(hashCodes);
        } catch (err) {
          hilog.error(DOMAIN, 'testTag', `send failed, errCode ${err.code}, errorMessage ${err.message}, and retry one times`);
          this.sppClientManager!.stopConnect();
          let connected = await this.sppClientManager!.startConnect();
          if (connected) {
            this.sppClientManager!.sendCancelNotificationData(hashCodes);
          } else {
            hilog.error(DOMAIN, 'testTag', `retry startConnect failed, skip send`);
          }
        }
      }
    }
    ```
