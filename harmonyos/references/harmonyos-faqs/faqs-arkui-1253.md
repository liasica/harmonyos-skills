---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1253
title: Text组件滚动虚化样式实现
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Text组件滚动虚化样式实现
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:95964304268ccde8c0003a80e34f5c8291d803992aaf8c0c3313e6756cc38b13
---

## 问题现象

在多行文本场景下，用户通常需要滚动文本块进行阅读。为了美观，滚动的过程如何添加边缘虚化样式呢？

预期效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/4s28f7LDSWeeNwaDEoRU5A/zh-cn_image_0000002628595510.png "点击放大")

## 背景知识

* [Text](../harmonyos-references/ts-basic-components-text.md)：显示一段文本的组件。可以包含Span、ImageSpan、SymbolSpan和ContainerSpan子组件。
* [Scroll](../harmonyos-references/ts-container-scroll.md)：可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
* [isAtEnd](../harmonyos-references/ts-container-scroll.md#isatend10)：判断容器是否滚动到底部，返回值true表示组件已经滚动到底部，false表示组件还没滚动到底部。
* [颜色渐变](../harmonyos-references/ts-universal-attributes-gradient-color.md)：设置组件的颜色渐变效果。
* [fadingEdge](../harmonyos-references/ts-container-scrollable-common.md#fadingedge14)：当enabled属性设置为true时，将开启边缘渐隐效果，options参数可用于配置渐隐区域的长度。

## 解决方案

1. 实现可拖动Text组件：

   为了使Text组件可拖动，可以使用Scroll组件嵌套Text组件。原理如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/XxIwcXKxTy-3avwp1a-8ng/zh-cn_image_0000002628755404.png "点击放大")

   在Text组件中文本量较大的情况下，如果设置了宽度，Text组件会自动拉高，将所有文字展示出来。同时，背景知识板块中提到：**当子组件的布局尺寸超过父组件的尺寸时**，Scroll组件内容可以滚动，因此可以给Scroll组件设置固定高度，且该高度要小于Text组件高度。

   ```ts
   @Entry
   @Component
   struct TextScrollBlurStyleOne {
     @State contentHeight: number = 0;
     scroller: Scroller = new Scroller();

     build() {
       Column() {
         Scroll(this.scroller) {
           Text('数字智能化发展的今天，线下场景的智能化改造及用户体验优化正逐步成为各行各业的新趋势。现在，HarmonyOS近场能力或许能成为这一趋势下的重要突破和解决方案。\n' +
             '从商家角度而言，获客一直是困扰商家的难题。类似商超、餐饮等领域，单一的公域流量争夺正转向全域运营的深度整合，核心就在于如何将公域流量转化为私域流量；类似文旅这类领域，' +
             '如何持续有效地获取客流也是行业运营的重中之重。\n' +
             '而从用户角度而言，先在庞大的线上平台筛选感兴趣、适合的门店、旅游景点；再搜索感兴趣的产品、旅游攻略；再到路线规划、出行；最后是找店、找景点。' +
             '这一系列的流程体验下来，不说繁琐，但耗时费力是必然的。\n' +
             'HarmonyOS近场能力基于意图框架，结合POI、精准位置等多维系统感知与AI大模型能力，可实现对用户显性与潜在意图的理解，并将用户需求传递给应用，' +
             '为用户匹配合时宜的服务的同时也为商家提供了精准获客、智能分发的渠道，即从传统的“人找服务”转化为“服务找人”。为商家提供更多精准客流，也为用户提供多模态、个性化的进阶场景体验。')
             .width(280)
             .onAreaChange((newValue: Area) => {
               this.contentHeight = newValue.height as number;
             });
         }
         .height(150);
       }
       .height('100%')
       .width('100%')
       .alignItems(HorizontalAlign.Center)
       .justifyContent(FlexAlign.Center);
     }
   }
   ```

   实现效果如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/DGKi2wARRfiScCRtSgfs8A/zh-cn_image_0000002658954727.png "点击放大")
