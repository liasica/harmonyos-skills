---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-999
title: RichEditor实现同时设置删除线和下划线
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > RichEditor实现同时设置删除线和下划线
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f87567bf945b3e8937815fc8fe67abbb0f510cc5ab8458100ce14c349dbec45d
---

## 问题现象

使用RichEditorController控制器初始化的RichEditor富文本组件，如何同时设置删除线和下划线。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/HHcYvJMSRzqKNduPfSHjGw/zh-cn_image_0000002628404768.png "点击放大")

## 背景知识

[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)支持图文混排和文本交互式编辑的组件，[RichEditorController](../harmonyos-references/ts-basic-components-richeditor.md#richeditorcontroller)是RichEditor组件的控制器，[RichEditorStyledStringController](../harmonyos-references/ts-basic-components-richeditor.md#richeditorstyledstringcontroller12)是使用属性字符串构建的RichEditor组件的控制器，均继承自[RichEditorBaseController](../harmonyos-references/ts-basic-components-richeditor.md#richeditorbasecontroller12)，两种控制器都可以实现同时设置删除线与下划线。

## 解决方案

RichEditorStyledStringController实现方案可参考官网[设置装饰线](../harmonyos-guides/arkts-common-components-richeditor.md#设置装饰线)来实现。如果项目中是用RichEditorController来初始化RichEditor，想要实现同时设置两种装饰线，可使用[fromStyledString](../harmonyos-references/ts-basic-components-richeditor.md#fromstyledstring12)方法将属性字符串转换为span信息，通过addTextSpan方法添加到RichEditor组件。示例代码如下：

```ts
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct RichEditorExample {
  private richEditorController: RichEditorController = new RichEditorController();
  private mutString: MutableStyledString = new MutableStyledString('设置富文本多装饰线', [
    {
      start: 0,
      length: 9,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontSize: LengthMetrics.vp(25) })
    },
    {
      start: 0,
      length: 5,
      styledKey: StyledStringKey.DECORATION,
      styledValue: new DecorationStyle(
        {
          type: TextDecorationType.Underline,
        },
        {
          // 开启多装饰线
          enableMultiType: true
        }
      )
    },
    {
      start: 2,
      length: 4,
      styledKey: StyledStringKey.DECORATION,
      styledValue: new DecorationStyle(
        {
          type: TextDecorationType.LineThrough,
        },
        {
          // 开启多装饰线
          enableMultiType: true
        }
      )
    },
  ]);

  private isTextSpanResult(item: RichEditorImageSpanResult | RichEditorTextSpanResult): boolean {
    return typeof (item as RichEditorImageSpanResult)['imageStyle'] == 'undefined';
  }

  build() {
    Column() {
      RichEditor({ controller: this.richEditorController })
      Button("调用fromStyledString").onClick(() => {
        try {
          // 将属性字符串转换成span信息
          let spans = this.richEditorController.fromStyledString(this.mutString);
          // 通过for循环拿出属性字符串的装饰信息，添加到richEditorController
          spans.forEach((item: RichEditorTextSpanResult | RichEditorImageSpanResult) => {
            if (this.isTextSpanResult(item)) {
              let richSpan = item as RichEditorTextSpanResult;
              this.richEditorController.addTextSpan(richSpan.value, {
                style:
                {
                  fontColor: richSpan.textStyle?.fontColor,
                  fontSize: richSpan.textStyle?.fontSize,
                  decoration: richSpan.textStyle.decoration
                }
              });
            }
          });
        } catch (error) {
          console.error('fromStyledString error');
        }
      })
    }
  }
}
```
