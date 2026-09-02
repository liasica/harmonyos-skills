---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-34
title: 应用内浏览文档上滑时不流畅
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 应用内浏览文档上滑时不流畅
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0f4a9727c71d7e728094c25e62bd89855c49303be97454c205bf223990182375
---

## 问题现象

应用内浏览文档上滑时不流畅，下滑正常。

## 背景知识

* [DevEco Testing](https://developer.huawei.com/consumer/cn/deveco-testing/)中的UIViewer工具支持设备镜像投屏、控件信息预览、高级控件查看等模式，显著提升控件信息获取效率，提供实用工具集合，可以通过该工具对页面中的组件进行定位与分析，检查其各项属性和参数详情。
* DevTools：Web前端开发调试工具，提供了电脑上调试移动设备前端页面的能力，利用DevTools工具可以分析Web组件加载页面的问题，具体可参考[使用DevTools工具调试前端页面](../harmonyos-guides/web-debugging-with-devtools.md)。
* [NestedScroll](../harmonyos-references/ts-container-scroll.md#nestedscroll10)：设置前后两个方向的嵌套滚动模式，实现与父组件的滚动联动。

## 问题定位

1. 通过UIViewer工具获取到发生问题页面的组件结构是Scroll组件中嵌套Web页面，并且Web组件同一层级还有两个Column容器。此时应用可滑动区域是由**三个容器组成**的。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/QoUZj_j0TD-HB_i6seubhw/zh-cn_image_0000002658794529.png "点击放大")
2. 使用DevTools工具抓取加载的Web页面，可以看到页面右侧有滚动条，且支持上下滑动。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/bg_eUHfxSduINBsQNBN2EA/zh-cn_image_0000002628555164.png)
3. 通过滚轮将Web页面滑动至顶部，此时再次在手机上尝试滑动，发现无卡顿现象，使用UIViewer根据抓取此时的组件结构。此时应用可滑动区域是由Web组件**单独**构成的。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/MSkQ32AsQGGmhBjt2z6XQw/zh-cn_image_0000002658914487.png "点击放大")
4. 使用DevEco Profiler Frame模板抓取滑动过程的Trace信息，搜索关键字**User events**、**H:WEB\_LIST\_FLING**、**H:TRAILING\_ANIMATION**。结合应用包名泳道中与浏览器内核相关的线程情况，可以看到前六次滑动手势操作的均为Scroll组件，后两次滑动手势才真正滑动了Web页面，此时浏览器内核相关线程才开始处理渲染Web页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/d6ckdKStSc-AHyN6cE7g8w/zh-cn_image_0000002628395256.png "点击放大")

   在代码中搜索关键字**NestedScrollMode**，发现设置滚动方式为PARENT\_FIRST，父组件优先滚动到边缘后自身滚动。以下是相关代码：

   ```ts
   import webview from "@ohos.web.webview";

   @Entry
   @Component
   struct NestedScroll {
     private scrollerForScroll: Scroller = new Scroller();
     private web = new webview.WebviewController();

     build() {
       Flex() {
         Scroll(this.scrollerForScroll) {
           Column() {
             Column(){
               Text("Scroll Area1.1")
                 .width("100%")
                 .height("5%")
                 .backgroundColor(0X330000FF)
                 .fontSize(16)
                 .textAlign(TextAlign.Center)
               Text("Scroll Area1.2")
                 .width("100%")
                 .height("5%")
                 .backgroundColor(0X330000FF)
                 .fontSize(16)
                 .textAlign(TextAlign.Center)
               Text("Scroll Area1.3")
                 .width("100%")
                 .height("5%")
                 .backgroundColor(0X330000FF)
                 .fontSize(16)
                 .textAlign(TextAlign.Center)
             }
             Column(){
               Text("Scroll Area2.1")
                 .width("100%")
                 .height("5%")
                 .backgroundColor(0X540000FF)
                 .fontSize(16)
                 .textAlign(TextAlign.Center)
               Text("Scroll Area2.2")
                 .width("100%")
                 .height("5%")
                 .backgroundColor(0X540000FF)
                 .fontSize(16)
                 .textAlign(TextAlign.Center)
             }

             Web({
               src: $r('app.string.test_url'), // 测试时请替换成实际地址
               controller: this.web
             })
               .width("100%")
               .height("100%")
               .nestedScroll({
                 scrollForward: NestedScrollMode.PARENT_FIRST,
                 scrollBackward: NestedScrollMode.SELF_FIRST
               })
               .fileAccess(false)
               .geolocationAccess(false)
           }
         }
         .width("100%")
         .height("100%")
       }
       .width('100%')
       .height('100%')
       .backgroundColor(0xDCDCDC)
       .padding({
         left: 20,
         right: 20,
         top: 50,
         bottom: 20
       })
     }
   }
   ```

## 分析结论

Scroll组件嵌套Web时，存在其他与Web组件同一层级的容器，发生手势识别冲突，导致Web页面滑动卡顿。

## 修改建议

使用[触摸测试控制](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md)来规避此种情况，给显示在上层的节点设置hitTestBehavior为HitTestMode.BLock。

```ts
import webview from "@ohos.web.webview";

@Entry
@Component
struct NestedScroll {
  private scrollerForScroll: Scroller = new Scroller();
  private web = new webview.WebviewController();

  build() {
    Flex() {
      Scroll(this.scrollerForScroll) {
        Column() {
          Column(){
            Text("Scroll Area1.1")
              .width("100%")
              .height("5%")
              .backgroundColor(0X330000FF)
              .fontSize(16)
              .textAlign(TextAlign.Center)
            Text("Scroll Area1.2")
              .width("100%")
              .height("5%")
              .backgroundColor(0X330000FF)
              .fontSize(16)
              .textAlign(TextAlign.Center)
            Text("Scroll Area1.3")
              .width("100%")
              .height("5%")
              .backgroundColor(0X330000FF)
              .fontSize(16)
              .textAlign(TextAlign.Center)
          }
          Column(){
            Text("Scroll Area2.1")
              .width("100%")
              .height("5%")
              .backgroundColor(0X540000FF)
              .fontSize(16)
              .textAlign(TextAlign.Center)
            Text("Scroll Area2.2")
              .width("100%")
              .height("5%")
              .backgroundColor(0X540000FF)
              .fontSize(16)
              .textAlign(TextAlign.Center)
          }

          Web({
            src: $r('app.string.test_url'), // 测试时请替换成实际地址
            controller: this.web
          })
            .width("100%")
            .height("100%")
            .hitTestBehavior(HitTestMode.Block)
            .fileAccess(false)
            .geolocationAccess(false)
        }
      }
      .width("100%")
      .height("100%")
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({
      left: 20,
      right: 20,
      top: 50,
      bottom: 20
    })
  }
}
```
