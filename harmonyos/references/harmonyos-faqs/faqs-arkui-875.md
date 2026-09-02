---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-875
title: 应用每输入一个字符软键盘就会收起
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 应用每输入一个字符软键盘就会收起
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1a7e5669a8a41cd1aa2cce5ea1b2e12da3106dd8827aadddcf6b1910c58894e5
---

## 问题现象

应用在输入框每输入一个字符后，软键盘都会收起，需要再次点击输入框才可以拉起软键盘重新输入。

## 背景知识

* [TextInput](../harmonyos-references/ts-basic-components-textinput.md)：文本输入框组件。
* [stopInputSession](../harmonyos-references/js-apis-inputmethod.md#stopinputsession9)：结束输入会话。

## 问题定位

1. 通过关键词“包名”过滤日志，出现多次焦点更新日志，部分如下所示：

   ```screen
   23873: 10-26 17:51:07.502  3240  3527 I C04207/com.ohos.sceneboard/WMSFocus: [] NotifyFocusStatus(4964): name: com.hm.example/EntryAbility/xxxx0, id: 1364, isFocused: 1
   23888: 10-26 17:51:07.504 38016 38066 I C04207/com.hm.example/WMSFocus: [] UpdateFocus(912): Report update focus: 1, id: 1364
   ```
2. 通过如下代码可复现问题现象：

   ```screen
   @Entry
   @Component
   struct CalculateInput {
   @State inputValue: string = '';
   controller: TextInputController = new TextInputController();

   build() {
       Column() {
       Row() {
           Text("现象复现：")
           .width('30%')
           TextInput({ text: this.inputValue, controller: this.controller })
           .onChange((value:string) => {
               this.inputValue = value;
               this.controller.stopEditing()
           })
           .width('70%')
           .type(InputType.Number)
       }
       .padding(15)
       }
       .height('100%')
       .width('100%')
   }
   }
   ```

   效果：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/A5x0MhWARjKMQ-PvWJ7R-A/zh-cn_image_0000002658798193.png "点击放大")
3. 排查业务代码中是否存在输入值变化时进行stopEditing函数调用。
4. 排查业务代码中是否存在输入值变化时设置输入框失去焦点。

## 分析结论

应用在输入过程中每个字符的变化都会退出编辑状态，从而导致每次只能输入一个字符键盘都会收起。

## 修改建议

使用输入法框架的结束输入会话能力在点击非输入框时，退出编辑能力，且收起输入法。参考代码：

```screen
import { inputMethod } from '@kit.IMEKit';

@Entry
@Component
struct CalculateInput {
  @State inputValue: string = '';
  controller: TextInputController = new TextInputController();

  build() {
    Column() {
      TextInput({ text: this.inputValue, controller: this.controller })
        .onChange((value: string) => {
          this.inputValue = value;
        })
        .width('100%')
        .type(InputType.Number)
        .backgroundColor('#FFFFFF');
    }
    .onClick(() => {
      inputMethod.getController().stopInputSession();
    })
    .height('100%')
    .width('100%')
    .padding({
      left: 16,
      right: 16,
      top: 40,
      bottom: 28
    })
    .backgroundColor('#F1F3F5');
  }
}
```
