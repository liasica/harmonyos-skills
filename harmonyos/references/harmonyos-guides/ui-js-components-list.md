---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-list
title: list开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 容器组件 > list开发指导
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:10+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:da80f5ea5c3ec309c2cffe858dc0900cca4653a40005ad9844d47d8adb9c18a6
---

list是用来显示列表的组件，包含一系列相同宽度的列表项，适合连续、多行地呈现同类数据。具体用法请参考[list API](../harmonyos-references/js-components-container-list.md)。

## 创建list组件

在pages/index目录下的hml文件中创建一个list组件。

```html
<!-- xxx.hml -->
<div class="container"> 
 <list>    
   <list-item class="listItem"></list-item>
   <list-item class="listItem"></list-item>
   <list-item class="listItem"></list-item>
   <list-item class="listItem"></list-item>
 </list>
</div>
```

```css
/* xxx.css */
.container {
  width:100%;
  height:100%;
  flex-direction: column;
  align-items: center;
  background-color: #F1F3F5;
}
.listItem{
  height: 20%;
  background-color:#d2e0e0;
  margin-top: 20px;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/SHn8UdmHSHqbBcj6A4cDDw/zh-cn_image_0000002788307024.png?HW-CC-KV=V1&HW-CC-Date=20261114T004710Z&HW-CC-Expire=31536000000&HW-CC-Sign=317F9F3D0F05C0F880BD14C545D2BFD0C7CD6E1F6698856D7FD16E6E1B1CB61A)

**说明** 

* <list-item-group>是<list>的子组件，实现列表分组功能，不能再嵌套<list>，可以嵌套<list-item>。
* <list-item>是<list>的子组件，展示列表的具体项。

## 添加滚动条

设置scrollbar属性为on即可在屏幕右侧生成滚动条，实现长列表或者屏幕滚动等效果。

```html
<!-- xxx.hml -->
<div class="container">
  <list class="listCss" scrollbar="on" >
    <list-item class="listItem"></list-item>
    <list-item class="listItem"></list-item>
    <list-item class="listItem"></list-item>
    <list-item class="listItem"></list-item>
    <list-item class="listItem"></list-item>
    <list-item class="listItem"></list-item>
 </list>
</div>
```

```css
/* xxx.css */
.container {
  flex-direction: column;
  background-color: #F1F3F5;
}
.listItem{
  height: 20%;
  background-color:#d2e0e0;
  margin-top: 20px;
}
.listCss{
  height: 100%;
  scrollbar-color: #8e8b8b;
  scrollbar-width: 50px;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/ucdrQWXKSnOArlTfwfc_Nw/zh-cn_image_0000002817426387.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004710Z&HW-CC-Expire=31536000000&HW-CC-Sign=C39B4F9FBB883788A93EC15C5D7416CEF606B9B7ACFCAC9705103430EFDF727A)

## 添加侧边索引栏

设置indexer属性为自定义索引时，索引栏会显示在列表右边界处，indexer属性设置为true，默认为字母索引表。

```html
<!-- xxx.hml -->
<div class="container">   
  <list class="listCss"  indexer="{{['#','1','2','3','4','5','6','7','8']}}" >  
    <list-item class="listItem"  section="#" ></list-item>   
  </list>
</div>
```

```css
/* xxx.css */
.container{
  flex-direction: column;
  background-color: #F1F3F5;
 }
.listCss{
  height: 100%;
  flex-direction: column;
  columns: 1
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/kef50jRxSu6dqKlb4G1KGw/zh-cn_image_0000002788466968.png?HW-CC-KV=V1&HW-CC-Date=20261114T004710Z&HW-CC-Expire=31536000000&HW-CC-Sign=F82B585D46CF3CF8BE326BBECB3449B1E1965D51C45B3852F18D888C3E42E1B7)

**说明** 

* indexer属性生效需要flex-direction属性配合设置为column，且columns属性设置为1。
* indexer可以自定义索引表，自定义时"#"必须要存在。

## 实现列表折叠和展开

为list组件添加groupcollapse和groupexpand事件实现列表的折叠和展开。

```html
<!-- xxx.hml -->
<div class="doc-page">
  <list style="width: 100%;" id="mylist">
    <list-item-group for="listgroup in list" id="{{listgroup.value}}" ongroupcollapse="collapse" ongroupexpand="expand">
      <list-item type="item" style="background-color:#FFF0F5;height:95px;">
        <div class="item-group-child">
          <text>One---{{listgroup.value}}</text>
        </div>
      </list-item>
      <list-item type="item" style="background-color: #87CEFA;height:145px;" primary="true">
        <div class="item-group-child">
          <text>Primary---{{listgroup.value}}</text>
        </div>
      </list-item>
    </list-item-group>
  </list>
