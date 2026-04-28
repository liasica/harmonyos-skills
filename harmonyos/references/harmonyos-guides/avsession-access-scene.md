---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avsession-access-scene
title: 应用接入AVSession场景介绍
breadcrumb: 指南 > 媒体 > AVSession Kit（音视频播控服务） > 本地媒体会话 > 应用接入AVSession场景介绍
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1d548cc0ba682ae971c60cec5ec8bf543799b36f78c0be9c341f81f4c2563abf
---

音视频应用在实现音视频功能的同时，需要接入媒体会话即AVSession Kit，下文将提供一些典型的接入AVSession的展示和控制场景，方便开发者根据场景进行适配。

对于不同的场景，将会在系统的播控中心看到不同的UI呈现。同时，在不同的场景下，应用的接入处理也需要遵循不同的规范约束。

## 哪些场景下需要接入AVSession

AVSession会对后台的音频播放、VOIP通话做约束，所以通常来说，长音频应用、听书类应用、长视频应用、VOIP类应用等都需要接入AVSession。当应用在没有创建接入AVSession的情况下进行了上述业务，那么系统会在检测到应用后台时，停止对应的音频播放，静音通话声音，以达到约束应用行为的目的。这种约束，应用上架前在本地就可以验证。

对于其他使用到音频播放的应用，比如游戏、直播等场景，接入AVSession只是可选，取决于应用是否有后台播放的使用诉求。若应用需要后台播放，那么接入AVSession仍然是必须的，否则业务的正常功能会受到限制。

当应用需要实现后台播放等功能时，需要使用[BackgroundTasks Kit](background-task-overview.md)（后台任务管理）的能力，申请对应的长时任务，避免进入挂起（Suspend）状态。

## 接入流程

应用接入AVSession流程分为如下几个步骤：

