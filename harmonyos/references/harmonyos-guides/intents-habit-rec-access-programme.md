---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-habit-rec-access-programme
title: 接入方案
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 习惯推荐方案 > 接入方案
category: harmonyos-guides
scraped_at: 2026-04-29T13:43:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:57f62a1f689f6438582305543786689a61cb2179d1d2873cb7fee90a1f366d34
---

## 方案概述

当用户在应用/元服务内使用功能时，开发者需要按照标准意图Schema向系统共享行为数据，并支持意图调用（空调用与传参调用），以实现用户点击模板卡后跳转回对应页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/nR_c_fSfRKCT8xk9qDp5tg/zh-cn_image_0000002589325683.png?HW-CC-KV=V1&HW-CC-Date=20260429T054329Z&HW-CC-Expire=86400&HW-CC-Sign=89D7542BD2A43E5786BBDCF14685CE814BD448E49B5CF1B7879EF91372099B0E)

## 意图注册

以歌曲续听推荐特性为例，首先要注册播放歌曲意图（PlayMusic），其他意图见[各垂域意图Schema](../service/intents-schema-0000001901962713.md)。

开发者需要编辑对应的意图配置insight\_intent.json文件实现意图声明。insight\_intent.json文件需要放置在任意一个module下面的指定目录：src/main/resources/base/profile/insight\_intent.json，并且整个工程中只能存在一个insight\_intent.json文件。

```
1. {
2. // 应用支持的意图列表
3. // 必须声明应用支持插件包含的必选意图，应用上架时会进行校验
4. "insightIntents": [
5. {
6. // 意图名称
7. // 名称应当遵循意图框架规范，当前仅支持预置垂域意图，不允许自定义
8. // 应用内意图名称唯一，不允许出现相同的名称定义
9. "intentName": "PlayMusic",
10. // 意图所属的垂域
11. "domain": "MusicDomain",
12. // 意图版本号
13. // 插件引用意图时会校验该版本号，只有和插件定义的版本号一致才能正常调用
14. "intentVersion": "1.0.1",
15. // 意图调用逻辑入口
16. // 根据意图调用文件实际路径和实际名称进行填写，此处文件仅做示意
17. "srcEntry": "./ets/entryability/InsightIntentExecutorImpl.ets",
18. "uiAbility": {
19. // 意图所在ability
20. "ability": "EntryAbility",
21. // UIAbility支持前后台两种执行模式
22. "executeMode": [
23. "background",
24. "foreground"
25. ]
26. }
27. }
28. ]
29. }
```

## 端侧意图共享

