---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-implementing-image-resizable
title: 基于resizable实现图片拉伸效果
breadcrumb: 最佳实践 > 主题与样式 > 基于resizable实现图片拉伸效果
category: best-practices
scraped_at: 2026-04-28T08:20:02+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:cfdcbd4fdd23798486ef1956aa21208c7e050d2c8e30847ce255b4f174bc1053
---

## 概述

在一些开发场景中，图片需适配不同尺寸的容器。若直接拉伸，容易导致关键区域（如圆角、边框或图案细节）变形、模糊，影响视觉效果。典型例子如聊天消息气泡，其背景图需随内容长度和高度动态调整。

Image组件提供的[resizable](../harmonyos-references/ts-basic-components-image.md#resizable11)属性，可精准指定图片的可拉伸区域与固定区域，从而确保图片在不同尺寸的容器中都能保持良好的视觉效果。

本文将以聊天消息气泡和可拉伸占位图两个典型场景为例，介绍如何使用resizable属性实现图片拉伸效果。

## 实现原理

通过Image组件的resizable属性实现精准图片拉伸，其核心原理是：使用特定规则划分图片的固定区域与可拉伸区域，当图片拉伸时，仅对可拉伸区域进行拉伸，固定区域保持原始尺寸与形态不变。

resizable属性参数类型为[ResizableOptions](../harmonyos-references/ts-basic-components-image.md#resizableoptions11)，支持使用slice(slice: { left, right, top, bottom })和lattice(lattice: [DrawingLattice](../harmonyos-references/ts-basic-components-image.md#drawinglattice12))两种图片拉伸方案。

### 使用slice拉伸图片

通过slice参数指定原图片在上、下、左、右四个方向的偏移值（px像素点），将图片划分为九宫格布局：四个角的区域为固定区域，其余为可拉伸区域。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/PGaoWRRITEOXtQf8VXHJ6A/zh-cn_image_0000002538512611.png?HW-CC-KV=V1&HW-CC-Date=20260428T002001Z&HW-CC-Expire=86400&HW-CC-Sign=C192C438B0C15DBC9A30911CF481CE34CFA9125B086C8E5584924094CAD15F21 "点击放大")

下图展示了图片拉伸时各区域的拉伸效果。四个角的区域保持固定的宽高，中间区域可上下左右拉伸，顶部和底部的可拉伸区域保持高度不变，左右两侧的可拉伸区域保持宽度不变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/5ia1P7ScQNanrfxFJn8Nyw/zh-cn_image_0000002538592581.png?HW-CC-KV=V1&HW-CC-Date=20260428T002001Z&HW-CC-Expire=86400&HW-CC-Sign=0EA36A0468F63BBA19C1225C68ED2E42077CB847771DBBEC18A4216FDF8C1CE8 "点击放大")

