---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-tool
title: Class (Tool)
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.drawing (绘制模块) > Class (Tool)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:766a8093ae4a889f23391a1880999125116bf4a690c2ab3983d461e266c299ce
---

本模块定义的工具类，仅提供静态的方法，主要完成其他模块和[common2D](js-apis-graphics-common2d.md)中定义的数据结构的转换功能等操作。

说明

* 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 15开始支持。
* 本模块使用屏幕物理像素单位px。
* 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { drawing } from '@kit.ArkGraphics2D';
```

## makeColorFromResourceColor15+

PhonePC/2in1TabletTVWearable

static makeColorFromResourceColor(resourceColor: ResourceColor): common2D.Color

将ResourceColor类型的值转换为common2D.Color对象。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourceColor | [ResourceColor](ts-types.md#resourcecolor) | 是 | ResourceColor格式的颜色值（支持所有的4种输入，示例中提供13个示例输入）。其中第4种类型[Resource](ts-types.md#resource)只接受$r('belonging.type.name')构造方法，需要确保该资源在main/resources/base/element目录下已定义(app支持color、string和integer，sys只支持color)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [common2D.Color](js-apis-graphics-common2d.md#color) | 转换后的common2D.Color颜色对象，若转换失败则返回空指针。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { drawing, common2D } from '@kit.ArkGraphics2D';

3. // Color
4. let color1: common2D.Color = drawing.Tool.makeColorFromResourceColor(Color.Blue);

6. // Number
7. let color2: common2D.Color = drawing.Tool.makeColorFromResourceColor(0xffc0cb);
8. let color3: common2D.Color = drawing.Tool.makeColorFromResourceColor(0x11ffa500);

10. // String
11. let color4: common2D.Color = drawing.Tool.makeColorFromResourceColor('#ff0000');
12. let color5: common2D.Color = drawing.Tool.makeColorFromResourceColor('#110000ff');
13. let color6: common2D.Color = drawing.Tool.makeColorFromResourceColor('#00f');
14. let color7: common2D.Color = drawing.Tool.makeColorFromResourceColor('#100f');
15. let color8: common2D.Color = drawing.Tool.makeColorFromResourceColor('rgb(255, 100, 255)');
16. let color9: common2D.Color = drawing.Tool.makeColorFromResourceColor('rgba(255, 100, 255, 0.5)');

18. // Resource
19. let color10: common2D.Color = drawing.Tool.makeColorFromResourceColor($r('sys.color.ohos_id_color_secondary'));

21. // Use color
22. let brush = new drawing.Brush();
23. brush.setColor(color1);
```
