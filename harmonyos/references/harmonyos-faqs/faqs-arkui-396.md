---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-396
title: 如何实现在图片进行绘制马赛克的效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现在图片进行绘制马赛克的效果
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:44+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:436c6f166342ebfeece24b46326f8aae1f1d8dc1acdae58c9275ab99e8f63874
---

在图片上进行绘制马赛克的效果可通过以下步骤来实现。

1. 给画布添加移动手势。

   ```
   1. import { DrawPathType, DrawViewModel } from '../viewmodel/DrawViewModel';

   3. @Component
   4. export struct DrawView {
   5. @ObjectLink viewModel: DrawViewModel;

   7. build() {
   8. Column({ space: 8 }) {
   9. Text('Please select the brush type')
   10. .fontColor(Color.Red)
   11. .textAlign(TextAlign.Center)
   12. .fontSize(30)
   13. .width('80%')
   14. .margin('10%')

   16. Canvas(this.viewModel.context)
   17. .width('100%')
   18. .height('75%')
   19. .onAreaChange((oldValue: Area, newValue: Area) => {
   20. this.viewModel.canvasAreaChange(newValue);
   21. })
   22. .gesture(
   23. GestureGroup(GestureMode.Exclusive,
   24. PanGesture()
   25. .onActionStart((event: GestureEvent) => {
   26. let finger: FingerInfo = event.fingerList[0];
   27. if (finger == undefined) {
   28. return;
   29. }
   30. let x = finger.localX;
   31. let y = finger.localY;
   32. this.viewModel.moveStart(x, y);
   33. })
   34. .onActionUpdate((event: GestureEvent) => {
   35. let finger: FingerInfo = event.fingerList[0];
   36. if (finger == undefined) {
   37. return;
   38. }
   39. let x = finger.localX;
   40. let y = finger.localY;
   41. this.viewModel.moveUpdate(x, y);
   42. })
   43. .onActionEnd((event: GestureEvent) => {
   44. let finger: FingerInfo = event.fingerList[0];
   45. if (finger == undefined) {
   46. return;
   47. }
   48. this.viewModel.moveEnd();
   49. })
   50. )
   51. )

   53. Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.SpaceAround }) {
   54. Button('Ordinary paintbrush')
   55. .onClick(() => {
   56. this.viewModel.drawModel.pathType = DrawPathType.pen;
   57. })
   58. Button('Mosaic brush')
   59. .onClick(() => {
   60. this.viewModel.drawModel.pathType = DrawPathType.pattern;
   61. })
   62. Button('Clear the content')
   63. .onClick(() => {
   64. this.viewModel.clearPath();
   65. })
   66. }
   67. }
   68. }
   69. }
   ```

   [MosaicEffect.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/MosaicEffect.ets#L21-L89)
2. 绘制路径以及马赛克。

   ```
   1. export class DrawPathPointModel {
   2. x: number = 0;
   3. y: number = 0;
   4. }

   6. export enum DrawPathType {
   7. pen = 0, // Brush
   8. pattern // Mosaic
   9. }

   11. // Configure the brush
   12. export class DrawPathModel {
   13. public pathType: DrawPathType = DrawPathType.pen;
   14. public color: string = '#ED1B1B';
   15. public lineWidth: number = 8;
   16. public img: ImageBitmap = new ImageBitmap('Images/startIcon.png');
   17. }

   19. @Observed
   20. export class DrawViewModel {
   21. public settings: RenderingContextSettings = new RenderingContextSettings(true);
   22. public context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
   23. public drawModel: DrawPathModel = new DrawPathModel();
   24. public canvasHeight: number = 0;
   25. public canvasWidth: number = 0;
   26. private pattern: CanvasPattern | null = null;
   27. private points: DrawPathPointModel[] = [];
   28. // Draw a path
   29. private drawPath = new Path2D();

   31. constructor() {
   32. this.pattern = this.context.createPattern(this.drawModel.img, 'repeat');
   33. }

   35. moveStart(x: number, y: number) {
   36. this.points.push({ x: x, y: y });
   37. this.drawPath.moveTo(x, y);
   38. this.drawCurrentPathModel();
   39. }

   41. moveUpdate(x: number, y: number) {
   42. let lastPoint = this.points[this.points.length - 1];
   43. this.points.push({ x: x, y: y });
   44. this.drawPath.quadraticCurveTo((x + lastPoint.x) / 2, (y + lastPoint.y) / 2, x, y);
   45. this.drawCurrentPathModel();
   46. }

   48. moveEnd() {
   49. this.points = [];
   50. this.drawPath = new Path2D();
   51. }

   53. clearPath() {
   54. this.points = [];
   55. this.drawPath = new Path2D();
   56. this.context.clearRect(0, 0, this.canvasWidth, this.canvasHeight);
   57. }

   59. canvasAreaChange(area: Area) {
   60. this.canvasHeight = area.height as number;
   61. this.canvasWidth = area.width as number;
   62. }

   64. private drawCurrentPathModel() {
   65. this.context.globalCompositeOperation = 'source-over';
   66. this.context.lineWidth = this.drawModel.lineWidth;
   67. if (this.drawModel.pathType == DrawPathType.pen) {
   68. this.context.strokeStyle = this.drawModel.color;
   69. } else {
   70. if (this.pattern) {
   71. this.context.strokeStyle = this.pattern;
   72. }
   73. }
   74. this.context.lineJoin = 'round';
   75. this.context.stroke(this.drawPath);
   76. }
   77. }
   ```

   [DrawViewModel.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/viewmodel/DrawViewModel.ets#L21-L97)
3. 使用Stack组件进行页面布局。

   ```
   1. import { DrawView } from './MosaicEffect';
   2. import { DrawViewModel } from '../viewmodel/DrawViewModel';

   4. @Entry
   5. @Component
   6. struct Index {
   7. @State viewModel: DrawViewModel = new DrawViewModel();

   9. build() {
   10. Stack() {
   11. Image($rawfile('test.jpg'))
   12. .objectFit(ImageFit.Fill)
   13. .width('100%')
   14. .height('100%')

   16. DrawView({ viewModel: this.viewModel })
   17. .width('100%')
   18. .height('100%')
   19. }
   20. }
   21. }
   ```

   [MosaicEffectIndex.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/MosaicEffectIndex.ets#L21-L41)
