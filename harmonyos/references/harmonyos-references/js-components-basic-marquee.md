---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-marquee
title: marquee
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 基础组件 > marquee
category: harmonyos-references
scraped_at: 2026-04-29T13:53:24+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ef7775566ce618e249a008a28e17dbf2bf9a57798d1ae66050643a0ab5a5f2da
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

从API version 6开始，仅当文本内容宽度超过跑马灯组件宽度时滚动。

跑马灯组件，用于展示一段单行滚动的文字。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

不支持。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-components-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| scrollamount | number | 6 | 否 | 跑马灯每次滚动时移动的最大长度。 |
| loop | number | -1 | 否 | 跑马灯滚动的次数。如果未指定，则默认值为-1，当该值小于等于零时表示marquee将连续滚动。 |
| direction | string | left | 否 | 设置跑马灯的文字滚动方向，可选值为left和right。 |

## 样式

PhonePC/2in1TabletTVWearable

除支持[通用样式](js-components-common-styles.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| color | <color> | #e5000000 | 否 | 设置跑马灯中文字的文本颜色。 |
| font-size | <length> | 37.5 | 否 | 设置跑马灯中文字的文本尺寸。 |
| allow-scale | boolean | true | 否 | 设置跑马灯中文字的文本尺寸是否跟随系统设置字体缩放尺寸进行放大缩小。true表示跟随系统放大缩小，false表示不跟随系统放大缩小。  如果在config描述文件中针对ability配置了fontSize的config-changes标签，则应用不会重启而直接生效。 |
| font-weight | number | string | normal | 否 | 设置跑马灯中文字的字体的粗细，见[text组件font-weight的样式属性](js-components-basic-text.md#样式)。 |
| font-family | string | sans-serif | 否 | 设置跑马灯中文字的字体列表，用逗号分隔，每个字体用字体名或者字体族名设置。列表中第一个系统中存在的或者通过[自定义字体](js-components-common-customizing-font.md)指定的字体，会被选中作为文本的字体。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](js-components-common-events.md)外，还支持如下事件：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| bounce | - | 当文本滚动到末尾时触发该事件。 |
| finish | - | 当完成滚动次数时触发该事件。需要在 loop 属性值大于 0 时触发。 |
| start | - | 当文本滚动开始时触发该事件。 |

## 方法

PhonePC/2in1TabletTVWearable

除支持[通用方法](js-components-common-methods.md)外，还支持如下方法：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| start | - | 开始滚动。 |
| stop | - | 停止滚动。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="tutorial-page">
3. <div class="mymarquee">
4. <marquee  style="color: {{color1}}" loop="{{loopval}}" scrollamount="{{scroll}}" direction="{{isleft}}" class="marqueetext"
5. id="testmarquee" onfinish="setfinish">
6. Life is a journey, not the destination.
7. </marquee>
8. </div>
9. <div style="width: 600px;height: 150px;flex-direction: row;justify-content: space-around;">
10. <button onclick="makestart"  value="start"></button>
11. <button onclick="makestop" value="stop"></button>
12. </div>
13. </div>
```

```
1. /* xxx.css */
2. .tutorial-page {
3. width: 750px;
4. height: 100%;
5. flex-direction: column;
6. align-items: center;
7. justify-content: center;
8. }
9. .marqueetext {
10. font-size: 37px;
11. }
12. .mymarquee {
13. margin-top: 20px;
14. width:100%;
15. height: 100px;
16. margin-left: 50px;
17. margin-right: 50px;
18. border: 1px solid #dc0f27;
19. border-radius: 15px;
20. align-items: center;
21. }
22. button{
23. width: 200px;
24. height: 80px;
25. margin-top: 100px;
26. }
```

```
1. // xxx.js
2. export default {
3. private: {
4. loopval: 1,
5. scroll: 8,
6. color1: 'red'
7. },
8. onInit(){
9. },
10. setfinish(e) {
11. this.loopval=  this.loopval + 1,
12. this.r = Math.floor(Math.random()*255),
13. this.g = Math.floor(Math.random()*255),
14. this.b = Math.floor(Math.random()*255),
15. this.color1 = 'rgba('+ this.r +','+ this.g +','+ this.b +',0.8)',
16. this.$element('testmarquee').start(),
17. this.loopval=  this.loopval - 1
18. },
19. makestart(e) {
20. this.$element('testmarquee').start()
21. },
22. makestop(e) {
23. this.$element('testmarquee').stop()
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/4wW-jh4sStyRX_--SIhRJg/zh-cn_image_0000002589246527.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055323Z&HW-CC-Expire=86400&HW-CC-Sign=6970937E756D6EDA3AA9EFDEDBE1B1E02201F97CCBBD88390DA8BD0471E504E2)