</div>
```

```css
/* xxx.css */
.doc-page {
  flex-direction: column;
  background-color: #F1F3F5;
}
.list-item {
  margin-top:30px;
}
.top-list-item {
  width:100%;
  background-color:#D4F2E7;
}
.item-group-child {
  justify-content: center;
  align-items: center;
  width:100%;
}
```

```js
// xxx.js
import promptAction from '@ohos.promptAction';
export default {
  data: {
    direction: 'column',
    list: []
  },
  onInit() {
    this.list = []
    this.listAdd = []
    for (var i = 1; i <= 2; i++) {
      var dataItem = {
        value: 'GROUP' + i,
      };
        this.list.push(dataItem);
    }
  },
  collapse(e) {
    promptAction.showToast({
      message: 'Close ' + e.groupid
    })
  },
  expand(e) {
    promptAction.showToast({
    message: 'Open ' + e.groupid
    })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/mcIpN78xQMi-QZ0qCZB0OA/zh-cn_image_0000002817506455.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004710Z&HW-CC-Expire=31536000000&HW-CC-Sign=290B237F65DC151A851B0B77146507D2C7AE7370B61E8735AFA9EA9749819550)

**说明** 

* groupcollapse和groupexpand事件仅支持list-item-group组件使用。

## 场景示例

在本场景中，开发者可以根据字母索引表查找对应联系人。

```html
<!-- xxx.hml -->
<div class="doc-page"> 
  <text style="font-size: 35px; font-weight: 500; text-align: center; margin-top: 20px; margin-bottom: 20px;"> 
      <span>Contacts</span> 
  </text> 
  <list class="list" indexer="true"> 
    <list-item class="item" for="{{namelist}}" type="{{$item.section}}" section="{{$item.section}}"> 
      <div class="container"> 
        <div class="in-container"> 
          <text class="name">{{$item.name}}</text> 
          <text class="number">18888888888</text> 
        </div> 
      </div> 
    </list-item> 
    <list-item type="end" class="item"> 
      <div style="align-items:center;justify-content:center;width:750px;"> 
        <text style="text-align: center;">Total: 10</text> 
      </div> 
    </list-item> 
  </list> 
</div>
```

```css
/* xxx.css */
.doc-page {
  width: 100%;
  height: 100%;
  flex-direction: column;
  background-color: #F1F3F5;
}
.list {
  width: 100%;
  height: 90%;
  flex-grow: 1;
}
.item {
  height: 120px;
  padding-left: 10%;
  border-top: 1px solid #dcdcdc;
}
.name {
  color: #000000;
  font-size: 39px;
}
.number {
  color: black;
  font-size: 25px;
}
.container {
  flex-direction: row;
  align-items: center;
}
.in-container {
  flex-direction: column;
  justify-content: space-around;
}
```

```js
// xxx.js
export default {
   data: {
     namelist:[{
       name: 'Zoey',
       section:'Z'
     },{
       name: 'Quin',
       section:'Q'
     },{
       name:'Sam',
       section:'S'
     },{
       name:'Leo',
       section:'L'
     },{
       name:'Zach',
       section:'Z'
     },{
       name:'Wade',
       section:'W'
     },{
       name:'Zoe',
       section:'Z'
     },{
        name:'Warren',
        section:'W'
     },{
        name:'Kyle',
        section:'K'
     },{
       name:'Zaneta',
       section:'Z'
     }]
   },
   onInit() {
   }
 }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/24F1wtP-TVeC8jFVnm-drQ/zh-cn_image_0000002788307026.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004710Z&HW-CC-Expire=31536000000&HW-CC-Sign=DCB73968083B101420AE1555DE60B4270096FDC1CE34EC7D305F5F8758DE8E7F)
