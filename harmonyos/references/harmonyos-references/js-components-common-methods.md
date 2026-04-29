---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-methods
title: 通用方法
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 组件通用信息 > 通用方法
category: harmonyos-references
scraped_at: 2026-04-29T13:53:15+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c65968e11fcf9563b1b2d2d393746d93a20e99135d3ed61a5236d1be24003c18
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

当组件通过id属性标识后，可以使用该id获取组件对象并调用相关组件方法。

## animate

PhonePC/2in1TabletTVWearable

animate( keyframes: Keyframes, options: Options)：void

设置动画样式和动画属性的对象列表。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyframes | keyframes | 是 | 设置动画样式。 |
| options | Options | 是 | 用于设置动画属性的对象列表。具体参数说明请参见表3 Options说明。 |

**表1** keyframes

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| frames | Array<Style> | 用于设置动画样式的对象列表。Style类型说明请见表2 Style类型说明。 |

**表2** Style类型说明

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| width | number | - | 动画执行过程中设置到组件上的宽度值。 |
| height | number | - | 动画执行过程中设置到组件上的高度值。 |
| backgroundColor | <color> | none | 动画执行过程中设置到组件上的背景颜色。 |
| opacity | number | 1 | 设置到组件上的透明度，取值范围在0到1之间。 |
| backgroundPosition | string | - | 格式为"x y"，单位为百分号或者px。  第一个值是水平位置，第二个值是垂直位置。  如果仅规定了一个值，另一个值为 50%。 |
| transformOrigin | string | 'center center' | 变换对象的中心点。  第一个参数表示x轴的值，可以设置为left、center、right、长度值或百分比值。  第二个参数表示y轴的值，可以设置为top、center、bottom、长度值或百分比值。 |
| transform | [Transform](js-components-common-animation.md) | - | 设置到变换对象上的类型。 |
| offset | number | - | - offset值（如果提供）必须在0.0到1.0（含）之间，并以升序排列。  - 若仅有两帧，offset参数可省略。  - 若超过两帧，offset必填。 |

**表3** Options说明

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| duration | number | 0 | 指定当前动画的运行时长，单位毫秒。有效取值范围为[0, +∞)，小于0时取默认值。 |
| easing | string | linear | 描述动画的时间曲线，支持的具体类型参数请参见表4 easing有效值。 |
| delay | number | 0 | 设置动画执行的延迟时间，默认值表示无延迟。 |
| iterations | number | string | 1 | 设置动画执行的次数。number表示固定次数，Infinity枚举表示无限次数播放。 |
| direction6+ | string | normal | 指定动画的播放模式：  normal： 动画正向循环播放；  reverse： 动画反向循环播放；  alternate：动画交替循环播放，奇数次正向播放，偶数次反向播放；  alternate-reverse：动画反向交替循环播放，奇数次反向播放，偶数次正向播放。 |
| fill | string | none | 指定动画开始和结束的状态：  none：在动画执行之前和之后都不会应用任何样式到目标上。  forwards：在动画结束后，目标将保留动画结束时的状态（在最后一个关键帧中定义）。  backwards6+：动画将在animation-delay期间应用第一个关键帧中定义的值。当animation-direction为"normal"或"alternate"时应用from关键帧中的值，当animation-direction为"reverse"或"alternate-reverse"时应用to关键帧中的值。  both：动画将遵循forwards和backwards的规则，从而在两个方向上扩展动画属性。 |

**表4** easing有效值说明

| 值 | 描述 |
| --- | --- |
| linear | 动画线性变化。 |
| ease-in | 动画速度先慢后快，cubic-bezier(0.42, 0.0, 1.0, 1.0)。 |
| ease-out | 动画速度先快后慢，cubic-bezier(0.0, 0.0, 0.58, 1.0)。 |
| ease-in-out | 动画先加速后减速，cubic-bezier(0.42, 0.0, 0.58, 1.0)。 |
| friction | 阻尼曲线，cubic-bezier(0.2, 0.0, 0.2, 1.0)。 |
| extreme-deceleration | 急缓曲线，cubic-bezier(0.0, 0.0, 0.0, 1.0)。 |
| sharp | 锐利曲线，cubic-bezier(0.33, 0.0, 0.67, 1.0)。 |
| rhythm | 节奏曲线，cubic-bezier(0.7, 0.0, 0.2, 1.0)。 |
| smooth | 平滑曲线，cubic-bezier(0.4, 0.0, 0.4, 1.0)。 |
| cubic-bezier(x1, y1, x2, y2) | 在三次贝塞尔函数中定义动画变化过程，入参的x和y值必须处于0-1之间。 |
| steps(number, step-position)6+ | Step曲线。  number必须设置，支持的类型为int。  step-position参数可选，支持设置start或end，默认值为end。 |

