---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-wear-engine-3
title: 如何实现手机向智能手表发送模板通知
breadcrumb: FAQ > 系统开发 > 硬件 > 穿戴服务（Wear Engine Kit） > 如何实现手机向智能手表发送模板通知
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:f47a95f89d6e8f072bb01a9ce25c9e7a48ecf4cad5dddf6c9661e41ae326bf5b
---

## 问题现象

手机应用主动向穿戴设备推送模板通知，如何实现？

## 背景知识

* Wear Engine聚焦华为穿戴设备能力开放，目前提供了应用间消息通信（设备基础能力）等能力，参考：[开放能力](../harmonyos-guides/we-business_introduction.md#开放能力)。
* 接入前需要[申请接入Wear Engine服务](../harmonyos-guides/wearengine_apply.md)和[配置Client ID](../harmonyos-guides/configuration_client_id.md)。
* [notify](../harmonyos-references/wearengine_api.md#notify)：向穿戴设备发送模板化通知。

## 解决方案

获取已连接设备列表，从已连接设备列表中选定需要通信的设备，调用[wearEngine.getNotifyClient](../harmonyos-references/wearengine_api.md#wearenginegetnotifyclient)方法，获取[NotifyClient](../harmonyos-references/wearengine_api.md#notifyclient)对象并定义[NotificationOptions](../harmonyos-references/wearengine_api.md#notificationoptions)配置参数类，调用[notify](../harmonyos-references/wearengine_api.md#notify)方法，从手机上的应用发送通知到智能手表侧。

完整的代码示例如下：

```ts
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';
import { promptAction } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('发送模板化通知')
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

              if (deviceList.length > 0) {
                // 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备且第一位即为目标设备)
                let targetDevice: wearEngine.Device = deviceList[0];

                // 获取NotifyClient对象
                let notifyClient: wearEngine.NotifyClient =
                  wearEngine.getNotifyClient(this.getUIContext().getHostContext());

                // 构造NotificationOptions对象
                let button1: wearEngine.NotificationButton = {
                  buttonId: wearEngine.ButtonId.FIRST_BUTTON,
                  // 按钮内容最大长度为12字节
                  content: '取消'
                };
                let button2: wearEngine.NotificationButton = {
                  buttonId: wearEngine.ButtonId.SECOND_BUTTON,
                  // 按钮内容最大长度为12字节
                  content: '确认'
                };
                let type1Notification: wearEngine.Notification = {
                  type: wearEngine.NotificationType.NOTIFICATION_WITH_TWO_BUTTONS,
                  // 包名与标题的最大长度为28字节
                  bundleName: 'bundleName',
                  title: '模板通知',
                  // 消息内容最大长度为400字节
                  text: '来自手机端的模板通知',
                  buttons: [button1, button2]
                };
                let options: wearEngine.NotificationOptions = {
                  notification: type1Notification,
                  onAction: (feedback: wearEngine.NotificationFeedback) => {
                    console.info(`one button notify get feedback is ${feedback.action ? feedback.action :
                      feedback.errorCode}`);
                  }
                };

                // 发送模板化通知至设备侧
                notifyClient.notify(targetDevice.randomId, options).then(result => {
                  console.info(`Succeeded in sending notification. Result is ${result}`);
                  this.getUIContext().getPromptAction().showToast({
                    message: `Succeeded in sending notification`,
                    duration: 2000,
                    showMode: promptAction.ToastShowMode.DEFAULT,
                    bottom: 80
                  });
                }).catch((error: BusinessError) => {
                  console.error(`Failed to send notification. Code is ${error.code}, message is ${error.message}`);
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
