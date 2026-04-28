---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-animate-frame
title: 动画帧
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 动效开发指导 > JS动画 > 插值器动画 > 动画帧
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:35+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d0db3305d4aea53d47ee00f3aba5b0148e333e628d8ea66eed22a34cb89ec5c8
---

## 请求动画帧

请求动画帧时通过requestAnimationFrame函数逐帧回调，传入一个回调函数。

runframe在调用requestAnimationFrame时传入带有timestamp参数的回调函数step，将step中的timestamp赋予起始的startTime。当timestamp与startTime的差值小于规定的时间时，会再次调用requestAnimationFrame，最终动画将会停止。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <tabs onchange="changecontent">
4. <tab-content>
5. <div class="container">
6. <stack style="width: 300px;height: 300px;margin-top: 100px;margin-bottom: 100px;">
7. <canvas id="mycanvas" style="width: 100%;height: 100%;background-color: coral;">
8. </canvas>
9. <div style="width: 50px;height: 50px;border-radius: 25px;background-color: indigo;position: absolute;left: {{left}};top: {{top}};">
10. </div>
11. </stack>
12. <button type="capsule" value="play" onclick="runframe"></button>
13. </div>
14. </tab-content>
15. </tabs>
16. </div>
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
9. button{
10. width: 300px;
11. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. timer: null,
5. left: 0,
6. top: 0,
7. flag: true,
8. animation: null,
9. startTime: 0,
10. },
11. onShow() {
12. var test = this.$element("mycanvas");
13. var ctx = test.getContext("2d");
14. ctx.beginPath();
15. ctx.moveTo(0, 0);
16. ctx.lineTo(300, 300);
17. ctx.lineWidth = 5;
18. ctx.strokeStyle = "red";
19. ctx.stroke();
20. },
21. runframe() {
22. this.left = 0;
23. this.top = 0;
24. this.flag = true;
25. this.animation = requestAnimationFrame(this.step);
26. },
27. step(timestamp) {
28. if (this.flag) {
29. this.left += 5;
30. this.top += 5;
31. if (this.startTime == 0) {
32. this.startTime = timestamp;
33. }
34. var elapsed = timestamp - this.startTime;
35. if (elapsed < 500) {
36. console.info('callback step timestamp: ' + timestamp);
37. this.animation = requestAnimationFrame(this.step);
38. }
39. } else {
40. this.left -= 5;
41. this.top -= 5;
42. this.animation = requestAnimationFrame(this.step);
43. }
44. if (this.left == 250 || this.left == 0) {
45. this.flag = !this.flag;
46. }
47. },
48. onDestroy() {
49. cancelAnimationFrame(this.animation);
50. }
51. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/X_2QuB5RQ5OHi5CSTrkaIQ/zh-cn_image_0000002552958150.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234034Z&HW-CC-Expire=86400&HW-CC-Sign=640DE3DDE3C13F6357F73E7D791B25761377F0443CA289EF04015061B99B1C69)

说明

requestAnimationFrame函数在调用回调函数时在第一个参数位置传入timestamp时间戳，表示requestAnimationFrame开始去执行回调函数的时刻。

## 取消动画帧

通过cancelAnimationFrame函数取消逐帧回调，在调用cancelAnimationFrame函数时取消requestAnimationFrame函数的请求。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <tabs onchange="changecontent">
4. <tab-content>
5. <div class="container">
6. <stack style="width: 300px;height: 300px;margin-top: 100px;margin-bottom: 100px;">
7. <canvas id="mycanvas" style="width: 100%;height: 100%;background-color: coral;">
8. </canvas>
9. <div style="width: 50px;height: 50px;border-radius: 25px;background-color: indigo;position: absolute;left: {{left}};top: {{top}};">
10. </div>
11. </stack>
12. <button type="capsule" value="play" onclick="runframe"></button>
13. </div>
14. </tab-content>
15. </tabs>
16. </div>
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
9. button{
10. width: 300px;
11. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. timer: null,
5. left: 0,
6. top: 0,
7. flag: true,
8. animation: null
9. },
10. onShow() {
11. var test = this.$element("mycanvas");
12. var ctx = test.getContext("2d");
13. ctx.beginPath();
14. ctx.moveTo(0, 0);
15. ctx.lineTo(300, 300);
16. ctx.lineWidth = 5;
17. ctx.strokeStyle = "red";
18. ctx.stroke();
19. },
20. runframe() {
21. this.left = 0;
22. this.top = 0;
23. this.flag = true;
24. this.animation = requestAnimationFrame(this.step);
25. },
26. step(timestamp) {
27. if (this.flag) {
28. this.left += 5;
29. this.top += 5;
30. this.animation = requestAnimationFrame(this.step);
31. } else {
32. this.left -= 5;
33. this.top -= 5;
34. this.animation = requestAnimationFrame(this.step);
35. }
36. if (this.left == 250 || this.left == 0) {
37. this.flag = !this.flag;
38. }
39. },
40. onDestroy() {
41. cancelAnimationFrame(this.animation);
42. }
43. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/mwWPfhRxR2Og2gcmcZeIPw/zh-cn_image_0000002583478151.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234034Z&HW-CC-Expire=86400&HW-CC-Sign=7BB74E3BC13AAA70D6A38220737E288EE95B325E3DE803186521F05355DC4808)

说明

在调用该函数时需传入一个具有标识id的参数。
