---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsession
title: Interface (AVSession)
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > ArkTS API > @ohos.multimedia.avsession (媒体会话管理) > Interface (AVSession)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:995ccf311eab873f7d4e8b23da0b06b102452600ac33bcb751088489a69debb8
---

调用[avSession.createAVSession](arkts-apis-avsession-f.md#avsessioncreateavsession10)后，返回会话的实例，可以获得会话ID，完成设置元数据，播放状态信息等操作。

说明

* 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 10开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { avSession } from '@kit.AVSessionKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sessionId10+ | string | 是 | 否 | AVSession对象唯一的会话标识。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| sessionType10+ | [AVSessionType](arkts-apis-avsession-t.md#avsessiontype10) | 是 | 否 | AVSession会话类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| sessionTag22+ | string | 是 | 否 | AVSession会话的自定义标签信息。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |

**示例：**

```
1. let sessionId: string = currentAVSession.sessionId;
2. let sessionType: avSession.AVSessionType = currentAVSession.sessionType;
```

## setAVMetadata10+

PhonePC/2in1TabletTVWearable

setAVMetadata(data: AVMetadata): Promise<void>

设置会话元数据。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [AVMetadata](arkts-apis-avsession-i.md#avmetadata10) | 是 | 会话元数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当元数据设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. let metadata: avSession.AVMetadata = {
2. assetId: "121278",
3. title: "lose yourself",
4. artist: "Eminem",
5. author: "ST",
6. album: "Slim shady",
7. writer: "ST",
8. composer: "ST",
9. duration: 2222,
10. mediaImage: "https://www.example.com/example.jpg",
11. subtitle: "8 Mile",
12. description: "Rap",
13. // LRC中有两类元素：一种是时间标签+歌词，一种是ID标签。
14. // 例如：[00:25.44]xxx\r\n[00:26.44]xxx\r\n
15. lyric: "lrc格式歌词内容",
16. // singleLyricText字段存储单条歌词文本，不包含时间戳。
17. // 例如："单条歌词内容"。
18. singleLyricText: "单条歌词内容",
19. previousAssetId: "121277",
20. nextAssetId: "121279"
21. };
22. currentAVSession.setAVMetadata(metadata).then(() => {
23. console.info('Succeeded in setting AVMetadata.');
24. });
```

## setAVMetadata10+

PhonePC/2in1TabletTVWearable

setAVMetadata(data: AVMetadata, callback: AsyncCallback<void>): void

设置会话元数据。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [AVMetadata](arkts-apis-avsession-i.md#avmetadata10) | 是 | 会话元数据。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当元数据设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. let metadata: avSession.AVMetadata = {
2. assetId: "121278",
3. title: "lose yourself",
4. artist: "Eminem",
5. author: "ST",
6. album: "Slim shady",
7. writer: "ST",
8. composer: "ST",
9. duration: 2222,
10. mediaImage: "https://www.example.com/example.jpg",
11. subtitle: "8 Mile",
12. description: "Rap",
13. // LRC中有两类元素：一种是时间标签+歌词，一种是ID标签。
14. // 例如：[00:25.44]xxx\r\n[00:26.44]xxx\r\n
15. lyric: "lrc格式歌词内容",
16. // singleLyricText字段存储单条歌词文本，不包含时间戳。
17. // 例如："单条歌词内容"。
18. singleLyricText: "单条歌词内容",
19. previousAssetId: "121277",
20. nextAssetId: "121279"
21. };
22. currentAVSession.setAVMetadata(metadata, () => {
23. console.info('Succeeded in setting AVMetadata.');
24. });
```

## setCallMetadata11+

PhonePC/2in1TabletTVWearable

setCallMetadata(data: CallMetadata): Promise<void>

设置通话会话元数据。结果通过Promise异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [CallMetadata](arkts-apis-avsession-i.md#callmetadata11) | 是 | 通话会话元数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当通话元数据设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { resourceManager } from '@kit.LocalizationKit';

4. import { avSession } from '@kit.AVSessionKit';

6. @Entry
7. @Component
8. struct Index {
9. build() {
10. Column() {
11. Text('Hello World')
12. .fontSize(50)
13. .fontWeight(FontWeight.Bold)
14. }
15. .width('100%')
16. .height('100%')
17. }
18. }

20. class CallManager {
21. private currentAVSession: avSession.AVSession | null = null;

23. async setCallMetadata() {
24. try {
25. let value = await resourceManager.getSysResourceManager().getRawFileContent('IMAGE_URI');
26. let imageSource = await image.createImageSource(value.buffer);
27. let imagePixel = await imageSource.createPixelMap({ desiredSize: { width: 150, height: 150 } });
28. let calldata: avSession.CallMetadata = {
29. name: "xiaoming",
30. phoneNumber: "111xxxxxxxx",
31. avatar: imagePixel
32. };
33. await this.currentAVSession?.setCallMetadata(calldata);
34. console.info('Succeeded in setting call metadata.');
35. }
36. }
37. }
```

## setCallMetadata11+

PhonePC/2in1TabletTVWearable

setCallMetadata(data: CallMetadata, callback: AsyncCallback<void>): void

设置通话会话元数据。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [CallMetadata](arkts-apis-avsession-i.md#callmetadata11) | 是 | 通话会话元数据。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当通话元数据设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { resourceManager } from '@kit.LocalizationKit';

4. import { avSession } from '@kit.AVSessionKit';

6. @Entry
7. @Component
8. struct Index {
9. build() {
10. Column() {
11. Text('Hello World')
12. .fontSize(50)
13. .fontWeight(FontWeight.Bold)
14. }
15. .width('100%')
16. .height('100%')
17. }
18. }

20. class CallManager {
21. private currentAVSession: avSession.AVSession | null = null;

23. async setCallMetadata() {
24. try {
25. let value = await resourceManager.getSysResourceManager().getRawFileContent('IMAGE_URI');
26. let imageSource = await image.createImageSource(value.buffer);
27. let imagePixel = await imageSource.createPixelMap({ desiredSize: { width: 150, height: 150 } });
28. let calldata: avSession.CallMetadata = {
29. name: "xiaoming",
30. phoneNumber: "111xxxxxxxx",
31. avatar: imagePixel
32. };
33. this.currentAVSession?.setCallMetadata(calldata, () => {
34. console.info('Succeeded in setting call metadata.');
35. });
36. }
37. }
38. }
```

## setAVCallState11+

PhonePC/2in1TabletTVWearable

setAVCallState(state: AVCallState): Promise<void>

设置通话状态。结果通过Promise异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [AVCallState](arkts-apis-avsession-i.md#avcallstate11) | 是 | 通话状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当通话元数据设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. let calldata: avSession.AVCallState = {
2. state: avSession.CallState.CALL_STATE_ACTIVE,
3. muted: false
4. };
5. currentAVSession.setAVCallState(calldata).then(() => {
6. console.info('Succeeded in setting AVCallState.');
7. });
```

## setAVCallState11+

PhonePC/2in1TabletTVWearable

setAVCallState(state: AVCallState, callback: AsyncCallback<void>): void

设置通话状态。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [AVCallState](arkts-apis-avsession-i.md#avcallstate11) | 是 | 通话状态。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当通话元数据设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. let avcalldata: avSession.AVCallState = {
2. state: avSession.CallState.CALL_STATE_ACTIVE,
3. muted: false
4. };
5. currentAVSession.setAVCallState(avcalldata, () => {
6. console.info('Succeeded in setting AVCallState.');
7. });
```

## setAVPlaybackState10+

PhonePC/2in1TabletTVWearable

setAVPlaybackState(state: AVPlaybackState): Promise<void>

设置会话播放状态。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [AVPlaybackState](arkts-apis-avsession-i.md#avplaybackstate10) | 是 | 会话播放状态，包括状态、倍数、循环模式等信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当播放状态设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. let playbackState: avSession.AVPlaybackState = {
2. state:avSession.PlaybackState.PLAYBACK_STATE_PLAY,
3. speed: 1.0,
4. position:{elapsedTime:10, updateTime:(new Date()).getTime()},
5. bufferedTime:1000,
6. loopMode:avSession.LoopMode.LOOP_MODE_SINGLE,
7. isFavorite:true
8. };
9. currentAVSession.setAVPlaybackState(playbackState).then(() => {
10. console.info('Succeeded in setting AVPlaybackState.');
11. });
```

## setAVPlaybackState10+

PhonePC/2in1TabletTVWearable

setAVPlaybackState(state: AVPlaybackState, callback: AsyncCallback<void>): void

设置会话播放状态。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [AVPlaybackState](arkts-apis-avsession-i.md#avplaybackstate10) | 是 | 会话播放状态，包括状态、倍数、循环模式等信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当播放状态设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. let PlaybackState: avSession.AVPlaybackState = {
2. state:avSession.PlaybackState.PLAYBACK_STATE_PLAY,
3. speed: 1.0,
4. position:{elapsedTime:10, updateTime:(new Date()).getTime()},
5. bufferedTime:1000,
6. loopMode:avSession.LoopMode.LOOP_MODE_SINGLE,
7. isFavorite:true
8. };
9. currentAVSession.setAVPlaybackState(PlaybackState, () => {
10. console.info('Succeeded in setting AVPlaybackState.');
11. });
```

## setLaunchAbility10+

PhonePC/2in1TabletTVWearable

setLaunchAbility(ability: WantAgent): Promise<void>

设置一个WantAgent用于拉起会话的Ability。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [WantAgent](js-apis-app-ability-wantagent.md) | 是 | 应用的相关属性信息，如bundleName，abilityName，deviceId等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当Ability设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { wantAgent } from '@kit.AbilityKit';

4. // WantAgentInfo对象。
5. let wantAgentInfo: wantAgent.WantAgentInfo = {
6. wants: [
7. {
8. deviceId: "deviceId",
9. bundleName: "com.example.myapplication",
10. abilityName: "EntryAbility",
11. action: "action1",
12. entities: ["entity1"],
13. type: "MIMETYPE",
14. uri: "key = {true,true,false}",
15. parameters:
16. {
17. mykey0: 2222,
18. mykey1: [1, 2, 3],
19. mykey2: "[1, 2, 3]",
20. mykey3: "ssssssssssssssssssssssssss",
21. mykey4: [false, true, false],
22. mykey5: ["qqqqq", "wwwwww", "aaaaaaaaaaaaaaaaa"],
23. mykey6: true
24. }
25. }
26. ],
27. operationType: wantAgent.OperationType.START_ABILITIES,
28. requestCode: 0,
29. wantAgentFlags:[wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
30. }

32. wantAgent.getWantAgent(wantAgentInfo).then((agent) => {
33. currentAVSession.setLaunchAbility(agent).then(() => {
34. console.info('Succeeded in setting launch ability.');
35. });
36. });
```

## setLaunchAbility10+

PhonePC/2in1TabletTVWearable

setLaunchAbility(ability: WantAgent, callback: AsyncCallback<void>): void

设置一个WantAgent用于拉起会话的Ability。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [WantAgent](js-apis-app-ability-wantagent.md) | 是 | 应用的相关属性信息，如bundleName，abilityName，deviceId等。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当Ability设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { wantAgent } from '@kit.AbilityKit';

4. // WantAgentInfo对象。
5. let wantAgentInfo: wantAgent.WantAgentInfo = {
6. wants: [
7. {
8. deviceId: "deviceId",
9. bundleName: "com.example.myapplication",
10. abilityName: "EntryAbility",
11. action: "action1",
12. entities: ["entity1"],
13. type: "MIMETYPE",
14. uri: "key = {true,true,false}",
15. parameters:
16. {
17. mykey0: 2222,
18. mykey1: [1, 2, 3],
19. mykey2: "[1, 2, 3]",
20. mykey3: "ssssssssssssssssssssssssss",
21. mykey4: [false, true, false],
22. mykey5: ["qqqqq", "wwwwww", "aaaaaaaaaaaaaaaaa"],
23. mykey6: true
24. }
25. }
26. ],
27. operationType: wantAgent.OperationType.START_ABILITIES,
28. requestCode: 0,
29. wantAgentFlags:[wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
30. }

32. wantAgent.getWantAgent(wantAgentInfo).then((agent) => {
33. currentAVSession.setLaunchAbility(agent, () => {
34. console.info('Succeeded in setting launch ability.');
35. });
36. });
```

## dispatchSessionEvent10+

PhonePC/2in1TabletTVWearable

dispatchSessionEvent(event: string, args: {[key: string]: Object}): Promise<void>

媒体提供方设置一个会话内自定义事件，包括事件名和键值对形式的事件内容。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 需要设置的会话事件的名称。 |
| args | {[key: string]: Object} | 是 | 需要传递的会话事件内容。 |

说明

参数args支持的数据类型有：字符串、数字、布尔值、对象、数组和文件描述符等，详细介绍请参见[@ohos.app.ability.Want(Want)](js-apis-app-ability-want.md)。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当事件设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { avSession } from '@kit.AVSessionKit';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'hello world';

8. build() {
9. Column() {
10. Text(this.message)
11. .onClick(()=>{
12. let currentAVSession: avSession.AVSession | undefined = undefined;
13. let tag = "createNewSession";
14. let context: Context = this.getUIContext().getHostContext() as Context;

16. avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
17. currentAVSession = data;
18. let eventName = "dynamic_lyric";
19. if (currentAVSession !== undefined) {
20. (currentAVSession as avSession.AVSession).dispatchSessionEvent(eventName, {lyric : "This is lyric"}).then(() => {
21. console.info('Succeeded in dispatching session event.');
22. })
23. }
24. });
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

## dispatchSessionEvent10+

PhonePC/2in1TabletTVWearable

dispatchSessionEvent(event: string, args: {[key: string]: Object}, callback: AsyncCallback<void>): void

媒体提供方设置一个会话内自定义事件，包括事件名和键值对形式的事件内容。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 需要设置的会话事件的名称。 |
| args | {[key: string]: Object} | 是 | 需要传递的会话事件内容。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当会话事件设置成功，err为undefined，否则返回错误对象。 |

说明

参数args支持的数据类型有：字符串、数字、布尔值、对象、数组和文件描述符等，详细介绍请参见[@ohos.app.ability.Want(Want)](js-apis-app-ability-want.md)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { avSession } from '@kit.AVSessionKit';
2. @Entry
3. @Component
4. struct Index {
5. @State message: string = 'hello world';

7. build() {
8. Column() {
9. Text(this.message)
10. .onClick(()=>{
11. let currentAVSession: avSession.AVSession | undefined = undefined;
12. let tag = "createNewSession";
13. let context: Context = this.getUIContext().getHostContext() as Context;

15. avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
16. currentAVSession = data;
17. let eventName: string = "dynamic_lyric";
18. if (currentAVSession !== undefined) {
19. (currentAVSession as avSession.AVSession).dispatchSessionEvent(eventName, {lyric : "This is lyric"}, () => {
20. console.info('Succeeded in dispatching session event.');
21. })
22. }
23. });
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

## setAVQueueItems10+

PhonePC/2in1TabletTVWearable

setAVQueueItems(items: Array<AVQueueItem>): Promise<void>

设置媒体播放列表。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | Array<[AVQueueItem](arkts-apis-avsession-i.md#avqueueitem10)> | 是 | 播放列表单项的队列，用以表示播放列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当播放列表设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { resourceManager } from '@kit.LocalizationKit';

4. import { avSession } from '@kit.AVSessionKit';
5. interface ExtrasType {
6. extras: string;
7. }

9. @Entry
10. @Component
11. struct Index {
12. build() {
13. Column() {
14. }
15. }
16. }

18. let currentAVSession: avSession.AVSession;

20. async function setAVQueueItems() {
21. try {
22. let value = await resourceManager.getSysResourceManager().getRawFileContent('IMAGE_URI');
23. let imageSource = await image.createImageSource(value.buffer);
24. let imagePixel = await imageSource.createPixelMap({desiredSize:{width: 150, height: 150}});
25. let queueItemDescription_1: avSession.AVMediaDescription = {
26. assetId: '001',
27. title: 'music_name',
28. subtitle: 'music_sub_name',
29. description: 'music_description',
30. mediaImage : imagePixel,
31. extras: {extras:'any'}
32. };
33. let queueItem_1: avSession.AVQueueItem = {
34. itemId: 1,
35. description: queueItemDescription_1
36. } as avSession.AVQueueItem;
37. let queueItemDescription_2: avSession.AVMediaDescription = {
38. assetId: '002',
39. title: 'music_name',
40. subtitle: 'music_sub_name',
41. description: 'music_description',
42. mediaImage: imagePixel,
43. extras: {extras:'any'}
44. };
45. let queueItem_2: avSession.AVQueueItem = {
46. itemId: 2,
47. description: queueItemDescription_2
48. } as avSession.AVQueueItem;
49. let queueItemsArray: avSession.AVQueueItem[] = [queueItem_1, queueItem_2];
50. currentAVSession.setAVQueueItems(queueItemsArray).then(() => {
51. console.info('Succeeded in setting AVQueueItems.');
52. });
53. }
54. }
```

## setAVQueueItems10+

PhonePC/2in1TabletTVWearable

setAVQueueItems(items: Array<AVQueueItem>, callback: AsyncCallback<void>): void

设置媒体播放列表。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | Array<[AVQueueItem](arkts-apis-avsession-i.md#avqueueitem10)> | 是 | 播放列表单项的队列，用以表示播放列表。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当播放状态设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { image } from '@kit.ImageKit';
2. import { resourceManager } from '@kit.LocalizationKit';

4. import { avSession } from '@kit.AVSessionKit'

6. interface ExtrasType {
7. extras: string;
8. }

10. @Entry
11. @Component
12. struct Index {
13. build() {
14. Column() {
15. }
16. }
17. }

19. let currentAVSession: avSession.AVSession;

21. async function setAVQueueItems() {
22. try {
23. let value = await resourceManager.getSysResourceManager().getRawFileContent('IMAGE_URI');
24. let imageSource = await image.createImageSource(value.buffer);
25. let imagePixel = await imageSource.createPixelMap({ desiredSize: { width: 150, height: 150 } });
26. let queueItemDescription_1: avSession.AVMediaDescription = {
27. assetId: '001',
28. title: 'music_name',
29. subtitle: 'music_sub_name',
30. description: 'music_description',
31. mediaImage: imagePixel,
32. extras: { extras: 'any' }
33. };
34. let queueItem_1: avSession.AVQueueItem = {
35. itemId: 1,
36. description: queueItemDescription_1
37. };
38. let queueItemDescription_2: avSession.AVMediaDescription = {
39. assetId: '002',
40. title: 'music_name',
41. subtitle: 'music_sub_name',
42. description: 'music_description',
43. mediaImage: imagePixel,
44. extras: { extras: 'any' }
45. };
46. let queueItem_2: avSession.AVQueueItem = {
47. itemId: 2,
48. description: queueItemDescription_2
49. };
50. let queueItemsArray: avSession.AVQueueItem[] = [queueItem_1, queueItem_2];
51. currentAVSession.setAVQueueItems(queueItemsArray, () => {
52. console.info('Succeeded in setting AVQueueItems.');
53. });
54. }
55. }
```

## setAVQueueTitle10+

PhonePC/2in1TabletTVWearable

setAVQueueTitle(title: string): Promise<void>

设置媒体播放列表名称。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 是 | 播放列表的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当播放列表设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. let queueTitle = 'QUEUE_TITLE';
2. currentAVSession.setAVQueueTitle(queueTitle).then(() => {
3. console.info('Succeeded in setting AVQueueTitle.');
4. });
```

## setAVQueueTitle10+

PhonePC/2in1TabletTVWearable

setAVQueueTitle(title: string, callback: AsyncCallback<void>): void

设置媒体播放列表名称。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 是 | 播放列表名称字段。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当播放状态设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. let queueTitle = 'QUEUE_TITLE';
2. currentAVSession.setAVQueueTitle(queueTitle, () => {
3. console.info('Succeeded in setting AVQueueTitle.');
4. });
```

## setExtras10+

PhonePC/2in1TabletTVWearable

setExtras(extras: {[key: string]: Object}): Promise<void>

媒体提供方设置键值对形式的自定义媒体数据包。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| extras | {[key: string]: Object} | 是 | 需要传递的自定义媒体数据包键值对。  **说明：** 参数extras支持的数据类型有：字符串、数字、布尔值、对象、数组和文件描述符等，详细介绍请参见[@ohos.app.ability.Want(Want)](js-apis-app-ability-want.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified.2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { avSession } from '@kit.AVSessionKit';
2. @Entry
3. @Component
4. struct Index {
5. @State message: string = 'hello world';

7. build() {
8. Column() {
9. Text(this.message)
10. .onClick(() => {
11. let currentAVSession: avSession.AVSession | undefined = undefined;
12. let tag = "createNewSession";
13. let context: Context = this.getUIContext().getHostContext() as Context;

15. avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
16. currentAVSession = data;
17. if (currentAVSession !== undefined) {
18. (currentAVSession as avSession.AVSession).setExtras({extras : "This is custom media packet"}).then(() => {
19. console.info('Succeeded in setting extras.');
20. })
21. }
22. });
23. })
24. }
25. .width('100%')
26. .height('100%')
27. }
28. }
```

## setExtras10+

PhonePC/2in1TabletTVWearable

setExtras(extras:{[key: string]: Object}, callback: AsyncCallback<void>): void

媒体提供方设置键值对形式的自定义媒体数据包，使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| extras | {[key: string]: Object} | 是 | 需要传递的自定义媒体数据包键值对。  **说明：** 参数extras支持的数据类型有：字符串、数字、布尔值、对象、数组和文件描述符等，详细介绍请参见[@ohos.app.ability.Want(Want)](js-apis-app-ability-want.md)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当自定义媒体数据包设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { avSession } from '@kit.AVSessionKit';
2. @Entry
3. @Component
4. struct Index {
5. @State message: string = 'hello world';

7. build() {
8. Column() {
9. Text(this.message)
10. .onClick(()=>{
11. let currentAVSession: avSession.AVSession | undefined = undefined;
12. let tag = "createNewSession";
13. let context: Context = this.getUIContext().getHostContext() as Context;

15. avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
16. currentAVSession = data;
17. if (currentAVSession !== undefined) {
18. (currentAVSession as avSession.AVSession).setExtras({extras : "This is custom media packet"}, () => {
19. console.info('Succeeded in setting extras.');
20. })
21. }
22. });
23. })
24. }
25. .width('100%')
26. .height('100%')
27. }
28. }
```

## sendCustomData20+

PhonePC/2in1TabletTV

sendCustomData(data: Record<string, Object>): Promise<void>

发送私有数据到远端设备。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Record<string, Object> | 是 | 应用程序填充的自定义数据。服务端仅解析key为'customData'，且Object为string类型的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception.You are advised to:1.Scheduled retry.2.Destroy the current session or session controller and re-create it. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { avSession } from '@kit.AVSessionKit';
2. @Entry
3. @Component
4. struct Index {
5. @State message: string = 'hello world';

7. build() {
8. Column() {
9. Text(this.message)
10. .onClick(()=>{
11. let currentAVSession: avSession.AVSession | undefined = undefined;
12. let tag = "createNewSession";
13. let context: Context = this.getUIContext().getHostContext() as Context;

15. avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
16. currentAVSession = data;
17. });
18. if (currentAVSession !== undefined) {
19. (currentAVSession as avSession.AVSession).sendCustomData({customData : "This is custom data"}).then(() => {
20. console.info('Succeeded in sending custom data.');
21. })
22. }
23. })
24. }
25. .width('100%')
26. .height('100%')
27. }
28. }
```

## enableDesktopLyric23+

PhonePC/2in1TabletTVWearable

enableDesktopLyric(enable: boolean): Promise<void>

当前会话是否启用桌面歌词功能。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否启用桌面歌词。true表示启用，false表示不启用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600111 | The desktop lyrics feature is not supported. |

**示例：**

```
1. import { avSession } from '@kit.AVSessionKit';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'hello world';

8. build() {
9. Column() {
10. Text(this.message)
11. .onClick(() => {
12. let currentAVSession: avSession.AVSession | undefined = undefined;
13. let tag = "createNewSession";
14. let context: Context = this.getUIContext().getHostContext() as Context;

16. avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
17. currentAVSession = data;
18. });
19. if (currentAVSession !== undefined) {
20. (currentAVSession as avSession.AVSession).enableDesktopLyric(true).then(() => {
21. console.info('Succeeded in enabling desktop lyric.');
22. })
23. }
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

## setDesktopLyricVisible23+

PhonePC/2in1TabletTVWearable

setDesktopLyricVisible(visible: boolean): Promise<void>

设置当前会话桌面歌词的显示状态。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visible | boolean | 是 | 是否显示桌面歌词。true表示显示；false表示不显示。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600110 | The desktop lyrics feature of this application is not enabled. |
| 6600111 | The desktop lyrics feature is not supported. |

**示例：**

```
1. import { avSession } from '@kit.AVSessionKit';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'hello world';

8. build() {
9. Column() {
10. Text(this.message)
11. .onClick(() => {
12. let currentAVSession: avSession.AVSession | undefined = undefined;
13. let tag = "createNewSession";
14. let context: Context = this.getUIContext().getHostContext() as Context;

16. avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
17. currentAVSession = data;
18. });
19. if (currentAVSession !== undefined) {
20. (currentAVSession as avSession.AVSession).setDesktopLyricVisible(true).then(() => {
21. console.info('Succeeded in setting desktop lyric visible.');
22. })
23. }
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

## isDesktopLyricVisible23+

PhonePC/2in1TabletTVWearable

isDesktopLyricVisible(): Promise<boolean>

查询当前会话桌面歌词的显示状态。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示显示桌面歌词；返回false表示不显示桌面歌词。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600110 | The desktop lyrics feature of this application is not enabled. |
| 6600111 | The desktop lyrics feature is not supported. |

**示例：**

```
1. import { avSession } from '@kit.AVSessionKit';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'hello world';

8. build() {
9. Column() {
10. Text(this.message)
11. .onClick(() => {
12. let currentAVSession: avSession.AVSession | undefined = undefined;
13. let tag = "createNewSession";
14. let context: Context = this.getUIContext().getHostContext() as Context;
15. avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
16. currentAVSession = data;
17. });
18. if (currentAVSession !== undefined) {
19. (currentAVSession as avSession.AVSession).isDesktopLyricVisible().then((visible: boolean) => {
20. console.info(`isDesktopLyricVisible: ${visible}`);
21. })
22. }
23. })
24. }
25. .width('100%')
26. .height('100%')
27. }
28. }
```

## onDesktopLyricVisibilityChanged23+

PhonePC/2in1TabletTVWearable

onDesktopLyricVisibilityChanged(callback: Callback<boolean>): void

显示桌面歌词状态变更的监听事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 是 | 回调函数。返回true表示开启显示桌面歌词状态；返回false表示关闭显示桌面歌词状态。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { avSession } from '@kit.AVSessionKit';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'hello world';

8. build() {
9. Column() {
10. Text(this.message)
11. .onClick(() => {
12. let currentAVSession: avSession.AVSession | undefined = undefined;
13. let tag = "createNewSession";
14. let context: Context = this.getUIContext().getHostContext() as Context;
15. avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
16. currentAVSession = data;
17. });
18. if (currentAVSession !== undefined) {
19. (currentAVSession as avSession.AVSession).onDesktopLyricVisibilityChanged((visible: boolean) => {
20. console.info(`desktop lyric visible state: ${visible}`);
21. });
22. }
23. })
24. }
25. .width('100%')
26. .height('100%')
27. }
28. }
```

## offDesktopLyricVisibilityChanged23+

PhonePC/2in1TabletTVWearable

offDesktopLyricVisibilityChanged(callback?: Callback<boolean>): void

取消显示桌面歌词状态变更事件监听，取消后将不再对该事件进行监听。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有显示桌面歌词状态变更事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { avSession } from '@kit.AVSessionKit';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'hello world';

8. build() {
9. Column() {
10. Text(this.message)
11. .onClick(() => {
12. let currentAVSession: avSession.AVSession | undefined = undefined;
13. let tag = "createNewSession";
14. let context: Context = this.getUIContext().getHostContext() as Context;
15. avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
16. currentAVSession = data;
17. });
18. if (currentAVSession !== undefined) {
19. (currentAVSession as avSession.AVSession).offDesktopLyricVisibilityChanged();
20. }
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

## setDesktopLyricState23+

PhonePC/2in1TabletTVWearable

setDesktopLyricState(state: DesktopLyricState): Promise<void>

设置当前会话桌面歌词状态。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [DesktopLyricState](arkts-apis-avsession-i.md#desktoplyricstate23) | 是 | 桌面歌词状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600110 | The desktop lyrics feature of this application is not enabled. |
| 6600111 | The desktop lyrics feature is not supported. |

**示例：**

```
1. import { avSession } from '@kit.AVSessionKit';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'hello world';

8. build() {
9. Column() {
10. Text(this.message)
11. .onClick(() => {
12. let currentAVSession: avSession.AVSession | undefined = undefined;
13. let tag = "createNewSession";
14. let context: Context = this.getUIContext().getHostContext() as Context;

16. avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
17. currentAVSession = data;
18. });
19. if (currentAVSession !== undefined) {
20. let state: avSession.DesktopLyricState = {
21. isLocked: true,
22. };
23. (currentAVSession as avSession.AVSession).setDesktopLyricState(state).then(() => {
24. console.info('Succeeded in setting desktop lyric state.');
25. })
26. }
27. })
28. }
29. .width('100%')
30. .height('100%')
31. }
32. }
```

## getDesktopLyricState23+

PhonePC/2in1TabletTVWearable

getDesktopLyricState(): Promise<DesktopLyricState>

获取当前会话桌面歌词状态。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DesktopLyricState](arkts-apis-avsession-i.md#desktoplyricstate23)> | Promise对象。返回桌面歌词状态。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600110 | The desktop lyrics feature of this application is not enabled. |
| 6600111 | The desktop lyrics feature is not supported. |

**示例：**

```
1. import { avSession } from '@kit.AVSessionKit';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'hello world';

8. build() {
9. Column() {
10. Text(this.message)
11. .onClick(() => {
12. let currentAVSession: avSession.AVSession | undefined = undefined;
13. let tag = "createNewSession";
14. let context: Context = this.getUIContext().getHostContext() as Context;

16. avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
17. currentAVSession = data;
18. });
19. if (currentAVSession !== undefined) {
20. (currentAVSession as avSession.AVSession).getDesktopLyricState()
21. .then((state: avSession.DesktopLyricState) => {
22. console.info(`getDesktopLyricState: ${state.isLocked}`);
23. })
24. }
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

## onDesktopLyricStateChanged23+

PhonePC/2in1TabletTVWearable

onDesktopLyricStateChanged(callback: Callback<DesktopLyricState>): void

桌面歌词状态变更的监听事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[DesktopLyricState](arkts-apis-avsession-i.md#desktoplyricstate23)> | 是 | 回调函数。返回桌面歌词状态。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { avSession } from '@kit.AVSessionKit';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'hello world';

8. build() {
9. Column() {
10. Text(this.message)
11. .onClick(() => {
12. let currentAVSession: avSession.AVSession | undefined = undefined;
13. let tag = "createNewSession";
14. let context: Context = this.getUIContext().getHostContext() as Context;

16. avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
17. currentAVSession = data;
18. });
19. if (currentAVSession !== undefined) {
20. (currentAVSession as avSession.AVSession).onDesktopLyricStateChanged((state: avSession.DesktopLyricState) => {
21. console.info(`desktop lyric isLocked : ${state.isLocked}`);
22. })
23. }
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

## offDesktopLyricStateChanged23+

PhonePC/2in1TabletTVWearable

offDesktopLyricStateChanged(callback?: Callback<DesktopLyricState>): void

取消桌面歌词状态变更事件监听，取消后将不再对该事件进行监听。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[DesktopLyricState](arkts-apis-avsession-i.md#desktoplyricstate23)> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有桌面歌词状态变更事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { avSession } from '@kit.AVSessionKit';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'hello world';

8. build() {
9. Column() {
10. Text(this.message)
11. .onClick(() => {
12. let currentAVSession: avSession.AVSession | undefined = undefined;
13. let tag = "createNewSession";
14. let context: Context = this.getUIContext().getHostContext() as Context;
15. avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
16. currentAVSession = data;
17. });
18. if (currentAVSession !== undefined) {
19. (currentAVSession as avSession.AVSession).offDesktopLyricStateChanged();
20. }
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

## getController10+

PhonePC/2in1TabletTVWearable

getController(): Promise<AVSessionController>

获取本会话对应的控制器。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AVSessionController](arkts-apis-avsession-avsessioncontroller.md)> | Promise对象。返回会话控制器。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { avSession } from '@kit.AVSessionKit';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'hello world';
7. build() {
8. Column() {
9. Text(this.message)
10. .onClick(async ()=>{
11. let context: Context = this.getUIContext().getHostContext() as Context;
12. let currentAVSession: avSession.AVSession = await avSession.createAVSession(context, 'SESSION_NAME', 'audio');
13. let avSessionController: avSession.AVSessionController;
14. currentAVSession.getController().then((avController: avSession.AVSessionController) => {
15. avSessionController = avController;
16. console.info(`Succeeded in getting controller, sessionid: ${avSessionController.sessionId}`);
17. });
18. })
19. }
20. .width('100%')
21. .height('100%')
22. }
23. }
```

## getController10+

PhonePC/2in1TabletTVWearable

getController(callback: AsyncCallback<AVSessionController>): void

获取本会话相应的控制器。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AVSessionController](arkts-apis-avsession-avsessioncontroller.md)> | 是 | 回调函数。返回会话控制器。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { avSession } from '@kit.AVSessionKit';

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'hello world';

9. build() {
10. Column() {
11. Text(this.message)
12. .onClick(async () => {
13. let context: Context = this.getUIContext().getHostContext() as Context;
14. let currentAVSession: avSession.AVSession = await avSession.createAVSession(context, 'SESSION_NAME', 'audio');
15. let avsessionController: avSession.AVSessionController;
16. currentAVSession.getController((avcontroller: avSession.AVSessionController) => {
17. avsessionController = avcontroller;
18. console.info(`Succeeded in getting controller, sessionid: ${avsessionController.sessionId}`);
19. });
20. })
21. }
22. .width('100%')
23. .height('100%')
24. }
25. }
```

## getAVCastController10+

PhonePC/2in1TabletTV

getAVCastController(): Promise<AVCastController>

设备建立连接后，获取投播控制器。结果通过Promise异步回调方式返回。如果 avsession 未处于投播状态，则控制器将返回 null。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AVCastController](arkts-apis-avsession-avcastcontroller.md)> | Promise对象。返回投播控制器实例。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600102 | The session does not exist. |
| 6600109 | The remote connection is not established. |

**示例：**

```
1. let avCastController: avSession.AVCastController;
2. currentAVSession.getAVCastController().then((avcontroller: avSession.AVCastController) => {
3. avCastController = avcontroller;
4. console.info('Succeeded in getting AV cast controller.');
5. });
```

## getAVCastController10+

PhonePC/2in1TabletTV

getAVCastController(callback: AsyncCallback<AVCastController>): void

设备建立连接后，获取投播控制器。结果通过callback异步回调方式返回。如果 avsession 未处于投播状态，则控制器将返回 null。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AVCastController](arkts-apis-avsession-avcastcontroller.md)> | 是 | 回调函数，返回投播控制器实例。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600102 | The session does not exist. |
| 6600109 | The remote connection is not established. |

**示例：**

```
1. let avCastController: avSession.AVCastController;
2. currentAVSession.getAVCastController((avcontroller: avSession.AVCastController) => {
3. avCastController = avcontroller;
4. console.info('Succeeded in getting AV cast controller.');
5. });
```

## getOutputDevice10+

PhonePC/2in1TabletTVWearable

getOutputDevice(): Promise<OutputDeviceInfo>

通过会话获取播放设备信息。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[OutputDeviceInfo](arkts-apis-avsession-i.md#outputdeviceinfo10)> | Promise对象。返回播放设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.getOutputDevice().then((outputDeviceInfo: avSession.OutputDeviceInfo) => {
2. console.info(`Succeeded in getting output device, devices length: ${outputDeviceInfo.devices.length}`);
3. })
```

## getOutputDevice10+

PhonePC/2in1TabletTVWearable

getOutputDevice(callback: AsyncCallback<OutputDeviceInfo>): void

通过会话获取播放设备相关信息。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[OutputDeviceInfo](arkts-apis-avsession-i.md#outputdeviceinfo10)> | 是 | 回调函数，返回播放设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.getOutputDevice((outputDeviceInfo: avSession.OutputDeviceInfo) => {
2. console.info(`Succeeded in getting output device, devices length: ${outputDeviceInfo.devices.length}`);
3. });
```

## activate10+

PhonePC/2in1TabletTVWearable

activate(): Promise<void>

激活会话，激活后可正常使用会话。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当会话激活成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.activate().then(() => {
2. console.info('Succeeded in activating.');
3. });
```

## activate10+

PhonePC/2in1TabletTVWearable

activate(callback: AsyncCallback<void>): void

激活会话，激活后可正常使用会话。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当会话激活成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.activate(() => {
2. console.info('Succeeded in activating.');
3. });
```

## deactivate10+

PhonePC/2in1TabletTVWearable

deactivate(): Promise<void>

禁用当前会话的功能，可通过[activate](arkts-apis-avsession-avsession.md#activate10)恢复。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当禁用会话成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.deactivate().then(() => {
2. console.info('Succeeded in deactivating.');
3. });
```

## deactivate10+

PhonePC/2in1TabletTVWearable

deactivate(callback: AsyncCallback<void>): void

禁用当前会话。结果通过callback异步回调方式返回。

禁用当前会话的功能，可通过[activate](arkts-apis-avsession-avsession.md#activate10)恢复。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当禁用会话成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.deactivate(() => {
2. console.info('Succeeded in deactivating.');
3. });
```

## destroy10+

PhonePC/2in1TabletTVWearable

destroy(): Promise<void>

销毁当前会话，使当前会话完全失效。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当会话销毁成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.destroy().then(() => {
2. console.info('Succeeded in destroying.');
3. });
```

## destroy10+

PhonePC/2in1TabletTVWearable

destroy(callback: AsyncCallback<void>): void

销毁当前会话，使当前会话完全失效。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当会话销毁成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.destroy(() => {
2. console.info('Succeeded in destroying.');
3. });
```

## on('play')10+

PhonePC/2in1TabletTVWearable

on(type: 'play', callback: () => void): void

设置播放命令监听事件。注册该监听，说明应用支持播放指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'play'，当播放命令被发送到会话时，触发该事件回调。 |
| callback | () => void | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('play', () => {
2. console.info('on play entry');
3. });
```

## onPlay22+

PhonePC/2in1TabletTVWearable

onPlay(callback: Callback<CommandInfo>): void

设置播放命令监听事件。使用callback异步回调。

应用将通过回调接收控制器发送的[CommandInfo](arkts-apis-avsession-i.md#commandinfo22)信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[CommandInfo](arkts-apis-avsession-i.md#commandinfo22)> | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.onPlay((info: avSession.CommandInfo) => {
2. console.info('on play entry');
3. });
```

## on('pause')10+

PhonePC/2in1TabletTVWearable

on(type: 'pause', callback: () => void): void

设置暂停命令监听事件。注册该监听，说明应用支持暂停指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'pause'，当暂停命令被发送到会话时，触发该事件回调。 |
| callback | () => void | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('pause', () => {
2. console.info('on pause entry');
3. });
```

## on('stop')10+

PhonePC/2in1TabletTVWearable

on(type:'stop', callback: () => void): void

设置停止命令监听事件。注册该监听，说明应用支持停止指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件是'stop'，当停止命令被发送到会话时，触发该事件回调。 |
| callback | () => void | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('stop', () => {
2. console.info('on stop entry');
3. });
```

## on('playNext')10+

PhonePC/2in1TabletTVWearable

on(type:'playNext', callback: () => void): void

设置播放下一首命令监听事件。注册该监听，说明应用支持下一首指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件是'playNext'，当播放下一首命令被发送到会话时，触发该事件回调。 |
| callback | () => void | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('playNext', () => {
2. console.info('on playNext entry');
3. });
```

## onPlayNext22+

PhonePC/2in1TabletTVWearable

onPlayNext(callback: Callback<CommandInfo>): void

设置播放下一首命令监听事件。使用callback异步回调。

应用将通过回调接收控制器发送的[CommandInfo](arkts-apis-avsession-i.md#commandinfo22)信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[CommandInfo](arkts-apis-avsession-i.md#commandinfo22)> | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.onPlayNext((info: avSession.CommandInfo) => {
2. console.info('on playNext entry');
3. });
```

## on('playPrevious')10+

PhonePC/2in1TabletTVWearable

on(type:'playPrevious', callback: () => void): void

设置播放上一首命令监听事件。注册该监听，说明应用支持上一首指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件是'playPrevious'，当播放上一首命令被发送到会话时，触发该事件回调。 |
| callback | () => void | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('playPrevious', () => {
2. console.info('on playPrevious entry');
3. });
```

## onPlayPrevious22+

PhonePC/2in1TabletTVWearable

onPlayPrevious(callback: Callback<CommandInfo>): void

设置播放上一首命令监听事件。使用callback异步回调。

应用将通过回调接收控制器发送的[CommandInfo](arkts-apis-avsession-i.md#commandinfo22)信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[CommandInfo](arkts-apis-avsession-i.md#commandinfo22)> | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.onPlayPrevious((info: avSession.CommandInfo) => {
2. console.info('on playPrevious entry');
3. });
```

## on('fastForward')10+

PhonePC/2in1TabletTVWearable

on(type: 'fastForward', callback: (time?: number) => void): void

设置快进命令监听事件。注册该监听，说明应用支持快进指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件是 'fastForward'，当快进命令被发送到会话时，触发该事件回调。 |
| callback | (time?: number) => void | 是 | 回调函数。参数time是时间节点，单位为秒。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('fastForward', (time?: number) => {
2. console.info('on fastForward entry');
3. });
```

## onFastForward22+

PhonePC/2in1TabletTVWearable

onFastForward(callback: TwoParamCallback<number, CommandInfo>): void

设置快进命令监听事件。使用callback异步回调。

应用将通过回调接收控制器发送的快进时间参数，以及对应的[CommandInfo](arkts-apis-avsession-i.md#commandinfo22)信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | TwoParamCallback<number, [CommandInfo](arkts-apis-avsession-i.md#commandinfo22)> | 是 | 回调函数。用于处理'fastForward'操作。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.onFastForward((time: number, info: avSession.CommandInfo) => {
2. console.info('on fastForward entry');
3. });
```

## on('rewind')10+

PhonePC/2in1TabletTVWearable

on(type:'rewind', callback: (time?: number) => void): void

设置快退命令监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件是'rewind'，当快退命令被发送到会话时，触发该事件回调。 |
| callback | (time?: number) => void | 是 | 回调函数。参数time是时间节点，单位为秒。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('rewind', (time?: number) => {
2. console.info('on rewind entry');
3. });
```

