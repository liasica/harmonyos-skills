---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-transition
title: 转场样式
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 组件通用信息 > 转场样式
category: harmonyos-references
scraped_at: 2026-04-28T08:02:54+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0f32a5463d59418951d2acd9c1acfa097ae8bdfd66c1d0a14a4099c33994103c
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 共享元素转场

PhonePC/2in1TabletTVWearable

### 属性

PhonePC/2in1TabletTVWearable

| 名称 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| shareid | string | 无 | 进行共享元素转场时使用，若不配置，则转场样式不生效。共享元素转场当前支持的组件：[list-item](js-components-container-list-item.md)、[image](js-components-basic-image.md)、[text](js-components-basic-text.md)、[button](js-components-basic-button.md)、[label](js-components-basic-label.md)。 |

### 样式

PhonePC/2in1TabletTVWearable

| 名称 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| shared-transition-effect | string | exchange | 配置共享元素转场时的入场样式。  - exchange（默认值）：源页面元素移动到目的页元素位置，并进行适当缩放。  - static：目的页元素位置不变，用户可配置透明度动画。当前仅跳转目标页配置的static效果生效。 |
| shared-transition-name | string | - | 转场时，目的页配置的样式优先生效。该样式用于配置共享元素的动画效果，一个由@keyframes定义的动画序列，支持transform和透明度动画。若共享元素效果与自定义的动画冲突，以自定义动画为准。 |
| shared-transition-timing-function | string | friction | 转场时，目的页配置的样式优先生效。该属性定义了共享元素转场时的插值曲线。若不配置，默认使用friction曲线。 |

### 注意事项

PhonePC/2in1TabletTVWearable

1. 若同时配置了共享元素转场和自定义页面转场样式，页面转场效果以自定义效果为准。
2. 共享元素的exchange效果类似下图。

   **图1** 共享元素转场默认效果

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/4bdmpHlNRXCl9YeRKbIYNw/zh-cn_image_0000002552800526.png?HW-CC-KV=V1&HW-CC-Date=20260428T000253Z&HW-CC-Expire=86400&HW-CC-Sign=EE6729D6A900A5932FE246E1F687938606A8F9B208D53699DF83D57FEF4F801B)
3. 共享元素动画对元素的边框、背景色不生效。
4. 共享元素转场时，由于页面元素会被隐藏，故页面元素配置的动画样式/动画方法失效。
5. 动态修改shareid5+：若组件A的shareid被组件B的shareid覆盖，组件A的共享元素效果将失效。即使后续修改组件B的shareid，组件A的共享元素效果也不会恢复。

### 示例

PhonePC/2in1TabletTVWearable

PageA跳转到PageB，跳转的共享元素为image， shareid为“shareImage”。

```
1. <!-- PageA -->
2. <!-- xxx.hml -->
3. <div>
4. <list>
5. <list-item type="description">
6. <image src="item.jpg" shareid="shareImage" onclick="jump" class="shared-transition-style"></image>
7. </list-item>
8. <list-item>
9. <text onclick="jump">Click on picture to jump to the details</text>
10. </list-item>
11. </list>
12. </div>
```

```
1. // xxx.js
2. import router from '@ohos.router';
3. export default {
4. jump() {
5. router.push({
6. // 路径要与config.json配置里面的相同
7. url: 'pages/detailpage',
8. });
9. },
10. }
```

```
1. /* xxx.css */
2. .shared-transition-style {
3. shared-transition-effect: exchange;
4. shared-transition-name: shared-transition;
5. }
6. @keyframes shared-transition {
7. from { opacity: 0; }
8. to { opacity: 1; }
9. }
```

```
1. <!-- PageB -->
2. <!-- xxx.hml -->
3. <div>
4. <image src="itemDetail.jpg" shareid="shareImage" onclick="jumpBack" class="shared-transition-style"></image>
5. </div>
```

```
1. // xxx.js
2. import router from '@ohos.router';
3. export default {
4. jumpBack() {
5. router.back();
6. },
7. }
```

```
1. /* xxx.css */
2. .shared-transition-style {
3. shared-transition-effect: exchange;
4. shared-transition-name: shared-transition;
5. }
6. @keyframes shared-transition {
7. from { opacity: 0; }
8. to { opacity: 1; }
9. }
```

## 卡片转场样式