1. 确定应用需要创建的会话类型，[创建对应的会话](avsession-access-scene.md#创建不同类型的会话)，不同类型决定了播控中心展示的控制模板样式。
2. 按需[创建后台任务](avsession-access-scene.md#创建后台任务)。
3. [设置必要的元数据（Metadata）](avsession-access-scene.md#设置元数据)，以在播控中心展示相应的信息，包括不限于：当前媒体的ID（assetId），上一首媒体的ID（previousAssetId），下一首媒体的ID（nextAssetId），标题（title），专辑作者（author），专辑名称（album），词作者（writer），媒体时长（duration）等属性。
4. [设置播放相关的状态](avsession-access-scene.md#设置播放状态)，包括不限于：当前媒体的播放状态（state）、播放位置（position）、播放倍速（speed）、缓冲时间（bufferedTime）、循环模式（loopMode）、是否收藏（isFavorite）、正在播放的媒体Id（activeItemId）、自定义媒体数据（extras）等属性。
5. 按需[注册不同的控制命令](avsession-access-scene.md#注册控制命令)，包括不限于：播放/暂停、上下一首、快进快退、收藏、循环模式、进度条。
6. 应用退出或者无对应业务时，注销会话。

## 创建不同类型的会话

AVSession在构造方法中支持不同的类型参数，由 [AVSessionType](../harmonyos-references/arkts-apis-avsession-t.md#avsessiontype10) 定义，不同的类型代表了不同场景的控制能力，对于播控中心来说，会展示不同的控制模版。

* audio类型，播控中心的控制样式为：收藏，上一首，播放/暂停，下一首，循环模式。
* video类型，播控中心的控制样式为：快退，上一首，播放/暂停，下一首，快进。
* voice\_call类型，通话类型。

使用代码示例：

说明

以下示例代码仅展示创建AVSession对象的接口调用，应用在真正使用时，需要确保AVSession对象实例在应用后台播放业务活动期间一直存在，避免被系统回收、释放，导致后台发声时被系统管控。

```
1. import { avSession as AVSessionManager } from '@kit.AVSessionKit';
2. // ...

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'hello world';
8. // ...

10. build() {
11. Column() {
12. // ...
13. Text(this.message)
14. .onClick(async () => {
15. // 开始创建并激活媒体会话。
16. // 创建session。
17. let context = this.getUIContext().getHostContext() as Context;
18. let type: AVSessionManager.AVSessionType = 'audio';
19. let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
20. // 激活接口要在元数据、控制命令注册完成之后再执行。
21. await session.activate();
22. console.info(`session create done : sessionId : ${session.sessionId}`);
23. // ...
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

## 创建后台任务

当应用需要实现后台播放等功能时，需要使用[BackgroundTasks Kit](background-task-overview.md)（后台任务管理）的能力，申请对应的长时任务，避免进入挂起（Suspend）状态。

对媒体类播放来说，需要申请[AUDIO\_PLAYBACK BackgroundMode](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundmode)的长时任务。

## 设置元数据

### 通用元数据

应用可以通过setAVMetadata把会话的一些元数据信息设置给系统，从而在播控中心界面进行展示，包括但不限于：当前媒体的ID（assetId），上一首媒体的ID（previousAssetId），下一首媒体的ID（nextAssetId），标题（title），专辑作者（author），专辑名称（album），词作者（writer），媒体时长（duration）等。

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
16. try {
17. let context = this.getUIContext().getHostContext() as Context;
18. // 假设已经创建了一个session，如何创建session可以参考之前的案例。
19. let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', 'audio');
20. // 设置必要的媒体信息。
21. let metadata: AVSessionManager.AVMetadata = {
22. assetId: '0', // 由应用指定，用于标识应用媒体库里的媒体。
23. title: 'TITLE',
24. mediaImage: 'IMAGE',
25. artist: 'ARTIST',
26. };
27. session.setAVMetadata(metadata).then(() => {
28. console.info(`SetAVMetadata successfully`);
29. // ...
30. }).catch((err: BusinessError) => {
31. console.error(`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}`);
32. // ...
33. });
34. } catch (err) {
35. if (err) {
36. console.error(`AVSession create Error: Code: ${err.code}, message: ${err.message}`);
37. // ...
38. }
39. }
40. })
41. }
42. .width('100%')
43. .height('100%')
44. }
45. }
```

### 歌词

对于长音频来说，播控中心提供了歌词的展示页面，对于应用来说，接入也比较简单，只需要把歌词内容设置给系统。播控中心会解析歌词内容，并根据播放进度进行同步的刷新。

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
18. let type: AVSessionManager.AVSessionType = 'audio';
19. let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);

21. // 把歌词信息设置给AVSession。
22. let metadata: AVSessionManager.AVMetadata = {
23. assetId: '0',
24. title: 'TITLE',
25. mediaImage: 'IMAGE',
26. // LRC中有两类元素：一种是时间标签+歌词，一种是ID标签。
27. // 例如：[00:25.44]xxx\r\n[00:26.44]xxx\r\n。
28. lyric: 'lrc格式歌词内容',
29. // singleLyricText字段存储单条歌词文本，不包含时间戳。
30. // 例如："单条歌词内容"。
31. singleLyricText: '单条歌词内容',
32. };
33. session.setAVMetadata(metadata).then(() => {
34. console.info(`SetAVMetadata successfully`);
35. // ...
36. }).catch((err: BusinessError) => {
37. console.error(`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}`);
38. // ...
39. });
40. // ...
41. })
42. }
43. .width('100%')
44. .height('100%')
45. }
46. }
```

### 历史歌单

针对音乐/听书类应用，播控中心提供一系列快捷播放能力，包括一键启动冷启动续播、以及历史歌单功能，其中歌单功能中支持显示的音频媒体内容有：音乐歌单、有声书专辑、播客专辑等。视频媒体内容、直播类媒体内容暂不支持歌单。应用在端侧注册并适配后台启动模式的[播放意图](intents-habit-rec-access-programme.md)，即可实现接入上述功能。接入后的体验自检，可以参考[快捷播放](quick-playback.md)。

开发者可参考下述示例，完成注册播放意图、设置歌单信息、实现意图启动播放。

**注册播放意图**

应用按照播放业务，选择PlayMusicList意图（音乐类应用）或者PlayAudio意图（听书类应用）其一注册。编辑对应的意图配置PROJECT\_HOME/entry/src/main/resources/base/profile/insight\_intent.json文件，实现播放意图注册。

注册示例如下：

```
1. {
2. // 应用支持的意图列表
3. "insightIntents": [
4. {
5. // 意图名称
6. // 名称应当遵循意图框架规范，当前仅支持预置垂域意图，不允许自定义
7. // 应用内意图名称唯一，不允许出现相同的名称定义
8. "intentName": "PlayMusicList", // 音乐类PlayMusicList，听书或有声书类PlayAudio
9. // 意图所属的垂域
10. "domain": "MusicDomain", // 音乐类MusicDomain，听书或有声书类AudioDomain
11. // 意图版本号
12. // 插件引用意图时会校验该版本号，只有和插件定义的版本号一致才能正常调用
13. "intentVersion": "1.0.1",
14. // 意图调用代码逻辑入口
15. "srcEntry": "./ets/entryability/InsightIntentExecutorImpl.ets",
16. "uiAbility": {
17. // 意图所在module、ability，以及代码相对路径入口
18. "ability": "EntryAbility",
19. // UIAbility支持前后台两种执行模式
20. "executeMode": [
21. "background", // 播控一键冷启动、历史歌单功能需要应用支持意图后台启动
22. "foreground"
23. ]
24. }
25. }
26. ]
27. }
```

**设置歌单信息**

通过[setAVMetadata](../harmonyos-references/arkts-apis-avsession-avsession.md#setavmetadata10)接口设置当前播放的歌单（专辑）信息，歌单（专辑）信息由下面几个字段组成：

* avQueueName: 歌单的名称，接入歌单必选
* avQueueId: 歌单的唯一标识id，接入歌单必选
* avQueueImage: 歌单的图片资源，接入歌单必选

系统媒体信息根据应用上报实时刷新，若应用接入歌单功能，则确保在[AVMetadata](../harmonyos-references/arkts-apis-avsession-i.md#avmetadata10)中一直携带歌单数据。

```
1. import { avSession as AVSessionManager } from '@kit.AVSessionKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let context: Context = getContext(this);
5. async function setListener() {
6. // 假设已经创建了一个session，如何创建session可以参考之前的案例
7. let type: AVSessionManager.AVSessionType = 'audio';
8. let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
9. // 将歌单信息设置给AVSession
10. let metadata: AVSessionManager.AVMetadata = {
11. // 下面内容均由应用设置
12. assetId: 'musicid123',
13. avQueueName: 'myQueue',
14. avQueueId: 'myQueue123',
15. avQueueImage: "PIXELMAP_OBJECT",
16. };
17. session.setAVMetadata(metadata).then(() => {
18. console.info(`SetAVMetadata successfully`);
19. }).catch((err: BusinessError) => {
20. console.error(`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}`);
21. });
22. // 上报播放状态，参考播放状态
23. }
```

**实现意图启动播放**

当应用接入歌单功能后，用户在系统播控中心界面可以播放应用的歌单，也可以在应用进程释放后，通过系统播控中心再次冷启动应用后台播放。

* 用户触发歌单播放时，系统会将歌单的唯一标识id传回应用，应用可以在意图调用接口中，通过解析意图参数(intentParam)中的entityId，获取到歌单的id，实现对应歌单的播放。
* 用户触发播控冷启动播放时，系统会在意图参数(intentParam)的包含空歌单id，即解析出得的entityId为空字符串，**由应用来决定播放内容**，可以实现为续播上一次的播放内容。
* **系统会在后台冷启动应用的播放，需要在播放前先设置[AVMetadata](../harmonyos-references/arkts-apis-avsession-i.md#avmetadata10)，注册[播控控制回调](avsession-access-scene.md#注册控制命令)，并申请播音长时任务。**

```
1. import { insightIntent, InsightIntentExecutor } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. /**
6. * 意图调用样例
7. */
8. export default class InsightIntentExecutorImpl extends InsightIntentExecutor {
9. /**
10. * override 执行后台启动UIAbility意图
11. *
12. * @param intentName 意图名称
13. * @param intentParam 意图参数
14. * @returns 意图调用结果
15. */
16. async onExecuteInUIAbilityBackgroundMode(intentName: string, intentParam: Record<string, Object>):
17. Promise<insightIntent.ExecuteResult> {
18. // 根据意图名称分发处理逻辑
19. switch (intentName) {
20. case 'PlayMusicList':
21. // PlayMusicList参照如下解析方式
22. let entityId: string = (intentParam.items as Array<object>)?.[0]?.['entityId'];
23. return this.playFunc(entityId);
24. case 'PlayAudio':
25. // PlayAudio参照如下解析方式
26. let data = intentParam as Record<string, string>;
27. return this.playFunc(data.entityId);
28. default:
29. break;
30. }
31. return Promise.resolve({
32. code: -1,
33. result: {
34. message: 'unknown intent'
35. }
36. } as insightIntent.ExecuteResult)
37. }

39. /**
40. * 实现调用播放功能
41. *
42. * @param entityId 播放内容id
43. */
44. private playFunc(entityId: string): Promise<insightIntent.ExecuteResult> {
45. // entityId 不为空，表示用户指定内容（歌单/专辑）播放
46. // entityId 为空（entityId.length == 0），由应用自行决定播放内容，续播历史内容或者是推荐内容
47. // 此时是后台拉起应用播放，除了初始化播放资源，还需要设置AVMetadata，注册播控控制回调，并申请播音长时任务
48. // TODO 实现具体的播放业务
49. return Promise.resolve({
50. code: 0,
51. result: {
52. message: 'Intent execute succeed'
53. }
54. } as insightIntent.ExecuteResult)
55. }
56. }
```

### 媒体资源金标

对于长音频，播控中心提供了媒体资源金标（即应用媒体音频音源的标识）的展示，目前只支持展示Audio Vivid标识。

对于应用来说，接入只需要在AVMetadata中通知系统，当前播放音频的音源标识，播控就会同步展示。

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
18. let type: AVSessionManager.AVSessionType = 'audio';
19. let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);

21. // 把媒体音源信息设置给AVSession。
22. let metadata: AVSessionManager.AVMetadata = {
23. assetId: '0',
24. title: 'TITLE',
25. mediaImage: 'IMAGE',
26. // 标识该媒体音源是Audio Vivid。
27. displayTags: AVSessionManager.DisplayTag.TAG_AUDIO_VIVID,
28. };
29. session.setAVMetadata(metadata).then(() => {
30. console.info(`SetAVMetadata successfully`);
31. // ...
32. }).catch((err: BusinessError) => {
33. console.error(`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}`);
34. // ...
35. });
36. // ...
37. })
38. }
39. .width('100%')
40. .height('100%')
41. }
42. }
```

