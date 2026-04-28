---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-event-router
title: 卡片跳转到应用页面（router事件）
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS卡片页面交互 > 卡片跳转到应用页面（router事件）
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:29+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7fc8d51466611dc2825da6f2773117234ca9cf521a8984be5c08c61d80ad30ff
---

在动态卡片中使用[postCardAction](../harmonyos-references/js-apis-postcardaction.md#postcardaction-1)接口的router能力，能够快速拉起动态卡片提供方应用的指定UIAbility(页面)，因此UIAbility较多的应用往往会通过卡片提供不同的跳转按钮，实现一键直达的效果。例如相机卡片，卡片上提供拍照、录像等按钮，点击不同按钮将拉起相机应用的不同UIAbility，从而提升用户的体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/n1oJ-sYXQyCFDnFcTaO5xQ/zh-cn_image_0000002552958296.png?HW-CC-KV=V1&HW-CC-Date=20260427T234128Z&HW-CC-Expire=86400&HW-CC-Sign=0AA9E151181ED479F76685C427DA819FE117D7BA9B38FC8160108D7B47DFF871)

说明

本文主要介绍动态卡片的事件开发。对于静态卡片，请参见[FormLink](../harmonyos-references/ts-container-formlink.md)。

## 开发步骤

1. 创建动态卡片，在工程的entry模块中，新建名为WidgetEventRouterCard的ArkTS卡片。
2. 构建ArkTS卡片页面代码布局，卡片页面布局中有两个按钮，点击其中一个按钮时调用postCardAction向指定UIAbility发送router事件，并在事件内定义需要传递的内容。

   ```
   1. // src/main/ets/widgeteventrouter/pages/WidgetEventRouterCard.ets
   2. @Entry
   3. @Component
   4. struct WidgetEventRouterCard {
   5. build() {
   6. Column() {
   7. // $r('app.string.JumpLabel')需要替换为开发者所需的资源文件
   8. Text($r('app.string.JumpLabel'))
   9. .fontColor('#FFFFFF')
   10. .opacity(0.9)
   11. .fontSize(14)
   12. .margin({ top: '8%', left: '10%' })
   13. Row() {
   14. Column() {
   15. Button() {
   16. // $r('app.string.ButtonA_label')需要替换为开发者所需的资源文件
   17. Text($r('app.string.ButtonA_label'))
   18. .fontColor('#45A6F4')
   19. .fontSize(12)
   20. }
   21. .width(120)
   22. .height(32)
   23. .margin({ top: '20%' })
   24. .backgroundColor('#FFFFFF')
   25. .borderRadius(16)
   26. .onClick(() => {
   27. postCardAction(this, {
   28. action: 'router',
   29. abilityName: 'EntryAbility',
   30. params: { targetPage: 'funA' }
   31. });
   32. })

   34. Button() {
   35. // $r('app.string.ButtonB_label')需要替换为开发者所需的资源文件
   36. Text($r('app.string.ButtonB_label'))
   37. .fontColor('#45A6F4')
   38. .fontSize(12)
   39. }
   40. .width(120)
   41. .height(32)
   42. .margin({ top: '8%', bottom: '15vp' })
   43. .backgroundColor('#FFFFFF')
   44. .borderRadius(16)
   45. .onClick(() => {
   46. postCardAction(this, {
   47. action: 'router',
   48. abilityName: 'EntryAbility',
   49. params: { targetPage: 'funB' }
   50. });
   51. })
   52. }
   53. }.width('100%').height('80%')
   54. .justifyContent(FlexAlign.Center)
   55. }
   56. .width('100%')
   57. .height('100%')
   58. .alignItems(HorizontalAlign.Start)
   59. // $r('app.media.CardEvent')需要替换为开发者所需的资源文件
   60. .backgroundImage($r('app.media.CardEvent'))
   61. .backgroundImageSize(ImageSize.Cover)
   62. }
   63. }
   ```
3. 处理router事件，在UIAbility中接收router事件并获取参数，根据传递的params不同，选择拉起不同的页面。

   ```
   1. // src/main/ets/entryability/EntryAbility.ts
   2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   3. import { window } from '@kit.ArkUI';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';

   6. const TAG: string = 'EntryAbility';
   7. const DOMAIN_NUMBER: number = 0xFF00;

   9. export default class EntryAbility extends UIAbility {
   10. private selectPage: string = 'funA';
   11. private currentWindowStage: window.WindowStage | null = null;

   13. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   14. // 获取router事件中传递的targetPage参数
   15. hilog.info(DOMAIN_NUMBER, TAG, `Ability onCreate, ${JSON.stringify(want)}`);
   16. if (want?.parameters?.params) {
   17. // want.parameters.params 对应 postCardAction() 中 params 内容
   18. let params: Record<string, Object> = JSON.parse(want.parameters.params as string);
   19. this.selectPage = params.targetPage as string;
   20. hilog.info(DOMAIN_NUMBER, TAG, `onCreate selectPage: ${this.selectPage}`);
   21. }
   22. }

   24. // 如果UIAbility已在后台运行，在收到Router事件后会触发onNewWant生命周期回调
   25. onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   26. hilog.info(DOMAIN_NUMBER, TAG, `onNewWant Want: ${JSON.stringify(want)}`);
   27. if (want?.parameters?.params) {
   28. // want.parameters.params 对应 postCardAction() 中 params 内容
   29. let params: Record<string, Object> = JSON.parse(want.parameters.params as string);
   30. this.selectPage = params.targetPage as string;
   31. hilog.info(DOMAIN_NUMBER, TAG, `onNewWant selectPage: ${this.selectPage}`);
   32. }
   33. if (this.currentWindowStage !== null) {
   34. this.onWindowStageCreate(this.currentWindowStage);
   35. }
   36. }

   38. onWindowStageCreate(windowStage: window.WindowStage): void {
   39. // Main window is created, set main page for this ability
   40. let targetPage: string;
   41. // 根据传递的targetPage不同，选择拉起不同的页面
   42. switch (this.selectPage) {
   43. case 'funA':
   44. targetPage = 'funpages/FunA';
   45. break;
   46. case 'funB':
   47. targetPage = 'funpages/FunB';
   48. break;
   49. default:
   50. targetPage = 'pages/Index';
   51. }
   52. if (this.currentWindowStage === null) {
   53. this.currentWindowStage = windowStage;
   54. }
   55. windowStage.loadContent(targetPage, (err, data) => {
   56. if (err.code) {
   57. hilog.error(DOMAIN_NUMBER, TAG, 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
   58. return;
   59. }
   60. hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
   61. });
   62. }
   63. }
   ```
4. 创建跳转后的UIAbility页面，新建FunA.ets和FunB.ets，构建页面布局。

   ```
   1. // src/main/ets/funpages/FunA.ets
   2. @Entry
   3. @Component
   4. struct FunA {
   5. build() {
   6. Column() {
   7. Row() {
   8. // $r('app.string.ButtonA_label')需要替换为开发者所需的资源文件
   9. Text(($r('app.string.ButtonA_label')))
   10. .fontSize(24)
   11. .fontWeight(FontWeight.Bold)
   12. .textAlign(TextAlign.Start)
   13. .margin({
   14. top: 12,
   15. bottom: 11,
   16. right: 24,
   17. left: 24
   18. })
   19. }
   20. .width('100%')
   21. .height(56)
   22. .justifyContent(FlexAlign.Start)

   24. // $r('app.media.pic_empty')需要替换为开发者所需的资源文件
   25. Image($r('app.media.pic_empty'))
   26. .width(120)
   27. .height(120)
   28. .margin({ top: 224 })

   30. // $r('app.string.NoContentAvailable')需要替换为开发者所需的资源文件
   31. Text($r('app.string.NoContentAvailable'))
   32. .fontSize(14)
   33. // $r('app.color.text_color')需要替换为开发者所需的资源文件
   34. .fontColor($r('app.color.text_color'))
   35. .opacity(0.4)
   36. .margin({
   37. top: 8,
   38. bottom: 317,
   39. right: 152,
   40. left: 152
   41. })
   42. }
   43. .width('100%')
   44. .height('100%')
   45. }
   46. }
   ```

   ```
   1. // src/main/ets/funpages/FunB.ets
   2. @Entry
   3. @Component
   4. struct FunB {
   5. build() {
   6. Column() {
   7. Row() {
   8. // $r('app.string.ButtonB_label')需要替换为开发者所需的资源文件
   9. Text(($r('app.string.ButtonB_label')))
   10. .fontSize(24)
   11. .fontWeight(FontWeight.Bold)
   12. .textAlign(TextAlign.Start)
   13. .margin({
   14. top: 12,
   15. bottom: 11,
   16. right: 24,
   17. left: 24
   18. })
   19. }
   20. .width('100%')
   21. .height(56)
   22. .justifyContent(FlexAlign.Start)

   24. // $r('app.media.pic_empty')需要替换为开发者所需的资源文件
   25. Image($r('app.media.pic_empty'))
   26. .width(120)
   27. .height(120)
   28. .margin({ top: 224 })

   30. // $r('app.string.NoContentAvailable')需要替换为开发者所需的资源文件
   31. Text($r('app.string.NoContentAvailable'))
   32. .fontSize(14)
   33. // $r('app.color.text_color')需要替换为开发者所需的资源文件
   34. .fontColor($r('app.color.text_color'))
   35. .opacity(0.4)
   36. .margin({
   37. top: 8,
   38. bottom: 317,
   39. right: 152,
   40. left: 152
   41. })
   42. }
   43. .width('100%')
   44. .height('100%')
   45. }
   46. }
   ```
5. 在resources/base/profile下的main\_pages.json文件中配置FunA.ets和FunB.ets页面。

   ```
   1. // src/main/resources/base/profile/main_pages.json
   2. {
   3. "src": [
   4. "pages/Index",
   5. "funpages/FunA",
   6. "funpages/FunB"
   7. ]
   8. }
   ```
6. 资源文件如下，请开发者替换为实际使用的资源。

   ```
   1. // src/main/resources/zh_CN/element/string.json
   2. {
   3. "string": [
   4. // ...
   5. {
   6. "name": "ButtonA_label",
   7. "value": "FunA页面"
   8. },
   9. {
   10. "name": "ButtonB_label",
   11. "value": "FunB页面"
   12. },
   13. {
   14. "name": "JumpLabel",
   15. "value": "router事件跳转"
   16. },
   17. {
   18. "name": "NoContentAvailable",
   19. "value": "暂无内容"
   20. }
   21. ]
   22. }
   ```

## 运行效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/hOpOTHskS1-zMmx6XwZ3Bg/zh-cn_image_0000002583478297.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234128Z&HW-CC-Expire=86400&HW-CC-Sign=7ACC6AA7F45BC601E46E4BBC9DFF4A2AA5D65B096819BFB059337A150BE771CD)
