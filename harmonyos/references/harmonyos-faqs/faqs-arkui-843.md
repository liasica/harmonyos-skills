---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-843
title: 实现相机录像按钮动效
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现相机录像按钮动效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:139e7880a28430579bc6b69a2a833e0049ef86a46e6e4e638b6d822dc3d89fee
---

## 问题现象

如何实现HarmonyOS系统相机录像开始和结束时的按钮动画？

## 背景知识

* HarmonyOS提供全局[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)显式动画接口来指定由于闭包代码导致的状态变化插入过渡动效。同属性动画，布局类改变宽高的动画，内容都是直接到终点状态，例如文字、Canvas的内容等，如果要内容跟随宽高变化，可以使用renderFit属性配置。
* [getUIContext](../harmonyos-references/arkts-apis-window-window.md#getuicontext10)接口可用于获取UIContext实例，此方法仅可在Stage模型下使用。

## 解决方案

1. 创建boolean类型的show变量，用于实现动画的转换，Row组件的属性如宽、高、背景颜色、边框颜色等依据show变量值的真假而改变。
2. 为Row组件添加onClick事件，通过getUIContext方法获取UIContext实例，调用animateTo函数，将动画的持续时间设置为300ms，并对show变量的值取反，即可实现动态切换的效果。

完整参考示例如下：

```ts
@Entry
@Component
struct CameraAnimationEffect {
  @State show: boolean = false;

  build() {
    Column() {
      Row() {
        Row()
          .width(this.show ? 40 : 80)
          .height(this.show ? 40 : 80)
          .backgroundColor(Color.Red)
          .borderRadius(this.show ? 10 : 80)
          .borderColor(this.show ? Color.Red : Color.White)
          .borderWidth(20);
      }
      .width(100)
      .height(100)
      .justifyContent(FlexAlign.Center)
      .backgroundColor(Color.Transparent)
      .borderRadius(100)
      .borderColor(Color.White)
      .borderWidth(2)
      // 添加点击事件
      .onClick(() => {
        this.getUIContext().animateTo({
          duration: 300
        }, () => {
          this.show = !this.show;
        });
      });
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
    .backgroundColor(Color.Black);
  }
}
```

## 总结

通过boolean类型的变量，实现组件属性的动态切换，可实现相机录像按钮的动态切换效果。
