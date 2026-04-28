---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-effectkit
title: @ohos.effectKit (图像效果)
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.effectKit (图像效果)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fa628b945f37e295d6c821fdf376218d2a4b820848d4e55e1ae49cc88748ef00
---

图像效果模块提供了处理图像的基础能力，包括亮度调节、模糊化、灰度调节和智能取色等。effectKit用于离线处理图像（如pixelmap、png、jpeg）以获得视觉效果，而uiEffect则实时接入渲染服务，针对屏幕帧缓存进行处理以获得动态视觉效果。

该模块提供以下图像效果相关的常用功能：

* [Filter](js-apis-effectkit.md#filter)：效果类，用于添加指定效果到图像源。
* [Color](js-apis-effectkit.md#color)：颜色类，用于保存取色的结果。
* [ColorPicker](js-apis-effectkit.md#colorpicker)：智能取色器。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { effectKit } from "@kit.ArkGraphics2D";
```

## effectKit.createEffect

PhonePC/2in1TabletTVWearable

createEffect(source: image.PixelMap): Filter

通过传入的PixelMap创建Filter实例。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | image模块创建的PixelMap实例。可通过图片解码或直接创建获得，具体可见[Image Kit简介](../harmonyos-guides/image-overview.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Filter](js-apis-effectkit.md#filter) | 返回不带任何效果的Filter链表头节点，失败时返回null。 |

**示例：**

```
1. import { image } from "@kit.ImageKit";
2. import { effectKit } from "@kit.ArkGraphics2D";

4. const color = new ArrayBuffer(96);
5. let opts : image.InitializationOptions = {
6. editable: true,
7. pixelFormat: 3,
8. size: {
9. height: 4,
10. width: 6
11. }
12. }
13. image.createPixelMap(color, opts).then((pixelMap) => {
14. let headFilter = effectKit.createEffect(pixelMap);
15. })
```

## effectKit.createColorPicker

PhonePC/2in1TabletTVWearable

createColorPicker(source: image.PixelMap): Promise<ColorPicker>

通过传入的PixelMap创建ColorPicker实例，使用Promise异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | image模块创建的PixelMap实例。可通过图片解码或直接创建获得，具体可见[Image Kit简介](../harmonyos-guides/image-overview.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ColorPicker](js-apis-effectkit.md#colorpicker)> | Promise对象。返回创建的ColorPicker实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Input parameter error. |

**示例：**

```
1. import { image } from "@kit.ImageKit";
2. import { effectKit } from "@kit.ArkGraphics2D";
3. import { BusinessError } from "@kit.BasicServicesKit";

5. const color = new ArrayBuffer(96);
6. let opts : image.InitializationOptions = {
7. editable: true,
8. pixelFormat: 3,
9. size: {
10. height: 4,
11. width: 6
12. }
13. }

15. image.createPixelMap(color, opts).then((pixelMap) => {
16. effectKit.createColorPicker(pixelMap).then(colorPicker => {
17. console.info("Succeeded in creating colorPicker.");
18. }).catch((err : BusinessError) => {
19. console.error(`Failed to create colorPicker. Code: ${err.code}, message: ${err.message}`);
20. })
21. })
```

## effectKit.createColorPicker10+

PhonePC/2in1TabletTVWearable

createColorPicker(source: image.PixelMap, region: Array<number>): Promise<ColorPicker>

通过传入的PixelMap创建选定取色区域的ColorPicker实例，使用Promise异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | image模块创建的PixelMap实例。可通过图片解码或直接创建获得，具体可见[Image Kit简介](../harmonyos-guides/image-overview.md)。 |
| region | Array<number> | 是 | 指定图片的取色区域。  数组元素个数为4，取值范围为[0, 1]，分别表示图片区域的左、上、右、下位置，图片最左侧和最上侧对应位置0，最右侧和最下侧对应位置1。数组第三个元素需大于第一个元素，第四个元素需大于第二个元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ColorPicker](js-apis-effectkit.md#colorpicker)> | Promise对象。返回创建的ColorPicker实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Input parameter error. |

**示例：**

```
1. import { image } from "@kit.ImageKit";
2. import { effectKit } from "@kit.ArkGraphics2D";
3. import { BusinessError } from "@kit.BasicServicesKit";

5. const color = new ArrayBuffer(96);
6. let opts : image.InitializationOptions = {
7. editable: true,
8. pixelFormat: 3,
9. size: {
10. height: 4,
11. width: 6
12. }
13. }

15. image.createPixelMap(color, opts).then((pixelMap) => {
16. effectKit.createColorPicker(pixelMap, [0, 0, 1, 1]).then(colorPicker => {
17. console.info("Succeeded in creating colorPicker.");
18. }).catch((err : BusinessError) => {
19. console.error(`Failed to create colorPicker. Code: ${err.code}, message: ${err.message}`);
20. })
21. })
```

## effectKit.createColorPicker

PhonePC/2in1TabletTVWearable

createColorPicker(source: image.PixelMap, callback: AsyncCallback<ColorPicker>): void

通过传入的PixelMap创建ColorPicker实例，使用callback异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | image模块创建的PixelMap实例。可通过图片解码或直接创建获得，具体可见[Image Kit简介](../harmonyos-guides/image-overview.md)。 |
| callback | AsyncCallback<[ColorPicker](js-apis-effectkit.md#colorpicker)> | 是 | 回调函数。返回创建的ColorPicker实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Input parameter error. |

**示例：**

```
1. import { image } from "@kit.ImageKit";
2. import { effectKit } from "@kit.ArkGraphics2D";

4. const color = new ArrayBuffer(96);
5. let opts : image.InitializationOptions = {
6. editable: true,
7. pixelFormat: 3,
8. size: {
9. height: 4,
10. width: 6
11. }
12. }
13. image.createPixelMap(color, opts).then((pixelMap) => {
14. effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
15. if (error) {
16. console.error('Failed to create color picker.');
17. } else {
18. console.info('Succeeded in creating color picker.');
19. }
20. })
21. })
```

## effectKit.createColorPicker10+

PhonePC/2in1TabletTVWearable

createColorPicker(source: image.PixelMap, region:Array<number>, callback: AsyncCallback<ColorPicker>): void

通过传入的PixelMap创建选定取色区域的ColorPicker实例，使用callback异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | image模块创建的PixelMap实例。可通过图片解码或直接创建获得，具体可见[Image Kit简介](../harmonyos-guides/image-overview.md)。 |
| region | Array<number> | 是 | 指定图片的取色区域。  数组元素个数为4，取值范围为[0, 1]，数组元素分别表示图片区域的左、上、右、下位置，图片最左侧和最上侧对应位置0，最右侧和最下侧对应位置1。数组第三个元素需大于第一个元素，第四个元素需大于第二个元素。 |
| callback | AsyncCallback<[ColorPicker](js-apis-effectkit.md#colorpicker)> | 是 | 回调函数。返回创建的ColorPicker实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Input parameter error. |

**示例：**

```
1. import { image } from "@kit.ImageKit";
2. import { effectKit } from "@kit.ArkGraphics2D";

4. const color = new ArrayBuffer(96);
5. let opts : image.InitializationOptions = {
6. editable: true,
7. pixelFormat: 3,
8. size: {
9. height: 4,
10. width: 6
11. }
12. }
13. image.createPixelMap(color, opts).then((pixelMap) => {
14. effectKit.createColorPicker(pixelMap, [0, 0, 1, 1], (error, colorPicker) => {
15. if (error) {
16. console.error('Failed to create color picker.');
17. } else {
18. console.info('Succeeded in creating color picker.');
19. }
20. })
21. })
```

## Color

PhonePC/2in1TabletTVWearable

颜色类，用于保存取色的结果。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| red | number | 否 | 否 | 红色分量值，取值范围[0x0, 0xFF]。 |
| green | number | 否 | 否 | 绿色分量值，取值范围[0x0, 0xFF]。 |
| blue | number | 否 | 否 | 蓝色分量值，取值范围[0x0, 0xFF]。 |
| alpha | number | 否 | 否 | 透明通道分量值，取值范围[0x0, 0xFF]。 |

## TileMode14+

PhonePC/2in1TabletTVWearable

着色器效果平铺模式的枚举。

**系统能力：** SystemCapability.Multimedia.Image.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CLAMP | 0 | 如果着色器效果超出其原始边界，剩余区域使用着色器的边缘颜色填充。 |
| REPEAT | 1 | 在水平和垂直方向上重复着色器效果。 |
| MIRROR | 2 | 在水平和垂直方向上重复着色器效果，交替镜像图像，以便相邻图像始终接合。 |
| DECAL | 3 | 仅在其原始边界内渲染着色器效果。 |

## ColorPicker

PhonePC/2in1TabletTVWearable

取色类，用于从一张图像数据中获取它的主要颜色。在调用ColorPicker的方法前，需要先通过[createColorPicker](js-apis-effectkit.md#effectkitcreatecolorpicker)创建一个ColorPicker实例。

### getMainColor

PhonePC/2in1TabletTVWearable

getMainColor(): Promise<Color>

读取图像主色的颜色值，结果写入[Color](js-apis-effectkit.md#color)里，使用Promise异步回调。该接口通过图像缩放算法，根据周围像素的加权计算，将原图缩小到1个像素以得到主色。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Color](js-apis-effectkit.md#color)> | Promise对象。返回图像主色对应的颜色值，失败时返回错误信息。 |

**示例：**

```
1. import { image } from "@kit.ImageKit";
2. import { effectKit } from "@kit.ArkGraphics2D";

4. const color = new ArrayBuffer(96);
5. let opts: image.InitializationOptions = {
6. editable: true,
7. pixelFormat: 3,
8. size: {
9. height: 4,
10. width: 6
11. }
12. }
13. image.createPixelMap(color, opts).then((pixelMap) => {
14. effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
15. if (error) {
16. console.error('Failed to create color picker.');
17. } else {
18. console.info('Succeeded in creating color picker.');
19. colorPicker.getMainColor().then(color => {
20. console.info('Succeeded in getting main color.');
21. console.info(`color[ARGB]=${color.alpha},${color.red},${color.green},${color.blue}`);
22. })
23. }
24. })
25. })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/09C70e2NSWOzPaNJDkrnjA/zh-cn_image_0000002552801208.png?HW-CC-KV=V1&HW-CC-Date=20260428T001434Z&HW-CC-Expire=86400&HW-CC-Sign=25899ED6F38954DCA57EADAA6574173882CA18B91B770CF5656B5932E8EECDA5)

