---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-input
title: input开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > input开发指导
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:06+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:60c7bf01c92a317c2b84bf773edc64c5979275a29d98a2f0756cc98297c64684
---

input是交互式组件，用于接收用户数据。其类型可设置为日期、多选框和按钮等。具体用法请参考[input API](../harmonyos-references/js-components-basic-input.md)。

## 创建input组件

在pages/index目录下的hml文件中创建一个input组件。

```html
<!-- xxx.hml -->
<div class="container">       
  <input type="text">             
     Please enter the content
  </input>
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
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/xZK28zvZRrKUnY9pB49xOg/zh-cn_image_0000002742123085.png)

## 设置input类型

通过设置type属性来定义input类型，如将input设置为button、date等。

```html
<!-- xxx.hml -->
<div class="container">
  <div class="div-button">
    <dialog class="dialogClass" id="dialogId">
      <div class="content">
        <text>this is a dialog</text>
      </div>
    </dialog>
    <input class="button" type="button" value="click" onclick="btnclick"></input>
  </div>
  <div class="content">
    <input onchange="checkboxOnChange" checked="true" type="checkbox"></input>
  </div>
  <div class="content">
    <input type="date" class="flex" placeholder="Enter date"></input>
  </div>
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
  background-color: #F1F3F5 ;
}
.div-button {
  flex-direction: column;
  align-items: center;
}
.dialogClass{
  width:80%;
  height: 200px;
}
.button {
  margin-top: 30px;
  width: 50%;
}
.content{
  width: 90%;
  height: 150px;
  align-items: center;
  justify-content: center;
}
.flex {
  width: 80%;
  margin-bottom:40px;
}
```

```js
// xxx.js
export default {
  btnclick(){
    this.$element('dialogId').show()
  },
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/su4q_zD0RcyCWGv0-DcGDQ/zh-cn_image_0000002712244172.gif)

**说明** 

仅当input类型为checkbox或radio时，当前组件选中的属性是checked才生效，默认值为false。

## 事件绑定

向input组件添加translate事件。

```html
<!-- xxx.hml -->
<div class="content">
    <text style="margin-left: -7px;">
        <span>Enter text and then touch and hold what you've entered</span>
    </text>
    <input class="input" type="text" ontranslate="translate" placeholder="translate"> </input>
</div>
```

```css
/* xxx.css */
.content {
  width: 100%;
  height: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #F1F3F5;
}
.input {
  margin-top: 50px;
  width: 60%;
  placeholder-color: gray;
}
text{
  width:100%;
  font-size:25px;
  text-align:center;
}
```

```js
// xxx.js
import promptAction from '@ohos.promptAction'

export default {
    translate(e) {
        promptAction.showToast({
            message: e.value,
            duration: 3000,
        });
    }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/xuOwH1AdRV-bXqkbZXFn0g/zh-cn_image_0000002742003125.gif)

## 设置输入提示

通过对input组件添加showError方法来提示输入的错误原因。

```html
<!-- xxx.hml -->
<div class="content">
  <input id="input" class="input" type="text"  maxlength="20" placeholder="Please input text" onchange="change">
  </input>
  <input class="button" type="button" value="Submit" onclick="buttonClick"></input>
</div>
```

```css
/* xxx.css */
.content {
  width: 100%;
  height: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #F1F3F5;
}
.input {
  width: 80%;
  placeholder-color: gray;
}
.button {
  width: 30%;
  margin-top: 50px;
}
```

```js
// xxx.js
import promptAction from '@ohos.promptAction'
 export default {
   data:{
     value:'',
   },
   change(e){
     this.value = e.value;
     promptAction.showToast({
     message: "value: " + this.value,
       duration: 3000,
      });
   },
   buttonClick(e){
     if(this.value.length > 6){
       this.$element("input").showError({
         error:  'Up to 6 characters are allowed.'
       });
      }else if(this.value.length == 0){
        this.$element("input").showError({
          error:this.value + 'This field cannot be left empty.'
        });
      }else{
        promptAction.showToast({
          message: "success "
        });
      }
   },
 }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/wLto4HVrRma8ZtZRX3GpLQ/zh-cn_image_0000002712404138.gif)

**说明** 

showError方法仅在input类型为text、email、date、time、number和password时生效。

## 场景示例

根据场景选择不同类型的input输入框，完成信息录入。

```html
<!-- xxx.hml -->
<div class="container">    
  <div class="label-item"> 
    <label>memorandum</label>   
  </div>    
  <div class="label-item">        
    <label class="lab" target="input1">content:</label>        
    <input class="flex" id="input1" placeholder="Enter content" />    
  </div>    
  <div class="label-item">        
    <label class="lab" target="input3">date:</label>        
    <input class="flex" id="input3" type="date" placeholder="Enter date" />    
  </div>    
  <div class="label-item">        
    <label class="lab" target="input4">time:</label>        
    <input class="flex" id="input4" type="time" placeholder="Enter time" />    
  </div>   
  <div class="label-item">        
    <label class="lab" target="checkbox1">Complete:</label>        
    <input class="flex" type="checkbox" id="checkbox1" style="width: 100px;height: 100px;" />    
  </div>    
  <div class="label-item">        
    <input class="flex" type="button" id="button" value="save" onclick="btnclick"/>    
  </div>
</div>
```

```css
/* xxx.css */
.container {
  flex-direction: column;
  background-color: #F1F3F5;
}
.label-item {
  align-items: center;
  border-bottom-width: 1px;border-color: #dddddd;
}
.lab {
  width: 400px;}
label {
  padding: 30px;
  font-size: 30px;
  width: 320px;
  font-family: serif;
  color: #9370d8;
  font-weight: bold;
}
.flex {
  flex: 1;
}
.textareaPadding {
  padding-left: 100px;
}
```

```js
// xxx.js
import promptAction from '@ohos.promptAction';
export default {
  data: {
  },
  onInit() {
  },
  btnclick(e) {
    promptAction.showToast({
      message:'Saved successfully!'
    })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/C3QRGVNYRUOjZrexs55m3w/zh-cn_image_0000002742123087.gif)