## onRewind22+

PhonePC/2in1TabletTVWearable

onRewind(callback: TwoParamCallback<number, CommandInfo>): void

设置快退命令监听事件。使用callback异步回调。

应用将通过回调接收控制器发送的快退时间参数，以及对应的[CommandInfo](arkts-apis-avsession-i.md#commandinfo22)信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | TwoParamCallback<number, [CommandInfo](arkts-apis-avsession-i.md#commandinfo22)> | 是 | 回调函数。用于处理'rewind'操作。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.onRewind((time: number, info: avSession.CommandInfo) => {
2. console.info('on rewind entry');
3. });
```

## on('playWithAssetId')20+

PhonePC/2in1TabletTVWearable

on(type:'playWithAssetId', callback: Callback<string>): void

设置指定资源id进行播放的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件是'playWithAssetId'，当指定资源id进行播放时，触发该事件回调。 |
| callback | Callback<string> | 是 | 回调函数。参数assetId是媒体id。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. let playWithAssetIdCallback = (assetId: string) => {
2. console.info(`on playWithAssetId entry,  assetId = ${assetId}`);
3. }
4. currentAVSession.on('playWithAssetId', playWithAssetIdCallback);
```

## off('playWithAssetId')20+

PhonePC/2in1TabletTVWearable

