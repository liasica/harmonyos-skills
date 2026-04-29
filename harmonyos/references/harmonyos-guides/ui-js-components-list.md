---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-list
title: list开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 容器组件 > list开发指导
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:45+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6055a9c0ee22a5ecb3a2c37f3a4ec931b8dcfae94ec8a759a0bccdeb64a3bd6f
---

list是用来显示列表的组件，包含一系列相同宽度的列表项，适合连续、多行地呈现同类数据。具体用法请参考[list API](../harmonyos-references/js-components-container-list.md)。

## 创建list组件

在pages/index目录下的hml文件中创建一个list组件。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <list>
4. <list-item class="listItem"></list-item>
5. <list-item class="listItem"></list-item>
6. <list-item class="listItem"></list-item>
7. <list-item class="listItem"></list-item>
8. </list>
9. </div>
```

```
1. /* xxx.css */
2. .container {
3. width:100%;
4. height:100%;
5. flex-direction: column;
6. align-items: center;
7. background-color: #F1F3F5;
8. }
9. .listItem{
10. height: 20%;
11. background-color:#d2e0e0;
12. margin-top: 20px;
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/EtJtINm6TnqBwmypQqjrDA/zh-cn_image_0000002558764576.png?HW-CC-KV=V1&HW-CC-Date=20260429T052844Z&HW-CC-Expire=86400&HW-CC-Sign=0D4241F47D9A2BD0027270CE0116CB04CBCB62DE8E1E37748F62EC8CE64D902C)

说明

* <list-item-group>是<list>的子组件，实现列表分组功能，不能再嵌套<list>，可以嵌套<list-item>。
* <list-item>是<list>的子组件，展示列表的具体项。

## 添加滚动条

设置scrollbar属性为on即可在屏幕右侧生成滚动条，实现长列表或者屏幕滚动等效果。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <list class="listCss" scrollbar="on" >
4. <list-item class="listItem"></list-item>
5. <list-item class="listItem"></list-item>
6. <list-item class="listItem"></list-item>
7. <list-item class="listItem"></list-item>
8. <list-item class="listItem"></list-item>
9. <list-item class="listItem"></list-item>
10. </list>
11. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. background-color: #F1F3F5;
5. }
6. .listItem{
7. height: 20%;
8. background-color:#d2e0e0;
9. margin-top: 20px;
10. }
11. .listCss{
12. height: 100%;
13. scrollbar-color: #8e8b8b;
14. scrollbar-width: 50px;
15. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/3Qi1qrTbQxOZ35s1erEZVg/zh-cn_image_0000002558604920.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052844Z&HW-CC-Expire=86400&HW-CC-Sign=62D1E8F124D11CD6830683C1B6053238878C370BB6229F9F941FAC9949A282E1)

## 添加侧边索引栏

设置indexer属性为自定义索引时，索引栏会显示在列表右边界处，indexer属性设置为true，默认为字母索引表。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <list class="listCss"  indexer="{{['#','1','2','3','4','5','6','7','8']}}" >
4. <list-item class="listItem"  section="#" ></list-item>
5. </list>
6. </div>
```

```
1. /* xxx.css */
2. .container{
3. flex-direction: column;
4. background-color: #F1F3F5;
5. }
6. .listCss{
7. height: 100%;
8. flex-direction: column;
9. columns: 1
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/MsMS8D0FRXCmGFb_qMiUcg/zh-cn_image_0000002589324445.png?HW-CC-KV=V1&HW-CC-Date=20260429T052844Z&HW-CC-Expire=86400&HW-CC-Sign=9357C82299F7D73BCAF3BD50C0CF360D54CF27052AC208BB88A36FF65D779752)

说明

* indexer属性生效需要flex-direction属性配合设置为column，且columns属性设置为1。
* indexer可以自定义索引表，自定义时"#"必须要存在。

## 实现列表折叠和展开

为list组件添加groupcollapse和groupexpand事件实现列表的折叠和展开。

