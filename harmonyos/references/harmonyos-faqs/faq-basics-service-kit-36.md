---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-36
title: HarmonyOS如何监听U盘插拔
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > HarmonyOS如何监听U盘插拔
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:64dfe5e1f5887bd67b3292b23693ff728562ffe056e52637553bf4649a07da93
---

## 问题现象

应用需要监听手机是否插入了U盘，HarmonyOS如何监听U盘插拔？

## 背景知识

[公共事件模块](../harmonyos-references/commoneventmanager-definitions.md)提供了公共事件相关的能力，包括发布公共事件、订阅公共事件、以及取消订阅公共事件。U盘插拔事件可以使用此模块来实现订阅和事件处理。

## 解决方案

* 步骤：
  1. 模块导入：

     使用[@ohos.commonEventManager](../harmonyos-references/js-apis-commoneventmanager.md)模块来管理公共事件。导入[BusinessError](../harmonyos-references/js-apis-base.md#businesserror)用于错误处理。
  2. 订阅U盘插拔事件：

     使用commonEventManager.createSubscriber创建订阅者。

     订阅usual.event.usb.action.USB\_STATE事件，监听U盘的插拔状态。
  3. 事件处理：

     在subscribe回调中解析事件参数，判断U盘的状态（connected或disconnected）。

     根据状态调用handleUsbAttached或handleUsbDetached方法。
  4. 取消订阅：

     在不需要监听时，调用commonEventManager.unsubscribe取消订阅。
* 代码实现：

  根据OpenHarmony的文档，U盘插拔的事件名称可能是以下之一：

  | 事件名称 | 描述 |
  | --- | --- |
  | usual.event.hardware.usb.action.USB\_STATE | 表示USB设备状态发生变化的公共事件。 |
  | usual.event.hardware.usb.action.USB\_DEVICE\_ATTACHED | 当用户设备作为USB主机时，USB设备已挂载的公共事件。 |
  | usual.event.hardware.usb.action.USB\_DEVICE\_DETACHED | 当用户设备作为USB主机时，USB设备被卸载的公共事件。 |

* 用USB是否挂载处理监听U盘插拔，代码如下：

  U盘插入事件：usual.event.hardware.usb.action.USB\_DEVICE\_ATTACHED。

  U盘拔出事件：usual.event.hardware.usb.action.USB\_DEVICE\_DETACHED。

  ```screen
  // 定义U盘插拔事件的监听器
  export default class UsbEventListener {
    private subscriber: commonEventManager.CommonEventSubscriber | null = null;

    // 订阅U盘插拔事件
    subscribeUsbEvents() {
      const subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
        events: [
          'usual.event.hardware.usb.action.USB_DEVICE_ATTACHED',
          'usual.event.hardware.usb.action.USB_DEVICE_DETACHED'
        ]
      };
      // 创建订阅者
      commonEventManager.createSubscriber(subscribeInfo,
        (err: BusinessError, subscriber: commonEventManager.CommonEventSubscriber) => {
          if (err) {
            console.error(`Failed to create subscriber. Code: ${err.code}, message: ${err.message}`);
            return;
          }
          this.subscriber = subscriber;
          // 订阅事件
          commonEventManager.subscribe(subscriber, (err: BusinessError, data: commonEventManager.CommonEventData) => {
            if (err) {
              console.error(`Failed to subscribe event. Code: ${err.code}, message: ${err.message}`);
              return;
            }
            console.error(data.event);
            // 获取连接的USB设备信息
            if (data.event === 'usual.event.hardware.usb.action.USB_DEVICE_ATTACHED') {
              console.info('U 盘已插入');
              this.handleUsbAttached();
            } else if (data.event === 'usual.event.hardware.usb.action.USB_DEVICE_DETACHED') {
              console.info('U 盘已拔出');
              this.handleUsbDetached();
            }
          });
        });
    }

    // 处理U盘插入事件
    private handleUsbAttached() {
      console.info('处理 U 盘插入逻辑');
    }

    // 处理U盘拔出事件
    private handleUsbDetached() {
      console.info('处理 U 盘拔出逻辑');
    }

    // 取消订阅
    unsubscribeUsbEvents() {
      if (this.subscriber) {
        commonEventManager.unsubscribe(this.subscriber, (err: BusinessError) => {
          if (err) {
            console.error(`Failed to unsubscribe. Code: ${err.code}, message: ${err.message}`);
            return;
          }
          console.info('已取消订阅 U 盘插拔事件');
        });
      }
    }
  }
  ```

  可运行的Index.ets代码参考如下：

  ```screen
  import { BusinessError } from '@ohos.base';
  import commonEventManager from '@ohos.commonEventManager';

  @Entry
  @Component
  struct Index {
    @State message: string = 'Hello World';
    private usbListener: UsbEventListener = new UsbEventListener();

    aboutToAppear() {
      this.usbListener.subscribeUsbEvents();
    }

    aboutToDisappear() {
      this.usbListener.unsubscribeUsbEvents();
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
          })
          .onClick(() => {
            this.message = 'Welcome';
          })
      }
      .height('100%')
      .width('100%')
    }
  }

  // 定义U盘插拔事件的监听器
  export default class UsbEventListener {
    private subscriber: commonEventManager.CommonEventSubscriber | null = null;

    // 订阅U盘插拔事件
    subscribeUsbEvents() {
      const subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
        events: [
          'usual.event.hardware.usb.action.USB_DEVICE_ATTACHED',
          'usual.event.hardware.usb.action.USB_DEVICE_DETACHED'
        ]
      };
      // 创建订阅者
      commonEventManager.createSubscriber(subscribeInfo,
        (err: BusinessError, subscriber: commonEventManager.CommonEventSubscriber) => {
          if (err) {
            console.error(`Failed to create subscriber. Code: ${err.code}, message: ${err.message}`);
            return;
          }
          this.subscriber = subscriber;
          // 订阅事件
          commonEventManager.subscribe(subscriber, (err: BusinessError, data: commonEventManager.CommonEventData) => {
            if (err) {
              console.error(`Failed to subscribe event. Code: ${err.code}, message: ${err.message}`);
              return;
            }
            console.error(data.event);
            // 获取连接的USB设备信息
            if (data.event === 'usual.event.hardware.usb.action.USB_DEVICE_ATTACHED') {
              console.info('U 盘已插入');
              this.handleUsbAttached();
            } else if (data.event === 'usual.event.hardware.usb.action.USB_DEVICE_DETACHED') {
              console.info('U 盘已拔出');
              this.handleUsbDetached();
            }
          });
        });
    }

    // 处理U盘插入事件
    private handleUsbAttached() {
      console.info('处理 U 盘插入逻辑');
    }

    // 处理U盘拔出事件
    private handleUsbDetached() {
      console.info('处理 U 盘拔出逻辑');
    }

    // 取消订阅
    unsubscribeUsbEvents() {
      if (this.subscriber) {
        commonEventManager.unsubscribe(this.subscriber, (err: BusinessError) => {
          if (err) {
            console.error(`Failed to unsubscribe. Code: ${err.code}, message: ${err.message}`);
            return;
          }
          console.info('已取消订阅 U 盘插拔事件');
        });
      }
    }
  }
  ```

## 常见FAQ

Q：如何查看U盘中的文件？

A：手机连接U盘后，打开手机设置，开启otg权限，在系统自带的文件管理应用中可以查看此U盘的文件。

Q：ArkTS感知到USB插入驱动，如何传递给Qt工程，实现消息监听？

A：使用[@ohos.commonEventManager](../harmonyos-references/js-apis-commoneventmanager.md)模块来管理公共事件，监听USB的插入和拔出事件；并通过[Node-API](https://developer.huawei.com/consumer/cn/training/course/slightMooc/C101705084078534051?pathId=101667550095504391)传递给Native侧，实现处理。
