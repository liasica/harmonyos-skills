---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-menu
title: menu开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > menu开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:28+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:599761b4608cce3df0e775869684ad33dc7234a250489f6958e444fec09ac60e
---

提供菜单组件，作为临时性弹出窗口，用于展示用户可执行的操作，具体用法请参考[menu](../harmonyos-references/js-components-basic-menu.md)。

## 创建menu组件

在pages/index目录下的hml文件中创建一个menu组件，添加target、type、title属性。

```
1. <!-- xxx.hml-->
2. <div class="container">
3. <text class="title-text" id="textId">show menu</text>
4. <menu target="textId" type="click" title="title">
5. <option value="Item 1">Item 1</option>
6. <option value="Item 2">Item 2</option>
7. <option value="Item 3">Item 3</option>
8. </menu>
9. </div>
```

```
1. /* xxx.css */
2. .container{
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. background-color: #F1F3F5;
7. align-items: center;
8. justify-content: center;
9. width: 100%;
10. }
11. .title-text{
12. font-size: 35px;
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/vxpTTtPcQdGFvzkvhjDNTQ/zh-cn_image_0000002583478123.png?HW-CC-KV=V1&HW-CC-Date=20260427T234027Z&HW-CC-Expire=86400&HW-CC-Sign=EDDE7E3752BC7867E2710D0A7658481CCF9FD5112A8756E1F60A96174023C9D1)

说明

* menu仅支持[option](../harmonyos-references/js-components-basic-option.md)子组件。
* menu组件不支持focusable、disabled属性。

## 设置样式

为menu组件设置样式，例如字体颜色、大小、字符间距等。

```
1. <!-- xxx.hml-->
2. <div class="container">
3. <text class="title-text" id="textId">show menu</text>
4. <menu target="textId" type="click" title="title">
5. <option value="Item 1">Item 1</option>
6. <option value="Item 2">Item 2</option>
7. <option value="Item 3">Item 3</option>
8. </menu>
9. </div>
```

```
1. /* xxx.css */
2. .container{
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. background-color: #F1F3F5;
7. align-items: center;
8. justify-content: center;
9. width: 100%;
10. }
11. .title-text{
12. font-size: 35px;
13. background-color: #5a5aee;
14. color: white;
15. width: 70%;
16. text-align: center;
17. height: 85px;
18. border-radius: 12px;
19. }
20. .menu{
21. text-color: blue;
22. font-size: 35px;
23. letter-spacing: 2px;
24. }
25. option{
26. color: #6a6aef;
27. font-size: 30px;
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/mET2Vt1fRXWrzJ0EQpLT2A/zh-cn_image_0000002552798474.png?HW-CC-KV=V1&HW-CC-Date=20260427T234027Z&HW-CC-Expire=86400&HW-CC-Sign=012294239EB25088BB4D417A189F0C305B90AF9B7D8BA7BDDFB8E79E8DD96B39)

## 绑定事件

为menu组件绑定oncancel事件（取消操作时触发）。

```
1. <!-- xxx.hml-->
2. <div class="container">
3. <text  class="title-text" id="textId" onclick="textClick">show menu</text>
4. <menu  title="title" oncancel="cancel" id="menuId">
5. <option value="Item 1">Item 1</option>
6. <option value="Item 2">Item 2</option>
7. <option value="Item 3">Item 3</option>
8. </menu>
9. </div>
```

```
1. /* xxx.css */
2. .container{
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. background-color: #F1F3F5;
7. width: 100%;
8. }
9. .title-text{
10. font-size: 35px;
11. background-color: #5a5aee;
12. color: white;
13. width: 70%;
14. text-align: center;
15. height: 85px;
16. border-radius: 12px;
17. margin-top: 500px;
18. margin-left: 15%;
19. }
20. menu{
21. text-color: blue;
22. font-size: 35px;
23. letter-spacing: 2px;
24. }
25. option{
26. color: #6a6aef;
27. font-size: 30px;
28. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction';
3. export default {
4. cancel() {
5. promptAction.showToast({
6. message: "cancel"
7. })
8. },
9. textClick() {
10. this.$element("menuId").show({ x: 175,y: 590 });
11. }
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/PA1xpzdDRC-BG1dsbcEqpg/zh-cn_image_0000002583438169.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234027Z&HW-CC-Expire=86400&HW-CC-Sign=18431DFFA8E4EF0AB4146B8C31090F34393A743A45912A7D7D2C757B6391974E)
