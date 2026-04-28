---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-normal-process
title: 单层图标处理
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 图标处理 > 单层图标处理
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b47a0bb4e24bf155e0498762734d203c8779c99d5cbf74ab011cd79fe926a7cb
---

## 场景介绍

从5.0.0(12)版本开始， Hds支持单层图标处理能力。

适用于图标为单层资源，且图标展示风格要与华为HarmonyOS Design System设计风格一致的应用场景，典型应用场景可参考分层图标[场景介绍](ui-design-layered-process.md#场景介绍)。

## 约束条件

单层图标处理支持Phone、Tablet、PC/2in1设备，并且从5.1.1(19)版本开始，新增支持TV设备。

## 开发步骤

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/Ax3YQuh0TOqNzoKU-W2m2A/zh-cn_image_0000002552958332.png?HW-CC-KV=V1&HW-CC-Date=20260427T234149Z&HW-CC-Expire=86400&HW-CC-Sign=D932FFEBB26EAD273A7FB212D19C2C352754CF9240DA64AD202872FFDB2B8661)

1. 在entry/src/main/resources/base/media下，配置一张图片资源normal\_icon.png。
2. 将图标处理的相关类添加至工程。

   ```
   1. import { LayeredDrawableDescriptor, DrawableDescriptor } from '@kit.ArkUI';
   2. import { hdsDrawable } from '@kit.UIDesignKit';
   3. import { image } from '@kit.ImageKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   5. import { resourceManager } from '@kit.LocalizationKit';
   6. import { common } from '@kit.AbilityKit';
   ```
3. 简单配置页面的布局，调用[单层图标接口](../harmonyos-references/ui-design-hdsdrawable.md#hdsdrawablegethdsicon)获取处理后的图标信息，也可以调用[异步批量处理接口](../harmonyos-references/ui-design-hdsdrawable.md#hdsdrawablegethdsicons)。

   ```
   1. @Entry
   2. @Component
   3. struct Index{
   4. bundleName: string = 'com.example.uidesignkit';
   5. resManager: resourceManager.ResourceManager | undefined = undefined;
   6. layeredDrawableDescriptor: LayeredDrawableDescriptor | undefined = undefined;
   7. drawableDescriptor: DrawableDescriptor | undefined = undefined;
   8. @State iconsResult: Array<hdsDrawable.ProcessedIcon> = [];

   10. build() {
   11. Column() {
   12. Column() {
   13. Text('getHdsIcon')
   14. .fontWeight(FontWeight.Bold)
   15. .fontSize(16)
   16. .margin(5)

   18. Image(this.getHdsIcon())
   19. .width(48)
   20. .height(48)
   21. }
   22. .margin(20)

   24. Text('getHdsIcons')
   25. .fontWeight(FontWeight.Bold)
   26. .fontSize(16)
   27. .margin(5)

   29. List() {
   30. ForEach(this.iconsResult,
   31. (item: hdsDrawable.ProcessedIcon, index?: number) => {
   32. ListItem() {
   33. Column() {
   34. Text(item.bundleName)
   35. .fontWeight(FontWeight.Medium)
   36. .fontSize(16)
   37. .margin(5)

   39. Image(item.pixelMap)
   40. .width(48)
   41. .height(48)
   42. }
   43. .margin(15)
   44. }
   45. .width('100%')
   46. }, (item: string) => item.toString())
   47. }
   48. .scrollBar(BarState.On)
   49. .height('60%')
   50. }
   51. .height('100%')
   52. .width('100%')
   53. }

   55. aboutToAppear(): void {
   56. // 获取资源管理器
   57. this.resManager = (this.getUIContext().getHostContext() as common.UIAbilityContext)?.resourceManager;
   58. if (!this.resManager) {
   59. return;
   60. }

   62. // 通过资源管理获取分层图标信息
   63. this.layeredDrawableDescriptor = (this.resManager.getDrawableDescriptor($r('app.media.drawable').id)) as LayeredDrawableDescriptor;

   65. // 通过资源管理获取单层图标信息
   66. this.drawableDescriptor =
   67. (this.resManager?.getDrawableDescriptor($r('app.media.normal_icon').id)) as DrawableDescriptor;

   69. this.getHdsIcons();
   70. }

   72. private getHdsIcon(): image.PixelMap | null {
   73. try {
   74. // 调用HDS单层图标接口
   75. return hdsDrawable.getHdsIcon(this.bundleName, this.drawableDescriptor?.getPixelMap(), 48,
   76. this.layeredDrawableDescriptor?.getMask().getPixelMap(), true);
   77. } catch (err) {
   78. let message = (err as BusinessError).message;
   79. let code = (err as BusinessError).code;
   80. console.error(`getHdsIcon failed, code: ${code}, message: ${message}`);
   81. return null;
   82. }
   83. }

   85. getHdsIcons(): void {
   86. if (!this.drawableDescriptor) {
   87. console.error(`getHdsIcons drawableDescriptor is undefined.`);
   88. return;
   89. }

   91. if (!this.layeredDrawableDescriptor) {
   92. console.error(`getHdsIcons layeredDrawableDescriptor is undefined.`);
   93. return;
   94. }

   96. // 构造批量接口传参
   97. let options: hdsDrawable.Options = {
   98. size: 48,
   99. hasBorder: true,
   100. parallelNumber: 4
   101. };

   103. let icons: Array<hdsDrawable.Icon> = [];
   104. for (let i = 0; i < 10; i++) {
   105. icons.push({
   106. bundleName: `${this.bundleName}-${i}`,
   107. pixelMap: this.drawableDescriptor.getPixelMap()
   108. })
   109. }

   111. try {
   112. // 调用HDS单层批量接口处理图标
   113. hdsDrawable.getHdsIcons(icons, this.layeredDrawableDescriptor.getMask().getPixelMap(), options)
   114. .then((data: Array<hdsDrawable.ProcessedIcon>) => {
   115. console.info(`getHdsIcons data size: ${data.length}`);
   116. this.iconsResult = data;
   117. })
   118. .catch((err: BusinessError) => {
   119. console.error(`getHdsIcons error, code: ${err.code}, msg: ${err.message}`);
   120. });
   121. } catch (err) {
   122. let message = (err as BusinessError).message;
   123. let code = (err as BusinessError).code;
   124. console.error(`getHdsIcons callback failed: ${message}, code: ${code}`);
   125. }
   126. }
   127. }
   ```
