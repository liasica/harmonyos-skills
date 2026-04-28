---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-qrcode
title: qrcode
category: harmonyos-references
scraped_at: 2026-04-28T08:03:07+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:aa837f111bbf66fb3e729c387d12315f6aa208e7d13d4a1351fe5232f3d0145a
---

说明

从API version 5开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

生成并显示二维码。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

不支持。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-components-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| value | string | - | 是 | 用来生成二维码的内容。 |
| type | string | rect | 否 | 二维码类型。可能选项有：  - rect：矩形二维码。  - circle：圆形二维码。 |

## 样式

PhonePC/2in1TabletTVWearable

除支持[通用样式](js-components-common-styles.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| color | <color> | #000000 | 否 | 二维码颜色。 |
| background-color | <color> | #ffffff | 否 | 二维码背景颜色。 |

说明

* width和height不一致时，取二者较小值作为二维码的边长。且最终生成的二维码居中显示。
* width和height只设置一个时，取设置的值作为二维码的边长。都不设置时，使用200px作为默认边长。
* 生成二维码不可用时，请参考[Scan Kit（统一扫码服务）](scan-api.md)。

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
2. <div class="container">
3. <qrcode value="{{qr_value}}" type="{{qr_type}}"
4. style="color: {{qr_col}};background-color: {{qr_bcol}};width: {{qr_size}};height: {{qr_size}};margin-bottom: 70px;"></qrcode>
5. <text class="txt">Type</text>
6. <switch showtext="true" checked="true" texton="rect" textoff="circle" onchange="setType"></switch>
7. <text class="txt">Color</text>
8. <select onchange="setCol">
9. <option for="{{col_list}}" value="{{$item}}">{{$item}}</option>
10. </select>
11. <text class="txt">Background Color</text>
12. <select onchange="setBCol">
13. <option for="{{bcol_list}}" value="{{$item}}">{{$item}}</option>
14. </select>
15. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. justify-content: center;
7. align-items: center;
8. }
9. .txt {
10. margin: 30px;
11. color: orangered;
12. }
13. select{
14. margin-top: 40px;
15. margin-bottom: 40px;
16. }
```

```
1. /* index.js */
2. export default {
3. data: {
4. qr_type: 'rect',
5. qr_size: '300px',
6. qr_col: '#87ceeb',
7. col_list: ['#87ceeb','#fa8072','#da70d6','#80ff00ff','#00ff00ff'],
8. qr_bcol: '#f0ffff',
9. bcol_list: ['#f0ffff','#ffffe0','#d8bfd8']
10. },
11. setType(e) {
12. if (e.checked) {
13. this.qr_type = 'rect'
14. } else {
15. this.qr_type = 'circle'
16. }
17. },
18. setCol(e) {
19. this.qr_col = e.newValue
20. },
21. setBCol(e) {
22. this.qr_bcol = e.newValue
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/oQC2TNgXTEWDkJkWEYXOPg/zh-cn_image_0000002552960198.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000304Z&HW-CC-Expire=86400&HW-CC-Sign=D7AF4DCB3B18A3160457759A1118A062119E48FA37EFB6691B7F9C95D30C09BB)
