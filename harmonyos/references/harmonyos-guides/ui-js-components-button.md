---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-button
title: button开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > button开发指导
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:06+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:ee6b43e65b9a177a2fcf59b0ea1b41bcb62878b6d7a5f385973170a2c09aa5af
---

button是按钮组件，其类型包括胶囊按钮、圆形按钮、文本按钮、弧形按钮、下载按钮。具体用法请参考[button API](../harmonyos-references/js-components-basic-button.md)。

## 创建button组件

在pages/index目录下的hml文件中创建一个button组件。

```html
<!-- xxx.hml -->
<div class="container">       
  <button  type="capsule" value="Capsule button"></button>
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/4rBMfYcLSXeq0vWigcHS3w/zh-cn_image_0000002712244174.png)

## 设置button类型

通过设置button的type属性来选择按钮类型，如定义button为圆形按钮、文本按钮等。

```html
<!-- xxx.hml -->
<div class="container">    
  <button class="circle" type="circle" >+</button>
  <button class="text" type="text"> button</button>
</div>
```

```css
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  background-color: #F1F3F5;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.circle {
  font-size: 120px;
  background-color: blue;
  radius: 72px;
}
.text {
  margin-top: 30px;
  text-color: white;
  font-size: 30px;
  font-style: normal;
  background-color: blue;
  width: 50%;
  height: 100px;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/RAaX6obGS3aDrKcvJOOmKg/zh-cn_image_0000002742122805.png)

**说明** 

* button组件使用的icon图标如果来自云端路径，需要添加网络访问权限 ohos.permission.INTERNET。

如果需要添加ohos.permission.INTERNET权限，则在resources文件夹下的config.json文件里进行权限配置。

```json
{
  "module": {
    "reqPermissions": [{
      "name": "ohos.permission.INTERNET"
    }]
  }
}
```

## 显示下载进度

为button组件添加setProgress方法，来实时显示下载进度条的进度。

```html
<!-- xxx.hml -->
<div class="container">
  <button class="button download" type="download" id="download-btn" onclick="setProgress">{{downloadText}}</button>
</div>
```

```css
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  background-color: #F1F3F5;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.download {
  width: 280px;
  text-color: white;
  background-color: #007dff;
}
```

```js
// xxx.js
export default {
  data: {
    percent: 0,
    downloadText: "Download",
    isPaused: true,
    intervalId : null,
  },
  start(){
    this.intervalId = setInterval(()=>{
      if(this.percent <100){
        this.percent += 1;
        this.downloadText = this.percent+ "%";
       } else{
         this.getUIContext().getPromptAction().showToast({
            message: "Download succeeded."
         })
         this.paused()
         this.downloadText = "Download";
         this.percent = 0;
         this.isPaused = true;
       }
    },100)
  },
  paused(){
    clearInterval(this.intervalId);
    this.intervalId = null;
  },
 setProgress(e) {
    if(this.isPaused){
      this.getUIContext().getPromptAction().showToast({
        message: "Started Downloading"
      })
      this.start();
      this.isPaused = false;
    }else{
      this.getUIContext().getPromptAction().showToast({
        message: "Paused."
      })
      this.paused();
      this.isPaused = true;
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/Lli6g1y6S8CMJ_i7FOeWAQ/zh-cn_image_0000002742003127.gif)

**说明** 

setProgress方法只支持button的类型为download。

## 场景示例

在本场景中，开发者可根据输入的文本内容进行input类型切换。

```html
<!-- xxx.hml -->
<div class="container">
  <div class="input-item">
    <input class="input-text" id="change" type="{{mytype}}"  placeholder="{{myholder}}"
      style="background-color:{{mystyle1}};
      placeholder-color:{{mystyle2}};flex-grow:{{myflex}};" name="{{myname}}" value="{{myvalue}}"></input>
  </div>
  <div class="input-item">
    <div class="doc-row">
      <input type="button" class="select-button color-3" value="text" onclick="changetype3"></input>
      <input type="button" class="select-button color-3" value="data" onclick="changetype4"></input>
    </div>
  </div>
</div>
```

```css
/* xxx.css */
.container {
  flex-direction: column;
  align-items: center;
  background-color: #F1F3F5;
}
.input-item {
  margin-bottom: 80px;
  flex-direction: column;
}
.doc-row {
  justify-content: center;
  margin-left: 30px;
  margin-right: 30px;
}
.input-text {
  height: 80px;
  line-height: 80px;
  padding-left: 30px;
  padding-right: 30px;
  margin-left: 30px;
  margin-right: 30px;
  margin-top:100px;
  border: 3px solid;
  border-color: #999999;
  font-size: 30px;
  background-color: #ffffff;
  font-weight: 400;
}
.select-button {
  width: 35%;
  text-align: center;
  height: 70px;
  padding-top: 10px;
  padding-bottom: 10px;
  margin-top: 30px;
  font-size: 30px;
  color: #ffffff;
}
.color-3 {
  background-color: #0598db;
}
```

```js
// xxx.js
export default {
  data: {
    myflex: '',
    myholder: 'Enter text.',
    myname: '',
    mystyle1: "#ffffff",
    mystyle2: "#ff0000",
    mytype: 'text',
    myvalue: '',
  },
  onInit() {
  },
  changetype3() {
    this.myflex = '';
    this.myholder = 'Enter text.';
    this.myname = '';
    this.mystyle1 = "#ffffff";
    this.mystyle2 = "#FF0000";
    this.mytype = 'text';
    this.myvalue = '';
  },
  changetype4() {
    this.myflex = '';
    this.myholder = 'Enter a date.';
    this.myname = '';
    this.mystyle1 = "#ffffff";
    this.mystyle2 = "#FF0000";
    this.mytype = 'date';
    this.myvalue = '';
  },
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/7pN8CrmQRv6849JFDT-_Ww/zh-cn_image_0000002712404140.gif)
