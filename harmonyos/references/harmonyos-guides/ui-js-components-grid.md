---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-grid
title: 栅格布局
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 栅格布局
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:31+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b33a8906b22bc0799fabf74363176f28a979563990bf45c187ec65df17a171de
---

栅格布局容器根节点，使用grid-row与grid-col进行栅格布局。API具体描述请参考[grid-container](../harmonyos-references/js-components-grid-container.md)。

## 创建grid-container组件

在pages/index目录下的hml文件中创建一个grid-container组件，并添加[grid-row](../harmonyos-references/js-components-grid-row.md)子组件。

```
1. <!-- index.hml -->
2. <div class="container">
3. <grid-container id="mygrid" gutter="20px" style="background-color: pink;">
4. <grid-row style="height:100px;justify-content:space-around;width: 80%;background-color: #f67002;margin-left:
5. 10%;"></grid-row>
6. <grid-row style="height:300px;justify-content:space-around;background-color: #ffcf00;width: 100%;"></grid-row>
7. <grid-row style="height:150px;justify-content:space-around;background-color: #032cf8;width: 100%;"></grid-row>
8. </grid-container>
9. </div>
```

```
1. /* xxx.css */
2. .container{
3. flex-direction: column;
4. background-color: #F1F3F5;
5. margin-top: 500px;
6. justify-content: center;
7. align-items: center;
8. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/tGiMii3NRSOq7Cyne9E4gA/zh-cn_image_0000002552798488.png?HW-CC-KV=V1&HW-CC-Date=20260427T234030Z&HW-CC-Expire=86400&HW-CC-Sign=AFBE7563F60B9F13A9C7DCE4AAF57A313F38B0EBA3D140DA07A10D59E5500FA7)

说明

grid-container仅支持grid-row为子组件。

## 调用方法

以下示例中，通过点击grid-container组件调用getColumns、getColumnWidth、getGutterWidth方法以返回栅格容器列数、column宽度及gutter宽度，通过长按调用getSizeType方法以返回当前容器响应尺寸类型（xs|sm|md|lg）。

```
1. <!-- index.hml -->
2. <div class="container">
3. <grid-container id="mygrid" gutter="20px" style="background-color: pink;padding-top: 100px;"
4. onclick="getColumns" onlongpress="getSizeType">
5. <grid-row style="height:100px;justify-content:space-around;background-color: #4cedf3;width: 20%;margin-left:
6. 40%;"></grid-row>
7. <grid-row style="height:150px;justify-content:space-around;background-color: #4cbff3;width: 50%;margin-left:
8. 25%;"></grid-row>
9. <grid-row style="height:200px;justify-content:space-around;background-color: #465ff6;width: 80%;margin-left:
10. 10%;"></grid-row>
11. <grid-row style="height:200px;justify-content:space-around;background-color: #5011ec;width: 100%;"></grid-row>
12. </grid-container>
13. </div>
```

```
1. /* xxx.css */
2. .container{
3. flex-direction: column;
4. background-color: #F1F3F5;
5. margin-top: 400px;
6. justify-content: center;
7. align-items: center;
8. }
```

```
1. // index.js
2. import promptAction from '@ohos.promptAction';
3. export default {
4. data:{
5. gutterWidth:'',
6. columnWidth:'',
7. columns:'',
8. },
9. getColumns(){
10. this.$element('mygrid').getColumnWidth((result)=>{
11. this.columnWidth = result;
12. })
13. this.$element('mygrid').getGutterWidth((result)=>{
14. this.gutterWidth = result;
15. })
16. this.$element('mygrid').getColumns((result)=>{
17. this.columns= result;
18. })
19. setTimeout(()=>{
20. promptAction.showToast({duration:5000,message:'columnWidth:'+this.columnWidth+',gutterWidth:'+
21. this.gutterWidth+',getColumns:'+this.columns})
22. })
23. },
24. getSizeType(){
25. this.$element('mygrid').getSizeType((result)=>{
26. promptAction.showToast({duration:2000,message:'get size type:'+result})
27. })
28. },
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/1J3NVeEJQEqwmX3NE7CqGA/zh-cn_image_0000002583438183.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234030Z&HW-CC-Expire=86400&HW-CC-Sign=08E8907B50BEB86381723B8926B1A3127B484DF446E426DAA9B5BB1D10A2B478)

## 添加grid-col

创建grid-container组件并添加grid-row，在grid-row组件内添加[grid-col](../harmonyos-references/js-components-grid-col.md)组件形成布局。

