---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1412
title: TextInput、RichEditor、TextArea避让软键盘
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > TextInput、RichEditor、TextArea避让软键盘
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7fea39e7b4dd0773c58387f7b77f5b996489c6a48037afccfd0a5618a74edcf7
---

## 问题现象

点击输入框TextInput拉起软键盘后，TextInput下方的组件会被覆盖。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/ffCc_9KLTN-YPqcaJ58xaQ/zh-cn_image_0000002658842533.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/EvSbDh1ZQ-Ov-nMkySWfkg/zh-cn_image_0000002628763168.png "点击放大")

## 背景知识

* [安全区域](../harmonyos-references/ts-universal-attributes-expand-safe-area.md)：安全区域是指页面的显示区域，默认不与系统设置的非安全区域比如状态栏、导航栏区域重叠。键盘避让区属于安全区域的一种，即键盘弹出所占区域。
* [@ohos.window (窗口)](../harmonyos-references/arkts-apis-window.md)：提供管理窗口的一些基础能力，包括对当前窗口的创建、销毁、各属性设置，以及对各窗口间的管理调度。可以通过[on('keyboardHeightChange')](../harmonyos-references/arkts-apis-window-window.md#onkeyboardheightchange7)监听键盘高度变化事件。

## 解决方案

TextInput、RichEditor、TextArea避让方案相同，以下以TextInput为例：

唤起软键盘时，系统会自动向上移动页面让输入框TextInput位于键盘避让区的上方，但TextInput下方的组件会被遮挡，所以需要监听键盘高度变化，自行控制页面向上偏移的距离。

1. 关闭页面对键盘的自动避让，避免键盘避让区对计算页面偏移距离的影响。
2. 设置状态变量offsetNum，用来控制组件向上偏移的距离。
3. 使用window.on('keyboardHeightChange', callback)监听键盘高度变化，在键盘弹出和收起时高度变化均会触发回调，在回调函数中改变状态变量offsetNum的数值。
4. 使用offset()设置页面向上指定offsetNum。

代码Demo如下：在键盘弹出时，整个页面向上偏移，偏移量为键盘弹出的高度。

```ts
import window from '@ohos.window';
import { KeyboardAvoidMode } from '@kit.ArkUI';

@Entry
@Component
struct KeyboardAvoidDemo {
  @State text: string = '';
  controller: TextInputController = new TextInputController();
  @State offsetNum: number = 0;

  onPageShow(): void {
    // 获取当前窗口实例
    window.getLastWindow(this.getUIContext().getHostContext()).then((curWindow) => {
      try {
        curWindow.getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.NONE); // 关闭当前页面对键盘的自动避让
        // 监听键盘高度变化，返回键盘高度，单位为像素px
        curWindow.on('keyboardHeightChange', (height) => {
          // 在键盘高度变化时改变状态变量offsetNum
          if (height > 0) {
            this.getUIContext().animateTo({
              duration: 200,
              curve: Curve.Smooth
            }, () => {
              this.offsetNum = this.getUIContext().px2vp(height); // 页面向上偏移的距离为键盘的高度
            });
          } else {
            this.getUIContext().animateTo({
              duration: 200,
              curve: Curve.Smooth
            }, () => {
              this.offsetNum = 0; // height为0说明键盘收起
            });
          }
          console.info(`Succeeded in enabling the listener for keyboard height changes. Data: ${height}`);
        });
      } catch (exception) {
        console.error(`Failed to listen keyboard height. Cause: ${exception.code}, message: ${exception.message}`);
      }
    }).catch((err: string) => {
      console.error(`setWindowOrientation： Failed to obtain the top window. Cause: ${err}`);
    });
  }

  build() {
    Column() {
      Row() {
      }
      .width('100%')
      .height(550);

      Column() {
        Text('这是一个文本组件text1，和输入框同层级');
        TextInput({ text: this.text, controller: this.controller, placeholder: '请输入内容' })
          .placeholderFont({ size: 16, weight: 400 })
          .width('90%')
          .onChange((value: string) => {
            this.text = value;
          });
        Text('这是一个文本组件text2，和输入框同层级');
      }
      .justifyContent(FlexAlign.SpaceAround)
      .height('600px');

      Text('这是一个文本组件text3')
        .width('100%')
        .textAlign(TextAlign.Center);
    }
    .width('100%')
    .height('100%')
    .offset({
      bottom: this.offsetNum // 相对于页面底部偏移
    });
  }
}
```
