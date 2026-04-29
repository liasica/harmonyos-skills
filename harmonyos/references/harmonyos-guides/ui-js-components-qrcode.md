---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-qrcode
title: qrcode开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > qrcode开发指导
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6ffcde741fef4d39bde3f035d913c630cebb6000894fad16b7509bed6eec2e22
---

生成并显示二维码，具体用法请参考[qrcode](../harmonyos-references/js-components-basic-qrcode.md)。

## 创建qrcode组件

在pages/index目录下的hml文件中创建一个qrcode组件。

```
1. <!-- xxx.hml-->
2. <div class="container">
3. <qrcode value="Hello"></qrcode>
4. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. align-items: center;
7. justify-content: center;
8. background-color: #F1F3F5;
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/qp90LKqSSQa72OJodLbElQ/zh-cn_image_0000002589324487.png?HW-CC-KV=V1&HW-CC-Date=20260429T052850Z&HW-CC-Expire=86400&HW-CC-Sign=7C10B05A50D436D113CA1E3AF6F82D9D4551A93FB7F0C14740461A89313E4F67)

说明

qrcode组件在创建的时候value的值为必填项。

## 设置组件类型

通过设置qrcode的type属性来选择二维码类型，如定义qrcode为矩形二维码、圆形二维码。

```
1. <!-- xxx.hml-->
2. <div class="container">
3. <select onchange="settype">
4. <option for="{{bcol_list}}" value="{{$item}}">{{$item}}</option>
5. </select>
6. <qrcode value="Hello" type="{{qr_type}}"></qrcode>
7. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. align-items: center;
7. justify-content: center;
8. background-color: #F1F3F5;
9. }
10. select{
11. margin-top: 50px;
12. margin-bottom: 50px;
13. }
```

```
1. // index.js
2. export default {
3. data: {
4. qr_type: 'rect',
5. bcol_list: ['rect','circle']
6. },
7. settype(e) {
8. this.qr_type = e.newValue
9. },
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/Dk7rs50mQSyvdeslgnGR1g/zh-cn_image_0000002589244425.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052850Z&HW-CC-Expire=86400&HW-CC-Sign=9F7633C8C823DC9DD4976EB61A0FA6811F40D9F139BC02DD1B5475363CD21D88)

## 设置样式

通过color和background-color样式为二维码设置显示颜色和背景颜色。

```
1. <!-- xxx.hml-->
2. <div class="container">
3. <qrcode value="Hello" type="rect"></qrcode>
4. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. align-items: center;
7. justify-content: center;
8. background-color: #F1F3F5;
9. }
10. qrcode{
11. width: 300px;
12. height: 300px;
13. color: blue;  background-color: #ffffff;
14. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/68h6HEzbTlqH-aEJiOpc9Q/zh-cn_image_0000002558764618.png?HW-CC-KV=V1&HW-CC-Date=20260429T052850Z&HW-CC-Expire=86400&HW-CC-Sign=E157D5E090F841CE339271E3F9B046555261A5C030165E25357BF11AB769A84D)

说明

* width和height不一致时，取二者较小值作为二维码的边长，且最终生成的二维码居中显示。
* width和height只设置一个时，取设置的值作为二维码的边长。都不设置时，使用200px作为默认边长。

## 场景示例

在本场景中将二维码与输入框绑定，通过改变输入框的内容改变二维码。

```
1. <!-- xxx.hml-->
2. <div class="container">
3. <input style="margin-bottom: 100px;" onchange="change"></input>
4. <qrcode value="{{textVal}}"></qrcode>
5. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. align-items: center;
7. justify-content: center;
8. background-color: #F1F3F5;
9. }
10. qrcode{
11. width: 400px;
12. height: 400px;
13. }
```

```
1. // index.js
2. export default{
3. data: {
4. textVal: ''
5. },
6. change(e){
7. this.textVal = e.value
8. }
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/IOREHO4cS0-Z7f7rWeMZmQ/zh-cn_image_0000002558604962.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052850Z&HW-CC-Expire=86400&HW-CC-Sign=EB30CAA8B8D8FAD1B81C95C03769A81E6D558C2F6069A77C1B9EAEA54B634911)