2. 滑动时添加边缘虚化样式：
   * **方案一**：Text组件没有直接设置边缘虚化的属性，因此该效果需要自定义实现。边缘虚化原理如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/Jk6UMYKcSLODf3G0suKoEw/zh-cn_image_0000002658834767.png "点击放大")

     在Scroll组件的上下两侧分别添加两个Row组件，并将它们设置成渐变白色（图示为了清晰，把渐变白变成了黑白渐变色）。

     判断滑动的位置：

     | 场景 | 判断条件 | 上方Row组件 | 下方Row组件 |
     | --- | --- | --- | --- |
     | 尚未滑动 | 没有Y轴方向上的偏移量 | 不展示 | 展示 |
     | 滑至底部 | isAtEnd()接口返回值 | 展示 | 不展示 |
     | 滑动中 | 有Y轴方向上的偏移量且不等于Scroll组件高度 | 展示 | 展示 |

     完整示例参考如下：

     ```ts
     @Entry
     @Component
     struct TextScrollBlurStyleTwo {
       @State topOverLayShow: boolean = false;
       @State bottomOverLayShow: boolean = true;
       scroller: Scroller = new Scroller();
       private scrollHeight: number = 150;

       @Builder
       OverlayNode() {
         Column() {
           Row()
             .width(280)
             .height(20)
             .linearGradient({
               angle: 180,
               colors: this.topOverLayShow ? [['rgba(255, 255, 255, 1)', 0], ['rgba(255, 255, 255, 0)', 1]] : []
             });
           Blank();
           Row()
             .width(280)
             .height(20)
             .alignItems(VerticalAlign.Bottom)
             .linearGradient({
               angle: 180,
               colors: this.bottomOverLayShow ? [['rgba(255, 255, 255, 0)', 0], ['rgba(255, 255, 255, 1)', 1]] : []
             });
         }
         .width(280)
         .height(this.scrollHeight)
         .alignItems(HorizontalAlign.Center);
       }

       build() {
         Column() {
           Scroll(this.scroller) {
             Text('数字智能化发展的今天，线下场景的智能化改造及用户体验优化正逐步成为各行各业的新趋势。现在，HarmonyOS近场能力或许能成为这一趋势下的重要突破和解决方案。\n' +
               '从商家角度而言，获客一直是困扰商家的难题。类似商超、餐饮等领域，单一的公域流量争夺正转向全域运营的深度整合，核心就在于如何将公域流量转化为私域流量；类似文旅这类领域，' +
               '如何持续有效地获取客流也是行业运营的重中之重。\n' +
               '而从用户角度而言，先在庞大的线上平台筛选感兴趣、适合的门店、旅游景点；再搜索感兴趣的产品、旅游攻略；再到路线规划、出行；最后是找店、找景点。' +
               '这一系列的流程体验下来，不说繁琐，但耗时费力是必然的。\n' +
               'HarmonyOS近场能力基于意图框架，结合POI、精准位置等多维系统感知与AI大模型能力，可实现对用户显性与潜在意图的理解，并将用户需求传递给应用，' +
               '为用户匹配合时宜的服务的同时也为商家提供了精准获客、智能分发的渠道，即从传统的“人找服务”转化为“服务找人”。为商家提供更多精准客流，也为用户提供多模态、个性化的进阶场景体验。')
               .width(280);
           }
           .height(150)
           .backgroundColor('#0A59F7')
           .overlay(this.OverlayNode(), { align: Alignment.Center })
           .onDidScroll(() => {
             let curr = this.scroller.currentOffset().yOffset;
             if (curr === 0) {
               this.topOverLayShow = false;
               this.bottomOverLayShow = true;
             } else if (this.scroller.isAtEnd()) {
               this.bottomOverLayShow = false;
               this.topOverLayShow = true;
             } else {
               this.bottomOverLayShow = true;
               this.topOverLayShow = true;
             }
           });
         }
         .height('100%')
         .width('100%')
         .alignItems(HorizontalAlign.Center)
         .justifyContent(FlexAlign.Center);
       }
     }
     ```

     实现效果如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/H915me-gSS-14zSRBoG8mg/zh-cn_image_0000002628595512.png "点击放大")
   * **方案二**：添加属性fadingEdge(true, { fadingEdgeLength: LengthMetrics.vp(20) })。

     完整示例参考如下：

     ```ts
     import { LengthMetrics } from '@kit.ArkUI';

     @Entry
     @Component
     struct TextScrollBlurStyleThree {
       scroller: Scroller = new Scroller();

       build() {
         Scroll(this.scroller) {
           Text('数字智能化发展的今天，线下场景的智能化改造及用户体验优化正逐步成为各行各业的新趋势。现在，HarmonyOS近场能力或许能成为这一趋势下的重要突破和解决方案。\n' +
             '从商家角度而言，获客一直是困扰商家的难题。类似商超、餐饮等领域，单一的公域流量争夺正转向全域运营的深度整合，核心就在于如何将公域流量转化为私域流量；类似文旅这类领域，' +
             '如何持续有效地获取客流也是行业运营的重中之重。\n' +
             '而从用户角度而言，先在庞大的线上平台筛选感兴趣、适合的门店、旅游景点；再搜索感兴趣的产品、旅游攻略；再到路线规划、出行；最后是找店、找景点。' +
             '这一系列的流程体验下来，不说繁琐，但耗时费力是必然的。\n' +
             'HarmonyOS近场能力基于意图框架，结合POI、精准位置等多维系统感知与AI大模型能力，可实现对用户显性与潜在意图的理解，并将用户需求传递给应用，' +
             '为用户匹配合时宜的服务的同时也为商家提供了精准获客、智能分发的渠道，即从传统的“人找服务”转化为“服务找人”。为商家提供更多精准客流，也为用户提供多模态、个性化的进阶场景体验。')
             .width(280);
         }
         .height(150)
         .margin({ left: 50, top: 250 })
         .fadingEdge(true, { fadingEdgeLength: LengthMetrics.vp(20) })
         .backgroundColor('#0A59F7');
       }
     }
     ```
