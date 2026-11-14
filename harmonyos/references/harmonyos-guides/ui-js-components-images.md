---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-images
title: image开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > image开发指导
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:10+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:633550a83536e8e4e5e95ef1d0aade37f24b5a29c554f7c8d8da7d807e9cd300
---

image是图片组件，用来渲染展示图片。具体用法请参考[image](../harmonyos-references/js-components-basic-image.md)组件。

## 创建image组件

在pages/index目录下的hml文件中创建一个image组件。

```html
<!-- index.hml -->
<div class="container">
  <image style="height: 30%;" src="common/images/bg-tv.jpg"> </image>
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/HFHYiVfZRQuA5V9siG3vFw/zh-cn_image_0000002817426409.png?HW-CC-KV=V1&HW-CC-Date=20261114T004532Z&HW-CC-Expire=31536000000&HW-CC-Sign=33CDB483AB73BD0C5D5356D419D47AAC423465DEC99F6F21B9A25CD53C074028)

## 设置image样式

通过设置width、height和object-fit属性定义图片的宽、高和缩放样式。

```html
<!-- index.hml -->
<div class="container">
  <image src="common/images/bg-tv.jpg"> </image>
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
  background-color:#F1F3F5;
}
image{
  width: 80%;
  height: 500px;
  border: 5px solid saddlebrown;
  border-radius: 20px;
  object-fit: contain;
  match-text-direction:true;
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/6ni3Rq96RzWncRibsj3-rA/zh-cn_image_0000002788466990.png?HW-CC-KV=V1&HW-CC-Date=20261114T004532Z&HW-CC-Expire=31536000000&HW-CC-Sign=B9D9F462C937EBA26084DEE2BB3BC1DFE656CC18C615CD9779CF8AA9E436BBF2)

## 加载图片

图片成功加载时触发complete事件，返回加载的图源尺寸。加载失败则触发error事件，打印图片加载失败。

```html
<!-- index.hml -->
<div class="container" >
  <div>
    <image src="common/images/bg-tv.jpg" oncomplete="imageComplete(1)" onerror="imageError(1)"> </image>
  </div>
  <div>
    <image src="common/images/bg-tv1.jpg" oncomplete="imageComplete(2)" onerror="imageError(2)"> </image>
  </div>
</div>
```

```css
/* xxx.css */
.container{
  width: 100%;
  height: 100%;
  flex-direction: column;
  justify-content: center;
  align-self: center;
  background-color: #F1F3F5;
}
.container div{
  margin-left: 10%;
  width: 80%;
  height: 300px;
  margin-bottom: 40px;
}
```

```js
// index.js
import promptAction from '@ohos.promptAction';
export default {
  imageComplete(i,e){
    promptAction.showToast({
      message: "image "+i+"'s width"+ e.width+"----image "+i+"'s height"+e.height,
      duration: 3000,
    })
  },
  imageError(i,e){
    setTimeout(()=>{
      promptAction.showToast({
        message: "Failed to load image "+i+".",
        duration: 3000,
      })
    },3000)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/IYqprL7AS0Shb_mYdkSLyg/zh-cn_image_0000002817506477.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004532Z&HW-CC-Expire=31536000000&HW-CC-Sign=004C3975BAABC4525E401EDFBF35A0252D0C43CDAE20C0FCBFCCAC78A50E7536)

## 场景示例

在本场景中，开发者长按图片后将慢慢隐藏图片，当完全隐藏后再重新显示原始图片。定时器setInterval每隔一段时间改变图片透明度，实现慢慢隐藏的效果，当透明度为0时清除定时器，设置透明度为1。

```html
<!-- index.hml -->
<div class="page-container">
  <div class="content">
    <div class="image-container">
      <image class="testimage" src="{{testuri}}" style="opacity:{{imageopacity}};" onlongpress="changeopacity"> </image>
    </div>
    <div class="text-container">
      <text style="font-size: 37px;font-weight:bold;color:orange;text-align: center;width: 100%;">Touch and hold the image</text>
    </div>
  </div>
</div>
```

```css
/* xxx.css */
.page-container {
  width: 100%;
  height: 100%;
  flex-direction:column;
  align-self: center;
  justify-content: center;
  background-color:#F1F3F5;
  background-color: #F1F3F5;
}
.content{
  flex-direction:column;
}
.image-container {
  width: 100%;
  height: 300px;
  align-items: center;
  justify-content: center;
}
.text-container {
  margin-top:50px;
  width: 100%;
  height: 60px;
  flex-direction: row;
  justify-content: space-between;
}
.testimage {
  width: 100%;  height: 400px;
  object-fit: scale-down;
  border-radius: 20px;
}
```

```js
// index.js
import promptAction from '@ohos.promptAction';
export default {
  data: {
    testuri: 'common/images/bg-tv.jpg',
    imageopacity:1,
    timer: null
  },
  changeopacity: function () {
    promptAction.showToast({
      message: 'Touch and hold the image.'
    })
    var opval = this.imageopacity * 20
    clearInterval(this.timer);
    this.timer = setInterval(()=>{
      opval--;
      this.imageopacity = opval / 20
      if (opval===0) {
        clearInterval(this.timer)
        this.imageopacity = 1
      }
    },100);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/yv2kVR3gQc6ctWlsdGBvKw/zh-cn_image_0000002788307048.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004532Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A93572A225C05BACDFA4777EABFE67A3E3EF6A20BF20E3EDBA1EA02C4BA0AB0)
