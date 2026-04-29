---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-image-animator
title: image-animator开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > image-animator开发指导
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:49+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9094a33a514daeef415373fd4c5e9535100174531faa903aaca91abaed8c3b2b
---

image-animator组件为图片帧动画播放器。具体用法请参考[image-animator](../harmonyos-references/js-components-basic-image-animator.md)。

## 创建image-animator组件

在pages/index目录下的hml文件中创建一个image-animator组件，css文件中编写组件样式，js文件中引用图片。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <image-animator class="animator" images="{{frames}}" duration="3s"/>
4. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. }
10. .animator {
11. width: 500px;
12. height: 500px;
13. }
```

```
1. // index.js
2. export default {
3. data: {
4. frames: [
5. {
6. src: "/common/landscape1.jpg",
7. },
8. {
9. src: "/common/landscape2.jpg",
10. }
11. ],
12. },
13. };
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/NaKtC2o7QqKiOoZtNj3vTw/zh-cn_image_0000002589324469.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052848Z&HW-CC-Expire=86400&HW-CC-Sign=596B7F986D5013DA59C938DB02B3240A8EF2000A16C9472015BFADAA50AB21B8)

## 设置image-animator组件属性

添加iteration（播放次数）、reverse（播放顺序）、fixedsize（图片大小是否固定为组件大小）、duration（播放时长）和fillmode（执行结束后的状态）属性，控制图片的播放效果。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <image-animator class="animator" fixedsize="false" iteration='2' reverse="false" ref="animator" fillmode="none" images="{{frames}}"   duration="5s" />
4. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. background-color: #F1F3F5;
7. }
8. .animator {
9. width: 500px;
10. height: 500px;
11. }
```

```
1. // index.js
2. export default {
3. data: {
4. frames: [
5. {
6. src: 'common/landscape1.jpg',
7. width: '250px',
8. height: '250px',
9. left: '150px',
10. top: '50px',
11. },
12. {
13. src: 'common/landscape2.jpg',
14. width: '300px',
15. height: '300px',
16. left: '150px',
17. top: '100px',
18. },
19. {
20. src: 'common/landscape1.jpg',
21. width: '350px',
22. height: '350px',
23. left: '150px',
24. top: '150px',
25. },
26. {
27. src: 'common/landscape2.jpg',
28. width: '400px',
29. height: '400px',
30. left: '150px',
31. top: '200px',
32. },
33. {
34. src: 'common/landscape3.jpg',
35. width: '450px',
36. height: '450px',
37. left: '150px',
38. top: '250px',
39. },
40. {
41. src: 'common/landscape4.jpg',
42. width: '500px',
43. height: '500px',
44. left: '150px',
45. top: '300px',
46. },
47. ],
48. },
49. };
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/pz0ihiqrRTuUs1zcdq1JCA/zh-cn_image_0000002589244409.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052848Z&HW-CC-Expire=86400&HW-CC-Sign=CE3AC13073437D53701FC5DF1867F6D9EF91A4EF89E4E1B2274E979FB8647C96)

说明

* 如果在images属性中设置了单独的duration属性，在image-animator组件中设置的duration属性无效。
* 如果fixedsize属性值设置为true，图片的width 、height 、top 和left属性无效。
* 如果reverse属性值设置为false，表示从第1张图片播放到最后1张图片。 如果reverse属性值设置为true，表示从最后1张图片播放到第1张图片。

## 绑定事件

向image-animator组件添加start、pause、stop和resume事件。当图片播放器开始播放时触发start事件，当图片播放器被点击时触发pause事件，长按图片播放器触发resume事件，图片播放器停止播放时触发stop事件。

```
1. <!-- xxx.hml -->
2. <div class="doc-page">
3. <image-animator class="img" id="img" images="{{imginfo}}" iteration="1" duration="10s" onstart="popstart" onpause="poppause"   onstop="popstop" onresume="popresume" onlongpress="setresume" onclick="setpause">
4. </image-animator>
5. </div>
```

```
1. /* xxx.css */
2. .doc-page {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. align-items: center;
7. justify-content: center;
8. background-color: #F1F3F5;
9. }
10. .img {
11. width: 600px;
12. height: 600px;
13. border: 3px solid orange;
14. }
```

