---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-animate-component
title: 组件动画
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 动效开发指导 > JS动画 > 组件动画
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:14+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:0ef466d328b7499b4e04cf645d5e8a595487afb03dcbe60560a80f9e429e491c
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/XTSPu4zUTse6ha7JiqT3qA/zh-cn_image_0000002792877066.gif?HW-CC-KV=V1&HW-CC-Date=20261121T010950Z&HW-CC-Expire=31536000000&HW-CC-Sign=2E1ABCD8192DFDF8D8CCC088AED6EAACF5808279E458DB38233151D268CAD0E5)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/fJH50OjyQ_qvdbCAgI74MQ/zh-cn_image_0000002821836973.gif?HW-CC-KV=V1&HW-CC-Date=20261121T010950Z&HW-CC-Expire=31536000000&HW-CC-Sign=37361C1069F2C92512C9F239464B1F87B6B896D856E42C11839CFCFD4FC094E8)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/zwk6pO8RRa2hPCVi4BrS2w/zh-cn_image_0000002821756975.gif?HW-CC-KV=V1&HW-CC-Date=20261121T010950Z&HW-CC-Expire=31536000000&HW-CC-Sign=4E25F33B6C7BE69DC25AEA21BC272AD4F42A390C627C43C4CFE5F88215D927FC)

**说明** 

direction：指定动画的播放模式。

normal： 动画正向循环播放。

reverse： 动画反向循环播放。

alternate：动画交替循环播放，奇数次正向播放，偶数次反向播放。

alternate-reverse：动画反向交替循环播放，奇数次反向播放，偶数次正向播放。