## 设置播放状态

### 通用播放状态

应用可以通过[setAVPlaybackState](../harmonyos-references/arkts-apis-avsession-avsession.md#setavplaybackstate10)。把当前的播放状态设置给系统，以在播控中心界面进行展示。

播放状态一般是在资源播放后会进行变化的内容，包括：当前媒体的播放状态（state）、播放位置（position）、播放倍速（speed）、缓冲时间（bufferedTime）、循环模式（loopMode）、是否收藏（isFavorite）、正在播放的媒体Id（activeItemId）、自定义媒体数据（extras）等。

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

20. // 播放器逻辑··· 引发媒体信息与播放状态的变更。
21. // 简单设置一个播放状态 - 暂停 未收藏。
22. let playbackState: AVSessionManager.AVPlaybackState = {
23. state: AVSessionManager.PlaybackState.PLAYBACK_STATE_PAUSE,
24. isFavorite: false
25. };
26. session.setAVPlaybackState(playbackState, (err: BusinessError) => {
27. if (err) {
28. console.error(`Failed to set AVPlaybackState. Code: ${err.code}, message: ${err.message}`);
29. // ...
30. } else {
31. console.info(`SetAVPlaybackState successfully`);
32. // ...
33. }
34. });
35. // ...
36. })
37. }
38. .width('100%')
39. .height('100%')
40. }
41. }
```

### 进度条

应用如果支持在播控中心展示进度，那么在媒体资源播放中，需要设置资源的时长、播放状态（暂停、播放）、播放位置、倍速，播控中心会使用这些信息进行进度的展示：

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
18. let type: AVSessionManager.AVSessionType = 'audio';
19. let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);

21. // 设置媒体资源时长。
22. let metadata: AVSessionManager.AVMetadata = {
23. assetId: '0',
24. title: 'TITLE',
25. mediaImage: 'IMAGE',
26. duration: 23000, // 资源的时长，以ms为单位。
27. };
28. session.setAVMetadata(metadata).then(() => {
29. console.info(`SetAVMetadata successfully`);
30. // ...
31. }).catch((err: BusinessError) => {
32. console.error(`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}`);
33. // ...
34. });

36. // 设置状态： 播放状态，进度位置，播放倍速，缓存的时间。
37. let playbackState: AVSessionManager.AVPlaybackState = {
38. state: AVSessionManager.PlaybackState.PLAYBACK_STATE_PLAY, // 播放状态。
39. position: {
40. elapsedTime: 1000, // 已经播放的位置，以ms为单位。
41. updateTime: new Date().getTime(), // 应用更新当前位置时的时间戳，以ms为单位。
42. },
43. speed: 1.0, // 可选，默认是1.0，播放的倍速，按照应用内支持的speed进行设置，系统不做校验。
44. bufferedTime: 14000, // 可选，资源缓存的时间，以ms为单位。
45. };
46. session.setAVPlaybackState(playbackState, (err) => {
47. if (err) {
48. console.error(`Failed to set AVPlaybackState. Code: ${err.code}, message: ${err.message}`);
49. // ...
50. } else {
51. console.info(`SetAVPlaybackState successfully`);
52. // ...
53. }
54. });
55. // ...
56. })
57. }
58. .width('100%')
59. .height('100%')
60. }
61. }
```

