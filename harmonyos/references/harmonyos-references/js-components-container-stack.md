---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-stack
title: stack
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 容器组件 > stack
category: harmonyos-references
scraped_at: 2026-04-29T13:53:20+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:08e95a2ed4027167d8844de35cd71eec66dda0bfcf50b7072b84dbcaf1399b01
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

支持。

## 属性

PhonePC/2in1TabletTVWearable

支持[通用属性](js-components-common-attributes.md)。

## 样式

PhonePC/2in1TabletTVWearable

支持[通用样式](js-components-common-styles.md)。

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](js-components-common-events.md)。

## 方法

PhonePC/2in1TabletTVWearable

支持[通用方法](js-components-common-methods.md)。

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
5. background-color: #ffffff;
6. border-width: 1px;
7. border-style: solid;
8. }
9. .back-child {
10. width: 300px;
11. height: 300px;
12. background-color: #3f56ea;
13. }
14. .front-child {
15. width: 100px;
16. height: 100px;
17. background-color: #00bfc9;
18. }
19. .positioned-child {
20. width: 100px;
21. height: 100px;
22. left: 50px;
23. top: 50px;
24. background-color: #47cc47;
25. }
26. .bd-radius {
27. border-radius: 16px;
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/ehdjQuNgQ1i0HxmyUK0DRQ/zh-cn_image_0000002589326577.png?HW-CC-KV=V1&HW-CC-Date=20260429T055319Z&HW-CC-Expire=86400&HW-CC-Sign=B5D6FB7E8A74080EC4426C437BB4520685C82EF6A728B3E0DA16FCBC17BD77A5)
