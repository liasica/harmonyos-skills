---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor
title: @ohos.arkui.drawableDescriptor (DrawableDescriptor)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.drawableDescriptor (DrawableDescriptor)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9fc768cdf6cb81323ebb38a1622b14f87c1b939796c79af12874de33d1c4bb51
---

本模块提供分层图标合成（包括前景，背景，蒙版），动图播放与控制，基础图像处理的能力。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import {
2. DrawableDescriptor,
3. LayeredDrawableDescriptor,
4. AnimatedDrawableDescriptor,
5. AnimationOptions,
6. AnimationController
7. } from '@kit.ArkUI';
```

## DrawableDescriptorLoadedResult21+

PhonePC/2in1TabletTVWearable

传入的图片资源或地址的加载结果。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| imageWidth | number | 否 | 否 | 图片的宽度。  单位：px |
| imageHeight | number | 否 | 否 | 图片的高度。  单位：px |

**示例：**

```
1. import { AnimatedDrawableDescriptor, AnimationOptions, DrawableDescriptor, DrawableDescriptorLoadedResult } from '@kit.ArkUI';

3. let options: AnimationOptions = { duration: 2000, iterations: 1 };
4. let drawable: DrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), options)
5. try {
6. // 可以提前手动加载动图资源到内存中。
7. let result: DrawableDescriptorLoadedResult = drawable.loadSync()
8. console.info(`load result = ${JSON.stringify(result)}`)
9. } catch(e) {
10. console.error("load failed")
11. }
```

## DrawableDescriptor

PhonePC/2in1TabletTVWearable

父类对象提供可重写的方法，包含：获取[PixelMap](arkts-apis-image-pixelmap.md)实例，图片资源加载能力。

### getPixelMap

PhonePC/2in1TabletTVWearable

getPixelMap(): image.PixelMap

获取PixelMap实例。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [image.PixelMap](arkts-apis-image-pixelmap.md) | PixelMap |

**示例：**

示例请参考[LayeredDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#layereddrawabledescriptor)中的示例代码。

### loadSync21+

PhonePC/2in1TabletTVWearable

loadSync(): DrawableDescriptorLoadedResult

发起图片资源的同步加载，并返回加载结果。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DrawableDescriptorLoadedResult](js-apis-arkui-drawabledescriptor.md#drawabledescriptorloadedresult21) | 图片资源的加载结果。 |

**错误码：**

以下错误码的详细介绍请参见[DrawableDescriptor错误码](errorcode-drawable-descriptor.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 111001 | resource loading failed. |

```
1. import { AnimatedDrawableDescriptor, DrawableDescriptor, DrawableDescriptorLoadedResult, AnimationOptions } from '@kit.ArkUI';

3. let options: AnimationOptions = { duration: 2000, iterations: 1 };
4. let drawable: DrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), options)
5. try {
6. // 可以提前手动加载动图资源到内存中
7. let result: DrawableDescriptorLoadedResult = drawable.loadSync()
8. console.info(`load result = ${JSON.stringify(result)}`)
9. } catch(e) {
10. console.error("load failed")
11. }
```

### load21+

PhonePC/2in1TabletTVWearable

load(): Promise<DrawableDescriptorLoadedResult>

发起图片资源的异步加载，并返回加载结果。使用Promise异步回调。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DrawableDescriptorLoadedResult](js-apis-arkui-drawabledescriptor.md#drawabledescriptorloadedresult21)> | 图片资源的加载结果。 |

**错误码：**

以下错误码的详细介绍请参见[DrawableDescriptor错误码](errorcode-drawable-descriptor.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 111001 | resource loading failed. |

```
1. import {
2. AnimatedDrawableDescriptor,
3. DrawableDescriptor,
4. DrawableDescriptorLoadedResult,
5. AnimationOptions
6. } from '@kit.ArkUI';

