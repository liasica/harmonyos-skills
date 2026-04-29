---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-animation
title: 动画样式
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 组件通用信息 > 动画样式
category: harmonyos-references
scraped_at: 2026-04-29T13:53:15+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d3bb0d9a2662080897a97618d0b0721e2efdf5fa86ba8f26a71e479e7e99bf06
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

组件支持动态的旋转、平移、缩放效果，可在style或css中设置。

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| transform-origin | string6+ |  <percentage> |  <length> string6+ |  <percentage> | <length> | 变换对象的原点位置，支持px和百分比(相对于动画目标组件)，如果仅设置一个值，另一个值为50%，第一个string的可选值为：left | center | right ，第二个string的可选值为：top | center | bottom。  示例：  transform-origin: 200px 30%。  transform-origin: 100px top。  transform-origin: center center。  默认值：center center |
| transform | string | 支持同时设置平移/旋转/缩放的属性。  详情请参见表1 transform操作说明。 |
| animation6+ | string | 格式：duration | timing-function | delay | iteration-count | direction | fill-mode | play-state | name，每个字段不区分先后，但是 duration / delay 按照出现的先后顺序解析。  默认值：0s ease 0s 1 normal none running none |
| animation-name | string | 指定@keyframes，详情请参见表2 @keyframes属性说明。 |
| animation-delay | <time> | 定义动画播放的延迟时间。支持的单位为[s(秒)|ms(毫秒) ]，默认单位为ms，格式为：1000ms或1s。  默认值：0 |
| animation-duration | <time> | 定义一个动画周期。支持的单位为[s(秒)|ms(毫秒) ]，默认单位为ms，格式为：1000ms或1s。  必须设置animation-duration 样式，否则时长为 0将不会播放动画。  默认值：0 |
| animation-iteration-count | number | infinite | 定义动画播放的次数，默认播放一次，可通过设置为infinite无限次播放。  默认值：1 |
| animation-timing-function | string | 描述动画执行的速度曲线，用于使动画更为平滑。  可选项有：  - linear：表示动画从头到尾的速度都是相同的。  - ease：表示动画以低速开始，然后加快，在结束前变慢，cubic-bezier(0.25, 0.1, 0.25, 1.0)。  - ease-in：表示动画以低速开始，cubic-bezier(0.42, 0.0, 1.0, 1.0)。  - ease-out：表示动画以低速结束，cubic-bezier(0.0, 0.0, 0.58, 1.0)。  - ease-in-out：表示动画以低速开始和结束，cubic-bezier(0.42, 0.0, 0.58, 1.0)。  - friction：阻尼曲线，cubic-bezier(0.2, 0.0, 0.2, 1.0)。  - extreme-deceleration：急缓曲线，cubic-bezier(0.0, 0.0, 0.0, 1.0)。  - sharp：锐利曲线，cubic-bezier(0.33, 0.0, 0.67, 1.0)。  - rhythm：节奏曲线，cubic-bezier(0.7, 0.0, 0.2, 1.0)。  - smooth：平滑曲线，cubic-bezier(0.4, 0.0, 0.4, 1.0)。  - cubic-bezier：在三次贝塞尔函数中定义动画变化过程，入参的x和y值必须处于0-1之间。  - steps: 阶梯曲线6+。语法：steps(number[, end|start])；number必须设置，支持的类型为正整数。第二个参数可选，表示在每个间隔的起点或是终点发生阶跃变化，支持设置end或start，默认值为end。  默认值：ease |
| animation-direction6+ | string | 指定动画的播放模式：  - normal： 动画正向循环播放。  - reverse： 动画反向循环播放。  - alternate：动画交替循环播放，奇数次正向播放，偶数次反向播放。  - alternate-reverse：动画反向交替循环播放，奇数次反向播放，偶数次正向播放。  默认值：normal |
| animation-fill-mode | string | 指定动画开始和结束的状态：  - none：在动画执行之前和之后都不会应用任何样式到目标上。  - forwards：在动画结束后，目标将保留动画结束时的状态（在最后一个关键帧中定义）。  - backwards6+：动画将在animation-delay期间应用第一个关键帧中定义的值。当animation-direction为"normal"或"alternate"时应用from关键帧中的值，当animation-direction为"reverse"或"alternate-reverse"时应用to关键帧中的值。  - both6+：动画将遵循forwards和backwards的规则，从而在两个方向上扩展动画属性。  默认值：none |
| animation-play-state6+ | string | 指定动画的当前状态：  - paused：动画状态为暂停。  - running：动画状态为播放。  默认值：running |
| transition6+ | string | 指定组件状态切换时的过渡效果，可以通过transition属性设置如下四个属性：  - transition-property：规定设置过渡效果的 CSS 属性的名称，目前支持宽、高、背景色。  - transition-duration：规定完成过渡效果需要的时间，单位秒。  - transition-timing-function：规定过渡效果的时间曲线，支持样式动画提供的曲线。  - transition-delay：规定过渡效果延时启动时间，单位秒。  默认值：all 0 ease 0 |

