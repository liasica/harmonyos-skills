---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-matrix
title: Class (Matrix)
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.drawing (绘制模块) > Class (Matrix)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f3659fd650933ec3f2ff69fa5733b95a26ca1bb1e1a7c969a43bf6df6df5fb71
---

矩阵对象。

表示为3\*3的矩阵，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/cV6pjRSLQuOVUQAJzhZFHQ/zh-cn_image_0000002583440909.png?HW-CC-KV=V1&HW-CC-Date=20260428T001437Z&HW-CC-Expire=86400&HW-CC-Sign=9C7B5686D1A9B49BAFA23439D208054E8C39EA1EAE88034FEAD727C65A9B2C9B)

矩阵中的元素从左到右，从上到下分别表示水平缩放系数、水平倾斜系数、水平位移系数、垂直倾斜系数、垂直缩放系数、垂直位移系数、X轴透视系数、Y轴透视系数、透视缩放系数。

设(x1, y1)为源坐标点，(x2, y2)为源坐标点通过矩阵变换后的坐标点，则两个坐标点的关系如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/_66T52cRRZWdDTbM7Xk3fw/zh-cn_image_0000002552960864.png?HW-CC-KV=V1&HW-CC-Date=20260428T001437Z&HW-CC-Expire=86400&HW-CC-Sign=507AFD14924CC53062729ECCD82AA163A3604DC6BB2A0C926A5FD795EB8D6063)

说明

* 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 12开始支持。
* 本模块使用屏幕物理像素单位px。
* 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { drawing } from '@kit.ArkGraphics2D';
```

## constructor12+

PhonePC/2in1TabletTVWearable

constructor()

构造一个矩阵对象。

**系统能力：** SystemCapability.Graphics.Drawing

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let matrix = new drawing.Matrix();
```

## constructor20+

PhonePC/2in1TabletTVWearable

constructor(matrix: Matrix)

拷贝一个矩阵。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| matrix | [Matrix](arkts-apis-graphics-drawing-matrix.md) | 是 | 被拷贝的矩阵。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let matrix = new drawing.Matrix();
4. let matrix2 = new drawing.Matrix(matrix);
```

## isAffine20+

PhonePC/2in1TabletTVWearable

isAffine(): boolean

判断当前矩阵是否为仿射矩阵。仿射矩阵是一种包括平移、旋转、缩放等变换的矩阵。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回当前矩阵是否为仿射矩阵。true表示是仿射矩阵，false表示不是仿射矩阵。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let matrix = new drawing.Matrix();
4. matrix.setMatrix([1, 0.5, 1, 0.5, 1, 1, 1, 1, 1]);
5. let isAff = matrix.isAffine();
6. console.info('isAff :', isAff);
```

## rectStaysRect20+

PhonePC/2in1TabletTVWearable

rectStaysRect(): boolean

判断经过该矩阵映射后的矩形的形状是否仍为矩形。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回经过该矩阵映射后的矩形的形状是否仍为矩形。true表示仍是矩形，false表示不是矩形。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let matrix = new drawing.Matrix();
4. matrix.setMatrix([1, 0.5, 1, 0.5, 1, 1, 1, 1, 1]);
5. let matrix2 = new drawing.Matrix(matrix);
6. let isRect = matrix2.rectStaysRect();
7. console.info('isRect :', isRect);
```

## setSkew20+

PhonePC/2in1TabletTVWearable

setSkew(kx: number, ky: number, px: number, py: number): void

设置矩阵的倾斜系数。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| kx | number | 是 | x轴上的倾斜量，该参数为浮点数。正值会使绘制沿y轴增量方向向右倾斜；负值会使绘制沿y轴增量方向向左倾斜。 |
| ky | number | 是 | y轴上的倾斜量，该参数为浮点数。正值会使绘制沿x轴增量方向向下倾斜；负值会使绘制沿x轴增量方向向上倾斜。 |
| px | number | 是 | 倾斜中心点的x轴坐标，该参数为浮点数。0表示坐标原点，正数表示位于坐标原点右侧，负数表示位于坐标原点左侧。 |
| py | number | 是 | 倾斜中心点的y轴坐标，该参数为浮点数。0表示坐标原点，正数表示位于坐标原点下侧，负数表示位于坐标原点上侧。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let matrix = new drawing.Matrix();
4. matrix.setMatrix([1, 0.5, 1, 0.5, 1, 1, 1, 1, 1]);
5. matrix.setSkew(2, 0.5, 0.5, 2);
```

