---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1632
title: 滑动Swiper组件时如何不触发子组件的点击事件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 滑动Swiper组件时如何不触发子组件的点击事件
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:e10118926df81778eb19d28d4b9821d8e525a14e6287e9720397538b1094227e
---

## 问题现象

当前应用通过Swiper组件垂直滚动展示公告通知，点击子组件的内容会有弹窗提示，左右滑动时也会触发Text组件的点击事件，如何保证在左右滑动时不触发子组件的点击事件？

问题代码示例参考如下：

```screen
import { PromptAction } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  promptAction: PromptAction = this.getUIContext().getPromptAction();

  build() {
    Column() {
      Swiper() {
        Text('公告')
          .width('80%')
          .fontSize(20)
          .textAlign(TextAlign.Center)
          .onClick(() => {
            this.promptAction.showToast({ message: '通知详情', alignment: Alignment.Top });
          })
      }
      .height('20%')
      .vertical(true)
    }
    .width('100%')
    .height('100%')
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/KNTwKq0EQ1SaE-gztk5Mjg/zh-cn_image_0000002628777522.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233155Z&HW-CC-Expire=31536000000&HW-CC-Sign=E77840C126007E4750CB411E3E8F1668513AE9B4B0AFCBDDD8BD381A16EC87D1 "点击放大")

## 背景知识

* [onClick点击事件](../harmonyos-references/ts-universal-events-click.md)是组件被点击时触发的事件，因此滑动后抬起手指也会触发onClick事件。可以新增distanceThreshold参数，设置点击手势移动阈值。手指移动超出阈值时，点击手势识别失败。
* [TapGesture点击手势](../harmonyos-guides/arkts-gesture-events-single-gesture.md#点击手势tapgesture)支持单次点击和多次点击。

## 解决方案

可通过限制手势移动阈值区分点击、滑动事件。

* **方案一**：onClick事件中增加distanceThreshold参数，将阈值设置为一个极小值1，当手指的移动距离超出预设的移动阈值时，点击识别失败，即不触发点击事件。

  ```screen
  import { PromptAction } from '@kit.ArkUI';

  @Entry
  @Component
  struct Index {
    promptAction: PromptAction = this.getUIContext().getPromptAction();

    build() {
      Column() {
        Swiper() {
          Text('公告')
            .width('80%')
            .fontSize(20)
            .textAlign(TextAlign.Center)
            .onClick(() => {
              this.promptAction.showToast({ message: '通知详情', alignment: Alignment.Top });
            }, 1);
        }
        .height('20%')
        .vertical(true)
        .indicator(false);
      }
      .width('100%')
      .height('100%');
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/AebrYACoQJG5otbf9C0dLA/zh-cn_image_0000002658976861.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233155Z&HW-CC-Expire=31536000000&HW-CC-Sign=D21092DC5A725F20726AF0FDF1989BEB18464ECB83DD6925B371A19F25A932C0 "点击放大")
* **方案二**：当需要识别单击、双击和多次点击事件，并阻止滑动过程中误触发子组件点击事件时，可将子组件的onClick事件替换为TapGesture。[TapGestureParameters](../harmonyos-references/ts-basic-gestures-tapgesture.md#tapgestureparameters12对象说明)中可设置连续点击次数count，同时设置distanceThreshold限制手势移动范围，当手势移动距离超过该阈值时，不识别为有效点击，从而有效避免滑动时的误触。

  ```screen
  import { PromptAction } from '@kit.ArkUI';

  @Entry
  @Component
  struct TapGestureExample {
    promptAction: PromptAction = this.getUIContext().getPromptAction();

    build() {
      Column() {
        Swiper() {
          // 单指双击文本触发手势事件
          Text('Click twice').fontSize(28)
            .gesture(
              TapGesture({ count: 2, distanceThreshold: 50 })
                .onAction((event: GestureEvent) => {
                  if (event) {
                    this.promptAction.showToast({ message: '通知详情', alignment: Alignment.Top });
                  }
                })
            );
          Text('');
        }.indicator(false);
      }
      .height(200)
      .width(300)
      .padding(20)
      .margin(30);
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/gjkdHuKzTky-hiPGBVj-rA/zh-cn_image_0000002658856921.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233155Z&HW-CC-Expire=31536000000&HW-CC-Sign=7564345C5BF9431923DB3CE010321306EE23E2BDF885AC1C6239C301F077D9AF "点击放大")
