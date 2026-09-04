---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-gradient
title: 渐变样式
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 组件通用信息 > 渐变样式
category: harmonyos-references
scraped_at: 2026-09-05T06:17:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:298978d7bc5aeb0c8c1058b0622d5f1c04c50742dd62917f83c575c97ba90a39
---

**说明** 

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

组件普遍支持在style或css中设置可以平滑过渡两个或多个指定的颜色。

开发框架支持线性渐变（linear-gradient）和重复线性渐变（repeating-linear-gradient）两种渐变效果。

## 线性渐变/重复线性渐变

使用渐变样式，需要定义过渡方向和过渡颜色。

### 过渡方向

通过direction或者angle指定过渡方向。

* direction：指定方向进行渐变。
* angle：指定角度进行渐变。

```js
// xxx.js
background: linear-gradient(direction/angle, color, color, ...);
background: repeating-linear-gradient(direction/angle, color, color, ...);
```

### 过渡颜色

支持以下四种方式：#ff0000、#ffff0000、rgb(255, 0, 0)、rgba(255, 0, 0, 1)，需要指定至少两种颜色。

**参数：**

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| direction | to <side-or-corner> <side-or-corner> = [left | right] | [top | bottom] | to bottom (由上到下渐变) | 否 | 指定过渡方向，如：to left (从右向左渐变) ；或者  to bottom right (从左上角到右下角)。 |
| angle | <deg> | 180deg | 否 | 指定过渡方向，以元素几何中心为坐标原点，水平方向为X轴，angle指定了渐变线与Y轴的夹角（顺时针方向）。 |
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/a2u85vEUQMuLwo31h2Cy2g/zh-cn_image_0000002712246674.png)
2. 45度夹角渐变。

   ```css
   /* 45度夹角，从红色渐变到绿色 */
   background: linear-gradient(45deg, rgb(255,0,0),rgb(0, 255, 0));
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/MWzkLdWvT2unHyta_yjH6A/zh-cn_image_0000002742005623.png)
3. 设置方向从左向右渐变。

   ```css
   /* 从左向右渐变，在距离左边90px和距离左边360px (600*0.6) 之间270px宽度形成渐变 */
   background: linear-gradient(to right, rgb(255,0,0) 90px, rgb(0, 255, 0) 60%);
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/oUIl-AIQQY-A0NbYwIY8uQ/zh-cn_image_0000002712406636.png)
4. 重复渐变。

   ```css
   /* 从左向右重复渐变，重复渐变区域30px（60-30）透明度0.5 */
   background: repeating-linear-gradient(to right, rgba(255, 255, 0, 1) 30px,rgba(0, 0, 255, .5) 60px);
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/2vsrfpPUQceX6vRSJu7InQ/zh-cn_image_0000002742125583.png)
