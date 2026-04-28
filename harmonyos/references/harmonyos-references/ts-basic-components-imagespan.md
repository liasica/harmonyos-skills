---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imagespan
title: ImageSpan
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 文本与输入 > ImageSpan
category: harmonyos-references
scraped_at: 2026-04-28T08:01:52+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7773e689841598b2a68e1912bc51c7a5c213d8207d30636a496935928f05f8b6
---

[Text](ts-basic-components-text.md)、[ContainerSpan](ts-basic-components-containerspan.md)组件的子组件，用于显示行内图片。

说明

该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

ImageSpan(value: ResourceStr | PixelMap)

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 图片的数据源，支持本地图片和网络图片。  当使用相对路径引用图片资源时，例如ImageSpan("common/test.jpg")，不支持跨包/跨模块调用该ImageSpan组件，建议使用$r方式来管理需全局使用的图片资源。  - 支持的图片格式包括png、jpg、bmp、svg、gif和heif。  - 支持Base64字符串。格式data:image/[png|jpeg|bmp|webp|heif];base64,[base64 data]，其中[base64 data]为Base64字符串数据。  - 支持file://data/storage路径前缀的字符串，用于读取本应用安装目录下file文件夹下的图片资源。需要保证目录包路径下的文件有可读权限。 |

## 属性

PhonePC/2in1TabletTVWearable