8. let options: AnimationOptions = { duration: 2000, iterations: 1 };
9. let drawable: DrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), options)
10. drawable.load().then((result: DrawableDescriptorLoadedResult) => {
11. console.info(`load result = ${JSON.stringify(result)}`)
12. }).catch(() => {
13. console.info(`load failed`)
14. })
```

## PixelMapDrawableDescriptor12+

PhonePC/2in1TabletTVWearable

支持通过传入PixelMap创建PixelMapDrawableDescriptor对象。继承自[DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor)。

### constructor12+

PhonePC/2in1TabletTVWearable

constructor(src?: image.PixelMap)

PixelMapDrawableDescriptor的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | PixelMap类型参数，存储 PixelMap 图片数据。 |

## LayeredDrawableDescriptor

PhonePC/2in1TabletTVWearable

当传入资源id或name为包含前景和背景资源的json文件时，生成LayeredDrawableDescriptor对象。继承自[DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor)。

drawable.json位于项目工程entry/src/main/resources/base/media目录下。定义请参考：

```
1. {
2. "layered-image":
3. {
4. "background" : "$media:background",
5. "foreground" : "$media:foreground"
6. }
7. }
```

**示例：**

使用json文件创建LayeredDrawableDescriptor，示例代码如下。

```
1. // xxx.ets
2. import { DrawableDescriptor, LayeredDrawableDescriptor } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Index {
7. private resManager = this.getUIContext().getHostContext()?.resourceManager;
8. // $r('app.media.drawable')需要替换为开发者所需的图像资源文件。
9. private layeredDrawableDescriptor: DrawableDescriptor | undefined =
10. this.resManager?.getDrawableDescriptor($r('app.media.drawable').id);

12. build() {
13. Row() {
14. Column() {
15. Image((this.layeredDrawableDescriptor instanceof LayeredDrawableDescriptor) ?
16. this.layeredDrawableDescriptor : undefined)
17. Image((this.layeredDrawableDescriptor instanceof LayeredDrawableDescriptor) ?
18. this.layeredDrawableDescriptor?.getForeground()?.getPixelMap() : undefined)
19. }.height('50%')
20. }.width('50%')
21. }
22. }
```

使用PixelMapDrawableDescriptor创建LayeredDrawableDescriptor，示例代码如下。

```
1. import { DrawableDescriptor, LayeredDrawableDescriptor, PixelMapDrawableDescriptor } from '@kit.ArkUI';
2. import { image } from '@kit.ImageKit';

4. @Entry
5. @Component
6. struct Index {
7. @State fore1: image.PixelMap | undefined = undefined;
8. @State back1: image.PixelMap | undefined = undefined;

10. @State foregroundDraw: DrawableDescriptor | undefined = undefined;
11. @State backgroundDraw: DrawableDescriptor | undefined = undefined;
12. @State maskDraw: DrawableDescriptor | undefined = undefined;
13. @State maskPixel: image.PixelMap | undefined = undefined;
14. @State draw: LayeredDrawableDescriptor | undefined = undefined;

16. async aboutToAppear() {
17. // $r('app.media.foreground')需要替换为开发者所需的图像资源文件。
18. this.fore1 = await this.getPixmapFromMedia($r('app.media.foreground'));
19. // $r('app.media.background')需要替换为开发者所需的图像资源文件。
20. this.back1 = await this.getPixmapFromMedia($r('app.media.background'));
21. // $r('app.media.ohos_icon_mask')需要替换为开发者所需的图像资源文件。
22. this.maskPixel = await this.getPixmapFromMedia($r('app.media.ohos_icon_mask'));
23. // 使用PixelMapDrawableDescriptor创建LayeredDrawableDescriptor。
24. this.foregroundDraw = new PixelMapDrawableDescriptor(this.fore1);
25. this.backgroundDraw = new PixelMapDrawableDescriptor(this.back1);
26. this.maskDraw = new PixelMapDrawableDescriptor(this.maskPixel);
27. this.draw = new LayeredDrawableDescriptor(this.foregroundDraw,this.backgroundDraw,this.maskDraw);
28. }

30. build() {
31. Row() {
32. Column() {
33. Image(this.draw)
34. .width(300)
35. .height(300)
36. }.height('100%').justifyContent(FlexAlign.Center)
37. }.width('100%').height("100%").backgroundColor(Color.Pink)
38. }
39. // 根据资源，通过图片框架获取pixelMap。
40. private async getPixmapFromMedia(resource: Resource) {
41. let unit8Array = await this.getUIContext().getHostContext()?.resourceManager?.getMediaContent(resource.id);
42. let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength));
43. let createPixelMap: image.PixelMap = await imageSource.createPixelMap({
44. desiredPixelFormat: image.PixelMapFormat.BGRA_8888
45. });
46. await imageSource.release();
47. return createPixelMap;
48. }
49. }
```

### constructor12+

PhonePC/2in1TabletTVWearable

constructor(foreground?: DrawableDescriptor, background?: DrawableDescriptor, mask?: DrawableDescriptor)

LayeredDrawableDescriptor的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| foreground | [DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor) | 否 | 分层图标的前景图片选项。 |
| background | [DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor) | 否 | 分层图标的背景图片选项。 |
| mask | [DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor) | 否 | 分层图标的遮罩选项。 |

### getForeground

PhonePC/2in1TabletTVWearable

getForeground(): DrawableDescriptor

获取前景的DrawableDescriptor对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor) | DrawableDescriptor对象。 |

**示例：**

```
1. import { DrawableDescriptor, LayeredDrawableDescriptor } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State drawableDescriptor: DrawableDescriptor | undefined = undefined;

