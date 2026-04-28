---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-marquee
title: marquee开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > marquee开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:29+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a366e336d7256fe210d9d8de2219bd84c4f0a9363e3df704e92e952cdeda5433
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/cfpzrgBxQsCdj3ZP8InXaQ/zh-cn_image_0000002552958124.png?HW-CC-KV=V1&HW-CC-Date=20260427T234028Z&HW-CC-Expire=86400&HW-CC-Sign=65A0B1F56DCE27F8078820ECCF7F71EB6B2A7FCE1113F307E30740C6E3479848)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/uk8F-RwrTBCP9k2WLmdeaA/zh-cn_image_0000002583478125.png?HW-CC-KV=V1&HW-CC-Date=20260427T234028Z&HW-CC-Expire=86400&HW-CC-Sign=1D01F3A58184D1B4017A75FD6EFDB0832C8F24C61E00E5E84A9DB32B66B4F94A)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/xGX6bOhLRou4yRKbN_YAZw/zh-cn_image_0000002552798476.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234028Z&HW-CC-Expire=86400&HW-CC-Sign=D80116556B99510E6A30395D295BC37178A60C60F83C785172662959FFD8DDE6)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/6bCzS7bAR1eb3URR_rVajQ/zh-cn_image_0000002583438171.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234028Z&HW-CC-Expire=86400&HW-CC-Sign=A3C9043224A61C485FA03539E346498953B2EFD3CEBF211C70607DA032963F05)
