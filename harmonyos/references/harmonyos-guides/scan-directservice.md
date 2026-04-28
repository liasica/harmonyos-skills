---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-directservice
title: 接入“扫码直达”服务
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > 接入“扫码直达”服务
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f07670b6fc1a3d67503de5df8279ce96996c872733625b7a1b50e3ffa5045bca
---

说明

扫码直达能力仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）接入使用。

在日常生活中，人们会使用各种应用扫各式各样的码，而“扫码直达”服务则为用户带来一种全新的扫码体验。

开发者将域名注册到“扫码直达”服务后，用户可通过控制中心等系统级的常驻入口，扫应用的二维码、条形码并跳转到应用对应服务页，实现一步直达服务的体验。

开发者接入“扫码直达”服务，能为应用带来：

* 更浅层的扫码入口和更便捷的“扫码直达”服务体验。
* HarmonyOS强大的扫码能力。
* 更容易触达用户的全新渠道。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/CCnYTl9eQhC_yQW8gK44nQ/zh-cn_image_0000002583478611.png?HW-CC-KV=V1&HW-CC-Date=20260427T234640Z&HW-CC-Expire=86400&HW-CC-Sign=4D28945C5787EC5D895E442D8FB9CE00E3678E4D68BBFC67963582B8E041BA05)

1. 开发者参考App Linking指导完成域名注册。
2. 用户通过HarmonyOS扫码入口发起扫码请求。
3. HarmonyOS扫码入口调用系统能力解析码值，查询码值对应的应用信息后拉起应用。
4. 解析码值结果跳转应用服务页。

## 开发步骤

1. 参考[开发准备](scan-config-agc.md)完成必要的准备工作。
2. 处理接收到的码值，完成应用内页面跳转逻辑。

   ```
   1. import { router, window } from '@kit.ArkUI';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { UIAbility, Want } from '@kit.AbilityKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';

   7. export default class EntryAbility extends UIAbility {
   8. private page: string = 'pages/Index';
   9. private uiContext?: UIContext;

   11. // 冷启动场景通过onCreate回调获取码值信息
   12. onCreate(want: Want): void {
   13. hilog.info(0x0001, '[Scan Access]', 'Succeeded in getting want in onCreate');
   14. // 从want中获取传入的链接信息。
   15. // 如传入的url为：https://www.example.com/programs?router=Access
   16. this.getRouterUri(want);
   17. }

   20. // 热启动场景通过onNewWant回调获取码值信息
   21. onNewWant(want: Want): void {
   22. hilog.info(0x0001, '[Scan Access]', 'Succeeded in getting want in onNewWant');
   23. // 从want中获取传入的链接信息
   24. this.getRouterUri(want);
   25. }

   28. onWindowStageCreate(windowStage: window.WindowStage): void {
   29. hilog.info(0x0001, '[Scan Access]', 'Ability onWindowStageCreate');
   30. try {
   31. windowStage.getMainWindow().then((windowObj: window.Window) => {
   32. try {
   33. windowStage.loadContent(this.page).then(() => {
   34. hilog.info(0x0001, '[Scan Access]', 'Succeeded in loading the content.');
   35. try {
   36. this.uiContext = windowObj.getUIContext();
   37. hilog.info(0x0001, '[Scan Access]', 'Succeeded in getting UIContext.');
   38. } catch (err) {
   39. hilog.error(0x0001, '[Scan Access]', `Failed to get UIContext by windowObj. Code: ${err.code}.`);
   40. }
   41. }).catch((err: BusinessError) => {
   42. hilog.error(0x0001, '[Scan Access]', `Failed to load the content. Code: ${err.code}.`);
   43. })
   44. } catch (err) {
   45. hilog.error(0x0001, '[Scan Access]', `Failed to load the content. Code: ${err.code}.`);
   46. }
   47. }).catch((err: BusinessError) => {
   48. hilog.error(0x0001, '[Scan Access]', `Failed to get MainWindow. Code: ${err.code}.`);
   49. })
   50. } catch (err) {
   51. hilog.error(0x0001, '[Scan Access]', `Failed to get MainWindow. Code: ${err.code}.`);
   52. }
   53. }

   56. // 解析扫码结果，跳转相应页面
   57. private getRouterUri(want: Want) {
   58. const uri: string | undefined = want?.uri;
   59. if (uri && this.uiContext) {
   60. // 开发者根据解析的uri跳转至相应页面，例如需要跳转页面为"pages/Access"
   61. const status: router.RouterState = this.uiContext.getRouter().getState();
   62. if (status && status.name !== 'Access' && uri) {
   63. try {
   64. // 根据uri参数做业务处理
   65. this.uiContext.getRouter().pushUrl({
   66. url: 'pages/Access'
   67. }).catch((err: BusinessError) => {
   68. hilog.error(0x0001, '[Scan Access]', `Failed to pushUrl by getRouter. Code: ${err.code}.`);
   69. });
   70. } catch (err) {
   71. hilog.error(0x0001, '[Scan Access]', `Failed to pushUrl by getRouter. Code: ${err.code}.`);
   72. }
   73. }
   74. }
   75. }
   76. }
   ```
3. 验证“扫码直达”服务。

   1. 将配置好域名映射关系的测试应用安装到本地。
   2. 打开HarmonyOS扫码入口（控制中心扫码入口），扫描应用发行的二维码。
   3. 确认能否拉起应用并跳转目标服务页。

集成效果，以美团单车场景为例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/jtt1o-poTDSx0DFTmc6AmA/zh-cn_image_0000002552798962.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234640Z&HW-CC-Expire=86400&HW-CC-Sign=57B2F288C9380F67D70857997E99C37ABBDD41E0B1CD94189B28695A536CB761)

## 开发后验证

集成扫码直达能力应用用户体验质量建议

应用完成开发后，可参照以下标准检查集成扫码直达后的用户体验是否符合预期：

| 标准编号 | 标准项名称 | 类型 | 标准详细描述 |
| --- | --- | --- | --- |
| 1 | 应用已安装跳转体验 | 规则 | 通过系统扫一扫扫描码图可以跳转到履约页面。履约页面指的是扫码后的目标服务页面，例如，扫支付码跳转到应用的支付页面，而非首页。 |
| 2 | 应用未安装跳转体验 | 建议 | 通过系统扫一扫扫描码图会拉起浏览器加载码值所对应的网页，请设计网页满足用户诉求、指导用户安装应用等。 |
