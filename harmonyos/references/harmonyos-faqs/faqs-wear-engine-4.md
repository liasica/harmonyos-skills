---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-wear-engine-4
title: 如何实现手机向智能手表发送消息
breadcrumb: FAQ > 系统开发 > 硬件 > 穿戴服务（Wear Engine Kit） > 如何实现手机向智能手表发送消息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-09-02
content_hash: sha256:fbf9081fbeaf335d5a599267ccc4215199b6198f273c8538f7b4897fc9e907c7
---

## 问题现象

手机与智能穿戴设备的互联通信是智能穿戴设备的核心开发场景，如何实现手机向智能手表发送消息？

## 背景知识

* Wear Engine聚焦华为穿戴设备能力开放，目前提供了应用间消息通信（设备基础能力）等能力，参考：[开放能力](../harmonyos-guides/we-business_introduction.md#开放能力)。
* 接入前需要[申请接入Wear Engine服务](../harmonyos-guides/wearengine_apply.md)和[配置Client ID](../harmonyos-guides/configuration_client_id.md)。

## 解决方案

1. 手机端应用使用WearEngine的[sendMessage](../harmonyos-references/wearengine_api.md#sendmessage)接口向智能手表端应用发送消息通知，需配置智能手表端应用的包名与指纹，代码示例如下：

   ```ts
   import { wearEngine } from '@kit.WearEngine';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { util } from '@kit.ArkTS';
   import { promptAction } from '@kit.ArkUI';

   @Entry
   @Component
   struct SendMessageForPhone {
     build() {
       Column() {
         Button('发送消息')
           .onClick(() => {
             // 获取DeviceClient对象
             try {
               let deviceClient: wearEngine.DeviceClient =
                 wearEngine.getDeviceClient(this.getUIContext().getHostContext());
               // 创建一个设备列表用于存储返回的设备
               let deviceList: wearEngine.Device[] = [];

               // 调用getConnectedDevices方法，查询用户是否有已连接的穿戴设备
               deviceClient.getConnectedDevices().then(devices => {
                 // 处理返回的设备列表
                 deviceList = devices;
                 console.info(`Succeeded in getting deviceList, deviceList number is ${deviceList.length}`);

                 if (deviceList.length > 0) {
                   // 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备且第一位即为目标设备)
                   let targetDevice: wearEngine.Device = deviceList[0];
                   console.info(`Succeeded in getting targetDevice, result is ${targetDevice}`);

                   // 构造穿戴设备侧应用参数
                   let appInfo: wearEngine.AppInfo = {
                     // 替换为穿戴设备应用的包名与指纹
                     bundleName: 'XXXX.XXXX.XXXX',
                     fingerprint: 'XXXXXXXXXXXXXXXXXXX'
                   };
                   let appParam: wearEngine.P2pAppParam = {
                     remoteApp: appInfo
                   };

                   // 设置需要发送的消息内容，长度限制为4096字节
                   let messageContent: string = 'this is message from phone';

                   // 构造消息结构体
                   let textEncoder: util.TextEncoder = new util.TextEncoder;
                   let message: wearEngine.P2pMessage = {
                     content: textEncoder.encodeInto(messageContent)
                   };

                   // 获取P2pClient对象
                   let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

                   // 发送消息
                   p2pClient.sendMessage(targetDevice.randomId, appParam, message).then((p2pResult) => {
                     console.info(`Succeeded in sending message, result is ${p2pResult.code}.`);
                     this.getUIContext().getPromptAction().showToast({
                       message: 'Succeeded in sending message',
                       duration: 2000,
                       showMode: promptAction.ToastShowMode.DEFAULT,
                       bottom: 80
                     });
                   }).catch((error: BusinessError) => {
                     console.error(`Failed to send message. Code is ${error.code}, message is ${error.message}.`);
                   });

                 }
               }).catch((error: BusinessError) => {
                 // 处理调用失败时捕获到的异常
                 console.error(`Failed to get deviceList. Code is ${error.code}, message is ${error.message}`);
               });
             } catch (error) {
               console.error(`Failed to get deviceClient. Code is ${error.code}, message is ${error.message}`);
             }

           });
       }.padding(20);
     }
   }
   ```
2. 智能手表端应用通过[registerMessageReceiver](../harmonyos-references/wearengine_api.md#registermessagereceiver)接口订阅接收手机端应用发来的消息，需配置手机端应用的包名与指纹，并在aboutToDisappear中调用[unregisterMessageReceiver](../harmonyos-references/wearengine_api.md#unregistermessagereceiver)方法，取消接收手机端应用发过来的消息，需要传入订阅监听时的同一个回调函数对象。代码示例如下：

   ```ts
   // 在使用Wear Engine服务前，请导入wearEngine与相关模块
   import { wearEngine } from '@kit.WearEngine';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { util } from '@kit.ArkTS';

   @Entry
   @Component
   struct ReceiveMessageforWearable {
     message: string = 'Hello';
     p2pClient?: wearEngine.P2pClient;
     targetDevice?: wearEngine.Device;
     appParam?: wearEngine.P2pAppParam;
     msgCallback = (p2pMessage: wearEngine.P2pMessage) => {
       console.info(`Succeeded in receiving message, the message is ${p2pMessage.content}.`);
       let decoder: util.TextDecoder = util.TextDecoder.create();
       if (canIUse('SystemCapability.Health.WearEngine')) {
         let str: string = decoder.decodeToString(p2pMessage.content);
         console.info(`Succeeded in receiving message, the message is ${str}.`);
         this.getUIContext().getPromptAction().openToast({
           message: 'message: ' + str,
           duration: 2000
         }).catch(() => {
           console.error('Failed to open Toast');
         });
       }
     };

     aboutToAppear(): void {
       try {
         // 获取DeviceClient对象
         let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());

         // 调用getConnectedDevices方法，查询用户是否有已连接的对端设备
         deviceClient.getConnectedDevices().then(devices => {
           console.info(`Succeeded in getting deviceList, deviceList number is ${devices.length}`);
           // 从已连接设备列表中选定需要通信的设备
           if (devices.length > 0) {
             this.targetDevice = devices[0];
             console.info(`Succeeded to get target device.`);

             // 获取P2pClient对象
             this.p2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

             // 构造手机侧应用参数
             let appInfo: wearEngine.AppInfo = {
               // 替换为手机侧的包名与指纹
               bundleName: 'XXXX.XXXX.XXXX',
               fingerprint: 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
             };
             // 将对端应用参数类定义为appParam
             this.appParam = {
               remoteApp: appInfo
             };

             // 订阅监听消息接收事件
             this.p2pClient.registerMessageReceiver(this.targetDevice.randomId, this.appParam, this.msgCallback)
               .then(() => {
                 console.info(`Succeeded in registering message receiver.`);
               })
               .catch((error: BusinessError) => {
                 console.error(`Failed to register message receiver. Code is ${error.code}, message is ${error.message}.`);
               });

           } else {
             console.warn(`Failed to get target device. deviceList is empty.`);
           }
         }).catch((error: BusinessError) => {
           // 处理调用失败时捕获到的异常
           console.error(`Failed to get deviceList. Code is ${error.code}, message is ${error.message}`);
         });
       } catch (error) {
         console.error(`Failed to get deviceClient. Code is ${error.code}, message is ${error.message}`);
       }
     }

     aboutToDisappear(): void {
       // 取消订阅监听消息接收事件
       this.p2pClient?.unregisterMessageReceiver(this.targetDevice?.randomId, this.appParam,
         this.msgCallback).catch(() => {
         console.error('Failed to unregister message receiver.');
       });
     }

     build() {
       RelativeContainer() {
         Text(this.message)
           .id('HelloWorld')
           .fontSize($r('app.float.page_text_font_size'))
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           });
       }
       .height('100%')
       .width('100%');
     }
   }
   ```

## 常见FAQ

Q：智能手表端应用的fingerprint如何获取？

A：通过命令hdc shell bm dump –n ${BundleName} | findstr appIdentifier获取。

Q：运动表端应用的fingerprint如何获取？

A：参考文档：[获取穿戴设备侧签名证书的指纹信息](../harmonyos-guides/wearengine_faq-9.md)。

Q：手机与智能穿戴设备已连接，发送消息时返回错误码206，如何处理？

A：当手机侧设置了transformLocalAppInfo为true时，通信时对外暴露的是云端存储的兼容包名和指纹，而非手机自身的本地包名和指纹。如果手表侧在发送消息或注册接收时仍使用手机的本地包名作为对端标识，会导致身份不一致，无法通过权限校验，通信失败并返回错误码206。解决方法是在手表侧调用消息发送或注册接收接口时，将对端包名修改为云端存储的兼容包名。更多排查方式可参考[Wear Engine FAQ](../harmonyos-guides/wearengine_faq-6.md)。