构建意图对象，并且调用[shareIntent()](../harmonyos-references/intents-arkts-api-insightintent.md#insightintentshareintent-1)，实现意图共享。可同时构建多个PlayMusic或PlayMusicList的意图对象。

```
1. import { insightIntent } from '@kit.IntentsKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let playMusicIntent1: insightIntent.InsightIntent;
5. let playMusicIntent2: insightIntent.InsightIntent;
6. // 共享数据接口  意图数组可以是更多的实体
7. // 根据实际代码上下文自行传入合适的context
8. insightIntent.shareIntent(context, [playMusicIntent1, playMusicIntent2]).then(() => {
9. console.info('shareIntent succeed');
10. }).catch((err: BusinessError) => {
11. console.error(`error.code: ${err?.code}, failed because ${err?.message}`);
12. });
```

PlayMusic的意图共享字段定义见[各垂域意图Schema](../service/intents-schema-0000001901962713.md)定义，代码示例如下：

```
1. import { insightIntent } from '@kit.IntentsKit';

3. let playMusicIntent: insightIntent.InsightIntent = {
4. intentName: "PlayMusic",
5. intentVersion: "1.0",
6. identifier: "52dac3b0-6520-4974-81e5-25f0879449b5",
7. intentActionInfo: {
8. actionMode: "EXECUTED",
9. executedTimeSlots: {
10. executedStartTime: 1637393112000,
11. executedEndTime: 1637393212000,
12. },
13. currentPercentage: 50,
14. },
15. intentEntityInfo: {
16. entityName: "Music",
17. entityId: "C10194368",
18. entityGroupId: "C10194321312",
19. displayName: "测试歌曲1",
20. description: "NA",
21. logoURL: "https://www-file.abc.com/-/media/corporate/images/home/logo/abc_logo.png",
22. keywords: ["华为音乐", "化妆"],
23. rankingHint: 99,
24. expirationTime: 1637393212000,
25. metadataModificationTime: 1637393212000,
26. activityType: ["1", "2", "3"],
27. artist: ["测试歌手1", "测试歌手2"],
28. lyricist: ["测试词作者1", "测试词作者2"],
29. composer: ["测试曲作者1", "测试曲作者2"],
30. albumName: "测试专辑",
31. duration: 244000,
32. playCount: 100000,
33. musicalGenre: ["流行", "华语", "金曲", "00后"],
34. isPublicData: false,
35. }
36. }
```

完整的意图共享示例如下所示，该示例构建了一个PlayMusic意图，并进行了shareIntent调用。

```
1. import { insightIntent } from '@kit.IntentsKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let playMusicIntent: insightIntent.InsightIntent = {
5. intentName: "PlayMusic",
6. intentVersion: "1.0",
7. identifier: "52dac3b0-6520-4974-81e5-25f0879449b5",
8. intentActionInfo: {
9. actionMode: "EXECUTED",
10. executedTimeSlots: {
11. executedStartTime: 1637393112000,
12. executedEndTime: 1637393212000,
13. },
14. currentPercentage: 50,
15. },
16. intentEntityInfo: {
17. entityName: "Music",
18. entityId: "C10194368",
19. entityGroupId: "C10194321312",
20. displayName: "测试歌曲1",
21. description: "NA",
22. logoURL: "https://www-file.abc.com/-/media/corporate/images/home/logo/abc_logo.png",
23. keywords: ["华为音乐", "化妆"],
24. rankingHint: 99,
25. expirationTime: 1637393212000,
26. metadataModificationTime: 1637393212000,
27. activityType: ["1", "2", "3"],
28. artist: ["测试歌手1", "测试歌手2"],
29. lyricist: ["测试词作者1", "测试词作者2"],
30. composer: ["测试曲作者1", "测试曲作者2"],
31. albumName: "测试专辑",
32. duration: 244000,
33. playCount: 100000,
34. musicalGenre: ["流行", "华语", "金曲", "00后"],
35. isPublicData: false,
36. }
37. }
38. // 共享数据接口  意图数组可以是更多的实体
39. // 根据实际代码上下文自行传入合适的context
40. insightIntent.shareIntent(context, [playMusicIntent]).then(() => {
41. console.info('shareIntent succeed');
42. }).catch((err: BusinessError) => {
43. console.error(`error.code: ${err?.code}, failed because ${err?.message}`);
44. });
```

## 端侧意图调用

### 意图执行组件为uiAbility的意图调用

如上文意图注册，当开发者注册的意图承载的运行组件为uiAbility时，开发者需要自己实现InsightIntentExecutor，并在对应回调实现打开落地页（点击推荐卡片跳转的界面）的能力，PlayMusic的意图调用字段定义见[各垂域意图Schema](../service/intents-schema-0000001901962713.md)。

步骤如下：

1. 继承InsightIntentExecutor。
2. 重写对应方法，例如目标拉起前台页面，则可重写onExecuteInUIAbilityForegroundMode方法。
3. 通过意图名称，识别播放歌曲意图（PlayMusic），在对应的方法中传递意图参数（param），并拉起对应落地页（如歌曲落地页）。

   ```
   1. import { insightIntent, InsightIntentExecutor } from '@kit.AbilityKit';
   2. import { window } from '@kit.ArkUI';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. /**
   6. * 意图调用样例
   7. */
   8. export default class InsightIntentExecutorImpl extends InsightIntentExecutor {
   9. private static readonly PLAY_MUSIC = 'PlayMusic';
   10. /**
   11. * override 执行前台UIAbility意图
   12. *
   13. * @param name 意图名称
   14. * @param param 意图参数
   15. * @param pageLoader 窗口
   16. * @returns 意图调用结果
   17. */
   18. onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>, pageLoader: window.WindowStage):
   19. Promise<insightIntent.ExecuteResult> {
   20. // 根据意图名称分发处理逻辑。接入方可根据实际业务实现页面跳转
   21. switch (name) {
   22. case InsightIntentExecutorImpl.PLAY_MUSIC:
   23. return this.playMusic(param, pageLoader);
   24. default:
   25. break;
   26. }
   27. return Promise.resolve({
   28. code: -1,
   29. result: {
   30. message: 'unknown intent'
   31. }
   32. } as insightIntent.ExecuteResult)
   33. }
   34. /**
   35. * 实现调用播放歌曲功能
   36. *
   37. * @param param 意图参数
   38. * @param pageLoader 窗口
   39. */
   40. private playMusic(param: Record<string, Object>, pageLoader: window.WindowStage): Promise<insightIntent.ExecuteResult> {
   41. return new Promise((resolve, reject) => {
   42. let para: Record<string, string> = {
   43. 'result': JSON.stringify(param)
   44. };
   45. let localStorage: LocalStorage = new LocalStorage(para);
   46. // TODO 实现意图调用，loadContent的入参为歌曲落地页路径，例如：pages/Index
   47. pageLoader.loadContent('pages/Index', localStorage)
   48. .then(() => {
   49. let entityId: string = (param.items as Array<object>)?.[0]?.['entityId'];
   50. // TODO 调用成功的情况，此处可以打印日志
   51. resolve({
   52. code: 0,
   53. result: {
   54. message: 'Intent execute succeed'
   55. }
   56. });
   57. })
   58. .catch((err: BusinessError) => {
   59. // TODO 调用失败的情况
   60. resolve({
   61. code: -1,
   62. result: {
   63. message: 'Intent execute failed'
   64. }
   65. })
   66. });
   67. })
   68. }
   69. }
   ```

### 意图执行组件为form的意图调用

如上文意图注册，当开发者注册的意图承载的运行组件为form（运行组件FormExtensionAbility）时，则需要开发者在实现的FormExtensionAbility中从want中获取并解析意图名和执行参数，用于卡片展示。

步骤如下：

1. 在意图执行绑定FormExtensionAbility的onAddForm(want: Want)中获取运行态意图框架传入的意图名（预定义keyName为ohos.insightIntent.executeParam.name）和意图执行参数（预定义keyName为ohos.insightIntent.executeParam.param）；
2. 通过意图名称，识别播放歌曲意图(PlayMusic)，在对应的方法中传递意图参数（param），并加载对应数据用于卡片展示。

```
1. import { Want } from '@kit.AbilityKit';
2. import { formBindingData, FormExtensionAbility } from '@kit.FormKit';

4. /**
5. * 卡片意图调用示例
6. */
7. export default class LoadCardFormAbility extends FormExtensionAbility {
8. onAddForm(want: Want): formBindingData.FormBindingData {
9. if (want?.parameters?.['ohos.insightIntent.executeParam.name'] != undefined) {
10. const intentName = want.parameters['ohos.insightIntent.executeParam.name']; //意图名
11. //TODO: 根据意图名称分发处理逻辑，若仅一个卡片意图，则可以忽略
12. }

14. if (want?.parameters?.['ohos.insightIntent.executeParam.param'] != undefined) {
15. const executeParameter = want.parameters['ohos.insightIntent.executeParam.param']; //意图执行参数
16. //TODO: 从 executeParameter 中解析具体意图执行参数，用于卡片内容展示
17. }

19. let formData = ''; //TODO: 仅示例，根据具体逻辑封装
20. return formBindingData.createFormBindingData(formData);
21. }
22. }
```
