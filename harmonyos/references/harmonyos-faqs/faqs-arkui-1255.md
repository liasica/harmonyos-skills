---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1255
title: RichEditor粘贴时去除文字源格式
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > RichEditor粘贴时去除文字源格式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6af53b9736970488ed0a0476724345800cb95c17ea422c4b7fd93b35506beebc
---

## 问题现象

RichEditor支持输入带有样式的图文，在复制有样式的图文后，粘贴时如何去除复制的图文样式？

## 背景知识

* [RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)是支持图文混排和文本交互式编辑的组件。
* [onPaste](../harmonyos-references/ts-basic-components-richeditor.md#onpaste11)方法在完成粘贴前，触发回调。开发者可以通过该方法，覆盖系统默认行为，实现图文的粘贴。preventDefault用于阻止系统默认粘贴事件。[addTextSpan](../harmonyos-references/ts-basic-components-richeditor.md#addtextspan)用于添加文本内容。
* [@ohos.pasteboard (剪贴板)](../harmonyos-references/js-apis-pasteboard.md)模块主要提供管理系统剪贴板的能力，为系统复制、粘贴功能提供支持。[pasteboard.getSystemPasteboard](../harmonyos-references/js-apis-pasteboard.md#pasteboardgetsystempasteboard)方法可以获取系统剪贴板对象。[getPrimaryText](../harmonyos-references/js-apis-pasteboard.md#getprimarytext)获取第一条纯文本内容。

## 解决方案

实现的思路如下：

1. 监听页面粘贴事件：在RichEditor组件中设置onPaste事件处理函数，当用户粘贴内容时触发。
2. 阻止默认粘贴行为：在事件处理函数中调用event.preventDefault()，阻止RichEditor默认的粘贴行为，避免保留原有样式。
3. 获取剪贴板数据：使用pasteboard.getSystemPasteboard()获取系统剪贴板实例，然后调用getData方法获取剪贴板中的数据。
4. 提取纯文本内容：从剪贴板数据中提取纯文本内容，使用pasteData.getPrimaryText()方法获取纯文本。
5. 插入指定样式的文本：使用RichEditorController的addTextSpan方法，将提取的纯文本以指定的样式（如字体大小和颜色）插入到编辑器中，从而去除原有样式。

参考代码如下：

```ts
import pasteboard from '@ohos.pasteboard';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct richEditorPage {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };

  build() {
    RelativeContainer() {
      RichEditor(this.options)
        .width(300)
        .height(400)
        .backgroundColor('#fafafa')
        // 粘贴时，触发回调。
        .onPaste((event?: PasteEvent) => {
          if (event !== undefined && event.preventDefault) {
            // 阻止默认粘贴行为
            event.preventDefault();
            // 获取系统剪贴板实例
            let systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
            // 获取剪贴板数据
            systemPasteboard.getData((err: BusinessError, pasteData: pasteboard.PasteData) => {
              if (err) {
                console.error(`Failed to get PasteData. Code:${err.code} ,message:${err.message}`);
                return;
              }
              // 提取纯文本内容
              let text: string = pasteData.getPrimaryText();
              this.controller.addTextSpan(text, { style: { fontSize: 16, fontColor: Color.Gray } });
            });
          }
        })
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        });
    }
    .height('100%')
    .width('100%');
  }
}
```
