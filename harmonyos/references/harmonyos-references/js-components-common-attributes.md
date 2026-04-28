---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-attributes
title: 通用属性
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 组件通用信息 > 通用属性
category: harmonyos-references
scraped_at: 2026-04-28T08:02:52+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ff0007f37a9a2f2a8cbc7bd1a5a3b3eb8131dd78f4ef01d12a9f9b94d50570c5
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 常规属性

PhonePC/2in1TabletTVWearable

常规属性是指组件普遍支持的用来设置组件基本标识和外观显示特征的属性。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| id | string | - | 否 | 组件的唯一标识。 |
| style | string | - | 否 | 组件的样式声明。 |
| class | string | - | 否 | 组件的样式类，用于引用样式表。 |
| ref | string | - | 否 | 用来指定指向子元素或子组件的引用信息，该引用将注册到父组件的$refs 属性对象上。 |
| disabled | boolean | false | 否 | 当前组件是否被禁用，在禁用场景下，组件将无法响应用户交互。设置为true时，组件不响应交互事件。设置为false时，组件响应交互事件。 |
| data | string | - | 否 | 给当前组件设置data属性，进行相应的数据存储和读取。JS文件中：  - 在事件回调中使用 e.target.attr.data 读取数据，e为事件回调函数入参。  - 使用$element或者$refs获取DOM元素后，通过attr.data 进行访问。  从API version 6 开始，建议使用data-\*。 |
| data-\*6+ | string | - | 否 | 给当前组件设置data-\*属性，进行相应的数据存储和读取。大小写不敏感，如data-A和data-a默认相同。JS文件中：  - 在事件回调中使用 e.target.dataSet.a读取数据，e为事件回调函数入参。  - 使用$element或者$refs获取DOM元素后，通过dataSet.a进行访问。 |
| click-effect5+ | string | - | 否 | 通过这个属性可以设置组件的弹性点击效果，当前支持如下三种效果：  - spring-small：建议小面积组件设置，缩放(90%)。  - spring-medium：建议中面积组件设置，缩放(95%)。  - spring-large：建议大面积组件设置，缩放(95%)。 |
| dir6+ | string | auto | 否 | 设置元素布局模式，支持设置rtl、ltr和auto三种属性值：  - rtl：使用从右往左布局模式。  - ltr：使用从左往右布局模式。  - auto：跟随系统语言环境。 |

## 渲染属性

PhonePC/2in1TabletTVWearable

渲染属性是指组件普遍支持的用来设置组件是否渲染的属性。

| 名称 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| for | Array | - | 根据设置的数据列表，展开当前元素。 |
| if | boolean | - | 根据设置的boolean值，添加或移除当前元素。true表示添加当前元素，false表示移除当前元素。 |
| show | boolean | - | 根据设置的boolean值，显示或隐藏当前元素。true表示显示当前元素，false表示隐藏当前元素。 |

说明

属性和样式不能混用，不能在属性字段中进行样式设置。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div id="container">
3. <button class="btn" type="capsule" value="toggleDisplay" onclick="toggleDisplay"></button>
4. <list class="list">
5. <list-item for="{{ array }}" class="listItem">
6. <text class="text" onclick="toggleShow" show="{{ visible }}"
7. if="{{ display }}">{{ $item.value }}</text>
8. </list-item>
9. </list>
10. </div>
```

```
1. /* xxx.css */
2. #container {
3. flex-direction: column;
4. width: 100%;
5. margin-top: 10px;
6. }
7. .text {
8. font-size: 50px;
9. font-weight: 500;
10. margin-left: 12px;
11. }
12. .listItem {
13. width: 100%;
14. height: 100px;
15. line-height: 60px;
16. border-bottom: 1px solid #DEDEDE;
17. font-size: 20px;
18. }
19. .btn{
20. width: 280px;
21. font-size: 26px;
22. margin: 10px 0;
23. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. visible: true,
5. display: true,
6. title: "",
7. i: 4,
8. array: [
9. {"value": "列表文本0"},
10. {"value": "列表文本1"},
11. {"value": "列表文本2"},
12. {"value": "列表文本3"},
13. ],
14. },
15. toggleShow: function() {
16. this.array.push({"value": "列表文本" + this.i })
17. this.i++
18. },
19. toggleDisplay: function() {
20. this.display = !this.display
21. },
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/HiNTOIy2TkOAGQ5gMwnIbA/zh-cn_image_0000002552800520.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000251Z&HW-CC-Expire=86400&HW-CC-Sign=94F223F70EB7C979E3D907B8B85245A15F3A9A1948EA856C305A0464EDA5E8AF)

### 示例2

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div>
4. <text class="text1" dir='rtl' >hello world</text>
5. </div>
6. <div>
7. <text class="text2" dir='ltr' >hello world</text>
8. </div>
9. </div>
```

```
1. /* xxx.css */
2. .container {
3. display: flex;
4. flex-direction: column;
5. justify-content: center;
6. align-items: center;
7. width: 100%;
8. height: 100%;
9. }
10. .text1{
11. width: 90%;
12. height: 100px;
13. background-color: aqua;
14. }
15. .text2{
16. width: 90%;
17. height: 100px;
18. background-color: blue;
19. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/QaOxYMoZQ_u-5i8L0lp9qQ/zh-cn_image_0000002583440215.png?HW-CC-KV=V1&HW-CC-Date=20260428T000251Z&HW-CC-Expire=86400&HW-CC-Sign=A20BE4ACF7CE558F25AF09B25DDDBF170E3ACEAA7B54512CC81D26BB1C6B819B)
