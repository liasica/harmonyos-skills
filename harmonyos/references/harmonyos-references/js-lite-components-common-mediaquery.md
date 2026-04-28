---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-common-mediaquery
title: 媒体查询
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 组件通用信息 > 媒体查询
category: harmonyos-references
scraped_at: 2026-04-28T08:03:26+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:2ebf1ef5d83de305b24f947918c20570608b07d584a9ec1d873e74072630601b
---

说明

* 从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* media属性值默认为设备的真实尺寸大小、物理像素和真实的屏幕分辨率。

媒体查询（Media Query）应用十分广泛，开发者经常需要根据设备的大致类型或者特定的特征和设备参数（例如屏幕分辨率）来修改应用的样式。使用媒体查询针对设备和应用的属性信息，可以设计出相匹配的布局样式。

## CSS语法规则

PhonePC/2in1TabletTVWearableLite Wearable

使用@media来引入查询语句，具体规则如下：

```
1. @media [media-type] [and|or] [(media-feature)] {
2. CSS-Code;
3. }
```

@media screen and (round-screen: true) { … } ： 当设备屏幕是圆形时条件成立

@media (max-height: 454) { … } ：范围查询，CSS level 3 写法

说明

* 不支持<=，>=，<，>操作符;
* 从API version 9开始，支持多重()嵌套使用；
* media语句整体长度不能超过 512 个字符；
* 单个media条件长度不能超过32个字符；

## 媒体类型

PhonePC/2in1TabletTVWearableLite Wearable

| 类型 | 说明 |
| --- | --- |
| screen | 按屏幕相关参数进行媒体查询。 |

## 媒体逻辑操作

PhonePC/2in1TabletTVWearableLite Wearable

媒体逻辑操作符：and、or9+用于构成媒体查询语句，详细解释说明如下表。

**表1** 媒体逻辑操作符

| 类型 | 说明 |
| --- | --- |
| and | 将多个媒体特征（Media Feature）以“与”的方式连接成一个媒体查询，只有当所有媒体特征都为true，查询条件成立。另外，它还可以将媒体类型和媒体功能结合起来。  例如：screen and (device-type: liteWearable) and (max-height: 454) 表示当设备类型是智能穿戴同时应用的最大高度小于等于454个像素单位时成立。 |
| or9+ | 将多个媒体特征以“或”的方式连接成一个媒体查询，如果存在结果为true的媒体特征，则查询条件成立。  例如：screen and (max-height: 454) or （round-screen：true）表示当应用高度小于等于454个像素单位或者设备屏幕是圆形时，条件成立。 |

## 媒体特征

PhonePC/2in1TabletTVWearableLite Wearable

| 类型 | 说明 |
| --- | --- |
| height | 应用页面显示区域的高度。 |
| min-height | 应用页面显示区域的最小高度。 |
| max-height | 应用页面显示区域的最大高度。 |
| width | 应用页面显示区域的宽度。 |
| min-width | 应用页面显示区域的最小宽度。 |
| max-width | 应用页面显示区域的最大宽度。 |
| aspect-ratio | 应用页面显示区域的宽度与高度的比值。  例如：aspect-ratio: 1/2 |
| min-aspect-ratio | 应用页面显示区域的宽度与高度的最小比值。 |
| max-aspect-ratio | 应用页面显示区域的宽度与高度的最大比值。 |
| round-screen | 屏幕类型，圆形屏幕为 true， 非圆形屏幕为 false。 |

## 通用媒体特征示例代码

PhonePC/2in1TabletTVWearableLite Wearable

多个.container中定义的属性个数及类型必须保持一致，否则可能导致显示异常。

```
1. <!-- xxx.hml -->
2. <div>
3. <div class="container">
4. <text class="title">Hello World</text>
5. </div>
6. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 300px;
4. height: 600px;
5. background-color: #008000;
6. }
7. .title {
8. font-size: 30px;
9. text-align: center;
10. }
11. @media (device-type: smartVision) {
12. .container {
13. width: 500px;
14. height: 500px;
15. background-color: #fa8072;
16. }
17. }
18. @media (device-type: liteWearable) {
19. .container {
20. width: 300px;
21. height: 300px;
22. background-color: #008b8b;
23. }
24. }
```
