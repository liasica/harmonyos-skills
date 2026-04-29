---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-media-video
title: video
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 媒体组件 > video
category: harmonyos-references
scraped_at: 2026-04-29T13:53:29+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:49d8ccaa565c273de91a976443e5ca5aacbc7f5c37ad5c1de45859bb2178ca8f
---

说明

* 从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

视频播放组件。

## 子组件

PhonePC/2in1TabletTVWearable

不支持。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-components-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| muted | boolean | false | 否 | 视频是否静音播放。  true：开启静音；  false：关闭静音。 |
| src | string | - | 否 | 播放视频内容的路径。 |
| autoplay | boolean | false | 否 | 视频是否自动播放。  true：开启自动播放；  false：关闭自动播放。 |
| controls | boolean | true | 否 | 控制视频播放的控制栏是否显示，如果设置为false，则不显示控制栏。默认为true，由系统决定显示或隐藏控制栏。 |

## 样式

PhonePC/2in1TabletTVWearable

除支持[通用样式](js-components-common-styles.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| object-fit | string | contain | 否 | 视频源的缩放类型，如果poster设置了值，那么此配置还会影响视频海报的缩放类型，可选值参考表 object-fit 类型说明。 |

**表1** object-fit 类型说明

| 类型 | 描述 |
| --- | --- |
| fill | 不保持宽高比进行放大缩小，使得图片填充满显示边界。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](js-components-common-events.md)外，还支持如下事件：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| prepared | { duration: value }5+ | 视频准备完成时触发该事件，通过duration可以获取视频时长，单位为s。 |
| start | - | 播放时触发该事件。 |
| pause | - | 暂停时触发该事件。 |
| finish | - | 播放结束时触发该事件。 |
| error | - | 播放失败时触发该事件。 |
| seeking | { currenttime: value } | 操作进度条过程时上报时间信息，单位为s。 |
| seeked | { currenttime: value } | 操作进度条完成后，上报播放时间信息，单位为s。 |
| timeupdate | { currenttime: value } | 播放进度变化时触发该事件，单位为s，更新时间间隔为250ms。 |

## 方法

PhonePC/2in1TabletTVWearable

除支持[通用方法](js-components-common-methods.md)外，还支持如下方法：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| start | - | 请求播放视频。 |
| pause | - | 请求暂停播放视频。 |
| setCurrentTime | { currenttime: value } | 指定视频播放的进度位置，单位为s。 |

说明

在attached组件生命周期回调后，可以调用上述组件方法。

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <!-- '/common/myDream.mp4'需要替换为开发者所需的视频资源文件 -->
4. <video id='videoId' src='/common/myDream.mp4' muted='false' autoplay='false'
5. controls='true' onprepared='preparedCallback' onstart='startCallback'
6. onpause='pauseCallback' onfinish='finishCallback' onerror='errorCallback'
7. onseeking='seekingCallback' onseeked='seekedCallback'
8. ontimeupdate='timeupdateCallback'
9. style="object-fit: fill; width: 100%; height: 900px;"
10. onclick="change_start_pause">
11. </video>
12. </div>
```

```
1. /* xxx.css */
2. .container {
3. justify-content: center;
4. align-items: center;
5. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. event: '',
5. seekingTime: '',
6. timeupdateTime: '',
7. seekedTime: '',
8. isStart: true,
9. duration: '',
10. },
11. preparedCallback: function (e) {
12. this.event = '视频连接成功';
13. this.duration = e.duration;
14. },
15. startCallback: function () {
16. this.event = '视频开始播放';
17. },
18. pauseCallback: function () {
19. this.event = '视频暂停播放';
20. },
21. finishCallback: function () {
22. this.event = '视频播放结束';
23. },
24. errorCallback: function () {
25. this.event = '视频播放错误';
26. },
27. seekingCallback: function (e) {
28. this.seekingTime = e.currenttime;
29. },
30. timeupdateCallback: function (e) {
31. this.timeupdateTime = e.currenttime;
32. },
33. change_start_pause: function () {
34. if (this.isStart) {
35. this.$element('videoId').pause();
36. this.isStart = false;
37. } else {
38. this.$element('videoId').start();
39. this.isStart = true;
40. }
41. },
42. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/1wjTK-fcT7i2bXqjngTFtA/zh-cn_image_0000002558766730.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055328Z&HW-CC-Expire=86400&HW-CC-Sign=2166EB44E48BB7A6A16499277CAE5E8F78674679758F92F51CF64AA1125B7382)