系统的播控中心会根据应用设置的信息自行进行播放进度的计算，而不需要应用实时更新播放进度；但是应用需要如下状态发生变化的时候，再更新AVPlaybackState，否则系统会发生计算错误。

* state
* position
* speed

应用在真实播放开始时，再上报进度起始position；若播放存在buffer状态，可以先上报播放状态为AVSessionManager.PlaybackState.PLAYBACK\_STATE\_BUFFERING，来通知系统不刷新进度。

关于进度条有一些特殊情况需要处理：

1. 歌曲支持试听

   （1）应用不需要设置完整的歌曲时长，则只需要设置歌曲的试听时长。当应用仅设置歌曲的试听时长而不是完整时长，用户在播控中心触发进度控制时，应用收到的时长也是VIP试听时长内的相对时间戳位置，而不是完整歌曲的绝对时间戳位置，应用需要重新计算歌曲从零开始的绝对时间戳进行实际响应处理。

   （2）如果应用设置完整歌曲时长，但需要系统支持试听片段，也可以在播放时上报起始进度position，当收到的seek指令超过试听片段时，上报试听截止position，系统播控的进度会跟随回弹。
2. 歌曲不支持试听

   如果歌曲不支持试听，那么理论上应用内也不支持播放，这时可以把 duration 设置为 -1，以通知系统不显示实际的时长。
