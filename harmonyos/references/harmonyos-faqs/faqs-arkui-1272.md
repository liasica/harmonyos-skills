---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1272
title: 组件外层加了Navigation后，该组件的高度不能达到整个屏幕高度
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 组件外层加了Navigation后，该组件的高度不能达到整个屏幕高度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:19+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0865ba721396f16f2ff5fad452f73c161a9b847b64f8a878e3c2c6f006af98f6
---

## 问题现象

RelativeContainer组件外层添加了Navigation后，该组件的高度不能达到整个屏幕高度。如何将Image组件放到整个手机屏幕最下方？

问题代码示例参考如下：

```screen
@Entry
@Component
struct PrivatePage34 {
  build() {
    Navigation() {
      RelativeContainer() {
        Row() {
          Image($r('app.media.app_icon'))
            .width('90%')
            .height(200);
        }
        .padding({ top: 20 })
        .justifyContent(FlexAlign.Center)
        .width('100%');
      }
      .height('100%')
      .width('100%')
      .backgroundColor('#ffeceeef');
    }
    .backgroundColor('#DFE1E3');
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/gaeorCjHT0KIuBeT-aOmLw/zh-cn_image_0000002658835379.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/dKPd0VKkQ_qGCFJoEokHcQ/zh-cn_image_0000002628756014.png "点击放大")

## 背景知识

[hideTitleBar](../harmonyos-references/ts-basic-components-navigation.md#hidetitlebar)：设置是否隐藏标题栏，默认值：false。

## 解决方案

Navigation组件是路由导航的根视图容器，一般作为页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏。RelativeContainer组件是在内容区的，因此达不到屏幕高度。需要先将默认显示的标题等隐藏，然后进行页面布局。

```screen
@Entry
@Component
struct PrivatePage {
  build() {
    Navigation() {
      RelativeContainer() {
        Row() {
          Image($r('app.media.startIcon')) // 根据实际情况添加图片
            .width('90%')
            .height(200);
        }
        .padding({ top: 20 })
        .justifyContent(FlexAlign.Center)
        // 设置对齐规则
        .alignRules({
          left: { anchor: '__container__', align: HorizontalAlign.Start },
          right: { anchor: '__container__', align: HorizontalAlign.End },
          bottom: { anchor: '__container__', align: VerticalAlign.Bottom }
        });
      }
      .backgroundColor('#ffeceeef');
    }
    .hideTitleBar(true)
    .backgroundColor('#DFE1E3');
  }
}
```
