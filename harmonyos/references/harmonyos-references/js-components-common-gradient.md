---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-gradient
title: 渐变样式
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 组件通用信息 > 渐变样式
category: harmonyos-references
scraped_at: 2026-11-21T09:14:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bafdfa0c6dedeb0740b10a721a4345ef7abe265132d0cff6a4a960919923b96d
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/dTWWfHx1RX6oIC93hfN4Kw/zh-cn_image_0000002792879476.png?HW-CC-KV=V1&HW-CC-Date=20261121T011318Z&HW-CC-Expire=31536000000&HW-CC-Sign=8695E89CE9F14C361C48057F52C5D7727C9C074CFCAFC1D87FE0AC6117DE440A)
2. 45度夹角渐变。

   ```css
   /* 45度夹角，从红色渐变到绿色 */
   background: linear-gradient(45deg, rgb(255,0,0),rgb(0, 255, 0));
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/f0SCFcOYTByXiVSFP3qTsg/zh-cn_image_0000002821839381.png?HW-CC-KV=V1&HW-CC-Date=20261121T011318Z&HW-CC-Expire=31536000000&HW-CC-Sign=6DA3F4CCD5976FD5140987FCB089DBA35E278EA4DBC3254A637125E9D7FD2659)
3. 设置方向从左向右渐变。

   ```css
   /* 从左向右渐变，在距离左边90px和距离左边360px (600*0.6) 之间270px宽度形成渐变 */
   background: linear-gradient(to right, rgb(255,0,0) 90px, rgb(0, 255, 0) 60%);
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/4jK01PD8SJe8k_Y0oF_6Rg/zh-cn_image_0000002821759379.png?HW-CC-KV=V1&HW-CC-Date=20261121T011318Z&HW-CC-Expire=31536000000&HW-CC-Sign=4156FD380BE6C38CD363B82BFE3655981477C06F13964A93AA86EF0EA3F56604)
4. 重复渐变。

   ```css
   /* 从左向右重复渐变，重复渐变区域30px（60-30）透明度0.5 */
   background: repeating-linear-gradient(to right, rgba(255, 255, 0, 1) 30px,rgba(0, 0, 255, .5) 60px);
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/JgQ7jFGASTCAK44iaaK5yQ/zh-cn_image_0000002793039452.png?HW-CC-KV=V1&HW-CC-Date=20261121T011318Z&HW-CC-Expire=31536000000&HW-CC-Sign=68319AF5CEE880BC3B4C9FF23392196E03D789AA58C259370CF24CC03EFD7230)