3. 广告等内容的时长设置

   对于有前贴广告、后贴广告的资源来说，建议这么处理：

   * 播放广告时，单独设置广告的时长 duration。
   * 当进入到正片播放的时候，则重新设置一次新的时长，以与广告进行区分。

## 注册控制命令

应用接入AVSession，可以通过注册不同的控制命令来实现播控中心界面上的控制操作，即通过on接口注册不同的控制命令参数，即可实现对应的功能。

具体的接口参考[接口注册](../harmonyos-references/arkts-apis-avsession-avsession.md#onplay10)。

说明

创建AVSession后，请先注册应用支持的控制命令，再激活 Session。

媒体资源支持的控制命令列表：

| 控制命令 | 功能说明 |
| --- | --- |
| play | 播放命令。 |
| pause | 暂停命令。 |
| stop | 停止命令。 |
| playNext | 播放下一首命令。 |
| playPrevious | 播放上一首命令。 |
| fastForward | 快进命令。 |
| rewind | 快退命令。 |
| playFromAssetId | 根据某个资源id进行播放命令。 |
| seek | 跳转命令。 |
| setSpeed | 设置播放速率命令。 |
| setLoopMode | 设置循环模式命令。 |
| toggleFavorite | 设置是否收藏命令。 |
| skipToQueueItem | 设置播放列表其中某项被选中播放的命令。 |
| handleKeyEvent | 设置按键事件的命令。 |
| commonCommand | 设置自定义控制命令。 |

通话类应用支持的控制：

| 控制命令 | 功能说明 |
| --- | --- |
| answer | 接听电话的命令。 |
| hangUp | 通话挂断的命令。 |
| toggleCallMute | 通话静音或解除静音的命令。 |

### 不支持命令的处理

系统支持的控制命令对于不支持的控制，比如应用不支持“上一首”的命令处理，只需要使用off 接口注销对应的控制命令，系统的播控中心会相应的对该控制界面进行置灰处理，以明确告知用户此控制命令不支持。

```
1. import { avSession as AVSessionManager } from '@kit.AVSessionKit';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'hello world';

8. build() {
9. Column() {
10. Text(this.message)
11. .onClick(async () => {
12. let context = this.getUIContext().getHostContext() as Context;
13. // 假设已经创建了一个session，如何创建session可以参考之前的案例。
14. let type: AVSessionManager.AVSessionType = 'audio';
15. let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);

17. // 取消指定session下的相关监听。
18. session.off('play');
19. session.off('pause');
20. session.off('stop');
21. session.off('playNext');
22. session.off('playPrevious');
23. // ...
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

### 快进快退

系统支持三种快进/快退的时长，应用可以通过接口进行设置；同时注册快进/快退的回调命令，以响应控制。

说明

应用注册快进/快退及上/下一首资源切换的命令时，在播控中心的显示存在实际差异。

* **当AVSessionType是audio时：**

  | 应用注册的事件组合 | 播放中心显示按钮 | 按钮是否可用 |
  | --- | --- | --- |
  | 未注册任何事件 | “上一首”、“下一首” | 所有按钮置灰，无法点击。 |
  | 注册上一首/下一首事件 | “上一首”、“下一首” | 注册上一首事件 →“上一首”按钮可用。  注册下一首事件 →“下一首”按钮可用。  未注册对应事件的按钮不可用。 |
  | 注册快进/快退事件 | “上一首”、“下一首” | 所有按钮置灰，无法点击。 |
  | 注册上一首/下一首及快进/快退事件 | “上一首”、“下一首” | 注册上一首事件 →“上一首”按钮可用。  注册下一首事件 →“下一首”按钮可用。  未注册对应事件的按钮不可用。 |
* **当AVSessionType是video时：**

  | 应用注册的事件组合 | 播放中心显示按钮 | 按钮是否可用 |
  | --- | --- | --- |
  | 未注册任何事件 | “快进”、“快退” | 所有按钮置灰，无法点击。 |
  | 注册上一首/下一首事件 | “上一首”、“下一首” | 注册上一首事件 →“上一首”按钮可用。  注册下一首事件 →“下一首”按钮可用。  未注册对应事件的按钮不可用。 |
  | 注册快进/快退事件 | “快进”、“快退” | 注册快进事件 →“快进”按钮可用。  注册快退事件 →“快退”按钮可用。  未注册对应事件的按钮不可用。 |
  | 注册上一首/下一首及快进/快退事件 | “快进”、“快退” | 注册快进事件 →“快进”按钮可用。  注册快退事件 →“快退”按钮可用。  未注册对应事件的按钮不可用。 |

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
  18. let type: AVSessionManager.AVSessionType = 'audio';
  19. let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
  20. // ...

  22. // 设置支持的快进快退的时长设置给AVSession。
  23. let metadata: AVSessionManager.AVMetadata = {
  24. assetId: '0', // Specified by the application, used to identify the media asset in the application media library.
  25. title: 'TITLE',
  26. mediaImage: 'IMAGE',
  27. skipIntervals: AVSessionManager.SkipIntervals.SECONDS_10,
  28. };
  29. session.setAVMetadata(metadata).then(() => {
  30. console.info(`SetAVMetadata successfully`);
  31. // ...
  32. }).catch((err: BusinessError) => {
  33. console.error(`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}`);
  34. // ...
  35. });

  37. session.on('fastForward', (time ?: number) => {
  38. console.info(`on fastForward , do fastForward task`);
  39. // ...
  40. // do some tasks ···
  41. });
  42. session.on('rewind', (time ?: number) => {
  43. console.info(`on rewind , do rewind task`);
  44. // ...
  45. // do some tasks ···
  46. });
  47. // ...
  48. })
  49. }
  50. .width('100%')
  51. .height('100%')
  52. }
  53. }
  ```

