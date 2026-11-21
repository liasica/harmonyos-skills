---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-text
title: text开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > text开发指导
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:14+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:fcfb008b3a82657a773430548b20e6f954409e61e88121a109ec054ff93a88a4
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/sJ4jlJ2cT_q-C2BioS61rA/zh-cn_image_0000002821756925.png?HW-CC-KV=V1&HW-CC-Date=20261121T010950Z&HW-CC-Expire=31536000000&HW-CC-Sign=3FAE4581E9D0022AAA8595ED4A2979270F581BE6E9B5ECB2A94EFC0DE8EBA02D)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/JNW-VLw6QnOrDm6oEXQx2w/zh-cn_image_0000002793036988.png?HW-CC-KV=V1&HW-CC-Date=20261121T010950Z&HW-CC-Expire=31536000000&HW-CC-Sign=913847FFE1C8A05D457F709463CC562DAE675AEB451539E006123D9C21426307)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/kZyCPodNT0CI_eTlwQzFbQ/zh-cn_image_0000002792877018.png?HW-CC-KV=V1&HW-CC-Date=20261121T010950Z&HW-CC-Expire=31536000000&HW-CC-Sign=F33BC241240D5A2CAB8554082C509467AA3C6C331F268C636393C972C654FFB0)
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

  ​ ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/2SHsZApVRKGB2kYrNwkFUA/zh-cn_image_0000002821836925.png?HW-CC-KV=V1&HW-CC-Date=20261121T010950Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F8F95BF6A2476DF6DC5207788DA524EFC3319FEFBBE1DC29EB98990C50C821A)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/cUVDtKTRRL6maMbKSOtyrA/zh-cn_image_0000002821756927.png?HW-CC-KV=V1&HW-CC-Date=20261121T010950Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7E9C4D12366E8FBD6C39E59619D154CDFFBBA535B6A2C38D90AFF80E7D0F7B1)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/mu2Rpsz1Q1K2tRXlBxa3aw/zh-cn_image_0000002793036990.gif?HW-CC-KV=V1&HW-CC-Date=20261121T010950Z&HW-CC-Expire=31536000000&HW-CC-Sign=8E8CE77DB5417280B56030B836CC40ABB84AB99CEFAC3E3A4C3F9A50B2BCFC81)
