---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-pointannotation
title: PointAnnotation
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > PointAnnotation
category: harmonyos-references
scraped_at: 2026-04-28T08:17:12+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:a5b4f32212fd859350ff20a8f72b8dd3e894eb4a05e7f131ca1879948bf609a4
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## PointAnnotation

PhonePC/2in1TabletWearable

点注释，继承[BasePriorityOverlay](map-map-basepriorityoverlay.md)。在调用map.[MapComponentController](map-map-mapcomponentcontroller.md)类的[addPointAnnotation](map-map-mapcomponentcontroller.md#addpointannotation)方法时会返回该类型的实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```
1. let pointAnnotationOptions: mapCommon.PointAnnotationParams = {
2. position: {
3. latitude: 32.120750,
4. longitude: 118.788765
5. },
6. titles: [{
7. content: "南京夫子庙"
8. }],
9. // 图标需存放在resources/rawfile目录下
10. icon: 'icon.png'
11. };
12. let pointAnnotation: map.PointAnnotation = await this.mapController.addPointAnnotation(pointAnnotationOptions);
```

### getPosition

PhonePC/2in1TabletWearable

getPosition(): mapCommon.LatLng

获取点注释的锚点坐标。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.LatLng](map-common.md#latlng) | 点注释的锚点坐标。 |

**示例：**

```
1. let position: mapCommon.LatLng = pointAnnotation.getPosition();
```

### getTitleText

PhonePC/2in1TabletWearable

getTitleText(): mapCommon.Text

获取点注释第一标题的属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.Text](map-common.md#text) | 获取点注释第一标题的属性。 |

**示例：**

```
1. let titleText: mapCommon.Text = pointAnnotation.getTitleText();
```

### setTitleText

PhonePC/2in1TabletWearable

setTitleText(text: mapCommon.Text): void

设置第一标题属性（除content）。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| text | [mapCommon.Text](map-common.md#text) | 是 | 第一标题属性（除content），异常值不处理。  **说明：**  约束条件：fontSize、strokeWidth大于等于0。 |

**示例：**

```
1. // 以pointAnnotation为例
2. pointAnnotation.setTitleText({
3. content: '',
4. color: 0xff00ffff,
5. fontSize: 15,
6. strokeColor: 0xff00ff00,
7. strokeWidth: 2,
8. fontStyle: mapCommon.FontStyle.BOLD_ITALIC
9. });
```

### setTitleAnimation

PhonePC/2in1TabletWearable

setTitleAnimation(animation: FontSizeAnimation): void

设置点注释的标题动画。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| animation | [FontSizeAnimation](map-map-fontsizeanimation.md) | 是 | 点注释的标题动画。 |

**示例：**

```
1. let animation: map.FontSizeAnimation = new map.FontSizeAnimation(5, 25);
2. animation.setDuration(3000);
3. animation.on("start",() => {
4. console.info('start Font Animation');
5. });
6. animation.on("end",() => {
7. console.info('end Font Animation');
8. });
9. // 设置动画完成的状态
10. animation.setFillMode(map.AnimationFillMode.BACKWARDS);
11. // 设置动画重复方式
12. animation.setRepeatMode(map.AnimationRepeatMode.REVERSE);
13. // 设置动画的插值器
14. animation.setInterpolator(Curve.Linear);
15. // 设置动画重复的次数
16. animation.setRepeatCount(100);
17. pointAnnotation.setTitleAnimation(animation);
18. pointAnnotation.startTitleAnimation();
```

### startTitleAnimation

PhonePC/2in1TabletWearable

startTitleAnimation(): void

启动点注释的标题动画。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```
1. pointAnnotation.startTitleAnimation();
```
