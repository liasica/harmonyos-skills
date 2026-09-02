---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-759
title: 如何实现宿主组件隐藏而绑定的半模态页面仍显示的效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现宿主组件隐藏而绑定的半模态页面仍显示的效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:03+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:71955a9a302c5097db60a95bb69b2c2e899e12baa66b86700ce40eb3d6967e4f
---

## 问题现象

在开发HarmonyOS应用时，为宿主组件绑定了半模态页面，点击后显示半模态页面。而该组件可以隐藏，如何在组件隐藏时，绑定的半模态页面仍显示的效果？目前宿主组件和半模态页面会同时消失。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/g4kN8xjFQRS3FXNtlHWdiQ/zh-cn_image_0000002628395792.gif "点击放大")

问题代码示例参考如下：

```screen
@Entry
@Component
struct Index {
  @State isShow: boolean = true;
  @State sheetShow: boolean = false;

  @Builder
  SheetBuilder() {
    Text('半模态内容')
      .margin({ top: 16 })
  }

  build() {
    Column({ space: 16 }) {
      Text('点击')
        .fontSize(24)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          this.sheetShow = !this.sheetShow;
          setTimeout(() => {
            // 隐藏绑定bindSheet的组件
            this.isShow = false;
          }, 3000)
        })

      if (this.isShow) {
        Text('绑定bindSheet的组件')
          .bindSheet($$this.sheetShow, this.SheetBuilder(), {
            height: 500
          })
      }
    }
    .padding(24)
    .height('100%')
    .width('100%')
  }
}
```

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/TGtufUAVQC6yERYvI3j96w/zh-cn_image_0000002658795059.gif "点击放大")

## 背景知识

* [半模态转场](../harmonyos-references/ts-universal-attributes-sheet-transition.md)默认是模态形式的非全屏弹窗式交互页面，允许部分底层父视图可见，帮助用户在与半模态交互时保留其父视图环境。
* [visibility](../harmonyos-references/ts-universal-attributes-visibility.md#visibility)是ArkUI框架中用于控制组件显隐状态的通用属性，通过设置不同[Visibility](../harmonyos-references/ts-appendix-enums.md#visibility)枚举值可实现三种显示模式：完全可见（Visibility.Visible）、不可见但占位（Visibility.Hidden）、完全隐藏不占位（Visibility.None），该属性是组件的通用属性，是处理动态界面布局的核心工具之一。

## 解决方案

问题代码中通过isShow控制了整个宿主组件的存在与否。当宿主组件不存在时，与其绑定的半模态弹窗自然也不存在。

可以通过控制Visibility.Visible与Visibility.None模式的切换，控制宿主组件的显隐，当宿主组件隐藏时，仍然存在于组件树中，半模态页面也会显示。

```screen
@Entry
@Component
struct SemiModal {
  @State isShow: boolean = true;
  @State sheetShow: boolean = false;

  @Builder
  SheetBuilder() {
    Text('半模态内容')
      .margin({ top: 16 })
  }

  build() {
    Column({ space: 16 }) {
      Text('点击')
        .fontSize(24)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          this.sheetShow = !this.sheetShow;
          setTimeout(() => {
            // 隐藏绑定bindSheet的组件
            this.isShow = false;
          }, 3000);
        })

      Text('绑定bindSheet的组件')
        // 利用visibility属性控制组件的显隐
        .visibility(this.isShow ? Visibility.Visible : Visibility.None)
        .bindSheet($$this.sheetShow, this.SheetBuilder(), {
          height: 500
        })
    }
    .padding(24)
    .height('100%')
    .width('100%')
  }
}
```