off(type: 'playWithAssetId', callback?: Callback<string>): void

取消指定资源id进行播放的事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'playWithAssetId'。 |
| callback | Callback<string> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。参数assetId是媒体id。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('playWithAssetId');
```

## on('seek')10+

PhonePC/2in1TabletTVWearable

on(type: 'seek', callback: (time: number) => void): void

设置跳转节点监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'seek'：当跳转节点命令被发送到会话时，触发该事件。 |
| callback | (time: number) => void | 是 | 回调函数。参数time是时间节点，单位为毫秒。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('seek', (time: number) => {
2. console.info(`on seek entry time : ${time}`);
3. });
```

## on('setSpeed')10+

PhonePC/2in1TabletTVWearable

on(type: 'setSpeed', callback: (speed: number) => void): void

设置播放速率的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'setSpeed'：当设置播放速率的命令被发送到会话时，触发该事件。 |
| callback | (speed: number) => void | 是 | 回调函数。参数speed是播放倍速。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('setSpeed', (speed: number) => {
2. console.info(`on setSpeed speed : ${speed}`);
3. });
```

## on('setLoopMode')10+

PhonePC/2in1TabletTVWearable

on(type: 'setLoopMode', callback: (mode: LoopMode) => void): void

设置循环模式的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'setLoopMode'：当设置循环模式的命令被发送到会话时，触发该事件。 |
| callback | (mode: [LoopMode](arkts-apis-avsession-e.md#loopmode10)) => void | 是 | 回调函数。参数mode是循环模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('setLoopMode', (mode: avSession.LoopMode) => {
2. console.info(`on setLoopMode mode : ${mode}`);
3. });
```