**表1** transform操作说明

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| none6+ | - | 不进行任何转换。 |
| matrix6+ | <number> | 入参为六个值的矩阵，6个值分别代表：scaleX, skewY, skewX, scaleY, translateX, translateY。 |
| matrix3d6+ | <number> | 入参为十六个值的4X4矩阵。 |
| translate | <length> | <percent> | 平移动画属性，支持设置x轴和y轴两个维度的平移参数。 |
| translate3d6+ | <length> | <percent> | 三个入参，分别代表X轴、Y轴、Z轴的平移距离。 |
| translateX | <length> | <percent> | X轴方向平移动画属性。 |
| translateY | <length> | <percent> | Y轴方向平移动画属性。 |
| translateZ6+ | <length> | <percent> | Z轴的平移距离。 |
| scale | <number> | 缩放动画属性，支持设置x轴和y轴两个维度的缩放参数。 |
| scale3d6+ | <number> | 三个入参，分别代表X轴、Y轴、Z轴的缩放参数。 |
| scaleX | <number> | X轴方向缩放动画属性。 |
| scaleY | <number> | Y轴方向缩放动画属性。 |
| scaleZ6+ | <number> | Z轴的缩放参数。 |
| rotate | <deg> | <rad> | <grad>6+ | <turn>6+ | 旋转动画属性，支持设置x轴和y轴两个维度的旋转参数。 |
| rotate3d6+ | <deg> | <rad> | <grad> | <turn> | 四个入参，前三个分别为X轴、Y轴、Z轴的旋转向量，第四个是旋转角度。 |
| rotateX | <deg> | <rad> | <grad>6+ | <turn>6+ | X轴方向旋转动画属性。 |
| rotateY | <deg> | <rad> | <grad>6+ | <turn>6+ | Y轴方向旋转动画属性。 |
| rotateZ6+ | <deg> | <rad> | <grad> | <turn> | Z轴方向的旋转角度。 |
| skew6+ | <deg> | <rad> | <grad> | <turn> | 两个入参，分别为X轴和Y轴的2D倾斜角度。 |
| skewX6+ | <deg> | <rad> | <grad> | <turn> | X轴的2D倾斜角度。 |
| skewY6+ | <deg> | <rad> | <grad> | <turn> | Y轴的2D倾斜角度。 |
| perspective6+ | <number> | 3D透视场景下镜头距离元素表面的距离。 |

**表2** @keyframes属性说明

| 名称 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| background-color | <color> | - | 动画执行后应用到组件上的背景颜色。 |
| opacity | number | 1 | 动画执行后应用到组件上的不透明度值，为介于0到1间的数值，默认为1。 |
| width | <length> | - | 动画执行后应用到组件上的宽度值。 |
| height | <length> | - | 动画执行后应用到组件上的高度值。 |
| transform | string | - | 定义应用在组件上的变换类型，详情请参见表1 transform操作说明。 |
| background-position6+ | string | <percentage> | <length> string |  <percentage> | <length> | 50% 50% | 背景图位置。单位支持百分比和px，第一个值是水平位置，第二个值是垂直位置。如果仅设置一个值，另一个值为50%。第一个string的可选值为：left | center | right ，第二个string的可选值为：top | center | bottom。  示例：  - background-position: 200px 30%  - background-position: 100px top  - background-position: center center |

