---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-text
title: text开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > text开发指导
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:10+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:1c0c65a1a946ee8ef1646c66ea0051301321f6dd760e4603cfc6f41053b64d33
---

text是文本组件，用于呈现一段文本信息。具体用法请参考[text](../harmonyos-references/js-components-basic-text.md)的API文档。

## 创建text组件

在pages/index目录下的hml文件中创建一个text组件。

```html
<!-- xxx.hml -->
<div class="container" style="text-align: center;justify-content: center; align-items: center;">
  <text>Hello World</text>
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/llKPDz__T7mNf2yOLTkAYw/zh-cn_image_0000002788466980.png?HW-CC-KV=V1&HW-CC-Date=20261114T004532Z&HW-CC-Expire=31536000000&HW-CC-Sign=6975A52F1C604F2B95F048B83ED3C705BF70F6140B49CAA4EFAFDFEC5E2D988D)

## 设置text组件样式和属性

* 添加文本样式

  设置color、font-size、allow-scale、word-spacing、text-align属性分别为文本添加颜色、大小、是否允许缩放、文本之间的间距和文本在水平方向的对齐方式。

  ```html
  <!-- xxx.hml -->
  <div class="container" style="background-color:#F1F3F5;flex-direction: column;justify-content: center; align-items: center;">   
    <text style="color: blueviolet; font-size: 40px; allow-scale:true"> 
      This is a passage
    </text>
    <text style="color: blueviolet; font-size: 40px; margin-top: 20px; allow-scale:true;word-spacing: 20px;text-align: center">
      This is a passage
    </text>
  </div>
  ```

  ```css
  /* xxx.css */
  .container {
    display: flex;
    width: 100%;
    height: 100%;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background-color: #F1F3F5;
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/Jtee7By-QfO_z6y6Un6Tow/zh-cn_image_0000002817506467.png?HW-CC-KV=V1&HW-CC-Date=20261114T004532Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB35062B9E600FF9B57582D1B174D08AE5378F53B10A549C3BB795CD6FAA7767)
* 添加划线

  设置text-decoration和text-decoration-color属性为文本添加划线和划线颜色，text-decoration枚举值请参考text自有样式。

  ```html
  <!-- xxx.hml -->
  <div class="container" style="background-color:#F1F3F5;">
    <text style="text-decoration:underline">
      This is a passage
    </text>
    <text style="text-decoration:line-through;text-decoration-color: red">
      This is a passage
     </text>
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
  }
  text{
    font-size: 50px;
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/e84Qp-WNSb--U1ZHAwN_eQ/zh-cn_image_0000002788307038.png?HW-CC-KV=V1&HW-CC-Date=20261114T004532Z&HW-CC-Expire=31536000000&HW-CC-Sign=DAC9B0397ED53B92AB040647ECAE61B7ED317B9B7FB3C19939DCAC9E47FB8E7A)
* 隐藏文本内容

  当文本内容过多而显示不全时，添加text-overflow属性将隐藏内容以省略号的形式展现。

  ```html
  <!-- xxx.hml -->
  <div class="container">
    <text class="text">
      This is a passage
    </text>
  </div>
  ```

  ```css
  /* xxx.css */
  .container {
    width: 100%;
    height: 100%;
    flex-direction: column;
    align-items: center;
    background-color: #F1F3F5;
    justify-content: center;
  }
  .text{
    width: 200px;
    max-lines: 1;
    text-overflow:ellipsis;
  }
  ```

  **说明** 

  + text-overflow样式需配合max-lines样式使用，在设置了最大行数的情况下才会生效。
  + max-lines属性设置文本最多可以展示的行数。

  ​ ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/emLDwmTESza_imWlKFYR-A/zh-cn_image_0000002817426401.png?HW-CC-KV=V1&HW-CC-Date=20261114T004532Z&HW-CC-Expire=31536000000&HW-CC-Sign=7F514A106FD8BCA0A66A572069423F2CA7FE74CB29A3DD7CC4DB6D2EA7DF2B7B)
* text组件支持[span](../harmonyos-references/js-components-basic-span.md)子组件

  ```html
  <!-- xxx.hml -->
  <div class="container" style="justify-content: center; align-items: center;flex-direction: column;background-color: #F1F3F5;  width: 100%;height: 100%;">
    <text style="font-size: 45px;">
      This is a passage
    </text>
    <text style="font-size: 45px;">
      <span style="color: aqua;">This </span><span style="color: #F1F3F5;">      1
      </span>   
      <span style="color: blue;"> is a </span>    <span style="color: #F1F3F5;">      1    </span>    
      <span style="color: red;">  passage </span>
    </text>
  </div>
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/yBnDxbgMRxCZwfM2alNofA/zh-cn_image_0000002788466982.png?HW-CC-KV=V1&HW-CC-Date=20261114T004532Z&HW-CC-Expire=31536000000&HW-CC-Sign=80285F07EE70B52FDF82C3E1EECBB4ED471B501FBC3071D76E4CF353047A4549)

  **说明** 

  + 当使用span子组件组成文本段落时，如果span属性样式异常（例如：font-weight设置为1000），将导致文本段落显示异常。
  + 在使用span子组件时，注意text组件内不能存在文本内容，如果在text组件同时包含文本内容和span子组件，则仅会显示子组件span中的内容。

## 场景示例

text组件通过数据绑定展示文本内容，span组件通过设置show属性来实现文本内容的隐藏和显示。

```html
<!-- xxx.hml -->
<div class="container">
  <div style="align-items: center;justify-content: center;">
    <text class="title">
      {{ content }}
    </text>
    <switch checked="true" onchange="test"></switch>
  </div>
  <text class="span-container" style="color: #ff00ff;">
    <span show="{{isShow}}">  {{ content  }}  </span>
    <span style="color: white;">
        1
    </span>
    <span style="color: #f76160">Hide clip </span>
  </text>
</div>
```

```css
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  background-color: #F1F3F5;
}
.title {
  font-size: 26px;
  text-align:center;
  width: 200px;
  height: 200px;
}
```

```js
// xxx.js
export default {
  data: {
    isShow:true,
    content: 'Hello World'
  },
  onInit(){    },
  test(e) {
    this.isShow = e.checked
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/U76czH3HRU2YKC4pnBNy0A/zh-cn_image_0000002817506469.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004532Z&HW-CC-Expire=31536000000&HW-CC-Sign=83508D7FA2776846FFD2350F672CAE0F9378AEB20E748BE4898F2009D5FCBB6F)