8. private getForeground(): DrawableDescriptor | undefined {
9. let resManager = this.getUIContext().getHostContext()?.resourceManager;
10. // $r('app.media.drawable')需要替换为开发者所需的图像资源文件。
11. let drawable: DrawableDescriptor | undefined = resManager?.getDrawableDescriptor($r('app.media.drawable').id);
12. if (!drawable) {
13. return undefined;
14. }
15. if (drawable instanceof LayeredDrawableDescriptor) {
16. let layeredDrawableDescriptor = (drawable as LayeredDrawableDescriptor).getForeground();
17. return layeredDrawableDescriptor;
18. }
19. return undefined;
20. }

22. aboutToAppear(): void {
23. this.drawableDescriptor = this.getForeground();
24. }

26. build() {
27. RelativeContainer() {
28. if (this.drawableDescriptor) {
29. Image(this.drawableDescriptor)
30. .width(100)
31. .height(100)
32. .borderWidth(1)
33. .backgroundColor(Color.Green);
34. }
35. }
36. .height('100%')
37. .width('100%')
38. }
39. }
```

### getBackground

PhonePC/2in1TabletTVWearable

getBackground(): DrawableDescriptor

获取背景的DrawableDescriptor对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor) | DrawableDescriptor对象。 |

**示例：**

```
1. import { DrawableDescriptor, LayeredDrawableDescriptor } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State drawableDescriptor: DrawableDescriptor | undefined = undefined;

8. private getBackground(): DrawableDescriptor | undefined {
9. let resManager = this.getUIContext().getHostContext()?.resourceManager;
10. // $r('app.media.drawable')需要替换为开发者所需的图像资源文件。
11. let drawable: DrawableDescriptor | undefined = resManager?.getDrawableDescriptor($r('app.media.drawable').id);
12. if (!drawable) {
13. return undefined;
14. }
15. let layeredDrawableDescriptor = (drawable as LayeredDrawableDescriptor).getBackground();
16. return layeredDrawableDescriptor;
17. }

19. aboutToAppear(): void {
20. this.drawableDescriptor = this.getBackground();
21. }

23. build() {
24. RelativeContainer() {
25. if (this.drawableDescriptor) {
26. Image(this.drawableDescriptor)
27. .width(100)
28. .height(100)
29. }
30. }
31. .height('100%')
32. .width('100%')
33. }
34. }
```

### getMask

PhonePC/2in1TabletTVWearable

getMask(): DrawableDescriptor

获取蒙版的DrawableDescriptor对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor) | DrawableDescriptor对象。 |

**示例：**

```
1. import { DrawableDescriptor, LayeredDrawableDescriptor } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State drawableDescriptor: DrawableDescriptor | undefined = undefined;