## on('setTargetLoopMode')18+

PhonePC/2in1TabletTVWearable

on(type: 'setTargetLoopMode', callback: Callback<LoopMode>): void

设置目标循环模式的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'setTargetLoopMode'。  - 'setTargetLoopMode'：当设置目标循环模式的命令被发送到会话时，触发该事件。 |
| callback | Callback<[LoopMode](arkts-apis-avsession-e.md#loopmode10)> | 是 | 回调函数。参数表示目标循环模式。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('setTargetLoopMode', (mode: avSession.LoopMode) => {
2. console.info(`on setTargetLoopMode mode : ${mode}`);
3. });
```

## on('toggleFavorite')10+

PhonePC/2in1TabletTVWearable

on(type: 'toggleFavorite', callback: (assetId: string) => void): void

设置是否收藏的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'toggleFavorite'：当是否收藏的命令被发送到会话时，触发该事件。 |
| callback | (assetId: string) => void | 是 | 回调函数。参数assetId是媒体ID。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('toggleFavorite', (assetId: string) => {
2. console.info(`on toggleFavorite mode : ${assetId}`);
3. });
```

## on('skipToQueueItem')10+

PhonePC/2in1TabletTVWearable

on(type: 'skipToQueueItem', callback: (itemId: number) => void): void

