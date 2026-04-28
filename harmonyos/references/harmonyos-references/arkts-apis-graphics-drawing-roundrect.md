---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-roundrect
title: Class (RoundRect)
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.drawing (绘制模块) > Class (RoundRect)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0d4326dfc83b1848b156ee13cedf7f5a0ffbe7927974a1800f8814e0999d0fc5
---

圆角矩形对象。

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

## constructor20+

PhonePC/2in1TabletTVWearable

constructor(roundRect: RoundRect)

拷贝一个圆角矩形。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| roundRect | [RoundRect](arkts-apis-graphics-drawing-roundrect.md) | 是 | 用于拷贝的圆角矩形。 |

**示例：**

```
1. import { common2D, drawing } from '@kit.ArkGraphics2D';

3. let rect: common2D.Rect = {left : 100, top : 100, right : 500, bottom : 300};
4. let roundRect = new drawing.RoundRect(rect, 50, 50);
5. let roundRect2 = new drawing.RoundRect(roundRect);
```

## constructor12+

PhonePC/2in1TabletTVWearable

constructor(rect: common2D.Rect, xRadii: number, yRadii: number)

构造一个圆角矩形对象，当且仅当xRadii和yRadii均大于0时，圆角生效，否则只会构造一个矩形。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rect | [common2D.Rect](js-apis-graphics-common2d.md#rect) | 是 | 需要创建的圆角矩形区域。 |
| xRadii | number | 是 | X轴上的圆角半径，该参数为浮点数，小于等于0时无效。 |
| yRadii | number | 是 | Y轴上的圆角半径，该参数为浮点数，小于等于0时无效。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { common2D, drawing } from '@kit.ArkGraphics2D';

3. let rect: common2D.Rect = {left : 100, top : 100, right : 500, bottom : 300};
4. let roundRect = new drawing.RoundRect(rect, 50, 50);
```

## setCorner12+

PhonePC/2in1TabletTVWearable

setCorner(pos: CornerPos, x: number, y: number): void

设置圆角矩形中指定圆角位置的圆角半径。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pos | [CornerPos](arkts-apis-graphics-drawing-e.md#cornerpos12) | 是 | 圆角位置。 |
| x | number | 是 | x轴方向的圆角半径，该参数为浮点数，小于等于0时无效。 |
| y | number | 是 | y轴方向的圆角半径，该参数为浮点数，小于等于0时无效。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let roundRect : drawing.RoundRect = new drawing.RoundRect({left: 0, top: 0, right: 300, bottom: 300}, 50, 50);
4. roundRect.setCorner(drawing.CornerPos.TOP_LEFT_POS, 150, 150);
```

## getCorner12+

PhonePC/2in1TabletTVWearable

getCorner(pos: CornerPos): common2D.Point

获取圆角矩形中指定圆角位置的圆角半径。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pos | [CornerPos](arkts-apis-graphics-drawing-e.md#cornerpos12) | 是 | 圆角位置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [common2D.Point](js-apis-graphics-common2d.md#point12) | 返回一个点，其横坐标表示圆角x轴方向上的半径，纵坐标表示y轴方向上的半径。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let roundRect : drawing.RoundRect = new drawing.RoundRect({left: 0, top: 0, right: 300, bottom: 300}, 50, 50);
4. let cornerRadius = roundRect.getCorner(drawing.CornerPos.BOTTOM_LEFT_POS);
5. console.info("getCorner---"+cornerRadius.x)
6. console.info("getCorner---"+cornerRadius.y)
```

## offset12+

PhonePC/2in1TabletTVWearable

offset(dx: number, dy: number): void

将圆角矩形分别沿x轴方向和y轴方向平移dx,dy。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dx | number | 是 | 表示x轴方向上的偏移量。正数表示向x轴正方向平移，负数表示向x轴负方向平移，该参数为浮点数。 |
| dy | number | 是 | 表示y轴方向上的偏移量。正数表示向y轴正方向平移，负数表示向y轴负方向平移，该参数为浮点数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let roundRect : drawing.RoundRect = new drawing.RoundRect({left: 0, top: 0, right: 300, bottom: 300}, 50, 50);
4. roundRect.offset(100, 100);
```