8. private getMask(): DrawableDescriptor | undefined {
9. let resManager = this.getUIContext().getHostContext()?.resourceManager;
10. // $r('app.media.drawable')需要替换为开发者所需的图像资源文件。
11. let drawable: DrawableDescriptor | undefined = resManager?.getDrawableDescriptor($r('app.media.drawable').id);
12. if (!drawable) {
13. return undefined;
14. }
15. let layeredDrawableDescriptor = (drawable as LayeredDrawableDescriptor).getMask();
16. return layeredDrawableDescriptor;
17. }

19. aboutToAppear(): void {
20. this.drawableDescriptor = this.getMask();
21. }

23. build() {
24. RelativeContainer() {
25. if (this.drawableDescriptor) {
26. Image(this.drawableDescriptor)
27. .width(100)
28. .height(100)
29. }
30. }
31. .height('100%')
32. .width('100%')
33. }
34. }
```

### getMaskClipPath

PhonePC/2in1TabletTVWearable

static getMaskClipPath(): string

LayeredDrawableDescriptor的静态方法，获取系统内置的裁切路径参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回裁切路径的命令字符串。 |

**示例：**

```
1. // xxx.ets
2. import { DrawableDescriptor, LayeredDrawableDescriptor } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
11. Image($r('app.media.icon'))
12. .width('200px').height('200px')
13. .clipShape(new Path({commands:LayeredDrawableDescriptor.getMaskClipPath()}))
14. Text(`获取系统内置的裁剪路径参数：`)
15. .fontWeight(800)
16. Text(JSON.stringify(LayeredDrawableDescriptor.getMaskClipPath()))
17. .padding({ left: 20, right: 20 })
18. }.height('100%').justifyContent(FlexAlign.Center)
19. }.width('100%')
20. }
21. }
```

### setBlendMode23+

PhonePC/2in1TabletTVWearable

setBlendMode(mode: drawing.BlendMode): void

设置LayeredDrawableDescriptor的混合模式。对同一LayeredDrawableDescriptor对象多次调用setBlendMode接口时，仅在绘制完成前的最后一次调用生效。该接口不支持动态切换。LayeredDrawableDescriptor的默认绘制顺序为背景、蒙版、前景。设置了混合模式后，绘制顺序变为背景、前景、蒙版。若设置的值无效，则按照未设置混合模式进行绘制。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [drawing.BlendMode](arkts-apis-graphics-drawing-e.md#blendmode) | 是 | 混合模式。 |

**示例：**

```
1. import { DrawableDescriptor, LayeredDrawableDescriptor } from '@kit.ArkUI';
2. import { image } from '@kit.ImageKit';
3. import { drawing } from '@kit.ArkGraphics2D';

5. @Entry
6. @Component
7. struct Index {
8. @State drawableDescriptor: DrawableDescriptor | undefined = undefined;

10. private setBlendMode(blendMode: drawing.BlendMode): DrawableDescriptor | undefined {
11. let resManager = this.getUIContext().getHostContext()?.resourceManager;
12. // $r('app.media.drawable')需要替换为开发者提供的分层图标文件。
13. let drawable: DrawableDescriptor | undefined = resManager?.getDrawableDescriptor($r('app.media.drawable').id);
14. if (!drawable) {
15. return undefined;
16. }
17. let layeredDrawableDescriptor = drawable as LayeredDrawableDescriptor;
18. layeredDrawableDescriptor.setBlendMode(blendMode);
19. return layeredDrawableDescriptor;
20. }

22. aboutToAppear(): void {
23. this.drawableDescriptor = this.setBlendMode(drawing.BlendMode.SRC_OVER);
24. }

26. build() {
27. RelativeContainer() {
28. if (this.drawableDescriptor) {
29. Image(this.drawableDescriptor)
30. .width(100)
31. .height(100)
32. }
33. }
34. .height('100%')
35. .width('100%')
36. }
37. }
```

## AnimationOptions12+

PhonePC/2in1TabletTVWearable

动画播放参数。包括播放时延，迭代次数，单帧播放时间，是否自动播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| duration | number | 否 | 是 | 设置图片数组播放总时间。  PixelMap数组的默认值是每张图片播放1秒。本地图片或者应用资源的默认值是图片资源中携带的播放时延。  单位：毫秒  取值范围：[0, +∞)  设置负数取默认值。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| iterations | number | 否 | 是 | 设置图片数组播放次数。  值为-1时表示无限播放，值为0时表示不播放，值大于0时表示有限的播放次数。  默认值为1。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| frameDurations21+ | Array<number> | 否 | 是 | 设置动图中的单帧播放时间。不设置则按照总时间播放。  设置的优先级高于duration，即同时设置了duration和frameDurations时，duration不生效。  当设置的frameDurations长度与图片的数量不一致时，按照总时间播放。  单位：毫秒  **元服务API：** 从API version 21开始，该接口支持在元服务中使用。 |
| autoPlay21+ | boolean | 否 | 是 | 设置动图是否自动播放。  true表示自动播放，false表示不自动播放。  默认值为true。  **元服务API：** 从API version 21开始，该接口支持在元服务中使用。 |

**示例：**

```
1. import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';
2. import { image } from '@kit.ImageKit';