### 收藏

音乐类应用实现收藏功能，那么需要注册收藏的控制响应[on('toggleFavorite')](../harmonyos-references/arkts-apis-avsession-avsession.md#ontogglefavorite10)。

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
18. let type: AVSessionManager.AVSessionType = 'audio';
19. let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
20. // ...
21. session.on('toggleFavorite', (assetId) => {
22. console.info(`on toggleFavorite `);
23. // ...
24. // 应用收到收藏命令，进行收藏处理。

26. // 应用内完成或者取消收藏，把新的收藏状态设置给AVSession。
27. let playbackState: AVSessionManager.AVPlaybackState = {
28. isFavorite: true,
29. };
30. session.setAVPlaybackState(playbackState).then(() => {
31. console.info(`SetAVPlaybackState successfully`);
32. // ...
33. }).catch((err: BusinessError) => {
34. console.error(`SetAVPlaybackState BusinessError: code: ${err.code}, message: ${err.message}`);
35. // ...
36. });
37. });
38. // ...
39. })
40. }
41. .width('100%')
42. .height('100%')
43. }
44. }
```

### 循环模式

针对音乐类应用，系统的播控中心界面会默认展示循环模式的控制操作，目前系统支持四种固定的循环模式控制，参考: [LoopMode](../harmonyos-references/arkts-apis-avsession-e.md#loopmode10)。

播控中心支持固定的四种循环模式的切换，即： 随机播放、顺序播放、单曲循环、列表循环。应用收到循环模式切换的指令并切换后，需要向系统上报切换后的LoopMode。

若应用内支持的LoopMode不在系统固定的四个循环模式内，需要选择四个固定循环模式其一向系统上报，由应用自定。

实现参考：

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
18. let type: AVSessionManager.AVSessionType = 'audio';
19. let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
20. // ...

22. // 应用启动时/内部切换循环模式，需要把应用内的当前的循环模式设置给AVSession。
23. let playBackState: AVSessionManager.AVPlaybackState = {
24. loopMode: AVSessionManager.LoopMode.LOOP_MODE_SINGLE,
25. };
26. session.setAVPlaybackState(playBackState).then(() => {
27. console.info(`set AVPlaybackState successfully`);
28. // ...
29. }).catch((err: BusinessError) => {
30. console.error(`Failed to set AVPlaybackState. Code: ${err.code}, message: ${err.message}`);
31. // ...
32. });

34. // 应用注册循环模式的控制监听。
35. session.on('setLoopMode', (mode) => {
36. console.info(`on setLoopMode ${mode}`);
37. // ...
38. // 应用收到设置循环模式的指令后，应用自定下一个模式，切换完毕后通过AVPlaybackState上报切换后的LoopMode。
39. let playBackState: AVSessionManager.AVPlaybackState = {
40. loopMode: AVSessionManager.LoopMode.LOOP_MODE_SINGLE,
41. };
42. session.setAVPlaybackState(playBackState).then(() => {
43. console.info(`set AVPlaybackState successfully`);
44. // ...
45. }).catch((err: BusinessError) => {
46. console.error(`Failed to set AVPlaybackState. Code: ${err.code}, message: ${err.message}`);
47. // ...
48. });
49. });
50. // ...
51. })
52. }
53. .width('100%')
54. .height('100%')
55. }
56. }
```

