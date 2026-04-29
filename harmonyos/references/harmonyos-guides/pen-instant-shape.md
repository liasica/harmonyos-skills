---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pen-instant-shape
title: 接入一笔成形
breadcrumb: 指南 > 系统 > 硬件 > Pen Kit（手写笔服务） > 手写功能开发 > 接入一笔成形
category: harmonyos-guides
scraped_at: 2026-04-29T13:33:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b3db9f0ac6d84133197a40967b68b00c8a72b11b7abd0aa0c915f38e23e585d2
---

接入一笔成形功能，可以传入手写笔迹的点位信息、通过手写笔/手指在屏幕上停顿一定的时间后触发此功能，触发功能后将自动识别当前绘制的图形，并生成对应的图像信息。

## 场景介绍

在应用中实现一笔成形，效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/BPGzH8EJTfy_HYt8qWz8SA/zh-cn_image_0000002589244781.gif?HW-CC-KV=V1&HW-CC-Date=20260429T053334Z&HW-CC-Expire=86400&HW-CC-Sign=ABBCC5F03854A7E3D4E4F8FED855FC23F8828C972D489EEAD15AE3EEBE394110)

1. 支持获取识别的图像信息，图像信息支持存储。
2. 支持从存储的图像信息中读取信息。

## 接口说明

| 类名 | 接口名 | 说明 |
| --- | --- | --- |
| [InstantShapeGenerator](../harmonyos-references/pen-instantsshapegenerator.md) | [processTouchEvent](../harmonyos-references/pen-instantsshapegenerator.md#processtouchevent) | 传递触摸事件。 |
| [InstantShapeGenerator](../harmonyos-references/pen-instantsshapegenerator.md) | [getPathFromString](../harmonyos-references/pen-instantsshapegenerator.md#getpathfromstring) | 从给定的形状字符串中提取形状信息。 |
| [InstantShapeGenerator](../harmonyos-references/pen-instantsshapegenerator.md) | [notifyAreaChange](../harmonyos-references/pen-instantsshapegenerator.md#notifyareachange) | 通知组件大小变化。 |
| [InstantShapeGenerator](../harmonyos-references/pen-instantsshapegenerator.md) | [setPauseTime](../harmonyos-references/pen-instantsshapegenerator.md#setpausetime) | 设置触发识别的暂停时间，单位：ms。 |
| [InstantShapeGenerator](../harmonyos-references/pen-instantsshapegenerator.md) | [release](../harmonyos-references/pen-instantsshapegenerator.md#release) | 销毁识别工具。 |
| [InstantShapeGenerator](../harmonyos-references/pen-instantsshapegenerator.md) | [onShapeRecognized](../harmonyos-references/pen-instantsshapegenerator.md#onshaperecognized) | 注册识别完成时的回调方法。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { InstantShapeGenerator, ShapeInfo } from '@kit.Penkit';
   ```
2. 构造包含一笔成形能力，下面以控件为例：

   ```
   1. @Entry
   2. @Component
   3. struct InstantShapeDemo {
   4. private instantShapeGenerator: InstantShapeGenerator = new InstantShapeGenerator();
   5. private points: DrawPathPointModel[] = [];
   6. // 绘制路径
   7. private drawPath = new Path2D();
   8. private shapePath = new Path2D();
   9. private mShapeSuccess = false;
   10. private settings: RenderingContextSettings = new RenderingContextSettings(true);
   11. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
   12. // 通过回调方法获取识别结果
   13. private shapeInfoCallback = (shapeInfo: ShapeInfo) => {
   14. this.shapePath = shapeInfo.shapePath;
   15. this.mShapeSuccess = true;
   16. this.context.beginPath();
   17. this.context.reset();
   18. this.drawCurrentPathModel(this.shapePath);
   19. }

   21. aboutToAppear() {
   22. console.info('InstantShapeGenerator aboutToAppear');
   23. // 设置触发识别的暂停时间
   24. this.instantShapeGenerator?.setPauseTime(280);
   25. // 注册完成时的回调方法
   26. this.instantShapeGenerator?.onShapeRecognized(this.shapeInfoCallback);
   27. }

   29. aboutToDisappear() {
   30. console.info('InstantShapeGenerator aboutToDisappear')
   31. this.instantShapeGenerator?.release();
   32. }

   34. build() {
   35. Stack({ alignContent: Alignment.TopEnd }) {
   36. Canvas(this.context)
   37. .width('100%')
   38. .height('100%')
   39. .onAreaChange((oldValue: Area, newValue: Area) => {
   40. // 通知组件大小变化。形状的大小（例如圆的半径）根据组件尺寸而变化
   41. this.instantShapeGenerator?.notifyAreaChange(Number(newValue.width), Number(newValue.height));
   42. }).onTouch((event: TouchEvent) => {
   43. // 传递触摸事件
   44. this.instantShapeGenerator?.processTouchEvent(event);
   45. switch (event.type) {
   46. case TouchType.Down:
   47. this.moveStart(event.touches[0]?.x, event.touches[0]?.y);
   48. break;
   49. case TouchType.Move:
   50. this.moveUpdate(event.touches[0]?.x, event.touches[0]?.y);
   51. break;
   52. case TouchType.Up:
   53. this.moveEnd();
   54. break;
   55. }
   56. })
   57. }.height('100%').width('100%')
   58. }

   60. moveStart(x: number, y: number) {
   61. this.points.push({ x: x, y: y })
   62. this.drawPath.moveTo(x, y);
   63. this.drawCurrentPathModel(this.drawPath);
   64. this.mShapeSuccess = false;
   65. }

   67. moveUpdate(x: number, y: number) {
   68. let lastPoint = this.points[this.points.length - 1];
   69. this.points.push({ x: x, y: y });
   70. this.drawPath.quadraticCurveTo((x + lastPoint?.x) / 2, (y + lastPoint?.y) / 2, x, y);
   71. if (!this.mShapeSuccess) {
   72. this.drawCurrentPathModel(this.drawPath);
   73. }
   74. }

   76. moveEnd() {
   77. this.points = [];
   78. this.drawPath = new Path2D();
   79. this.shapePath = new Path2D();
   80. }

   82. private drawCurrentPathModel(path: Path2D) {
   83. this.context.globalCompositeOperation = 'source-over';
   84. this.context.lineWidth = 8;
   85. this.context.strokeStyle = "#ED1B1B";
   86. this.context.lineJoin = 'round';
   87. this.context.stroke(path);
   88. }
   89. }

   91. export class DrawPathPointModel {
   92. x: number = 0;
   93. y: number = 0;
   94. }
   ```
