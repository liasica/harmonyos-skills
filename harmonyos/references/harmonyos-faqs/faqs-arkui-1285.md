---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1285
title: 组件设置maskShape不生效
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 组件设置maskShape不生效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:75084596e4eab7775e404c976afa51fea6f8e64aeb0ff6ca33e5d5f426426a8d
---

## 问题现象

设置组件的maskShape属性后，组件遮罩未生效且组件本身消失，注释该属性后组件恢复正常显示。

问题代码示例参考如下：

```screen
@Entry
@Component
struct Index {
  maskSize: string | number = 180

  build() {
    Column() {
      Circle()
        .width(200)
        .height(200)
        .fill('#0D5AF5')
        .maskShape(new CircleShape({ width: this.maskSize, height: this.maskSize }).fill('#00000000'))
    }
    .width(300)
    .height(300)
  }
}
```

注释maskShape属性前后效果图对比：

注释前：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/S0ApbEAcQB2w24vd1X7YKg/zh-cn_image_0000002658957193.png "点击放大")

注释后：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/KEIj9aCrTyexiVeTPLPTOw/zh-cn_image_0000002658837241.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/LBO4B4mIRzC0Fbr4prR_UQ/zh-cn_image_0000002628597976.png "点击放大")

## 背景知识

* 通用属性[maskShape](../harmonyos-references/ts-universal-attributes-sharp-clipping.md#maskshape12)是用于为组件添加指定形状的遮罩，遮罩后，组件显示为遮罩的形状（即若指定圆形遮罩，则组件最终显示为圆形），遮罩形状从组件的左上角开始绘制。
* 在指定遮罩形状时可以通过[fill](../harmonyos-references/ts-drawing-components-circle.md#fill)属性填充形状颜色，使遮罩后的组件呈现不同的透明度；当填充的颜色为黑色（Color.Black或000000）、透明（Color.Transparent）或透明度为00（16进制颜色00XXXXXX）的颜色时，会将组件完全遮罩，组件不显示。

## 问题定位

1. 排查maskShape是否设置了黑色、透明色或透明度为00的颜色；
2. 确认组件在遮罩后的位置有可显示的内容。

## 分析结论

问题代码中，组件Circle设置的遮罩层形状CircleShape填充了颜色#00000000，即透明度为00的黑色，导致组件被完全遮罩，不显示。

## 修改建议

调整maskShape形状的填充颜色，不设置为黑色、透明色或透明度为00的颜色。

```screen
import { CircleShape } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  maskSize: string | number = 180;

  build() {
    Column() {
      Circle()
        .width(200)
        .height(200)
        .fill('#0D5AF5')
        .maskShape(new CircleShape().width(this.maskSize).height(this.maskSize).fill('#0000FF'))
    }
    .width(300)
    .height(300)
  }
}
```
