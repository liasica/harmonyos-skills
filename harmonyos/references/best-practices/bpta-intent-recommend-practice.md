---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-intent-recommend-practice
title: 意图框架习惯推荐场景
breadcrumb: 最佳实践 > AI使能 > 意图框架习惯推荐场景
category: best-practices
scraped_at: 2026-04-28T08:22:13+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:d2275b722516f348a421ce3c8c98e7f151c919664a87bec6dd989e65c4827d15
---

## 概述

意图框架是HarmonyOS系统级的意图标准体系。将应用和元服务的业务功能智能分发给不同的系统入口，以“音乐播放”为例，HarmonyOS将业务分发给“小艺建议”，提供了桌面大流量曝光，同时为开发者实现业务增长。习惯推荐类别下典型场景主要分为常用接续、常用复访以及常用推新三大类。比如“音乐播放”就属于常用接续场景。具体可参考[习惯推荐典型场景](../harmonyos-guides/intents-habit-rec-scene-experience.md#section19150165420493)。

* 常用接续：涵盖长视频、音乐、有声以及课程等领域，接续指在某个时间节点进行续播。
* 常用复访：涵盖导航、打车以及小游戏等领域，推荐用户经常使用的应用并展示卡片入口。
* 常用推新：涵盖资讯及短视频等领域，推荐用户新的资讯或者视频。

接入意图框架首先需要确定特性类别和具体意图，详细请参见[Intents Kit接入流程](../harmonyos-guides/intents-access-flow.md)。

本文以“音乐播放”意图为例，详细讲解意图接入与开发全过程。

## 音乐播放开发

以“音乐播放”为例，从意图注册、意图共享以及意图调用三大块介绍意图运行的开发过程。如果应用支持播放功能并且需要实现推荐播放接续，例如音乐、长视频以及课程的播放接续，可以参考本文。首先需要在设置中开启意图框架调试，如下图所示。确保意图框架调试开启且在界面成功展示设备支持测试应用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/pjgcil6PQM-vKyEWFfV-TA/zh-cn_image_0000002229337513.png?HW-CC-KV=V1&HW-CC-Date=20260428T001932Z&HW-CC-Expire=86400&HW-CC-Sign=974AB1D398A39962E9111C8193B3BB0C2164FBB324FAF5B698B77F8F56D1D61E "点击放大")

**开发步骤**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/WALY6QIbRCWmFN3Dez5dUg/zh-cn_image_0000002521635964.png?HW-CC-KV=V1&HW-CC-Date=20260428T001932Z&HW-CC-Expire=86400&HW-CC-Sign=F4382653C6E1029ED0BD47B78D0C69ADA005EC9D15C7E9C0885A1BCB5408AA46 "点击放大")

1. 在应用工程中新增PROJECT\_HOME/entry/src/main/resources/base/profile/insight\_intent.json文件注册意图，指定意图名称和所属垂域，并且指定一个意图调用逻辑入口。比如在本示例中将调用逻辑放在了EntryAbility下的InsightIntentExecutorImpl文件中。

   ```
   1. {
   2. "insightIntents": [
   3. {
   4. "intentName": "PlayMusic",
   5. "domain": "MusicDomain",
   6. "intentVersion": "1.0.1",
   7. "srcEntry": "./ets/entryability/InsightIntentExecutorImpl.ets",
   8. "uiAbility": {
   9. "ability": "EntryAbility",
   10. "executeMode": [
   11. "background",
   12. "foreground"
   13. ]
   14. }
   15. },
   16. {
   17. "intentName": "PlayMusicList",
   18. "domain": "MusicDomain",
   19. "intentVersion": "1.0.1",
   20. "srcEntry": "./ets/entryability/InsightIntentExecutorImpl.ets",
   21. "uiAbility": {
   22. "ability": "EntryAbility",
   23. "executeMode": [
   24. "background",
   25. "foreground"
   26. ]
   27. }
   28. }
   29. ]
   30. }
   ```