设置播放列表其中某项被选中的监听事件，session端可以选择对这个单项歌曲进行播放。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'skipToQueueItem'：当播放列表选中单项的命令被发送到会话时，触发该事件。 |
| callback | (itemId: number) => void | 是 | 回调函数。参数itemId是选中的播放列表项的ID。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('skipToQueueItem', (itemId: number) => {
2. console.info(`on skipToQueueItem id : ${itemId}`);
3. });
```

## on('handleKeyEvent')10+

PhonePC/2in1TabletTVWearable

on(type: 'handleKeyEvent', callback: (event: KeyEvent) => void): void

设置蓝牙/有线等外设接入的按键输入事件的监听，监听多媒体按键事件中播放、暂停、上下一首、快进、快退的指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'handleKeyEvent'：当按键事件被发送到会话时，触发该事件。 |
| callback | (event: [KeyEvent](js-apis-keyevent.md)) => void | 是 | 回调函数。参数event是按键事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { KeyEvent } from '@kit.InputKit';

3. currentAVSession.on('handleKeyEvent', (event: KeyEvent) => {
4. console.info(`on handleKeyEvent event : ${event}`);
5. });
```

## on('outputDeviceChange')10+

PhonePC/2in1TabletTVWearable

on(type: 'outputDeviceChange', callback: (state: ConnectionState, device: OutputDeviceInfo) => void): void

