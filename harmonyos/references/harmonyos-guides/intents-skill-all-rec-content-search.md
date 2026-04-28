---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-content-search
title: 内容搜索方案
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 本地搜索方案 > 接入方案 > 内容搜索方案
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0cfaadb1927ebdba3a1f7cb3d3833cab882b00db5de93a7394f34db5366afe97
---

## 方案概述

当用户使用应用/元服务时，开发者可以按照标准意图Schema（具体意图详见[各垂域意图Schema](../service/intents-schema-0000001901962713.md)）向系统共享数据（数据包含用户行为和内容实体），并实现意图调用（空调用与传参调用）。已实现用户点击卡片后，可后台执行功能（例如播放指定歌曲）或跳转至指定内容页面（例如指定的歌曲播放页面）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/kTRtySE3Qb6XyVJ8MEqGnA/zh-cn_image_0000002552959324.png?HW-CC-KV=V1&HW-CC-Date=20260427T235342Z&HW-CC-Expire=86400&HW-CC-Sign=AF6285942F2AF7139238DDE19D75595D8D4BC10301F75CF4D03F4860C5197BD0)

## 意图声明

以歌曲本地搜索特性为例，首先要注册播放歌曲意图（PlayMusic），其他意图见[各垂域意图Schema](../service/intents-schema-0000001901962713.md)。