### getMainColorSync

PhonePC/2in1TabletTVWearable

getMainColorSync(): Color

读取图像主色的颜色值，结果写入[Color](js-apis-effectkit.md#color)里，使用同步方式返回。该接口通过图像缩放算法，根据周围像素的加权计算，将原图缩小到1个像素以得到主色。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Color](js-apis-effectkit.md#color) | Color实例，即图像主色对应的颜色值，失败时返回null。 |

**示例：**

```
1. import { image } from "@kit.ImageKit";
2. import { effectKit } from "@kit.ArkGraphics2D";

4. const color = new ArrayBuffer(96);
5. let opts : image.InitializationOptions = {
6. editable: true,
7. pixelFormat: 3,
8. size: {
9. height: 4,
10. width: 6
11. }
12. }
13. image.createPixelMap(color, opts).then((pixelMap) => {
14. effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
15. if (error) {
16. console.error('Failed to create color picker.');
17. } else {
18. console.info('Succeeded in creating color picker.');
19. let color = colorPicker.getMainColorSync();
20. console.info('get main color =' + color);
21. }
22. })
23. })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/UqGeZ0gjTIaxxGIiD9nq0Q/zh-cn_image_0000002552801208.png?HW-CC-KV=V1&HW-CC-Date=20260428T001434Z&HW-CC-Expire=86400&HW-CC-Sign=0748E6C97CB7FF73EF1C0E9BFC2A44CF90D312C75BD93E5017C8B63246D48286)

### getLargestProportionColor10+

PhonePC/2in1TabletTVWearable

getLargestProportionColor(): Color

读取图像中占比最多的颜色值，结果写入[Color](js-apis-effectkit.md#color)里，使用同步方式返回。该接口使用中位切分算法划分颜色空间，获取占比最多的颜色空间的平均颜色。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Color](js-apis-effectkit.md#color) | Color实例，即图像占比最多的颜色值，失败时返回null。 |

**示例：**

```
1. import { image } from "@kit.ImageKit";
2. import { effectKit } from "@kit.ArkGraphics2D";

4. const color = new ArrayBuffer(96);
5. let opts : image.InitializationOptions = {
6. editable: true,
7. pixelFormat: 3,
8. size: {
9. height: 4,
10. width: 6
11. }
12. }
13. image.createPixelMap(color, opts).then((pixelMap) => {
14. effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
15. if (error) {
16. console.error('Failed to create color picker.');
17. } else {
18. console.info('Succeeded in creating color picker.');
19. let color = colorPicker.getLargestProportionColor();
20. console.info('get largest proportion color =' + color);
21. }
22. })
23. })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/PQDIkrFWSD2qDkshMUqRJQ/zh-cn_image_0000002583440903.png?HW-CC-KV=V1&HW-CC-Date=20260428T001434Z&HW-CC-Expire=86400&HW-CC-Sign=A998CA7C2FF64D0FECBB0683644B2BDF364882D03848217B229700AD9305F6F8)

