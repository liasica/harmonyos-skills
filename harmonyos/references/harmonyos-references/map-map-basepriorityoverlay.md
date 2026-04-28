---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-basepriorityoverlay
title: BasePriorityOverlay
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > BasePriorityOverlay
category: harmonyos-references
scraped_at: 2026-04-28T08:17:12+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:ae94c2dfa78c9a14e5b053ede6931a005ec2a5dd9c9bf92f33bbbefe59c5ac74
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## BasePriorityOverlay

PhonePC/2in1TabletWearable

具有优先级控制的覆盖物基础类，继承[BaseOverlay](map-map-baseoverlay.md)。[PointAnnotation](map-map-pointannotation.md)和[Bubble](map-map-bubble.md)继承该基础类。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

### getMaxZoom

PhonePC/2in1TabletWearable

getMaxZoom(): number

获取覆盖物的最大展示层级。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 覆盖物的最大展示层级。 |

**示例：**

```
1. // 以pointAnnotation为例
2. let pointAnnotationOptions: mapCommon.PointAnnotationParams = {
3. position: {
4. latitude: 32.120750,
5. longitude: 118.788765
6. },
7. titles: [{
8. content: "南京夫子庙"
9. }],
10. // 图标需存放在resources/rawfile目录下
11. icon: 'icon.png'
12. };
13. let pointAnnotation: map.PointAnnotation = await this.mapController.addPointAnnotation(pointAnnotationOptions);
14. let maxZoom: number = pointAnnotation.getMaxZoom();
```

### getMinZoom

PhonePC/2in1TabletWearable

getMinZoom(): number

获取覆盖物的最小展示层级。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 覆盖物的最小展示层级。 |

**示例：**

```
1. // 以pointAnnotation为例
2. let minZoom: number = pointAnnotation.getMinZoom();
```

### setPriority

PhonePC/2in1TabletWearable

setPriority(priority: number): void

设置覆盖物碰撞优先级，值越大优先级越低。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| priority | number | 是 | 设置覆盖物的碰撞优先级。 |

**示例：**

```
1. // 以pointAnnotation为例
2. pointAnnotation.setPriority(100);
```

### setZoom

PhonePC/2in1TabletWearable

setZoom(minZoom: number, maxZoom: number): void

设置覆盖物的显示层级。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| minZoom | number | 是 | 覆盖物的最小显示层级，取值范围：[2, 20]。  传入的值高于20，最小缩放级别会取20。  传入的值小于2，最小缩放级别会取2。  **说明：**  minZoom大于maxZoom，方法不生效。 |
| maxZoom | number | 是 | 覆盖物的最大显示层级，取值范围：[2, 20]。  传入的值高于20，最大缩放级别会取20。  传入的值小于2，最大缩放级别会取2。 |

**示例：**

```
1. // 以pointAnnotation为例
2. pointAnnotation.setZoom(3, 10);
```

### setAnimation

PhonePC/2in1TabletWearable

setAnimation(animation: Animation): void

设置覆盖物的动画。仅支持[AlphaAnimation](map-map-alphaanimation.md)、[ScaleAnimation](map-map-scaleanimation.md)和[AnimationSet](map-map-animationset.md)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| animation | [Animation](map-map-animation.md) | 是 | 动画。 |

**示例：**

```
1. // 创建一个透明度动画，从0.2到1
2. let animation: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
3. // 设置动画持续时间为3000毫秒
4. animation.setDuration(3000);
5. // 定义动画开始时的回调函数
6. let callbackStart = () => {
7. console.info("animationStart", `callback`);
8. };
9. // 定义动画结束时的回调函数
10. let callbackEnd = () => {
11. console.info("animationEnd", `callback`);
12. };
13. // 注册动画开始事件监听器
14. animation.on("animationStart", callbackStart);
15. // 注册动画结束事件监听器
16. animation.on("animationEnd", callbackEnd);
17. // 设置动画填充模式为BACKWARDS，表示动画结束后回到初始状态
18. animation.setFillMode(map.AnimationFillMode.BACKWARDS);
19. // 设置动画重复模式为RESTART，表示每次重复从头开始
20. animation.setRepeatMode(map.AnimationRepeatMode.RESTART);
21. // 设置动画重复次数为100次
22. animation.setRepeatCount(100);
23. // 将动画应用到点注释上
24. pointAnnotation.setAnimation(animation);
```

### startAnimation

PhonePC/2in1TabletWearable

startAnimation(): void

启动覆盖物的动画。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```
1. // 创建一个透明度动画，从0.2到1
2. let animation: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
3. // 设置动画持续时间为3000毫秒
4. animation.setDuration(3000);
5. // 定义动画开始时的回调函数
6. let callbackStart = () => {
7. console.info("animationStart", `callback`);
8. };
9. // 定义动画结束时的回调函数
10. let callbackEnd = () => {
11. console.info("animationEnd", `callback`);
12. };
13. // 注册动画开始事件监听器
14. animation.on("animationStart", callbackStart);
15. // 注册动画结束事件监听器
16. animation.on("animationEnd", callbackEnd);
17. // 设置动画填充模式为BACKWARDS，表示动画结束后回到初始状态
18. animation.setFillMode(map.AnimationFillMode.BACKWARDS);
19. // 设置动画重复模式为RESTART，表示每次重复从头开始
20. animation.setRepeatMode(map.AnimationRepeatMode.RESTART);
21. // 设置动画重复次数为100次
22. animation.setRepeatCount(100);
23. // 将动画应用到点注释上
24. pointAnnotation.setAnimation(animation);
25. // 启动动画
26. pointAnnotation.startAnimation();
```

### clearAnimation

PhonePC/2in1TabletWearable

clearAnimation(): void

清除覆盖物的动画。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```
1. pointAnnotation.clearAnimation();
```
