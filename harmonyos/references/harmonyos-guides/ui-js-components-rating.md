---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-rating
title: rating开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > rating开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b5745c7872a36f5b8977eb2cf0cae788d1d48a61d35679975749a46a18a608cb
---

rating是评分组件，用于展示用户对某项内容的评价等级。具体用法请参考[rating](../harmonyos-references/js-components-basic-rating.md)。

## 创建rating组件

在pages/index目录下的hml文件中创建一个rating组件。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <rating></rating>
4. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. display: flex;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. }
10. .rating {
11. width: 80%;
12. height: 150px;
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/Wy9byfCWT62CP4VNpMr1Uw/zh-cn_image_0000002552958112.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234026Z&HW-CC-Expire=86400&HW-CC-Sign=1162FA080003DA709122CB8C95FBC5BB8FCD3F1390CAC36DC294E68A11A3EC33)

## 设置评分星级

rating组件通过设置numstars和rating属性设置评分条的星级总数和当前评星数。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <rating numstars="6" rating="5">
4. </rating>
5. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. display: flex;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. }
10. .rating {
11. width: 80%;
12. height: 150px;
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/xAUTJfwtSvGK5EV_YWcNCA/zh-cn_image_0000002583478113.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234026Z&HW-CC-Expire=86400&HW-CC-Sign=4E7FF87C1795D933AF252530E1F0D3225DD48E802EBA20F4B695BE71274FBA7C)

## 设置评分样式

rating组件通过star-background、star-foreground和star-secondary属性设置单个星级未选择、选中和选中的次级背景图片。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div style="width: 500px;height: 500px;align-items: center;justify-content: center;flex-direction: column;">
4. <rating numstars="5" rating="1" class="myrating" style="width: {{ratewidth}}; height:{{rateheight}};
5. star-background: {{backstar}}; star-secondary: {{secstar}};star-foreground: {{forestar}};rtl-flip: true;">
6. </rating>
7. </div>
8. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. align-items: center;
7. justify-content: center;
8. background-color: #F1F3F5;
9. }
```

```
1. // index.js
2. export default {
3. data: {
4. backstar: 'common/love.png',
5. secstar: 'common/love.png',
6. forestar: 'common/love1.png',
7. ratewidth: '400px',
8. rateheight: '150px'
9. },
10. onInit(){
11. }
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/LoKY0XaeS72LNsDRhPrCwA/zh-cn_image_0000002552798464.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234026Z&HW-CC-Expire=86400&HW-CC-Sign=C14D60C7F61DE45FABB0EC0046E4E21C8A672BC5074C1C2B5858C19D6B0A2AAD)

说明

* star-background、star-secondary、star-foreground属性的星级图源必须全部设置，否则默认的星级颜色为灰色，提示图源设置错误。
* star-background、star-secondary、star-foreground属性只支持本地路径图片，图片格式为png和jpg。

## 绑定事件

向rating组件添加change事件，打印当前评分。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <rating numstars="5" rating="0" onchange="showrating"></rating>
4. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. display: flex;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. }
10. .rating {
11. width: 80%;
12. height: 150px;
13. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction';
3. export default {
4. showrating(e) {
5. promptAction.showToast({
6. message: '当前评分' + e.rating
7. })
8. }
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/OtcsM1-vRiK_fduKhBuXqw/zh-cn_image_0000002583438159.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234026Z&HW-CC-Expire=86400&HW-CC-Sign=4D147A2F4A5A5409EDF4200CCB2AF316D1E1FA557069F61AB0A9FC5E4C24C559)

## 场景示例

开发者可以通过改变开关状态切换星级背景图，通过改变滑动条的值调整星级总数。

```
1. <!-- xxx.hml -->
2. <div style="width: 100%;height:100%;flex-direction: column;align-items: center;background-color: #F1F3F5;">
3. <div style="width: 500px;height: 500px;align-items: center;justify-content: center;flex-direction: column;">
4. <rating numstars="{{stars}}" rating="{{rate}}" stepsize="{{step}}" onchange="showrating" class="myrating"
5. style="width: {{ratewidth}};height:{{rateheight}};star-background: {{backstar}};star-secondary: {{secstar}};
6. star-foreground: {{forestar}};rtl-flip: true;"></rating>
7. </div>
8. <div style="flex-direction: column;width: 80%;align-items: center;">
9. <div style="width: 100%;height: 100px;align-items: center;justify-content: space-around;">
10. <text>替换自定义图片</text>
11. <switch checked="false" showtext="true" onchange="setstar"></switch>
12. </div>
13. <div style="width: 100%;height:120px;margin-top: 50px;margin-bottom: 50px;flex-direction: column;align-items: center;
14. justify-content: space-around;">
15. <text>numstars   {{stars}}</text>
16. <slider id="sli1" min="0" max="10" value="5" step="1" onchange="setnumstars"></slider>
17. </div>
18. <div style="width: 100%;height:120px;flex-direction: column;align-items: center;justify-content: space-around;">
19. <text>rating   {{rate}}</text>
20. <slider id="sli2" min="0" max="10" value="{{rate}}" step="0.5" onchange="setrating"></slider>
21. </div>
22. </div>
23. </div>
```

```
1. /* xxx.css */
2. .myrating:active {
3. width: 500px;
4. height: 100px;
5. }
6. .switch{
7. font-size: 40px;
8. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction';
3. export default {
4. data: {
5. backstar: '',
6. secstar: '',
7. forestar: '',
8. stars: 5,
9. ratewidth: '300px',
10. rateheight: '60px',
11. step: 0.5,
12. rate: 0
13. },
14. onInit(){
15. },
16. setstar(e) {
17. if (e.checked == true) {
18. this.backstar = '/common/love.png'
19. this.secstar = 'common/love.png'
20. this.forestar = 'common/love1.png'
21. } else {
22. this.backstar = ''
23. this.secstar = ''
24. this.forestar = ''
25. }
26. },
27. setnumstars(e) {
28. this.stars = e.progress
29. this.ratewidth = 60 * parseInt(this.stars) + 'px'
30. },
31. setstep(e) {
32. this.step = e.progress
33. },
34. setrating(e){
35. this.rate = e.progress
36. },
37. showrating(e) {
38. this.rate = e.rating
39. promptAction.showToast({
40. message: '当前评分' + e.rating
41. })
42. }
43. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/tvAjpOpDRj-KAu9ZUX_yOg/zh-cn_image_0000002552958114.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234026Z&HW-CC-Expire=86400&HW-CC-Sign=21D35D5F6BB3BF9543D43D6695893F88454BA9B655BDB548503B796CCE49FA3A)
