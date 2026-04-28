---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-swiper
title: swiper开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 容器组件 > swiper开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:25+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c1db5ce405f457f634f41ab008650dac7394774c6f3e98bad7b2946e59a1da27
---

swiper为滑动容器，提供切换显示子组件的能力。具体用法请参考[swiper](../harmonyos-references/js-components-container-swiper.md)。

## 创建swiper组件

在pages/index目录下的hml文件中创建一个swiper组件。

```
1. <!-- xxx.hml-->
2. <div class="container">
3. <swiper>
4. <div class="item" style="background-color: #bf45ea;">
5. <text>item1</text>
6. </div>
7. <div class="item" style="background-color: #088684;">
8. <text>item2</text>
9. </div>
10. <div class="item" style="background-color: #7786ee;">
11. <text>item3</text>
12. </div>
13. </swiper>
14. </div>
```

```
1. /* xxx.css */
2. .container{
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. background-color: #F1F3F5;
7. align-items: center;
8. justify-content: center;
9. width: 100%;
10. }
11. swiper{
12. height: 30%;
13. }
14. .item{
15. width: 100%;
16. height: 500px;
17. }
18. text{
19. width: 100%;
20. height: 100%;
21. text-align: center;
22. font-size: 50px;
23. color: white;
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/NwtGwh5wQZusWK3EOxeZzQ/zh-cn_image_0000002583438141.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234024Z&HW-CC-Expire=86400&HW-CC-Sign=D22E11601D7DC172F17DCC0BD428E1AD3BA2FFE56BB36786ED14E8D429A7DD7C)

说明

swiper组件支持除<list>之外的子组件。

## 添加属性

在swiper组件不开启循环播放（loop="false"）时添加自动播放属性（autoplay），设置自动播放时播放时间间隔（interval），页面会自动切换并停留在最后一个子组件页面。添加digital属性启用数字导航点，设置切换时为渐隐滑动效果（scrolleffect="fade"）。

```
1. <!-- xxx.hml-->
2. <div class="container">
3. <swiper index="1"  autoplay="true" interval="2000" indicator="true" digital="true" duration="500"
4. scrolleffect="fade" loop="false">
5. <div class="item" style="background-color: #bf45ea;">
6. <text>item1</text>
7. </div>
8. <div class="item" style="background-color: #088684;">
9. <text>item2</text>
10. </div>
11. <div class="item" style="background-color: #7786ee;">
12. <text>item3</text>
13. </div>
14. <div class="item" style="background-color: #c88cee;">
15. <text>item4</text>
16. </div>
17. </swiper>
18. </div>
```

```
1. /* xxx.css */
2. .container{
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. background-color: #F1F3F5;
7. align-items: center;
8. justify-content: center;
9. }
10. swiper{
11. height: 30%;
12. }
13. .item{
14. width: 100%;
15. height: 500px;
16. }
17. text{
18. width: 100%;
19. height: 100%;
20. text-align: center;
21. font-size: 50px;
22. color: white;
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/E4s1slmpS5GJ8YY0e1Ie6A/zh-cn_image_0000002552958096.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234024Z&HW-CC-Expire=86400&HW-CC-Sign=71F63E4889EEF9F43C601BBED512CCE4E3E1B809D64F3BF6B1BC951C2D7F7F34)

说明

* 设置indicator（是否启用导航点指示器）属性为true时digital（是否启用数字导航点）属性才会生效。
* swiper子组件的个数大于等于2时设置的loop属性才会生效。
* scrolleffect属性仅在loop属性值为false时生效。

## 设置样式

设置swiper组件的宽高，导航点指示器的直径大小（indicator-size）、颜色（indicator-color）、相对位置（indicator-top）及选中时的颜色（indicator-selected-color）。

```
1. <!-- xxx.hml-->
2. <div class="container">
3. <swiper index="1" autoplay="true" interval="2000"  duration="500" >
4. <div class="item" style="background-color: bisque;">
5. <text>item1</text>
6. </div>
7. <div class="item" style="background-color: darkkhaki;">
8. <text>item2</text>
9. </div>
10. <div class="item" style="background-color: cadetblue;">
11. <text>item3</text>
12. </div>
13. </swiper>
14. </div>
```

