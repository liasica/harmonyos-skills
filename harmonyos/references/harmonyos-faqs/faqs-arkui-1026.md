---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1026
title: 智能表如何适配智慧手势
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 智能表如何适配智慧手势
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0cc306c9b9f8d78edd8a4a62e90e58462036413e0f54147a5d8627595493b8ca
---

## 问题现象

智慧手势是智能穿戴设备除屏幕交互、表冠交互和按键交互外的独特感知交互方式，应用如何进行适配？

## 效果预览

1. 佩戴智能表，开启智慧手势识别开关：设置-手势-智慧手势识别。打开应用：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/BcSNbiSxT1Kz48gMO5MDAg/zh-cn_image_0000002658804083.png "点击放大")
2. 捏合确认，第一个按钮文字变为“Confirmed”：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/kDgJiwvzQkGUsG8YaIeXaw/zh-cn_image_0000002628564720.png "点击放大")
3. 滑动切焦，焦点从第一个按钮切换到第二个按钮：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/QwN5ptBwQ_ieQv-YAMuDnw/zh-cn_image_0000002658924027.png "点击放大")
4. 捏合确认，第二个按钮文字变为“Confirmed”：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/DBdGclCJRuyjSNJ8X5jE2g/zh-cn_image_0000002628404816.png "点击放大")

## 背景知识

* 使用智慧手势功能要确保设备上的智慧手势识别开关已打开。
* 手势类型包括捏合确认和滑动切焦。捏合确认会触发组件的[onKeyEvent](../harmonyos-references/ts-universal-events-key.md#onkeyevent)事件，KeyCode为KEYCODE\_ENTER，type为KeyType.Down。滑动切焦会分别触发失焦组件和获焦组件的[onBlur](../harmonyos-references/ts-universal-focus-event.md#onblur)和[onFocus](../harmonyos-references/ts-universal-focus-event.md#onfocus)事件。

## 解决方案

1. 使用[activate](../harmonyos-references/arkts-apis-uicontext-focuscontroller.md#activate14)激活当前界面的焦点激活态。

   ```ts
   aboutToAppear(): void {
     this.getUIContext().getFocusController().activate(true, false);
   }
   ```
2. 激活焦点激活态后，可调用[requestFocus](../harmonyos-references/arkts-apis-uicontext-focuscontroller.md#requestfocus12)方法使目标组件获得焦点，随后手势操作方可生效。

   ```ts
   onDidBuild(): void {
     try {
       // register a button to get focus by default.
       this.getUIContext().getFocusController().requestFocus('btn1');
     } catch (error) {
       console.error(`requestFocus function error. Code is ${error.code}, message is ${error.message}.`);
     }
   }
   ```
3. 捏合确认会触发组件的onKeyEvent事件，KeyCode为KEYCODE\_ENTER，type为KeyType.Down，应用可以在该条件触发后进行功能执行。

   ```ts
   .onKeyEvent((event: KeyEvent) => {
     if (event.keyCode === KeyCode.KEYCODE_ENTER && event.type === KeyType.Down) {
       // Trigger the pinching gesture
       this.oneButton1Text = 'Confirmed';
     }
   });
   ```
4. 滑动切焦会分别触发失焦组件和获焦组件的onBlur和onFocus事件，应用可以在该条件触发后进行功能执行。

   ```ts
   .onFocus(() => {
     this.oneButton1Text = 'One';
     this.oneButton2Text = 'Two';
   })
   .onBlur(() => {
     this.oneButton1Text = 'One';
   })
   ```
5. 退出页面时，设置当前界面的焦点激活态为false，退出焦点激活态。

   ```ts
   aboutToDisappear(): void {
     this.getUIContext().getFocusController().activate(false);
   }
   ```

完整示例参考如下：

```ts
import { KeyCode } from '@kit.InputKit';
import { ColorMetrics, LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State oneButton1Text: string = 'One';
  @State oneButton2Text: string = 'Two';

  aboutToAppear(): void {
    this.getUIContext().getFocusController().activate(true, false);
  }

  onDidBuild(): void {
    try {
      // register a button to get focus by default.
      this.getUIContext().getFocusController().requestFocus('btn1');
    } catch (error) {
      console.error(`requestFocus function error. Code is ${error.code}, message is ${error.message}.`);
    }
  }

  aboutToDisappear(): void {
    this.getUIContext().getFocusController().activate(false);
  }

  build() {
    NavDestination() {
      Scroll() {
        Column({ space: 20 }) {
          Button(this.oneButton1Text)
            .width(165)
            .height(40)
            .focusBox({
              margin: LengthMetrics.px(10),
              strokeColor: ColorMetrics.rgba(255, 255, 255),
              strokeWidth: LengthMetrics.px(5)
            })
            .defaultFocus(true)
            .id('btn1')

            .onFocus(() => {
              this.oneButton1Text = 'One';
              this.oneButton2Text = 'Two';
            })
            .onBlur(() => {
              this.oneButton1Text = 'One';
            })
            .onKeyEvent((event: KeyEvent) => {
              if (event.keyCode === KeyCode.KEYCODE_ENTER && event.type === KeyType.Down) {
                // Trigger the pinching gesture
                this.oneButton1Text = 'Confirmed';
              }
            });
          Button(this.oneButton2Text)
            .width(165)
            .height(40)
            .focusBox({
              margin: LengthMetrics.px(10),
              strokeColor: ColorMetrics.rgba(255, 255, 255),
              strokeWidth: LengthMetrics.px(5)
            })
            .onFocus(() => {
              this.oneButton1Text = 'One';
              this.oneButton2Text = 'Two';
            })
            .onBlur(() => {
              this.oneButton2Text = 'Two';
            })
            .onKeyEvent((event: KeyEvent) => {
              if (event.keyCode === KeyCode.KEYCODE_ENTER && event.type === KeyType.Down) {
                // Trigger the pinching gesture
                this.oneButton2Text = 'Confirmed';
              }
            });

        }
        .alignItems(HorizontalAlign.Center)
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('100%');
      };
    }
    .hideTitleBar(true)
    .width('100%')
    .height('100%');
  }
}
```