2. 新增PROJECT\_HOME/entry/src/main/resources/rawfile/config/shareIntent.json文件，定义共享数据。数据体除了意图名、版本和标识前三个公共字段外，必选字段还包括动作模式、当前播放百分比、实体名称和ID、音乐名、logo、歌手以及音乐时长等。以下是“音乐播放”的完整数据。具体意图共享字段含义可参考[各垂域意图Schema](../service/intents-schema-0000001901962713.md)中的音乐垂类。

   ```
   1. [
   2. {
   3. "intentName": "PlayMusic",
   4. "intentVersion": "1.0",
   5. "identifier": "52dac3b0-6520-4974-81e5-25f0879449b5",
   6. "intentActionInfo": {
   7. "actionMode": "EXECUTED",
   8. "executedTimeSlots": {
   9. "executedStartTime": 1637393112000,
   10. "executedEndTime": 1637393212000
   11. },
   12. "currentPercentage": 50
   13. },
   14. "intentEntityInfo": {
   15. "entityName": "Music",
   16. "entityId": "C10194368",
   17. "entityGroupId": "C10194321312",
   18. "displayName": "红颜如霜",
   19. "description": "NA",
   20. "logoURL": "https://www-file.huawei.com/-/media/corporate/images/home/logo/huawei_logo.png",
   21. "keywords": [
   22. "华为音乐",
   23. "化妆"
   24. ],
   25. "rankingHint": 99,
   26. "expirationTime": 1637393212000,
   27. "metadataModificationTime": 1637393212000,
   28. "activityType": [
   29. "1",
   30. "2",
   31. "3"
   32. ],
   33. "artist": [
   34. "测试歌手1",
   35. "测试歌手2"
   36. ],
   37. "lyricist": [
   38. "测试词作者1",
   39. "测试词作者2"
   40. ],
   41. "composer": [
   42. "测试曲作者1",
   43. "测试曲作者2"
   44. ],
   45. "albumName": "测试专辑",
   46. "duration": 244000,
   47. "playCount": 100000,
   48. "musicalGenre": [
   49. "流行",
   50. "话语",
   51. "抖音",
   52. "00后"
   53. ],
   54. "isPublicData": false
   55. }
   56. },
   57. {
   58. "intentName": "PlayMusicList",
   59. "intentVersion": "1.0",
   60. "identifier": "52dac3b0-6520-4974-81e5-25f0879449b5",
   61. "intentActionInfo": {
   62. "actionMode": "EXECUTED",
   63. "executedTimeSlots": {
   64. "executedStartTime": 1637393112000,
   65. "executedEndTime": 1637393212000
   66. },
   67. "currentPercentage": 50
   68. },
   69. "intentEntityInfo": {
   70. "entityName": "MusicList",
   71. "entityId": "C10194368",
   72. "entityGroupId": "C10194321312",
   73. "displayName": "测试歌单",
   74. "description": "这是xxx歌单",
   75. "logoURL": "https://www-file.huawei.com/-/media/corporate/images/home/logo/huawei_logo.png",
   76. "keyWords": [
   77. "抖音",
   78. "动感"
   79. ],
   80. "rankingHint": 99,
   81. "expirationTime": 1637393212000,
   82. "metadataModificationTime": 1637393212000,
   83. "activityType": [
   84. "1",
   85. "2",
   86. "3"
   87. ],
   88. "isPublicData": false,
   89. "briefDescription": "这是xxx歌单，来自xxx，是xxx风格",
   90. "artist": [
   91. "测试歌手1",
   92. "测试歌手2"
   93. ],
   94. "numberOfSongs": 20,
   95. "type": "1",
   96. "creator": "测试创建者",
   97. "createDate": "2023-10-08T08:00:00+08:00",
   98. "musicNameList": [
   99. "测试歌曲1",
   100. "测试歌曲2"
   101. ],
   102. "playCount": 30,
   103. "musicalGenre": [
   104. "流行",
   105. "华语",
   106. "抖音",
   107. "00后"
   108. ]
   109. }
   110. }
   111. ]
   ```
