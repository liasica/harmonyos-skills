---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-switch
title: switch开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > switch开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:28+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d62b414abf3cb376ebdabc1d261d23e4653fcc680eae9ca2bd3ba82db93e98ca
---

switch为开关选择器，切换开启或关闭状态。具体用法请参考[switch](../harmonyos-references/js-components-basic-switch.md)。

## 创建switch组件

在pages/index目录下的hml文件中创建一个switch组件。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <switch checked="true"></switch>
4. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. background-color: #F1F3F5;
5. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/ezWn2kULTIuBL8WOeF4D4w/zh-cn_image_0000002583478119.png?HW-CC-KV=V1&HW-CC-Date=20260427T234027Z&HW-CC-Expire=86400&HW-CC-Sign=15DF949E847A1858F43294509434B0FAB09EA3B9AB1B27DF9F9A6F46057EF8D3)

## 添加属性和方法

switch组件通过textoff和showtext属性设置文本选中和未选中时的状态。设置checked属性值为true（组件为打开状态）。添加change事件，当组件状态改变时触发，触发后执行switchChange函数获取组件当前状态（关闭/打开）。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <switch showtext="true" texton="open" textoff="close" checked="true" @change="switchChange"></switch>
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
10. switch {
11. texton-color: #002aff;
12. textoff-color: silver;
13. text-padding: 20px;
14. font-size: 50px;
15. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction';
3. export default {
4. switchChange(e){
5. if(e.checked){
6. promptAction.showToast({
7. message: "open"
8. });
9. }else{
10. promptAction.showToast({
11. message: "close"
12. });
13. }
14. }
15. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/M-L2ZheyRTObMZVCxxu8jQ/zh-cn_image_0000002552798470.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234027Z&HW-CC-Expire=86400&HW-CC-Sign=E96F09D63C3EBA332900A600949FF39690F163592D46FF90D09DF25389E01655)

说明

当showtext属性值设置为true时，texton和textoff设置的文本才会生效。

## 场景示例

在下面示例中设置开关为打开状态（使用默认收货地址），关闭开关后页面显示选择地址按钮，点击按钮即可改变收货地址。

实现方法：创建switch开关，设置checked属性为true，通过数据绑定改变收货地址。设置display属性（默认为none），当关闭开关改变display属性值为flex后显示地址模块，点击按钮改变颜色。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div class="change">
4. <text>Choose default address:</text>
5. <switch showtext="true" texton="on" textoff="off" checked="true" @change="switchChange"></switch>
6. </div>
7. <div class="content">
8. <text class="address"><span>Shipping address:</span><span class="textSpan">{{address}}</span></text>
9. </div>
10. <div class="myAddress" style="display: {{addressDisplay}};">
11. <text style="font-size: 30px;margin-bottom: 50px;">Choose an address:</text>
12. <text class="addressText" style="background-color: {{item == address?'#0fabe7':''}};color: {{item == address?'white':'black'}};"
13. for="item in addressList"@click="changeAddress({{$idx}}})">{{item}}</text>
14. </div>
15. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. background-color: #F1F3F5;
6. flex-direction: column;
7. padding: 50px;
8. }
9. .change{
10. margin-top: 20%;
11. width: 100%;
12. justify-content: center;
13. }
14. switch{
15. texton-color: #002aff;
16. textoff-color: silver;
17. text-padding: 20px;
18. }
19. .content{
20. width: 70%;
21. text-align: center;
22. flex-direction: column;
23. border: 1px solid #002aff;
24. margin-left: 15%;
25. text-align: center;
26. }
27. .address{
28. width: 100%;
29. height: 100px;
30. line-height: 100px;
31. text-align: center;
32. font-size: 28px;
33. margin-bottom: 50px;
34. }
35. .textSpan{
36. color: #0aa9f1;
37. }
38. .myAddress{
39. flex-direction: column;
40. margin-top: 50px;
41. }
42. .addressText{
43. margin-left: 35%;
44. width: 30%;
45. height: 75px;
46. text-align: center;
47. color: white;
48. margin-bottom: 30px;
49. border-radius: 10px;
50. border: 1px solid #0fabe7;
51. }
```

```
1. // xxx.js
2. export default {
3. data:{
4. address: '',
5. addressDisplay: 'none',
6. addressList: ['family','company','commissary'],
7. },
8. onInit(){
9. // 初始化默认地址为地址列表中的第一个
10. this.address = this.addressList[0];
11. },
12. switchChange(e){
13. if(e.checked){
14. this.addressDisplay = "none";
15. }else{
16. this.addressDisplay = "flex";
17. }
18. },
19. changeAddress(i){
20. this.address= this.addressList[i];
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/f-ZSSjrQT4yQS7ZG1eqLvg/zh-cn_image_0000002583438165.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234027Z&HW-CC-Expire=86400&HW-CC-Sign=CD3093A5312ADF97A78F7C762B07F3D38C4B340B37C4FFA3A1135D4461D89912)
