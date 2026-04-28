---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pen-suite
title: 接入手写套件
breadcrumb: 指南 > 系统 > 硬件 > Pen Kit（手写笔服务） > 手写功能开发 > 接入手写套件
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e95f225f2af0dda9615466bba91d3549b3d60322185788fc4dd58754b48550dd
---

接入手写套件后，可以在应用中创建手写功能界面。界面包括画布和工具栏两部分，画布部分支持手写笔和手指的书写效果绘制，工具栏部分提供多种笔刷和编辑工具，并支持对手写功能进行设置。接入手写套件后将自动开启一笔成形和报点预测功能，无需再单独接入。

从5.1.0(18)开始，手写套件新增支持设置工具栏默认笔刷、各笔刷默认宽度。

从6.0.0(20)开始，手写套件新增支持自定义画布大小、缩略图能力。

从6.1.0(23)开始，手写套件新增禁用画布缩放、设置滚动位置ScrollTo及监听长画布滚动位置、自定义长画布最大高度能力。

## 场景介绍

在应用中创建手写功能界面，效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/CTd65G1VRt26cIXeQhj2DQ/zh-cn_image_0000002583478477.png?HW-CC-KV=V1&HW-CC-Date=20260427T234441Z&HW-CC-Expire=86400&HW-CC-Sign=6A28774207430E6767CF449ACCC63D10DB9F338A4594C8B561DD622EBDDEB820)

1. 可以加载和显示手写文件。
2. 可以编辑和保存手写文件。
3. Pen Kit手写套件仅支持上下滑动，不支持左右滑动。

## 开发流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/mMfY8JBWSSmPvGrvXzMGaA/zh-cn_image_0000002552798828.png?HW-CC-KV=V1&HW-CC-Date=20260427T234441Z&HW-CC-Expire=86400&HW-CC-Sign=A5DD10CD9E5A18064EEDD428E3B5CA6E3100CAF7C8E41BA704962A82A2ABBAC2)

## 接口说明

| 接口 | 接口描述 |
| --- | --- |
| [HandwriteComponent](../harmonyos-references/pen-handwritecomponent.md) | 构建画布控件 |
| [HandwriteController](../harmonyos-references/pen-handwritecontroller.md) | 画布的主要功能入口类 |

## 开发步骤

1. EntryAbility入口设置Context。

   ```
   1. import { UIAbility } from '@kit.AbilityKit';
   2. import { window } from '@kit.ArkUI';
   3. import GlobalContext from '../utils/ContextConfig';

   5. export default class EntryAbility extends UIAbility {

   7. onWindowStageCreate(windowStage: window.WindowStage): void {
   8. // 主窗口已创建，为此功能设置主页面
   9. windowStage.loadContent('pages/HandWritingDemo', (err) => {
   10. if (err.code) {
   11. return;
   12. }
   13. });
   14. GlobalContext.setContext(this.context);
   15. }
   16. }
   ```
2. 新建GlobalContext类。

   ```
   1. import { common } from "@kit.AbilityKit";

   3. declare namespace globalThis {
   4. let _brushEngineContext: common.UIAbilityContext;
   5. };

   7. export default class GlobalContext {
   8. static getContext(): common.UIAbilityContext {
   9. return globalThis._brushEngineContext;
   10. }

   12. static setContext(context: common.UIAbilityContext): void {
   13. globalThis._brushEngineContext = context;
   14. }
   15. }
   ```
3. 构造包含手写组件的控件/页面，下面以控件为例。

   ```
   1. import { HandwriteController, HandwriteComponent, PenType, PenHspInfo } from '@kit.Penkit';

   3. @Entry
   4. @Component
   5. struct HandWriteDemoComp {
   6. controller: HandwriteController = new HandwriteController();
   7. // 根据应用存储规则，获取到手写文件保存的路径，此处仅为实例参考
   8. initPath: string = this.getUIContext().getHostContext()?.filesDir + '/aa';
   9. penWidth: number = 5;
   10. ballpointPenWidth: number = 6;
   11. @State yOffset: number = 0;

   13. aboutToAppear() {
   14. // 加载时设置保存动作完成后的回调。
   15. this.controller.onLoad(this.callback);
   16. }

   18. // 手写文件内容加载完毕渲染上屏后的回调,通知接入用户,可在此处进行自定义行为
   19. callback = () => {
   20. // 自定义行为,例如文件加载完毕后展示用户操作指导
   21. }

   23. build() {
   24. Row() {
   25. Stack({ alignContent: Alignment.TopStart }) {
   26. HandwriteComponent({
   27. handwriteController: this.controller,
   28. defaultPenType: PenType.PEN, // 可选属性，默认笔刷
   29. defaultPenInfo: [{ penType: PenType.PEN, penWidth: this.penWidth },
   30. { penType: PenType.BALLPOINT_PEN, penWidth: this.ballpointPenWidth }] as PenHspInfo[], // 可选属性，各笔刷的默认宽度
   31. widthRatio: 1, // 可选属性，自定义画布大小，宽度占比（0-1）。
   32. heightRatio: 1, // 可选属性，自定义画布大小，高度占比（0-1）。
   33. maxCanvasHeight: 5000, // 可选属性，自定义画布最大高度
   34. scaleDisabled: false, // 可选属性，是否禁止缩放
   35. onInit: () => {
   36. // 画布初始化完成时的回调。此时可以调用接口加载和显示笔记内容
   37. this.controller?.load(this.initPath);
   38. },
   39. onScale: (scale: number) => {
   40. // 画布缩放时的回调方法，将返回当前手写控件的缩放比例，可在此处进行自定义行为。
   41. },
   42. onDidScroll: (yOffset: number) => {
   43. // 画布滚动时的回调方法，将返回当前滚动位置的纵坐标，可在此处进行自定义行为。
   44. this.yOffset = yOffset
   45. }
   46. })
   47. // 保存及获取缩略图。非必要组件，用户可自行调整或删除。
   48. Button("save")
   49. .onClick(async () => {
   50. // 需根据应用存储规则，获取到手写文件保存的路径，此处仅为实例参考
   51. const path = this.getUIContext().getHostContext()?.filesDir + '/aa';
   52. await this.controller?.save(path).then().catch((error: Error) => {
   53. console.error("save err：" + error.message);
   54. })
   55. // 获取缩略图
   56. this.controller.getThumbnail(this.controller?.getContentRange())?.then((pixelMap: PixelMap) => {
   57. if (pixelMap) {
   58. pixelMap.release()
   59. console.info('getThumbnail success')
   60. }
   61. })
   62. })
   63. // 设置长画布的滚动位置。当前可滚动最大距离为px2vp(1000000)减去list组件高度。
   64. Search()
   65. .searchButton('scrollTo').onSubmit((value: string) => {
   66. if (!Number.isNaN(Number(value))) {
   67. this.controller.scrollTo(Number(value))
   68. }
   69. }).margin({ top: 100 }).width(220)
   70. // 当前画布的偏移量。
   71. Text("onDidScroll：" + this.yOffset)
   72. .margin({ top: 150 }).width(220)
   73. }
   74. .width('100%')
   75. }
   76. .height('100%')
   77. }
   78. }
   ```

完整示例代码可参考[手写笔服务（ArkTS）](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_PenKit-Next-Easy)。