```
1. <!-- xxx.hml -->
2. <div class="doc-page">
3. <list style="width: 100%;" id="mylist">
4. <list-item-group for="listgroup in list" id="{{listgroup.value}}" ongroupcollapse="collapse" ongroupexpand="expand">
5. <list-item type="item" style="background-color:#FFF0F5;height:95px;">
6. <div class="item-group-child">
7. <text>One---{{listgroup.value}}</text>
8. </div>
9. </list-item>
10. <list-item type="item" style="background-color: #87CEFA;height:145px;" primary="true">
11. <div class="item-group-child">
12. <text>Primary---{{listgroup.value}}</text>
13. </div>
14. </list-item>
15. </list-item-group>
16. </list>
17. </div>
```

```
1. /* xxx.css */
2. .doc-page {
3. flex-direction: column;
4. background-color: #F1F3F5;
5. }
6. .list-item {
7. margin-top:30px;
8. }
9. .top-list-item {
10. width:100%;
11. background-color:#D4F2E7;
12. }
13. .item-group-child {
14. justify-content: center;
15. align-items: center;
16. width:100%;
17. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction';
3. export default {
4. data: {
5. direction: 'column',
6. list: []
7. },
8. onInit() {
9. this.list = []
10. this.listAdd = []
11. for (var i = 1; i <= 2; i++) {
12. var dataItem = {
13. value: 'GROUP' + i,
14. };
15. this.list.push(dataItem);
16. }
17. },
18. collapse(e) {
19. promptAction.showToast({
20. message: 'Close ' + e.groupid
21. })
22. },
23. expand(e) {
24. promptAction.showToast({
25. message: 'Open ' + e.groupid
26. })
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/nKjwNLksRlmDpSptT750og/zh-cn_image_0000002589244385.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052844Z&HW-CC-Expire=86400&HW-CC-Sign=4B7D13C2BA201B99A98AFDC57F01DD549B778C27670C9793B8DFA7F9DBBFD59D)

说明

* groupcollapse和groupexpand事件仅支持list-item-group组件使用。

## 场景示例

在本场景中，开发者可以根据字母索引表查找对应联系人。

```
1. <!-- xxx.hml -->
2. <div class="doc-page">
3. <text style="font-size: 35px; font-weight: 500; text-align: center; margin-top: 20px; margin-bottom: 20px;">
4. <span>Contacts</span>
5. </text>
6. <list class="list" indexer="true">
7. <list-item class="item" for="{{namelist}}" type="{{$item.section}}" section="{{$item.section}}">
8. <div class="container">
9. <div class="in-container">
10. <text class="name">{{$item.name}}</text>
11. <text class="number">18888888888</text>
12. </div>
13. </div>
14. </list-item>
15. <list-item type="end" class="item">
16. <div style="align-items:center;justify-content:center;width:750px;">
17. <text style="text-align: center;">Total: 10</text>
18. </div>
19. </list-item>
20. </list>
21. </div>
```

```
1. /* xxx.css */
2. .doc-page {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. background-color: #F1F3F5;
7. }
8. .list {
9. width: 100%;
10. height: 90%;
11. flex-grow: 1;
12. }
13. .item {
14. height: 120px;
15. padding-left: 10%;
16. border-top: 1px solid #dcdcdc;
17. }
18. .name {
19. color: #000000;
20. font-size: 39px;
21. }
22. .number {
23. color: black;
24. font-size: 25px;
25. }
26. .container {
27. flex-direction: row;
28. align-items: center;
29. }
30. .in-container {
31. flex-direction: column;
32. justify-content: space-around;
33. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. namelist:[{
5. name: 'Zoey',
6. section:'Z'
7. },{
8. name: 'Quin',
9. section:'Q'
10. },{
11. name:'Sam',
12. section:'S'
13. },{
14. name:'Leo',
15. section:'L'
16. },{
17. name:'Zach',
18. section:'Z'
19. },{
20. name:'Wade',
21. section:'W'
22. },{
23. name:'Zoe',
24. section:'Z'
25. },{
26. name:'Warren',
27. section:'W'
28. },{
29. name:'Kyle',
30. section:'K'
31. },{
32. name:'Zaneta',
33. section:'Z'
34. }]
35. },
36. onInit() {
37. }
38. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/F2lzmYT3RveZCVsUie3ytA/zh-cn_image_0000002558764578.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052844Z&HW-CC-Expire=86400&HW-CC-Sign=2A9E9AA6824A0A4D9A1117339A8DB9FB391F17184E5420B24CCAA7BADDE0CE31)