```
1. <!-- index.hml -->
2. <div class="container">
3. <grid-container id="mygrid" columns="4" gutter="0" style="background-color: pink;" onclick="getColumns" onlongpress="getSizeType">
4. <grid-row style="height: 100px;justify-content: space-around;background-color: #4cbff3;width: 100%;">
5. <grid-col span="0">
6. <div style="align-items: center;justify-content: center;height: 100%;width: 100%;">
7. <text style="color: dodgerblue;" onclick="getCol">top</text>
8. </div>
9. </grid-col>
10. </grid-row>
11. <grid-row style="height:500px;justify-content:space-around;background-color: #3b55ef;width: 100%;">
12. <grid-col span="0" style="width: 20%;">
13. <div style="align-items: center;justify-content: center;height: 100%;width: 100%;">
14. <text style="color: dodgerblue;">left</text>
15. </div>
16. </grid-col>
17. <grid-col span="0" style="background-color:orange;width: 80%;">
18. <div style="width: 100%;height: 100%;align-items: center;justify-content: center;">
19. <text>right</text>
20. </div>
21. </grid-col>
22. </grid-row>
23. <grid-row style="height: 100px;justify-content: space-around;background-color: #4cbff3;width: 100%;">
24. <grid-col style="background-color:#c075ef;" span="0">
25. <div style="width: 100%;height: 100%;padding: 20px;align-items: center;justify-content: center;">
26. <text>bottom</text>
27. </div>
28. </grid-col>
29. </grid-row>
30. </grid-container>
31. </div>
```

```
1. /* xxx.css */
2. .container{
3. flex-direction: column;
4. background-color: #F1F3F5;
5. width: 100%;
6. height: 100%;
7. justify-content: center;
8. align-items: center;
9. }
10. text{
11. color: white;
12. font-size: 40px;
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/LkmSjPxlTa2MLy_LESKIrA/zh-cn_image_0000002552958138.png?HW-CC-KV=V1&HW-CC-Date=20260427T234030Z&HW-CC-Expire=86400&HW-CC-Sign=8C4089A647A66165CAF7DC50CA4240072C701635D1F3F0BD87B5289ACC24388C)

说明

grid-row仅支持grid-col为子组件，只能在grid-col组件中添加填充的内容。

## 场景示例

本场景中循环输出list中的内容，创建出网格布局。进行下拉操作时触发refresh（刷新页面）方法，这时会向list数组中添加一条数据并设置setTimeout（延迟触发），达到刷新请求数据的效果。

```
1. <!-- index.hml -->
2. <div class="container">
3. <refresh refreshing="{{fresh}}" onrefresh="refresh">
4. <grid-container id="mygrid" gutter="20" style="margin: 10px;">
5. <grid-row style="height:200px;width: 100%;background-color: #e7e7e2;margin-top: 50px; padding: 0px 20px;border-radius: 15px;" for="item in list">
6. <grid-col span="0" style="width: 40%;">
7. <div style="align-items: center;justify-content: center">
8. <image src="{{item.src}}" style="object-fit: contain;border-radius: 30px;"></image>
9. </div>
10. </grid-col>
11. <grid-col span="0" style="width: 60%;">
12. <div style="align-items: center;justify-content: center;width: 100%;height: 100%;text-align: center;">
13. <text>image{{item.id}}</text>
14. </div>
15. </grid-col>
16. </grid-row>
17. </grid-container>
18. </refresh>
19. </div>
```

```
1. /* xxx.css */
2. .container{
3. flex-direction: column;
4. background-color: #F1F3F5;
5. width: 100%;
6. height: 100%;
7. }
8. text{
9. color: #0a0aef;
10. font-size: 60px;
11. }
```

```
1. // index.js
2. import promptAction from '@ohos.promptAction';
3. export default {
4. data:{
5. list:[
6. {src:'common/images/1.png',id:'1'},
7. {src:'common/images/2.png',id:'2'},
8. {src:'common/images/3.png',id:'3'}
9. ],
10. fresh:false
11. },
12. refresh(e) {
13. promptAction.showToast({
14. message: 'refreshing'
15. })
16. var that = this;
17. that.fresh = e.refreshing;
18. setTimeout(function () {
19. that.fresh = false;
20. that.list.unshift({src: 'common/images/4.png',id:'4'});
21. promptAction.showToast({
22. message: 'succeed'
23. })
24. }, 2000)
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/zuYCOYN8TTi0kNyIT5FVlg/zh-cn_image_0000002583478139.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234030Z&HW-CC-Expire=86400&HW-CC-Sign=CE7E78742121502A9D2D801900BE55936B91B4BA10722B5CABB30A4563BA9FC9)
