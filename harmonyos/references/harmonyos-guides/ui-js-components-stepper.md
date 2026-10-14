---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-stepper
title: stepper开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 容器组件 > stepper开发指导
category: harmonyos-guides
scraped_at: 2026-10-15T07:04:14+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:8c51b87868c529b36c77ffb70597cce3992b966f7a8cc990d5d41a519c7138e6
---

当一个任务需要多个步骤时，可以使用stepper组件展示当前进展。具体用法请参考[stepper API](../harmonyos-references/js-components-container-stepper.md)。

## 创建stepper组件

在pages/index目录下的hml文件中创建一个stepper组件。

```html
<!-- xxx.hml -->
<div class="container"> 
 <stepper>    
   <stepper-item>     
     <text>Step 1</text>
   </stepper-item> 
   <stepper-item>     
     <text>Step 2</text>
   </stepper-item> 
 </stepper> 
</div>
```

```css
/* xxx.css */
.container {
  width:100%;
  height:100%;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #F1F3F5;
}
text{
  width: 100%;
  height: 100%;
  text-align: center;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/wGyplgKrTiOLIIfCHvfTqg/zh-cn_image_0000002762340010.gif)

## 设置index和label属性

页面默认显示索引值为index的步骤。

```html
<!-- xxx.hml -->
<div class="container"> 
 <stepper index="2">    
   <stepper-item>     
     <text>stepper-item1</text>
   </stepper-item> 
   <stepper-item>     
     <text>stepper-item2</text>
   </stepper-item> 
   <stepper-item>     
     <text>stepper-item3</text>
   </stepper-item> 
  </stepper> 
</div>
```

```css
/* xxx.css */
.container {
  width:100%;
  height:100%;
  flex-direction: column;
  background-color: #F1F3F5;
}
text{
  width: 100%;
  height: 100%;
  text-align: center;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/IastT6hmT5qFuzExwJiwgQ/zh-cn_image_0000002791858805.gif)

通过设置label属性，自定义stepper-item的提示按钮。

```html
<!-- xxx.hml -->
<div class="container"> 
 <stepper index="1">    
   <stepper-item label="{{label_1}}">     
     <text>stepper-item1</text>
   </stepper-item> 
   <stepper-item label="{{label_2}}">     
     <text>stepper-item2</text>
   </stepper-item> 
   <stepper-item label="{{label_3}}">     
     <text>stepper-item3</text>
   </stepper-item>
   <stepper-item>     
     <text>stepper-item4</text>
   </stepper-item> 
 </stepper> 
</div>
```

```css
/* xxx.css */
.container {
  width:100%;
  height:100%;
  flex-direction: column;
  background-color: #F1F3F5;
}
text{
  width: 100%;
  height: 100%;
  text-align: center;
}
```

```js
// xxx.js
export default {
  data: {
    label_1:{
      nextLabel: 'NEXT',
      status: 'normal'
    },
    label_2:{
      prevLabel: 'BACK',
      nextLabel: 'NEXT',
      status: 'normal'
    },
    label_3:{
      prevLabel: 'BACK',
      nextLabel: 'END',
      status: 'disabled'
    },
  },
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/B0PU4eM3Smy3rsunxGKAnw/zh-cn_image_0000002762499930.gif)

## 设置样式

stepper组件默认填充父容器，通过border和background-color设置边框、背景色。

```html
<!-- xxx.hml -->
<div class="container" > 
  <div class="stepperContent">
    <stepper class="stepperClass">    
      <stepper-item>     
        <text>stepper-item1</text>
      </stepper-item> 
    </stepper> 
  </div>
</div>
```

```css
/* xxx.css */
.container {
  width:100%;
  height:100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color:#F1F3F5;
}
.stepperContent{
  width: 300px;
  height: 300px;
}
.stepperClass{
  border:1px solid silver ;
  background-color: white;
}
text{
  width: 100%;
  height: 100%;
  text-align: center;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/jJ43f3pzT2WYpPdGYVGtKw/zh-cn_image_0000002791738593.png)

## 添加事件

stepper分别添加finish，change，next，back，skip事件。

* 当change与next或back同时存在时，会先执行next或back事件再去执行change事件。
* 重新设置index属性值时要先清除index的值再重新设置，否则检测不到值的改变。

```html
<!-- xxx.hml -->
<div class="container"  style="background-color:#F1F3F5;">
  <div >
    <stepper onfinish="stepperFinish" onchange="stepperChange" onnext="stepperNext" onback="stepperBack" onskip="stepperSkip" id="stepperId" index="{{index}}">
      <stepper-item>
        <text>stepper-item1</text>
        <button value="skip" onclick="skipClick"></button>
      </stepper-item>
      <stepper-item>
         <text>stepper-item2</text>
         <button value="skip" onclick="skipClick"></button>
      </stepper-item>
      <stepper-item>
        <text>stepper-item3</text>
      </stepper-item>
    </stepper>
  </div>
</div>
```

```css
/* xxx.css */
.container {
  width:100%;
  height:100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
stepper-item{
  width: 100%;
  flex-direction: column;
  align-self: center;
  justify-content: center;
}
text{
  margin-top: 45%;
  justify-content: center;
  align-self: center;
  margin-bottom: 50px;
}
button{
  width: 80%;
  height: 60px;
  margin-top: 20px;
}
```

```js
// xxx.js
import promptAction from '@ohos.promptAction';
export default {
  data: {
    index:0,
  },
   stepperSkip(){
    this.index=2;
  },
   skipClick(){
    this.$element('stepperId').setNextButtonStatus({status: 'skip', label: 'SKIP'});
  },
  stepperFinish(){
    promptAction.showToast({
      message: 'All Finished'
    })
  },
  stepperChange(e){
    console.info("stepperChange"+e.index)
    promptAction.showToast({
      // index表示当前步骤的序号
      message: 'Previous step: '+e.prevIndex+"-------Current step:"+e.index
    })
  },
  stepperNext(e){
    console.info("stepperNext"+e.index)
    promptAction.showToast({
      // pendingIndex表示将要跳转的序号
      message: 'Current step:'+e.index+"-------Next step:"+e.pendingIndex
    })
    var index = {pendingIndex:e.pendingIndex }
    return index;
  },
  stepperBack(e){
    console.info("stepperBack"+e.index)
    var index = {pendingIndex: e.pendingIndex }
    return index;
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/njG-egPZSPmFHrT0u7lFBg/zh-cn_image_0000002762340012.gif)
