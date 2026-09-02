---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1289
title: bindSheet底部按钮如何固定
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > bindSheet底部按钮如何固定
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:566b233042a6783cb90279d38903e91208c2dcd7de299d2a3d4ca75cc5679113
---

## 问题现象

展开、收起bindSheet时，底部按钮位置都会发生变动，该如何固定？

问题效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/cI_pzSn2Q_KZv9jJgikfVg/zh-cn_image_0000002628757878.gif "点击放大")

## 背景知识

* [bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)：给组件绑定半模态页面，点击后显示模态页面。
* [constraintSize](../harmonyos-references/ts-universal-attributes-size.md#constraintsize)：设置约束尺寸，组件布局时，进行尺寸范围限制。
* [position](../harmonyos-references/ts-universal-attributes-location.md#position)绝对定位，确定子组件相对父组件内容区的位置，支持[attributeModifier](../harmonyos-references/ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

## 解决方案

给bindSheet所绑定的自定义构建函数[@Builder](../harmonyos-guides/arkts-builder.md)内部的根容器组件设置constraintSize({minHeight:300,maxHeight:300})属性即可解决，高度值根据实际开发场景需要进行设置。示例代码如下：

```screen
@Entry
@Component
struct SheetTransitionExample {
  @State isShow: boolean = false;

  @Builder
  myBuilder() {
    Row() {
      Button('content1')
        .margin(10)
        .fontSize(20)

      Button('content2')
        .margin(10)
        .fontSize(20)
    }
    .width('100%')
    .height('100%')
    .alignItems(VerticalAlign.Bottom)
    .justifyContent(FlexAlign.Center)
    .constraintSize({ minHeight: 300, maxHeight: 300 })
  }

  build() {
    Column() {
      Button('transition modal 1')
        .onClick(() => {
          this.isShow = true;
        })
        .fontSize(20)
        .margin(10)
        .bindSheet($$this.isShow, this.myBuilder(), {
          detents: [SheetSize.MEDIUM, SheetSize.LARGE, 200],
          backgroundColor: Color.White,
          blurStyle: BlurStyle.Thick,
          showClose: true,
          title: { title: 'title', subtitle: 'subtitle' },
        })
    }
    .justifyContent(FlexAlign.Start)
    .width('100%')
    .height('100%')
  }
}
```

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/ZzvwQCj5SWyYOe39xG9Xhw/zh-cn_image_0000002658957195.png "点击放大")

## 常见FAQ

Q：为什么bindSheet高度改变的时候固定在底部的按钮出现跳动？

A：在上下布局中bindSheet高度改变时，模态框重新渲染，底部按钮重新渲染，底部按钮相对于原来位置发生改变，会出现跳动一下的效果，这是正常现象。

Q：正文中提供了底部按钮位于半模态窗的相对位置固定的解决方案，如何保证底部按钮的绝对位置一直不变呢？

A：给需要保持固定不变的组件设置position({bottom:0})属性即可。
