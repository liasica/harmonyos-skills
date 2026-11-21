---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-toolbar
title: toolbar开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > toolbar开发指导
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:14+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:25c17616ef7f55af061bd5b1c9f1aba9ed052175cb0f206ad7b0d954235797de
---

toolbar为页面工具栏组件，用于展示针对当前界面的操作选项，可作为页面的一级导航。具体用法请参考[toolbar](../harmonyos-references/js-components-basic-toolbar.md)。

## 创建toolbar组件

在pages/index目录下的hml文件中创建一个toolbar组件。

```html
<!-- xxx.hml -->
<div class="container">
  <toolbar style="background-color: #F1F3F5;">
    <toolbar-item value="item1"></toolbar-item>
    <toolbar-item value="item2"></toolbar-item>
  </toolbar>
</div>
```

```css
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #F1F3F5;
}
toolbar-item{
  font-size: 35px;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/2kvWcHZ2Rg2NlUBGIKmPHQ/zh-cn_image_0000002821836945.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011114Z&HW-CC-Expire=31536000000&HW-CC-Sign=56B19317E411AED42A7CA617B30F6F54621BCC61C2285F91BD2C636DF67144C4)

## 添加子组件

toolbar组件仅支持toolbar-item为子组件，页面最多可以展示5个toolbar-item子组件，如果存在6个及以上toolbar-item，则保留前面4个，后续的将收纳到工具栏上的更多项中，通过点击更多项弹窗进行展示。并且更多项展示的组件样式采用系统默认样式，toolbar-item上设置的自定义样式不生效。

```html
<!-- xxx.hml -->
<div class="container">
  <toolbar>
    <toolbar-item value="item1"></toolbar-item>    
    <toolbar-item value="item2"></toolbar-item>    
    <toolbar-item value="item3"></toolbar-item>    
    <toolbar-item value="item4"></toolbar-item>    
    <toolbar-item value="item5"></toolbar-item>    
    <toolbar-item value="item6"></toolbar-item>
  </toolbar>
</div>
```

```css
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #F1F3F5;
}
toolbar-item{
  font-size: 35px;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/nxyp77vrR1m38IeyZFsRyg/zh-cn_image_0000002821756947.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011114Z&HW-CC-Expire=31536000000&HW-CC-Sign=F4BB753E4BE7EB033FA77E526BEFE63E426CC83E9CF749A542B1DE0B4D7EB746)

## 设置样式

设置position样式控制toolbar组件的位置，并设置子组件toolbar-item的字体颜色、大小及背景色。

```html
<!-- xxx.hml -->
<div class="container">
  <toolbar style="position: fixed;bottom: 5%;width: 100%;background-color: #F1F3F5;">
    <toolbar-item value="item1" icon="common/images/1.png" class="toolbarActive"></toolbar-item>
    <toolbar-item value="item2" icon="common/images/2.png"></toolbar-item>
    <toolbar-item value="item3" icon="common/images/1.png"></toolbar-item>
    <toolbar-item value="item4" icon="common/images/2.png"></toolbar-item>
  </toolbar>
</div>
```

```css
/* xxx.css */
.container {
  background-color: #F1F3F5;
  flex-direction: column;
  width: 100%;
  height: 100%;
  justify-content: center;
  align-items: center;
}
toolbar-item{
  font-size: 35px;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/0V9hG0wcTDWWIWFT67XPng/zh-cn_image_0000002793037010.png?HW-CC-KV=V1&HW-CC-Date=20261121T011114Z&HW-CC-Expire=31536000000&HW-CC-Sign=DEC1B0E7649A5756E24AA8CE770D874195F68DC5A26E95061702AC0BDEF6A0FE)

## 绑定事件

分别给toolbar-item绑定单击事件和长按事件，单击后文本变红，长按时文本变蓝。

```html
<!-- xxx.hml -->
<div class="container">
  <toolbar style="position: fixed;top: 50%;width: 100%;background-color: #F1F3F5;">
    <toolbar-item value="item1" icon="common/images/1.png" style="color: {{itemColor}};" onclick="itemClick"></toolbar-item>
    <toolbar-item value="item2" icon="common/images/2.png"  style="color: {{itemColor}}"></toolbar-item>
    <toolbar-item value="item3" icon="common/images/3.png"  style="color: {{itemColor}}" onlongpress="itemLongPress"></toolbar-item>
  </toolbar>
</div>
```

```css
/* xxx.css */
.container {
  background-color: #F1F3F5;
  flex-direction: column;
  width: 100%;
  height: 100%;
  justify-content: center;
  align-items: center;
}
toolbar-item{
  font-size: 35px;
}
```

```js
// xxx.js
import promptAction from '@ohos.promptAction';
export default {
  data:{
    itemColor:'black'
  },
  itemClick(){
    this.itemColor= "red";
    promptAction.showToast({duration:2000,message:'item click'});
  },
  itemLongPress(){
    promptAction.showToast({duration:2000,message:'item long press'});
    this.itemColor= "blue";
  },
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/0v5l6NJ-QQW3Q1cXQMnD_Q/zh-cn_image_0000002792877040.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011114Z&HW-CC-Expire=31536000000&HW-CC-Sign=A966847D224E91D2B7785E541250B4D5C8AFF51B749433E1227DEC68032F809E)

**说明** 

toolbar组件不支持添加事件和方法，但其子组件toolbar-item支持。

## 场景示例

本场景中开发者可点击toolbar-item组件，改变当前组件文本颜色并更换相对应的图片内容。

使用for循环创建toolbar-item组件并添加点击事件，点击后获得索引值进行存储。设置文本颜色时，判断当前索引值是否为储存的值，若相同则设置为红色，不同则使用默认颜色。

```html
<!-- xxx.hml -->
<div class="container">
  <image src="{{imgList[active]}}"></image>
  <toolbar style="position: fixed;bottom: 5%;width: 100%;background-color: #F1F3F5;">
    <toolbar-item value="{{ item.option}}" icon="{{item.icon}}" style="color: {{active == $idx?'red':'black'}};background-color: {{active== $idx?'#dbe7f1':'#F1F3F5'}};" for="{{item in itemList}}" onclick="itemClick({{$idx}})"></toolbar-item>
    </toolbar>
</div>
```

```css
/* xxx.css */
.container {
  background-color: #F1F3F5;
  flex-direction: column;
  width: 100%;
  justify-content: center;
  align-items: center;
}
toolbar-item{
  font-size: 35px;
}
```

```js
// xxx.js
export default {
  data:{
    active: 0,
    imgList:["common/images/1.png","common/images/2.png","common/images/3.png","common/images/4.png"],
    itemList:[
      {option:'item1',icon:'common/images/1.png'},
      {option:'item2',icon:'common/images/2.png'},
      {option:'item3',icon:'common/images/3.png'},
      {option:'item4',icon:'common/images/4.png'},
    ]
  },
  itemClick(id){
    this.active= id;
  },
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/XIwvvG7dRn6dG8IKvBP66A/zh-cn_image_0000002821836947.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011114Z&HW-CC-Expire=31536000000&HW-CC-Sign=548B3F0868500BE26C98C2F2BC2C6EC8ED1651038B16B3B6F69A01D4B9D9F8E1)