### 进度控制

应用如果支持进度显示，进一步也可以支持进度控制。应用需要响应seek的控制命令，那么当用户在播控中心的界面上进行拖动操作时，应用就会收到对应的回调。参考实现：

```
1. import { avSession as AVSessionManager } from '@kit.AVSessionKit';
2. // ...

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'hello world';
8. // ...

10. build() {
11. Column() {
12. // ...
13. Text(this.message)
14. .onClick(async () => {
15. let context = this.getUIContext().getHostContext() as Context;
16. // 假设已经创建了一个session，如何创建session可以参考之前的案例。
17. let type: AVSessionManager.AVSessionType = 'audio';
18. let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
19. // ...

21. session.on('seek', (position: number) => {
22. console.info(`on seek , the time is ${JSON.stringify(position)}`);
23. // ...

25. // 由于应用内seek可能会触发较长的缓冲等待，可以先把状态设置为 Buffering。
26. let playbackState: AVSessionManager.AVPlaybackState = {
27. state: AVSessionManager.PlaybackState.PLAYBACK_STATE_BUFFERING, // Buffering state.
28. };
29. session.setAVPlaybackState(playbackState, (err) => {
30. if (err) {
31. console.error(`Failed to set AVPlaybackState. Code: ${err.code}, message: ${err.message}`);
32. // ...
33. } else {
34. console.info(`SetAVPlaybackState successfully`);
35. // ...
36. }
37. });

39. // 应用响应seek命令，使用应用内播放器完成seek实现。

41. // 应用内更新新的位置后，也需要同步更新状态给系统。
42. playbackState.state = AVSessionManager.PlaybackState.PLAYBACK_STATE_PLAY; // 播放状态。
43. playbackState.position = {
44. elapsedTime: position, // 已经播放的位置，以ms为单位。
45. updateTime: new Date().getTime(), // 应用更新当前位置的时间戳，以ms为单位。
46. }
47. session.setAVPlaybackState(playbackState, (err) => {
48. if (err) {
49. console.error(`Failed to set AVPlaybackState. Code: ${err.code}, message: ${err.message}`);
50. // ...
51. } else {
52. console.info(`SetAVPlaybackState successfully`);
53. // ...
54. }
55. });
56. });

58. // ...
59. })
60. }
61. .width('100%')
62. .height('100%')
63. }
64. }
```

## 适配媒体通知

当前系统不直接向应用提供主动发送媒体控制通知的接口，那么当应用正确接入媒体播控中心并进入播放状态时，系统会自动发送通知，同时在通知和锁屏界面进行展示。

说明

通知中心、锁屏下的播控卡片的展示，由系统进行发送，并控制相应的生命周期。

## 适配蓝牙按键与有线按键事件

当前系统不直接向应用提供监听多模按键事件的接口，应用如需要监听蓝牙与有线耳机的媒体按键事件，可以通过注册AVSession的控制指令来实现。AVSession提供了如下两种实现方式：