## setSinCos20+

PhonePC/2in1TabletTVWearable

setSinCos(sinValue: number, cosValue: number, px: number, py: number): void

设置矩阵，使其围绕旋转中心(px, py)以指定的正弦值和余弦值旋转。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sinValue | number | 是 | 旋转角度的正弦值。仅当正弦值和余弦值的平方和为1时，为旋转变换，否则矩阵可能包含平移缩放等其他变换。 |
| cosValue | number | 是 | 旋转角度的余弦值。仅当正弦值和余弦值的平方和为1时，为旋转变换，否则矩阵可能包含平移缩放等其他变换。 |
| px | number | 是 | 旋转中心的x轴坐标，该参数为浮点数。0表示坐标原点，正数表示位于坐标原点右侧，负数表示位于坐标原点左侧。 |
| py | number | 是 | 旋转中心的y轴坐标，该参数为浮点数。0表示坐标原点，正数表示位于坐标原点下侧，负数表示位于坐标原点上侧。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let matrix = new drawing.Matrix();
4. matrix.setMatrix([1, 0.5, 1, 0.5, 1, 1, 1, 1, 1]);
5. matrix.setSinCos(0, 1, 1, 0);
```

## setRotation12+

PhonePC/2in1TabletTVWearable

setRotation(degree: number, px: number, py: number): void

设置矩阵为单位矩阵，并围绕位于(px, py)的旋转轴点进行旋转。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| degree | number | 是 | 角度，单位为度。正数表示顺时针旋转，负数表示逆时针旋转，该参数为浮点数。 |
| px | number | 是 | 旋转轴点的横坐标，该参数为浮点数。 |
| py | number | 是 | 旋转轴点的纵坐标，该参数为浮点数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let matrix = new drawing.Matrix();
4. matrix.setRotation(90, 100, 100);
```

## setScale12+

PhonePC/2in1TabletTVWearable

setScale(sx: number, sy: number, px: number, py: number): void

设置矩阵为单位矩阵围绕位于(px, py)的中心点，以sx和sy进行缩放后的结果。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sx | number | 是 | x轴方向缩放系数，为负数时可看作是先关于y = px作镜像翻转后再进行缩放，该参数为浮点数。 |
| sy | number | 是 | y轴方向缩放系数，为负数时可看作是先关于x = py作镜像翻转后再进行缩放，该参数为浮点数。 |
| px | number | 是 | 缩放中心点的横坐标，该参数为浮点数。 |
| py | number | 是 | 缩放中心点的纵坐标，该参数为浮点数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let matrix = new drawing.Matrix();
4. matrix.setScale(100, 100, 150, 150);
```

## setTranslation12+

PhonePC/2in1TabletTVWearable

setTranslation(dx: number, dy: number): void

设置矩阵为单位矩阵平移(dx, dy)后的结果。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dx | number | 是 | x轴方向平移距离，正数表示往x轴正方向平移，负数表示往x轴负方向平移，该参数为浮点数。 |
| dy | number | 是 | y轴方向平移距离，正数表示往y轴正方向平移，负数表示往y轴负方向平移，该参数为浮点数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let matrix = new drawing.Matrix();
4. matrix.setTranslation(100, 100);
```

## setMatrix12+

PhonePC/2in1TabletTVWearable

setMatrix(values: Array<number>): void