### getTopProportionColors12+

PhonePC/2in1TabletTVWearable

getTopProportionColors(colorCount: number): Array<Color | null>

读取图像占比靠前的颜色值，个数由colorCount指定，结果写入[Color](js-apis-effectkit.md#color)的数组里，使用同步方式返回。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorCount | number | 是 | 需要取主色的个数，向下取整。  **说明：** 在HarmonyOS 6.1.0之前，取值范围为[1, 10]，取色个数大于10视为取前10个；从HarmonyOS 6.1.0开始，取值范围为[1, 20]，取色个数大于20视为取前20个。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[Color](js-apis-effectkit.md#color) | null> | Color数组，即图像占比前colorCount的颜色值数组，按占比排序。  - 当实际读取的特征色个数小于colorCount时，数组大小为实际特征色个数。  - 取色失败或取色个数小于1返回[null]。 |

**示例：**

```
1. import { image } from "@kit.ImageKit";
2. import { effectKit } from "@kit.ArkGraphics2D";

4. const color = new ArrayBuffer(96);
5. let opts : image.InitializationOptions = {
6. editable: true,
7. pixelFormat: 3,
8. size: {
9. height: 4,
10. width: 6
11. }
12. }
13. image.createPixelMap(color, opts).then((pixelMap) => {
14. effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
15. if (error) {
16. console.error('Failed to create color picker.');
17. } else {
18. console.info('Succeeded in creating color picker.');
19. let colors = colorPicker.getTopProportionColors(2);
20. for(let index = 0; index < colors.length; index++) {
21. if (colors[index]) {
22. console.info('get top proportion colors: index ' + index + ', color ' + colors[index]);
23. }
24. }
25. }
26. })
27. })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/H9CGBnSeSO688qoCvCmPpA/zh-cn_image_0000002552960858.png?HW-CC-KV=V1&HW-CC-Date=20260428T001434Z&HW-CC-Expire=86400&HW-CC-Sign=A78FAEA5F609F32CEB66EA2C90C8A8FA78568B361897FBA197D6F33BECB46DF8)

### getHighestSaturationColor10+

PhonePC/2in1TabletTVWearable

getHighestSaturationColor(): Color

读取图像饱和度最高的颜色值，结果写入[Color](js-apis-effectkit.md#color)里，使用同步方式返回。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Color](js-apis-effectkit.md#color) | Color实例，即图像饱和度最高的颜色值，失败时返回null。 |

**示例：**

```
1. import { image } from "@kit.ImageKit";
2. import { effectKit } from "@kit.ArkGraphics2D";

4. const color = new ArrayBuffer(96);
5. let opts: image.InitializationOptions = {
6. editable: true,
7. pixelFormat: 3,
8. size: {
9. height: 4,
10. width: 6
11. }
12. }
13. image.createPixelMap(color, opts).then((pixelMap) => {
14. effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
15. if (error) {
16. console.error('Failed to create color picker.');
17. } else {
18. console.info('Succeeded in creating color picker.');
19. let color = colorPicker.getHighestSaturationColor();
20. console.info('get highest saturation color =' + color);
21. }
22. })
23. })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/NrhRkfTEQVOhtnrUWZMg5Q/zh-cn_image_0000002583480859.png?HW-CC-KV=V1&HW-CC-Date=20260428T001434Z&HW-CC-Expire=86400&HW-CC-Sign=D3758C7630474AE28E2CAA530057F72F20FCB6CCBAE9270FC97C38D73566178E)

