---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1073
title: 如何设置软键盘避让
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何设置软键盘避让
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-07-31
content_hash: sha256:f7a8e1e9a91ff4b2e28438ce64c260b07136aa9536b3543205e148d21027d261
---

## 问题现象

用户与软键盘进行交互时，可能会出现重要信息被软键盘遮挡、软键盘弹出导致布局错位、软键盘弹出导致弹窗过度上抬问题，如何实现软键盘避让，提高用户体验？

## 背景知识

* [软键盘避让模式](../best-practices/bpta-keyboard-layout-adapt.md#section19987195213425)：当用户在输入时，为了确保输入框不会被键盘遮挡，系统提供了避让模式来解决这一问题。可以通过[setKeyboardAvoidMode](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#setkeyboardavoidmode11)控制虚拟键盘抬起时页面的避让模式，键盘抬起时页面避让模式可分为上抬模式、压缩模式，默认采用上抬模式。
* [安全区域](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)：安全区域是指页面的显示区域，默认不与系统设置的非安全区域比如状态栏、导航栏区域重叠，默认情况下开发者开发的界面都被布局在安全区域内。
* [@ohos.window (窗口)](../harmonyos-references/arkts-apis-window.md)：提供管理窗口的一些基础能力，包括对当前窗口的创建、销毁、各属性设置，以及对各窗口间的管理调度。可以通过[on('keyboardHeightChange')](../harmonyos-references/arkts-apis-window-window.md#onkeyboardheightchange7)监听键盘高度变化事件。
* [customKeyboard](../harmonyos-references/ts-basic-components-textinput.md#customkeyboard10)接口用于设置自定义键盘，[KeyboardOptions](../harmonyos-references/ts-basic-components-richeditor.md#keyboardoptions12)接口用于设置自定义键盘是否支持避让功能。

## 解决方案

实现软键盘避让的方式及其适用场景内容如下：

| 实现场景 | 实现方式 | 适用场景 |
| --- | --- | --- |
| 场景一 | 设置避让模式为RESIZE（压缩模式） | 重要信息被软键盘遮挡(如底部操作栏被遮挡) |
| 场景二 | 设置避让模式为OFFSET\_WITH\_CARET或RESIZE\_WITH\_CARET | 多个输入框中切换时触发键盘避让（输入框光标位置发生变化时候也会触发） |
| 场景三 | 组件设置.expandSafeArea([SafeAreaType.KEYBOARD])属性 | 软键盘弹出导致布局错位（如顶部标题被软键盘向上抬） |
| 场景四 | 设置NavDestination的mode为NavDestinationMode.DIALOG弹窗类型，将软键盘避让模式设置为压缩 | 软键盘弹出导致弹窗过度上抬（如自定义弹窗被键盘顶起） |
| 场景五 | 设置KeyboardOptions属性的supportAvoidance字段为true | 自定义软键盘 |
| 场景六 | 使用window.on('keyboardHeightChange', callback)监听键盘高度变化 | 重要信息被软键盘遮挡(如底部操作栏被遮挡) |

* 场景一：若重要信息被软键盘遮挡(如底部操作栏被遮挡)，可以设置软键盘的避让模式为KeyboardAvoidMode.RESIZE（压缩模式），压缩内容区域的高度。
* 场景二：若想在多个输入框中切换时触发键盘避让（输入框光标位置发生变化时候也会触发），可以将键盘避让模式设置为[KeyboardAvoidMode](../harmonyos-references/arkts-apis-uicontext-e.md#keyboardavoidmode11)类型的枚举值OFFSET\_WITH\_CARET或RESIZE\_WITH\_CARET，可以根据需要选择使用OFFSET或RESIZE模式。
* 场景三：若软键盘弹出导致布局错位（如顶部标题被软键盘向上抬），需要给对应的组件设置.expandSafeArea([SafeAreaType.KEYBOARD])属性，使标题组件不避让键盘。
* 场景四：若软键盘弹出导致弹窗过度上抬（如自定义弹窗被键盘顶起），可以参考[页面显示类型](../harmonyos-guides/arkts-navigation-navdestination.md#页面显示类型)中的弹窗类型，通过设置NavDestination的mode为NavDestinationMode.DIALOG弹窗类型，并且将软键盘避让模式设置为压缩模式，具体实现可参考[自定义弹窗被键盘顶起](../best-practices/bpta-keyboard-layout-adapt.md#section381324419328)。
* 场景五：若使用自定义软键盘，则设置KeyboardOptions属性的supportAvoidance字段为true，设置自定义键盘支持避让功能。
* 场景六：若唤起软键盘时，系统会自动向上移动页面让输入组件位于键盘避让区的上方，但输入组件下方的组件会被遮挡，可以通过监听键盘高度变化，自行控制页面向上偏移的距离。

1. 关闭页面对键盘的自动避让，避免键盘避让区对计算页面偏移距离的影响。
2. 设置状态变量offsetNum，用来控制组件向上偏移的距离。
3. 使用window.on('keyboardHeightChange', callback)监听键盘高度变化，在键盘弹出和收起时高度变化均会触发回调，在回调函数中改变状态变量offsetNum的数值。
4. 使用offset()设置页面向上指定offsetNum。

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

   效果如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/fCofdXfdTpmdlkUXp0ZpdQ/zh-cn_image_0000002628407234.png "点击放大")

   * 更多场景案例请参考官网：[软键盘布局适配](../best-practices/bpta-keyboard-layout-adapt.md)、[软键盘适配示例代码](https://gitee.com/harmonyos_samples/keyboard)。

## 常见FAQ

Q：设置软键盘避让模式时报错，报错信息如下所示：

```txt
Property 'RESIZE' does not exist on type 'typeof KeyboardAvoidMode'. <ArkTSCheck>
```

A：需要导入模块KeyboardAvoidMode。

```ts
import { KeyboardAvoidMode } from '@kit.ArkUI';
```

Q：KeyboardAvoidMode的生效范围是什么？

A：生效范围是整个窗口，如果需要在单页面指定特定的KeyboardAvoidMode，可以在aboutToAppear和aboutToDisappear中更改和回退KeyboardAvoidMode的值。