PhonePC/2in1TabletTVWearable

说明

卡片转场无法和其他转场(包括共享元素转场和自定义转场)共同使用。

### 样式

PhonePC/2in1TabletTVWearable

| 名称 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| transition-effect | string | - | 用于配置当前页面中的某个组件在卡片转场过程中是否进行转场动效，当前支持如下配置：  - unfold：配置这个属性的组件，如在卡片的上方，则向上移动一个卡片的高度，如在卡片的下方，则向下移动一个卡片的高度。  - none：转场过程中没有动效。 |

### 示例

PhonePC/2in1TabletTVWearable

source\_page包含顶部内容以及卡片列表，点击卡片可以跳转到target\_page。

```
1. <!-- source_page -->
2. <!-- xxx.hml -->
3. <div class="container">
4. <div class="outer">
5. <text style="font-size: 23px; margin-bottom: 20px" >MAIN TITLE</text>
6. </div>
7. <list style="width:340px;height:600px;flex-direction:column;justify-content:center;align-items:center">
8. <list-item type="listItem" class="item" card="true" for="list" id="{{$item.id}}" onclick="jumpPage({{$item.id}}, {{$item.url}})">
9. <text style="margin-left: 10px; font-size: 23px;">{{$item.title}}</text>
10. </list-item>
11. </list>
12. </div>
```

```
1. // xxx.js
2. import router from '@ohos.router';
3. export default {
4. data: { list: [] },
5. onInit() {
6. for(var i = 0; i < 10; i++) {
7. var item = { url: "pages/card_transition/target_page/index",
8. title: "this is title" + i, id: "item_" + i }
9. this.list.push(item);
10. }
11. },
12. jumpPage(id, url) {
13. var cardId = this.$element(id).ref;
14. router.push({ url: url, params : { ref : cardId } });
15. }
16. }
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. align-items: center;
7. background-color: #ABDAFF;
8. }
9. .item {
10. height: 80px;
11. background-color: #FAFAFA;
12. margin-top: 2px;
13. }
14. .outer {
15. width: 300px;
16. height: 100px;
17. align-items: flex-end;
18. transition-effect: unfold;
19. }
```

