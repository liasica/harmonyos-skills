---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-943
title: RichEditor获取ImageSpan中图片信息
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > RichEditor获取ImageSpan中图片信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ea0b2597b4350f46b3f79ff191b9da9ad12ddab38e0313d05dff8e9a3c8512e4
---

## 问题现象

在RichEditor组件中通过$r('app.media.background')方式添加ImageSpan，并使用getSpans获取span信息时，由于base目录中的资源文件会被编译成二进制文件并分配资源ID，导致获取的图片名称与实际图片名称不一致。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/vKmRvw4ySVmhQHnG8bEk9w/zh-cn_image_0000002658800487.png "点击放大")

## 背景知识

[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)是支持图文混排和文本交互式编辑的组件，可以通过[getSpans](../harmonyos-references/ts-basic-components-richeditor.md#getspans)方法获取所有span信息。

## 解决方案

将图片资源放到rawfile文件夹下，再通过getSpans获取valueResourceStr字段，能够正常获取到图片的名称。

```ts
@Entry
@Component
struct RichEditorPage {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };

  build() {
    Column() {
      RichEditor(this.options)
        .onReady(() => {
          this.controller.addTextSpan('点击按钮在此处添加image。', {
            style: {
              fontColor: Color.Black,
              fontSize: 15
            }
          });
        })
        .width('100%')
        .height(100);
      Row() {
        Button('添加图片', {
          buttonStyle: ButtonStyleMode.NORMAL
        })
          .height(30)
          .fontSize(13)
          .onClick(() => {
            this.controller.addImageSpan($rawfile('background.png'), {
              imageStyle: {
                size: ['57px', '57px']
              }
            });
          });
        Button('获取图片span', {
          buttonStyle: ButtonStyleMode.NORMAL
        })
          .onClick(() => {
            this.controller.getSpans({ start: 0 }).forEach(item => {
              console.info(`imageName is : ${(item as RichEditorImageSpanResult).valueResourceStr}`);
            });
          });
      }
      .justifyContent(FlexAlign.SpaceAround)
      .width('100%');
    }
    .border({ width: 1 });
  }
}
```

效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/C_cNKk7OSTiC_HyiHa5AQw/zh-cn_image_0000002628561128.png "点击放大")
