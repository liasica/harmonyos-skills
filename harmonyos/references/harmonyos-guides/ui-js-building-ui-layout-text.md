---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-building-ui-layout-text
title: 添加标题行和文本区域
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 构建用户界面 > 构建布局 > 添加标题行和文本区域
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:43+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:19c35e530af3a45fc0b4892a01efcaf003557ca183eb9e2372a5e44fde260567
---

实现标题和文本区域最常用的是基础组件text。text组件用于展示文本，可以设置不同的属性和样式，文本内容需要写在标签内容区，完整属性和样式信息请参考[text](../harmonyos-references/js-components-basic-text.md)。在页面中插入标题和文本区域的示例如下：

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <text class="title-text">{{headTitle}}</text>
4. <text class="paragraph-text">{{paragraphFirst}}</text>
5. <text class="paragraph-text">{{paragraphSecond}}</text>
6. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. margin-top: 20px;
5. margin-left: 30px;
6. }
7. .title-text {
8. color: #1a1a1a;
9. font-size: 50px;
10. margin-top: 40px;
11. margin-bottom: 20px;
12. font-weight: 700;
13. }
14. .paragraph-text {
15. width: 95%;
16. color: #000000;
17. font-size: 35px;
18. line-height: 60px;
19. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. headTitle: 'Capture the Beauty in Moment',
5. paragraphFirst: 'Capture the beauty of light during the transition and fusion of ice and water. At the instant of movement and stillness, softness and rigidity, force and beauty, condensing moving moments.',
6. paragraphSecond: 'Reflecting the purity of nature, the innovative design upgrades your visual entertainment and ergonomic comfort. Effortlessly capture what you see and let it speak for what you feel.',
7. },
8. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/0q2yKO5eT7O03yNL3-xOxg/zh-cn_image_0000002589324441.png?HW-CC-KV=V1&HW-CC-Date=20260429T052842Z&HW-CC-Expire=86400&HW-CC-Sign=F416D789DB18E834E95B71BCDBFF5995574FFA6548A97D82DB2AAA4147FAF4A7)