设置播放设备变化的监听事件。应用接入[multimedia.avCastPicker (投播组件)](ohos-multimedia-avcastpicker.md)，当用户通过组件切换设备时，会收到设备切换的回调。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'outputDeviceChange'：当播放设备变化时，触发该事件。 |
| callback | (state: [ConnectionState](arkts-apis-avsession-e.md#connectionstate10), device: [OutputDeviceInfo](arkts-apis-avsession-i.md#outputdeviceinfo10)) => void | 是 | 回调函数，参数device是设备相关信息。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('outputDeviceChange', (state: avSession.ConnectionState, device: avSession.OutputDeviceInfo) => {
2. console.info(`on outputDeviceChange device : ${device}`);
3. });
```

## on('commonCommand')10+

PhonePC/2in1TabletTVWearable

on(type: 'commonCommand', callback: (command :string, args:{[key: string]: Object}) => void): void

设置自定义控制命令变化的监听器。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'commonCommand'：当自定义控制命令变化时，触发该事件。 |
| callback | (command :string, args:{[key: string]: Object}) => void | 是 | 回调函数，command为变化的自定义控制命令名，args为自定义控制命令的参数，参数内容与[sendCommonCommand](arkts-apis-avsession-avsessioncontroller.md#sendcommoncommand10)方法设置的参数内容完全一致。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. import { avSession } from '@kit.AVSessionKit';
2. @Entry
3. @Component
4. struct Index {
5. @State message: string = 'hello world';

7. build() {
8. Column() {
9. Text(this.message)
10. .onClick(()=>{
11. let currentAVSession: avSession.AVSession | undefined = undefined;
12. let tag = "createNewSession";
13. let context: Context = this.getUIContext().getHostContext() as Context;

15. avSession.createAVSession(context, tag, "audio", (data: avSession.AVSession) => {
16. currentAVSession = data;
17. if (currentAVSession !== undefined) {
18. (currentAVSession as avSession.AVSession).on('commonCommand', (commonCommand, args) => {
19. console.info(`OnCommonCommand, the command is ${commonCommand}, args: ${JSON.stringify(args)}`);
20. });
21. }
22. });
23. })
24. }
25. .width('100%')
26. .height('100%')
27. }
28. }
```