slice除了在resizable属性中使用，还支持在[backgroundImageResizable](../harmonyos-references/ts-universal-attributes-background.md#backgroundimageresizable12)属性中使用。

需要注意的是，坐标参数传入数字时，默认单位为vp，最终会被转化为px。若要使固定区域的显示效果在不同设备上保持一致，需传入px像素单位的数据。

```
1. Image($r('app.media.bg_right_message'))
2. // ...
3. .resizable({
4. slice: {
5. left: '40px',
6. top: '80px',
7. right: '70px',
8. bottom: '40px'
9. }
10. })
```

[ChatMessageView.ets](https://gitcode.com/HarmonyOS_Samples/resizable-image/blob/master/entry/src/main/ets/view/ChatMessageView.ets#L88-L105)

### 使用lattice拉伸图片

通过设置lattice参数，可以利用原图水平和垂直方向的坐标点数组（px像素点）将图片划分为规则矩形网格，行列数为数组长度+1。其中，偶数行与偶数列交叉处的格子为固定区域（如下图中蓝色部分所示），其余区域为可拉伸区域。拉伸时，固定区域保持原尺寸，其他区域根据需要进行拉伸。

例如，下图使用x轴坐标点数组[1, 50, 648]和y轴坐标点数组，将图像划分为3行3列的网格，图中蓝色区域即为偶数行与偶数列相交的固定区域。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/2Heat1_GSbW2k-E5Nr9NIA/zh-cn_image_0000002506872706.png?HW-CC-KV=V1&HW-CC-Date=20260428T002001Z&HW-CC-Expire=86400&HW-CC-Sign=0ED88DBEEB13E313962F5EBA13BD32D7DBFBC4DD034607E0DFCE546CE74FA0B2 "点击放大")

说明

需要注意的是，此处的行列数计数从0行0列开始。例如，上述蓝色区域为0行0列、0行2列、2行0列、2行2列，均为偶数行列交叉区域，属于固定不可拉伸区域。

示例代码如下：

```
1. // Array of x-coordinate values for image segmentation,
2. // where the coordinates refer to pixel positions in the original image
3. private xDivs: Array<number> = [1, 60, 243];
4. // Array of y-coordinate values for image segmentation,
5. // where the coordinates refer to pixel positions in the original image
6. private yDivs: Array<number> = [1, 50, 253];
7. // Divide the original image into a (3+1)×(3+1) grid (based on the division coordinates above)
8. private drawingLatticeFirst: DrawingLattice =
9. drawing.Lattice.createImageLattice(this.xDivs, this.yDivs, this.xDivs.length, this.yDivs.length);
10. // ...
11. Image($r('app.media.placeholder_img'))
12. .height(this.imgHeight)
13. .width('100%')
14. .resizable({
15. lattice: this.drawingLatticeFirst
16. })
17. // ...
```

[PlaceholderImgView.ets](https://gitcode.com/HarmonyOS_Samples/resizable-image/blob/master/entry/src/main/ets/view/PlaceholderImgView.ets#L32-L82)

相较于使用slice实现图片拉伸（仅能指定四个角的区域不可拉伸），lattice功能实现图片拉伸更为灵活，通过设置合理的坐标参数，可指定任意区域进行拉伸或保持不变。

### 使用slice与lattice实现图片拉伸对比

下面对比了slice与lattice的实现方式及适用场景，开发者可参考以选择合适的方案。

| 对比维度 | slice参数实现 | lattice参数实现 |
| --- | --- | --- |
| 核心实现逻辑 | 通过上、下、左、右四个偏移量定义四个角的区域为固定区域。 | 通过横向与纵向的坐标点，将图片划分为网格矩阵，偶数行与偶数列的交叉区域为固定区域。 |
| 适用场景 | 适用于四个角不拉伸的场景，例如聊天消息气泡、输入框背景、优惠券背景等。 | 适用于更复杂或中间区域不拉伸的场景，如带Logo的占位图、四周带装饰的卡片背景、复杂边框的弹窗背景等。 |

## 使用slice实现聊天消息气泡

### 场景描述

聊天消息气泡在社交应用中是一种常见场景，效果如下图所示。当消息内容的长度和高度不同时，消息气泡需保持四周圆角和小三角指示符的形状不变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/bkv2t4hhTRaKKgybADyx5w/zh-cn_image_0000002506712868.png?HW-CC-KV=V1&HW-CC-Date=20260428T002001Z&HW-CC-Expire=86400&HW-CC-Sign=F5465E845ECC5A115396816421E23C52822FD6B585B69C0C8B612EF5DC76F9DA "点击放大")

### 场景实现

通过slice方案实现消息气泡场景，主要方案是通过保持四周的圆角和三角形固定不变来实现的，具体步骤如下：

1. 将图片划分为网格区域，确定对应的偏移值。

   开发者可以通过UX提供的坐标点或者使用PhotoShop等图片编辑工具，找到原始图固定区域上、下、左、右准确的偏移值。消息气泡图片区域划分和坐标点如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/dfzObmjjRxW3U6OtmCQOHA/zh-cn_image_0000002538512613.png?HW-CC-KV=V1&HW-CC-Date=20260428T002001Z&HW-CC-Expire=86400&HW-CC-Sign=19B15DE36C6228DF45E220C530A9D5CF8ACD64F092552990BD96EFE87BE1759F "点击放大")
