---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-687
title: RichEditor实现“@XXX”自动替换图片
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > RichEditor实现“@XXX”自动替换图片
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:adfc7bc91e5b7a278ac5b99d7c79857664b4adef5280a54aff0973e502ba0b64
---

## 问题现象

使用RichEditor实现“@XXX”替换成图片的功能，同时@XXX的图片可以对应到具体用户，如何实现？例如：评论区输入@logo，出现logo图片。

## 背景知识

[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)是支持图文混排和文本交互式编辑的组件。其支持通过addXXXSpan方法插入文本、图片、自定义布局等内容，并可通过deleteSpans方法删除指定范围内的文本和图片。

## 解决方案

使用aboutToIMEInput方法监听输入内容，判断输入内容是否图片名称，并完成替换动作。具体实现如下：

1. 添加变量imageList存放所有图片的名称信息。
2. 使用aboutToIMEInput方法监听输入内容是否为“@”，当输入“@”时赋值标志符flag为true。
3. 当输入空格时结束输入图片名，并判断当前图片是否存在。
4. 使用deleteSpans删除当前“@XXX”，并使用addImageSpan添加对应图片内容。

以下为代码示例：

```ts
@Entry
@Component
struct RichEditorReplaceImageDemo {
  controller: RichEditorController = new RichEditorController();
  @State pictureName: string = '';
  @State start: number = 0;
  // 当前是否输入@符号
  @State flag: boolean = false;
  // 存放图片名称
  imageList: Array<string> = ['logo', 'startIcon'];

  build() {
    Column() {
      RichEditor({ controller: this.controller })
        .aboutToIMEInput((value: RichEditorInsertValue) => {
          if (value.insertValue === '@') {
            this.flag = true;
            this.start = this.controller.getCaretOffset();
            return true;
          }
          if (!this.flag) {
            return true;
          }
          // 设置通过空格结束输入图片名
          if (value.insertValue === ' ') {
            // 判断当前图片是否存在
            if (this.imageList.includes(this.pictureName)) {
              this.controller.deleteSpans({ start: this.start, end: this.controller.getCaretOffset() });
              this.controller.addImageSpan($r('app.media.' + this.pictureName), {
                imageStyle: { size: ['100px', '100px'] }
              });
            }
            // 重置标志符
            this.flag = false;
            this.pictureName = '';
          } else {
            this.pictureName += value.insertValue;
          }
          return true;
        })
        .width('98%')
        .height('30%')
        .borderWidth(1);
    }
    .width('100%')
    .height('100%');
  }
}
```
