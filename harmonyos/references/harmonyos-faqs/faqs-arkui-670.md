---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-670
title: 如何实现基于StyledString的气泡动态适配
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现基于StyledString的气泡动态适配
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1e05ee578bc4c6ca26b2ec9c5ede8c65017e27d9c6d55325ac0e12949f313cdf
---

## 问题现象

如何根据StyledString文本高度动态调整气泡的高度？

## 效果预览

可以看到气泡大小会跟随StyledString而变化。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/2cEfcK1WT8GXWfg-lwesmQ/zh-cn_image_0000002628394678.png "点击放大")

## 背景知识

* [StyledString](../harmonyos-references/ts-universal-styled-string.md#styledstring)对象支持灵活设置文本样式，可通过TextController的[setStyledString](../harmonyos-references/ts-basic-components-richeditor.md#setstyledstring12)方法与Text组件绑定，也可通过RichEditor组件的控制器方法与RichEditor组件关联。
* [objectFit](../harmonyos-references/ts-basic-components-image.md#objectfit)方法用于设置图片的填充效果。

## 解决方案

气泡高度的动态调整可通过Column自适应Text内容实现，StyledString提供样式化文本内容，其高度由Text组件渲染后自动传递给Column。

```ts
@Builder
function bubbleBackgroundOne() {
  Image($r('app.media.backgroundcolorgray')) // 此处'backgroundcolorgray'仅作示例，请开发者自行替换。
    .objectFit(ImageFit.Fill)
    .width('100%')
    .height('100%');
}

@Entry
@Component
struct StyledStringDemo {
  styledString1: StyledString = new StyledString('运动45分钟');
  mutableStyledString1: MutableStyledString = new MutableStyledString('运动35分钟');
  controller1: TextController = new TextController();
  controller2: TextController = new TextController();

  async onPageShow() {
    this.controller1.setStyledString(this.styledString1);
    this.controller2.setStyledString(this.mutableStyledString1);
  }

  build() {
    Row() {
      Column() {
        // 显示属性字符串
        Text(undefined, { controller: this.controller1 });
        Text(undefined, { controller: this.controller2 });
        Text('测试')
          .onClick(async () => {
            this.styledString1 = new StyledString('运动45分钟XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX');
            this.controller1.setStyledString(this.styledString1);
          })
      }
      .background(bubbleBackgroundOne)
      .padding(10)
      .borderRadius(5)
      .width('100%');
    }
    .height('100%')
    .width('100%')
    .padding(10);
  }
}
```