### getAverageColor10+

PhonePC/2in1TabletTVWearable

getAverageColor(): Color

读取图像平均的颜色值，结果写入[Color](js-apis-effectkit.md#color)里，使用同步方式返回。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Color](js-apis-effectkit.md#color) | Color实例，即图像平均的颜色值，失败时返回null。 |

**示例：**

```
1. import { image } from "@kit.ImageKit";
2. import { effectKit } from "@kit.ArkGraphics2D";

4. const color = new ArrayBuffer(96);
5. let opts: image.InitializationOptions = {
6. editable: true,
7. pixelFormat: 3,
8. size: {
9. height: 4,
10. width: 6
11. }
12. }
13. image.createPixelMap(color, opts).then((pixelMap) => {
14. effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
15. if (error) {
16. console.error('Failed to create color picker.');
17. } else {
18. console.info('Succeeded in creating color picker.');
19. let color = colorPicker.getAverageColor();
20. console.info('get average color =' + color);
21. }
22. })
23. })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/Z3ZwR-s8Ss-cM_FGO7XIfA/zh-cn_image_0000002552801210.png?HW-CC-KV=V1&HW-CC-Date=20260428T001434Z&HW-CC-Expire=86400&HW-CC-Sign=F40C99C532A57B4A31E93F9CBF565AC1E9453E5D98B8E1609224CA10B41A67EB)

### isBlackOrWhiteOrGrayColor10+

PhonePC/2in1TabletTVWearable

isBlackOrWhiteOrGrayColor(color: number): boolean

判断图像是否为黑白灰颜色，返回true或false。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | number | 是 | 需要判断是否黑白灰色的颜色值，取值范围[0x0, 0xFFFFFFFF]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果图像为黑白灰颜色，则返回true；否则返回false。 |

**示例：**

```
1. import { image } from "@kit.ImageKit";
2. import { effectKit } from "@kit.ArkGraphics2D";

4. const color = new ArrayBuffer(96);
5. let opts: image.InitializationOptions = {
6. editable: true,
7. pixelFormat: 3,
8. size: {
9. height: 4,
10. width: 6
11. }
12. }
13. image.createPixelMap(color, opts).then((pixelMap) => {
14. effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
15. if (error) {
16. console.error('Failed to create color picker.');
17. } else {
18. console.info('Succeeded in creating color picker.');
19. let bJudge = colorPicker.isBlackOrWhiteOrGrayColor(0xFFFFFFFF);
20. console.info('is black or white or gray color[bool](white) =' + bJudge);
21. }
22. })
23. })
```

## Filter

PhonePC/2in1TabletTVWearable

图像效果类，用于将指定的效果添加到输入图像中。在调用Filter的方法前，需要先通过[createEffect](js-apis-effectkit.md#effectkitcreateeffect)创建一个Filter实例。

### blur

PhonePC/2in1TabletTVWearable

blur(radius: number): Filter

将模糊效果添加到效果链表中，返回链表的头节点。

说明

该接口为静态模糊接口，为静态图像提供模糊化效果，如果要对组件进行实时渲染的模糊，可以使用[动态模糊](../harmonyos-guides/arkts-blur-effect.md)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radius | number | 是 | 模糊半径，单位是像素。模糊效果与所设置的值成正比，值越大效果越明显。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Filter](js-apis-effectkit.md#filter) | 返回已添加的图像效果。 |

**示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { effectKit } from '@kit.ArkGraphics2D';
3. import { common } from '@kit.AbilityKit';
4. // 传入读取的图片数据
5. function ImageBlur(Image: ArrayBuffer): Promise<image.PixelMap> {
6. return new Promise(async (resolve, reject) => {
7. let imageSource = image.createImageSource(Image);
8. await imageSource.createPixelMap().then(async (pixelMap: image.PixelMap) => {
9. let radius = 5;
10. let headFilter = effectKit.createEffect(pixelMap);
11. if (headFilter != null) {
12. // 对图片添加效果标识
13. headFilter.blur(radius);
14. }
15. // 按照添加的效果标识对图片进行处理并且返回处理好的图片数据
16. headFilter.getEffectPixelMap().then(imageData => {
17. resolve(imageData);
18. })
19. })
20. })
21. }

23. @Entry
24. @Component
25. struct Index {
26. @State imagePixelMap: image.PixelMap | null = null;
27. private imageBuffer: ArrayBuffer | undefined = undefined;
28. // 读取rawfile文件夹下的图片文件，也可根据需求更换读取方式，保证最终得到的是ArrayBuffer格式的图片数据即可
29. async getFileBuffer(): Promise<ArrayBuffer | undefined> {
30. try{
31. const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
32. const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
33. const buffer: ArrayBuffer = fileData.buffer.slice(0);
34. return buffer;
35. }catch (err){
36. return undefined
37. }
38. }

40. async aboutToAppear(): Promise<void>{
41. this.imageBuffer = await this.getFileBuffer();
42. if(this.imageBuffer == undefined){
43. return;
44. }
45. // 图片处理为异步操作，可以依据是否需要拿到处理好的图片数据再进行下一步逻辑，按需添加await进行同步
46. this.imagePixelMap = await ImageBlur(this.imageBuffer);
47. }

49. build() {
50. Column() {
51. Image(this.imagePixelMap)
52. .width(304)
53. .height(305)
54. }
55. .height('100%')
56. .width('100%')
57. }
58. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/7tdJjSjsTx-4c52_Jz7M8g/zh-cn_image_0000002583440905.png?HW-CC-KV=V1&HW-CC-Date=20260428T001434Z&HW-CC-Expire=86400&HW-CC-Sign=B926193CA793168F7268D0C5150E74AFED72E35A37D6B692570B4CE08A40551C)

### blur14+

PhonePC/2in1TabletTVWearable

blur(radius: number, tileMode: TileMode): Filter

将模糊效果添加到效果链表中，返回链表的头节点。

说明

该接口为静态模糊接口，为静态图像提供模糊化效果，如果要对组件进行实时渲染的模糊，可以使用[动态模糊](../harmonyos-guides/arkts-blur-effect.md)。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radius | number | 是 | 模糊半径，单位是像素。模糊效果与所设置的值成正比，值越大效果越明显。 |
| tileMode | [TileMode](js-apis-effectkit.md#tilemode14) | 是 | 着色器效果平铺模式。影响图像边缘的模糊效果。目前仅支持CPU渲染，所以目前着色器平铺模式仅支持DECAL。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Filter](js-apis-effectkit.md#filter) | 返回已添加的图像效果。 |

**示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { effectKit } from '@kit.ArkGraphics2D';
3. import { common } from '@kit.AbilityKit';
4. // 传入读取的图片数据
5. function ImageBlur(Image: ArrayBuffer): Promise<image.PixelMap> {
6. return new Promise(async (resolve, reject) => {
7. let imageSource = image.createImageSource(Image);
8. await imageSource.createPixelMap().then(async (pixelMap: image.PixelMap) => {
9. let radius = 30;
10. let headFilter = effectKit.createEffect(pixelMap);
11. if (headFilter != null) {
12. // 对图片添加效果标识
13. headFilter.blur(radius, effectKit.TileMode.DECAL);
14. }
15. // 按照添加的效果标识对图片进行处理并且返回处理好的图片数据
16. headFilter.getEffectPixelMap().then(imageData => {
17. resolve(imageData);
18. })
19. })
20. })
21. }

23. @Entry
24. @Component
25. struct Index {
26. @State imagePixelMap: image.PixelMap | null = null;
27. private imageBuffer: ArrayBuffer | undefined = undefined;
28. // 读取rawfile文件夹下的图片文件，也可根据需求更换读取方式，保证最终得到的是ArrayBuffer格式的图片数据即可
29. async getFileBuffer(): Promise<ArrayBuffer | undefined> {
30. try{
31. const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
32. const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
33. const buffer: ArrayBuffer = fileData.buffer.slice(0);
34. return buffer;
35. }catch (err){
36. return undefined
37. }
38. }

40. async aboutToAppear(): Promise<void>{
41. this.imageBuffer = await this.getFileBuffer();
42. if(this.imageBuffer == undefined){
43. return;
44. }
45. // 图片处理为异步操作，可以依据是否需要拿到处理好的图片数据再进行下一步逻辑，按需添加await进行同步
46. this.imagePixelMap = await ImageBlur(this.imageBuffer);
47. }

49. build() {
50. Column() {
51. Image(this.imagePixelMap)
52. .width(304)
53. .height(305)
54. }
55. .height('100%')
56. .width('100%')
57. }
58. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/0wj7MO7hSdq9npCcR_aCkw/zh-cn_image_0000002552960860.png?HW-CC-KV=V1&HW-CC-Date=20260428T001434Z&HW-CC-Expire=86400&HW-CC-Sign=1AE82AE757E4309CA0ED298DEBEE8DBD4D8E5B1CFDD94D018170AE6C8C8A86C3)

### invert12+

PhonePC/2in1TabletTVWearable

invert(): Filter

将反转效果添加到效果链表中，返回链表的头节点。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Filter](js-apis-effectkit.md#filter) | 返回已添加的图像效果。 |

**示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { effectKit } from '@kit.ArkGraphics2D';
3. import { common } from '@kit.AbilityKit';
4. // 传入读取的图片数据
5. function ImageInvert(Image: ArrayBuffer): Promise<image.PixelMap> {
6. return new Promise(async (resolve, reject) => {
7. let imageSource = image.createImageSource(Image);
8. await imageSource.createPixelMap().then(async (pixelMap: image.PixelMap) => {
9. let headFilter = effectKit.createEffect(pixelMap);
10. if (headFilter != null) {
11. // 对图片添加效果标识
12. headFilter.invert();
13. }
14. // 按照添加的效果标识对图片进行处理并且返回处理好的图片数据
15. headFilter.getEffectPixelMap().then(imageData => {
16. resolve(imageData);
17. })
18. })
19. })
20. }

22. @Entry
23. @Component
24. struct Index {
25. @State imagePixelMap: image.PixelMap | null = null;
26. private imageBuffer: ArrayBuffer | undefined = undefined;
27. // 读取rawfile文件夹下的图片文件，也可根据需求更换读取方式，保证最终得到的是ArrayBuffer格式的图片数据即可
28. async getFileBuffer(): Promise<ArrayBuffer | undefined> {
29. try{
30. const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
31. const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
32. const buffer: ArrayBuffer = fileData.buffer.slice(0);
33. return buffer;
34. }catch (err){
35. return undefined
36. }
37. }

39. async aboutToAppear(): Promise<void>{
40. this.imageBuffer = await this.getFileBuffer();
41. if(this.imageBuffer == undefined){
42. return;
43. }
44. // 图片处理为异步操作，可以依据是否需要拿到处理好的图片数据再进行下一步逻辑，按需添加await进行同步
45. this.imagePixelMap = await ImageInvert(this.imageBuffer);
46. }

48. build() {
49. Column() {
50. Image(this.imagePixelMap)
51. .width(304)
52. .height(305)
53. }
54. .height('100%')
55. .width('100%')
56. }
57. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/zIwb8-vyRwag3dwlNzW9XQ/zh-cn_image_0000002583480861.png?HW-CC-KV=V1&HW-CC-Date=20260428T001434Z&HW-CC-Expire=86400&HW-CC-Sign=2CD61801F467B2CD8B9E02A297AED01CFC34A13879C683DB5F522F002F2E7D8E)

### setColorMatrix12+

PhonePC/2in1TabletTVWearable

setColorMatrix(colorMatrix: Array<number>): Filter

将自定义效果添加到效果链表中，返回链表的头节点。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorMatrix | Array<number> | 是 | 自定义颜色矩阵。  用于创建效果滤镜的 5x4 大小的矩阵，矩阵元素取值范围为[0, 1]，0和1代表的是矩阵中对应位置的颜色通道的权重，0代表该颜色通道不参与计算，1代表该颜色通道参与计算并保持原始权重。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Filter](js-apis-effectkit.md#filter) | 返回已添加的图像效果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Input parameter error. |

**示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { effectKit } from '@kit.ArkGraphics2D';
3. import { common } from '@kit.AbilityKit';
4. // 传入读取的图片数据
5. function ImageColorFilter(Image: ArrayBuffer): Promise<image.PixelMap> {
6. return new Promise(async (resolve, reject) => {
7. let imageSource = image.createImageSource(Image);
8. await imageSource.createPixelMap().then(async (pixelMap: image.PixelMap) => {
9. let colorMatrix:Array<number> = [
10. 0.2126,0.7152,0.0722,0,0,
11. 0.2126,0.7152,0.0722,0,0,
12. 0.2126,0.7152,0.0722,0,0,
13. 0,0,0,1,0
14. ];
15. let headFilter = effectKit.createEffect(pixelMap);
16. if (headFilter != null) {
17. // 对图片添加效果标识
18. headFilter.setColorMatrix(colorMatrix);
19. }
20. // 按照添加的效果标识对图片进行处理并且返回处理好的图片数据
21. headFilter.getEffectPixelMap().then(imageData => {
22. resolve(imageData);
23. })
24. })
25. })
26. }

28. @Entry
29. @Component
30. struct Index {
31. @State imagePixelMap: image.PixelMap | null = null;
32. private imageBuffer: ArrayBuffer | undefined = undefined;
33. // 读取rawfile文件夹下的图片文件，也可根据需求更换读取方式，保证最终得到的是ArrayBuffer格式的图片数据即可
34. async getFileBuffer(): Promise<ArrayBuffer | undefined> {
35. try{
36. const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
37. const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
38. const buffer: ArrayBuffer = fileData.buffer.slice(0);
39. return buffer;
40. }catch (err){
41. return undefined
42. }
43. }

45. async aboutToAppear(): Promise<void>{
46. this.imageBuffer = await this.getFileBuffer();
47. if(this.imageBuffer == undefined){
48. return;
49. }
50. // 图片处理为异步操作，可以依据是否需要拿到处理好的图片数据再进行下一步逻辑，按需添加await进行同步
51. this.imagePixelMap = await ImageColorFilter(this.imageBuffer);
52. }

54. build() {
55. Column() {
56. Image(this.imagePixelMap)
57. .width(304)
58. .height(305)
59. }
60. .height('100%')
61. .width('100%')
62. }
63. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/ThPnH1oKSAuspsTJKvAtxw/zh-cn_image_0000002552801212.png?HW-CC-KV=V1&HW-CC-Date=20260428T001434Z&HW-CC-Expire=86400&HW-CC-Sign=23C2864649C3FC0DD2B30DC285BACAEBABD1DFE7067012041C34F6E2EB3586EE)

### brightness

PhonePC/2in1TabletTVWearable

brightness(bright: number): Filter

将高亮效果添加到效果链表中，返回链表的头节点。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bright | number | 是 | 高亮程度，取值范围为[0, 1]，取值为0时图像保持不变，取值为1时图像达到预设的最大亮度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Filter](js-apis-effectkit.md#filter) | 返回已添加的图像效果。 |

**示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { effectKit } from '@kit.ArkGraphics2D';
3. import { common } from '@kit.AbilityKit';
4. // 传入读取的图片数据
5. function ImageBrightness(Image: ArrayBuffer): Promise<image.PixelMap> {
6. return new Promise(async (resolve, reject) => {
7. let imageSource = image.createImageSource(Image);
8. await imageSource.createPixelMap().then(async (pixelMap: image.PixelMap) => {
9. let bright = 0.5;
10. let headFilter = effectKit.createEffect(pixelMap);
11. if (headFilter != null) {
12. // 对图片添加效果标识
13. headFilter.brightness(bright);
14. }
15. // 按照添加的效果标识对图片进行处理并且返回处理好的图片数据
16. headFilter.getEffectPixelMap().then(imageData => {
17. resolve(imageData);
18. })
19. })
20. })
21. }

23. @Entry
24. @Component
25. struct Index {
26. @State imagePixelMap: image.PixelMap | null = null;
27. private imageBuffer: ArrayBuffer | undefined = undefined;
28. // 读取rawfile文件夹下的图片文件，也可根据需求更换读取方式，保证最终得到的是ArrayBuffer格式的图片数据即可
29. async getFileBuffer(): Promise<ArrayBuffer | undefined> {
30. try{
31. const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
32. const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
33. const buffer: ArrayBuffer = fileData.buffer.slice(0);
34. return buffer;
35. }catch (err){
36. return undefined
37. }
38. }

40. async aboutToAppear(): Promise<void>{
41. this.imageBuffer = await this.getFileBuffer();
42. if(this.imageBuffer == undefined){
43. return;
44. }
45. // 图片处理为异步操作，可以依据是否需要拿到处理好的图片数据再进行下一步逻辑，按需添加await进行同步
46. this.imagePixelMap = await ImageBrightness(this.imageBuffer);
47. }

49. build() {
50. Column() {
51. Image(this.imagePixelMap)
52. .width(304)
53. .height(305)
54. }
55. .height('100%')
56. .width('100%')
57. }
58. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/y02c1BwjSi2zzRq6ufrXdg/zh-cn_image_0000002583440907.png?HW-CC-KV=V1&HW-CC-Date=20260428T001434Z&HW-CC-Expire=86400&HW-CC-Sign=C6E071E9712907ECB4774BB7E45553E1EE4EE3778CCACBE9687C902E4C30313C)

### grayscale

PhonePC/2in1TabletTVWearable

grayscale(): Filter

将灰度效果添加到效果链表中，返回链表的头节点。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Filter](js-apis-effectkit.md#filter) | 返回已添加的图像效果。 |

**示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { effectKit } from '@kit.ArkGraphics2D';
3. import { common } from '@kit.AbilityKit';
4. // 传入读取的图片数据
5. function ImageGrayscale(Image: ArrayBuffer): Promise<image.PixelMap> {
6. return new Promise(async (resolve, reject) => {
7. let imageSource = image.createImageSource(Image);
8. await imageSource.createPixelMap().then(async (pixelMap: image.PixelMap) => {
9. let headFilter = effectKit.createEffect(pixelMap);
10. if (headFilter != null) {
11. // 对图片添加效果标识
12. headFilter.grayscale();
13. }
14. // 按照添加的效果标识对图片进行处理并且返回处理好的图片数据
15. headFilter.getEffectPixelMap().then(imageData => {
16. resolve(imageData);
17. })
18. })
19. })
20. }

22. @Entry
23. @Component
24. struct Index {
25. @State imagePixelMap: image.PixelMap | null = null;
26. private imageBuffer: ArrayBuffer | undefined = undefined;
27. // 读取rawfile文件夹下的图片文件，也可根据需求更换读取方式，保证最终得到的是ArrayBuffer格式的图片数据即可
28. async getFileBuffer(): Promise<ArrayBuffer | undefined> {
29. try{
30. const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
31. const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
32. const buffer: ArrayBuffer = fileData.buffer.slice(0);
33. return buffer;
34. }catch (err){
35. return undefined
36. }
37. }

39. async aboutToAppear(): Promise<void>{
40. this.imageBuffer = await this.getFileBuffer();
41. if(this.imageBuffer == undefined){
42. return;
43. }
44. // 图片处理为异步操作，可以依据是否需要拿到处理好的图片数据再进行下一步逻辑，按需添加await进行同步
45. this.imagePixelMap = await ImageGrayscale(this.imageBuffer);
46. }

48. build() {
49. Column() {
50. Image(this.imagePixelMap)
51. .width(304)
52. .height(305)
53. }
54. .height('100%')
55. .width('100%')
56. }
57. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/Z9iE1ZbeTPed7Z0xk7uLjw/zh-cn_image_0000002552960862.png?HW-CC-KV=V1&HW-CC-Date=20260428T001434Z&HW-CC-Expire=86400&HW-CC-Sign=20514B441BF5112CFC62EF4E5FEA73DC8CDA0CA7778C40F71A997321D5736F3F)

### getEffectPixelMap11+

PhonePC/2in1TabletTVWearable

getEffectPixelMap(): Promise<image.PixelMap>

获取已添加链表效果的源图像的image.PixelMap，使用CPU渲染，使用Promise异步回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[image.PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象。返回已添加链表效果的源图像的image.PixelMap。 |

**示例：**

```
1. import { image } from "@kit.ImageKit";
2. import { effectKit } from "@kit.ArkGraphics2D";

