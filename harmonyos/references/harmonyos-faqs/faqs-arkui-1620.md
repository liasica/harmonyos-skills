---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1620
title: 如何在系统键盘和自定义键盘切换时自动适配输入框的高度
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何在系统键盘和自定义键盘切换时自动适配输入框的高度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5e5554acfb974395c49d5cdbb2557f4ee93224ecb7d0727c24e06c10bd5731be
---

## 问题现象

定义了一个自定义键盘，在系统键盘和自定义键盘之间切换时，如何自动适配输入框的高度？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/svo1muPZSBmARo1q0vm-0Q/zh-cn_image_0000002658976783.png "点击放大")

## 背景知识

* [requestFocus](../harmonyos-references/ts-universal-attributes-focus.md#requestfocus9)：调用requestFocus方法，可以主动让焦点在下一帧渲染时转移到参数指定的组件上。
* [customKeyboard](../harmonyos-references/ts-basic-components-richeditor.md#customkeyboard)：设置自定义键盘。当设置自定义键盘时，输入框激活后不会打开系统输入法，而是加载指定的自定义组件。自定义键盘的高度可以通过自定义组件根节点的height属性设置，宽度不可设置，使用系统默认值。默认在输入控件失去焦点时，关闭自定义键盘。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)：组件区域变化时触发该回调。仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。

## 解决方案

1. 切换键盘时，通过状态变量isCustomKeyBoard切换实现自定义键盘和系统键盘之间的切换。
2. 通过onAreaChange获取RichEditor组件编辑区域变化前后的高度，计算出新增的高度。初次渲染时，不需要移动RichEditor，后续onAreaChange方法触发需计算RichEditor移动距离。
3. 通过translate和animation实现RichEditor组件编辑区域变化时，组件上下移动，解决被键盘遮挡的问题。
4. 点击切换键盘时，重新主动给RichEditor获取焦点。

完整示例参考如下：

```ts
import { KeyboardAvoidMode, window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct RichEditorExample {
  controller: RichEditorController = new RichEditorController();
  // RichEditor需要移动的距离
  @State RichEditorMoveDistance: number = 0;
  // 是否是自定义键盘
  @State isCustomKeyBoard: boolean = false;
  // 是否初次渲染
  @State isInit: boolean = true;

  aboutToAppear(): void {
    // 设置沉浸式
    this.setWindowSystemBarEnable();
    // 设置键盘避让
    this.getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.RESIZE);
  }

  // 设置沉浸式
  setWindowSystemBarEnable(){
    let windowClass: window.Window | undefined = undefined;
    let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
    context.windowStage.getMainWindow((err: BusinessError, data) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      windowClass = data;
      let isLayoutFullScreen = true;
      try {
        // 设置沉浸式模式
        let promise1 = windowClass.setWindowLayoutFullScreen(isLayoutFullScreen);
        Promise.all([promise1]).then(() => {
          console.info('Succeeded in setting the window layout to full-screen mode.');
        }).catch(() => {
          console.error(`Failed to set the window layout to full-screen mode. Cause code: ${err.code}, message: ${err.message}`);
        });
      } catch (exception) {
        console.error(`Failed to set the window layout to full-screen mode. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    });
  }

  @Builder
  CustomKeyboardBuilder() {
    Grid() {
      ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item: number | string) => {
        GridItem() {
          Button(item + '').width(110).fontColor(Color.Black).backgroundColor('#f3f5f7').onClick(() => {
            this.controller.addTextSpan(item + '', {
              offset: this.controller.getCaretOffset(),
              style: { fontColor: Color.Black, fontSize: 30 }
            });
            this.controller.setCaretOffset(this.controller.getCaretOffset() + item.toString().length);
          });
        };
      });
    }.maxCount(3).columnsGap(10).rowsGap(10).padding(10);
  }

  build() {
    Column() {
      Row() {
      }
      .layoutWeight(1)
      .width('100%')
      .backgroundColor('rgba(241, 243, 245, 1)')
      .padding({ bottom: 50 });

      Row() {
        RichEditor({ controller: this.controller })
          .customKeyboard(this.isCustomKeyBoard ? this.CustomKeyboardBuilder() : undefined, { supportAvoidance: true })
          .margin({ left: 16, right: 4 })
          .backgroundColor('rgba(0, 0, 0, 0.05)')
          .layoutWeight(1)
          .id('richEditorId')
          .borderRadius(24)
          .enableKeyboardOnFocus(true)
          .onAreaChange((old, newArea) => {
            // 初次渲染会调用onAreaChange方法，第一次不用移动RichEditor
            if (this.isInit) {
              this.isInit = false;
            } else {
              this.RichEditorMoveDistance =
                this.RichEditorMoveDistance + (newArea.height as number) - (old.height as number);
            }
          });

        Button('切换键盘')
          .id('buttonId')
          .width(96)
          .height(40)
          .borderRadius(20)
          .fontSize(14)
          .fontWeight(FontWeight.Medium)
          .margin({ left: 4, right: 16 })
          .onClick(() => {
            // 切换键盘后重新获焦拉起键盘
            this.isCustomKeyBoard = !this.isCustomKeyBoard;
            //切换键盘相当于关闭系统键盘，需要切换焦点，解决切换键盘后，输入框被遮挡问题
            focusControl.requestFocus('buttonId');
            setTimeout(() => {
              focusControl.requestFocus('richEditorId');
            }, 100);

          });
      }
      .padding({ top: 8, bottom: 16 })
      .backgroundColor(Color.White)
      .alignItems(VerticalAlign.Center)
      .width('100%')
      .animation({
        duration: 300,
        curve: Curve.EaseOut
      });
    }
    .width('100%')
    .height('100%');
  }
}
```
