---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-swiper
title: swiper
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 容器组件 > swiper
category: harmonyos-references
scraped_at: 2026-04-29T13:53:21+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0291de14892837aebb6c17dfb21ee9e39823ae8945c1dbccf2cc23fa03282f47
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

滑动容器，提供切换子组件显示的能力。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

可以包含子组件。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-components-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| index | number | 0 | 否 | 当前在容器中显示的子组件的索引值。 |
| autoplay | boolean | false | 否 | 子组件是否自动播放，自动播放状态下，导航点不可操作5+。true为自动轮播，false为不自动轮播。 |
| interval | number | 3000 | 否 | 使用自动播放时播放的时间间隔，单位为ms。 |
| indicator | boolean | true | 否 | 是否启用导航点指示器，默认true。true为启用导航点指示器，false为不启用导航点指示器。 |
| digital5+ | boolean | false | 否 | 是否启用数字导航点，默认为false。true为启用数字导航点，false为不启用数字导航点。  必须设置indicator时才能生效数字导航点。 |
| indicatordisabled5+ | boolean | false | 否 | 指示器是否禁止用户手势操作，设置为true时，指示器不会响应用户的点击拖拽。 |
| loop | boolean | true | 否 | 是否开启循环滑动。true为开启循环，false为不开启循环。 |
| duration | number | - | 否 | 子组件切换的动画时长。 |
| vertical | boolean | false | 否 | 是否为纵向滑动，纵向滑动时采用纵向的指示器。true为纵向滑动，false为水平滑动。 |
| cachedsize7+ | number | -1 | 否 | swiper延迟加载时item最少缓存数量。-1表示全部缓存。 |
| scrolleffect7+ | string | spring | 否 | 滑动效果。目前支持如下：  - spring：弹性物理动效，滑动到边缘后可以根据初始速度或通过触摸事件继续滑动一段距离，松手后回弹。  - fade：渐隐物理动效，滑动到边缘后展示一个波浪形的渐隐，根据速度和滑动距离的变化渐隐也会发生一定的变化。  - none：滑动到边缘后无效果。  该属性仅在loop属性为false时生效。 |

## 样式

PhonePC/2in1TabletTVWearable

除支持[通用样式](js-components-common-styles.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| indicator-color | <color> | - | 否 | 导航点指示器的填充颜色。 |
| indicator-selected-color | <color> | #ff007dff | 否 | 导航点指示器选中的颜色。 |
| indicator-size | <length> | 4px | 否 | 导航点指示器的直径大小。 |
| indicator-top|left|right|bottom | <length> | <percentage> | - | 否 | 导航点指示器在swiper中的相对位置。 |
| next-margin7+ | <length> | <percentage> | - | 否 | 后边距，用于露出后一项的一小部分。 |
| previous-margin7+ | <length> | <percentage> | - | 否 | 前边距，用于露出前一项的一小部分。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](js-components-common-events.md)外，还支持如下事件：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | { index: currentIndex } | 当前显示的组件索引变化时触发该事件。 |
| rotation | { value: rotationValue } | 智能穿戴表冠旋转事件触发时的回调。 |
| animationfinish7+ | - | 动画结束时触发该事件。 |

## 方法

PhonePC/2in1TabletTVWearable

除支持[通用方法](js-components-common-methods.md)外，还支持如下方法：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| swipeTo | { index: number(指定位置) } | 切换到index位置的子组件。 |
| showNext | 无 | 显示下一个子组件。 |
| showPrevious | 无 | 显示上一个子组件。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <swiper class="swiper" id="swiper" index="0" indicator="true" loop="true" digital="false" cachedsize="-1"
4. scrolleffect="spring">
5. <div class = "swiperContentOne" >
6. <text class = "text">First screen</text>
7. </div>
8. <div class = "swiperContentTwo">
9. <text class = "text">Second screen</text>
10. </div>
11. <div class = "swiperContentThree">
12. <text class = "text">Third screen</text>
13. </div>
14. </swiper>
15. <input class="button" type="button" value="swipeTo" onclick="swipeTo"></input>
16. <input class="button" type="button" value="showNext" onclick="showNext"></input>
17. <input class="button" type="button" value="showPrevious" onclick="showPrevious"></input>
18. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. width: 100%;
5. height: 100%;
6. align-items: center;
7. }
8. .swiper {
9. flex-direction: column;
10. align-content: center;
11. align-items: center;
12. width: 70%;
13. height: 130px;
14. border: 1px solid #000000;
15. indicator-color: #cf2411;
16. indicator-size: 14px;
17. indicator-bottom: 20px;
18. indicator-right: 30px;
19. margin-top: 100px;
20. next-margin:20px;
21. previous-margin:20px;
22. }
23. .swiperContentOne{
24. height: 100%;
25. width: 100%;
26. justify-content: center;
27. background-color: #007dff;
28. }
29. .swiperContentTwo{
30. height: 100%;
31. width: 100%;
32. justify-content: center;
33. background-color: #ff7500;
34. }
35. .swiperContentThree{
36. height: 100%;
37. width: 100%;
38. justify-content: center;
39. background-color: #41ba41;
40. }
41. .button {
42. width: 70%;
43. margin: 10px;
44. }
45. .text {
46. font-size: 40px;
47. }
```

```
1. // xxx.js
2. export default {
3. swipeTo() {
4. this.$element('swiper').swipeTo({index: 2});
5. },
6. showNext() {
7. this.$element('swiper').showNext();
8. },
9. showPrevious() {
10. this.$element('swiper').showPrevious();
11. }
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/WhpkWRqsSSG_d4WKFwvbsg/zh-cn_image_0000002558766712.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055320Z&HW-CC-Expire=86400&HW-CC-Sign=02526F40FFDED48D8E48BF2C6B51CE0DAC8D87BC23DF8DCF43EA41DCA9D99B8F)