```
1. // index.js
2. import promptAction from '@ohos.promptAction';
3. export default {
4. data: {
5. imginfo: [
6. {
7. src: 'common/landscape1.jpg',
8. },{
9. src: 'common/landscape2.jpg',
10. },{
11. src: 'common/landscape3.jpg',
12. },{
13. src: 'common/landscape4.jpg',
14. }
15. ],
16. },
17. onInit() {
18. },
19. setpause(e) {
20. this.$element('img').pause()
21. },
22. setresume(e) {
23. this.$element('img').resume()
24. },
25. popstart(e) {
26. promptAction.showToast({
27. message: '开始'
28. })
29. },
30. poppause(e) {
31. promptAction.showToast({
32. message: '暂停'
33. })
34. },
35. popstop(e) {
36. promptAction.showToast({
37. message: '停止'
38. })
39. },
40. popresume(e) {
41. promptAction.showToast({
42. message: '恢复'
43. })
44. }
45. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/nLNzWZdkSC6zakhKVOymZQ/zh-cn_image_0000002558764602.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052848Z&HW-CC-Expire=86400&HW-CC-Sign=F03994A87743869664E82E56BDD0FAD05A4F0F7EC043E510789988203918D02A)

## 场景示例

在本场景中，开发者可通过开始播放、停止播放等按钮切换图片的播放状态。

image-animator组件通过调用start、pause、stop和resume方法控制图片的开始、暂停、停止和重新播放，通过getState方法查询图片的播放状态。

```
1. <!-- xxx.hml -->
2. <div class="doc-page">
3. <image-animator class="img" id="img" images="{{imginfo}}" iteration="2" reverse="{{rev}}" duration="10s">
4. </image-animator>
5. <div style="width: 700px;height:450px;margin-top: 40px;flex-direction:column;justify-content:space-around;">
6. <div class="container">
7. <button type="capsule" value="开始播放" onclick="startimg"></button>
8. <button type="capsule" value="暂停播放" onclick="pauseimg"></button>
9. </div>
10. <div class="container">
11. <button type="capsule" value="停止播放" onclick="stopimg"></button>
12. <button type="capsule" value="重新播放" onclick="resumeimg"></button>
13. </div>
14. <div class="container">
15. <button type="capsule" value="获取播放状态" onclick="getimgstate"></button>
16. <button type="capsule" value="{{revVal}}" onclick="revimg"></button>
17. </div>
18. </div>
19. </div>
```

```
1. /* xxx.css */
2. .doc-page {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. align-items: center;
7. justify-content: center;
8. background-color: #F1F3F5;
9. }
10. .img {
11. width: 600px;
12. height: 600px;
13. border: 3px solid orange;
14. }
15. button{
16. width: 260px
17. }
18. .container {
19. width: 100%;
20. height: 120px;
21. align-items: center;
22. justify-content: space-around;
23. }
```

```
1. // index.js
2. import promptAction from '@ohos.promptAction';
3. export default {
4. data: {
5. rev:false,
6. imginfo: [
7. {
8. src: 'common/landscape1.jpg',
9. },{
10. src: 'common/landscape2.jpg',
11. },{
12. src: 'common/landscape3.jpg',
13. },{
14. src: 'common/landscape4.jpg',
15. }
16. ],
17. revVal: '反向播放'
18. },
19. onInit() {
20. },
21. startimg(e) {
22. this.$element('img').start()
23. },
24. pauseimg(e) {
25. this.$element('img').pause()
26. },
27. stopimg(e) {
28. this.$element('img').stop()
29. },
30. resumeimg(e) {
31. this.$element('img').resume()
32. },
33. getimgstate(e) {
34. promptAction.showToast({
35. message: '当前状态：' + this.$element('img').getState()
36. })
37. },
38. revimg(e) {
39. this.rev = !this.rev
40. if (this.rev) {
41. this.revVal = '正向播放'
42. } else {
43. this.revVal = '反向播放'
44. }
45. }
46. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/qs8r7MB8RNia5a6gpwzwoA/zh-cn_image_0000002558604946.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052848Z&HW-CC-Expire=86400&HW-CC-Sign=D287952EFEA50F7EB3B435B598B7839C1252325FC5F13C414EB473DC882476FA)