2. 实现消息气泡布局。

   slice支持在[backgroundImageResizable](../harmonyos-references/ts-universal-attributes-background.md#backgroundimageresizable12)属性中使用。开发者可直接为消息内容的Text组件设置backgroundImage属性，将其作为内容的背景图片。当内容宽高不同时，背景图片会随之进行伸缩。然后，将前面获取的偏移值（{ left: '70px', top: '80px', right: '40px', bottom: '40px' }），赋给Text组件backgroundImageResizable属性中的slice参数即可。

   ```
   1. Text(this.message)
   2. .fontSize($r('sys.float.Body_L'))
   3. .fontColor($r('sys.color.font_primary'))
   4. // Set the background image
   5. .backgroundImage($r('app.media.bg_left_message'))
   6. // Set the maximum width and minimum width/height of the text
   7. // to avoid abnormal display when content is too much or too little.
   8. .constraintSize({
   9. maxWidth: 'calc(100% - 90vp)',
   10. minHeight: 40,
   11. minWidth: 50
   12. })
   13. // Set the padding of the text content
   14. .padding({
   15. left: 20,
   16. top: 10,
   17. right: 10,
   18. bottom: 10
   19. })
   20. // Set the size of the background image
   21. .backgroundImageSize({
   22. height: '100%',
   23. width: '100%'
   24. })
   25. // Set the offset value of the fixed area (nine-grid slice)
   26. .backgroundImageResizable({
   27. slice: {
   28. left: '70px',
   29. top: '80px',
   30. right: '40px',
   31. bottom: '40px'
   32. }
   33. })
   ```

   [ChatMessageView.ets](https://gitcode.com/HarmonyOS_Samples/resizable-image/blob/master/entry/src/main/ets/view/ChatMessageView.ets#L36-L68)

## 使用lattice实现可拉伸占位图

### 场景描述

可拉伸占位图需实现边缘区域可拉伸，而中间的Logo区域保持不变，如下图所示。针对可拉伸占位图场景，本文将采用lattice属性实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/g_UDY5BMRtu_H22Bapom4Q/zh-cn_image_0000002538592583.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002001Z&HW-CC-Expire=86400&HW-CC-Sign=DE724FC4CE0FCB4491CF7DCFF0A923AE773FBB9E0ECC64BC62EE8B600449215D "点击放大")

### 场景实现

可拉伸占位图的中间区域为固定部分。根据[使用lattice拉伸图片](bpta-implementing-image-resizable.md#section0797147172420)的原理，开发者在划分图片时，需将中间区域划分为偶数行与偶数列的交叉点。具体实现步骤如下：

1. 将图片划分为网格区域，确定坐标点数组。

   图片Logo区域的坐标数组，可由UX设计人员提供，或由开发者通过Photoshop等图像编辑工具手动定位获取。示例场景中，该区域的x轴坐标数组为[150, 648]，y轴坐标数组为[150, 733]。若直接使用该坐标点数组，图片将被划分为3行3列的网格，Logo区域将位于第1行第1列（非偶数行和列）的交叉点，无法达到预期效果。如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/HDmvQ30WRtGl1PnZQu9owQ/zh-cn_image_0000002506872708.png?HW-CC-KV=V1&HW-CC-Date=20260428T002001Z&HW-CC-Expire=86400&HW-CC-Sign=B150F59AA99A37941D41EA895FA6034D02B9596461088C5D0D8C5945D4742619 "点击放大")

   为解决此问题，可在x轴和y轴各增加一个坐标点，使Logo区域位于第2行第2列（偶数行和列）的交叉点。为避免影响显示效果，可在原坐标前添加一个较小的坐标值，如1。如此，新的x轴坐标点数组变为[1, 150, 648]，y轴坐标点数组变为[1, 150, 733]，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/iemmYw4vSkSVPn8WxKcIww/zh-cn_image_0000002506712870.png?HW-CC-KV=V1&HW-CC-Date=20260428T002001Z&HW-CC-Expire=86400&HW-CC-Sign=1B5EF057D7C9DDAF2546B9FCBB70AF90026D4062ACAAA83B68E8824D3D38E422 "点击放大")
