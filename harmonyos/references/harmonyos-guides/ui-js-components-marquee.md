---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-marquee
title: marquee开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > marquee开发指导
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:50+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c37cfd02d6c0934101280c8d43ce52ccd204f1c4f40362f57f1c31b7b17be374
---

marquee为跑马灯组件，用于展示一段单行滚动的文字。具体用法请参考[marquee](../harmonyos-references/js-components-basic-marquee.md)。

## 创建marquee组件

在pages/index目录下的hml文件中创建一个marquee组件。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <marquee style="width: 100%;height: 80px; color: #ffffff; background-color: #0820ef;padding-left: 200px;">It's a racing lamp.</marquee>
4. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/LQSIy0pHTOqI9A1nlhmK0Q/zh-cn_image_0000002589324485.png?HW-CC-KV=V1&HW-CC-Date=20260429T052849Z&HW-CC-Expire=86400&HW-CC-Sign=4514F5D4DB46D9036B2A2248B87E40A31A9E14D8A70B52B99455D371BFA9EF1D)

## 设置属性和样式

marquee通过color和font-weight属性设置跑马灯中文本的颜色、字体粗细和边框样式。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <marquee class="custommarquee">It's a racing lamp.</marquee>
4. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. }
10. .custommarquee {
11. width: 100%;
12. height: 80px;
13. padding: 10px;
14. margin: 20px;
15. border: 4px solid #6712f1;
16. border-radius: 20px;
17. font-size: 40px;
18. color: #ffffff;  font-weight: bolder;
19. font-family: serif;
20. background-color: #1567f3;
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/7qOUs0nwSMiDBXZx39Kfbg/zh-cn_image_0000002589244423.png?HW-CC-KV=V1&HW-CC-Date=20260429T052849Z&HW-CC-Expire=86400&HW-CC-Sign=A20043A41BAE5730372B243EAE453A299C24A8C82CC6F252EBFF9F16697CBFE3)

通过scrollamount、loop和direction属性实现跑马灯滚动时移动的最大长度、滚动次数和文字滚动方向。

```
1. <!-- xxx.hml -->
2. <div class="tutorial-page">
3. <div class="mymarquee">
4. <marquee loop="{{loopval}}" scrollamount="{{scroll}}" direction="{{isleft}}" class="marqueetext" id="testmarquee" onclick="makestart">
5. Life is a journey, not the destination.
6. </marquee>
7. </div>
8. <div style="width: 600px;height: 150px;flex-direction: row;justify-content: space-around;">
9. <button onclick="setleft"  value="left"></button>
10. <button onclick="setright" value="right"></button>
11. </div>
12. </div>
```

```
1. /* xxx.css */
2. .tutorial-page {
3. width: 750px;
4. height: 100%;
5. flex-direction: column;
6. align-items: center;
7. justify-content: center;
8. background-color: #F1F3F5;
9. }
10. .marqueetext {
11. color: #ffffff;
12. font-family: serif;
13. font-size: 37px;
14. }
15. .mymarquee {
16. margin-top: 20px;
17. width:100%;
18. height: 100px;
19. margin-left: 50px;
20. margin-right: 50px;
21. border: 1px solid #6712f1;
22. background-color: #1567f3;
23. border-radius: 15px;
24. align-items: center;
25. }
26. button{
27. width: 200px;
28. height: 80px;
29. margin-top: 100px;
30. }
```

```
1. // xxx.js
2. export default {
3. private: {
4. loopval: -1,
5. scroll: 10,
6. isleft: "left",
7. },
8. onInit(){
9. },
10. setleft(e) {
11. this.isleft = "left"
12. },
13. setright(e) {
14. this.isleft = "right"
15. },
16. makestart(e) {
17. this.$element('testmarquee').start()
18. }
19. }
```

说明

当loop的值小于等于零时，跑马灯marquee将连续滚动。如果loop未指定，则默认为-1。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/SoZ6qaGBQ5eIplTtL6UXVw/zh-cn_image_0000002558764616.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052849Z&HW-CC-Expire=86400&HW-CC-Sign=7E1F51BFA58C7439F927F0D6109744359B56371A481ACFC4D4335323750C741A)

## 场景示例

本场景可以控制跑马灯文字的滚动和暂停。

跑马灯的次数设置为1，在结束的时候触发finish事件使跑马灯的次数加1，字体颜色变为随机颜色，调用start方法使跑马灯再次开始滚动。

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
11. this.loopval = this.loopval + 1,
12. this.r = Math.floor(Math.random()*255),
13. this.g = Math.floor(Math.random()*255),
14. this.b = Math.floor(Math.random()*255),
15. this.color1 = 'rgba('+ this.r +','+ this.g +','+ this.b +',0.8)',
16. this.$element('testmarquee').start(),
17. this.loopval = this.loopval - 1
18. },
19. makestart(e) {
20. this.$element('testmarquee').start()
21. },
22. makestop(e) {
23. this.$element('testmarquee').stop()
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/rOJIvspRS7uV9jFp10V_vg/zh-cn_image_0000002558604960.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052849Z&HW-CC-Expire=86400&HW-CC-Sign=B3032AE422E14135F890E31FDC046E867D1D900C3F123FC268B6A7B1EE2A0194)