```
1. /* xxx.css */
2. .container{
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. background-color: #F1F3F5;
7. align-items: center;
8. justify-content: center;
9. }
10. swiper{
11. width:  500px;
12. height: 500px;
13. border-radius: 250px;
14. indicator-color: white;
15. indicator-selected-color: blue;
16. indicator-size: 40px;
17. indicator-top: 100px;
18. overflow: hidden ;
19. }
20. .item{
21. width: 100%;
22. height: 500px;
23. }
24. text{
25. width: 100%;
26. text-align: center;
27. margin-top: 150px;
28. font-size: 50px;
29. color: white;
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/dNIL_qkDQxOxmintyjXTXg/zh-cn_image_0000002583478097.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234024Z&HW-CC-Expire=86400&HW-CC-Sign=4030C830C1DBFC149E93FC57F86B9163F1323135C07DADCC828C5CE141CC46F2)

## 绑定事件

创建两个text组件添加点击事件，当点击后就调用showPrevious（显示上一个子组件）或showNext（显示下一个子组件）方法。添加select组件下拉选择时触发change事件后调用swipeTo方法跳转到指定轮播页面。swiper组件绑定change（当前显示的组件索引变化时触发）和finish（切换动画结束时触发）事件。

```
1. <!-- xxx.hml-->
2. <div class="container">
3. <swiper interval="2000" onchange="change" loop="false" onanimationfinish="finish" id="swiper">
4. <div class="item" style="background-color: #bf45ea">
5. <text>item1</text>
6. </div>
7. <div class="item" style="background-color: #088684;">
8. <text>item2</text>
9. </div>
10. <div class="item" style="background-color: #7786ee;">
11. <text>item3</text>
12. </div>
13. <div class="item" style="background-color: #c88cee;">
14. <text>item4</text>
15. </div>
16. </swiper>
17. <div class="content">
18. <button class="pnbtn" onclick="previous">Previous</button>
19. <select onchange="selectChange">
20. <option value="0">swipeTo 1</option>
21. <option value="1">swipeTo 2</option>
22. <option value="2">swipeTo 3</option>
23. <option value="3">swipeTo 4</option>
24. </select>
25. <button class="pnbtn" onclick="next">Next</button>
26. </div>
27. </div>
```

```
1. /* xxx.css */
2. .container{
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. background-color: #F1F3F5;
7. align-items: center;
8. justify-content: center;
9. }
10. swiper{
11. height: 30%;
12. }
13. .item{
14. width: 100%;
15. height: 500px;
16. }
17. text{
18. width: 100%;
19. height: 100%;
20. text-align: center;
21. font-size: 50px;
22. color: white;
23. }
24. select{
25. background-color: white;
26. width: 250px;
27. height: 80px;
28. }
29. .content{
30. margin-top: 100px;
31. justify-content: space-around;
32. }
33. .pnbtn{
34. width: 200px;
35. height: 80px;
36. font-size: 30px;
37. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction';
3. export default{
4. change(e){
5. promptAction.showToast({duration:2000,message:"current index:"+e.index});
6. },
7. finish(){
8. promptAction.showToast({duration:2000,message:"切换动作结束"});
9. },
10. selectChange(e){
11. this.$element('swiper').swipeTo({index: Number(e.newValue)});
12. },
13. previous(){
14. this.$element('swiper').showPrevious();
15. },
16. next(){
17. this.$element('swiper').showNext();
18. }
19. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/hGZEzakTQHinIpJp_2ZrSg/zh-cn_image_0000002552798448.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234024Z&HW-CC-Expire=86400&HW-CC-Sign=F8FD4B8AB185619B7D520E246FBD3B197B370885236D2A74C95643AE3FE2F7A0)

## 场景示例

本场景中使用swiper创建一个轮播图，在轮播图底部制作一个缩略图，点击缩略图后调用swipeTo方法切换到对应的轮播图。

```
1. <!-- xxx.hml-->
2. <div class="container">
3. <swiper duration="500" indicator="false" id="swiper" onchange="change">
4. <div class="item" for="item in list">
5. <image src="{{item.src}}"></image>
6. </div>
7. </swiper>
8. <div class="content">
9. <div class="content_item {{index == $idx?'activated':''}}" for="item in list" onclick="imageTo({{$idx}})">
10. <image src="{{item.src}}"></image>
11. </div>
12. </div>
13. </div>
```

```
1. /* xxx.css */
2. .container{
3. flex-direction: column;
4. background-color: #F1F3F5;
5. align-items: center;
6. justify-content: center;
7. width: 100%;
8. }
9. swiper{
10. width: 100%;
11. height: 500px;
12. }
13. .item{
14. width: 100%;
15. height: 500px;
16. }
17. .content{
18. margin-top: -120px;
19. width: 70%;
20. display: flex;
21. justify-content: space-around;
22. height: 100px;
23. }
24. .content_item{
25. padding: 5px;
26. transform: scale(0.5);
27. }
28. .activated{
29. transform: scale(1);
30. border: 1px solid #b20937ea;
31. }
```

```
1. // xxx.js
2. export default {
3. data:{
4. index: 0,
5. list:[
6. {src: 'common/images/1.png'},
7. {src: 'common/images/2.png'},
8. {src: 'common/images/3.png'},
9. {src: 'common/images/4.png'},]
10. },
11. imageTo(index){
12. this.index = index;
13. this.$element('swiper').swipeTo({index: index});
14. },
15. change(e){
16. this.index = e.index;
17. }
18. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/xN-uYVYUQ5O4Jj6VwwAJXQ/zh-cn_image_0000002583438143.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234024Z&HW-CC-Expire=86400&HW-CC-Sign=E55F2D5686ACFA47E66C427A96F3B4C14988D3466AF5F5032672EF73DB2B6F2C)
