---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-building-ui-interactions
title: 添加交互
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 构建用户界面 > 添加交互
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:22+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6fbed71dc38d5fc43f310add44e08c6495e5a7eca1bfc3ba7f29b3e9fa2ef776
---

添加交互可以通过在组件上关联事件实现。本节将介绍如何用div、text、image组件关联click事件，构建一个如下图所示的点赞按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/m1kusfLsQdeSRcNTgneXDw/zh-cn_image_0000002583478083.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234021Z&HW-CC-Expire=86400&HW-CC-Sign=B74F792435539A38B3C0401D948B4AE9A1B167DD19E2D3488EC532CF27EA3216)

点赞按钮通过一个div组件关联click事件实现。div组件包含一个image组件和一个text组件：

* image组件用于显示未点赞和点赞的效果。click事件函数会交替更新点赞和未点赞图片的路径。
* text组件用于显示点赞数，点赞数会在click事件的函数中同步更新。

click事件作为一个函数定义在js文件中，可以更改isPressed的状态，从而更新显示的image组件。如果isPressed为真，则点赞数加1。该函数在hml文件中对应的div组件上生效，点赞按钮各子组件的样式设置在css文件当中。具体的实现示例如下：

```
1. <!-- xxx.hml -->
2. <!-- 点赞按钮 -->
3. <div>
4. <div class="like" onclick="likeClick">
5. <image class="like-img" src="{{likeImage}}" focusable="true"></image>
6. <text class="like-num" focusable="true">{{total}}</text>
7. </div>
8. </div>
```

```
1. /* xxx.css */
2. .like {
3. width: 104px;
4. height: 54px;
5. border: 2px solid #bcbcbc;
6. justify-content: space-between;
7. align-items: center;
8. margin-left: 72px;
9. border-radius: 8px;
10. }
11. .like-img {
12. width: 33px;
13. height: 33px;
14. margin-left: 14px;
15. }
16. .like-num {
17. color: #bcbcbc;
18. font-size: 20px;
19. margin-right: 17px;
20. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. likeImage: '/common/unLike.png',
5. isPressed: false,
6. total: 20,
7. },
8. likeClick() {
9. var temp;
10. if (!this.isPressed) {
11. temp = this.total + 1;
12. this.likeImage = '/common/like.png';
13. } else {
14. temp = this.total - 1;
15. this.likeImage = '/common/unLike.png';
16. }
17. this.total = temp;
18. this.isPressed = !this.isPressed;
19. },
20. }
```

除此之外，还提供了很多表单组件，例如开关、标签、滑动选择器等，以便于开发者在页面布局时灵活使用和提高交互性。
