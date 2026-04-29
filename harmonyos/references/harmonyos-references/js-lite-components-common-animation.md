---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-common-animation
title: 动画样式
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 组件通用信息 > 动画样式
category: harmonyos-references
scraped_at: 2026-04-29T13:53:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f2232ea1a7aeecb690058123515cb3a65fa7e8e94b3b4f85b018873d1ba16d7d
---

组件支持通过style或css设置动态的旋转、平移及缩放效果。

| 名称 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| transform | string | - | 详见表1。 |
| animation-name | string | - | 指定@keyframes，详见表2。 |
| animation-delay | <time> | 0 | 定义动画播放的延迟时间。支持的单位为[s(秒)|ms(毫秒) ]，默认单位为ms，格式为：1000ms或1s。 |
| animation-duration | <time> | 0 | 定义一个动画周期。支持的单位为[s(秒)|ms(毫秒) ]，默认单位为ms，格式为：1000ms或1s。  **说明：**  animation-duration 样式必须设置，否则时长为 0，则不会播放动画。 |
| animation-iteration-count | number | infinite | 1 | 定义动画播放的次数，默认播放一次，可通过设置为infinite无限次播放。 |
| animation-timing-function | string | linear | 描述动画执行的速度曲线，用于使动画更为平滑。  可选项有：  - linear：表示动画从头到尾的速度都是相同的。  - ease-in：表示动画以低速开始，cubic-bezier(0.42, 0.0, 1.0, 1.0)。  - ease-out：表示动画以低速结束，cubic-bezier(0.0, 0.0, 0.58, 1.0)。  - ease-in-out：表示动画以低速开始和结束，cubic-bezier(0.42, 0.0, 0.58, 1.0)。 |
| animation-fill-mode | string | none | 指定动画开始和结束的状态：  - none：在动画执行之前和之后都不会应用任何样式到目标上。  - forwards：在动画结束后，目标将保留动画结束时的状态（在最后一个关键帧中定义）。 |

**表1** transform操作说明

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| translateX | <length> | X轴方向平移动画属性 |
| translateY | <length> | Y轴方向平移动画属性 |
| rotate | <deg> | <rad> | 旋转动画属性 |

说明

轻量级智能穿戴仅支持原始大小的图片进行旋转。

**表2** @keyframes属性说明

| 名称 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| background-color | <color> | - | 动画执行后应用到组件上的背景颜色。 |
| width | <length> | - | 动画执行后应用到组件上的宽度值。 |
| height | <length> | - | 动画执行后应用到组件上的高度值。 |
| transform | string | - | 定义应用在组件上的变换类型，见表1。 |

对于不支持起始值或终止值缺省的情况，可以通过from和to显式指定起始和结束。示例：

```
1. @keyframes Go
2. {
3. from {
4. background-color: #f76160;
5. }
6. to {
7. background-color: #09ba07;
8. }
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/SBesjR5GTjKfXNzijBMjmA/zh-cn_image_0000002558607270.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055344Z&HW-CC-Expire=86400&HW-CC-Sign=BC0830B33BAFEC96B2B49C69E93D9ECCE169410173753CC7AB0580512CD3876E)

说明

@keyframes的from/to不支持动态绑定。
