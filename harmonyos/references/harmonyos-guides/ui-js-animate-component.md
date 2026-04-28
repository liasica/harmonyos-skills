---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-animate-component
title: 组件动画
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 动效开发指导 > JS动画 > 组件动画
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:34+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8cd4a55455d9abb43a76d0c3dc36906f132fc1c83dbe44eaab192dc767ab7885
---

在组件上创建和运行动画的快捷方式。具体用法请参考[通用方法](../harmonyos-references/js-components-common-methods.md)。

## 获取动画对象

通过调用animate方法获得animation对象，animation对象支持动画属性、动画方法和动画事件。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div id="content" class="box" onclick="Show"></div>
4. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. justify-content: center;
5. align-items: center;
6. width: 100%;
7. }
8. .box{
9. width: 200px;
10. height: 200px;
11. background-color: #ff0000;
12. margin-top: 30px;
13. }
```

```
1. /* xxx.js */
2. export default {
3. data: {
4. animation: '',
5. options: {},
6. frames: {}
7. },
8. onInit() {
9. this.options = {
10. duration: 1500,
11. };
12. this.frames = [
13. {
14. width: 200, height: 200,
15. },
16. {
17. width: 300, height: 300,
18. }
19. ];
20. },
21. Show() {
22. this.animation = this.$element('content').animate(this.frames, this.options); //获取动画对象
23. this.animation.play();
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/rRNvqGNlQ0eNyqIOXyEpwQ/zh-cn_image_0000002583438193.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234033Z&HW-CC-Expire=86400&HW-CC-Sign=C762B104AEAFCEC2058EFC715E2B8297EEF0E17C575A7F3E6FE0737E4269DA0F)

说明

* 使用animate方法时必须传入Keyframes和Options参数。
* 多次调用animate方法时，采用replace策略，即最后一次调用时传入的参数生效。

## 设置动画参数

在获取动画对象后，通过设置参数Keyframes设置动画在组件上的样式。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div id="content" class="box" onclick="Show"></div>
4. </div>
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
9. .box{
10. width: 200px;
11. height: 200px;
12. background-color: #ff0000;
13. margin-top: 30px;
14. }
```

```
1. /* xxx.js */
2. export default {
3. data: {
4. animation: '',
5. keyframes:{},
6. options:{}
7. },
8. onInit() {
9. this.options = {
10. duration: 4000,
11. }
12. this.keyframes = [
13. {
14. transform: {
15. translate: '-120px -0px',
16. scale: 1,
17. rotate: 0
18. },
19. transformOrigin: '100px 100px',
20. offset: 0.0,
21. width: 200,
22. height: 200
23. },
24. {
25. transform: {
26. translate: '120px 0px',
27. scale: 1.5,
28. rotate: 90
29. },
30. transformOrigin: '100px 100px',
31. offset: 1.0,
32. width: 300,
33. height: 300
34. }
35. ]
36. },
37. Show() {
38. this.animation = this.$element('content').animate(this.keyframes, this.options)
39. this.animation.play()
40. }
41. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/77Vm5_eQSsur6Z0ZmpkCAw/zh-cn_image_0000002552958148.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234033Z&HW-CC-Expire=86400&HW-CC-Sign=7BB559621DE9DD92FB11AD9AE6D827AAC4B9D002110F2B0BBB57881D08951BDC)

说明

* translate、scale和rotate的先后顺序会影响动画效果。
* transformOrigin只对scale和rotate起作用。

在获取动画对象后，通过设置参数Options来设置动画的属性。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div id="content" class="box" onclick="Show"></div>
4. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. justify-content: center;
5. align-items: center;
6. width: 100%;
7. }
8. .box{
9. width: 200px;
10. height: 200px;
11. background-color: #ff0000;
12. margin-top: 30px;
13. }
```

```
1. /* xxx.js */
2. export default {
3. data: {
4. animation: '',
5. options: {},
6. frames: {}
7. },
8. onInit() {
9. this.options = {
10. duration: 1500,
11. easing: 'ease-in',
12. delay: 5,
13. iterations: 2,
14. direction: 'normal',
15. };
16. this.frames = [
17. {
18. transform: {
19. translate: '-150px -0px'
20. }
21. },
22. {
23. transform: {
24. translate: '150px 0px'
25. }
26. }
27. ];
28. },
29. Show() {
30. this.animation = this.$element('content').animate(this.frames, this.options);
31. this.animation.play();
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/FHCRMFjGTAGOV-JUt3I1sQ/zh-cn_image_0000002583478149.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234033Z&HW-CC-Expire=86400&HW-CC-Sign=A330984CA77F968A501F7DB265E59857C8583D9B916D838518EDA57DAA28445C)

说明

direction：指定动画的播放模式。

normal： 动画正向循环播放。

reverse： 动画反向循环播放。

alternate：动画交替循环播放，奇数次正向播放，偶数次反向播放。

alternate-reverse：动画反向交替循环播放，奇数次反向播放，偶数次正向播放。