## off('play')10+

PhonePC/2in1TabletTVWearable

off(type: 'play', callback?: () => void): void

取消会话播放事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'play'。 |
| callback | () => void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('play');
```

## offPlay22+

PhonePC/2in1TabletTVWearable

offPlay(callback?: Callback<CommandInfo>): void

取消会话播放事件监听。使用callback异步回调。

指定callback，取消对应监听；未指定callback，则取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[CommandInfo](arkts-apis-avsession-i.md#commandinfo22)> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.offPlay();
```

## off('pause')10+

PhonePC/2in1TabletTVWearable

off(type: 'pause', callback?: () => void): void

取消会话暂停事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'pause'。 |
| callback | () => void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('pause');
```

## off('stop')10+

PhonePC/2in1TabletTVWearable

off(type: 'stop', callback?: () => void): void

取消会话停止事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'stop'。 |
| callback | () => void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('stop');
```

## off('playNext')10+

PhonePC/2in1TabletTVWearable

off(type: 'playNext', callback?: () => void): void

取消会话播放下一首事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是 'playNext'。 |
| callback | () => void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('playNext');
```

## offPlayNext22+

PhonePC/2in1TabletTVWearable

offPlayNext(callback?: Callback<CommandInfo>): void

取消会话播放下一首事件监听。使用callback异步回调。

指定callback，取消对应监听；未指定callback，则取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[CommandInfo](arkts-apis-avsession-i.md#commandinfo22)> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.offPlayNext();
```

## off('playPrevious')10+

PhonePC/2in1TabletTVWearable

off(type: 'playPrevious', callback?: () => void): void

取消会话播放上一首事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'playPrevious'。 |
| callback | () => void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('playPrevious');
```

## offPlayPrevious22+

PhonePC/2in1TabletTVWearable

offPlayPrevious(callback?: Callback<CommandInfo>): void

取消会话播放上一首事件监听。使用callback异步回调。

指定callback，取消对应监听；未指定callback，则取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[CommandInfo](arkts-apis-avsession-i.md#commandinfo22)> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.offPlayPrevious();
```

## off('fastForward')10+

PhonePC/2in1TabletTVWearable

off(type: 'fastForward', callback?: () => void): void

取消会话快进事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'fastForward'。 |
| callback | () => void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('fastForward');
```

## offFastForward22+

PhonePC/2in1TabletTVWearable

offFastForward(callback?: TwoParamCallback<number, CommandInfo>): void

取消会话快进事件监听。使用callback异步回调。

指定callback，取消对应监听；未指定callback，则取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | TwoParamCallback<number, [CommandInfo](arkts-apis-avsession-i.md#commandinfo22)> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.offFastForward();
```

## off('rewind')10+

PhonePC/2in1TabletTVWearable

off(type: 'rewind', callback?: () => void): void

取消会话快退事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'rewind'。 |
| callback | () => void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('rewind');
```

## offRewind22+

PhonePC/2in1TabletTVWearable

offRewind(callback?: TwoParamCallback<number, CommandInfo>): void

取消会话快退事件监听。使用callback异步回调。

指定callback，取消对应监听；未指定callback，则取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | TwoParamCallback<number, [CommandInfo](arkts-apis-avsession-i.md#commandinfo22)> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.offRewind();
```

## off('seek')10+

PhonePC/2in1TabletTVWearable

off(type: 'seek', callback?: (time: number) => void): void

取消跳转节点事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持关闭事件'seek'。 |
| callback | (time: number) => void | 否 | 回调函数，参数time是时间节点，单位为毫秒。  当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('seek');
```

## off('setSpeed')10+

PhonePC/2in1TabletTVWearable

off(type: 'setSpeed', callback?: (speed: number) => void): void

取消播放速率变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持关闭事件'setSpeed'。 |
| callback | (speed: number) => void | 否 | 回调函数，参数speed是播放倍速。  当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('setSpeed');
```

## off('setLoopMode')10+

PhonePC/2in1TabletTVWearable

off(type: 'setLoopMode', callback?: (mode: LoopMode) => void): void

