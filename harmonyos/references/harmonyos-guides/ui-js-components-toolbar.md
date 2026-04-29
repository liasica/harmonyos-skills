---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-toolbar
title: toolbar开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > toolbar开发指导
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:50+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:21ca0cb36374f14b3cd11fff64c0d93fe9e44c9cd42bfd53c675ede86feaa497
---

toolbar为页面工具栏组件，用于展示针对当前界面的操作选项，可作为页面的一级导航。具体用法请参考[toolbar](../harmonyos-references/js-components-basic-toolbar.md)。

## 创建toolbar组件

在pages/index目录下的hml文件中创建一个toolbar组件。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <toolbar style="background-color: #F1F3F5;">
4. <toolbar-item value="item1"></toolbar-item>
5. <toolbar-item value="item2"></toolbar-item>
6. </toolbar>
7. </div>
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
10. toolbar-item{
11. font-size: 35px;
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/mQLYaS3eTiepdVx-CdW9Ag/zh-cn_image_0000002589324481.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052848Z&HW-CC-Expire=86400&HW-CC-Sign=DB88CAEAC66F11B2126C792CB5D30E60CF01CE039FBB95218F61F89613E130CE)

## 添加子组件

toolbar组件仅支持toolbar-item为子组件，页面最多可以展示5个toolbar-item子组件，如果存在6个及以上toolbar-item，则保留前面4个，后续的将收纳到工具栏上的更多项中，通过点击更多项弹窗进行展示。并且更多项展示的组件样式采用系统默认样式，toolbar-item上设置的自定义样式不生效。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <toolbar>
4. <toolbar-item value="item1"></toolbar-item>
5. <toolbar-item value="item2"></toolbar-item>
6. <toolbar-item value="item3"></toolbar-item>
7. <toolbar-item value="item4"></toolbar-item>
8. <toolbar-item value="item5"></toolbar-item>
9. <toolbar-item value="item6"></toolbar-item>
10. </toolbar>
11. </div>
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
10. toolbar-item{
11. font-size: 35px;
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/NXw5D1NaQu67uszlhvcRmw/zh-cn_image_0000002589244419.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052848Z&HW-CC-Expire=86400&HW-CC-Sign=3533FC5029794956CA443C8E2E1C1DA553D04EB10CE7686C65B54C1400F49155)

## 设置样式

设置position样式控制toolbar组件的位置，并设置子组件toolbar-item的字体颜色、大小及背景色。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <toolbar style="position: fixed;bottom: 5%;width: 100%;background-color: #F1F3F5;">
4. <toolbar-item value="item1" icon="common/images/1.png" class="toolbarActive"></toolbar-item>
5. <toolbar-item value="item2" icon="common/images/2.png"></toolbar-item>
6. <toolbar-item value="item3" icon="common/images/1.png"></toolbar-item>
7. <toolbar-item value="item4" icon="common/images/2.png"></toolbar-item>
8. </toolbar>
9. </div>
```

```
1. /* xxx.css */
2. .container {
3. background-color: #F1F3F5;
4. flex-direction: column;
5. width: 100%;
6. height: 100%;
7. justify-content: center;
8. align-items: center;
9. }
10. toolbar-item{
11. font-size: 35px;
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/BV5C1xxjTjGiTHCfzJPTrg/zh-cn_image_0000002558764612.png?HW-CC-KV=V1&HW-CC-Date=20260429T052848Z&HW-CC-Expire=86400&HW-CC-Sign=4E6A1B7C9ACD2F6D5613BFD6E347A14A5ACE94FFF963D2EF367448610AF75DD4)

## 绑定事件

分别给toolbar-item绑定单击事件和长按事件，单击后文本变红，长按时文本变蓝。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <toolbar style="position: fixed;top: 50%;width: 100%;background-color: #F1F3F5;">
4. <toolbar-item value="item1" icon="common/images/1.png" style="color: {{itemColor}};" onclick="itemClick"></toolbar-item>
5. <toolbar-item value="item2" icon="common/images/2.png"  style="color: {{itemColor}}"></toolbar-item>
6. <toolbar-item value="item3" icon="common/images/3.png"  style="color: {{itemColor}}" onlongpress="itemLongPress"></toolbar-item>
7. </toolbar>
8. </div>
```

```
1. /* xxx.css */
2. .container {
3. background-color: #F1F3F5;
4. flex-direction: column;
5. width: 100%;
6. height: 100%;
7. justify-content: center;
8. align-items: center;
9. }
10. toolbar-item{
11. font-size: 35px;
12. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction';
3. export default {
4. data:{
5. itemColor:'black'
6. },
7. itemClick(){
8. this.itemColor= "red";
9. promptAction.showToast({duration:2000,message:'item click'});
10. },
11. itemLongPress(){
12. promptAction.showToast({duration:2000,message:'item long press'});
13. this.itemColor= "blue";
14. },
15. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/Su616zsySteYQdFN4eKpEg/zh-cn_image_0000002558604956.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052848Z&HW-CC-Expire=86400&HW-CC-Sign=7D2237C22B4E1720572F8D46A5B023EFFE3130EEB648849BC2B9BFC24CCC7662)

说明

toolbar组件不支持添加事件和方法，但其子组件toolbar-item支持。

## 场景示例

本场景中开发者可点击toolbar-item组件，改变当前组件文本颜色并更换相对应的图片内容。

使用for循环创建toolbar-item组件并添加点击事件，点击后获得索引值进行存储。设置文本颜色时，判断当前索引值是否为储存的值，若相同则设置为红色，不同则使用默认颜色。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <image src="{{imgList[active]}}"></image>
4. <toolbar style="position: fixed;bottom: 5%;width: 100%;background-color: #F1F3F5;">
5. <toolbar-item value="{{ item.option}}" icon="{{item.icon}}" style="color: {{active == $idx?'red':'black'}};background-color: {{active== $idx?'#dbe7f1':'#F1F3F5'}};" for="{{item in itemList}}" onclick="itemClick({{$idx}})"></toolbar-item>
6. </toolbar>
7. </div>
```

```
1. /* xxx.css */
2. .container {
3. background-color: #F1F3F5;
4. flex-direction: column;
5. width: 100%;
6. justify-content: center;
7. align-items: center;
8. }
9. toolbar-item{
10. font-size: 35px;
11. }
```

```
1. // xxx.js
2. export default {
3. data:{
4. active: 0,
5. imgList:["common/images/1.png","common/images/2.png","common/images/3.png","common/images/4.png"],
6. itemList:[
7. {option:'item1',icon:'common/images/1.png'},
8. {option:'item2',icon:'common/images/2.png'},
9. {option:'item3',icon:'common/images/3.png'},
10. {option:'item4',icon:'common/images/4.png'},
11. ]
12. },
13. itemClick(id){
14. this.active= id;
15. },
16. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/Od8h1unjSLaTybs1Ygqncg/zh-cn_image_0000002589324483.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052848Z&HW-CC-Expire=86400&HW-CC-Sign=F13559E3756E8C468ECCB841BE4238370359BEA6518EB0C197E277EACC60C0A6)
