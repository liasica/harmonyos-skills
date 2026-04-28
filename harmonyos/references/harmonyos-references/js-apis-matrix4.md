---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-matrix4
title: @ohos.matrix4 (矩阵变换)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.matrix4 (矩阵变换)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3babf5232dec8292d147254fd0edf2ffa123b8ac1e47f49748836e30adbfeb82
---

用于对组件进行[图形变换](ts-universal-attributes-transformation.md)的各种操作，为组件提供矩阵变换能力，支持对图形进行平移、旋转和缩放等。

Matrix4的使用场景包括：

[图形变换](ts-universal-attributes-transformation.md)中的[transform](ts-universal-attributes-transformation.md#transform18)接口通过使用图形变换矩阵Matrix4对象显示二维变换时的矩阵变换，[transform3D](ts-universal-attributes-transformation.md#transform3d20)接口通过使用图形变换矩阵Matrix4对象设置组件的三维变换矩阵。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { matrix4 } from '@kit.ArkUI';
```

## matrix4.init

PhonePC/2in1TabletTVWearable

init(options: [number,number,number,number,number,number,number,number,number,number,number,number,number,number,number,number]): Matrix4Transit

Matrix的构造函数，可以通过传入的参数创建一个四阶矩阵，矩阵为列优先。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [number,number,number,number,  number,number,number,number,  number,number,number,number,  number,number,number,number] | 是 | 参数为长度为16（4\*4）的number数组, 详情见四阶矩阵说明。  各number取值范围：(-∞, +∞)  默认值：  [1, 0, 0, 0,  0, 1, 0, 0,  0, 0, 1, 0,  0, 0, 0, 1] |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Matrix4Transit](js-apis-matrix4.md#matrix4transit) | 根据入参创建的四阶矩阵对象。 |

**四阶矩阵说明：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| m00 | number | 是 | x轴缩放值，单位矩阵默认为1。 |
| m01 | number | 是 | 第2个值，xyz轴旋转或倾斜会影响这个值。 |
| m02 | number | 是 | 第3个值，xyz轴旋转会影响这个值。 |
| m03 | number | 是 | 第4个值，透视投影会影响这个值。 |
| m10 | number | 是 | 第5个值，xyz轴旋转或倾斜会影响这个值。 |
| m11 | number | 是 | y轴缩放值，单位矩阵默认为1。 |
| m12 | number | 是 | 第7个值，xyz轴旋转会影响这个值。 |
| m13 | number | 是 | 第8个值，透视投影会影响这个值。 |
| m20 | number | 是 | 第9个值，xyz轴旋转会影响这个值。 |
| m21 | number | 是 | 第10个值，xyz轴旋转会影响这个值。 |
| m22 | number | 是 | z轴缩放值，单位矩阵默认为1。 |
| m23 | number | 是 | 第12个值，透视投影会影响这个值。 |
| m30 | number | 是 | x轴平移值，单位px，单位矩阵默认为0。 |
| m31 | number | 是 | y轴平移值，单位px，单位矩阵默认为0。 |
| m32 | number | 是 | z轴平移值，单位px，单位矩阵默认为0。 |
| m33 | number | 是 | 齐次坐标下生效，产生透视投影效果。 |

**示例**

```
1. import { matrix4 } from '@kit.ArkUI';

3. // 创建一个四阶矩阵
4. let matrix = matrix4.init(
5. [1.0, 0.0, 0.0, 0.0,
6. 0.0, 1.0, 0.0, 0.0,
7. 0.0, 0.0, 1.0, 0.0,
8. 0.0, 0.0, 0.0, 1.0]);

10. @Entry
11. @Component
12. struct Tests {
13. build() {
14. Column() {
15. // $r("app.media.zh")需要替换为开发者所需的图像资源文件。
16. Image($r("app.media.zh"))
17. .width("40%")
18. .height(100)
19. .transform(matrix)
20. }
21. }
22. }
```

## matrix4.identity

PhonePC/2in1TabletTVWearable

identity(): Matrix4Transit

Matrix的初始化函数，可以返回一个单位矩阵对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Matrix4Transit](js-apis-matrix4.md#matrix4transit) | 单位矩阵对象。 |

**示例：**

```
1. // matrix1 和 matrix2 效果一致
2. import { matrix4 } from '@kit.ArkUI';

4. let matrix1 = matrix4.init(
5. [1.0, 0.0, 0.0, 0.0,
6. 0.0, 1.0, 0.0, 0.0,
7. 0.0, 0.0, 1.0, 0.0,
8. 0.0, 0.0, 0.0, 1.0]);
9. let matrix2 = matrix4.identity();

11. @Entry
12. @Component
13. struct Tests {
14. build() {
15. Column() {
16. // $r("app.media.zh")需要替换为开发者所需的图像资源文件。
17. Image($r("app.media.zh"))
18. .width("40%")
19. .height(100)
20. .transform(matrix1)
21. // $r("app.media.zh")需要替换为开发者所需的图像资源文件。
22. Image($r("app.media.zh"))
23. .width("40%")
24. .height(100)
25. .margin({ top: 150 })
26. .transform(matrix2)
27. }
28. }
29. }
```

## Matrix4Transit

PhonePC/2in1TabletTVWearable

矩阵对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### copy

PhonePC/2in1TabletTVWearable

copy(): Matrix4Transit

Matrix的拷贝函数，可以拷贝一份当前的矩阵对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Matrix4Transit](js-apis-matrix4.md#matrix4transit) | 当前矩阵的拷贝对象。 |

**示例：**

```
1. // xxx.ets
2. import { matrix4 } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Test {
7. private matrix1 = matrix4.identity().scale({ x: 1.5 });
8. private matrix2 = this.matrix1.copy().translate({ x: 200 });
9. imageSize: Length = '300px';

11. build() {
12. Column({ space: "50px" }) {
13. // $r("app.media.testImage")需要替换为开发者所需的图像资源文件。
14. Image($r("app.media.testImage"))
15. .width(this.imageSize)
16. .height(this.imageSize)
17. // $r("app.media.testImage")需要替换为开发者所需的图像资源文件。
18. Image($r("app.media.testImage"))
19. .width(this.imageSize)
20. .height(this.imageSize)
21. .transform(this.matrix1)
22. // $r("app.media.testImage")需要替换为开发者所需的图像资源文件。
23. Image($r("app.media.testImage"))
24. .width(this.imageSize)
25. .height(this.imageSize)
26. .transform(this.matrix2)
27. }.alignItems(HorizontalAlign.Center)
28. .height('100%').width("100%")
29. .justifyContent(FlexAlign.Center)
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/GtygjPT5Ro-5CvOl2qqQPw/zh-cn_image_0000002552959418.png?HW-CC-KV=V1&HW-CC-Date=20260428T000030Z&HW-CC-Expire=86400&HW-CC-Sign=41D8896AC0619CC6570190163454D95EDD02FF71806981702661394663332370)

### combine

PhonePC/2in1TabletTVWearable

combine(options: Matrix4Transit): Matrix4Transit

Matrix的叠加函数，可以将两个矩阵的效果叠加起来生成一个新的矩阵对象。会改变调用该函数的原始矩阵。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Matrix4Transit](js-apis-matrix4.md#matrix4transit) | 是 | 待叠加的矩阵对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Matrix4Transit](js-apis-matrix4.md#matrix4transit) | 矩阵叠加后的对象。 |

**示例：**

```
1. // xxx.ets
2. import { matrix4 } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Test {
7. private matrix1 = matrix4.identity().translate({ x: 200 });
8. private matrix2 = matrix4.identity().scale({ x: 2 });

10. build() {
11. Column() {
12. // 矩阵变换前
13. // $r("app.media.icon")需要替换为开发者所需的图像资源文件。
14. Image($r("app.media.icon"))
15. .width("40%")
16. .height(100)
17. .margin({ top: 50 })
18. // 先平移x轴200px，再缩放两倍x轴，得到矩阵变换后的效果图
19. // $r("app.media.icon")需要替换为开发者所需的图像资源文件。
20. Image($r("app.media.icon"))
21. .transform(this.matrix1.copy().combine(this.matrix2))
22. .width("40%")
23. .height(100)
24. .margin({ top: 50 })
25. }
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/e5eXlp95QwGZMPwKXS4PxA/zh-cn_image_0000002583479419.png?HW-CC-KV=V1&HW-CC-Date=20260428T000030Z&HW-CC-Expire=86400&HW-CC-Sign=47EA5147B36D8BD362533DA316846D2192E0E8387ED5A53DB21AC8165E262E19)

### invert

PhonePC/2in1TabletTVWearable

invert(): Matrix4Transit

Matrix的逆函数，可以返回一个当前矩阵对象的逆矩阵，即效果正好相反。会改变调用该函数的原始矩阵。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Matrix4Transit](js-apis-matrix4.md#matrix4transit) | 当前矩阵的逆矩阵对象。 |

**示例：**

```
1. import { matrix4 } from '@kit.ArkUI';

3. // matrix1(宽放大2倍) 和 matrix2(宽缩小2倍) 效果相反
4. let matrix1 = matrix4.identity().scale({ x: 2 });
5. let matrix2 = matrix1.copy().invert();

7. @Entry
8. @Component
9. struct Tests {
10. build() {
11. Column() {
12. // $r("app.media.zh")需要替换为开发者所需的图像资源文件。
13. Image($r("app.media.zh"))
14. .width(200)
15. .height(100)
16. .transform(matrix1)
17. .margin({ top: 100 })
18. // $r("app.media.zh")需要替换为开发者所需的图像资源文件。
19. Image($r("app.media.zh"))
20. .width(200)
21. .height(100)
22. .margin({ top: 150 })
23. .transform(matrix2)
24. }
25. }
26. }
```

### translate

PhonePC/2in1TabletTVWearable

translate(options: TranslateOption): Matrix4Transit

Matrix的平移函数，可以为当前矩阵增加x轴/y轴/z轴平移效果。会改变调用该函数的原始矩阵。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TranslateOption](js-apis-matrix4.md#translateoption) | 是 | 设置平移参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Matrix4Transit](js-apis-matrix4.md#matrix4transit) | 平移效果后的矩阵对象。 |

**示例：**

```
1. // xxx.ets
2. import { matrix4 } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Test {
7. private matrix1 = matrix4.identity().translate({ x: 100, y: 200, z: 30 });

9. build() {
10. Column() {
11. // $r("app.media.bg1")需要替换为开发者所需的图像资源文件。
12. Image($r("app.media.bg1")).transform(this.matrix1)
13. .width("40%")
14. .height(100)
15. }
16. }
17. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/qejRztZxSLyRPc_JIM-hAw/zh-cn_image_0000002552799770.png?HW-CC-KV=V1&HW-CC-Date=20260428T000030Z&HW-CC-Expire=86400&HW-CC-Sign=55BD8D5F9A4894D7E4CE6520C6EC826E515F0F1F3D105837D3B88935412B8382)

### scale

PhonePC/2in1TabletTVWearable

scale(options: ScaleOption): Matrix4Transit

Matrix的缩放函数，可以为当前矩阵增加x轴/y轴/z轴缩放效果。会改变调用该函数的原始矩阵。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ScaleOption](js-apis-matrix4.md#scaleoption) | 是 | 设置缩放参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Matrix4Transit](js-apis-matrix4.md#matrix4transit) | 缩放效果后的矩阵对象。 |

**示例：**

```
1. // xxx.ets
2. import { matrix4 } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Test {
7. private matrix1 = matrix4.identity()
8. .scale({
9. x: 2,
10. y: 3,
11. z: 4,
12. centerX: 50,
13. centerY: 50
14. });

16. build() {
17. Column() {
18. // $r("app.media.testImage")需要替换为开发者所需的图像资源文件。
19. Image($r("app.media.testImage")).transform(this.matrix1)
20. .width("300px")
21. .height("300px")
22. }.width("100%").height("100%").justifyContent(FlexAlign.Center)
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/b8OFg_vYRXyCEOgZIcLSIQ/zh-cn_image_0000002583439465.png?HW-CC-KV=V1&HW-CC-Date=20260428T000030Z&HW-CC-Expire=86400&HW-CC-Sign=6356949A47CEC4F0A8EDF300C073E29587274731BDBFBF40A0B44B2627DB667B)

### skew12+

PhonePC/2in1TabletTVWearable

skew(x: number, y: number): Matrix4Transit

Matrix的倾斜函数，可以为当前矩阵增加x轴/y轴倾斜效果。会改变调用该函数的原始矩阵。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 设置x轴倾斜参数。 |
| y | number | 是 | 设置y轴倾斜参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Matrix4Transit](js-apis-matrix4.md#matrix4transit) | 倾斜效果后的矩阵对象。 |

**示例：**

```
1. // xxx.ets
2. import { matrix4 } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Test {
7. private matrix1 = matrix4.identity().skew(2, 3);

9. build() {
10. Column() {
11. // $r("app.media.bg1")需要替换为开发者所需的图像资源文件。
12. Image($r("app.media.bg1")).transform(this.matrix1)
13. .height(100)
14. .margin({
15. top: 300
16. })
17. }
18. .width("100%")
19. .height("100%")
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/bRwPgt61Tn23Fcr98ek6TA/zh-cn_image_0000002552959420.jpeg?HW-CC-KV=V1&HW-CC-Date=20260428T000030Z&HW-CC-Expire=86400&HW-CC-Sign=4FCF928DD084479ECC1235CE4B3DFE913CA30DF0971F41EF53434902557FE9A9)

### rotate

PhonePC/2in1TabletTVWearable

rotate(options: RotateOption): Matrix4Transit

Matrix的旋转函数，可以为当前矩阵增加x轴/y轴/z轴旋转效果。会改变调用该函数的原始矩阵。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RotateOption](js-apis-matrix4.md#rotateoption) | 是 | 设置旋转参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Matrix4Transit](js-apis-matrix4.md#matrix4transit) | 旋转效果后的矩阵对象。 |

**示例：**

```
1. // xxx.ets
2. import { matrix4 } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Test {
7. private matrix1 = matrix4.identity()
8. .rotate({
9. x: 1,
10. y: 1,
11. z: 2,
12. angle: 30
13. });

15. build() {
16. Column() {
17. // $r("app.media.bg1")需要替换为开发者所需的图像资源文件。
18. Image($r("app.media.bg1")).transform(this.matrix1)
19. .width("40%")
20. .height(100)
21. }.width("100%").margin({ top: 50 })
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/QNe8NH9xSAaWHpX34UoxNQ/zh-cn_image_0000002583479421.png?HW-CC-KV=V1&HW-CC-Date=20260428T000030Z&HW-CC-Expire=86400&HW-CC-Sign=20BDD1E184007025882DD97A57CDAAA48F47E67085AA914D3E73B19DCA8B38C2)

### transformPoint

PhonePC/2in1TabletTVWearable

transformPoint(options: [number, number]): [number, number]

Matrix的坐标点转换函数，可以将当前的变换效果作用到一个坐标点上。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [number, number] | 是 | 需要转换的坐标点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [number, number] | 返回矩阵变换后的Point对象。 |

**示例：**

```
1. // xxx.ets
2. import { matrix4 } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Test {
7. private originPoint: number[] = [50, 50];
8. private matrix_1 = matrix4.identity().translate({ x: 150, y: -50 });
9. private transformPoint = this.matrix_1.transformPoint([this.originPoint[0], this.originPoint[1]]);
10. private matrix_2 = matrix4.identity().translate({ x: this.transformPoint[0], y: this.transformPoint[1] });

12. build() {
13. Column() {
14. Text(`矩阵变换前的坐标：[${this.originPoint}]`)
15. .fontSize(16)
16. // $r("app.media.image")需要替换为开发者所需的图像资源文件。
17. Image($r("app.media.image"))
18. .width('600px')
19. .height('300px')
20. .margin({ top: 50 })
21. Text(`矩阵变换后的坐标：[${this.transformPoint}]`)
22. .fontSize(16)
23. .margin({ top: 100 })
24. // $r("app.media.image")需要替换为开发者所需的图像资源文件。
25. Image($r("app.media.image"))
26. .width('600px')
27. .height('300px')
28. .margin({ top: 50 })
29. .transform(this.matrix_2)
30. }.width("100%").padding(50)
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/03AuytpTRvOk1Au5UU46PQ/zh-cn_image_0000002552799772.png?HW-CC-KV=V1&HW-CC-Date=20260428T000030Z&HW-CC-Expire=86400&HW-CC-Sign=CF698B935AC66826D5B4C3C94FE4FF06578024ACE5E03DC839DCB0E89CA48B80)

### setPolyToPoly12+

PhonePC/2in1TabletTVWearable

setPolyToPoly(options: PolyToPolyOptions): Matrix4Transit

将一个多边形的顶点坐标映射到另外一个多边形的顶点坐标。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [PolyToPolyOptions](js-apis-matrix4.md#polytopolyoptions12) | 是 | 映射相关的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Matrix4Transit](js-apis-matrix4.md#matrix4transit) | 当前矩阵变换后的对象。 |

说明

需要配合scale({centerX:0,centerY:0,x:1})保证变换的中心点是组件左上角。

**示例：**

```
1. import { matrix4 } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. private matrix1 = matrix4.identity().setPolyToPoly({
7. src: [{ x: 0, y: 0 }, { x: 500, y: 0 }, { x: 0, y: 500 }, { x: 500, y: 500 }],
8. dst: [{ x: 0, y: 0 }, { x: 500, y: 0 }, { x: 0, y: 500 }, { x: 750, y: 1000 }], pointCount: 4
9. });

11. build() {
12. Stack() {
13. Column().backgroundColor(Color.Blue)
14. .width('500px')
15. .height('500px')
16. // $r("app.media.transition_image1")需要替换为开发者所需的图像资源文件。
17. Image($r('app.media.transition_image1'))
18. .scale({ centerX: 0, centerY: 0, x: 1 })
19. .transform(this.matrix1)
20. .width('500px')
21. .height('500px')
22. }.width("100%").height("100%").opacity(0.5)
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/Cq_vWubyR-itcOz7gKiSnw/zh-cn_image_0000002583439467.png?HW-CC-KV=V1&HW-CC-Date=20260428T000030Z&HW-CC-Expire=86400&HW-CC-Sign=81E719D58193778A757AF93EB3C043351BFC0C5C7EB3B5D8903D108833647412)

## TranslateOption

PhonePC/2in1TabletTVWearable

平移参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 是 | x轴的平移距离。  单位：px  默认值：0  取值范围 (-∞, +∞) |
| y | number | 否 | 是 | y轴的平移距离。  单位：px  默认值：0  取值范围 (-∞, +∞) |
| z | number | 否 | 是 | z轴的平移距离。  单位：px  默认值：0  取值范围 (-∞, +∞) |

## ScaleOption

PhonePC/2in1TabletTVWearable

缩放参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 是 | x轴的缩放倍数。x>1时以x轴方向放大，0<x<1时以x轴方向缩小，x<0时沿x轴反向并缩放。  默认值：1  取值范围 (-∞, +∞) |
| y | number | 否 | 是 | y轴的缩放倍数。y>1时以y轴方向放大，0<y<1时以y轴方向缩小，y<0时沿y轴反向并缩放。  默认值：1  取值范围 (-∞, +∞) |
| z | number | 否 | 是 | z轴的缩放倍数。z>1时以z轴方向放大，0<z<1时以z轴方向缩小，z<0时沿z轴反向并缩放。  默认值：1  取值范围 (-∞, +∞) |
| centerX | number | 否 | 是 | 变换中心点x轴坐标。  单位：px  默认值：组件中心点x轴坐标。  取值范围 (-∞, +∞) |
| centerY | number | 否 | 是 | 变换中心点y轴坐标。  单位：px  默认值：组件中心点y轴坐标。  取值范围 (-∞, +∞) |

## RotateOption

PhonePC/2in1TabletTVWearable

旋转参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 是 | 旋转轴向量x坐标。  默认值：0。  取值范围 (-∞, +∞) |
| y | number | 否 | 是 | 旋转轴向量y坐标。  默认值：0。  取值范围 (-∞, +∞) |
| z | number | 否 | 是 | 旋转轴向量z坐标。  默认值：0。  取值范围 (-∞, +∞)。  **说明：** 旋转向量中x、y、z至少有一个不为0才有意义。 |
| angle | number | 否 | 是 | 旋转角度。  默认值：0 |
| centerX | number | 否 | 是 | 单次矩阵变换中心点相对于组件变换中心点（锚点）的额外x轴偏移值。  单位：px  默认值：0  **说明：**  为0时表示x方向的矩阵变换中心恰好为组件x方向锚点，取值表示相对组件x方向锚点的额外偏移量。具体实现可参考[示例3（按中心点旋转）](ts-universal-attributes-transformation.md#示例3按中心点旋转)。 |
| centerY | number | 否 | 是 | 单次矩阵变换中心点相对于组件变换中心点（锚点）的额外y轴偏移值。  单位：px  默认值：0  **说明：**  为0时表示y方向的矩阵变换中心恰好为组件y方向锚点，取值表示相对组件y方向锚点的额外偏移量。具体实现可参考[示例3（按中心点旋转）](ts-universal-attributes-transformation.md#示例3按中心点旋转)。 |

## PolyToPolyOptions12+

PhonePC/2in1TabletTVWearable

多边形到多边形的映射选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| src | Array<[Point](js-apis-matrix4.md#point12)> | 否 | 否 | 源点坐标。 |
| srcIndex | number | 否 | 是 | 源点坐标起始索引。  默认值:0  取值范围：[0, +∞) |
| dst | Array<[Point](js-apis-matrix4.md#point12)> | 否 | 否 | 目标点坐标。 |
| dstIndex | number | 否 | 是 | 目标坐标起始索引。  默认值: src.length/2  取值范围：[0, +∞) |
| pointCount | number | 否 | 是 | 使用到的点数量。要使用的点的数量如果为0，则返回单位矩阵。如果为1，则返回一个将两个点改变之前的平移矩阵。如果为2-4，则返回一个变换矩阵。  默认值: 0  取值范围：[0, +∞) |

## Point12+

PhonePC/2in1TabletTVWearable

坐标点的数据结构。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | x轴坐标。  取值范围：(-∞, +∞) |
| y | number | 否 | 否 | y轴坐标。  取值范围：(-∞, +∞) |

## matrix4.copy(deprecated)

PhonePC/2in1TabletTVWearable

copy(): Matrix4Transit

Matrix的拷贝函数，可以拷贝一份当前的矩阵对象。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[Matrix4Transit.copy](js-apis-matrix4.md#copy)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Matrix4Transit](js-apis-matrix4.md#matrix4transit) | 当前矩阵的拷贝对象。 |

**示例：**

```
1. // xxx.ets
2. import { matrix4 } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Test {
7. private matrix1 = matrix4.identity().translate({ x: 100 });
8. // 对matrix1的拷贝矩阵做scale操作，不影响到matrix1
9. private matrix2 = this.matrix1.copy().scale({ x: 2 });

11. build() {
12. Column() {
13. // $r("app.media.bg1")需要替换为开发者所需的图像资源文件。
14. Image($r("app.media.bg1"))
15. .width("40%")
16. .height(100)
17. .transform(this.matrix1)
18. // $r("app.media.bg2")需要替换为开发者所需的图像资源文件。
19. Image($r("app.media.bg2"))
20. .width("40%")
21. .height(100)
22. .margin({ top: 50 })
23. .transform(this.matrix2)
24. }
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/62aoUPoAT4a9LDmV2D66NQ/zh-cn_image_0000002552959422.png?HW-CC-KV=V1&HW-CC-Date=20260428T000030Z&HW-CC-Expire=86400&HW-CC-Sign=6878B2F2BA0A1B38F47E911C510FF546F93470A252A92B1F6306987D87887BCD)

## matrix4.invert(deprecated)

PhonePC/2in1TabletTVWearable

invert(): Matrix4Transit

Matrix的逆函数，可以返回一个当前矩阵对象的逆矩阵，即效果正好相反。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[Matrix4Transit.invert](js-apis-matrix4.md#invert)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Matrix4Transit](js-apis-matrix4.md#matrix4transit) | 当前矩阵的逆矩阵对象。 |

## matrix4.combine(deprecated)

PhonePC/2in1TabletTVWearable

combine(options: Matrix4Transit): Matrix4Transit

Matrix的叠加函数，可以将两个矩阵的效果叠加起来生成一个新的矩阵对象。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[Matrix4Transit.combine](js-apis-matrix4.md#combine)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Matrix4Transit](js-apis-matrix4.md#matrix4transit) | 是 | 待叠加的矩阵对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Matrix4Transit](js-apis-matrix4.md#matrix4transit) | 叠加后的矩阵对象。 |

## matrix4.translate(deprecated)

PhonePC/2in1TabletTVWearable

translate(options: TranslateOption): Matrix4Transit

Matrix的平移函数，可以为当前矩阵增加x轴/y轴/z轴平移效果。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[Matrix4Transit.translate](js-apis-matrix4.md#translate)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TranslateOption](js-apis-matrix4.md#translateoption) | 是 | 设置平移参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Matrix4Transit](js-apis-matrix4.md#matrix4transit) | 平移后的矩阵对象。 |

## matrix4.scale(deprecated)

PhonePC/2in1TabletTVWearable

scale(options: ScaleOption): Matrix4Transit

Matrix的缩放函数，可以为当前矩阵增加x轴/y轴/z轴缩放效果。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[Matrix4Transit.scale](js-apis-matrix4.md#scale)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ScaleOption](js-apis-matrix4.md#scaleoption) | 是 | 设置缩放参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Matrix4Transit](js-apis-matrix4.md#matrix4transit) | 缩放后的矩阵对象。 |

## matrix4.rotate(deprecated)

PhonePC/2in1TabletTVWearable

rotate(options: RotateOption): Matrix4Transit

Matrix的旋转函数，可以为当前矩阵增加x轴/y轴/z轴旋转效果。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[Matrix4Transit.rotate](js-apis-matrix4.md#rotate)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RotateOption](js-apis-matrix4.md#rotateoption) | 是 | 设置旋转参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Matrix4Transit](js-apis-matrix4.md#matrix4transit) | 旋转后的矩阵对象。 |

## matrix4.transformPoint(deprecated)

PhonePC/2in1TabletTVWearable

transformPoint(options: [number, number]): [number, number]

Matrix的坐标点转换函数，可以将当前的变换效果作用到一个坐标点上。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[Matrix4Transit.transformPoint](js-apis-matrix4.md#transformpoint)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [number, number] | 是 | 需要转换的坐标点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [number, number] | 返回矩阵变换后的Point对象。 |
