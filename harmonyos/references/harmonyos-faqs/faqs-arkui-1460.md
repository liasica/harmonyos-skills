---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1460
title: TextInput组件中如何实现点击输入框弹出Popup气泡，选中内容时关闭Popup
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > TextInput组件中如何实现点击输入框弹出Popup气泡，选中内容时关闭Popup
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e6f1350a58dc246f1bc5f963f58d624876d8af6e509ddadc14f94d88e975149d
---

## 问题现象

使用TextInput组件时，如何实现编辑状态打开Popup且使用键盘输入不关闭，点击Popup气泡中内容并填充至TextInput中时，关闭Popup？

## 背景知识

* [TextInput](../harmonyos-references/ts-basic-components-textinput.md)：TextInput是输入框组件，用于响应用户输入，比如评论区的输入、聊天框的输入、表格的输入等，也可以结合其它组件构建功能页面，例如登录注册页面。具体用法请参考[TextInput](../harmonyos-references/ts-basic-components-textinput.md)。
* [onEditChange](../harmonyos-references/ts-basic-components-textinput.md#oneditchange8)：输入状态变化时，触发该回调。有光标时为编辑态，无光标时为非编辑态。
* [Popup](../harmonyos-guides/arkts-popup-and-menu-components-popup.md)：Popup属性可绑定在组件上显示气泡弹窗提示，设置弹窗内容、交互逻辑和显示状态。主要用于屏幕录制、信息弹出提醒等显示状态。
* [使用Emitter进行线程间通信](../harmonyos-guides/itc-with-emitter.md)：Emitter是一种作用在进程内的事件处理机制，为应用程序提供订阅事件、发布事件、取消事件订阅的能力。

## 解决方案

* 在TextInput的onEditChange事件中进行判断，处于编辑状态时，Popup弹出，退出编辑状态时，Popup关闭。
* 使用Emitter订阅事件，当点击Popup中的值时，给message进行赋值并且关闭Popup，退出TextInput的编辑状态。

运行效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/3OYxNvWuTM2DHEvzli7hSQ/zh-cn_image_0000002658964561.png "点击放大")

完整示例参考如下：

```ts
import { emitter } from '@kit.BasicServicesKit';

@Entry
@Component
struct bindPopupDemo {
  @State message: string = '';
  @State customPopup: boolean = false;
  controller: TextInputController = new TextInputController();
  // 定义一个eventId为1的事件，事件优先级为Low。
  private event: emitter.InnerEvent = {
    eventId: 1,
    priority: emitter.EventPriority.LOW
  };

  aboutToAppear(): void {
    // 收到eventId为1的事件后执行回调函数。
    emitter.on(this.event, data => {
      this.message = data.data!['message'];
      this.customPopup = false;
      this.controller.stopEditing();
    });
  };

  aboutToDisappear(): void {
    // 取消eventId为1的事件。
    emitter.off(this.event.eventId);
  };

  @Builder
  popupBuilder() {
    Column({ space: 2 }) {
      Text('内容一')
        .fontSize(20)
        .onClick(() => {
          let eventData: emitter.EventData = {
            data: {
              message: '内容一'
            }
          };
          // 发送eventId为1的事件，事件内容为eventData。
          emitter.emit(this.event, eventData);
        })
        .margin({
          left: 24,
          right: 24,
          bottom: 8,
          top: 8
        });
      Text('内容二').fontSize(20).onClick(() => {
        let eventData: emitter.EventData = {
          data: {
            message: '内容二'
          }
        };
        emitter.emit(this.event, eventData);
      })
        .margin({
          left: 24,
          right: 24,
          bottom: 8,
          top: 8
        });
    }
    .padding(5)
    .alignItems(HorizontalAlign.Center)
  };

  build() {
    Row() {
      TextInput({ text: this.message, placeholder: '请输入正确内容', controller: this.controller })
        .layoutWeight(1)
        .enableAutoFill(false)
        .alignSelf(ItemAlign.Center)
        // 实现气泡弹窗。
        .bindPopup(this.customPopup, {
          builder: this.popupBuilder,
          placement: Placement.BottomLeft,
          mask: false,
          backgroundBlurStyle: BlurStyle.NONE,
          enableArrow: false,
          autoCancel: true,
          showInSubWindow: false,
          targetSpace: 15
        })
        // 当输入框编辑态改变时，处于编辑态时气泡出现。
        .onEditChange((isEditing: boolean) => {
          this.customPopup = isEditing;
        })
        .onChange((value: string) => {
          this.message = value;
        })
        .margin({ left: 16, right: 16 });
    }.alignItems(VerticalAlign.Top)
    .width('100%')
    .height('100%');
  };
}
```