设置矩阵对象的各项参数。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | Array<number> | 是 | 长度为9的浮点数组，表示矩阵对象参数。数组中的值按下标从小，到大分别表示水平缩放系数、水平倾斜系数、水平位移系数、垂直倾斜系数、垂直缩放系数、垂直位移系数、X轴透视系数、Y轴透视系数、透视缩放系数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let matrix = new drawing.Matrix();
4. let value : Array<number> = [2, 2, 2, 2, 2, 2, 2, 2, 2];
5. matrix.setMatrix(value);
```

## preConcat12+

PhonePC/2in1TabletTVWearable

preConcat(matrix: Matrix): void

将当前矩阵设置为当前矩阵左乘matrix的结果。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| matrix | [Matrix](arkts-apis-graphics-drawing-matrix.md) | 是 | 表示矩阵对象，位于乘法表达式右侧。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let matrix1 = new drawing.Matrix();
4. matrix1.setMatrix([2, 1, 3, 1, 2, 1, 3, 1, 2]);
5. let matrix2 = new drawing.Matrix();
6. matrix2.setMatrix([-2, 1, 3, 1, 0, -1, 3, -1, 2]);
7. matrix1.preConcat(matrix2);
```

## setMatrix20+

PhonePC/2in1TabletTVWearable

setMatrix(matrix: Array<number> | Matrix): void

用一个矩阵对当前矩阵进行更新。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| matrix | Array<number> | [Matrix](arkts-apis-graphics-drawing-matrix.md) | 是 | 用于更新的数组或矩阵。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let matrix1 = new drawing.Matrix();
4. matrix1.setMatrix([2, 1, 3, 1, 2, 1, 3, 1, 2]);
5. let matrix2 = new drawing.Matrix();
6. matrix1.setMatrix(matrix2);
```

## setConcat20+

PhonePC/2in1TabletTVWearable

setConcat(matrixA: Matrix, matrixB: Matrix): void

用两个矩阵的乘积更新当前矩阵。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| matrixA | [Matrix](arkts-apis-graphics-drawing-matrix.md) | 是 | 用于运算的矩阵A。 |
| matrixB | [Matrix](arkts-apis-graphics-drawing-matrix.md) | 是 | 用于运算的矩阵B。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let matrix1 = new drawing.Matrix();
4. matrix1.setMatrix([2, 1, 3, 1, 2, 1, 3, 1, 2]);
5. let matrix2 = new drawing.Matrix();
6. matrix2.setMatrix([-2, 1, 3, 1, 0, -1, 3, -1, 2]);
7. matrix1.setConcat(matrix2, matrix1);
```

## postConcat20+

PhonePC/2in1TabletTVWearable

postConcat(matrix: Matrix): void

用当前矩阵右乘一个矩阵。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| matrix | [Matrix](arkts-apis-graphics-drawing-matrix.md) | 是 | 用于运算的矩阵。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let matrix = new drawing.Matrix();
4. if (matrix.isIdentity()) {
5. console.info("matrix is identity.");
6. } else {
7. console.info("matrix is not identity.");
8. }
9. let matrix1 = new drawing.Matrix();
10. matrix1.setMatrix([2, 1, 3, 1, 2, 1, 3, 1, 2]);
11. let matrix2 = new drawing.Matrix();
12. matrix2.setMatrix([-2, 1, 3, 1, 0, -1, 3, -1, 2]);
13. matrix1.postConcat(matrix2);
```

## isEqual12+

PhonePC/2in1TabletTVWearable

isEqual(matrix: Matrix): Boolean

判断两个矩阵是否相等。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| matrix | [Matrix](arkts-apis-graphics-drawing-matrix.md) | 是 | 另一个矩阵。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Boolean | 返回两个矩阵的比较结果。true表示两个矩阵相等，false表示两个矩阵不相等。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let matrix1 = new drawing.Matrix();
4. matrix1.setMatrix([2, 1, 3, 1, 2, 1, 3, 1, 2]);
5. let matrix2 = new drawing.Matrix();
6. matrix2.setMatrix([-2, 1, 3, 1, 0, -1, 3, -1, 2]);
7. if (matrix1.isEqual(matrix2)) {
8. console.info("matrix1 and matrix2 are equal.");
9. } else {
10. console.info("matrix1 and matrix2 are not equal.");
11. }
```

## invert12+

PhonePC/2in1TabletTVWearable

invert(matrix: Matrix): Boolean

