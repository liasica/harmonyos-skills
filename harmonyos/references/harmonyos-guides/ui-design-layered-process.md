---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-layered-process
title: （推荐）分层图标处理
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 图标处理 > （推荐）分层图标处理
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:10f057a1898121280030291a5f971a23ab3639c18812e196dda660c2ef7f7370
---

## 场景介绍

从5.0.0(12)版本开始， Hds支持分层图标处理能力。

适用于图标为分层资源，且图标展示风格要与华为HarmonyOS Design System设计风格一致的应用场景。以下是一些典型的应用场景：

* 展示带图标的应用列表：可调用UI Design Kit批量处理分层图标的接口获取处理后的应用图标。
* 展示应用详情：可调用UI Design Kit处理单个分层图标的接口获取处理后的应用图标。
* 展示跟随在线主题的应用图标：可调用UI Design Kit处理分层图标的接口获取主题换肤后的应用图标。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/o1p22WigTO2fOCI8rao9RQ/zh-cn_image_0000002552958330.png?HW-CC-KV=V1&HW-CC-Date=20260427T234149Z&HW-CC-Expire=86400&HW-CC-Sign=36934F1B63BB68315BE942FF6B09D4A9DB39CCCC95EA29B178D36EC8A4BD580A)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/SUILzQutRC2GXbIPhziHQQ/zh-cn_image_0000002583478331.png?HW-CC-KV=V1&HW-CC-Date=20260427T234149Z&HW-CC-Expire=86400&HW-CC-Sign=44755A8E39A2551D0F58C2F6F5572AF763EC17262FB8437715BF18E749E13CF9)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/d6mnuKrqRN2lpk5g2n79lQ/zh-cn_image_0000002552798682.png?HW-CC-KV=V1&HW-CC-Date=20260427T234149Z&HW-CC-Expire=86400&HW-CC-Sign=B88830F0564423461536EA9BF6E7621CE2F2F8689AF19A789590446564684258)

## 约束条件

分层图标处理支持Phone、Tablet、PC/2in1设备，并且从5.1.1(19)版本开始，新增支持TV设备。

## 开发步骤

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/SyDK8D7oSlm0Yh49soqwiQ/zh-cn_image_0000002583438377.png?HW-CC-KV=V1&HW-CC-Date=20260427T234149Z&HW-CC-Expire=86400&HW-CC-Sign=48BAC53B0B3CDCD584065C6AE7C02F6C4149F5961F77409A72ACE281F509792B)

1. 设置分层图标，将前景资源和背景资源放至entry/src/main/resources/base/media文件中，并在该目录下创建一个json文件（例如：drawable.json）：

   ```
   1. {
   2. "layered-image":
   3. {
   4. "background" : "$media:background",
   5. "foreground" : "$media:foreground"
   6. }
   7. }
   ```
2. 将图标处理的相关类添加至工程。

   ```
   1. import { LayeredDrawableDescriptor } from '@kit.ArkUI';
   2. import { hdsDrawable } from '@kit.UIDesignKit';
   3. import { image } from '@kit.ImageKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   5. import { resourceManager } from '@kit.LocalizationKit';
   6. import { common } from '@kit.AbilityKit';
   ```
3. 简单配置页面的布局，调用[分层图标接口](../harmonyos-references/ui-design-hdsdrawable.md#hdsdrawablegethdslayeredicon)获取处理后的图标信息，也可以调用[异步批量处理接口](../harmonyos-references/ui-design-hdsdrawable.md#hdsdrawablegethdslayeredicons)。

   ```
   1. @Entry
   2. @Component
   3. struct Index{
   4. bundleName: string = 'com.example.uidesignkit';
   5. resManager: resourceManager.ResourceManager | undefined = undefined;
   6. layeredDrawableDescriptor: LayeredDrawableDescriptor | undefined = undefined;
   7. @State layeredIconsResult: Array<hdsDrawable.ProcessedIcon> = [];

   9. build() {
   10. Column() {
   11. Column() {
   12. Text('getHdsLayeredIcon')
   13. .fontWeight(FontWeight.Bold)
   14. .fontSize(16)
   15. .margin(5)

   17. Image(this.getHdsLayeredIcon())
   18. .width(48)
   19. .height(48)
   20. }
   21. .margin(20)

   23. Text('getHdsLayeredIcons')
   24. .fontWeight(FontWeight.Bold)
   25. .fontSize(16)
   26. .margin(5)

   28. List() {
   29. ForEach(this.layeredIconsResult,
   30. (item: hdsDrawable.ProcessedIcon, index?: number) => {
   31. ListItem() {
   32. Column() {
   33. Text(item.bundleName)
   34. .fontWeight(FontWeight.Medium)
   35. .fontSize(16)
   36. .margin(5)

   38. Image(item.pixelMap)
   39. .width(48)
   40. .height(48)
   41. }
   42. .margin(15)
   43. }
   44. .width('100%')
   45. }, (item: string) => item.toString())
   46. }
   47. .scrollBar(BarState.On)
   48. .height('60%')
   49. }
   50. .height('100%')
   51. .width('100%')
   52. }

   54. aboutToAppear(): void {
   55. // 获取资源管理器
   56. this.resManager = (this.getUIContext().getHostContext() as common.UIAbilityContext)?.resourceManager;
   57. if (!this.resManager) {
   58. return;
   59. }
   60. // 通过资源管理获取原始分层图标信息
   61. this.layeredDrawableDescriptor = (this.resManager.getDrawableDescriptor($r('app.media.drawable')
   62. .id)) as LayeredDrawableDescriptor;
   63. this.getHdsLayeredIcons();
   64. }

   66. private getHdsLayeredIcon(): image.PixelMap | null {
   67. try {
   68. // 调用HDS分层图标接口处理图标
   69. return hdsDrawable.getHdsLayeredIcon(this.bundleName, this.layeredDrawableDescriptor, 48, true);
   70. } catch (err) {
   71. let message = (err as BusinessError).message;
   72. let code = (err as BusinessError).code;
   73. console.error(`getHdsLayeredIcon failed, code: ${code}, message: ${message}`);
   74. return null;
   75. }
   76. }

   78. private getHdsLayeredIcons(): void {
   79. if (!this.layeredDrawableDescriptor) {
   80. console.error(`getHdsLayeredIcons layeredDrawableDescriptor is undefined.`);
   81. return;
   82. }

   84. // 构造批量接口传参
   85. let options: hdsDrawable.Options = {
   86. size: 48,
   87. hasBorder: true,
   88. parallelNumber: 4
   89. };

   91. let layeredIcons: Array<hdsDrawable.LayeredIcon> = [];
   92. for (let i = 0; i < 10; i++) {
   93. layeredIcons.push({
   94. bundleName: `${this.bundleName}-${i}`,
   95. layeredDrawableDescriptor: this.layeredDrawableDescriptor
   96. });
   97. }

   99. try {
   100. // 调用HDS批量分层接口处理图标
   101. hdsDrawable.getHdsLayeredIcons(layeredIcons, options)
   102. .then((data: Array<hdsDrawable.ProcessedIcon>) => {
   103. console.info(`getHdsLayeredIcons data size: ${data.length}`);
   104. this.layeredIconsResult = data;
   105. })
   106. .catch((err: BusinessError) => {
   107. console.error(`getHdsLayeredIcons return error, code: ${err.code}, msg: ${err.message}`);
   108. });
   109. } catch (err) {
   110. let message = (err as BusinessError).message;
   111. let code = (err as BusinessError).code;
   112. console.error(`getHdsLayeredIcons failed, code: ${code}, message: ${message}`);
   113. }
   114. }
   115. }
   ```
