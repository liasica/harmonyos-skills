---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-picture-in-picture
title: Web组件支持画中画
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 使用网页多媒体 > Web组件支持画中画
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:27+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:2cdf8a69c765f647b5f45ba4b3244035773ded3f1ea46204ff4e3dfc99c722c4
---

Web组件提供画中画功能支持，应用可利用W3C标准的Picture-in-Picture API在网页中创建浮动窗口以播放视频，使用户在浏览其他网页或与其他应用交互时，可通过该画中画窗口继续观看视频。

若使用线上视频资源，则需在配置文件中设置网络权限。权限的添加方法请参考[在配置文件中声明权限](declare-permissions.md#在配置文件中声明权限)。

```
1. "requestPermissions": [
2. {
3. "name": "ohos.permission.INTERNET"
4. }
5. ]
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ArkWebPictureInPicture/entry/src/main/module.json5#L64-L70)

## 约束与限制

1. 当前H264/H265/HLS格式的视频可在创建的画中画窗口中播放。
2. 画中画窗口的大小调整依据系统能力，具体参照设计指南中的系统特性与能力部分。

## 进入画中画

以仅包含媒体源的video元素和一个用户交互的button元素为例，介绍如何创建一个浮动窗口播放视频，使用户在浏览其他网页或与其他应用交互时，能够通过该画中画窗口持续观看视频。

```
1. <!-- 使用时需要自行替换视频链接 -->
2. <video id="video" src="https://example.com/file.mp4" controls></video>
3. <button id="togglePipButton">开启画中画</button>
```

HTMLVideoElement接口提供的requestPictureInPicture()方法请求进入画中画，如果系统支持画中画能力，则会以画中画模式显示视频。

```
1. togglePipButton.addEventListener("click", async () => {
2. try {
3. // 请求进入画中画模式
4. await video.requestPictureInPicture();
5. } catch (err) {
6. // 如果画中画模式切换失败，打印错误信息
7. console.error("Picture-in-Picture mode failed:", err);
8. }
9. });
```

## 退出画中画

请求退出画中画模式，请使用Document接口的exitPictureInPicture()方法，视频将重新在原始标签页中显示。

```
1. // ...
2. try {
3. if (videoElement !== document.pictureInPictureElement) {
4. await videoElement.requestPictureInPicture();
5. } else {
6. await document.exitPictureInPicture();
7. }
8. }
9. // ...
```

## 监听画中画事件

当用户进入画中画模式播放视频时，会显示一个浮动窗口用于播放视频。系统规定每次只能播放一个画中画视频。

HTMLVideoElement的enterpictureinpicture事件在HTMLVideoElement成功进入画中画模式时触发，而HTMLVideoElement的leavepictureinpicture事件在HTMLVideoElement成功退出画中画模式时触发。

在监听到这些事件变化时，开发者可以进行相应的处理。

```
1. videoElement.addEventListener('enterpictureinpicture', function (event) {
2. // 视频进入画中画模式。
3. });

5. videoElement.addEventListener('leavepictureinpicture', function (event) {
6. // 视频退出画中画模式。
7. });
```

## 画中画窗口交互

* 画中画整体窗口控制：

  支持双击画中画窗口控制放大或缩小窗口尺寸。

  支持拖拽画中画窗口到屏幕任意位置。

  支持单击画中画窗口控制画中画控制层UI控件的显示与隐藏。
* 画中画控制层UI控件：

  画中画窗口控制层包含“关闭”（关闭画中画窗口）、“恢复”（从画中画窗口恢复到原应用界面）。

  播放控制包含暂停，播放，前进/后退（默认显示前进/后退UI控件，若原视频不支持前进后退，单击无响应）。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/hEEjaWRrTBK-yOURcAebxw/zh-cn_image_0000002589324593.png?HW-CC-KV=V1&HW-CC-Date=20260429T052926Z&HW-CC-Expire=86400&HW-CC-Sign=7FF7A4E46D564F72F103526C0A62938C8DD396985239E4BFA4D0C593F7821B3A)

## 完整示例

支持启动/退出画中画的完整示例如下：

* 应用侧ets代码。

  ```
  1. import { webview } from '@kit.ArkWeb';

  3. @Entry
  4. @Component
  5. struct Index {
  6. @State videoSrc: Resource = $rawfile('PictureInPicture.html');
  7. controller: webview.WebviewController = new webview.WebviewController();

  9. build() {
  10. Column() {
  11. Web({src: this.videoSrc, controller: this.controller})
  12. }
  13. }
  14. }
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ArkWebPictureInPicture/entry/src/main/ets/pages/Index.ets#L16-L31)
* 前端页面HTML代码。

  ```
  1. <!-- PictureInPicture.html -->
  2. <!DOCTYPE html>
  3. <html lang="en">
  4. <head>
  5. <meta charset="UTF-8" />
  6. <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  7. <title>Picture-in-Picture Demo</title>
  8. <style>
  9. body {
  10. font-family: Arial, sans-serif;
  11. display: flex;
  12. flex-direction: column;
  13. align-items: center;
  14. justify-content: center;
  15. height: 100vh;
  16. margin: 0;
  17. }
  18. video {
  19. width: 60%;
  20. border: 1px solid #ccc;
  21. border-radius: 8px;
  22. margin-bottom: 20px;
  23. }
  24. button {
  25. padding: 10px 20px;
  26. font-size: 16px;
  27. cursor: pointer;
  28. }
  29. </style>
  30. </head>
  31. <body>
  32. <!-- 使用时需要自行替换视频链接 -->
  33. <video id="video" src="https://example.com/file.mp4" controls></video>
  34. <button id="togglePipButton">开启画中画</button>

  36. <script>
  37. const video = document.getElementById("video");
  38. const togglePipButton = document.getElementById("togglePipButton");

  40. // 如果浏览器不支持画中画功能或被禁用，则隐藏按钮
  41. togglePipButton.hidden =
  42. !document.pictureInPictureEnabled || video.disablePictureInPicture;

  44. // 监听按钮单击事件，切换画中画模式
  45. togglePipButton.addEventListener("click", async () => {
  46. try {
  47. if (document.pictureInPictureElement) {
  48. // 如果当前处于画中画模式，退出画中画
  49. await document.exitPictureInPicture();
  50. } else {
  51. // 否则，进入画中画模式
  52. await video.requestPictureInPicture();
  53. }
  54. } catch (err) {
  55. // 如果画中画模式切换失败，打印错误信息
  56. console.error("Picture-in-Picture mode failed:", err);
  57. }
  58. });

  60. // 监听进入画中画事件
  61. video.addEventListener("enterpictureinpicture", () => {
  62. // 更新按钮文本为“退出画中画”
  63. togglePipButton.textContent = "退出画中画";
  64. });

  66. // 监听退出画中画事件
  67. video.addEventListener("leavepictureinpicture", () => {
  68. // 更新按钮文本为“开启画中画”
  69. togglePipButton.textContent = "开启画中画";
  70. });
  71. </script>
  72. </body>
  73. </html>
  ```
