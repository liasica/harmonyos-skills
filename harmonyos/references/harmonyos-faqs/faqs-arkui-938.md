---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-938
title: Text组件计算文本行数
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Text组件计算文本行数
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7a7e3de4b2c70cac729048837ad8eee898f65a0156114ff42209731ecf924541
---

## 问题现象

当文本内容过长，或当文本内容包含换行符时该如何计算文本行数？

## 背景知识

[@ohos.graphics.text](../harmonyos-references/js-apis-graphics-text.md)是HarmonyOS提供的文本模块，该模块可提供一系列用于文本布局和字体管理的编程接口。其中[getLineCount](../harmonyos-references/js-apis-graphics-text.md#getlinecount)方法可用于返回文本的总行数。

## 解决方案

可以使用Text组件控制器的[布局管理器对象](../harmonyos-references/ts-basic-components-text.md#getlayoutmanager12)中的[getLineCount](../harmonyos-references/js-apis-graphics-text.md#getlinecount)方法获取组件内容的总行数，该方法包含了因文本过长导致的换行，能准确获取文本内容行数。

完整代码如下：

```ts
@Entry
@Component
struct Index1 {
  private controller: TextController = new TextController();
  textStr: string =
    '测试文本\n测试文本\n测试文本\n测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本测试文本';
  @State lineCount: number = 0;

  build() {
    Column({ space: 20 }) {
      Text(this.textStr, { controller: this.controller })
        .fontSize(20)
        .backgroundColor(Color.White)
        .borderRadius('50px')
        .padding(16)
        .margin({ left: 16, right: 16 });

      Text(`该文本总共有${this.lineCount}行`)
        .fontColor('#0A59F7');
      Button('点击计算')
        .onClick(() => {
          let layoutManager: LayoutManager = this.controller.getLayoutManager();
          let lineCount = layoutManager.getLineCount();
          this.lineCount = lineCount;
        });
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
    .backgroundColor('#efefef')
    .alignItems(HorizontalAlign.Center);

  }
}
```

效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/7DB9T9yQQzyNVuy0WPaMRQ/zh-cn_image_0000002628561100.png "点击放大")
