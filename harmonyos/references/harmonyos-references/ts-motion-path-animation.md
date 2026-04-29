---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-motion-path-animation
title: 路径动画 (motionPath)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 动画 > 路径动画 (motionPath)
category: harmonyos-references
scraped_at: 2026-04-29T13:52:42+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b22e3fe34605e07a8f04559efbfc0062409c53d25bbd62c52fb8a603ceba920c
---

设置组件进行位移动画时的运动路径。

说明

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## motionPath

PhonePC/2in1TabletTVWearable

motionPath(value: MotionPathOptions): T

设置组件的路径动画。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [MotionPathOptions](ts-motion-path-animation.md#motionpathoptions) | 是 | 设置组件的运动路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## MotionPathOptions

PhonePC/2in1TabletTVWearable

设置组件的运动路径。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| path | string | 否 | 否 | 位移动画的运动路径，使用[svg路径字符串](ts-drawing-components-path.md#svg路径描述规范)。path中支持使用start和end进行起点和终点的替代，如：'Mstart.x start.y L50 50 Lend.x end.y Z'，更多说明请参考[绘制路径](../harmonyos-guides/ui-js-components-svg-path.md)。  设置为空字符串时相当于不设置路径动画。 |
| from | number | 否 | 是 | 运动路径的起点。  默认值：0.0  取值范围：[0.0, 1.0]  设置小于0.0或大于1.0的值时，按默认值0.0处理。 |
| to | number | 否 | 是 | 运动路径的终点。  默认值：1.0  取值范围：[0.0, 1.0]  设置小于0.0或大于1.0的值时，按默认值1.0处理，且满足to值 >= 异常值处理后的from值。 |
| rotatable | boolean | 否 | 是 | 是否跟随路径进行旋转。true代表跟随路径进行旋转，false代表不跟随路径进行旋转。  默认值：false |

## 示例

PhonePC/2in1TabletTVWearable

该示例主要演示如何设置组件进行位移动画时的运动路径。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct MotionPathExample {
5. @State toggle: boolean = true;

7. build() {
8. Column() {
9. Button('click me').margin(50)
10. .motionPath({
11. path: 'Mstart.x start.y L300 200 L300 500 Lend.x end.y',
12. from: 0.0,
13. to: 1.0,
14. rotatable: true
15. }) // 执行动画：从起点移动到(300,200)，再到(300,500)，再到终点
16. .onClick(() => {
17. this.getUIContext()?.animateTo({ duration: 4000, curve: Curve.Linear }, () => {
18. this.toggle = !this.toggle; // 通过this.toggle变化组件的位置
19. });
20. })
21. }.width('100%').height('100%').alignItems(this.toggle ? HorizontalAlign.Start : HorizontalAlign.Center)
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/g2qWye7oSfyBZqDJ-xjr4w/zh-cn_image_0000002589326421.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055241Z&HW-CC-Expire=86400&HW-CC-Sign=AF9B30BC96479C0719F7989BDA6645CF0114AFC40ACA933C99F55984BC53172A)
