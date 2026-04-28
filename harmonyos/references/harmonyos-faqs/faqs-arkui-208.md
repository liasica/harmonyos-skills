---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-208
title: 是否有处理"9图"（又称"draw9patch"、".9图"、"点9图"等）的平替方案
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 是否有处理"9图"（又称"draw9patch"、".9图"、"点9图"等）的平替方案
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:55+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6022bfc9077928c490000118da922a11e39b729fafe8b54bde7f5a2066f6530d
---

Image组件提供与点九图相同功能的API设置，通过设置resizable属性来配置ResizableOptions，即图像拉伸时的大小调整选项。ResizableOptions的参数slice包含top、left、bottom和right四个属性，分别表示图片在上下左右四个方向拉伸时保持不变的距离。

参考代码如下：

```
1. @Entry
2. @Component
3. struct NineMapPrinciple {
4. build() {
5. Row() {
6. Image($r('app.media.startIcon'))
7. .resizable({ slice: { top: 10, left: 10, bottom: 50, right: 50 } })
8. }
9. .height('50%')
10. }
11. }
```

[HandleDrawNineMapPrinciple.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/HandleDrawNineMapPrinciple.ets#L21-L31)

点九图的常见用法是实现聊天气泡的拉伸效果，参考代码如下：

```
1. @Entry
2. @Component
3. struct ChatBubbleStretchDemo {
4. @State text: string = 'Hello World Hello World Hello World Hello World';
5. @State left: number = 10;
6. @State right: number = 10;
7. @State top: number = 10;
8. @State bottom: number = 10;
9. @State line: number = 2;
10. @State textSize: SizeOptions = this.getUIContext().getMeasureUtils().measureTextSize({
11. textContent: this.text
12. });

14. build() {
15. Column() {
16. Stack() {
17. Image($r('app.media.lightBluexhdpi'))
18. .width(this.getUIContext().px2vp(Number(`${this.textSize.width}`)) < 350 ? 60 + px2vp
19. (Number(`${this.textSize.width}`)) : 350)
20. .height(this.text.length < 40 ? 50 + px2vp(Number(`${this.textSize.height}`))
21. : 50 + (this.getUIContext().px2vp(Number(`${this.textSize.height}`)) * this.line))
22. // The reason for using the px unit is that the image itself is a physical pixel, and the segmentation algorithm is executed on the image itself. Therefore, these values are ultimately converted into physical pixel values.
23. // Therefore, these divided lines must not exceed the size of the picture itself.
24. .resizable({
25. slice: {
26. top: `${this.top}px`,
27. left: `${this.left}px`,
28. bottom: `${this.bottom}px`,
29. right: `${this.right}px`
30. }
31. })
32. Text(this.text)
33. }
34. .width(350)
35. .height(200)
36. }
37. .height('100%')
38. .width('100%')
39. }
40. }
```

[HandleDrawNinePatchReplacementRegimen.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/HandleDrawNinePatchReplacementRegimen.ets#L21-L61)

效果如图所示。

正常大小

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/2pi3HoDuRCiwpmG26Qs6pw/zh-cn_image_0000002229758793.png?HW-CC-KV=V1&HW-CC-Date=20260428T002553Z&HW-CC-Expire=86400&HW-CC-Sign=4BA1070F17D19CCA22C13B14E29B624A26D684322AB2B2AE2A1D3A0B62A6B42D "点击放大")

左右拉伸操作

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/PQ_FricPSiGHex6JtRL7MA/zh-cn_image_0000002194158916.png?HW-CC-KV=V1&HW-CC-Date=20260428T002553Z&HW-CC-Expire=86400&HW-CC-Sign=9F2F0CD34302DA5A7C5ECB1C3DEBBC4CC40BC2F2593B2F8EF8C0C13BAE8AFC52 "点击放大")

支持多行上下左右拉伸

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/BwAvisWpTW--uTA_PeNCuA/zh-cn_image_0000002194318528.png?HW-CC-KV=V1&HW-CC-Date=20260428T002553Z&HW-CC-Expire=86400&HW-CC-Sign=3DD4F111D6A21D7176B90A6AF722D37D2030DAAED92C1A2152AA3AD1A2752476 "点击放大")

上述示例实现的是图片拉伸中间，四周保持不变。还有另一种拉伸方式，实现图片拉伸四周，中间保持不变，示例如下。

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. @Entry
4. @Component
5. struct DrawingLatticeResizeDemo {
6. // lattice grid definition
7. private xDivs: Array<number> = [40, 100, 120, 180];
8. private yDivs: Array<number> = [];
9. private fXCount: number = 4;
10. private fYCount: number = 0;
11. private drawingLatticeFirst: DrawingLattice =
12. drawing.Lattice.createImageLattice(this.xDivs, this.yDivs, this.fXCount, this.fYCount);
13. @State widthValue: number = 260;
14. @State heightValue: number = 260;

16. build() {
17. Scroll() {
18. Column({ space: 20 }) {
19. Text('Dynamic Resize by Lattice')
20. .fontSize(22)
21. .fontWeight(FontWeight.Bold)

23. // The picture shows
24. Image($r('app.media.lightBluexhdpi'))
25. .width(String(this.widthValue) + 'px')
26. .height(String(this.heightValue) + 'px')
27. .borderWidth(2)
28. .resizable({
29. lattice: this.drawingLatticeFirst
30. })

32. // Width adjustment
33. Column({ space: 5 }) {
34. Text(`Width: ${this.widthValue.toFixed(0)} px`)
35. Slider({
36. value: this.widthValue,
37. min: 100,
38. max: 400,
39. step: 10
40. })
41. .onChange(value => {
42. this.widthValue = value;
43. })
44. }

46. // Height adjustment
47. Column({ space: 5 }) {
48. Text(`Width: ${this.heightValue.toFixed(0)} px`)
49. Slider({
50. value: this.heightValue,
51. min: 78,
52. max: 400,
53. step: 10
54. })
55. .onChange(value => {
56. this.heightValue = value;
57. })
58. }
59. }
60. .width('100%')
61. .padding(20)
62. }
63. }
64. }
```

[ResizableStretchAround.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ResizableStretchAround.ets#L22-L86)

**参考链接**

[ResizableOptions](../harmonyos-references/ts-basic-components-image.md#resizableoptions11)
