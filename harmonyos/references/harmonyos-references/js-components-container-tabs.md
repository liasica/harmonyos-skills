---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-tabs
title: tabs
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 容器组件 > tabs
category: harmonyos-references
scraped_at: 2026-04-29T13:53:22+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f33284a0ea864562b8ad07816908ef8cb29c84954a96ee4891d70627e5c51d0b
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

tab页签容器。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

仅支持<[tab-bar](js-components-container-tab-bar.md)>和<[tab-content](js-components-container-tab-content.md)>。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-components-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| index | number | 0 | 否 | 当前处于激活态的tab索引。 |
| vertical | boolean | false | 否 | 是否为纵向的tab，默认为false，可选值为：  - false：tabbar和tabcontent上下排列。  - true：tabbar和tabcontent左右排列。 |

## 样式

PhonePC/2in1TabletTVWearable

支持[通用样式](js-components-common-styles.md)。

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](js-components-common-events.md)外，还支持如下事件：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | { index: indexValue } | tab页签切换后触发，动态修改index值不会触发该回调。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <tabs class = "tabs" index="0" vertical="false" onchange="change">
4. <tab-bar class="tab-bar" mode="fixed">
5. <text class="tab-text">Home</text>
6. <text class="tab-text">Index</text>
7. <text class="tab-text">Detail</text>
8. </tab-bar>
9. <tab-content class="tabcontent" scrollable="true">
10. <div class="item-content" >
11. <text class="item-title">First screen</text>
12. </div>
13. <div class="item-content" >
14. <text class="item-title">Second screen</text>
15. </div>
16. <div class="item-content" >
17. <text class="item-title">Third screen</text>
18. </div>
19. </tab-content>
20. </tabs>
21. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. justify-content: flex-start;
5. align-items: center;
6. }
7. .tabs {
8. width: 100%;
9. }
10. .tabcontent {
11. width: 100%;
12. height: 80%;
13. justify-content: center;
14. }
15. .item-content {
16. height: 100%;
17. justify-content: center;
18. }
19. .item-title {
20. font-size: 60px;
21. }
22. .tab-bar {
23. margin: 10px;
24. height: 60px;
25. border-color: #007dff;
26. border-width: 1px;
27. }
28. .tab-text {
29. width: 300px;
30. text-align: center;
31. }
```

```
1. // xxx.js
2. export default {
3. change: function(e) {
4. console.info("Tab index: " + e.index);
5. },
6. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/dOSDD_1LQGagWdK4rhODaw/zh-cn_image_0000002558607052.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055321Z&HW-CC-Expire=86400&HW-CC-Sign=5E2CC2DBD589F51261D4440ADB663390C7415E505E077D58355DD1AD6C96732A)
