---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-text
title: text开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > text开发指导
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:47+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:773d6cd1ddaeed72d9a27aeec9204f4b58ca4f24db2e461c7b06c6586029a71a
---

text是文本组件，用于呈现一段文本信息。具体用法请参考[text](../harmonyos-references/js-components-basic-text.md)的API文档。

## 创建text组件

在pages/index目录下的hml文件中创建一个text组件。

```
1. <!-- xxx.hml -->
2. <div class="container" style="text-align: center;justify-content: center; align-items: center;">
3. <text>Hello World</text>
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
8. background-color: #F1F3F5;
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/zbIQnrKaQmOqUt3eO4JQnA/zh-cn_image_0000002589324457.png?HW-CC-KV=V1&HW-CC-Date=20260429T052846Z&HW-CC-Expire=86400&HW-CC-Sign=198404074BFB09C13F9FB11ED5B144B1AE619D1F31365B459D92C0FE72DF4F48)

## 设置text组件样式和属性

* 添加文本样式

  设置color、font-size、allow-scale、word-spacing、text-align属性分别为文本添加颜色、大小、缩放、文本之间的间距和文本在水平方向的对齐方式。

  ```
  1. <!-- xxx.hml -->
  2. <div class="container" style="background-color:#F1F3F5;flex-direction: column;justify-content: center; align-items: center;">
  3. <text style="color: blueviolet; font-size: 40px; allow-scale:true">
  4. This is a passage
  5. </text>
  6. <text style="color: blueviolet; font-size: 40px; margin-top: 20px; allow-scale:true;word-spacing: 20px;text-align: center">
  7. This is a passage
  8. </text>
  9. </div>
  ```

  ```
  1. /* xxx.css */
  2. .container {
  3. display: flex;
  4. width: 100%;
  5. height: 100%;
  6. flex-direction: column;
  7. align-items: center;
  8. justify-content: center;
  9. background-color: #F1F3F5;
  10. }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/pN3U4MRxRAeMvPVFNzM_RQ/zh-cn_image_0000002589244397.png?HW-CC-KV=V1&HW-CC-Date=20260429T052846Z&HW-CC-Expire=86400&HW-CC-Sign=890C7B4F9BD0B7DD141E3CEE36217154C0D0FC5B604AFED33D920B7205684F0F)
* 添加划线

  设置text-decoration和text-decoration-color属性为文本添加划线和划线颜色，text-decoration枚举值请参考 text自有样式。

  ```
  1. <!-- xxx.hml -->
  2. <div class="container" style="background-color:#F1F3F5;">
  3. <text style="text-decoration:underline">
  4. This is a passage
  5. </text>
  6. <text style="text-decoration:line-through;text-decoration-color: red">
  7. This is a passage
  8. </text>
  9. </div>
  ```

  ```
  1. /* xxx.css */
  2. .container {
  3. width: 100%;
  4. height: 100%;
  5. flex-direction: column;
  6. align-items: center;
  7. justify-content: center;
  8. }
  9. text{
  10. font-size: 50px;
  11. }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/N8wrox4KQjGC78IMGBBwZg/zh-cn_image_0000002558764590.png?HW-CC-KV=V1&HW-CC-Date=20260429T052846Z&HW-CC-Expire=86400&HW-CC-Sign=9320261A0873BEEF1CE930BD1FBBCDC1B1AFD7253AD970FFBBC2DC09CE1AF6DE)
* 隐藏文本内容

  当文本内容过多而显示不全时，添加text-overflow属性将隐藏内容以省略号的形式展现。

  ```
  1. <!-- xxx.hml -->
  2. <div class="container">
  3. <text class="text">
  4. This is a passage
  5. </text>
  6. </div>
  ```

  ```
  1. /* xxx.css */
  2. .container {
  3. width: 100%;
  4. height: 100%;
  5. flex-direction: column;
  6. align-items: center;
  7. background-color: #F1F3F5;
  8. justify-content: center;
  9. }
  10. .text{
  11. width: 200px;
  12. max-lines: 1;
  13. text-overflow:ellipsis;
  14. }
  ```

  说明

  + text-overflow样式需配合max-lines样式使用，在设置了最大行数的情况下才会生效。
  + max-lines属性设置文本最多可以展示的行数。

  ​ ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/Rzf81ZIAQB2T94epZj5QZQ/zh-cn_image_0000002558604934.png?HW-CC-KV=V1&HW-CC-Date=20260429T052846Z&HW-CC-Expire=86400&HW-CC-Sign=D6A2B2040C1BDCC599EDE45C21876CEB30EBCEE3CD7CC25BAF47D3F702B0FAE9)
* text组件支持[span](../harmonyos-references/js-components-basic-span.md)子组件

  ```
  1. <!-- xxx.hml -->
  2. <div class="container" style="justify-content: center; align-items: center;flex-direction: column;background-color: #F1F3F5;  width: 100%;height: 100%;">
  3. <text style="font-size: 45px;">
  4. This is a passage
  5. </text>
  6. <text style="font-size: 45px;">
  7. <span style="color: aqua;">This </span><span style="color: #F1F3F5;">      1
  8. </span>
  9. <span style="color: blue;"> is a </span>    <span style="color: #F1F3F5;">      1    </span>
  10. <span style="color: red;">  passage </span>
  11. </text>
  12. </div>
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/D9zdnR6kRZ2J_iCqMwcV7g/zh-cn_image_0000002589324459.png?HW-CC-KV=V1&HW-CC-Date=20260429T052846Z&HW-CC-Expire=86400&HW-CC-Sign=35B1364EB8B17529DF8C1E5C1FF40CF04E5D248A1F8D5D219B7BBE5AFBB126CA)

  说明

  + 当使用span子组件组成文本段落时，如果span属性样式异常（例如：font-weight设置为1000），将导致文本段落显示异常。
  + 在使用span子组件时，注意text组件内不能存在文本内容，如果在text组件同时包含文本内容和span子组件，则仅会显示子组件span中的内容。

## 场景示例

text组件通过数据绑定展示文本内容，span组件通过设置show属性来实现文本内容的隐藏和显示。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div style="align-items: center;justify-content: center;">
4. <text class="title">
5. {{ content }}
6. </text>
7. <switch checked="true" onchange="test"></switch>
8. </div>
9. <text class="span-container" style="color: #ff00ff;">
10. <span show="{{isShow}}">  {{ content  }}  </span>
11. <span style="color: white;">
12. 1
13. </span>
14. <span style="color: #f76160">Hide clip </span>
15. </text>
16. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. align-items: center;
6. flex-direction: column;
7. justify-content: center;
8. background-color: #F1F3F5;
9. }
10. .title {
11. font-size: 26px;
12. text-align:center;
13. width: 200px;
14. height: 200px;
15. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. isShow:true,
5. content: 'Hello World'
6. },
7. onInit(){    },
8. test(e) {
9. this.isShow = e.checked
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/smg7mui8Qkiv0RqjfYL9Lg/zh-cn_image_0000002589244399.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052846Z&HW-CC-Expire=86400&HW-CC-Sign=4389ED8F73F7F6429D9F25A5C76C635AC85634931948AC9EBB3DC7086F2ABBBE)