* 方式一（推荐使用）：

  按照应用业务需求，正确接入媒体播控中心，[注册需要的控制指令](avsession-access-scene.md#注册控制命令)并实现对应的功能。AVSession会监听多模按键事件，将其转换为AVSession的控制指令发送回应用。应用无须区分不同的按键事件，按照AVSession的回调处理即可。按照此方式接入播放暂停，也等同于适配了蓝牙耳机的佩戴检测，在双耳佩戴与摘下时也会收到如下播放暂停控制指令。目前支持转换的AVSession控制指令如下：

  | 控制命令 | 功能说明 |
  | --- | --- |
  | play | 播放命令。 |
  | pause | 暂停命令。 |
  | stop | 停止命令。 |
  | playNext | 播放下一首命令。 |
  | playPrevious | 播放上一首命令。 |
  | fastForward | 快进命令。 |
  | rewind | 快退命令。 |

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
  16. try {
  17. let context = this.getUIContext().getHostContext() as Context;
  18. let type: AVSessionManager.AVSessionType = 'audio';
  19. let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
  20. // ...
  21. // 设置必要的媒体信息，务必设置，否则接收不到控制事件。
  22. let metadata: AVSessionManager.AVMetadata = {
  23. assetId: '0', // 由应用指定，用于标识应用媒体库里的媒体。
  24. title: 'TITLE',
  25. mediaImage: 'IMAGE',
  26. artist: 'ARTIST'
  27. };
  28. session.setAVMetadata(metadata).then(() => {
  29. console.info(`SetAVMetadata successfully`);
  30. // ...
  31. }).catch((err: BusinessError) => {
  32. console.error(`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}`);
  33. // ...
  34. });
  35. // 一般在监听器中会对播放器做相应逻辑处理。
  36. // 处理完后需要通过set接口同步播放相关信息，参考上面的用例。
  37. session.on('play', () => {
  38. console.info(`on play , do play task`);
  39. // ...
  40. // 如暂不支持该指令，请勿注册；或在注册后但暂不使用时，通过session.off('play')取消监听。
  41. // 处理完毕后，请使用setAVPlayState上报播放状态。
  42. });
  43. session.on('pause', () => {
  44. console.info(`on pause , do pause task`);
  45. // ...
  46. // 如暂不支持该指令，请勿注册；或在注册后但暂不使用时，通过session.off('pause')取消监听。
  47. // 处理完毕后，请使用setAVPlayState上报播放状态。
  48. });
  49. // ...
  50. } catch (err) {
  51. if (err) {
  52. console.error(`AVSession create Error: Code: ${err.code}, message: ${err.message}`);
  53. // ...
  54. }
  55. }
  56. })
  57. }
  58. .width('100%')
  59. .height('100%')
  60. }
  61. }
  ```
* 方式二：

  通过AVSession注册[HandleMediaKeyEvent](../harmonyos-references/arkts-apis-avsession-avsession.md#onhandlekeyevent10)指令。该回调接口会直接转发媒体按键事件[KeyEvent](../harmonyos-references/js-apis-keyevent.md)。应用需要自行识别按键事件的类型，并响应事件实现对应的功能。目前支持转发的按键事件类型如下：

  | 按键类型([KeyCode](../harmonyos-references/js-apis-keycode.md#keycode)) | 功能说明 |
  | --- | --- |
  | KEYCODE\_MEDIA\_PLAY\_PAUSE | 多媒体键：播放/暂停 |
  | KEYCODE\_MEDIA\_STOP | 多媒体键：停止 |
  | KEYCODE\_MEDIA\_NEXT | 多媒体键：下一首 |
  | KEYCODE\_MEDIA\_PREVIOUS | 多媒体键：上一首 |
  | KEYCODE\_MEDIA\_REWIND | 多媒体键：快退 |
  | KEYCODE\_MEDIA\_FAST\_FORWARD | 多媒体键：快进 |
  | KEYCODE\_MEDIA\_PLAY | 多媒体键：播放 |
  | KEYCODE\_MEDIA\_PAUSE | 多媒体键：暂停 |

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
  17. let type: AVSessionManager.AVSessionType = 'audio';
  18. let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
  19. // ...
  20. // 设置必要的媒体信息，务必设置，否则接收不到按键事件。
  21. let metadata: AVSessionManager.AVMetadata = {
  22. assetId: '0', // 由应用指定，用于标识应用媒体库里的媒体。
  23. title: 'TITLE',
  24. mediaImage: 'IMAGE',
  25. artist: 'ARTIST'
  26. };
  27. session.setAVMetadata(metadata).then(() => {
  28. console.info(`SetAVMetadata successfully`);
  29. // ...
  30. }).catch((err: BusinessError) => {
  31. console.error(`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}`);
  32. // ...
  33. });
  34. session.on('handleKeyEvent', (event) => {
  35. // 解析keycode，应用需要根据keycode对播放器做相应逻辑处理。
  36. console.info(`on handleKeyEvent, keyCode=${event.key.code}`);
  37. // ...
  38. });
  39. // ...
  40. })
  41. }
  42. .width('100%')
  43. .height('100%')
  44. }
  45. }
  ```

说明

1. 方式一与方式二均需正确设置媒体信息AVMetadata并注册相应控制接口，否则会无法接收到控制指令与按键事件。
2. 方式一与方式二，选择其一接入即可，无须同时接入，系统推荐按照方式一接入。

## 示例代码

* [媒体会话-提供方](https://gitcode.com/HarmonyOS_Samples/media-provider)
