---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-menu
title: menu开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > menu开发指导
category: harmonyos-guides
scraped_at: 2026-09-21T06:17:27+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:4e9f4796ac20a6e1bc4b38d748aff822e1663b7c024196bc685eb2e6b0160ce9
---

提供菜单组件，作为临时性弹出窗口，用于展示用户可执行的操作，具体用法请参考[menu](../harmonyos-references/js-components-basic-menu.md)。

## 创建menu组件

在pages/index目录下的hml文件中创建一个menu组件，添加target、type、title属性。

```html
<!-- xxx.hml-->
<div class="container">
  <text class="title-text" id="textId">show menu</text>
  <menu target="textId" type="click" title="title">
    <option value="Item 1">Item 1</option>
    <option value="Item 2">Item 2</option>
    <option value="Item 3">Item 3</option>
  </menu>
</div>
```

```css
/* xxx.css */
.container{
  width: 100%;
  height: 100%;
  flex-direction: column;
  background-color: #F1F3F5;
  align-items: center;
  justify-content: center;
  width: 100%;
}
.title-text{
  font-size: 35px;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/JKzj7ZjiToKI1OnQOqHRCA/zh-cn_image_0000002733274338.png)

**说明** 

* menu仅支持[option](../harmonyos-references/js-components-basic-option.md)子组件。
* menu组件不支持focusable、disabled属性。

## 设置样式

为menu组件设置样式，例如字体颜色、大小、字符间距等。

```html
<!-- xxx.hml-->
<div class="container">
  <text class="title-text" id="textId">show menu</text>
  <menu target="textId" type="click" title="title">
    <option value="Item 1">Item 1</option>
    <option value="Item 2">Item 2</option>
    <option value="Item 3">Item 3</option>
  </menu>
</div>
```

```css
/* xxx.css */
.container{
  width: 100%;
  height: 100%;
  flex-direction: column;
  background-color: #F1F3F5;
  align-items: center;
  justify-content: center;
  width: 100%;
}
.title-text{
  font-size: 35px;
  background-color: #5a5aee;
  color: white;
  width: 70%;
  text-align: center;
  height: 85px;
  border-radius: 12px;
}
.menu{
  text-color: blue;
  font-size: 35px;
  letter-spacing: 2px;
}
option{
  color: #6a6aef;
  font-size: 30px;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/fn_ofdsbRSaxmcWuqF4XzA/zh-cn_image_0000002733434220.png)

## 绑定事件

为menu组件绑定oncancel事件（取消操作时触发）。

```html
<!-- xxx.hml-->
<div class="container">
  <text  class="title-text" id="textId" onclick="textClick">show menu</text>
  <menu  title="title" oncancel="cancel" id="menuId">
    <option value="Item 1">Item 1</option>
    <option value="Item 2">Item 2</option>
    <option value="Item 3">Item 3</option>
  </menu>
</div>
```

```css
/* xxx.css */
.container{
  width: 100%;
  height: 100%;
  flex-direction: column;
  background-color: #F1F3F5;
  width: 100%;
}
.title-text{
  font-size: 35px;
  background-color: #5a5aee;
  color: white;
  width: 70%;
  text-align: center;
  height: 85px;
  border-radius: 12px;
  margin-top: 500px;
  margin-left: 15%;
}
menu{
  text-color: blue;
  font-size: 35px;
  letter-spacing: 2px;
}
option{
  color: #6a6aef;
  font-size: 30px;
}
```

```js
// xxx.js
export default {
  cancel() {
    this.getUIContext().getPromptAction().showToast({
      message: "cancel"
    })
  },
  textClick() {
    this.$element("menuId").show({ x: 175,y: 590 });
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/CPohyjJKQz6dmdn9Qa88TQ/zh-cn_image_0000002762993741.gif)