4. const color = new ArrayBuffer(96);
5. let opts : image.InitializationOptions = {
6. editable: true,
7. pixelFormat: 3,
8. size: {
9. height: 4,
10. width: 6
11. }
12. };
13. image.createPixelMap(color, opts).then((pixelMap) => {
14. effectKit.createEffect(pixelMap).grayscale().getEffectPixelMap().then(data => {
15. console.info('getPixelBytesNumber = ', data.getPixelBytesNumber());
16. })
17. })
```

### getEffectPixelMap20+

PhonePC/2in1TabletTVWearable

getEffectPixelMap(useCpuRender : boolean): Promise<image.PixelMap>

获取已添加链表效果的源图像的image.PixelMap，支持指定渲染模式（CPU渲染或者GPU渲染），使用Promise异步回调。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| useCpuRender | boolean | 是 | 指定渲染模式。true表示使用CPU渲染，false表示使用GPU渲染。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[image.PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象。返回已添加链表效果的源图像的image.PixelMap。 |

**示例：**

```
1. import { image } from "@kit.ImageKit";
2. import { effectKit } from "@kit.ArkGraphics2D";

4. const color = new ArrayBuffer(96);
5. let opts : image.InitializationOptions = {
6. editable: true,
7. pixelFormat: 3,
8. size: {
9. height: 4,
10. width: 6
11. }
12. };
13. image.createPixelMap(color, opts).then((pixelMap) => {
14. effectKit.createEffect(pixelMap).grayscale().getEffectPixelMap(false).then(data => {
15. console.info('getPixelBytesNumber = ', data.getPixelBytesNumber());
16. })
17. })
```

### getPixelMap(deprecated)

PhonePC/2in1TabletTVWearable

getPixelMap(): image.PixelMap

获取已添加链表效果的源图像的image.PixelMap。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[getEffectPixelMap](js-apis-effectkit.md#geteffectpixelmap11)替代。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [image.PixelMap](arkts-apis-image-pixelmap.md) | 已添加效果的源图像的image.PixelMap。 |

**示例：**

```
1. import { image } from "@kit.ImageKit";
2. import { effectKit } from "@kit.ArkGraphics2D";

4. const color = new ArrayBuffer(96);
5. let opts : image.InitializationOptions = {
6. editable: true,
7. pixelFormat: 3,
8. size: {
9. height: 4,
10. width: 6
11. }
12. };
13. image.createPixelMap(color, opts).then((pixelMap) => {
14. let pixel = effectKit.createEffect(pixelMap).grayscale().getPixelMap();
15. console.info('getPixelBytesNumber = ', pixel.getPixelBytesNumber());
16. })
```