属性继承自[BaseSpan](ts-basic-components-span.md#basespan)，通用属性方法支持[尺寸设置](ts-universal-attributes-size.md)、[背景设置](ts-universal-attributes-background.md)、[边框设置](ts-universal-attributes-border.md)。

### verticalAlign

PhonePC/2in1TabletTVWearable

verticalAlign(value: ImageSpanAlignment)

设置图片基于行高的对齐方式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ImageSpanAlignment](ts-appendix-enums.md#imagespanalignment10) | 是 | 图片基于行高的对齐方式。  默认值：ImageSpanAlignment.BOTTOM |

### objectFit

PhonePC/2in1TabletTVWearable

objectFit(value: ImageFit)

设置图片的缩放类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ImageFit](ts-appendix-enums.md#imagefit) | 是 | 图片的缩放类型。  默认值：ImageFit.Cover |

### alt12+

PhonePC/2in1TabletTVWearable

alt(value: PixelMap)

设置图片加载过程中显示的占位图。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 设置图片加载过程中显示的占位图，支持[PixelMap](arkts-apis-image-pixelmap.md)类型。  默认值：null |

### colorFilter14+

PhonePC/2in1TabletTVWearable

colorFilter(filter: ColorFilter | DrawingColorFilter)

为图像设置颜色滤镜效果。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filter | [ColorFilter](ts-types.md#colorfilter9) | [DrawingColorFilter](ts-basic-components-image.md#drawingcolorfilter12) | 是 | 1. 给图像设置颜色滤镜效果，入参为一个4x5的RGBA转换矩阵。  矩阵第一行表示R（红色）的向量值，第二行表示G（绿色）的向量值，第三行表示B（蓝色）的向量值，第四行表示A（透明度）的向量值，4行分别代表不同的RGBA的向量值。  当矩阵对角线值为1，其余值为0时，保持图片原有色彩。  **计算规则：**  如果输入的滤镜矩阵为：    像素点为[R, G, B, A]，色值的范围[0, 255]  则过滤后的颜色为 [R’, G’, B’, A’]    2. 支持@ohos.graphics.drawing的ColorFilter类型作为入参。  **说明：**  该接口中的DrawingColorFilter类型支持在元服务中使用。其中，svg类型的图源只对stroke属性生效。 |

### supportSvg222+

PhonePC/2in1TabletTVWearable

supportSvg2(enable: Optional<boolean>)

开启或关闭[SVG标签解析能力增强功能](ts-image-svg2-capabilities.md)，开启后相关SVG图片显示效果会有变化。

ImageSpan组件创建后，不支持动态修改该属性的值。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | Optional<boolean> | 是 | 控制是否开启[SVG标签解析能力增强功能](ts-image-svg2-capabilities.md)。  true：支持SVG解析新能力；false：保持原有SVG解析能力。  默认值：false |

## 事件

PhonePC/2in1TabletTVWearable

通用事件仅支持[点击事件](ts-universal-attributes-click.md)。还支持以下事件：

### onComplete12+

PhonePC/2in1TabletTVWearable

onComplete(callback: ImageCompleteCallback)

图片数据加载成功和解码成功时均触发该回调，返回成功加载的图片尺寸。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ImageCompleteCallback](ts-basic-components-imagespan.md#imagecompletecallback12) | 是 | 图片数据加载成功和解码成功时触发的回调。 |

### onError12+

PhonePC/2in1TabletTVWearable

onError(callback: ImageErrorCallback)

图片加载异常时触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ImageErrorCallback](ts-basic-components-image.md#imageerrorcallback9) | 是 | 图片加载异常时触发的回调。 |

## ImageCompleteCallback12+

PhonePC/2in1TabletTVWearable

type ImageCompleteCallback = (result: ImageLoadResult) => void

图片加载成功和解码成功时触发的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | [ImageLoadResult](ts-basic-components-imagespan.md#imageloadresult12对象说明) | 是 | 图片数据加载成功和解码成功触发回调时返回的对象。 |

## ImageLoadResult12+对象说明

PhonePC/2in1TabletTVWearable

图片数据加载成功和解码成功触发回调时返回的对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number | 否 | 否 | 图片的宽。  单位：[px](ts-pixel-units.md) |
| height | number | 否 | 否 | 图片的高。  单位：[px](ts-pixel-units.md) |
| componentWidth | number | 否 | 否 | 组件的宽。  单位：[px](ts-pixel-units.md) |
| componentHeight | number | 否 | 否 | 组件的高。  单位：[px](ts-pixel-units.md) |
| loadingStatus | number | 否 | 否 | 图片加载成功的状态值。  **说明：**  返回的状态值为0时，表示图片数据加载成功。返回的状态值为1时，表示图片解码成功。 |
| contentWidth | number | 否 | 否 | 图片实际绘制的宽度。  单位：[px](ts-pixel-units.md)  **说明：**  仅在loadingStatus返回1时有效。 |
| contentHeight | number | 否 | 否 | 图片实际绘制的高度。  单位：[px](ts-pixel-units.md)  **说明：**  仅在loadingStatus返回1时有效。 |
| contentOffsetX | number | 否 | 否 | 实际绘制内容相对于组件自身的x轴偏移。  单位：[px](ts-pixel-units.md)  **说明：**  仅在loadingStatus返回1时有效。 |
| contentOffsetY | number | 否 | 否 | 实际绘制内容相对于组件自身的y轴偏移。  单位：[px](ts-pixel-units.md)  **说明：**  仅在loadingStatus返回1时有效。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置对齐方式）

从API version 10开始，该示例通过[verticalAlign](ts-basic-components-imagespan.md#verticalalign)、[objectFit](ts-basic-components-imagespan.md#objectfit)属性展示了ImageSpan组件的对齐方式以及缩放效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SpanExample {
5. build() {
6. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
7. Text() {
8. Span('This is the Span and ImageSpan component').fontSize(25).textCase(TextCase.Normal)
9. .decoration({ type: TextDecorationType.None, color: Color.Pink })
10. }.width('100%').textAlign(TextAlign.Center)

12. Text() {
13. // $r('app.media.app_icon')需要替换为开发者所需的图像资源文件。
14. ImageSpan($r('app.media.app_icon'))
15. .width('200px')
16. .height('200px')
17. .objectFit(ImageFit.Fill)
18. .verticalAlign(ImageSpanAlignment.CENTER)
19. Span('I am LineThrough-span')
20. .decoration({ type: TextDecorationType.LineThrough, color: Color.Red }).fontSize(25)
21. ImageSpan($r('app.media.app_icon'))
22. .width('50px')
23. .height('50px')
24. .verticalAlign(ImageSpanAlignment.TOP)
25. Span('I am Underline-span')
26. .decoration({ type: TextDecorationType.Underline, color: Color.Red }).fontSize(25)
27. ImageSpan($r('app.media.app_icon'))
28. .size({ width: '100px', height: '100px' })
29. .verticalAlign(ImageSpanAlignment.BASELINE)
30. Span('I am Underline-span')
31. .decoration({ type: TextDecorationType.Underline, color: Color.Red }).fontSize(25)
32. ImageSpan($r('app.media.app_icon'))
33. .width('70px')
34. .height('70px')
35. .verticalAlign(ImageSpanAlignment.BOTTOM)
36. Span('I am Underline-span')
37. .decoration({ type: TextDecorationType.Underline, color: Color.Red }).fontSize(50)
38. }
39. .width('100%')
40. .textIndent(50)
41. }.width('100%').height('100%').padding({ left: 0, right: 0, top: 0 })
42. }
43. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/HhotTUHIQeSEQ7wppG9XCQ/zh-cn_image_0000002583479813.png?HW-CC-KV=V1&HW-CC-Date=20260428T000148Z&HW-CC-Expire=86400&HW-CC-Sign=74729E61E0D35645DB3269C1EF50C4487D9963A0B9A89508409BF47FD2D0B32B)

### 示例2（设置背景样式）

从API version 11开始，该示例通过[textBackgroundStyle](ts-basic-components-span.md#textbackgroundstyle11)属性展示了文本设置背景样式的效果。

```
1. // xxx.ets
2. @Component
3. @Entry
4. struct Index {
5. build() {
6. Row() {
7. Column() {
8. Text() {
9. // $r('app.media.sky')需要替换为开发者所需的图像资源文件。
10. ImageSpan($r('app.media.sky'))
11. .width('60vp')
12. .height('60vp')
13. .verticalAlign(ImageSpanAlignment.CENTER)
14. .borderRadius(20)
15. .textBackgroundStyle({ color: '#7F007DFF', radius: "5vp" })
16. }
17. }.width('100%')
18. }.height('100%')
19. }
20. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/5SvfdX3uSg-Eugex8BktZg/zh-cn_image_0000002552800164.png?HW-CC-KV=V1&HW-CC-Date=20260428T000148Z&HW-CC-Expire=86400&HW-CC-Sign=48C8AB7950C3C77C98923EA8B24546D48BB346ADC5EDD3D15152CFEA24B270D1)

### 示例3（为图片添加事件）

从API version 12开始，该示例通过[onComplete](ts-basic-components-imagespan.md#oncomplete12)、[onError](ts-basic-components-imagespan.md#onerror12)为图片添加加载成功和加载异常的事件。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. // $r('app.media.app_icon')需要替换为开发者所需的图像资源文件。
6. @State src: ResourceStr = $r('app.media.app_icon');

8. build() {
9. Column() {
10. Text() {
11. ImageSpan(this.src)
12. .width(100).height(100)
13. .onError((err) => {
14. console.info("onError: " + err.message);
15. })
16. .onComplete((event) => {
17. console.info("onComplete: " + event.loadingStatus);
18. })
19. }
20. }.width('100%').height('100%')
21. }
22. }
```

### 示例4（设置颜色滤镜）

从API version 14开始，该示例通过[colorFilter](ts-basic-components-imagespan.md#colorfilter14)属性展示了给ImageSpan图像设置颜色滤镜的效果。

```
1. // xxx.ets
2. import { drawing } from '@kit.ArkGraphics2D';

4. @Entry
5. @Component
6. struct SpanExample {
7. private ColorFilterMatrix: number[] = [0.239, 0, 0, 0, 0, 0, 0.616, 0, 0, 0, 0, 0, 0.706, 0, 0, 0, 0, 0, 1, 0];
8. @State DrawingColorFilterFirst: ColorFilter | undefined = new ColorFilter(this.ColorFilterMatrix);

10. build() {
11. Row() {
12. Column({ space: 10 }) {
13. //创建ColorFilter对象的方式为图片设置颜色滤镜
14. Text() {
15. // $r('app.media.sky')需要替换为开发者所需的图像资源文件。
16. ImageSpan($r('app.media.sky'))
17. .width('60vp')
18. .height('60vp')
19. .colorFilter(this.DrawingColorFilterFirst)
20. }

22. //通过drawing.ColorFilter的方式为图片设置颜色滤镜
23. Text() {
24. // $r('app.media.sky')需要替换为开发者所需的图像资源文件。
25. ImageSpan($r('app.media.sky'))
26. .width('60vp')
27. .height('60vp')
28. .colorFilter(drawing.ColorFilter.createBlendModeColorFilter({
29. alpha: 255,
30. red: 112,
31. green: 112,
32. blue: 112
33. }, drawing.BlendMode.SRC))
34. }
35. }.width('100%')
36. }.height('100%')
37. }
38. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/hmpr05pbQz-A91ox00vKxg/zh-cn_image_0000002583439859.png?HW-CC-KV=V1&HW-CC-Date=20260428T000148Z&HW-CC-Expire=86400&HW-CC-Sign=7EB5CF1FBAC7B9BCF87DE68694B2205486A1DC95AEE12F76CDE111909E342A08)

### 示例5（设置加载占位图）

从API version 12开始，该示例[alt](ts-basic-components-imagespan.md#alt12)属性展示了ImageSpan设置加载网络图片时占位图的效果。

```
1. // xxx.ets
2. import { http } from '@kit.NetworkKit';
3. import { image } from '@kit.ImageKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct SpanExample {
9. @State imageAlt: PixelMap | undefined = undefined;

11. httpRequest() {
12. // 直接加载网络地址，请填写一个具体的网络图片地址
13. http.createHttp().request("https://www.example.com/xxx.png", (error: BusinessError, data: http.HttpResponse) => {
14. if (error) {
15. console.error(`http request failed with. Code: ${error.code}, message: ${error.message}`);
16. } else {
17. console.info(`http request success.`);
18. let imageData: ArrayBuffer = data.result as ArrayBuffer;
19. let imageSource: image.ImageSource = image.createImageSource(imageData);

21. class tmp {
22. height: number = 100;
23. width: number = 100;
24. }

26. let option: Record<string, number | boolean | tmp> = {
27. 'alphaType': 0, // 透明度
28. 'editable': false, // 是否可编辑
29. 'pixelFormat': 3, // 像素格式
30. 'scaleMode': 1, // 缩略值
31. 'size': { height: 100, width: 100 }
32. };
33. //创建图片大小
34. imageSource.createPixelMap(option).then((pixelMap: PixelMap) => {
35. this.imageAlt = pixelMap;
36. })
37. }
38. })
39. }

41. build() {
42. Column() {
43. Button("获取网络图片")
44. .onClick(() => {
45. this.httpRequest();
46. })

48. Text() {
49. // 直接加载网络地址，请填写一个具体的网络图片地址
50. ImageSpan('https://www.example.com/xxx.png')
51. .alt(this.imageAlt)
52. .width(300)
53. .height(300)
54. }

56. }.width('100%').height(250).padding({ left: 35, right: 35, top: 35 })
57. }
58. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/mW214kLdSs-rBR75zLQO_w/zh-cn_image_0000002552959814.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000148Z&HW-CC-Expire=86400&HW-CC-Sign=06E66C2E9EF51F3BBFFBA1B70D3F2DF93E65CA5460861C80E757A2BFA72A1DC8)

### 示例6（使用supportSvg2属性时，SVG图片的显示效果）

从API version 22开始，该示例通过设置[supportSvg2](ts-basic-components-imagespan.md#supportsvg222)属性，使[SVG标签解析能力增强功能](ts-image-svg2-capabilities.md#svg易用性提升)的SVG易用性提升能力生效。

```
1. import { drawing } from '@kit.ArkGraphics2D';
2. @Entry
3. @Component
4. struct Index {
5. build() {
6. Row() {
7. Column() {
8. Text('属性字符串不支持svg2')
9. // $r("app.media.ice")需要替换为开发者所需的图像资源文件。
10. Text() {
11. ImageSpan($r("app.media.ice"))
12. .width(50)
13. .height(50)
14. .colorFilter(drawing.ColorFilter.createBlendModeColorFilter(
15. drawing.Tool.makeColorFromResourceColor(Color.Blue), drawing.BlendMode.SRC_IN))
16. }
17. Text('属性字符串支持svg2')
18. // $r("app.media.ice")需要替换为开发者所需的图像资源文件。
19. Text() {
20. ImageSpan($r("app.media.ice"))
21. .width(50)
22. .height(50)
23. .supportSvg2(true)
24. .colorFilter(drawing.ColorFilter.createBlendModeColorFilter(
25. drawing.Tool.makeColorFromResourceColor(Color.Blue), drawing.BlendMode.SRC_IN))
26. }
27. }
28. .width('100%')
29. }
30. .height('100%')
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/JkGHIUHYTgSz6tPO7xLsjw/zh-cn_image_0000002583479815.png?HW-CC-KV=V1&HW-CC-Date=20260428T000148Z&HW-CC-Expire=86400&HW-CC-Sign=7378F52B96DB241C6A5D4742C04963FE15CD28AAFC21AF010A6873ACBA8DB707)
