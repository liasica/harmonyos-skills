---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-gradient
title: 渐变样式
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > JS服务卡片UI组件 > 组件通用信息 > 渐变样式
category: harmonyos-references
scraped_at: 2026-04-28T08:03:35+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:fc682e32f8ed3e326518d611c2778d69681b29f675626483f5256d39e1f8bf7c
---

组件普遍支持在style或css中设置渐变样式，可以平稳过渡两个或多个指定的颜色。

说明

从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

开发框架支持线性渐变 (linear-gradient)和重复线性渐变 (repeating-linear-gradient)两种渐变效果。

## 线性渐变/重复线性渐变

PhonePC/2in1TabletTVWearable

使用渐变样式，需要定义过渡方向和过渡颜色。

### 过渡方向

PhonePC/2in1TabletTVWearable

通过direction或者angle指定过渡方向。

* direction：进行方向渐变。
* angle：进行角度渐变。

```
1. background: linear-gradient(direction/angle, color, color, ...);
2. background: repeating-linear-gradient(direction/angle, color, color, ...);
```

### 过渡颜色

PhonePC/2in1TabletTVWearable

支持以下四种方式：#ff0000、#ffff0000、rgb(255, 0, 0)、rgba(255, 0, 0, 1)，需要指定至少两种颜色。

**参数：**

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| direction | to <side-or-corner> <side-or-corner> = [left | right] || [top | bottom] | to bottom (由上到下渐变) | 否 | 指定过渡方向，如：to left (从右向左渐变) ，或者to bottom right (从左上角到右下角)。 |
| angle | <deg> | 180deg | 否 | 指定过渡方向，以元素几何中心为坐标原点，水平方向为X轴，angle指定了渐变线与Y轴的夹角(顺时针方向)。 |
| color | <color> [<length>|<percentage>] | - | 是 | 定义使用渐变样式区域内颜色的渐变效果。 |

**示例：**

1. 默认渐变方向为从上向下渐变。

   ```
   1. #gradient {
   2. height: 300px;
   3. width: 600px;
   4. /* 从顶部开始向底部由红色向绿色渐变 */
   5. background: linear-gradient(red, #00ff00);
   6. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/W4lbs_XzT8iuhPM_4bhzFA/zh-cn_image_0000002552960422.png?HW-CC-KV=V1&HW-CC-Date=20260428T000334Z&HW-CC-Expire=86400&HW-CC-Sign=1DDA9F8BEE19A667F2F10E05CA1ECA8AA42BE271ECD6BBC2EE2FD12E06B03A89)
2. 45度夹角渐变。

   ```
   1. /* 45度夹角，从红色渐变到绿色 */
   2. background: linear-gradient(45deg, rgb(255, 0, 0),rgb(0, 255, 0));
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/QlKG1-84TOaHpxI1ZqTI2g/zh-cn_image_0000002583480423.png?HW-CC-KV=V1&HW-CC-Date=20260428T000334Z&HW-CC-Expire=86400&HW-CC-Sign=BA7BB1B8C85086C354C738288781380EEED3ED76BDA644B7021E26961B3110AA)
3. 设置方向从左向右渐变。

   ```
   1. /* 从左向右渐变，在距离左边90px和距离左边360px (600*0.6) 之间270px宽度形成渐变 */
   2. background: linear-gradient(to right, rgb(255, 0, 0) 90px, rgb(0, 255, 0) 60%);
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/W1JCbVeGQzmt_LcdL5AMTA/zh-cn_image_0000002552800774.png?HW-CC-KV=V1&HW-CC-Date=20260428T000334Z&HW-CC-Expire=86400&HW-CC-Sign=9965EFBF5672FB15B0320078EA8406EC343315973B0367E558121E176EE847E9)
4. 重复渐变。

   ```
   1. /* 从左向右重复渐变，重复渐变区域30px（60-30）透明度0.5 */
   2. background: repeating-linear-gradient(to right, rgba(255, 255, 0, 1) 30vp,rgba(0, 0, 255, .5) 60vp);
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/A15qHVAyRZGSZyWnlAtyNg/zh-cn_image_0000002583440469.png?HW-CC-KV=V1&HW-CC-Date=20260428T000334Z&HW-CC-Expire=86400&HW-CC-Sign=2D7C51818EAC8EBF466A93C5212653305943A3314BF7483D42EC382C267185F7)
