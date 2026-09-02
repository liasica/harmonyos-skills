---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-944
title: RichEditor组件高度限制失败
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > RichEditor组件高度限制失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:eec39250f977aef96a6715553c79cdb82bdc0bdedb9fcb712980fe44ba66f18f
---

## 问题现象

在父组件Column设置了尺寸限制，但是却未能在子组件RichEditor中生效，当给RichEditor输入多行文本后，RichEditor与其他子组件的总高度会超过父组件的尺寸限制。

问题代码示例参考如下：

```ts
@Entry
@Component
struct Question {
  richEditorController: RichEditorController = new RichEditorController();

  build() {
    Column() {
      Row().width('100%').height(50).backgroundColor('#87ceeb')
      RichEditor({ controller: this.richEditorController })
        .backgroundColor('#f8f8f8')
        .width('100%')
    }
    .width(200)
    .constraintSize({
      maxHeight: 100
    })
  }
}
```

## 背景知识

* [RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)是支持图文混排和文本交互式编辑的组件，通常用于响应用户对图文混合内容的输入操作，例如可以输入图文的评论区。
* [constraintSize](../harmonyos-references/ts-universal-attributes-size.md#constraintsize)：设置约束尺寸，组件布局时，进行尺寸范围限制。
* [layoutWeight](../harmonyos-references/ts-universal-attributes-size.md#layoutweight)：用于设置组件的布局权重，使组件在父容器（Row/Column/Flex）的主轴方向按照权重分配尺寸。
  + 父容器尺寸确定时，不设置layoutWeight属性或者layoutWeight属性生效值为0的元素优先占位，这些元素占位后在主轴留下的空间称为主轴剩余空间。
  + 设置了layoutWeight属性且layoutWeight属性生效值大于0的子元素会从主轴剩余空间中按照各自所设置的权重占比分配尺寸，分配时会忽略元素本身的尺寸设置。

## 问题定位

检查父组件constraintSize是否可以对子组件进行有效限制：当子元素高度小于父组件高度限制时，父组件高度为设置的最小高度；子元素高度大于父组件高度限制时，父组件高度随子元素高度自适应。

## 分析结论

当前代码未对子组件进行有效的高度限制，需要添加子组件的高度限制属性。

## 修改建议

对子组件进行高度限制的方法如下：为子组件添加constraintSize。

```ts
import { window } from '@kit.ArkUI';

@Entry
@Component
struct RichEditorDemo {
  richEditorController: RichEditorController = new RichEditorController();

  aboutToAppear() {
    window.getLastWindow(this.getUIContext().getHostContext(), (err, win) => {
      if (err.code) {
        return;
      }
      win.setWindowLayoutFullScreen(true);
    });
  }

  build() {
    Column({ space: 16 }) {
      Row() {
        Text('此处用于对比50的高度')
      }
      .width('100%')
      .height(50)
      .backgroundColor('#ffffff')
      .justifyContent(FlexAlign.Center)
      .borderRadius(16)

      RichEditor({ controller: this.richEditorController })
        .backgroundColor('#ffffff')
        .width('100%')
        // 添加constraintSize属性，将高度限制为50，子组件高度相加不超过100（父组件高度限制）
        .constraintSize({ maxHeight: 50 })
        .borderRadius(16)
    }
    .width('100%')
    .height('100%')
    .padding(16)
    .backgroundColor('#f1f3f5')
    .margin({ top: 40 })
    // 添加constraintSize属性，将高度限制为148(50+50+32+16)，子组件高度相加不超过100（父组件高度限制）
    .constraintSize({ maxHeight: 148 })
  }
}
```