将矩阵matrix设置为当前矩阵的逆矩阵，并返回是否设置成功的结果。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| matrix | [Matrix](arkts-apis-graphics-drawing-matrix.md) | 是 | 矩阵对象，用于存储获取到的逆矩阵。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Boolean | 返回matrix是否被设置为逆矩阵的结果。true表示当前矩阵可逆，matrix被设置为逆矩阵，false表示当前矩阵不可逆，matrix不被设置。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let matrix1 = new drawing.Matrix();
4. matrix1.setMatrix([2, 1, 3, 1, 2, 1, 3, 1, 2]);
5. let matrix2 = new drawing.Matrix();
6. matrix2.setMatrix([-2, 1, 3, 1, 0, -1, 3, -1, 2]);
7. if (matrix1.invert(matrix2)) {
8. console.info("matrix1 is invertible and matrix2 is set as an inverse matrix of the matrix1.");
9. } else {
10. console.info("matrix1 is not invertible and matrix2 is not changed.");
11. }
```

## isIdentity12+

PhonePC/2in1TabletTVWearable

isIdentity(): Boolean

判断矩阵是否是单位矩阵。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Boolean | 返回矩阵是否是单位矩阵。true表示矩阵是单位矩阵，false表示矩阵不是单位矩阵。 |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let matrix = new drawing.Matrix();
4. if (matrix.isIdentity()) {
5. console.info("matrix is identity.");
6. } else {
7. console.info("matrix is not identity.");
8. }
```

## getValue12+

PhonePC/2in1TabletTVWearable

getValue(index: number): number

获取矩阵给定索引位的值。索引范围0-8。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 索引位置，范围0-8，该参数为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 函数返回矩阵给定索引位对应的值，该返回值为整数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例：**

```
1. import { drawing } from "@kit.ArkGraphics2D";

3. let matrix = new drawing.Matrix();
4. for (let i = 0; i < 9; i++) {
5. console.info("matrix "+matrix.getValue(i).toString());
6. }
```

## postRotate12+

PhonePC/2in1TabletTVWearable

postRotate(degree: number, px: number, py: number): void

将矩阵设置为矩阵右乘围绕轴心点旋转一定角度的单位矩阵后得到的矩阵。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| degree | number | 是 | 旋转角度，单位为度。正数表示顺时针旋转，负数表示逆时针旋转，该参数为浮点数。 |
| px | number | 是 | 旋转中心点的横坐标，该参数为浮点数。 |
| py | number | 是 | 旋转中心点的纵坐标，该参数为浮点数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from "@kit.ArkGraphics2D";

3. let matrix = new drawing.Matrix();
4. let degree: number = 2;
5. let px: number = 3;
6. let py: number = 4;
7. matrix.postRotate(degree, px, py);
8. console.info("matrix= "+matrix.getAll().toString());
```

## postScale12+

PhonePC/2in1TabletTVWearable

postScale(sx: number, sy: number, px: number, py: number): void

将矩阵设置为矩阵右乘围绕轴心点按一定缩放系数缩放后的单位矩阵后得到的矩阵。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sx | number | 是 | x轴方向缩放系数，负数表示先关于y = px作镜像翻转后再进行缩放，该参数为浮点数。 |
| sy | number | 是 | y轴方向缩放系数，负数表示先关于x = py作镜像翻转后再进行缩放，该参数为浮点数。 |
| px | number | 是 | 缩放中心点的横坐标，该参数为浮点数。 |
| py | number | 是 | 缩放中心点的纵坐标，该参数为浮点数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from "@kit.ArkGraphics2D";

3. let matrix = new drawing.Matrix();
4. let sx: number = 2;
5. let sy: number = 0.5;
6. let px: number = 1;
7. let py: number = 1;
8. matrix.postScale(sx, sy, px, py);
9. console.info("matrix= "+matrix.getAll().toString());
```

## postTranslate12+

PhonePC/2in1TabletTVWearable

postTranslate(dx: number, dy: number): void

将矩阵设置为矩阵右乘平移一定距离后的单位矩阵后得到的矩阵。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dx | number | 是 | x轴方向平移距离，正数表示往x轴正方向平移，负数表示往x轴负方向平移，该参数为浮点数。 |
| dy | number | 是 | y轴方向平移距离，正数表示往y轴正方向平移，负数表示往y轴负方向平移，该参数为浮点数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from "@kit.ArkGraphics2D";

