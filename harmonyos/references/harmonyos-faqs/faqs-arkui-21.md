---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-21
title: 如何加载和使用自定义字体
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何加载和使用自定义字体
category: harmonyos-faqs
scraped_at: 2026-04-29T14:16:11+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c8628bbb266b292af0a47817e3788eb3d3517eb7b3be2249ef82dc760781a4bc
---

1. 字体管理中[@ohos.font (注册自定义字体)](../harmonyos-references/js-apis-font.md)。
2. 设置对应文本的字体家族。可参考以下代码：

   ```
   1. // xxx.ets
   2. import { Font } from '@kit.ArkUI';

   4. @Entry
   5. @Component
   6. struct FontExample {
   7. @State message: string = 'Hello World';

   9. aboutToAppear() {
   10. // Register in black font
   11. let font: Font = this.getUIContext().getFont()
   12. font.registerFont({
   13. familyName: 'Condensed_Black', // Registered font name
   14. familySrc: '/font/Sans_Condensed_Black.ttf' // The font folder is at the same level as the pages directory
   15. })

   17. // Register in black oblique font
   18. font.registerFont({
   19. familyName: 'Condensed_Black_Italic', // Registered font name
   20. familySrc: '/font/Sans_Condensed_Black_Italic.ttf' // The font folder is at the same level as the pages directory
   21. })
   22. }

   24. build() {
   25. Column() {
   26. Text(this.message)
   27. .align(Alignment.Center)
   28. .fontSize(50)
   29. .fontFamily('Condensed_Black') // Use black font
   30. Text(this.message)
   31. .align(Alignment.Center)
   32. .fontSize(50)
   33. .fontFamily('Condensed_Black_Italic') // Use black oblique font
   34. Text(this.message)
   35. .align(Alignment.Center)
   36. .fontSize(50)
   37. }
   38. .width('100%')
   39. .margin({ top: 30 })
   40. }
   41. }
   ```

   [LoadingAndUsingCustomFonts.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/LoadingAndUsingCustomFonts.ets#L21-L61)

效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/xguF_tpOSSCNgzsuLxmTlQ/zh-cn_image_0000002194158888.png?HW-CC-KV=V1&HW-CC-Date=20260429T061610Z&HW-CC-Expire=86400&HW-CC-Sign=3E9412415365D00347E1EBF243E34AA08A972751B789477823A192CB2707716F "点击放大")
