---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-images
title: image开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > image开发指导
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:48+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:74059c9a554ed967057c7ffd1ee444ba2d6af3ee8dd8c682699ca7b2913053ef
---

image是图片组件，用来渲染展示图片。具体用法请参考[image](../harmonyos-references/js-components-basic-image.md)组件。

## 创建image组件

在pages/index目录下的hml文件中创建一个image组件。

```
1. <!-- index.hml -->
2. <div class="container">
3. <image style="height: 30%;" src="common/images/bg-tv.jpg"> </image>
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/F5zAVfp8R4uLCkoDUeXe_g/zh-cn_image_0000002589324467.png?HW-CC-KV=V1&HW-CC-Date=20260429T052847Z&HW-CC-Expire=86400&HW-CC-Sign=24D08600ED91BCE335A6D929F2B5FD4E9ABADEB5B472DA3469E24FEF0236C30A)

## 设置image样式

通过设置width、height和object-fit属性定义图片的宽、高和缩放样式。

```
1. <!-- index.hml -->
2. <div class="container">
3. <image src="common/images/bg-tv.jpg"> </image>
4. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. align-items: center;
7. justify-content: center;
8. background-color:#F1F3F5;
9. }
10. image{
11. width: 80%;
12. height: 500px;
13. border: 5px solid saddlebrown;
14. border-radius: 20px;
15. object-fit: contain;
16. match-text-direction:true;
17. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/0REX6IzyRdu7DA1LB_o-Kw/zh-cn_image_0000002589244407.png?HW-CC-KV=V1&HW-CC-Date=20260429T052847Z&HW-CC-Expire=86400&HW-CC-Sign=75AC77873A77677760D53EC57163AA8FBCD5197B02A9BC240727EFCDEECA3D7E)

## 加载图片

图片成功加载时触发complete事件，返回加载的图源尺寸。加载失败则触发error事件，打印图片加载失败。

```
1. <!-- index.hml -->
2. <div class="container" >
3. <div>
4. <image src="common/images/bg-tv.jpg" oncomplete="imageComplete(1)" onerror="imageError(1)"> </image>
5. </div>
6. <div>
7. <image src="common/images/bg-tv1.jpg" oncomplete="imageComplete(2)" onerror="imageError(2)"> </image>
8. </div>
9. </div>
```

```
1. /* xxx.css */
2. .container{
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. justify-content: center;
7. align-self: center;
8. background-color: #F1F3F5;
9. }
10. .container div{
11. margin-left: 10%;
12. width: 80%;
13. height: 300px;
14. margin-bottom: 40px;
15. }
```

```
1. // index.js
2. import promptAction from '@ohos.promptAction';
3. export default {
4. imageComplete(i,e){
5. promptAction.showToast({
6. message: "image "+i+"'s width"+ e.width+"----image "+i+"'s height"+e.height,
7. duration: 3000,
8. })
9. },
10. imageError(i,e){
11. setTimeout(()=>{
12. promptAction.showToast({
13. message: "Failed to load image "+i+".",
14. duration: 3000,
15. })
16. },3000)
17. }
18. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/T4V7810MS6iCLoIskUiAtg/zh-cn_image_0000002558764600.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052847Z&HW-CC-Expire=86400&HW-CC-Sign=D58EBB597EEC0FB05D632EFFC5C17093B3D8F9D566EC70A4C703107A48DC068B)

## 场景示例

在本场景中，开发者长按图片后将慢慢隐藏图片，当完全隐藏后再重新显示原始图片。定时器setInterval每隔一段时间改变图片透明度,实现慢慢隐藏的效果，当透明度为0时清除定时器，设置透明度为1。

```
1. <!-- index.hml -->
2. <div class="page-container">
3. <div class="content">
4. <div class="image-container">
5. <image class="testimage" src="{{testuri}}" style="opacity:{{imageopacity}};" onlongpress="changeopacity"> </image>
6. </div>
7. <div class="text-container">
8. <text style="font-size: 37px;font-weight:bold;color:orange;text-align: center;width: 100%;">Touch and hold the image</text>
9. </div>
10. </div>
11. </div>
```

```
1. /* xxx.css */
2. .page-container {
3. width: 100%;
4. height: 100%;
5. flex-direction:column;
6. align-self: center;
7. justify-content: center;
8. background-color:#F1F3F5;
9. background-color: #F1F3F5;
10. }
11. .content{
12. flex-direction:column;
13. }
14. .image-container {
15. width: 100%;
16. height: 300px;
17. align-items: center;
18. justify-content: center;
19. }
20. .text-container {
21. margin-top:50px;
22. width: 100%;
23. height: 60px;
24. flex-direction: row;
25. justify-content: space-between;
26. }
27. .testimage {
28. width: 100%;  height: 400px;
29. object-fit: scale-down;
30. border-radius: 20px;
31. }
```

```
1. // index.js
2. import promptAction from '@ohos.promptAction';
3. export default {
4. data: {
5. testuri: 'common/images/bg-tv.jpg',
6. imageopacity:1,
7. timer: null
8. },
9. changeopacity: function () {
10. promptAction.showToast({
11. message: 'Touch and hold the image.'
12. })
13. var opval = this.imageopacity * 20
14. clearInterval(this.timer);
15. this.timer = setInterval(()=>{
16. opval--;
17. this.imageopacity = opval / 20
18. if (opval===0) {
19. clearInterval(this.timer)
20. this.imageopacity = 1
21. }
22. },100);
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/2k1vQcNrSAKnba3tov7jMw/zh-cn_image_0000002558604944.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052847Z&HW-CC-Expire=86400&HW-CC-Sign=E3C552CDD57012C174D1F4576AA136A2B0E007CE9CED094FB4511EC5CE45EAD8)
