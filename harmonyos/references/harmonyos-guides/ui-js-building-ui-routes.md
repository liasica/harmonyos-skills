---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-building-ui-routes
title: 页面路由
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 构建用户界面 > 页面路由
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:23+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:97cf8b86ada734b863440290f476878888347cf01b6c7d3104f920489b3e43fb
---

很多应用由多个页面组成，比如用户可以从音乐列表页面点击歌曲，跳转到该歌曲的播放界面。开发者需要通过页面路由将这些页面串联起来，按需实现跳转。

页面路由router根据页面的uri找到目标页面，从而实现跳转。以最基础的两个页面之间的跳转为例，具体实现步骤如下：

1. 在“Project“窗口，打开src > main >js >MainAbility，右键点击pages文件夹，选择NewJS Page，创建一个详情页。
2. 调用router.push()路由到详情页。
3. 调用router.back()回到首页。

## 构建页面布局

index和detail这两个页面均包含一个text组件和button组件：text组件用来指明当前页面，button组件用来实现两个页面之间的相互跳转。hml文件代码示例如下：

```
1. <!-- index.hml -->
2. <div class="container">
3. <text class="title">This is the index page.</text>
4. <button type="capsule" value="Go to the second page" class="button" onclick="launch"></button>
5. </div>
```

```
1. <!-- detail.hml -->
2. <div class="container">
3. <text class="title">This is the detail page.</text>
4. <button type="capsule" value="Go back" class="button" onclick="launch"></button>
5. </div>
```

## 构建页面样式

构建index和detail页面的页面样式，text组件和button组件居中显示，两个组件之间间距为50px。css代码如下（两个页面样式代码一致）：

```
1. /* index.css */
2. /* detail.css */
3. .container {
4. width: 100%;
5. height: 100%;
6. flex-direction: column;
7. justify-content: center;
8. align-items: center;
9. }

11. .title {
12. font-size: 50px;
13. margin-bottom: 50px;
14. }
```

## 实现跳转

为了使button组件的launch方法生效，需要在页面的js文件中实现跳转逻辑。调用router.push()接口将uri指定的页面添加到路由栈中，即跳转到uri指定的页面。在调用router方法之前，需要导入router模块。代码示例如下：

```
1. // index.js
2. import router from '@ohos.router';
3. export default {
4. launch() {
5. router.push ({
6. url: 'pages/detail/detail',
7. });
8. },
9. }
```

```
1. // detail.js
2. import router from '@ohos.router';
3. export default {
4. launch() {
5. this.getUIContext().getRouter().back();
6. },
7. }
```

运行效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/pHtFio-bSBi2vtTWQMy4ew/zh-cn_image_0000002583478085.png?HW-CC-KV=V1&HW-CC-Date=20260427T234022Z&HW-CC-Expire=86400&HW-CC-Sign=316B2CFA34A06C337AA247E968785EF175FC88AEEEFF9B83084F219D088AD3C2)
