---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-549
title: 部分用户头像无法点击进入主页
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 部分用户头像无法点击进入主页
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1c059a941a5f789f980897e6b6d98e15b189d82baaf185eac6b8a96274e80daa
---

## 问题现象

应用内点击无头像框的用户头像可以进入主页，但是点击有头像框的用户头像无法进入主页。

## 背景知识

* [层叠布局 (Stack)](../harmonyos-guides/arkts-layout-development-stack-layout.md)：用于在屏幕上预留一块区域来显示组件中的元素，提供元素可以重叠的布局。层叠布局通过Stack容器组件实现位置的固定定位与层叠，容器中的子元素依次入栈，后一个子元素覆盖前一个子元素，子元素可以叠加，也可以设置位置。
* [overlay](../harmonyos-references/ts-universal-attributes-overlay.md#overlay)：在当前组件上，增加遮罩文本或者叠加自定义组件以及ComponentContent作为该组件的浮层。浮层的定位同样基于当前组件进行计算。浮层不通过组件树进行渲染，部分接口（例如getRectangleById）不支持获取浮层中的组件。
* [hitTestBehavior](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md#hittestbehavior)：设置组件的触摸测试类型。如果组件不设置hitTestBehavior，其默认触摸测试类型为HitTestMode.Default。
* [HitTestMode.Transparent](../harmonyos-references/ts-appendix-enums.md#hittestmode9)：自身和子节点都响应触摸测试，不会阻塞兄弟节点的触摸测试，不会影响祖先节点的触摸测试。

## 问题定位

1. 使用DevEco Testing查看无头像框的用户头像组件树，如下图所示，Stack容器中只有一个头像组件，并且clickable属性为true，所以可以点击并进入主页。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/jPAz-GrERyS7HAsA34TUVg/zh-cn_image_0000002658910841.png "点击放大")
2. 查看有头像框的用户头像组件树，如下面两张图所示，可以看到Stack容器中从上到下的顺序是：头像组件（clickable属性为true），头像框组件（clickable属性为false）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/IbpWMol0RHOYt1HlIljsQQ/zh-cn_image_0000002658790889.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/1P8kADHaRMa-w-utmLquug/zh-cn_image_0000002628551524.png "点击放大")

## 分析结论

含有头像框的用户头像，使用了Stack层叠布局，Stack中头像框组件的顺序在头像组件之后，所以头像框组件覆盖了头像组件。而且头像框组件没有设置点击事件，导致无法进入主页。

## 修改建议

* 可以在最外层的Stack组件设置点击事件进行跳转。
* 可以使用overlay将头像框组件设置头像组件的浮层，这样只需要设置头像组件的点击事件。

示例代码如下：

```ts
import { promptAction } from "@kit.ArkUI";

@Entry
@Component
struct Index {
  @Builder
  OverlayNode() {
    Image($r('app.media.foreground')) // 表示头像框图片
      .height(100)
      .width(100)
      .hitTestBehavior(HitTestMode.Transparent); // 配置浮层不阻塞交互
  }

  showToast(str: string) {
    this.getUIContext().getPromptAction().showToast({
      message: str,
      duration: 2000,
      showMode: promptAction.ToastShowMode.DEFAULT,
      bottom: 80
    });
  }

  build() {
    Column() {
      Text('使用Stack方式：');
      Stack() {
        Image($r('app.media.background')) // 表示头像图片
          .height(100)
          .width(100);
        Image($r('app.media.foreground')) // 表示头像框图片
          .height(100)
          .width(100);
      }
      .onClick(() => {
        this.showToast('使用Stack方式，点击头像进入下一页');
      })
      .margin(30);

      Text('使用overlay方式：');
      Image($r('app.media.background')) // 表示头像图片
        .height(100)
        .width(100)
        .overlay(this.OverlayNode(), { align: Alignment.Center })
        .onClick(() => {
          this.showToast('使用overlay方式，点击头像进入下一页');
        })
        .margin(30);
    }
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}
```