取消循环模式变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持关闭事件'setLoopMode'。 |
| callback | (mode: [LoopMode](arkts-apis-avsession-e.md#loopmode10)) => void | 否 | 回调函数，参数mode是循环模式。  - 当监听事件取消成功，err为undefined，否则返回错误对象。  - 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('setLoopMode');
```

## off('setTargetLoopMode')18+

PhonePC/2in1TabletTVWearable

off(type: 'setTargetLoopMode', callback?: Callback<LoopMode>): void

取消目标循环模式变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持关闭事件'setTargetLoopMode'。 |
| callback | Callback<[LoopMode](arkts-apis-avsession-e.md#loopmode10)> | 否 | 回调函数，参数表示目标循环模式。  - 当监听事件取消成功，err为undefined，否则返回错误对象。  - 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('setTargetLoopMode');
```

## off('toggleFavorite')10+

PhonePC/2in1TabletTVWearable

off(type: 'toggleFavorite', callback?: (assetId: string) => void): void

取消是否收藏的事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持关闭事件'toggleFavorite'。 |
| callback | (assetId: string) => void | 否 | 回调函数，参数assetId是媒体ID。  当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('toggleFavorite');
```

## off('skipToQueueItem')10+

PhonePC/2in1TabletTVWearable

off(type: 'skipToQueueItem', callback?: (itemId: number) => void): void

取消播放列表单项选中的事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持关闭事件'skipToQueueItem'。 |
| callback | (itemId: number) => void | 否 | 回调函数，参数itemId是播放列表单项ID。  当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('skipToQueueItem');
```

## off('handleKeyEvent')10+

PhonePC/2in1TabletTVWearable

off(type: 'handleKeyEvent', callback?: (event: KeyEvent) => void): void

取消按键事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持关闭事件'handleKeyEvent'。 |
| callback | (event: [KeyEvent](js-apis-keyevent.md)) => void | 否 | 回调函数，参数event是按键事件。  当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('handleKeyEvent');
```

## off('outputDeviceChange')10+

PhonePC/2in1TabletTVWearable

off(type: 'outputDeviceChange', callback?: (state: ConnectionState, device: OutputDeviceInfo) => void): void

取消播放设备变化的事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持关闭事件'outputDeviceChange'。 |
| callback | (state: [ConnectionState](arkts-apis-avsession-e.md#connectionstate10), device: [OutputDeviceInfo](arkts-apis-avsession-i.md#outputdeviceinfo10)) => void | 否 | 回调函数，参数device是设备相关信息。  当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('outputDeviceChange');
```

## off('commonCommand')10+

PhonePC/2in1TabletTVWearable

off(type: 'commonCommand', callback?: (command: string, args:{[key: string]: Object}) => void): void

取消自定义控制命令的变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'commonCommand'。 |
| callback | (command: string, args:{[key: string]: Object}) => void | 否 | 回调函数，参数command是变化的自定义控制命令名，args为自定义控制命令的参数。  该参数为可选参数，若不填写该参数，则认为取消所有对command事件的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('commonCommand');
```

## on('answer')11+

PhonePC/2in1TabletTVWearable

on(type: 'answer', callback: Callback<void>): void

设置通话接听的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'answer'：当通话接听时，触发该事件。 |
| callback | Callback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('answer', () => {
2. console.info('on call answer');
3. });
```

## off('answer')11+

PhonePC/2in1TabletTVWearable

off(type: 'answer', callback?: Callback<void>): void

取消通话接听事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'answer'。 |
| callback | Callback<void> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('answer');
```

## on('hangUp')11+

PhonePC/2in1TabletTVWearable

on(type: 'hangUp', callback: Callback<void>): void

设置通话挂断的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'hangUp'：当通话挂断时，触发该事件。 |
| callback | Callback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('hangUp', () => {
2. console.info('on call hangUp');
3. });
```

## off('hangUp')11+

PhonePC/2in1TabletTVWearable

off(type: 'hangUp', callback?: Callback<void>): void

取消通话挂断事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'hangUp'。 |
| callback | Callback<void> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('hangUp');
```

## on('toggleCallMute')11+

PhonePC/2in1TabletTVWearable

on(type: 'toggleCallMute', callback: Callback<void>): void

设置通话静音的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'toggleCallMute'：当通话静音或解除静音时，触发该事件。 |
| callback | Callback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('toggleCallMute', () => {
2. console.info('on call toggleCallMute');
3. });
```

## off('toggleCallMute')11+

PhonePC/2in1TabletTVWearable

off(type: 'toggleCallMute', callback?: Callback<void>): void

取消通话静音事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'toggleCallMute'。 |
| callback | Callback<void> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('toggleCallMute');
```

## on('castDisplayChange')12+

PhoneTablet

on(type: 'castDisplayChange', callback: Callback<CastDisplayInfo>): void

设置扩展屏投播显示设备变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'castDisplayChange'：当扩展屏投播显示设备变化时触发事件。 |
| callback | Callback<[CastDisplayInfo](arkts-apis-avsession-i.md#castdisplayinfo12)> | 是 | 回调函数。参数是扩展屏投播显示设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. let castDisplay: avSession.CastDisplayInfo;
2. currentAVSession.on('castDisplayChange', (display: avSession.CastDisplayInfo) => {
3. if (display.state === avSession.CastDisplayState.STATE_ON) {
4. castDisplay = display;
5. console.info(`Succeeded in castDisplayChange display : ${display.id} ON`);
6. } else if (display.state === avSession.CastDisplayState.STATE_OFF){
7. console.info(`Succeeded in castDisplayChange display : ${display.id} OFF`);
8. }
9. });
```

## off('castDisplayChange')12+

PhoneTablet

off(type: 'castDisplayChange', callback?: Callback<CastDisplayInfo>): void

取消扩展屏投播显示设备变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'castDisplayChange'。 |
| callback | Callback<[CastDisplayInfo](arkts-apis-avsession-i.md#castdisplayinfo12)> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('castDisplayChange');
```

## stopCasting10+

PhonePC/2in1TabletTV

stopCasting(callback: AsyncCallback<void>): void

结束投播。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当命令发送成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600109 | The remote connection is not established. |

**示例：**

```
1. currentAVSession.stopCasting(() => {
2. console.info('Succeeded in stopping casting.');
3. });
```

## stopCasting10+

PhonePC/2in1TabletTV

stopCasting(): Promise<void>

结束投播。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当成功结束投播，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600109 | The remote connection is not established. |

**示例：**

```
1. currentAVSession.stopCasting().then(() => {
2. console.info('Succeeded in stopping casting.');
3. });
```

## getOutputDeviceSync10+

PhonePC/2in1TabletTVWearable

getOutputDeviceSync(): OutputDeviceInfo

使用同步方法获取当前输出设备信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [OutputDeviceInfo](arkts-apis-avsession-i.md#outputdeviceinfo10) | 当前输出设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. let currentOutputDevice: avSession.OutputDeviceInfo = currentAVSession.getOutputDeviceSync();
```

## getAllCastDisplays12+

PhoneTablet

getAllCastDisplays(): Promise<Array<CastDisplayInfo>>

获取当前系统中所有支持扩展屏投播的显示设备。通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[CastDisplayInfo](arkts-apis-avsession-i.md#castdisplayinfo12)>> | Promise对象，返回当前系统中所有支持扩展屏投播的显示设备。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. let castDisplay: avSession.CastDisplayInfo;
2. currentAVSession.getAllCastDisplays().then((data: Array< avSession.CastDisplayInfo >) => {
3. if (data.length >= 1) {
4. castDisplay = data[0];
5. }
6. });
```

## on('playFromAssetId')(deprecated)

PhonePC/2in1TabletTVWearable

on(type:'playFromAssetId', callback: (assetId: number) => void): void

设置媒体id播放监听事件。

说明

从 API version 11 开始支持，从 API version 20 开始废弃。建议使用[on('playWithAssetId')](arkts-apis-avsession-avsession.md#onplaywithassetid20)设置媒体id播放监听事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件是'playFromAssetId'，当媒体id播放时，触发该事件回调。 |
| callback | (assetId: number) => void | 是 | 回调函数。参数assetId是媒体id。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('playFromAssetId', (assetId: number) => {
2. console.info('on playFromAssetId entry');
3. });
```

## off('playFromAssetId')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'playFromAssetId', callback?: (assetId: number) => void): void

取消媒体id播放事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

说明

从 API version 11 开始支持，从 API version 20 开始废弃。建议使用[off('playWithAssetId')](arkts-apis-avsession-avsession.md#offplaywithassetid20)取消媒体id播放事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 关闭对应的监听事件，支持的事件是'playFromAssetId'。 |
| callback | (assetId: number) => void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。参数assetId是媒体id。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('playFromAssetId');
```

## on('customDataChange')20+

PhonePC/2in1TabletTV

on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void

注册从远程设备发送的自定义数据的监听器。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'customDataChange'，当媒体提供方发送自定义数据时，触发该事件。 |
| callback | Callback<Record<string, Object>> | 是 | 回调函数，用于接收自定义数据。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.on('customDataChange', (callback) => {
2. console.info(`Caught customDataChange event,the new callback is: ${JSON.stringify(callback)}`);
3. });
```

## off('customDataChange')20+

PhonePC/2in1TabletTV

off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void

取消自定义数据监听。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持的事件是'customDataChange'。 |
| callback | Callback<Record<string, Object>> | 否 | 注册监听事件时的回调函数。该参数为可选参数，若不填写该参数，则认为取消会话所有与此事件相关的监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**示例：**

```
1. currentAVSession.off('customDataChange');
```
