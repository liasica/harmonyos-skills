---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-gradient
title: 渐变样式
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > JS服务卡片UI组件 > 组件通用信息 > 渐变样式
category: harmonyos-references
scraped_at: 2026-04-29T13:53:57+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e439a7468cee3181f6e2c523c8f859edd5fdfb2221f6f8c417d83e5472557e9c
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/w3aZV432SHGbST-0C0KdWA/zh-cn_image_0000002558607288.png?HW-CC-KV=V1&HW-CC-Date=20260429T055356Z&HW-CC-Expire=86400&HW-CC-Sign=C821484C7971DB813B700E1B8F47FDFCE7FE4AF2BAF70154445A7308B0ADEA06)
2. 45度夹角渐变。

   ```
   1. /* 45度夹角，从红色渐变到绿色 */
   2. background: linear-gradient(45deg, rgb(255, 0, 0),rgb(0, 255, 0));
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/IA2jpVGdQH-FW6RkdaCCQQ/zh-cn_image_0000002589326817.png?HW-CC-KV=V1&HW-CC-Date=20260429T055356Z&HW-CC-Expire=86400&HW-CC-Sign=D45D09D227224B9115810BE8B8A695246515B73A47239928B0C438A52C9AF291)
3. 设置方向从左向右渐变。

   ```
   1. /* 从左向右渐变，在距离左边90px和距离左边360px (600*0.6) 之间270px宽度形成渐变 */
   2. background: linear-gradient(to right, rgb(255, 0, 0) 90px, rgb(0, 255, 0) 60%);
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/kDOwjDuRThq0daq5bvdgpA/zh-cn_image_0000002589246757.png?HW-CC-KV=V1&HW-CC-Date=20260429T055356Z&HW-CC-Expire=86400&HW-CC-Sign=8A5BD5B217B4F74F176C91D6EA89C0525CD93BF3BD828C8110137F5793B6254A)
4. 重复渐变。

   ```
   1. /* 从左向右重复渐变，重复渐变区域30px（60-30）透明度0.5 */
   2. background: repeating-linear-gradient(to right, rgba(255, 255, 0, 1) 30vp,rgba(0, 0, 255, .5) 60vp);
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/oGzFTfBWTxGMDuJJukkjPw/zh-cn_image_0000002558766950.png?HW-CC-KV=V1&HW-CC-Date=20260429T055356Z&HW-CC-Expire=86400&HW-CC-Sign=F514E2C8FCC9AD7EB4953A0D9925438170C710C75C1A7F3613490FC6E6D0E734)
