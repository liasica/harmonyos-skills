---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avsession-desktop-lyrics
title: 应用接入桌面歌词
breadcrumb: 指南 > 媒体 > AVSession Kit（音视频播控服务） > 本地媒体会话 > 应用接入桌面歌词
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2cc0a6e8c5d179cc9e01e0c0d9983625915336a0535e911e7e89806a40d7c145
---

从API version 23开始，支持应用接入桌面歌词功能，将歌词以悬浮窗形式展示在系统桌面，让用户无需进入应用即可查看歌词，适用于音乐播放器或有歌词展示需求的音频类应用。

桌面歌词采用悬浮窗形式显示，支持歌词内容的同步展示、窗口显示/隐藏控制及锁定操作。该功能可帮助应用快速实现桌面歌词显示能力，提升用户听歌体验。

实现桌面歌词功能，需遵循以下流程：

1. 创建会话。
2. 判断当前系统版本是否支持桌面歌词功能，若支持则设置歌词元数据。
3. 通过接口控制歌词的使能与显示状态。
4. 监听系统侧的状态变化以同步UI。
5. 在退出时正确销毁会话。

## 具体步骤

1. 首先创建[AVSession实例](avsession-access-scene.md#创建不同类型的会话)，通过[设置元数据](avsession-access-scene.md#设置元数据)填入符合LRC格式的歌词内容。系统播控中心将解析该内容，实现歌词内容的同步展示。歌词内容必须包含时间标签及对应歌词文本。

   说明

   * 设置元数据时，必须包含lyric字段，否则桌面歌词功能无法生效。
2. 应用根据自身业务需求，调用接口控制桌面歌词的使能与显示状态，同时提供用户入口供用户手动操作。可调用以下接口：

   * **判断是否支持桌面歌词：** 调用[isDesktopLyricSupported](../harmonyos-references/arkts-apis-avsession-f.md#avsessionisdesktoplyricsupported23)接口，判断应用是否支持桌面歌词功能。
   * **使能桌面歌词：** 调用[enableDesktopLyric](../harmonyos-references/arkts-apis-avsession-avsession.md#enabledesktoplyric23)接口，启用桌面歌词。
   * **设置可见性：** 调用[setDesktopLyricVisible](../harmonyos-references/arkts-apis-avsession-avsession.md#setdesktoplyricvisible23)接口，切换歌词窗口的可见性状态。
   * **设置锁定状态：** 调用[setDesktopLyricState](../harmonyos-references/arkts-apis-avsession-avsession.md#setdesktoplyricstate23)接口，设置歌词窗口的锁定状态，从而限制歌词窗口的拖动或关闭操作。
3. 应用监听系统侧发出的桌面歌词状态变更通知，响应桌面歌词组件的控制并同步刷新应用内UI。

   应用需监听系统侧发出的桌面歌词状态变更通知（如用户在系统设置中关闭了歌词），以便同步刷新应用内的开关状态。

   说明

   * 必须响应[onDesktopLyricEnabled](../harmonyos-references/arkts-apis-avsession-avsessioncontroller.md#ondesktoplyricenabled23)和[offDesktopLyricEnabled](../harmonyos-references/arkts-apis-avsession-avsessioncontroller.md#offdesktoplyricenabled23)回调，根据回调值更新UI，确保应用内UI与系统实际状态一致。
4. 当应用退出时，必须销毁当前会话。

   当应用退出或不再需要播放媒体时，必须主动销毁AVSession。销毁操作将导致关联的桌面歌词组件自动跟随退出。再次启动时，需重新初始化AVSession以恢复会话。

   说明

   * 确保AVSession对象在后台播放期间不被系统回收，否则会导致歌词中断。

   ```
   1. import { avSession as AVSessionManager } from '@kit.AVSessionKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. // ...

   5. @Entry
   6. @Component
   7. struct Index {
   8. @State message: string = 'hello world';
   9. // ...

   11. build() {
   12. Column() {
   13. // ...
   14. Text(this.message)
   15. .onClick(async () => {
   16. let context = this.getUIContext().getHostContext() as Context;
   17. // 假设已经创建了一个session，如何创建session可以参考之前的案例。
   18. let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', 'audio');

   20. // 系统是否支持桌面歌词。
   21. let isDesktopLyricSupported: boolean = false;
   22. try {
   23. isDesktopLyricSupported = await AVSessionManager.isDesktopLyricSupported();
   24. } catch (err) {
   25. console.error(`Failed to get isDesktopLyricSupported. Code: ${err.code}, message: ${err.message}`);
   26. }
   27. if (!isDesktopLyricSupported) {
   28. return;
   29. }

   31. try {
   32. // 监听桌面歌词是否开启。
   33. session.onDesktopLyricVisibilityChanged((isVisible: boolean) => {
   34. console.info(`onDesktopLyricVisibilityChanged changed: ${isVisible}`)
   35. });
   36. } catch (err) {
   37. console.error(`onDesktopLyricVisibilityChanged err. Code: ${err.code}, message: ${err.message}`);
   38. }

   40. try {
   41. // 监听桌面歌词锁定状态。
   42. session.onDesktopLyricStateChanged((state) => {
   43. console.info(`onDesktopLyricStateChanged changed: ${state.isLocked}`)
   44. });
   45. } catch (err) {
   46. console.error(`onDesktopLyricStateChanged err. Code: ${err.code}, message: ${err.message}`);
   47. }

   49. try {
   50. // 使能桌面歌词。
   51. session.enableDesktopLyric(true);
   52. } catch (err) {
   53. console.error(`enableDesktopLyric err. Code: ${err.code}, message: ${err.message}`);
   54. }

   56. try {
   57. // 开启或关闭桌面歌词。
   58. await session.setDesktopLyricVisible(true);
   59. } catch (err) {
   60. console.error(`setDesktopLyricVisible err. Code: ${err.code}, message: ${err.message}`);
   61. }

   63. try {
   64. // 桌面歌词锁定状态。
   65. await session.setDesktopLyricState({isLocked: true});
   66. } catch (err) {
   67. console.error(`setDesktopLyricState err. Code: ${err.code}, message: ${err.message}`);
   68. }

   70. })
   71. }
   72. .width('100%')
   73. .height('100%')
   74. }
   75. }
   ```
