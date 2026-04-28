---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-mediaquery
title: 媒体查询
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > JS服务卡片UI组件 > 组件通用信息 > 媒体查询
category: harmonyos-references
scraped_at: 2026-04-28T08:03:35+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2073983e982aa859361ecb73d7aaef267e0191e35a1c360f97d34056824382f8
---

媒体查询（MediaQuery）在移动设备上应用十分广泛，开发者经常需要根据设备的大致类型或者特定的特征和设备参数（例如屏幕分辨率）来修改应用的样式。为此媒体查询提供了如下功能：

1. 针对设备和应用的属性信息，可以设计出相匹配的布局样式。
2. 当屏幕发生动态改变时（比如分屏、横竖屏切换），应用页面布局同步更新。

说明

从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

media属性值默认为设备的真实尺寸大小、物理像素和真实的屏幕分辨率。请勿与以720px为基准的项目配置宽度px混淆。

## CSS语法规则

PhonePC/2in1TabletTVWearable

使用@media来引入查询语句，具体规则如下：

```
1. @media [media-type] [and|not|only] [(media-feature)] {
2. CSS-Code;
3. }
```

例子：

@media screen and (round-screen: true) { … } // 当设备屏幕是圆形时条件成立

@media (max-height: 800) { … } // 范围查询，CSS level 3 写法

@media (height <= 800) { … } // 范围查询，CSS level 4 写法，与CSS level3写法等价

@media screen and (device-type: tv) or (resolution < 2) { … } // 同时包含媒体类型和多个媒体特征的多条件复杂语句查询

## 页面中引用资源

PhonePC/2in1TabletTVWearable

通过@import方式引入媒体查询，具体使用方法如下：

```
1. @import url [media-type] [and|not|only] [(media-feature)];
```

例如：

```
1. @import '../common/style.css' screen and (min-width: 600) and (max-width: 1200);
```

## 媒体类型

PhonePC/2in1TabletTVWearable

| 类型 | 说明 |
| --- | --- |
| screen | 按屏幕相关参数进行媒体查询。 |

## 媒体逻辑操作

PhonePC/2in1TabletTVWearable

媒体逻辑操作符：and、or、not、only用于构成复杂媒体查询，也可以通过comma（,）将其组合起来，详细解释说明如下表。

**表1** 媒体逻辑操作符

| 类型 | 说明 |
| --- | --- |
| and | 将多个媒体特征（Media Feature）以逻辑运算符“与”的方式连接成一个媒体查询，只有当所有媒体特征都为true，查询条件成立。另外，它还可以将媒体类型和媒体功能结合起来。  例如：screen and (device-type: wearable) and (max-height: 600) 表示当设备类型是智能穿戴同时应用的最大高度小于等于600个像素单位时成立。 |
| not | 取反媒体查询结果，媒体查询结果不成立时返回true，否则返回false。在媒体查询列表中应用not，则not仅取反应用它的媒体查询。  例如：not screen and (min-height: 50) and (max-height: 600) 表示当应用高度小于50个像素单位或者大于600个像素单位时成立。  使用not运算符时必须指定媒体类型。 |
| only | 当整个表达式都匹配时，才会应用选择的样式，可以应用在防止某些较早的版本的浏览器上产生歧义的场景。一些较早版本的浏览器对于同时包含了媒体类型和媒体特征的语句会产生歧义，比如：  screen and (min-height: 50)  老版本浏览器会将这句话理解成screen，从而导致仅仅匹配到媒体类型（screen），就应用了指定样式，使用only可以很好地规避这种情况。  使用only时必须指定媒体类型。 |
| ,(comma) | 将多个媒体特征以“或”的方式连接成一个媒体查询，如果存在结果为true的媒体特征，则查询条件成立。其效果等同于or运算符。  例如：screen and (min-height: 1000), （round-screen：true） 表示当应用高度大于等于1000个像素单位或者设备屏幕是圆形时，条件成立。 |
| or | 将多个媒体特征以“或”的方式连接成一个媒体查询，如果存在结果为true的媒体特征，则查询条件成立。  例如：screen and (max-height: 1000) or （round-screen：true）表示当应用高度小于等于1000个像素单位或者设备屏幕是圆形时，条件成立。 |

在MediaQuery Level 4中引入了范围查询，使其能够使用max-，min-的同时，也支持了<=，>=，<，>操作符。

**表2** 媒体逻辑范围操作符

| 类型 | 说明 |
| --- | --- |
| <= | 小于等于，例如：screen and (height <= 50)。 |
| >= | 大于等于，例如：screen and (height >= 600)。 |
| < | 小于，例如：screen and (height < 50)。 |
| > | 大于，例如：screen and (height > 600)。 |

## 媒体特征

PhonePC/2in1TabletTVWearable

| 类型 | 说明 |
| --- | --- |
| height | 应用页面显示区域的高度。 |
| min-height | 应用页面显示区域的最小高度。 |
| max-height | 应用页面显示区域的最大高度。 |
| width | 应用页面显示区域的宽度。 |
| min-width | 应用页面显示区域的最小宽度。 |
| max-width | 应用页面显示区域的最大宽度。 |
| resolution | 设备的分辨率，支持dpi，dppx和dpcm单位。其中：  - dpi表示每英寸中物理像素个数，1dpi≈0.39dpcm；  - dpcm表示每厘米上的物理像素个数，1dpcm ≈ 2.54dpi；  - dppx表示每个px中的物理像素数（此单位按96px=1英寸为基准，与页面中的px单位计算方式不同），1dppx = 96dpi。 |
| min-resolution | 设备的最小分辨率。 |
| max-resolution | 设备的最大分辨率。 |
| orientation | 屏幕的方向。  可选值：  - orientation: portrait（设备竖屏）  - orientation: landscape（设备横屏） |
| aspect-ratio | 应用页面显示区域的宽度与高度的比值。  例如：aspect-ratio:1/2 |
| min-aspect-ratio | 应用页面显示区域的宽度与高度的最小比值。 |
| max-aspect-ratio | 应用页面显示区域的宽度与高度的最大比值。 |
| device-height | 设备的高度。 |
| min-device-height | 设备的最小高度。 |
| max-device-height | 设备的最大高度。 |
| device-width | 设备的宽度。 |
| min-device-width | 设备的最小宽度。 |
| max-device-width | 设备的最大宽度。 |
| round-screen | 屏幕类型，圆形屏幕为true， 非圆形屏幕为 false。 |
| dark-mode6+ | 系统为深色模式时为true，否则为false。 |

## 示例代码

PhonePC/2in1TabletTVWearable

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

8. @media (device-type: wearable) {
9. .container-inner {
10. justify-content: center;
11. align-items: center;
12. padding: 40px 26px;
13. }

15. .title {
16. text-align: center;
17. }

19. .detail_text {
20. max-lines: 2;
21. text-align: center;
22. }
23. }

25. @media (device-type: tv) {
26. .title {
27. font-size: 16px;
28. }

30. .detail_text {
31. font-size: 12px;
32. }
33. }

35. @media (device-type: car) {
36. .title {
37. font-size: 12px;
38. color: #FFFFFF;
39. font-family: @id_text_font_family_medium;
40. }

42. .detail_text {
43. font-size: 12px;
44. margin-top: 2px;
45. font-family: @id_text_font_family_regular;
46. color: #FFFFFF;
47. }
48. }
```
