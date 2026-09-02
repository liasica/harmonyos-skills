---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-439
title: ArcSwiper如何适配表冠
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > ArcSwiper如何适配表冠
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:63b5fbefe5fde7f291536d4fb71821e3e005e81f6eee91a080bd56b5b4fed27f
---

可以滑动的组件需要适配旋转表冠，默认支持的组件在获焦时即可响应表冠事件。

1. 默认支持表冠事件的组件: Slider、DatePicker、TextPicker、 TimePicker、Scroll、List、Grid、WaterFlow、ArcList、Refresh和ArcSwiper。

   默认支持组件只需要添加.focusable(true)、 .focusOnTouch(true)、.defaultFocus(true)属性获焦即可响应。
2. 通过onDigitalCrown监听表冠事件。

   示例代码如下：

   ```screen
   import {
     ArcSwiper,
     ArcSwiperAttribute,
     ArcDotIndicator,
     ArcDirection,
     ArcSwiperController
   } from '@kit.ArkUI';

   @Entry
   @Component
   struct ArcSwiperDemo {
     @State currentIndex: number = 0;
     private swiperController: ArcSwiperController = new ArcSwiperController();

     build() {
       ArcSwiper(this.swiperController) {
         Text('page 1')
           .width('100%').height('100%').backgroundColor(Color.Red)
         Text('page 2')
           .width('100%').height('100%').backgroundColor(Color.Green)
         Text('page 3')
           .width('100%').height('100%').backgroundColor(Color.Blue)
       }
       .focusable(true)
       .focusOnTouch(true)
       .defaultFocus(true)
       .onDigitalCrown((event: CrownEvent) => {
         if (event.degree > 0) {
           this.swiperController.showNext();
         } else if (event.degree < 0) {
           this.swiperController.showPrevious();
         }
       })
     }
   }
   ```

**参考链接**

[表冠事件](../harmonyos-references/ts-universal-events-crown.md)

[焦点控制](../harmonyos-references/ts-universal-attributes-focus.md)

[ArcSwiper示例](../harmonyos-references/ts-container-arcswiper.md#示例)
