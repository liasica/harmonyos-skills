---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-qrcode
title: qrcode开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > qrcode开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f63c75047e7421195198f1773fb408cd10d2c0aeac9f230db4ca686e7fdb7345
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/h1gA2HqNShyM1_JaD8wVog/zh-cn_image_0000002552958126.png?HW-CC-KV=V1&HW-CC-Date=20260427T234028Z&HW-CC-Expire=86400&HW-CC-Sign=9B68ECB29B7C397B530062FE146D0A803F742760C5DA39AFA7462D85434ED05F)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/-iPKdYrZQxyBfKrQ-znSSg/zh-cn_image_0000002583478127.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234028Z&HW-CC-Expire=86400&HW-CC-Sign=9817F478180BE6877C476B871153217F5155D94D8E90CB5FA8640244E970F3C5)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/moZ8RK0dRZueUJk74hJCgA/zh-cn_image_0000002552798478.png?HW-CC-KV=V1&HW-CC-Date=20260427T234028Z&HW-CC-Expire=86400&HW-CC-Sign=979B38CEEE183D4EE10C23EA65C45FF8762F45D04FBB3005471BEB2098FBCE86)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/fVtsv0GARZWCw2E6TIurHw/zh-cn_image_0000002583438173.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234028Z&HW-CC-Expire=86400&HW-CC-Sign=9C509284D4C53648A762FC8521A71054037EBFB52C62B36EE66BA8048A4089DB)