**返回值：**

animation对象属性：

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| finished | boolean | 只读，用于表示当前动画是否已播放完成。返回true时，动画播放完成。返回false时，动画没播放完成。 |
| pending | boolean | 只读，用于表示当前动画是否处于等待其他异步操作完成的等待状态（例如启动一个延时播放的动画）。返回true时，动画处于等待状态。返回false时，动画不处于等待状态。 |
| playState | string | 可读可写，动画的执行状态：  - idle：未执行状态，包括已结束或未开始。  - running：动画正在运行。  - paused：动画暂停。  - finished：动画播放完成。 |
| startTime | number | 可读可写，动画播放开始的预定时间，用途类似于options参数中的delay。 |

animation对象方法：

| 方法 | 参数 | 说明 |
| --- | --- | --- |
| play | - | 组件播放动画。 |
| finish | - | 组件完成动画。 |
| pause | - | 组件暂停动画。 |
| cancel | - | 组件取消动画。 |
| reverse | - | 组件倒播动画。 |

animation对象事件：

| 事件 | 说明 |
| --- | --- |
| start6+ | 动画开始事件。 |
| cancel | 动画被强制取消。 |
| finish | 动画播放完成。 |
| repeat | 动画重播事件。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div id="idName" class="box"></div>
4. <div class="buttonBox">
5. <button @click="start">
6. start
7. </button>
8. <button @click="cancel">
9. cancel
10. </button>
11. </div>
12. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. justify-content: center;
5. align-items: center;
6. width: 100%;
7. }
8. .box{
9. width: 200px;
10. height: 200px;
11. background-color: #ff0000;
12. margin-top: 30px;
13. }
14. .buttonBox{
15. margin-top: 30px;
16. width: 250px;
17. justify-content: space-between;
18. }
19. button{
20. background-color: #8e8b89;
21. color: white;
22. width: 100px;
23. height: 40px;
24. font-size: 24px;
25. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. animation: '',
5. options: {},
6. frames: {}
7. },
8. onInit() {
9. this.options = {
10. duration: 1500,
11. easing: 'friction',
12. delay: 500,
13. fill: 'forwards',
14. iterations: 2,
15. direction: 'normal',
16. };
17. this.frames = [
18. {
19. transform: {
20. translate: '-120px -0px'
21. }, opacity: 0.1, offset: 0.0
22. },
23. {
24. transform: {
25. translate: '120px 0px'
26. }, opacity: 1.0, offset: 1.0
27. }
28. ];
29. },

31. start() {
32. this.animation = this.$element('idName').animate(this.frames, this.options);
33. this.animation.play();
34. },
35. cancel() {
36. this.animation.cancel();
37. }
38. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/L_fr0AZ9SimahjRdCksJ0Q/zh-cn_image_0000002589326563.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055314Z&HW-CC-Expire=86400&HW-CC-Sign=E40DCA254BAEFF4E9AB77EA1158AE18AFC4B3F896715576D4CD7DF0E9E687409)

## getBoundingClientRect

PhonePC/2in1TabletTVWearable

getBoundingClientRect(): <Rect>

获取元素的大小及其相对于窗口的位置。

**返回值：**

**表5** Rect对象说明6+

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| width | number | 该元素的宽度。 |
| height | number | 该元素的高度。 |
| left | number | 该元素左边界距离窗口的偏移。 |
| top | number | 该元素上边界距离窗口的偏移。 |

**示例：**

```
1. // xxx.js
2. var rect = this.$element('id').getBoundingClientRect();
3. console.info(`current element position is ${rect.left}, ${rect.top}`);
```

## createIntersectionObserver

PhonePC/2in1TabletTVWearable

createIntersectionObserver(param?: ObserverParam): Observer

监听元素在当前页面的可见范围。

**参数：**

| 参数名 | 参数类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| param | ObserverParam | - | 获取observer的回调。 |

**表6** ObserverParam对象说明6+

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| ratios | Array<number> | 组件超出或小于范围时触发observer的回调。 |

**返回值：**

**表7** Observer对象支持的方法6+

| 方法 | 参数 | 描述 |
| --- | --- | --- |
| observe | callback: function | 开启observer的订阅方法，超出或小于阈值时触发callback。 |
| unobserve | - | 取消observer的订阅方法。 |

**示例：**

```
1. // xxx.js
2. let observer = this.$element('broad').createIntersectionObserver({
3. ratios: [0.2, 0.5], // number
4. });

6. observer.observe((isVisible, ratio)=> {
7. console.info('this element is ' + isVisible + 'ratio is ' + ratio)
8. })

10. observer.unobserve()
```