4. @Entry
5. @Component
6. struct Example {
7. pixelMaps: Array<image.PixelMap> = [];
8. // 设置了4张图，同时设置4张图的duration。
9. options: AnimationOptions = {
10. duration: 2000,
11. iterations: 1,
12. frameDurations: [20, 30, 40, 50],
13. autoPlay: true
14. };
15. @State animated?: DrawableDescriptor = undefined;

17. aboutToAppear() {
18. // $r('app.media.png1')需要替换为开发者所需的图像资源文件。
19. this.pixelMaps.push(this.getPixmapFromMedia($r('app.media.png1')));
20. // $r('app.media.png2')需要替换为开发者所需的图像资源文件。
21. this.pixelMaps.push(this.getPixmapFromMedia($r('app.media.png2')));
22. // $r('app.media.png3')需要替换为开发者所需的图像资源文件。
23. this.pixelMaps.push(this.getPixmapFromMedia($r('app.media.png3')));
24. // $r('app.media.png4')需要替换为开发者所需的图像资源文件。
25. this.pixelMaps.push(this.getPixmapFromMedia($r('app.media.png4')));
26. this.animated = new AnimatedDrawableDescriptor(this.pixelMaps, this.options);
27. }

29. build() {
30. Column() {
31. Row() {
32. Image(this.animated)
33. .width(100)
34. .height(100)
35. }
36. }
37. }

39. private getPixmapFromMedia(resource: Resource) {
40. let unit8Array = this.getUIContext().getHostContext()?.resourceManager?.getMediaContentSync(resource.id);
41. let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength));
42. let pixelMap: image.PixelMap = imageSource.createPixelMapSync({
43. desiredPixelFormat: image.PixelMapFormat.RGBA_8888
44. });
45. imageSource.release();
46. return pixelMap;
47. }
48. }
```

## AnimatedDrawableDescriptor12+

PhonePC/2in1TabletTVWearable

使用[Image](ts-basic-components-image.md)组件播放PixelMap数组或动图资源时传入AnimatedDrawableDescriptor对象，该对象继承自[DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor)。

### constructor12+

PhonePC/2in1TabletTVWearable

constructor(pixelMaps: Array<image.PixelMap>, options?: AnimationOptions)

AnimatedDrawableDescriptor的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pixelMaps | Array<[image.PixelMap](arkts-apis-image-pixelmap.md)> | 是 | PixelMap 数组类型参数，存储 PixelMap 图片数据。 |
| options | [AnimationOptions](js-apis-arkui-drawabledescriptor.md#animationoptions12) | 否 | 动画控制选项。 |

### constructor21+

PhonePC/2in1TabletTVWearable

constructor(src: ResourceStr | Array<image.PixelMap>, options?: AnimationOptions)

AnimatedDrawableDescriptor的构造函数。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [ResourceStr](ts-types.md#resourcestr) | Array<[image.PixelMap](arkts-apis-image-pixelmap.md)> | 是 | 动图资源地址或者[PixelMap](arkts-apis-image-pixelmap.md)对象构成的数组。  ResourceStr当前支持的范围：应用资源Resource，沙箱路径（file://<bundleName>/<sandboxPath>），BASE64字符串。 |
| options | [AnimationOptions](js-apis-arkui-drawabledescriptor.md#animationoptions12) | 否 | 动画控制参数。 |

**示例：**

```
1. import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';
2. import { fileUri } from '@kit.CoreFileKit';

