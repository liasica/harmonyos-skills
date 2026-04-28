---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-308
title: 如何将内容直接复制到剪贴板
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何将内容直接复制到剪贴板
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:18+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f60634cef010c1774b01ed2678a78afdde0948fe94f5373f39b4b16b9514b7d3
---

通过[@ohos.pasteboard（剪贴板）](../harmonyos-references/js-apis-pasteboard.md)模块提供的管理系统剪贴板能力，可以为系统复制、粘贴功能提供支持。系统剪贴板支持对文本、HTML、URI、Want、PixelMap等内容的操作。

示例如下：

1. 使用pasteboard.createData创建剪贴板内容对象，传入数据类型和内容。
2. 使用pasteboard.getSystemPasteboard获取系统剪贴板对象。
3. 通过获取系统剪贴板对象并调用setData方法，将数据写入剪贴板。调用getData方法，读取剪贴板的内容。

   ```
   1. import { pasteboard } from '@kit.BasicServicesKit';

   3. @Entry
   4. @Component
   5. struct CopyText {
   6. private textContent: string = 'Copy me';

   8. aboutToAppear(): void {
   9. AppStorage.setOrCreate('context', this.getUIContext());
   10. }

   12. build() {
   13. Column() {
   14. Text(this.textContent)
   15. .fontSize(20)
   16. .borderRadius(9)
   17. .borderWidth(1)
   18. .padding({
   19. left: 8,
   20. right: 8
   21. })
   22. .fontColor($r('sys.color.ohos_id_color_text_primary'))
   23. .fontWeight(FontWeight.Medium)
   24. .opacity($r('sys.float.ohos_id_alpha_content_secondary'))
   25. .onClick(() => copyText(this.textContent))
   26. }
   27. .width('100%')
   28. .height('100%')
   29. .justifyContent(FlexAlign.Center)
   30. .alignSelf(ItemAlign.Center)
   31. }
   32. }

   34. /*
   35. * Copy the text to the system clipboard
   36. * @param text - text
   37. * @returns void
   38. */
   39. function copyText(text: string) {
   40. const uiContext: UIContext | undefined = AppStorage.get('context');
   41. // Create clipboard content object
   42. const pasteboardData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, text);
   43. // Get system clipboard object
   44. const systemPasteboard = pasteboard.getSystemPasteboard();
   45. systemPasteboard.setData(pasteboardData); // Put data into clipboard
   46. systemPasteboard.getData().then((data) => { // Read clipboard content
   47. if (data) {
   48. uiContext?.getPromptAction().showToast({ message: 'Copy succeeded' });
   49. } else {
   50. uiContext?.getPromptAction().showToast({ message: 'Copy failed' });
   51. }
   52. })
   53. }
   ```

   [CopyContentDirectlyClipboard.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/CopyContentDirectlyClipboard.ets#L21-L73)
