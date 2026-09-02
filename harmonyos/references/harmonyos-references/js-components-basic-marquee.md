---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-marquee
title: marquee
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 基础组件 > marquee
category: harmonyos-references
scraped_at: 2026-09-02T15:01:12+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:9aa297db83aa8ba5cb71e64ba5f7bec203fe123bdde1d601d2bc9cda9e038c3c
---

**说明** 

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

从API version 6开始，仅当文本内容宽度超过跑马灯组件宽度时滚动。

跑马灯组件，用于展示一段单行滚动的文字。

## 权限列表

无

## 子组件

不支持。

## 属性

除支持[通用属性](js-components-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| scrollamount | number | 6 | 否 | 跑马灯每次滚动时移动的步长。 |
| loop | number | -1 | 否 | 跑马灯滚动的次数。如果未指定，则默认值为-1，当该值小于等于零时表示跑马灯将连续滚动。 |
| direction | string | left | 否 | 设置跑马灯的文字滚动方向，可选值为left和right。 |

## 样式

除支持[通用样式](js-components-common-styles.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| color | <color> | #e5000000 | 否 | 设置跑马灯中文字的文本颜色。 |
| font-size | <length> | 37.5px | 否 | 设置跑马灯中文字的文本尺寸。 |
| allow-scale | boolean | true | 否 | 设置跑马灯中文字的文本尺寸是否跟随系统设置字体缩放尺寸进行放大缩小。true表示跟随系统放大缩小，false表示不跟随系统放大缩小。  如果在config描述文件中针对ability配置了fontSize的config-changes标签，则应用不会重启而直接生效。 |
| font-weight | number | string | normal | 否 | 设置跑马灯中文字的字体的粗细，见[text组件font-weight的样式属性](js-components-basic-text.md#样式)。 |
| font-family | string | sans-serif | 否 | 设置跑马灯中文字的字体列表，用逗号分隔，每个字体用字体名或者字体族名设置。列表中第一个系统中存在的或者通过[自定义字体](js-components-common-customizing-font.md)指定的字体，会被选中作为文本的字体。 |

## 事件

除支持[通用事件](js-components-common-events.md)外，还支持如下事件：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| bounce | - | 当文本滚动到末尾时触发该事件。 |
| finish | - | 当完成滚动次数时触发该事件。需要在 loop 属性值大于 0 时触发。 |
| start | - | 当文本滚动开始时触发该事件。 |

## 方法

除支持[通用方法](js-components-common-methods.md)外，还支持如下方法：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| start | - | 开始滚动。 |
| stop | - | 停止滚动。 |

## 示例

```html
<!-- xxx.hml -->
<div class="tutorial-page">
    <div class="myMarquee">
        <marquee  style="color: {{color1}}" loop="{{loopVal}}" scrollamount="{{scroll}}" direction="{{isLeft}}" class="marqueeText"
                  id="testMarquee" onfinish="setFinish">
            Life is a journey, not the destination.
        </marquee>
    </div>
    <div style="width: 600px;height: 150px;flex-direction: row;justify-content: space-around;">
        <button onclick="makeStart"  value="start"></button>
        <button onclick="makeStop" value="stop"></button>
    </div>
</div>
```

```css
/* xxx.css */
.tutorial-page {
  width: 750px;
  height: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.marqueeText {
  font-size: 40px;
}
.myMarquee {
  margin-top: 20px;
  width:100%;
  height: 100px;
  margin-left: 50px;
  margin-right: 50px;
  border: 1px solid #dc0f27;
  border-radius: 15px;
  align-items: center;
}
button{
  width: 200px;
  height: 80px;
  margin-top: 100px;
}
```

```js
// xxx.js
export default {
    private: {
        loopVal: 1,
        scroll: 8,
        color1: 'red',
        isLeft: 'left',
        r: 255,
        g: 0,
        b: 0
    },
    onInit(){
    },
    setFinish(e) {
        this.loopVal=  this.loopVal + 1,
        this.r = Math.floor(Math.random()*255),
        this.g = Math.floor(Math.random()*255),
        this.b = Math.floor(Math.random()*255),
        this.color1 = 'rgba('+ this.r +','+ this.g +','+ this.b +',0.8)',
        this.$element('testMarquee').start(),
        this.loopVal=  this.loopVal - 1
    },
    makeStart(e) {
        this.$element('testMarquee').start()
    },
    makeStop(e) {
        this.$element('testMarquee').stop()
    }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/TFaMdMBzRYu62YY-W9Sbvw/zh-cn_image_0000002706836384.gif)