3. let matrix = new drawing.Matrix();
4. let dx: number = 3;
5. let dy: number = 4;
6. matrix.postTranslate(dx, dy);
7. console.info("matrix= "+matrix.getAll().toString());
```

## preRotate12+

PhonePC/2in1TabletTVWearable

preRotate(degree: number, px: number, py: number): void

将矩阵设置为矩阵左乘围绕轴心点旋转一定角度的单位矩阵后得到的矩阵。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| degree | number | 是 | 旋转角度，单位为度。正数表示顺时针旋转，负数表示逆时针旋转，该参数为浮点数。 |
| px | number | 是 | 旋转中心点的横坐标，该参数为浮点数。 |
| py | number | 是 | 旋转中心点的纵坐标，该参数为浮点数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from "@kit.ArkGraphics2D";

3. let matrix = new drawing.Matrix();
4. let degree: number = 2;
5. let px: number = 3;
6. let py: number = 4;
7. matrix.preRotate(degree, px, py);
8. console.info("matrix= "+matrix.getAll().toString());
```

## postSkew20+

PhonePC/2in1TabletTVWearable

postSkew(kx: number, ky: number, px: number, py: number): void

当前矩阵右乘一个倾斜变换矩阵。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| kx | number | 是 | x轴上的倾斜量，该参数为浮点数。正值会使绘制沿y轴增量方向向右倾斜；负值会使绘制沿y轴增量方向向左倾斜。 |
| ky | number | 是 | y轴上的倾斜量，该参数为浮点数。正值会使绘制沿x轴增量方向向下倾斜；负值会使绘制沿x轴增量方向向上倾斜。 |
| px | number | 是 | 倾斜中心点的x轴坐标，该参数为浮点数。0表示坐标原点，正数表示位于坐标原点右侧，负数表示位于坐标原点左侧。 |
| py | number | 是 | 倾斜中心点的y轴坐标，该参数为浮点数。0表示坐标原点，正数表示位于坐标原点下侧，负数表示位于坐标原点上侧。 |

**示例：**

```
1. import { drawing } from "@kit.ArkGraphics2D"

3. let matrix = new drawing.Matrix();
4. matrix.postSkew(2.0, 1.0, 2.0, 1.0);
```

## preSkew20+

PhonePC/2in1TabletTVWearable

preSkew(kx: number, ky: number, px: number, py: number): void

当前矩阵左乘一个倾斜变换矩阵。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| kx | number | 是 | x轴上的倾斜量，该参数为浮点数。正值会使绘制沿y轴增量方向向右倾斜；负值会使绘制沿y轴增量方向向左倾斜。 |
| ky | number | 是 | y轴上的倾斜量，该参数为浮点数。正值会使绘制沿x轴增量方向向下倾斜；负值会使绘制沿x轴增量方向向上倾斜。 |
| px | number | 是 | 倾斜中心点的x轴坐标，该参数为浮点数。0表示坐标原点，正数表示位于坐标原点右侧，负数表示位于坐标原点左侧。 |
| py | number | 是 | 倾斜中心点的y轴坐标，该参数为浮点数。0表示坐标原点，正数表示位于坐标原点下侧，负数表示位于坐标原点上侧。 |

**示例：**

```
1. import { drawing } from "@kit.ArkGraphics2D"

3. let matrix = new drawing.Matrix();
4. matrix.preSkew(2.0, 1.0, 2.0, 1.0);
```

## mapRadius20+

PhonePC/2in1TabletTVWearable

mapRadius(radius: number): number

返回半径为radius的圆经过当前矩阵映射形成的椭圆的平均半径。平均半径的平方为椭圆长轴长度和短轴长度的乘积。若当前矩阵包含透视变换，则该结果无意义。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radius | number | 是 | 用于计算的圆的半径，浮点数。如果是负数，则按照绝对值进行计算。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回经过变换之后的平均半径。 |

**示例：**

