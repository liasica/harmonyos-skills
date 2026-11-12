---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-qrcode
title: qrcode开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > qrcode开发指导
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:38d842f956bc7c6187c6b6dd2e4193e9fe2156f6e0ee091cd1978fb58b84f6f9
---

生成并显示二维码，具体用法请参考[qrcode](../harmonyos-references/js-components-basic-qrcode.md)。

## 创建qrcode组件

在pages/index目录下的hml文件中创建一个qrcode组件。

```html
<!-- xxx.hml-->
<div class="container">
  <qrcode value="Hello"></qrcode>
</div>
```

```css
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #F1F3F5;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/sLxTzzWBRFC3CiKrorVL4A/zh-cn_image_0000002786359332.png?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=F9505FC1371FB7560AD834D2371597789C3A80330EA6E7FDF457AAEFFB60B0C1)

**说明** 

qrcode组件在创建的时候value的值为必填项。

## 设置组件类型

通过设置qrcode的type属性来选择二维码类型，如定义qrcode为矩形二维码、圆形二维码。

```html
<!-- xxx.hml-->
<div class="container">
  <select onchange="settype">
    <option for="{{bcol_list}}" value="{{$item}}">{{$item}}</option>
  </select>
  <qrcode value="Hello" type="{{qr_type}}"></qrcode>
</div>
```

```css
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #F1F3F5;
}
select{
  margin-top: 50px;
  margin-bottom: 50px;
}
```

```js
// index.js
export default {
  data: {
    qr_type: 'rect',
    bcol_list: ['rect','circle']
  },
  settype(e) {
    this.qr_type = e.newValue
  },
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/mreT9ywIRjOvZUdkC-ISKA/zh-cn_image_0000002815558753.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=635758E6DB587ED3423353FCDAFCAF4B005C31141D801EDFD3D1C10F7BE728C0)

## 设置样式

通过color和background-color样式为二维码设置显示颜色和背景颜色。

```html
<!-- xxx.hml-->
<div class="container">
  <qrcode value="Hello" type="rect"></qrcode>
</div>
```

```css
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #F1F3F5;
}
qrcode{
  width: 300px;
  height: 300px;
 color: blue;  background-color: #ffffff;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/w8M3j897TYSo73-b0juSCA/zh-cn_image_0000002815398837.png?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=89EAADD01A0A51D41CCE3003532DA3019D9304282C085F91B9C37322A36430AD)

**说明** 

* width和height不一致时，取二者较小值作为二维码的边长，且最终生成的二维码居中显示。
* width和height只设置一个时，取设置的值作为二维码的边长。都不设置时，使用200px作为默认边长。

## 场景示例

在本场景中将二维码与输入框绑定，通过改变输入框的内容改变二维码。

```html
<!-- xxx.hml-->
<div class="container">
  <input style="margin-bottom: 100px;" onchange="change"></input>
  <qrcode value="{{textVal}}"></qrcode>
</div>
```

```css
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #F1F3F5;
}
qrcode{
  width: 400px;
  height: 400px;
}
```

```js
// index.js
export default {
  data: {
    textVal: ''
  },
  change(e){
    this.textVal = e.value
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/lQESucG2S0umnmlh4bmNLA/zh-cn_image_0000002786519262.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=4762980D8A8A96B948E7C493ECB59A62C82C42F4355CE04B44A6E93A375F0764)
