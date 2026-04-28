---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-container-swiper
title: swiper
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > JS服务卡片UI组件 > 容器组件 > swiper
category: harmonyos-references
scraped_at: 2026-04-28T08:03:38+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:de8c1567306df638bba7f3326d9aa3fa70866f21c2c6e90339d2a1e77c2d39e5
---

滑动容器，提供切换子组件显示的能力。

说明

从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-service-widget-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| index | number | 0 | 否 | 当前在容器中显示的子组件的索引值。 |
| indicator | boolean | true | 否 | 是否启用导航点指示器，默认true。true为启用导航点指示器，false为不启用。 |
| digital | boolean | false | 否 | 是否启用数字导航点，默认为false。true为启用数字导航点，false为不启用。  必须设置indicator时才能生效数字导航点。 |
| loop | boolean | true | 否 | 是否开启循环滑动。true为开启循环，false为关闭循环。 |
| duration | number | 0 | 否 | 子组件切换的动画时长。  单位：毫秒  取值范围：[0, +∞) |
| vertical | boolean | false | 否 | 是否为纵向滑动。true为纵向滑动，false为水平滑动。纵向滑动时采用纵向的指示器。 |

## 样式

PhonePC/2in1TabletTVWearable

除支持[通用样式](js-service-widget-common-styles.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| indicator-color | <color> | - | 否 | 导航点指示器的填充颜色。 |
| indicator-selected-color | <color> | - | 否 | 导航点指示器选中的颜色。 |
| indicator-size | <length> | 4px | 否 | 导航点指示器的直径大小。 |
| indicator-top|left|right|bottom | <length> | <percentage> | - | 否 | 导航点指示器在swiper中的相对位置。 |

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](js-service-widget-common-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <swiper class="container" index="{{index}}">
3. <div class="swiper-item primary-item">
4. <text>1</text>
5. </div>
6. <div class="swiper-item warning-item">
7. <text>2</text>
8. </div>
9. <div class="swiper-item success-item">
10. <text>3</text>
11. </div>
12. </swiper>
```

```
1. /* xxx.css */
2. .container {
3. left: 0px;
4. top: 0px;
5. width: 454px;
6. height: 454px;
7. }
8. .swiper-item {
9. width: 454px;
10. height: 454px;
11. justify-content: center;
12. align-items: center;
13. }
14. .primary-item {
15. background-color: #007dff;
16. }
17. .warning-item {
18. background-color: #ff7500;
19. }
20. .success-item {
21. background-color: #41ba41;
22. }
```

```
1. {
2. "data": {
3. "index": 1
4. }
5. }
```

**4×4卡片**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/A35HhgndToCNyQbH6FqxIw/zh-cn_image_0000002583480427.png?HW-CC-KV=V1&HW-CC-Date=20260428T000336Z&HW-CC-Expire=86400&HW-CC-Sign=C0A91C0C210ECCDB061CF39C10C12EB401CD128C884C2F334C2181D6AA48F8F9)
