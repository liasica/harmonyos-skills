---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-gradient
title: 渐变样式
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > JS服务卡片UI组件 > 组件通用信息 > 渐变样式
category: harmonyos-references
scraped_at: 2026-11-19T09:51:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f05f009dc54b62df0030e94617e4e4565a7250a50d88d34fcf9bace27fdec58c
---

组件普遍支持在style或css中设置渐变样式，可以平稳过渡两个或多个指定的颜色。

**说明** 

从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

开发框架支持线性渐变 (linear-gradient)和重复线性渐变 (repeating-linear-gradient)两种渐变效果。

## 线性渐变/重复线性渐变

使用渐变样式，需要定义过渡方向和过渡颜色。

### 过渡方向

通过direction或者angle指定过渡方向。

* direction：进行方向渐变。
* angle：进行角度渐变。

```css
background: linear-gradient(direction/angle, color, color, ...);
background: repeating-linear-gradient(direction/angle, color, color, ...);
```

### 过渡颜色

支持以下四种方式：#ff0000、#ffff0000、rgb(255, 0, 0)、rgba(255, 0, 0, 1)，需要指定至少两种颜色。

**参数：**

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| direction | to <side-or-corner> <side-or-corner> = [left | right] || [top | bottom] | to bottom (由上到下渐变) | 否 | 指定过渡方向，如：to left (从右向左渐变) ，或者to bottom right (从左上角到右下角)。 |
| angle | <deg> | 180deg | 否 | 指定过渡方向，以元素几何中心为坐标原点，水平方向为X轴，angle指定了渐变线与Y轴的夹角(顺时针方向)。 |
| color | <color> [<length>|<percentage>] | - | 是 | 定义使用渐变样式区域内颜色的渐变效果。 |

**示例：**

1. 默认渐变方向为从上向下渐变。

   ```css
   #gradient {
     height: 300px;
     width: 600px;
     /* 从顶部开始向底部由红色向绿色渐变 */
     background: linear-gradient(red, #00ff00);
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/Y1igP4YHQS6izaTbdXANQQ/zh-cn_image_0000002820527997.png?HW-CC-KV=V1&HW-CC-Date=20261119T015030Z&HW-CC-Expire=31536000000&HW-CC-Sign=DAC00B3064DAEBD006241F65C69D955022888CA6A15E23E303EAD84939851E88)
2. 45度夹角渐变。

   ```css
   /* 45度夹角，从红色渐变到绿色 */
   background: linear-gradient(45deg, rgb(255, 0, 0),rgb(0, 255, 0));
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/G5ok6qH9TOSYr9CsPy0amw/zh-cn_image_0000002820407999.png?HW-CC-KV=V1&HW-CC-Date=20261119T015030Z&HW-CC-Expire=31536000000&HW-CC-Sign=EB96A640970917FB36CE3D8E6B620128C770B683653567122D98FB8FB9589CB3)
3. 设置方向从左向右渐变。

   ```css
   /* 从左向右渐变，在距离左边90px和距离左边360px (600*0.6) 之间270px宽度形成渐变 */
   background: linear-gradient(to right, rgb(255, 0, 0) 90px, rgb(0, 255, 0) 60%);
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/nD4KXseqTRWfsDuyV4ybzQ/zh-cn_image_0000002791728018.png?HW-CC-KV=V1&HW-CC-Date=20261119T015030Z&HW-CC-Expire=31536000000&HW-CC-Sign=6626D9F9500661370EF2C3DEDC501F25B68CBC990D2DFE08C918410CC289B1A9)
4. 重复渐变。

   ```css
   /* 从左向右重复渐变，重复渐变区域30vp（60-30）透明度0.5 */
   background: repeating-linear-gradient(to right, rgba(255, 255, 0, 1) 30vp,rgba(0, 0, 255, .5) 60vp);
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/ReAFm-o4TVilwVhcvVaFNQ/zh-cn_image_0000002791568046.png?HW-CC-KV=V1&HW-CC-Date=20261119T015030Z&HW-CC-Expire=31536000000&HW-CC-Sign=1F175F6B76590324765E6713E89EE6E54F8D12E7ADBDB1D8EE65ED26F83B85C9)