```
1. import { drawing } from "@kit.ArkGraphics2D"

3. let matrix = new drawing.Matrix();
4. matrix.setMatrix([2, 1, 3, 1, 2, 1, 3, 1, 2]);
5. let radius = matrix.mapRadius(10);
6. console.info('radius', radius);
```

## preScale12+

PhonePC/2in1TabletTVWearable

preScale(sx: number, sy: number, px: number, py: number): void

将矩阵设置为矩阵左乘围绕轴心点按一定缩放系数缩放后的单位矩阵后得到的矩阵。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sx | number | 是 | x轴方向缩放系数，为负数时可看作是先关于y = px作镜像翻转后再进行缩放，该参数为浮点数。 |
| sy | number | 是 | y轴方向缩放系数，为负数时可看作是先关于x = py作镜像翻转后再进行缩放，该参数为浮点数。 |
| px | number | 是 | 轴心点横坐标，该参数为浮点数。 |
| py | number | 是 | 轴心点纵坐标，该参数为浮点数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from "@kit.ArkGraphics2D";

3. let matrix = new drawing.Matrix();
4. let sx: number = 2;
5. let sy: number = 0.5;
6. let px: number = 1;
7. let py: number = 1;
8. matrix.preScale(sx, sy, px, py);
9. console.info("matrix"+matrix.getAll().toString());
```

## preTranslate12+

PhonePC/2in1TabletTVWearable

preTranslate(dx: number, dy: number): void

将矩阵设置为矩阵左乘平移一定距离后的单位矩阵后得到的矩阵。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dx | number | 是 | x轴方向平移距离，正数表示往x轴正方向平移，负数表示往x轴负方向平移，该参数为浮点数。 |
| dy | number | 是 | y轴方向平移距离，正数表示往y轴正方向平移，负数表示往y轴负方向平移，该参数为浮点数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from "@kit.ArkGraphics2D";

3. let matrix = new drawing.Matrix();
4. let dx: number = 3;
5. let dy: number = 4;
6. matrix.preTranslate(dx, dy);
7. console.info("matrix"+matrix.getAll().toString());
```

## reset12+

PhonePC/2in1TabletTVWearable

reset(): void

重置当前矩阵为单位矩阵。

**系统能力：** SystemCapability.Graphics.Drawing

**示例：**

```
1. import { drawing } from "@kit.ArkGraphics2D";

3. let matrix = new drawing.Matrix();
4. matrix.postScale(2, 3, 4, 5);
5. matrix.reset();
6. console.info("matrix= "+matrix.getAll().toString());
```

## mapPoints12+

PhonePC/2in1TabletTVWearable

mapPoints(src: Array<common2D.Point>): Array<common2D.Point>

