---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-refresh
title: refresh
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 容器组件 > refresh
category: harmonyos-references
scraped_at: 2026-04-28T08:02:58+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f5e256d89b3e33f2eda619d41f6618767a054bb6460e120b9e8c0a3a79c9e6d0
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

下拉刷新容器。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

支持。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-components-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| offset | <length> | - | 否 | 刷新组件静止时距离父组件顶部的距离。 |
| refreshing | boolean | false | 否 | 标识刷新组件当前是否正在刷新。  - true：刷新组件当前处于刷新状态。  - false：刷新组件当前未处于刷新状态。 |
| type | string | auto | 否 | 设置组件刷新时的动效。两个可选值，不支持动态修改。  - auto: 默认效果，列表界面拉到顶后，列表不移动，下拉后有转圈弹出。  - pulldown: 列表界面拉到顶后，可以继续往下滑动一段距离触发刷新，刷新完成后有回弹效果（如果子组件含有list，防止下拉效果冲突，需将list的scrolleffect设置为no）。 |
| lasttime | boolean | false | 否 | 设置是否显示上次更新时间，字符串格式为：“上次更新时间：XXXX ”，XXXX 按照时间日期显示规范显示，不可动态修改（建议type为pulldown时使用，固定距离位于内容下拉区域底部，使用时注意offset属性设置，防止出现重叠）。  - true：显示上次更新时间。  - false：不显示上次更新时间。 |
| timeoffset6+ | <length> | - | 否 | 设置更新时间距离父组件顶部的距离。 |
| friction | number | 42 | 否 | 下拉摩擦系数，取值范围：0-100，数值越大refresh组件跟手性高，数值越小refresh跟手性低。 |

## 样式

PhonePC/2in1TabletTVWearable

除支持[通用样式](js-components-common-styles.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| background-color | <color> | white | 否 | 设置刷新组件的背景颜色。 |
| progress-color | <color> | black | 否 | 设置刷新组件的loading图标颜色。 |

## 事件

PhonePC/2in1TabletTVWearable

仅支持如下事件：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| refresh | { refreshing: refreshingValue } | 下拉刷新状态变化时触发。可能值：  - true：当前处于下拉刷新中状态。  - false：当前未处于下拉刷新中状态。 |
| pulldown | { state: string } | 下拉开始和松手时触发。可能值：  - start：表示开始下拉。  - end：表示结束下拉。 |

## 方法

PhonePC/2in1TabletTVWearable

不支持[通用方法](js-components-common-methods.md)。

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <refresh refreshing="{{fresh}}" onrefresh="refresh">
4. <list class="list" scrolleffect="no">
5. <list-item class="listitem" for="list">
6. <div class="content">
7. <text class="text">{{$item}}</text>
8. </div>
9. </list-item>
10. </list>
11. </refresh>
12. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. align-items: center;
5. width: 100%;
6. height: 100%;
7. }

9. .list {
10. width: 100%;
11. height: 100%;
12. }

14. .listitem {
15. width: 100%;
16. height: 150px;
17. }

19. .content {
20. width: 100%;
21. height: 100%;
22. flex-direction: column;
23. align-items: center;
24. justify-content: center;
25. }

27. .text {
28. font-size: 35px;
29. font-weight: bold;
30. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction';
3. export default {
4. data: {
5. list:[],
6. fresh:false
7. },
8. onInit() {
9. this.list = [];
10. for (var i = 0; i <= 3; i++) {
11. var item = '列表元素' + i;
12. this.list.push(item);
13. }
14. },
15. refresh: function (e) {
16. promptAction.showToast({
17. message: '刷新中...'
18. })
19. var that = this;
20. that.fresh = e.refreshing;
21. setTimeout(function () {
22. that.fresh = false;
23. var addItem = '更新元素';
24. that.list.unshift(addItem);
25. promptAction.showToast({
26. message: '刷新完成!'
27. })
28. }, 2000)
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/_TNBqboHQIqHUdkcjWSb3g/zh-cn_image_0000002552960184.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000256Z&HW-CC-Expire=86400&HW-CC-Sign=7A277C5F61F1C64E5B27758C3F55484C3EA1B8BD35D8096B1881BD814FB09FA5)
