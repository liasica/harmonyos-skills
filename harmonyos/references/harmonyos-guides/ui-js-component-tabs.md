---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-component-tabs
title: tabs开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 容器组件 > tabs开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:25+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:dee8d48643c9812420ec9b25720382dac113a6dcaf281683f32c51c7848f9283
---

tabs是一种常见的界面导航结构。通过页签容器，用户可以快捷地访问应用的不同模块。具体用法请参考[tabs API](../harmonyos-references/js-components-container-tabs.md)。

## 创建tabs

在pages/index目录下的hml文件中创建一个tabs组件。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <tabs>
4. <tab-bar>
5. <text>item1</text>
6. <text>item2</text>
7. </tab-bar>
8. <tab-content class="tabContent">
9. <div class="text">
10. <text>content1</text>
11. </div>
12. <div class="text">
13. <text>content2</text>
14. </div>
15. </tab-content>
16. </tabs>
17. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. justify-content: center;
5. align-items: center;
6. background-color: #F1F3F5;
7. }
8. .tabContent{
9. width: 100%;
10. height: 100%;
11. }
12. .text{
13. width: 100%;
14. height: 100%;
15. justify-content: center;
16. align-items: center;
17. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/jHu3RVEQSlG1Bv7wJ9yflg/zh-cn_image_0000002583438139.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234023Z&HW-CC-Expire=86400&HW-CC-Sign=7B6EF5284BC2CBE47565F7246309FC0E83633C9DCDD4F5049690BE3AD3D9FC95)

## 设置样式

设置tabs背景色及边框和tab-content布局。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <tabs class="tabs">
4. <tab-bar class="tabBar">
5. <text class="tabBarItem">item1</text>
6. <text class="tabBarItem">item2</text>
7. </tab-bar>
8. <tab-content class="tabContent">
9. <div class="tabContent">
10. <text>content1</text>
11. </div>
12. <div class="tabContent" >
13. <text>content2</text>
14. </div>
15. </tab-content>
16. </tabs>
17. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. justify-content: flex-start;
5. align-items: center;
6. background-color:#F1F3F5;
7. }
8. .tabs{
9. margin-top: 20px;
10. border: 1px solid #2262ef;
11. width: 99%;
12. padding: 10px;
13. }
14. .tabBar{
15. width: 100%;
16. border: 1px solid #78abec;
17. }
18. .tabContent{
19. width: 100%;
20. margin-top: 10px;
21. height: 300px;
22. color: blue;
23. justify-content: center;
24. align-items: center;
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/-KOzb-DkQqiKG8gEWdJBZw/zh-cn_image_0000002552958094.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234023Z&HW-CC-Expire=86400&HW-CC-Sign=183063B1BEB226CAE981177607A79E9A451ACE75FAB0E6C443E49EEDBCFA9B63)

## 显示页签索引

开发者可以为tabs添加change事件，实现页签切换后显示当前页签索引的功能。

```
1. <!-- xxx.hml -->
2. <div class="container" style="background-color:#F1F3F5;">
3. <tabs class="tabs" onchange="tabChange">
4. <tab-bar class="tabBar">
5. <text class="tabBarItem">item1</text>
6. <text class="tabBarItem">item2</text>
7. </tab-bar>
8. <tab-content class="tabContent">
9. <div>
10. <image src="common/images/bg-tv.jpg" style="object-fit: contain;"> </image>
11. </div>
12. <div>
13. <image src="common/images/img1.jpg" style="object-fit: contain;"> </image>
14. </div>
15. </tab-content>
16. </tabs>
17. </div>
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction';
3. export default {
4. tabChange(e){
5. promptAction.showToast({
6. message: "Tab index: " + e.index
7. })
8. }
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/fiBr-b7iTjq8ya_e9XaYuw/zh-cn_image_0000002583478095.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234023Z&HW-CC-Expire=86400&HW-CC-Sign=C65FC73F4548004B92692D4EED45A7E04EA3C66CC6084F0AE0C6B07AAF082CFB)

说明

tabs子组件仅支持一个[<tab-bar>](../harmonyos-references/js-components-container-tab-bar.md)和一个[<tab-content>](../harmonyos-references/js-components-container-tab-content.md)。

## 场景示例

在本场景中，开发者可以点击标签切换内容，选中后标签文字颜色变红，并显示下划线。

用tabs、tab-bar和tab-content实现点击切换功能，再定义数组，设置属性。使用change事件改变数组内的属性值实现变色及下划线的显示。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <tabs onchange="changeTabactive">
4. <tab-content>
5. <div class="item-container" for="data.list">
6. <div if="{{$item.title=='List1'?true:false}}">
7. <image src="common/images/bg-tv.jpg" style="object-fit: contain;"> </image>
8. </div>
9. <div if="{{$item.title=='List2'?true:false}}">
10. <image src="common/images/img1.jpg" style="object-fit: none;"> </image>
11. </div>
12. <div if="{{$item.title=='List3'?true:false}}">
13. <image src="common/images/img2.jpg" style="object-fit: contain;"> </image>
14. </div>
15. </div>
16. </tab-content>
17. <tab-bar class="tab_bar mytabs" mode="scrollable">
18. <div class="tab_item" for="data.list">
19. <text style="color: {{$item.color}};">{{$item.title}}</text>
20. <div class="underline-show" if="{{$item.show}}"></div>
21. <div class="underline-hide" if="{{!$item.show}}"></div>
22. </div>
23. </tab-bar>
24. </tabs>
25. </div>
```

```
1. /* xxx.css */
2. .container{
3. width: 100%;
4. height: 100%;
5. background-color:#F1F3F5;
6. }
7. .tab_bar {
8. width: 100%;
9. height: 150px;
10. }
11. .tab_item {
12. height: 30%;
13. flex-direction: column;
14. align-items: center;
15. }
16. .tab_item text {
17. font-size: 32px;
18. }
19. .item-container {
20. justify-content: center;
21. flex-direction: column;
22. }
23. .underline-show {
24. height: 2px;
25. width: 160px;
26. background-color: #FF4500;
27. margin-top: 7.5px;
28. }
29. .underline-hide {
30. height: 2px;
31. margin-top: 7.5px;
32. width: 160px;
33. }
```

```
1. // xxx.js
2. export default {
3. data() {
4. return {
5. data: {
6. color_normal: '#878787',
7. color_active: '#ff4500',
8. show: true,
9. list: [{
10. i: 0,
11. color: '#ff4500',
12. show: true,
13. title: 'List1'
14. }, {
15. i: 1,
16. color: '#878787',
17. show: false,
18. title: 'List2'
19. }, {
20. i: 2,
21. color: '#878787',
22. show: false,
23. title: 'List3'
24. }]
25. }
26. }
27. },
28. changeTabactive (e) {
29. for (let i = 0; i < this.data.list.length; i++) {
30. let element = this.data.list[i];
31. element.show = false;
32. element.color = this.data.color_normal;
33. if (i === e.index) {
34. element.show = true;
35. element.color = this.data.color_active;
36. }
37. }
38. }
39. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/pLjPlVlWR9SfRrvRLhteFw/zh-cn_image_0000002552798446.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234023Z&HW-CC-Expire=86400&HW-CC-Sign=BC9418AAFE71570CFDB87B926DE3655559EA71B4AAE6B66CC25B33CC88E9658C)