```
1. <!-- target_page -->
2. <!-- xxx.hml -->
3. <div class="container">
4. <div class="div">
5. <text style="font-size: 30px">this is detail</text>
6. </div>
7. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. align-items: center;
7. background-color: #EBFFD7;
8. }
9. .div {
10. height: 600px;
11. flex-direction: column;
12. align-items: center;
13. justify-content: center;
14. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/_seWuembSjOhlMoBy_nOmg/zh-cn_image_0000002583440221.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000253Z&HW-CC-Expire=86400&HW-CC-Sign=82B2698AAD17614124561AC7EC53ED7AABE3464ADDA2C3D063367C235ACE9C07)

## 页面转场样式

PhonePC/2in1TabletTVWearable

### 样式

PhonePC/2in1TabletTVWearable

| 名称 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| transition-enter | string | - | 与@keyframes配套使用，支持transform和透明度动画，详见[动画样式 表2 @keyframes属性说明](js-components-common-animation.md)。 |
| transition-exit | string | - | 与@keyframes配套使用，支持transform和透明度动画，详见[动画样式 表2 @keyframes属性说明](js-components-common-animation.md)。 |
| transition-duration | string | 跟随设备默认的页面转场时间 | 支持的单位为[s(秒)|ms(毫秒) ]，默认单位为ms，未配置时使用系统默认值。 |
| transition-timing-function | string | friction | 描述转场动画执行的速度曲线，用于使转场更为平滑。详细参数见[动画样式](js-components-common-animation.md)中“animation-timing-function”有效值说明。 |

### 注意事项

PhonePC/2in1TabletTVWearable

1. 配置自定义转场时，建议配置页面背景色为不透明颜色，否则在转场过程中可能会出现衔接不自然的现象。
2. transition-enter和transition-exit可单独配置，没有配置时使用系统默认的参数。
3. transition-enter/transition-exit说明如下：

   a. push场景下：进入页面栈的Page2.js应用transition-enter描述的动画配置；进入页面栈第二位置的Page1.js应用transition-exit描述的动画配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/ME9QvmabTv2g12fYwrMJqw/zh-cn_image_0000002552960176.png?HW-CC-KV=V1&HW-CC-Date=20260428T000253Z&HW-CC-Expire=86400&HW-CC-Sign=024213C18CAFD46531CBC4729B5D018DB7B97E9DDAD48435E3C7741E39B4CA04)

   b. back场景下：退出页面栈的Page2.js应用transition-enter描述的动画配置，并进行倒播；从页面栈第二位置进入栈顶位置的Page1.js应用transition-exit描述的动画配置，并进行倒播。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/Avr57fswTFaE5-gVrzEM7A/zh-cn_image_0000002583480177.png?HW-CC-KV=V1&HW-CC-Date=20260428T000253Z&HW-CC-Expire=86400&HW-CC-Sign=B6B20E29D789351997BA48F28D56FA652AFA7853E10B07F7DA430C4992F9E49A)

### 示例

PhonePC/2in1TabletTVWearable

Page1有一个不透明盒子，点击盒子会跳转到Page2，当点击Page2中的盒子，会回退到Page1页面。

1. Page1

   ```
   1. <!-- xxx.hml -->
   2. <div class="container">
   3. <text>index</text>
   4. <div class="move_page" onclick="jump"></div>
   5. </div>
   ```

   ```
   1. // xxx.js
   2. import router from '@ohos.router';
   3. export default {
   4. data: {

   6. },
   7. jump() {
   8. router.push({
   9. url:'pages/transition2/transition2'
   10. })
   11. }
   12. }
   ```

   ```
   1. /* xxx.css */
   2. .container {
   3. flex-direction: column;
   4. justify-content: center;
   5. align-items: center;
   6. width: 100%;
   7. height: 100%;
   8. }
   9. .move_page {
   10. width: 100px;
   11. height: 100px;
   12. background-color: #72d3fa;
   13. transition-enter: go_page;
   14. transition-exit: exit_page;
   15. transition-duration: 5s;
   16. transition-timing-function: friction;
   17. }

   19. @keyframes go_page {
   20. from {
   21. opacity: 0;
   22. transform: translate(0px) rotate(60deg) scale(1.0);
   23. }

   25. to {
   26. opacity: 1;
   27. transform: translate(100px) rotate(360deg) scale(1.0);
   28. }
   29. }
   30. @keyframes exit_page {
   31. from {
   32. opacity: 1;
   33. transform: translate(200px) rotate(60deg) scale(2);
   34. }

   36. to {
   37. opacity: 0;
   38. transform: translate(200px) rotate(360deg) scale(2);
   39. }
   40. }
   ```
2. Page2

   ```
   1. <!-- xxx.hml -->
   2. <div class="container">
   3. <text>transition</text>
   4. <div class="move_page" onclick="jumpBack"></div>
   5. </div>
   ```

   ```
   1. // xxx.js
   2. import router from '@ohos.router';
   3. export default {
   4. data: {

   6. },
   7. jumpBack() {
   8. router.back()
   9. }
   10. }
   ```

   ```
   1. /* xxx.css */
   2. .container {
   3. flex-direction: column;
   4. justify-content: center;
   5. align-items: center;
   6. width: 100%;
   7. height: 100%;
   8. }

   10. .move_page {
   11. width: 100px;
   12. height: 100px;
   13. background-color: #f172fa;
   14. transition-enter: go_page;
   15. transition-exit: exit_page;
   16. transition-duration: 5s;
   17. transition-timing-function: ease;
   18. }

   20. @keyframes go_page {
   21. from {
   22. opacity: 0;
   23. transform:translate(100px) rotate(0deg) scale(1.0);
   24. }
   25. to {
   26. opacity: 1;
   27. transform:translate(100px) rotate(180deg) scale(2.0);
   28. }
   29. }

   31. @keyframes exit_page {
   32. from {
   33. opacity: 1;
   34. transform: translate(0px) rotate(60deg) scale(1);
   35. }
   36. to {
   37. opacity: 0;
   38. transform: translate(0px) rotate(360deg) scale(1);
   39. }
   40. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/3GD7L367T3i97SBM3efDDQ/zh-cn_image_0000002552800528.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000253Z&HW-CC-Expire=86400&HW-CC-Sign=3A3F8A33F7E11383C34845EE27B976BC5569DCF84ECCC9D32F670422C72C8897)
