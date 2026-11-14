---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-animate-component
title: 组件动画
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 动效开发指导 > JS动画 > 组件动画
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:11+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:06747a37ade1481f4d6a8e5a025b79e7756c0168d6b169c98d439fd54189822e
---

在组件上创建和运行动画的快捷方式。具体用法请参考[通用方法](../harmonyos-references/js-components-common-methods.md)。

## 获取动画对象

通过调用animate方法获得animation对象，animation对象支持动画属性、动画方法和动画事件。

```html
<!-- xxx.hml -->
<div class="container">
  <div id="content" class="box" onclick="Show"></div>
</div>
```

```css
/* xxx.css */
.container {
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
}
.box{
  width: 200px;
  height: 200px;
  background-color: #ff0000;
  margin-top: 30px;
}
```

```js
/* xxx.js */
export default {
    data: {
        animation: '',
        options: {},
        frames: {}
    },
    onInit() {
        this.options = {
            duration: 1500,
        };
        this.frames = [
            {
                width: 200, height: 200,
            },
            {
                width: 300, height: 300,
            }
        ];
    },
    Show() {
        this.animation = this.$element('content').animate(this.frames, this.options); // 获取动画对象
        this.animation.play();
    }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/Ilr8P9_hTQKuwp9j2BAKeQ/zh-cn_image_0000002788307086.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B7F9A82E1F3409FBD6881A6C93C581D7D36ABA9D7EE1AC59CEE984F29EB0268)

**说明** 

* 使用animate方法时必须传入Keyframes和Options参数。
* 多次调用animate方法时，采用replace策略，即最后一次调用时传入的参数生效。

## 设置动画参数

在获取动画对象后，通过设置参数Keyframes设置动画在组件上的样式。

```html
<!-- xxx.hml -->
<div class="container">
   <div id="content" class="box" onclick="Show"></div>
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
.box{
  width: 200px;
  height: 200px;
  background-color: #ff0000;
  margin-top: 30px;
}
```

```js
/* xxx.js */
export default {
  data: {
    animation: '',
    keyframes:{},
    options:{}
  },
  onInit() {
    this.options = {
      duration: 4000,
    }
    this.keyframes = [
    {
      transform: {
        translate: '-120px -0px',
        scale: 1,
        rotate: 0
        },
        transformOrigin: '100px 100px',
        offset: 0.0,
        width: 200,
        height: 200
      },
      {
        transform: {
          translate: '120px 0px',
          scale: 1.5,
          rotate: 90
          },
          transformOrigin: '100px 100px',
          offset: 1.0,
          width: 300,
          height: 300
      }
    ]
  },
  Show() {
    this.animation = this.$element('content').animate(this.keyframes, this.options)
    this.animation.play()
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/e_buMsfpSN67Hme_o9-RHg/zh-cn_image_0000002817426449.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=440608BD7CFF6787EEF822357933076EC60AD149E5FA0DD9F192F2188636B513)

**说明** 

* translate、scale和rotate的先后顺序会影响动画效果。
* transformOrigin只对scale和rotate起作用。

在获取动画对象后，通过设置参数Options来设置动画的属性。

```html
<!-- xxx.hml -->
<div class="container">
   <div id="content" class="box" onclick="Show"></div>
</div>
```

```css
/* xxx.css */
.container {
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
}
.box{
  width: 200px;
  height: 200px;
  background-color: #ff0000;
  margin-top: 30px;
}
```

```js
/* xxx.js */
export default {
    data: {
        animation: '',
        options: {},
        frames: {}
    },
    onInit() {
        this.options = {
            duration: 1500,
            easing: 'ease-in',
            delay: 5,
            iterations: 2,
            direction: 'normal',
        };
        this.frames = [
            {
                transform: {
                    translate: '-150px -0px'
                }
            },
            {
                transform: {
                    translate: '150px 0px'
                }
            }
        ];
    },
    Show() {
        this.animation = this.$element('content').animate(this.frames, this.options);
        this.animation.play();
    }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/l_4t14vWRGCcNIbJimmGhg/zh-cn_image_0000002788467030.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=125CDB6F7B2FD00C7C15FB5F92EFBC3A4DBAA5179FFE3107CC2DA25F18AA084C)

**说明** 

direction：指定动画的播放模式。

normal： 动画正向循环播放。

reverse： 动画反向循环播放。

alternate：动画交替循环播放，奇数次正向播放，偶数次反向播放。

alternate-reverse：动画反向交替循环播放，奇数次反向播放，偶数次正向播放。