开发者需要编辑对应的意图配置insight\_intent.json文件实现意图注册。insight\_intent.json文件需要放置在module下面的指定目录：src/main/resources/base/profile/insight\_intent.json，并且整个工程中只能存在一个insight\_intent.json文件。

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
16. "srcEntry": "./ets/entryability/InsightIntentExecutorImpl.ets",
17. "uiAbility": {
18. // 意图所在ability
19. "ability": "EntryAbility",
20. // UIAbility支持前后台两种执行模式
21. "executeMode": [
22. "background",
23. "foreground"
24. ]
25. }
26. }
27. ]
28. }
```

## 意图共享

构建意图对象，并且调用[insightIntent.shareIntent](../harmonyos-references/intents-arkts-api-insightintent.md#insightintentshareintent-1)，实现意图共享。可同时构建多个PlayMusic或PlayMusicList的意图对象。

以歌曲本地搜索特性为例，首先要注册播放歌曲意图（PlayMusic），其他意图见[各垂域意图Schema](../service/intents-schema-0000001901962713.md)。开发者需要编辑对应的意图配置insight\_intent.json文件实现意图注册。insight\_intent.json文件需要放置在module下面的指定目录：src/main/resources/base/profile/insight\_intent.json，并且整个工程中只能存在一个insight\_intent.json文件。

```
1. import { insightIntent } from '@kit.IntentsKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. let playMusicIntent1: insightIntent.InsightIntent;
4. let playMusicIntent2: insightIntent.InsightIntent;
5. // 共享数据接口  意图数组可以是更多的实体
6. insightIntent.shareIntent(this.context, [playMusicIntent1, playMusicIntent2]).then(() => {
7. console.info('shareIntent succeed');
8. }).catch((err: BusinessError) => {
9. console.error(`error.code: ${err?.code}, failed because ${err?.message}`);
10. });
```

PlayMusic的意图共享字段定义见[各垂域意图Schema](../service/intents-schema-0000001901962713.md)定义，代码示例如下：

```
1. import { insightIntent } from '@kit.IntentsKit';
2. let playMusicIntent: insightIntent.InsightIntent = {
3. intentName: "PlayMusic",
4. intentVersion: "1.0.1",
5. identifier: "52dac3b0-6520-4974-81e5-25f0879449b5",
6. intentActionInfo: {
7. actionMode: "EXECUTED",
8. executedTimeSlots: {
9. executedStartTime: 1637393212000,
10. executedEndTime: 1637393112000,
11. },
12. currentPercentage: 50,
13. },
14. intentEntityInfo: {
15. entityName: "Music",
16. entityId: "C10194368",
17. entityGroupId: "C10194321312",
18. displayName: "测试歌曲1",
19. description: "NA",
20. logoURL: "https://www-file.abc.com/-/media/corporate/images/home/logo/abc_logo.png",
21. keywords: ["华为音乐", "化妆"],
22. rankingHint: 99,
23. expirationTime: 1637393212000,
24. metadataModificationTime: 1637393212000,
25. activityType: ["1", "2", "3"],
26. artist: ["测试歌手1", "测试歌手2"],
27. lyricist: ["测试词作者1", "测试词作者2"],
28. composer: ["测试曲作者1", "测试曲作者2"],
29. albumName: "测试专辑",
30. duration: 244000,
31. playCount: 100000,
32. musicalGenre: ["流行", "华语", "金曲", "00后"],
33. isPublicData: false,
34. }
35. }
```

完整的意图共享示例如下所示，该示例构建了一个PlayMusic意图、一个PlayMusicList意图，并进行了shareIntent调用。

```
1. import { insightIntent } from '@kit.IntentsKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. let playMusicIntent: insightIntent.InsightIntent = {
4. intentName: "PlayMusic",
5. intentVersion: "1.0.1",
6. identifier: "52dac3b0-6520-4974-81e5-25f0879449b5",
7. intentActionInfo: {
8. actionMode: "EXECUTED",
9. executedTimeSlots: {
10. executedStartTime: 1637393212000,
11. executedEndTime: 1637393112000,
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
37. // 共享数据接口  意图数组可以是更多的实体
38. insightIntent.shareIntent(this.context, [playMusicIntent]).then(() => {
39. console.info('shareIntent succeed');
40. }).catch((err: BusinessError) => {
41. console.error(`error.code: ${err?.code}, failed because ${err?.message}`);
42. });
```

## 端侧意图调用

开发者需要自己实现InsightIntentExecutor，并在对应回调实现打开落地页（点击推荐卡片跳转的界面）或后台执行的能力，PlayMusic的意图调用字段定义见[各垂域意图Schema](../service/intents-schema-0000001901962713.md)。

步骤如下：

1. 继承InsightIntentExecutor。
2. 重写对应方法，例如目标拉起前台页面，则可重写onExecuteInUIAbilityForegroundMode方法。
3. 通过意图名称，识别播放歌曲意图（PlayMusic），在对应的方法中传递意图参数（param），并拉起对应落地页（如播放歌曲落地页）或后台执行（播放歌曲）。

```
1. import { insightIntent, InsightIntentExecutor } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. /**
5. * 意图调用样例
6. */
7. export default class InsightIntentExecutorImpl extends InsightIntentExecutor {
8. private static readonly PLAY_MUSIC = 'PlayMusic';
9. /**
10. * override 执行前台UIAbility意图
11. *
12. * @param name 意图名称
13. * @param param 意图参数
14. * @param pageLoader 窗口
15. * @returns 意图调用结果
16. */
17. onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>, pageLoader: window.WindowStage):
18. Promise<insightIntent.ExecuteResult> {
19. // 根据意图名称分发处理逻辑。接入方可根据实际业务实现页面跳转
20. switch (name) {
21. case InsightIntentExecutorImpl.PLAY_MUSIC:
22. return this.playMusic(param, pageLoader);
23. default:
24. break;
25. }
26. return Promise.resolve({
27. code: -1,
28. result: {
29. message: 'unknown intent'
30. }
31. } as insightIntent.ExecuteResult)
32. }
33. /**
34. * 实现调用播放歌曲功能
35. *
36. * @param param 意图参数
37. * @param pageLoader 窗口
38. */
39. private playMusic(param: Record<string, Object>, pageLoader: window.WindowStage): Promise<insightIntent.ExecuteResult> {
40. return new Promise((resolve, reject) => {
41. // TODO 实现意图调用，loadContent的入参为歌曲落地页路径，例如：pages/SongPage
42. pageLoader.loadContent('pages/SongPage')
43. .then(() => {
44. let entityId: string = (param.items as Array<object>)?.[0]?.['entityId'];
45. // TODO 调用成功的情况，此处可以打印日志
46. resolve({
47. code: 0,
48. result: {
49. message: 'Intent execute succeed'
50. }
51. });
52. })
53. .catch((err: BusinessError) => {
54. // TODO 调用失败的情况
55. resolve({
56. code: -1,
57. result: {
58. message: 'Intent execute failed'
59. }
60. })
61. });
62. })
63. }
```
