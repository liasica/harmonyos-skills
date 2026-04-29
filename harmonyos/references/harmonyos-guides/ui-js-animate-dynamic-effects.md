---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-animate-dynamic-effects
title: 动画动效
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 动效开发指导 > JS动画 > 插值器动画 > 动画动效
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:56+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1808b10d5bceeba8dd5b08fd2bc60f4e0de0af9bf7ddb35c7a56130dc8b41b58
---

通过设置插值器来实现动画效果。

## 创建动画对象

通过createAnimator创建一个动画对象，通过设置参数options来设置动画的属性。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div style="width: 300px;height: 300px;margin-top: 100px;background: linear-gradient(pink, purple);transform: translate({{translateVal}});">
4. </div>
5. <div class="row">
6. <button type="capsule" value="play" onclick="playAnimation"></button>
7. </div>
8. </div>
```

```
1. /* xxx.css */
2. .container {
3. width:100%;
4. height:100%;
5. flex-direction: column;
6. align-items: center;
7. justify-content: center;
8. }
9. button{
10. width: 200px;
11. }
12. .row{
13. width: 65%;
14. height: 100px;
15. align-items: center;
16. justify-content: space-between;
17. margin-top: 50px;
18. margin-left: 260px;
19. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. translateVal: 0,
5. animation: null
6. },
7. onInit() {},
8. onShow(){
9. var options = {
10. duration: 3000,
11. easing:"friction",
12. delay:"1000",
13. fill: 'forwards',
14. direction:'alternate',
15. iterations: 2,
16. begin: 0,
17. end: 180
18. }; // 设置参数
19. this.animation = this.getUIContext().createAnimator(options); // 创建动画
20. },
21. playAnimation() {
22. var _this = this;
23. this.animation.onframe = function(value) {
24. _this.translateVal= value;
25. };
26. this.animation.play();
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/RK63UjohRVWdupApiMnKcw/zh-cn_image_0000002558764640.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052855Z&HW-CC-Expire=86400&HW-CC-Sign=DEE45B70C8EFA7AE2E11C2CAFA09E635A6E6D7FF36997614931BFCBA00B132BF)

说明

* 使用createAnimator创建动画对象时必须传入options参数。
* begin插值起点，不设置时默认为0。
* end插值终点，不设置时默认为1。
* 示例代码不支持模拟器运行。

## 添加动画事件和调用接口

animator支持事件和接口，可以通过添加frame、cancel、repeat、finish事件和调用update、play、pause、cancel、reverse、finish接口自定义动画效果。animator支持的事件和接口具体见动画中的[createAnimator](../harmonyos-references/arkts-apis-uicontext-uicontext.md#createanimator)。

```
1. <!-- xxx.hml -->
2. <div style="flex-direction: column;align-items: center;width: 100%;height: 100%;">
3. <div style="width:200px;height: 200px;margin-top: 100px;background: linear-gradient(#b30d29, #dcac1b);
4. transform: scale({{scaleVal}});"></div>
5. <div style="width: {{DivWidth}};height: {{DivHeight}};margin-top: 200px;
6. background: linear-gradient(pink, purple);margin-top: 200px;transform:translateY({{translateVal}});">
7. </div>
8. <div class="row">
9. <button type="capsule" value="play" onclick="playAnimation"></button>
10. <button type="capsule" value="update" onclick="updateAnimation"></button>
11. </div>
12. <div class="row1">
13. <button type="capsule" value="pause" onclick="pauseAnimation"></button>
14. <button type="capsule" value="finish" onclick="finishAnimation"></button>
15. </div>
16. <div class="row2">
17. <button type="capsule" value="cancel" onclick="cancelAnimation"></button>
18. <button type="capsule" value="reverse" onclick="reverseAnimation"></button>
19. </div>
20. </div>
```

```
1. /* xxx.css */
2. button{
3. width: 200px;
4. }
5. .row{
6. width: 65%;
7. height: 100px;
8. align-items: center;
9. justify-content: space-between;
10. margin-top: 150px;
11. position: fixed;
12. top: 52%;
13. left: 120px;
14. }
15. .row1{
16. width: 65%;
17. height: 100px;
18. align-items: center;
19. justify-content: space-between;
20. margin-top: 120px;
21. position: fixed;
22. top: 65%;
23. left: 120px;
24. }
25. .row2{
26. width: 65%;
27. height: 100px;
28. align-items: center;
29. justify-content: space-between;
30. margin-top: 100px;
31. position: fixed;
32. top: 75%;
33. left: 120px;
34. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. scaleVal:1,
5. DivWidth:200,
6. DivHeight:200,
7. translateVal:0,
8. animation: null
9. },
10. onInit() {},
11. onShow() {
12. var options = {
13. duration: 3000,
14. fill: 'forwards',
15. begin: 200,
16. end: 270
17. };
18. this.animation = this.getUIContext().createAnimator(options);
19. var _this= this;
20. // 添加动画重放事件
21. this.animation.onrepeat = function() {
22. this.getUIContext().getPromptAction().showToast({
23. message: 'repeat'
24. });
25. var repeatOptions = {
26. duration: 2000,
27. iterations: 1,
28. direction: 'alternate',
29. begin: 180,
30. end: 240
31. };
32. _this.animation?.update(repeatOptions);
33. _this.animation?.play();
34. };
35. },
36. playAnimation() {
37. var _this= this;
38. // 添加动画逐帧插值回调事件
39. this.animation.onframe = function(value) {
40. _this.scaleVal= value/150,
41. _this.DivWidth = value,
42. _this.DivHeight = value,
43. _this.translateVal = value-180
44. };
45. this.animation.play();
46. },
47. updateAnimation() {
48. var newoptions = {
49. duration: 5000,
50. iterations: 2,
51. begin: 120,
52. end: 180
53. };
54. this.animation.update(newoptions);
55. this.animation.play(); // 调用动画播放接口
56. },
57. pauseAnimation() {
58. this.animation.pause(); // 调用动画暂停接口
59. },
60. finishAnimation() {
61. var _this= this;
62. // 添加动画完成事件
63. this.animation.onfinish = function() {
64. this.getUIContext().getPromptAction().showToast({
65. message: 'finish'
66. });
67. };
68. this.animation.finish(); // 调用动画完成接口
69. },
70. cancelAnimation() {
71. this.animation.cancel(); // 调用动画取消接口
72. },
73. reverseAnimation() {
74. this.animation.reverse(); // 调用动画倒放接口
75. }
76. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/MEFf4sqaTRuwzy1NE1-lAQ/zh-cn_image_0000002558604984.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052855Z&HW-CC-Expire=86400&HW-CC-Sign=CD6D4E25CE334D3CF2253CCD26A8357534E6EFCAE3958EBF10CC26994C2B1B12)

说明

在调用[reset](../harmonyos-references/js-apis-animator.md#reset9)接口的过程中可以使用这个接口更新动画参数，入参与[createAnimator](../harmonyos-references/arkts-apis-uicontext-uicontext.md#createanimator)一致。