对于不支持起始值或终止值缺省的情况，可以通过from和to显式指定起始和结束。可以通过百分比指定动画运行的中间状态6+。示例：

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div class="rect">
4. </div>
5. </div>
```

```
1. /* xxx.css */
2. .container {
3. display: flex;
4. justify-content: center;
5. align-items: center;
6. margin: 150px;
7. }
8. .rect{
9. width: 200px;
10. height: 200px;
11. background-color: #f76160;
12. animation: Go 3s infinite;
13. }
14. @keyframes Go
15. {
16. from {
17. background-color: #f76160;
18. transform:translate(100px) rotate(0deg) scale(1.0);
19. }
20. /* 可以通过百分比指定动画运行的中间状态 */
21. 50% {
22. background-color: #f76160;
23. transform:translate(100px) rotate(60deg) scale(1.3);
24. }
25. to {
26. background-color: #09ba07;
27. transform:translate(100px) rotate(180deg) scale(2.0);
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/YxV7690vTdmgSfP0x5awrQ/zh-cn_image_0000002589246505.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055314Z&HW-CC-Expire=86400&HW-CC-Sign=882CEFC37CD873B266AC5197E4B6B70C482E594A7701534C4DFE36BF6E0680C0)

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div class="simpleAnimation simpleSize" style="animation-play-state: {{playState}}"></div>
4. <text onclick="toggleState">animation-play-state: {{playState}}</text>
5. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. justify-content: center;
5. align-items: center;
6. }
7. .simpleSize {
8. background-color: blue;
9. width: 100px;
10. height: 100px;
11. }
12. .simpleAnimation {
13. animation: simpleFrames 9s;
14. }
15. @keyframes simpleFrames {
16. from { transform: translateX(0px); }
17. to { transform: translateX(100px); }
18. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. title: "",
5. playState: "running"
6. },
7. toggleState() {
8. if (this.playState ===  "running") {
9. this.playState = "paused";
10. } else {
11. this.playState = "running";
12. }
13. }
14. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/Inof8TS8RQKbacm2W8dmRQ/zh-cn_image_0000002558766698.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055314Z&HW-CC-Expire=86400&HW-CC-Sign=F939B92AED985684398791A31FCBBD7F04A2E18B4CCBE4924BFCF580D1C144BC)

```
1. <!-- xxx.hml -->
2. <div id='img' class="img"></div>
```

```
1. /* xxx.css */
2. .img {
3. width: 294px;
4. height: 233px;
5. background-image: url('common/heartBeat.jpg');
6. background-repeat: no-repeat;
7. background-position: 0% 0%;
8. background-size: 900%;
9. animation-name: heartBeating;
10. animation-duration: 1s;
11. animation-delay: 0s;
12. animation-fill-mode: forwards;
13. animation-iteration-count: -1;
14. animation-timing-function: steps(8, end);
15. }

17. @keyframes heartBeating {
18. from { background-position: 0% 0%;}
19. to { background-position: 100% 0%;}
20. }
```

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div class="content"></div>
4. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. justify-content: center;
5. align-items: center;
6. }
7. .content { /* 组件状态1 */
8. height: 200px;
9. width: 200px;
10. background-color: red;
11. transition: all 5s ease 0s;
12. }
13. .content:active { /* 组件状态2 */
14. height: 400px;
15. width: 400px;
16. background-color: blue;
17. transition: all 5s linear 0s;
18. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/Z9Jk-LyzToO8Nh_B8TOjZg/zh-cn_image_0000002558607038.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055314Z&HW-CC-Expire=86400&HW-CC-Sign=118F3AD617B0848EDB08DF226B71783C61C81CC68EBBC1735AFE87E3F7C7F4BE)

说明

@keyframes的from/to不支持动态绑定。

steps函数的end和start含义如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/Ku6yeWntTNO9NIlpsg5uUg/zh-cn_image_0000002589326565.png?HW-CC-KV=V1&HW-CC-Date=20260429T055314Z&HW-CC-Expire=86400&HW-CC-Sign=78E9350BCA249268FC6F9F94A304CFB7C01684E748292A3747BAD25F1D00D4CA)