4. @Entry
5. @Component
6. struct Example {
7. options: AnimationOptions = { duration: 1000, iterations: -1, autoPlay: false };
8. // 支持传入file://xx沙箱路径和应用资源Resource。
9. @State animated1: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);
10. @State animated2: AnimatedDrawableDescriptor | undefined = undefined;

12. aboutToAppear() {
13. let files = this.getUIContext().getHostContext()?.filesDir
14. let originPath = files + "/flower.gif"
15. let resultPath = fileUri.getUriFromPath(originPath)
16. this.animated2 = new AnimatedDrawableDescriptor(resultPath, { iterations: -1 })
17. }

19. build() {
20. Column() {
21. Row() {
22. Image(this.animated1).width(100).height(100)
23. Image(this.animated2).width(100).height(100)
24. }
25. }
26. }
27. }
```

### getAnimationController21+

PhonePC/2in1TabletTVWearable

getAnimationController(id?: string): AnimationController | undefined

获取动画控制器。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 | 组件的id。  当[Image](ts-basic-components-image.md)组件与AnimatedDrawableDescriptor确保1比1持有（仅传入一个[Image](ts-basic-components-image.md)组件）时，id非必填；  若同一AnimatedDrawableDescriptor需绑定多个[Image](ts-basic-components-image.md)组件，则必须设置唯一id以准确获取对应组件的动画控制器（唯一性由开发者保证）。  此规则基于动画系统设计原则：动画数据可多组件共享，但各组件动画独立运行，AnimationController与组件严格1比1持有关系（一个组件一个AnimationController对象）。  另外，[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)支持不可见时自动暂停播放功能，详见[onVisibleAreaChange](ts-universal-component-visible-area-change-event.md#onvisibleareachange)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AnimationController](js-apis-arkui-drawabledescriptor.md#animationcontroller21) | undefined | 动画控制器对象。 |

**示例：**

[Image](ts-basic-components-image.md)组件与AnimatedDrawableDescriptor保持1比1持有关系，示例代码如下。

```
1. import { AnimationOptions, AnimatedDrawableDescriptor, AnimationController } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Example {
6. options: AnimationOptions = { duration: 1000, iterations: -1, autoPlay: false };
7. // $r('app.media.gif')需要替换为开发者所需的图像资源文件。
8. @State animated: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);

10. build() {
11. Column() {
12. Image(this.animated)
13. .width(100)
14. .height(100)
15. .borderColor(Color.Red)
16. .borderWidth(1)
17. Button("start")
18. .onClick(() => {
19. let controller = this.animated.getAnimationController()
20. controller?.start()
21. })
22. Button("stop")
23. .onClick(() => {
24. let controller = this.animated.getAnimationController()
25. controller?.stop()
26. })
27. }
28. }
29. }
```

[Image](ts-basic-components-image.md)组件与AnimatedDrawableDescriptor保持1比N持有关系，示例代码如下。

```
1. import { AnimationOptions, AnimatedDrawableDescriptor, AnimationController } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Example {
6. options: AnimationOptions = { duration: 1000, iterations: -1, autoPlay: false };
7. // $r('app.media.gif')需要替换为开发者所需的图像资源文件。
8. @State animated: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);

