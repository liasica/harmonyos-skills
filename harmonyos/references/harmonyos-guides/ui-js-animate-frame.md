---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-animate-frame
title: 动画帧
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 动效开发指导 > JS动画 > 插值器动画 > 动画帧
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:07+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a2ce9e989b32cfdbb76365dd8f2abd437166e8de028a8a0f1b575b6033044d83
---

## 请求动画帧

请求动画帧时通过requestAnimationFrame函数逐帧回调，传入一个回调函数。

runframe在调用requestAnimationFrame时传入带有timestamp参数的回调函数step，将step中的timestamp赋予起始的startTime。当timestamp与startTime的差值小于规定的时间时，会再次调用requestAnimationFrame，最终动画将会停止。

```html
<!-- xxx.hml -->
<div class="container">
  <tabs onchange="changecontent">
    <tab-content>
      <div class="container">
        <stack style="width: 300px;height: 300px;margin-top: 100px;margin-bottom: 100px;">
          <canvas id="mycanvas" style="width: 100%;height: 100%;background-color: coral;">
          </canvas>
          <div style="width: 50px;height: 50px;border-radius: 25px;background-color: indigo;position: absolute;left: {{left}};top: {{top}};">
          </div>
        </stack>
        <button type="capsule" value="play" onclick="runframe"></button>
      </div>
    </tab-content>
  </tabs>
</div>
```

```css
/* xxx.css */
.container {
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}
button{
  width: 300px;
}
```

```js
// xxx.js
export default {
  data: {
    timer: null,
    left: 0,
    top: 0,
    flag: true,
    animation: null,
    startTime: 0,
  },
  onShow() {
    var test = this.$element("mycanvas");
    var ctx = test.getContext("2d");
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(300, 300);
    ctx.lineWidth = 5;
    ctx.strokeStyle = "red";
    ctx.stroke();
  },
  runframe() {
    this.left = 0;
    this.top = 0;
    this.flag = true;
    this.animation = requestAnimationFrame(this.step);
  },
  step(timestamp) {
    if (this.flag) {
      this.left += 5;
      this.top += 5;
      if (this.startTime == 0) {
        this.startTime = timestamp;
      }
      var elapsed = timestamp - this.startTime;
        if (elapsed < 500) {
          console.info('callback step timestamp: ' + timestamp);
          this.animation = requestAnimationFrame(this.step);
        }
      } else {
        this.left -= 5;
        this.top -= 5;
        this.animation = requestAnimationFrame(this.step);
      }
      if (this.left == 250 || this.left == 0) {
        this.flag = !this.flag;
     }
    },
    onDestroy() {
      cancelAnimationFrame(this.animation);
    }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/m_i8ryalQ_6TyNNlR_5PDw/zh-cn_image_0000002712244220.gif)

**说明** 

requestAnimationFrame函数在调用回调函数时在第一个参数位置传入timestamp时间戳，表示requestAnimationFrame开始去执行回调函数的时刻。

## 取消动画帧

通过cancelAnimationFrame函数取消逐帧回调，在调用cancelAnimationFrame函数时取消requestAnimationFrame函数的请求。

```html
<!-- xxx.hml -->
<div class="container">
  <tabs onchange="changecontent">
    <tab-content>
      <div class="container">
        <stack style="width: 300px;height: 300px;margin-top: 100px;margin-bottom: 100px;">
          <canvas id="mycanvas" style="width: 100%;height: 100%;background-color: coral;">
          </canvas>
          <div style="width: 50px;height: 50px;border-radius: 25px;background-color: indigo;position: absolute;left: {{left}};top: {{top}};">
          </div>
        </stack>
        <button type="capsule" value="play" onclick="runframe"></button>
      </div>
    </tab-content>
  </tabs>
</div>
```

```css
/* xxx.css */
.container {
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}
button{
  width: 300px;
}
```

```js
// xxx.js
export default {
  data: {
    timer: null,
    left: 0,
    top: 0,
    flag: true,
    animation: null
  },
  onShow() {
    var test = this.$element("mycanvas");
    var ctx = test.getContext("2d");
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(300, 300);
    ctx.lineWidth = 5;
    ctx.strokeStyle = "red";
    ctx.stroke();
  },
  runframe() {
    this.left = 0;
    this.top = 0;
    this.flag = true;
    this.animation = requestAnimationFrame(this.step);
  },
  step(timestamp) {
    if (this.flag) {
      this.left += 5;
      this.top += 5;
      this.animation = requestAnimationFrame(this.step);
    } else {
      this.left -= 5;
      this.top -= 5;
      this.animation = requestAnimationFrame(this.step);
    }
    if (this.left == 250 || this.left == 0) {
      this.flag = !this.flag;
    }
  },
  onDestroy() {
    cancelAnimationFrame(this.animation);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/Z7yxw3AIQkCyg33cOdNbsA/zh-cn_image_0000002742003173.gif)

**说明** 

在调用该函数时需传入一个具有标识id的参数。