2. 实现可拉伸占位图布局。

   根据上述获得的x轴和y轴坐标点数组，使用[createImageLattice()](../harmonyos-references/arkts-apis-graphics-drawing-lattice.md#createimagelattice12)方法创建矩形网格对象，并设置给lattice参数。

   ```
   1. @Component
   2. struct PlaceholderImgView {
   3. // Default image height
   4. @State imgHeight: Length = '35%';
   5. // Flag indicating whether the image is stretched
   6. @State isEnlarge: boolean = false;
   7. // Array of x-coordinate values for image segmentation,
   8. // where the coordinates refer to pixel positions in the original image
   9. private xDivs: Array<number> = [1, 60, 243];
   10. // Array of y-coordinate values for image segmentation,
   11. // where the coordinates refer to pixel positions in the original image
   12. private yDivs: Array<number> = [1, 50, 253];
   13. // Divide the original image into a (3+1)×(3+1) grid (based on the division coordinates above)
   14. private drawingLatticeFirst: DrawingLattice =
   15. drawing.Lattice.createImageLattice(this.xDivs, this.yDivs, this.xDivs.length, this.yDivs.length);
   16. // ...

   18. build() {
   19. NavDestination() {
   20. Stack() {
   21. Image($r('app.media.placeholder_img'))
   22. .height(this.imgHeight)
   23. .width('100%')
   24. .resizable({
   25. lattice: this.drawingLatticeFirst
   26. })
   27. .onClick(() => {
   28. if (this.isEnlarge) {
   29. this.imgHeight = '35%';
   30. } else {
   31. this.imgHeight = '100%';
   32. }
   33. this.isEnlarge = !this.isEnlarge;
   34. })
   35. }
   36. }
   37. // ...
   38. }
   39. }
   ```

   [PlaceholderImgView.ets](https://gitcode.com/HarmonyOS_Samples/resizable-image/blob/master/entry/src/main/ets/view/PlaceholderImgView.ets#L25-L84)

## 常见问题

### 给Image组件设置resizable属性之后，在不同手机上的拉伸区域显示效果不一致

**问题描述**

在使用resizable的slice参数设置不拉伸区域之后，在手机和平板上的显示效果不一致，在手机上显示正常，但是在平板上不可拉伸区域会变形。

**可能原因**

开发者在使用resizable设置slice参数时，可能直接传入无单位的数字，该参数会默认以vp为单位。由于不同设备对vp单位的px换算比例存在差异，最终会导致固定区域的显示效果不一致。

**解决方案**

建议使用px作为参数单位，示例代码如下：

```
1. Image($r('app.media.bg_right_message'))
2. // ...
3. .resizable({
4. slice: {
5. left: '40px',
6. top: '80px',
7. right: '70px',
8. bottom: '40px'
9. }
10. })
```

[ChatMessageView.ets](https://gitcode.com/HarmonyOS_Samples/resizable-image/blob/master/entry/src/main/ets/view/ChatMessageView.ets#L88-L105)

### 设置resizable属性后未生效，图片仍然被拉伸变形

**问题描述**

通过slice或lattice给图片设定了不可拉伸区域，图片拉伸时该区域依旧会变形。

**可能原因**

1. 使用slice或lattice划分不可拉伸区域时，坐标值定位不准确，无法精准锁定目标区域，导致不可拉伸区域划分错误。
2. slice或lattice参数配置异常，比如参数值超出图片宽高范围，或是设置了无效的参数值。

**解决方案**

1. 若因坐标点定位不准导致问题，开发者可参考[实现原理](bpta-implementing-image-resizable.md#section318520366349)章节，重新校准并划分不可拉伸区域的坐标点。
2. 若因参数设置异常导致问题，开发者需要保证坐标点在图片区域内。
   * 对于lattice的x轴坐标点数组元素的值，需要大于等于0，并且小于图片宽度；对于lattice的y轴坐标点数组元素的值，需要大于等于0，并且小于图片高度。
   * 对于slice参数值的取值范围，可以参考[ResizableOptions](../harmonyos-references/ts-basic-components-image.md#resizableoptions11)中slice的参数说明。

## 示例代码

* [基于resizable实现图片拉伸效果](https://gitcode.com/harmonyos_samples/resizable-image)
