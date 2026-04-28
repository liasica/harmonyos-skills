---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-building-ui-layout-external-container
title: 添加容器
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 构建用户界面 > 构建布局 > 添加容器
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:22+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:021743dfac9b28c3d1fdfd96f7126db37738777b8421ece6f2a536ea4edb72bf
---

要将页面的基本元素组装在一起，需要使用容器组件。在页面布局中常用到三种容器组件，分别是div、list和tabs。在页面结构相对简单时，可以直接用div作为容器，因为div作为单纯的布局容器，可以支持多种子组件，使用起来更为方便。

## List组件

当页面结构较为复杂时，如果使用div循环渲染，容易出现卡顿，因此推荐使用list组件代替div组件实现长列表布局，从而实现更加流畅的列表滚动体验。需要注意的是，list仅支持list-item作为子组件，具体的使用示例如下：

```
1. <!-- xxx.hml -->
2. <list class="list">
3. <list-item type="listItem" for="{{textList}}">
4. <text class="desc-text">{{$item.value}}</text>
5. </list-item>
6. </list>
```

```
1. /* xxx.css */
2. .desc-text {
3. width: 683.3px;
4. font-size: 35.4px;
5. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. textList:  [{value: 'JS FA'}],
5. },
6. }
```

为避免示例代码过长，以上示例的list中只包含一个list-item，list-item中只有一个text组件。在实际应用中可以在list中加入多个list-item，同时list-item下可以包含多个其他子组件。

## Tabs组件

当页面经常需要动态加载时，推荐使用tabs组件。tabs组件支持change事件，在页签切换后触发。tabs组件仅支持一个tab-bar和一个tab-content。具体的使用示例如下：

```
1. <!-- xxx.hml -->
2. <tabs>
3. <tab-bar>
4. <text>Home</text>
5. <text>Index</text>
6. <text>Detail</text>
7. </tab-bar>
8. <tab-content>
9. <image src="{{homeImage}}"></image>
10. <image src="{{indexImage}}"></image>
11. <image src="{{detailImage}}"></image>
12. </tab-content>
13. </tabs>
```

```
1. // xxx.js
2. export default {
3. data: {
4. homeImage: '/common/home.png',
5. indexImage: '/common/index.png',
6. detailImage: '/common/detail.png',
7. },
8. }
```

tab-content组件用来展示页签的内容区，高度默认充满tabs剩余空间。