10. build() {
11. Column() {
12. Image(this.animated)
13. .width(100)
14. .height(100)
15. .borderColor(Color.Red)
16. .borderWidth(1)
17. .id("Component1")
18. Image(this.animated)
19. .width(100)
20. .height(100)
21. .borderColor(Color.Red)
22. .borderWidth(1)
23. Button("start")
24. .onClick(() => {
25. let controller = this.animated.getAnimationController("Component1")
26. controller?.start()
27. })
28. Button("stop")
29. .onClick(() => {
30. let controller = this.animated.getAnimationController("Component1")
31. controller?.stop()
32. })
33. }
34. }
35. }
```

## AnimationController21+

PhonePC/2in1TabletTVWearable

动画控制器对象。包含控制动画播放、停止、恢复、暂停和状态查询等方法。

### start21+

PhonePC/2in1TabletTVWearable

start(): void

从首帧开始播放。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Example {
6. options: AnimationOptions = { duration: 1000, iterations: -1, autoPlay: false };
7. // $r('app.media.gif')需要替换为开发者所需的图像资源文件。
8. @State animated: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);

10. build() {
11. Column() {
12. Image(this.animated)
13. .width(100)
14. .height(100)
15. .onClick(() => {
16. let controller = this.animated.getAnimationController()
17. // 可以通过start启动动图播放。
18. controller?.start()
19. })
20. }
21. }
22. }
```

### stop21+

PhonePC/2in1TabletTVWearable

stop(): void

停止动图的播放并回到首帧。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Example {
6. options: AnimationOptions = { duration: 1000, iterations: -1 };
7. // $r('app.media.gif')需要替换为开发者所需的图像资源文件。
8. @State animated: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);

10. build() {
11. Column() {
12. Image(this.animated)
13. .width(100)
14. .height(100)
15. .onClick(() => {
16. let controller = this.animated.getAnimationController()
17. // 可以在动图播放时，通过stop停下播放并回到动图的首帧。
18. controller?.stop()
19. })
20. }
21. }
22. }
```

### resume21+

PhonePC/2in1TabletTVWearable

resume(): void

在当前帧恢复播放动图。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Example {
6. options: AnimationOptions = { duration: 1000, iterations: -1 };
7. // $r('app.media.gif')需要替换为开发者所需的图像资源文件。
8. @State animated: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);

10. build() {
11. Column() {
12. Image(this.animated)
13. .width(100)
14. .height(100)
15. .onClick(() => {
16. let controller = this.animated.getAnimationController()
17. // 可以在动图暂停或停止时从当前帧开始播放。
18. controller?.resume()
19. })
20. }
21. }
22. }
```

### pause21+

PhonePC/2in1TabletTVWearable

pause(): void

暂停动图的播放，保持在当前帧。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Example {
6. options: AnimationOptions = { duration: 1000, iterations: -1 };
7. // $r('app.media.gif')需要替换为开发者所需的图像资源文件。
8. @State animated: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);

10. build() {
11. Column() {
12. Image(this.animated)
13. .width(100)
14. .height(100)
15. .onClick(() => {
16. let controller = this.animated.getAnimationController()
17. // 可以在动图播放时，暂停播放并保持在当前帧。
18. controller?.pause()
19. })
20. }
21. }
22. }
```

### getStatus21+

PhonePC/2in1TabletTVWearable

getStatus(): AnimationStatus

获取当前动图播放的状态。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AnimationStatus](ts-appendix-enums.md#animationstatus) | 动图的播放状态。包含4种状态：初始态、播放态、暂停态、停止态。 |

**示例：**

```
1. import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Example {
6. options: AnimationOptions = { duration: 1000, iterations: -1 };
7. // $r('app.media.gif')需要替换为开发者所需的图像资源文件。
8. @State animated: AnimatedDrawableDescriptor = new AnimatedDrawableDescriptor($r('app.media.gif'), this.options);

10. statusToString(status: AnimationStatus): string {
11. switch (status) {
12. case AnimationStatus.Initial:
13. return "Initial"
14. case AnimationStatus.Running:
15. return "Running"
16. case AnimationStatus.Paused:
17. return "Paused"
18. case AnimationStatus.Stopped:
19. return "Stopped"
20. default:
21. return "Error"
22. }
23. }

25. build() {
26. Column() {
27. Image(this.animated)
28. .width(100)
29. .height(100)
30. .onClick(() => {
31. let controller = this.animated.getAnimationController()
32. // 获取当前动画的状态。
33. let status = controller?.getStatus()
34. console.info(`animation status = ${this.statusToString(status)}`)
35. })
36. }
37. }
38. }
```
