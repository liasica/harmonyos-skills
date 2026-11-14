---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-gradient
title: 渐变样式
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 组件通用信息 > 渐变样式
category: harmonyos-references
scraped_at: 2026-11-14T08:50:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ffca42d6d13c67d29d3d5fd24c2db3a20080359e2f0dcacfcad5d1d61f7b9157
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/1J2VRw_DTTynWe0NJxOCdg/zh-cn_image_0000002817428829.png?HW-CC-KV=V1&HW-CC-Date=20261114T005029Z&HW-CC-Expire=31536000000&HW-CC-Sign=C26577C961A2FFE877BE4033A6CAD3783F19901AC8BFE6C5B1AC0D889F31500F)
2. 45度夹角渐变。

   ```css
   /* 45度夹角，从红色渐变到绿色 */
   background: linear-gradient(45deg, rgb(255,0,0),rgb(0, 255, 0));
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/9__XosZBRnWbIAqkO6h-qA/zh-cn_image_0000002788469410.png?HW-CC-KV=V1&HW-CC-Date=20261114T005029Z&HW-CC-Expire=31536000000&HW-CC-Sign=1F7F493EF78359E411C7C4262B5484FA96DE51DAA6FEDFF0231839C71105799A)
3. 设置方向从左向右渐变。

   ```css
   /* 从左向右渐变，在距离左边90px和距离左边360px (600*0.6) 之间270px宽度形成渐变 */
   background: linear-gradient(to right, rgb(255,0,0) 90px, rgb(0, 255, 0) 60%);
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/1F8PTvJrS4mSaCn9HPMVrw/zh-cn_image_0000002817508899.png?HW-CC-KV=V1&HW-CC-Date=20261114T005029Z&HW-CC-Expire=31536000000&HW-CC-Sign=BABE63FD853BE1B02E197770E19DC8032016AC1FE848CB10807ED851EB5E3136)
4. 重复渐变。

   ```css
   /* 从左向右重复渐变，重复渐变区域30px（60-30）透明度0.5 */
   background: repeating-linear-gradient(to right, rgba(255, 255, 0, 1) 30px,rgba(0, 0, 255, .5) 60px);
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/6Zm2emQRQBqCGYon3xNawg/zh-cn_image_0000002788309468.png?HW-CC-KV=V1&HW-CC-Date=20261114T005029Z&HW-CC-Expire=31536000000&HW-CC-Sign=FE2CC0E94A4BF6A35F35C03E0F689A491FE368F2BD96E069555069D8C7DC55E0)
