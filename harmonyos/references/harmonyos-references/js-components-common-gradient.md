---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-gradient
title: 渐变样式
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 组件通用信息 > 渐变样式
category: harmonyos-references
scraped_at: 2026-04-28T08:02:53+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:7499978669167d36e6aaa655b9127f4c6c44904abf948b9dc372ee5051438770
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

组件普遍支持在style或css中设置可以平滑过渡两个或多个指定的颜色。

开发框架支持线性渐变（linear-gradient）和重复线性渐变（repeating-linear-gradient）两种渐变效果。

## 线性渐变/重复线性渐变

PhonePC/2in1TabletTVWearable

使用渐变样式，需要定义过渡方向和过渡颜色。

### 过渡方向

PhonePC/2in1TabletTVWearable

通过direction或者angle指定过渡方向。

* direction：指定方向进行渐变。
* angle：指定角度进行渐变。

```
1. // xxx.js
2. background: linear-gradient(direction/angle, color, color, ...);
3. background: repeating-linear-gradient(direction/angle, color, color, ...);
```

### 过渡颜色

PhonePC/2in1TabletTVWearable

支持以下四种方式：#ff0000、#ffff0000、rgb(255, 0, 0)、rgba(255, 0, 0, 1)，需要指定至少两种颜色。

**参数：**

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| direction | to <side-or-corner> <side-or-corner> = [left | right] | [top | bottom] | to bottom (由上到下渐变) | 否 | 指定过渡方向，如：to left (从右向左渐变) ；或者  to bottom right (从左上角到右下角)。 |
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/CkKiTTMTSfiRPzEJYir5Cw/zh-cn_image_0000002552800524.png?HW-CC-KV=V1&HW-CC-Date=20260428T000252Z&HW-CC-Expire=86400&HW-CC-Sign=535F4F1B59DA5B7897D3782A5360EE156C2472220705872A51542F69A56E9DCC)
2. 45度夹角渐变。

   ```
   1. /* 45度夹角，从红色渐变到绿色 */
   2. background: linear-gradient(45deg, rgb(255,0,0),rgb(0, 255, 0));
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/UQ-kJcw3RWiGBZbZ1LnoVg/zh-cn_image_0000002583440219.png?HW-CC-KV=V1&HW-CC-Date=20260428T000252Z&HW-CC-Expire=86400&HW-CC-Sign=689289B30C28648740AF415553B3315D13F91502C8F73837E58E9E03491B9C02)
3. 设置方向从左向右渐变。

   ```
   1. /* 从左向右渐变，在距离左边90px和距离左边360px (600*0.6) 之间270px宽度形成渐变 */
   2. background: linear-gradient(to right, rgb(255,0,0) 90px, rgb(0, 255, 0) 60%);
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/zLfRzyWeTNerc_cQ5OP9hw/zh-cn_image_0000002552960174.png?HW-CC-KV=V1&HW-CC-Date=20260428T000252Z&HW-CC-Expire=86400&HW-CC-Sign=8E5495CDDAF9ECBECA3746B9C4BD5DDCCEEE3E61C9363F9E277395EB4B503D2A)
4. 重复渐变。

   ```
   1. /* 从左向右重复渐变，重复渐变区域30px（60-30）透明度0.5 */
   2. background: repeating-linear-gradient(to right, rgba(255, 255, 0, 1) 30px,rgba(0, 0, 255, .5) 60px);
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/uzy6DZZDRZeZlsn2bo3EQA/zh-cn_image_0000002583480175.png?HW-CC-KV=V1&HW-CC-Date=20260428T000252Z&HW-CC-Expire=86400&HW-CC-Sign=DB1CF01A52B1C9874ABF70AF9DC3BDA3680A2CB2C9E005AA14451D90FF8867E9)
