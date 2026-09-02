---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1518
title: Tabs使用overlay实现在页签栏添加自定义组件
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Tabs使用overlay实现在页签栏添加自定义组件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b2cb995f9ec67c327e944e2f7bd0c53243f109c6231db22ac36ef9e00eecda46
---

## 问题现象

Tabs组件如何在TabBar添加页签之外的自定义组件，如文字和图片等？

## 背景知识

* [Tabs](../harmonyos-references/ts-container-tabs.md)通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。
* [overlay](../harmonyos-references/ts-universal-attributes-overlay.md)支持在绑定的组件上方增加类似遮罩的效果，遮罩可以是文本、自定义组件以及ComponentContent。

## 解决方案

使用浮层overlay可以实现，步骤如下：

1. 通过Builder设置浮层。值得注意的是：为了避免阻塞对TabBar的操作，需在浮层Builder的最外层组件上配置.hitTestBehavior(HitTestMode.Transparent)。

   ```ts
   @Builder
   overlayExample() {
     Flex({ justifyContent: FlexAlign.SpaceBetween, direction: FlexDirection.Row, alignItems: ItemAlign.Center }) {
       Text('登录').fontSize(18).fontColor('#ffcd6c18');
       Image($r('app.media.search'))
         .width(24)
         .height(24);
     }
     .padding({ left: 20, right: 20 })
     .width('100%')
     .height(56)
     .hitTestBehavior(HitTestMode.Transparent); // 配置浮层不阻塞交互
   }
   ```
2. 将浮层添加到Tabs上，注意设置barWidth限制页签大小，腾出浮层容纳的空间，barHeight与浮层的最外层组件高度保持一致。

   ```ts
   Tabs() {
     TabContent() {
       Column().width('100%').height('100%').backgroundColor(Color.Pink);
     }.tabBar(SubTabBarStyle.of('订阅'));

     TabContent() {
       Column().width('100%').height('100%').backgroundColor(Color.Green);
     }.tabBar(SubTabBarStyle.of('推荐'));

     TabContent() {
       Column().width('100%').height('100%').backgroundColor(Color.Blue);
     }.tabBar(SubTabBarStyle.of('热门'));
   }
   .width('100%')
   .height('100%')
   .backgroundColor(0xf1f3f5)
   .barMode(this.barMode)
   .barWidth(200)
   .overlay(this.overlayExample(), { align: Alignment.Top });
   ```

完整示例参考如下：

```ts
@Entry
@Component
struct TabsExample {
  text: string = '文本';
  barMode: BarMode = BarMode.Fixed;

  @Builder
  overlayExample() {
    Flex({ justifyContent: FlexAlign.SpaceBetween, direction: FlexDirection.Row, alignItems: ItemAlign.Center }) {
      Text('登录').fontSize(18).fontColor('#ffcd6c18');
      Image($r('app.media.search'))
        .width(24)
        .height(24);
    }
    .padding({ left: 20, right: 20 })
    .width('100%')
    .height(56)
    .hitTestBehavior(HitTestMode.Transparent); // 配置浮层不阻塞交互
  }

  build() {
    Column() {
      Tabs() {
        TabContent() {
          Column().width('100%').height('100%').backgroundColor(Color.Pink);
        }.tabBar(SubTabBarStyle.of('订阅'));

        TabContent() {
          Column().width('100%').height('100%').backgroundColor(Color.Green);
        }.tabBar(SubTabBarStyle.of('推荐'));

        TabContent() {
          Column().width('100%').height('100%').backgroundColor(Color.Blue);
        }.tabBar(SubTabBarStyle.of('热门'));
      }
      .width('100%')
      .height('100%')
      .backgroundColor(0xf1f3f5)
      .barMode(this.barMode)
      .barWidth(200)
      .overlay(this.overlayExample(), { align: Alignment.Top });
    }
    .width('100%')
    .height('100%');
  }
}
```
