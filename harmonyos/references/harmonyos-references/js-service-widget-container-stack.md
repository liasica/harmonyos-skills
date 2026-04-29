---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-container-stack
title: stack
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > JS服务卡片UI组件 > 容器组件 > stack
category: harmonyos-references
scraped_at: 2026-04-29T13:54:00+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:cca221c953174f3205bd745d7ddc9957648e651786376f02ad93400435bc4a2f
---

堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

说明

从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

支持。

## 属性

PhonePC/2in1TabletTVWearable

支持[通用属性](js-service-widget-common-attributes.md)。

## 样式

PhonePC/2in1TabletTVWearable

支持[通用样式](js-service-widget-common-styles.md)。

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](js-service-widget-common-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <stack class="stack-parent">
3. <div class="back-child bd-radius"></div>
4. <div class="positioned-child bd-radius"></div>
5. <div class="front-child bd-radius"></div>
6. </stack>
```

```
1. /* xxx.css */
2. .stack-parent {
3. width: 400px;
4. height: 400px;
5. margin: 50px;
6. background-color: #ffffff;
7. border-width: 1px;
8. border-style: solid;
9. }
10. .back-child {
11. width: 300px;
12. height: 300px;
13. background-color: #3f56ea;
14. }
15. .front-child {
16. width: 100px;
17. height: 100px;
18. background-color: #00bfc9;
19. }
20. .positioned-child {
21. width: 100px;
22. height: 100px;
23. left: 50px;
24. top: 50px;
25. background-color: #47cc47;
26. }
27. .bd-radius {
28. border-radius: 16px;
29. }
```

**4×4卡片**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/478bNh8xQNyht_pETiRyXw/zh-cn_image_0000002558607292.png?HW-CC-KV=V1&HW-CC-Date=20260429T055359Z&HW-CC-Expire=86400&HW-CC-Sign=F1DC322AE0C89BFC95D81DA3E447FD92F644EEB2DFF91B8AA633A305301CA276)
