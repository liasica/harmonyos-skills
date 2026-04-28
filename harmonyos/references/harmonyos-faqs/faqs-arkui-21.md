---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-21
title: 如何加载和使用自定义字体
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何加载和使用自定义字体
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:03+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:039da50da42e215adb7c9952400d32bc19ec77cf6351303b77c5cc6343d721c1
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/xguF_tpOSSCNgzsuLxmTlQ/zh-cn_image_0000002194158888.png?HW-CC-KV=V1&HW-CC-Date=20260428T002502Z&HW-CC-Expire=86400&HW-CC-Sign=9B1F2088012030A4647AE1E1CF16D7D4AA9C24005A37741A3453F9A818D28444 "点击放大")