通过矩阵变换将源点数组映射到目标点数组。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | Array<[common2D.Point](js-apis-graphics-common2d.md#point12)> | 是 | 源点数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[common2D.Point](js-apis-graphics-common2d.md#point12)> | 源点数组经矩阵变换后的点数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing, common2D } from "@kit.ArkGraphics2D";

3. let src: Array<common2D.Point> = [];
4. src.push({x: 15, y: 20});
5. src.push({x: 20, y: 15});
6. src.push({x: 30, y: 10});
7. let matrix = new drawing.Matrix();
8. let dst: Array<common2D.Point> = matrix.mapPoints(src);
9. console.info("matrix= src: "+JSON.stringify(src));
10. console.info("matrix= dst: "+JSON.stringify(dst));
```

## getAll12+

PhonePC/2in1TabletTVWearable

getAll(): Array<number>

获取矩阵的所有元素值。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<number> | 存储矩阵元素值的浮点数组，长度为9。 |

**示例：**

```
1. import { drawing } from "@kit.ArkGraphics2D";

3. let matrix = new drawing.Matrix();
4. console.info("matrix "+ matrix.getAll());
```

## mapRect12+

PhonePC/2in1TabletTVWearable

mapRect(dst: common2D.Rect, src: common2D.Rect): boolean

将目标矩形设置为源矩形通过矩阵变换后的图形的外接矩形。如下图所示，蓝色矩形为源矩形，假设黄色矩形为源矩形通过矩阵变换形成的图形，此时黄色矩形的边不与坐标轴平行，无法使用矩形对象表示，因此，将目标矩形设置为黄色矩形的外接矩形，即黑色矩形。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/41pqp6qHTC-CoaiaemcVCQ/zh-cn_image_0000002583480865.png?HW-CC-KV=V1&HW-CC-Date=20260428T001437Z&HW-CC-Expire=86400&HW-CC-Sign=FE65F3C113262A3783E54493BE38AD8F2F1D084CC641EFE77756253035A8AACC)

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dst | [common2D.Rect](js-apis-graphics-common2d.md#rect) | 是 | 目标矩形对象，用于存储源矩形经矩阵变换后的图形的外接矩形。 |
| src | [common2D.Rect](js-apis-graphics-common2d.md#rect) | 是 | 源矩形对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回源矩形经过矩阵变换后的图形是否仍然是矩形，true表示是矩形，false表示不是矩形。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing, common2D } from "@kit.ArkGraphics2D";

3. let dst: common2D.Rect = { left: 100, top: 20, right: 130, bottom: 60 };
4. let src: common2D.Rect = { left: 100, top: 80, right: 130, bottom: 120 };
5. let matrix = new drawing.Matrix();
6. if (matrix.mapRect(dst, src)) {
7. console.info("matrix= dst "+JSON.stringify(dst));
8. }
```

## setRectToRect12+

PhonePC/2in1TabletTVWearable

setRectToRect(src: common2D.Rect, dst: common2D.Rect, scaleToFit: ScaleToFit): boolean

将当前矩阵设置为能使源矩形映射到目标矩形的变换矩阵。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [common2D.Rect](js-apis-graphics-common2d.md#rect) | 是 | 源矩形。 |
| dst | [common2D.Rect](js-apis-graphics-common2d.md#rect) | 是 | 目标矩形。 |
| scaleToFit | [ScaleToFit](arkts-apis-graphics-drawing-e.md#scaletofit12) | 是 | 源矩形到目标矩形的映射方式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回矩阵是否可以表示矩形之间的映射，true表示可以，false表示不可以。如果源矩形的宽高任意一个小于等于0，则返回false，并将矩阵设置为单位矩阵；如果目标矩形的宽高任意一个小于等于0，则返回true，并将矩阵设置为除透视缩放系数为1外其余值皆为0的矩阵。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```
1. import { drawing, common2D } from "@kit.ArkGraphics2D";

3. let src: common2D.Rect = { left: 100, top: 100, right: 300, bottom: 300 };
4. let dst: common2D.Rect = { left: 200, top: 200, right: 600, bottom: 600 };
5. let scaleToFit: drawing.ScaleToFit = drawing.ScaleToFit.FILL_SCALE_TO_FIT
6. let matrix = new drawing.Matrix();
7. if (matrix.setRectToRect(src, dst, scaleToFit)) {
8. console.info("matrix"+matrix.getAll().toString());
9. }
```

## setPolyToPoly12+

PhonePC/2in1TabletTVWearable

setPolyToPoly(src: Array<common2D.Point>, dst: Array<common2D.Point>, count: number): boolean

将当前矩阵设置为能够将源点数组映射到目标点数组的变换矩阵。源点和目标点的个数必须大于等于0，小于等于4。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | Array<[common2D.Point](js-apis-graphics-common2d.md#point12)> | 是 | 源点数组，长度必须为count。 |
| dst | Array<[common2D.Point](js-apis-graphics-common2d.md#point12)> | 是 | 目标点数组，长度必须为count。 |
| count | number | 是 | 在src和dst点的数量，该参数为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回设置矩阵是否成功的结果，true表示设置成功，false表示设置失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing, common2D } from "@kit.ArkGraphics2D";

3. let srcPoints: Array<common2D.Point> = [ {x: 10, y: 20}, {x: 200, y: 150} ];
4. let dstPoints: Array<common2D.Point> = [{ x:0, y: 10 }, { x:300, y: 600 }];
5. let matrix = new drawing.Matrix();
6. if (matrix.setPolyToPoly(srcPoints, dstPoints, 2)) {
7. console.info("matrix"+matrix.getAll().toString());
8. }
```
