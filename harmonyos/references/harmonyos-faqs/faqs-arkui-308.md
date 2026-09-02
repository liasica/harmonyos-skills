---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-308
title: 如何将内容直接复制到剪贴板
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何将内容直接复制到剪贴板
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:71085afe9f5b11b856bb0dad3146eea591106cbd7a8f569782a82770c47bb8f2
---

通过[@ohos.pasteboard（剪贴板）](../harmonyos-references/js-apis-pasteboard.md)模块提供的管理系统剪贴板能力，可以为系统复制、粘贴功能提供支持。系统剪贴板支持对文本、HTML、URI、Want、PixelMap等内容的操作。

示例如下：

1. 使用pasteboard.createData创建剪贴板内容对象，传入数据类型和内容。
2. 使用pasteboard.getSystemPasteboard获取系统剪贴板对象。
3. 通过获取系统剪贴板对象并调用setData方法，将数据写入剪贴板。调用getData方法，读取剪贴板的内容。

   ```ts
   import { pasteboard } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct CopyText {
     private textContent: string = 'Copy me';

     aboutToAppear(): void {
       AppStorage.setOrCreate('context', this.getUIContext());
     }

     build() {
       Column() {
         Text(this.textContent)
           .fontSize(20)
           .borderRadius(9)
           .borderWidth(1)
           .padding({
             left: 8,
             right: 8
           })
           .fontColor($r('sys.color.ohos_id_color_text_primary'))
           .fontWeight(FontWeight.Medium)
           .opacity($r('sys.float.ohos_id_alpha_content_secondary'))
           .onClick(() => copyText(this.textContent))
       }
       .width('100%')
       .height('100%')
       .justifyContent(FlexAlign.Center)
       .alignSelf(ItemAlign.Center)
     }
   }

   /*
    * Copy the text to the system clipboard
    * @param text - text
    * @returns void
    */
   function copyText(text: string) {
     const uiContext: UIContext | undefined = AppStorage.get('context');
     // Create clipboard content object
     const pasteboardData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, text);
     // Get system clipboard object
     const systemPasteboard = pasteboard.getSystemPasteboard();
     systemPasteboard.setData(pasteboardData); // Put data into clipboard
     systemPasteboard.getData().then((data) => { // Read clipboard content
       if (data) {
         uiContext?.getPromptAction().showToast({ message: 'Copy succeeded' });
       } else {
         uiContext?.getPromptAction().showToast({ message: 'Copy failed' });
       }
     })
   }
   ```