3. 调用[insightIntent.shareIntent()](../harmonyos-references/intents-arkts-api-insightintent.md#section144826162913)接口将意图对象输入到HarmonyOS，用于学习用户的行为规律。成功共享后“小艺建议”会展示对应应用的音乐模板卡片。展示效果如图所示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/gKQBF79STEiSzk9GRAx4Cg/zh-cn_image_0000002229337517.png?HW-CC-KV=V1&HW-CC-Date=20260428T001932Z&HW-CC-Expire=86400&HW-CC-Sign=C8ACCE7A7A5B6B047308B0AF9D4C37CAD959C7D3086AC86A87B8418CA3FEC057 "点击放大")

   ```
   1. static async shareIntent(context: Context, input: string): Promise<string> {
   2. Logger.debug(TAG, 'shareIntent');
   3. try {
   4. let insightIntents: insightIntent.InsightIntent[] = JSON.parse(input);
   5. if (!insightIntents || insightIntents.length === 0) {
   6. Logger.error(TAG, 'shareIntent: json invalid.');
   7. return 'shareIntent: json invalid.';
   8. }
   9. return await insightIntent.shareIntent(context, insightIntents).then(() => {
   10. Logger.info(TAG, 'shareIntent success');
   11. return 'share intent success';
   12. }, (err: BusinessError) => {
   13. Logger.error(TAG, `shareIntent error message: ${JSON.stringify(err)}`);
   14. return `shareIntent error message: ${JSON.stringify(err)}`;
   15. });
   16. } catch (err) {
   17. Logger.error(TAG, 'shareIntent fail', err);
   18. }
   19. return Promise.reject('shareIntent fail');
   20. }
   ```

   [InsightIntentSharer.ets](https://gitcode.com/harmonyos_samples/intents-kit-samplecode-clientdemo-arkts/blob/master/entry/src/main/ets/utils/InsightIntentSharer.ets#L34-L54)
4. 配置PROJECT\_HOME/entry/src/main/ets/entryability/InsightIntentExecutorImpl.ets文件，定义onExecuteInUIAbilityForegroundMode()方法。点击卡片，会拉起对应的应用并触发onCreate()和onExecuteInUIAbilityForegroundMode()等方法。意图调用如果会拉起应用界面，采取前台模式，如果不需要拉起采取后台模式。应用在foreground模式和background模式下会触发不同的生命周期与方法：

   | 前后台模式 | 启动模式 | 触发生命周期 |  |
   | --- | --- | --- | --- |
   | foreground | 冷启动 | onCreate->onWindowStageCreate->onExecuteInUIAbilityForegroundMode |  |
   |  | 热启动 | onNewWant->onExecuteInUIAbilityForegroundMode |  |
   | background | 冷启动 | onCreate->onExecuteInUIAbilityBackgroundMode |  |
   |  | 热启动 | onExecuteInUIAbilityBackgroundMode |  |

   本示例中采取foreground模式，可以在onCreate()或者onNewWant()解析want和launchParam。并将参数result存储在AppStorage中。如果是在真实开发中意图调用传参字段可以在开发前和接口方协商。

   ```
   1. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   2. Logger.info(TAG, 'onCreate');
   3. if (want.parameters?.['result']) {
   4. this.result = want.parameters?.['result'] as string;
   5. }
   6. }
   ```

   [EntryAbility.ets](https://gitcode.com/harmonyos_samples/intents-kit-samplecode-clientdemo-arkts/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L16-L22)

   want解析完毕后，会触发onExecuteInUIAbilityForegroundMode()方法进行真正逻辑处理，根据意图名称去分发处理方法并且返回一个Promise，成功调用code返回0，失败时返回-1。

   ```
   1. /**
   2. * Override the method to execute the intent in the foreground UIAbility.
   3. *
   4. * @param name Intent name.
   5. * @param param Intent parameters.
   6. * @param pageLoader Window.
   7. * @returns Intent call result.
   8. */
   9. onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>, pageLoader: window.WindowStage):
   10. Promise<insightIntent.ExecuteResult> {
   11. Logger.info(TAG, `onExecuteInUIAbilityForegroundMode name: ${name}, param: ${JSON.stringify(param)}`);
   12. // Distribute the processing logic based on the intent name.
   13. switch (name) {
   14. case InsightIntentExecutorImpl.PLAY_MUSIC:
   15. return this.playMusic(param, pageLoader);
   16. case InsightIntentExecutorImpl.PLAY_MUSIC_LIST:
   17. return this.playMusicList(param, pageLoader);
   18. default:
   19. break;
   20. }

   22. return Promise.resolve({
   23. code: -1,
   24. result: {
   25. message: 'unknown intent'
   26. }
   27. } as insightIntent.ExecuteResult)
   28. }
   ```

   [InsightIntentExecutorImpl.ets](https://gitcode.com/harmonyos_samples/intents-kit-samplecode-clientdemo-arkts/blob/master/entry/src/main/ets/entryability/InsightIntentExecutorImpl.ets#L20-L48)

   最后完成playMusic()的功能逻辑，小艺建议基于共享数据生成推荐卡片，点击卡片后将上述shareIntent.json定义的实体ID值传递到应用中。

   ```
   1. /**
   2. * Implement the music playback function.
   3. *
   4. * @param param Intent parameters.
   5. * @param pageLoader Window.
   6. */
   7. private playMusic(param: Record<string, Object>,
   8. pageLoader: window.WindowStage): Promise<insightIntent.ExecuteResult> {
   9. return new Promise((resolve, reject) => {
   10. let para: Record<string, string> = {
   11. 'result': `intent execute success, entityId: ${param.entityId}`
   12. };
   13. let localStorage: LocalStorage = new LocalStorage(para);
   14. // TODO Implement an intent call.
   15. pageLoader.loadContent('pages/Index', localStorage)
   16. .then(() => {
   17. // TODO The intent is called successfully.
   18. Logger.info(TAG, "Intent execute success");
   19. resolve({
   20. code: 0,
   21. result: {
   22. message: 'Intent execute success'
   23. }
   24. });
   25. })
   26. .catch((err: BusinessError) => {
   27. // TODO Handle the failure if the intent fails to be called.
   28. Logger.error(TAG, `Intent execute failed: ${JSON.stringify(err)}`);
   29. resolve({
   30. code: -1,
   31. result: {
   32. message: 'Intent execute failed'
   33. }
   34. })
   35. });
   36. })
   37. }
   ```

   [InsightIntentExecutorImpl.ets](https://gitcode.com/harmonyos_samples/intents-kit-samplecode-clientdemo-arkts/blob/master/entry/src/main/ets/entryability/InsightIntentExecutorImpl.ets#L51-L88)

   如果想删除掉意图，可以调用[insightIntent.deleteIntent()](../harmonyos-references/intents-arkts-api-insightintent.md#section138017435231)，在注册文件只有一个意图的情况下卡片入口会消失。运行效果如下图所示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/D7Cs__uBRgSNHWdLtZHLNA/zh-cn_image_0000002229452009.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001932Z&HW-CC-Expire=86400&HW-CC-Sign=03D963EA7914C3646641BE6B9B431A3E68000B360E3D3370A711C07ADF8F0B39 "点击放大")

说明

在真机设备上，小艺建议卡片不会实时刷新。可以通过点击卡片中的服务，重新返回到桌面后，进行卡片刷新。

## 示例代码

* [意图框架服务](https://gitcode.com/HarmonyOS_Samples/intents-kit-samplecode-clientdemo-arkts)
