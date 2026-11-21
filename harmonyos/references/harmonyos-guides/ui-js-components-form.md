---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-form
title: form开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 容器组件 > form开发指导
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:13+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:559968f46ccecdd8a39609b3cd0e07eff35a7c269ed083edb0fa8c268a945f66
---

form是一个表单容器，支持容器内[Input](../harmonyos-references/js-components-basic-input.md)组件内容的提交和重置。具体用法请参考[form API](../harmonyos-references/js-components-container-form.md)。

## 创建form组件

在pages/index目录下的hml文件中创建一个form组件。

```html
<!-- xxx.hml -->
<div class="container">
  <form style="width: 100%; height: 20%">  
    <input type="text" style="width:80%"></input>
  </form>
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
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/AJW_PHiSTzOieEXLxth4UQ/zh-cn_image_0000002792877008.png?HW-CC-KV=V1&HW-CC-Date=20261121T010949Z&HW-CC-Expire=31536000000&HW-CC-Sign=B7E3BC0B44D3D271B64941DBC827BCE5832C45CC9A2109F3741F4030592F305D)

## 实现表单缩放

为form组件添加click-effect属性，实现点击表单后的缩放效果，click-effect枚举值请参考[通用属性](../harmonyos-references/js-components-common-attributes.md)。

```html
<!-- xxx.hml -->
<div class="container">
  <form  id="formId" class="formClass" click-effect="spring-large">
    <input type="text"></input>  
  </form>
</div>
```

## 设置form样式

通过为form添加border属性，来设置表单的边框。

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
.formClass{
  width: 80%;
  height: 100px;
  padding: 10px;
  border: 1px solid #cccccc;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/sKOaPv99T8uf401kkoFzkQ/zh-cn_image_0000002821836915.gif?HW-CC-KV=V1&HW-CC-Date=20261121T010949Z&HW-CC-Expire=31536000000&HW-CC-Sign=D87DF0EF9D82399FAFC78178D2194509C85FFD69A1F699973C642253D4B87BB7)

## 添加响应事件

为form组件添加submit和reset事件，来提交表单内容或重置表单选项。

```html
<!-- xxx.hml -->
<div class="container">
  <form onsubmit='onSubmit' onreset='onReset' class="form">
    <div style="width: 100%;justify-content: center;">
      <label>Option 1</label>
      <input type='radio' name='radioGroup' value='radio1'></input>
      <label>Option 2</label>
      <input type='radio' name='radioGroup' value='radio2'></input>
    </div>
    <div style="width: 100%;justify-content: center; margin-top: 20px">
      <input type="submit" value="Submit" style="width:120px; margin-right:20px;" >   
      </input>
      <input type="reset" value="Reset" style="width:120px;"></input>
    </div>
  </form>
</div>
```

```css
/* index.css */
.container{
  width: 100%;
  height: 100%;
  flex-direction: column;
  justify-items: center;
  align-items: center;
  background-color: #F1F3F5;
}
.form{
  width: 100%;
  height: 30%;
  margin-top: 40%;
  flex-direction: column;
  justify-items: center;
  align-items: center;
}
```

```js
// xxx.js
import promptAction from '@ohos.promptAction';
export default{
  onSubmit(result) {
    promptAction.showToast({
      message: result.value.radioGroup
    })
  },
  onReset() {
    promptAction.showToast({
      message: 'Reset All'
    })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/a18KfUKMRrWjqAx3fQgj9A/zh-cn_image_0000002821756917.gif?HW-CC-KV=V1&HW-CC-Date=20261121T010949Z&HW-CC-Expire=31536000000&HW-CC-Sign=26FCC7B3532BAFDFDB0BB744B41B6727122CF800897A36896BF47C716925BCAE)

## 场景示例

在本场景中，开发者可以选择相应选项并提交或重置数据。

创建[Input](../harmonyos-references/js-components-basic-input.md)组件，分别设置type属性为checkbox（多选框）和radio（单选框），再使用form组件的onsubmit和onreset事件实现表单数据的提交与重置。

```html
<!-- xxx.hml -->
<div class="container">
   <form onsubmit="formSubmit" onreset="formReset">
 <text style="font-size: 30px; margin-bottom: 20px; margin-top: 100px;">
      <span > Form </span>
  </text>
    <div style="flex-direction: column;width: 90%;padding: 30px 0px;">
     <text class="txt">Select 1 or more options</text>
      <div style="width: 90%;height: 150px;align-items: center;justify-content: space-around;">
        <label target="checkbox1">Option 1</label>
        <input id="checkbox1" type="checkbox" name="checkbox1"></input>
        <label target="checkbox2">Option 2</label>
        <input id="checkbox2" type="checkbox" name="checkbox2"></input>
       </div>
       <divider style="margin: 20px 0px;color: pink;height: 5px;"></divider>
       <text class="txt">Select 1 option</text>
       <div style="width: 90%;height: 150px;align-items: center;justify-content: space-around;">
         <label target="radio1">Option 1</label>
         <input id="radio1" type="radio" name="myradio"></input>
         <label target="radio2">Option 2</label>
         <input id="radio2" type="radio" name="myradio"></input>
       </div>
       <divider style="margin: 20px 0px;color: pink;height: 5px;"></divider>
       <text class="txt">Text box</text>
       <input type="text" placeholder="Enter content." style="margin-top: 50px;"></input>
       <div style="width: 90%;align-items: center;justify-content: space-between;margin: 40px;">
         <input type="submit">Submit</input>
         <input type="reset">Reset</input>
       </div>
    </div>
  </form>
</div>
```

```css
/* index.css */
.container {
  width: 100%;
  height: 100%;
  flex-direction:column;
  align-items:center;
  background-color:#F1F3F5;
}
.txt {
  font-size:33px;
  font-weight:bold;
  color:darkgray;
}
label{
  font-size: 20px;
}
```

```js
// xxx.js
import promptAction from '@ohos.promptAction';
export default {
  formSubmit() {
    promptAction.showToast({
      message: 'Submitted.'
    })
  },
  formReset() {
    promptAction.showToast({
      message: 'Reset.'
    })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/TQXo71a9Q26jrhRYsWd7wA/zh-cn_image_0000002793036980.gif?HW-CC-KV=V1&HW-CC-Date=20261121T010949Z&HW-CC-Expire=31536000000&HW-CC-Sign=554452D43A8718E0CA52894430C9CB3F275627A354F73526D1DD7973423C6179)
