---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-textreader-api
title: TextReader（朗读控件）
breadcrumb: API参考 > AI > Speech Kit（场景化语音服务） > ArkTS API > TextReader（朗读控件）
category: harmonyos-references
scraped_at: 2026-04-29T14:09:50+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:5fe390f4c07f372ecc627452d38cdbbbde04a5427f2b0848c36e96425b7c582d
---

朗读控件使用AI能力将文本实时转化成语音并进行朗读，适用于一些新闻类文本内容浏览类APP，帮助用户在一些无法直接浏览文本内容的场景下，通过文本朗读来高效获取信息。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { TextReader } from '@kit.SpeechKit';
```

## 注意事项

PhonePC/2in1Tablet

调用朗读控件接口前，必须先调用[init](speech-textreader-api.md#init)初始化，否则会报错。

## init

PhonePC/2in1Tablet

init(context: common.BaseContext, readParams: ReaderParam): Promise<void>

朗读控件初始化，用于初始化TTS引擎和底层播放器，初始化失败会返回对应错误码。

使用Promise异步回调。若要配置长时权限，请参考[开发指南步骤9](../harmonyos-guides/speech-textreader-guide.md#开发步骤)。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.KEEP\_BACKGROUND\_RUNNING

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.BaseContext](js-apis-inner-application-basecontext.md) | 是 | 当前应用上下文。 |
| readParams | [ReaderParam](speech-textreader-api.md#readerparam) | 是 | 朗读参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. Interface caller does not have permission ohos.permission.KEEP\_BACKGROUND\_RUNNING. |
| 401 | Parameter error. |
| 1010600011 | Initialize failed. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. // 获取应用上下文

9. async aboutToAppear(): Promise<void> {
10. let context: Context | undefined = this.getUIContext().getHostContext();
11. if (context) {
12. // 设置朗读参数
13. const readerParams: TextReader.ReaderParam = {
14. isVoiceBrandVisible: true,
15. businessBrandInfo: {
16. panelName: '小艺朗读',
17. panelIcon: $r('app.media.startIcon')
18. }
19. };
20. // 初始化朗读控件
21. await TextReader.init(context, readerParams).then(() => {
22. console.info(`TextReader succeeded in initializing.`);
23. }).catch((e: BusinessError) => {
24. console.error(`TextReader failed to initialize. Code: ${e.code}, message: ${e.message}`);
25. })
26. }
27. }

29. build() {
30. // ...
31. }
32. }
```

## start

PhonePC/2in1Tablet

start(readInfoList: ReadInfo[], articleId?: string): Promise<void>

朗读控件起播。播放失败返回对应错误码。

使用Promise异步回调。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| readInfoList | [ReadInfo](speech-textreader-api.md#readinfo)[] | 是 | 播放文章列表。  - 若列表的第一篇文章是有分类的（即带有category或categoryObject字段），后续文章不带分类，也会归为“其他”分类下。  - 若列表的第一篇是没有分类的，后续文章即使带分类，也不会生效。 |
| articleId | string | 否 | 文章id，articleId不传时，默认从文章列表中的第一篇开始播放；传参时，从传入articleId对应的文章开始依次往下播放。（文章id不能重复，否则从列表进入同id的文章，会自动选择同id的第一篇朗读） |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1010600012 | The TextReader is not initialized. |
| 1010600013 | Text-to-speech engine error. |
| 1010600014 | AudioRenderer play error. |
| 1010600015 | Audio decode error. |
| 1010600016 | AVSession error. |
| 1010600017 | Other error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const readInfoList: TextReader.ReadInfo[] = [{
5. id: '001',
6. title: {
7. text:'水调歌头.明月几时有',
8. isClickable:true
9. },
10. author:{
11. text:'宋.苏轼',
12. isClickable:true
13. },
14. date: {
15. text:'2024/01/01',
16. isClickable:false
17. },
18. bodyInfo: '明月几时有？把酒问青天。'
19. }];
20. // 启动朗读控件
21. TextReader.start(readInfoList).then(() => {
22. console.info(`TextReader succeeded in starting`);
23. }).catch((e: BusinessError) => {
24. console.error(`TextReader failed to start. Code: ${e.code}, message: ${e.message}`);
25. })
```

## start

PhonePC/2in1Tablet

start(readInfoList: ReadInfo[], articleId: string | undefined, startParams: StartParams): Promise<void>

朗读控件起播，可以通过设置startParams参数实现隐藏Minibar等效果。播放失败返回对应错误码。

使用Promise异步回调。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| readInfoList | [ReadInfo](speech-textreader-api.md#readinfo)[] | 是 | 播放文章列表。  - 若列表的第一篇文章是有分类的（即带有category或categoryObject字段），后续文章不带分类，也会归为“其他”分类下。  - 若列表的第一篇是没有分类的，后续文章即使带分类，也不会生效。 |
| articleId | string | undefined | 是 | 文章id（文章id不能重复，否则从列表进入同id的文章，会自动选择同id的第一篇文章），articleId不传时，默认从文章列表中的第一篇开始播放；传参时，从传入articleId对应的文章开始依次往下播放。 |
| startParams | [StartParams](speech-textreader-api.md#startparams) | 是 | 朗读控件起播参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1010600012 | The TextReader is not initialized. |
| 1010600013 | Text-to-speech engine error. |
| 1010600014 | AudioRenderer play error. |
| 1010600015 | Audio decode error. |
| 1010600016 | AVSession error. |
| 1010600017 | Other error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const readInfoList: TextReader.ReadInfo[] = [{
5. id: '001',
6. title: {
7. text:'水调歌头.明月几时有',
8. isClickable:true
9. },
10. author:{
11. text:'宋.苏轼',
12. isClickable:true
13. },
14. date: {
15. text:'2024/01/01',
16. isClickable:false
17. },
18. bodyInfo: '明月几时有？把酒问青天。'
19. }];
20. const startParams: TextReader.StartParams = {
21. isMinibarHidden: false,
22. callbackParam: '0'
23. }
24. // 启动朗读控件
25. TextReader.start(readInfoList, undefined, startParams).then(() => {
26. console.info(`TextReader succeeded in starting`);
27. }).catch((e: BusinessError) => {
28. console.error(`TextReader failed to start. Code: ${e.code}, message: ${e.message}`);
29. })
```

## stop

PhonePC/2in1Tablet

stop(): Promise<void>

朗读控件停止朗读，执行播放面板的关闭，注销监听，重置参数。

使用Promise异步回调。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010600012 | The TextReader is not initialized. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. TextReader.stop().then(() => {
5. console.info(`TextReader succeeded in stopping.`);
6. }).catch((e: BusinessError) => {
7. console.error(`TextReader failed to stop. Code: ${e.code}, message: ${e.message}`);
8. })
```

## resetParam

PhonePC/2in1Tablet

resetParam(paramName: ResetParamType) : void

提供重置初始化参数、清除播放列表接口。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| paramName | [ResetParamType](speech-textreader-api.md#resetparamtype) | 是 | 重置参数类型。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.resetParam(TextReader.ResetParamType.BAR_PARAM)
5. console.info(`TextReader succeeded in resetParam.`);
6. } catch (e) {
7. console.error(`TextReader failed to resetParam. Code: ${e.code}, message: ${e.message}`);
8. }
```

## release

PhonePC/2in1Tablet

release(): Promise<void>

释放朗读控件的所有资源。

使用Promise异步回调。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010600012 | The TextReader is not initialized. |
| 1010600020 | Release error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. TextReader.release().then(() => {
5. console.info(`TextReader succeeded in releasing.`);
6. }).catch((e: BusinessError) => {
7. console.error(`TextReader failed to release. Code: ${e.code}, message: ${e.message}`);
8. })
```

## pause

PhonePC/2in1Tablet

pause(): void

暂停播放。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010600012 | The TextReader is not initialized. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.pause();
5. } catch (e) {
6. console.error(`TextReader failed to pause. Code: ${e.code}, message: ${e.message}`);
7. }
```

## resume

PhonePC/2in1Tablet

resume(): void

继续播放。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010600012 | The TextReader is not initialized. |
| 1010600013 | Text-to-speech engine error. |
| 1010600014 | AudioRenderer play error. |
| 1010600015 | Audio decode error. |
| 1010600016 | AVSession error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.resume();
5. } catch (e) {
6. console.error(`TextReader failed to resume. Code: ${e.code}, message: ${e.message}`);
7. }
```

## playPrev

PhonePC/2in1Tablet

playPrev(): void

播放上一篇文章。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010600012 | The TextReader is not initialized. |
| 1010600018 | playPrev failed. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.playPrev();
5. } catch (e) {
6. console.error(`TextReader failed to play previous article. Code: ${e.code}, message: ${e.message}`);
7. }
```

## playNext

PhonePC/2in1Tablet

playNext(): void

播放下一篇文章。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010600012 | The TextReader is not initialized. |
| 1010600019 | playNext failed. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.playNext();
5. } catch (e) {
6. console.error(`TextReader failed to play next article. Code: ${e.code}, message: ${e.message}`);
7. }
```

## hidePanel

PhonePC/2in1Tablet

hidePanel(): void

隐藏播放面板。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010600012 | The TextReader is not initialized. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.hidePanel();
5. } catch (e) {
6. console.error(`TextReader failed to hide panel. Code: ${e.code}, message: ${e.message}`);
7. }
```

## showPanel

PhonePC/2in1Tablet

showPanel(): void

打开播放面板。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010600012 | The TextReader is not initialized. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.showPanel();
5. } catch (e) {
6. console.error(`TextReader failed to show panel. Code: ${e.code}, message: ${e.message}`);
7. }
```

## showMinibar

PhonePC/2in1Tablet

showMinibar(): void

显示Minibar。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.2(14)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010600012 | The TextReader is not initialized. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.showMinibar();
5. } catch (e) {
6. console.error(`TextReader failed to show Minibar. Code: ${e.code}, message: ${e.message}`);
7. }
```

## hideMinibar

PhonePC/2in1Tablet

hideMinibar(): void

隐藏Minibar。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.2(14)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1010600012 | The TextReader is not initialized. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.hideMinibar();
5. } catch (e) {
6. console.error(`TextReader failed to hide Minibar. Code: ${e.code}, message: ${e.message}`);
7. }
```

## queryReadState

PhonePC/2in1Tablet

queryReadState(id?: string): ReadState

查询文章播报状态。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 | 文章id，默认为当前正在朗读的文章id。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ReadState](speech-textreader-api.md#readstate) | 文章播报状态 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. let readState = TextReader.queryReadState('article_01');
5. console.info(`Succeeded in querying read state, read state: ${JSON.stringify(readState)}`);
6. } catch(e) {
7. console.error(`TextReader failed to queryReadState. Code: ${e.code}, message: ${e.message}`);
8. }
```

## setArticleContent

PhonePC/2in1Tablet

setArticleContent(id: string, content?: string): void

设置文章内容。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 文章id。 |
| content | string | 否 | 文章内容，content不传或者为空时，播放指定id的文章时，控件内容页显示加载失败；传参时，将指定id文章的内容设置为content。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.setArticleContent('article_01', '明月几时有？把酒问青天。');
5. } catch (e) {
6. console.error(`TextReader failed to setArticleContent. Code: ${e.code}, message: ${e.message}`);
7. }
```

## setArticle

PhonePC/2in1Tablet

setArticle(readInfo: ReadInfo): void

设置指定文章的信息，并立即播放。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| readInfo | [ReadInfo](speech-textreader-api.md#readinfo) | 是 | 文章信息，仅更新image、imageUrl、bodyInfo、bodyInfoObject；如果文章的ID不在列表中，则不会生效。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';
2. import { image } from '@kit.ImageKit';

4. const readInfo: TextReader.ReadInfo = {
5. id: '001',
6. title: {
7. text:'水调歌头.明月几时有',
8. isClickable:true
9. },
10. author:{
11. text:'宋.苏轼',
12. isClickable:true
13. },
14. date: {
15. text:'2024/01/01',
16. isClickable:false
17. },
18. bodyInfo: '明月几时有？把酒问青天。',
19. image: {} as image.PixelMap
20. };
21. try {
22. TextReader.setArticle(readInfo);
23. } catch (e) {
24. console.error(`TextReader failed to setArticle. Code: ${e.code}, message: ${e.message}`);
25. }
```

## loadMore

PhonePC/2in1Tablet

loadMore(readInfos: ReadInfo[], isEnd: boolean): void

加载更多文章到文章列表。需在项目init和start之后调用，建议在'requestMore'操作监听中使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| readInfos | [ReadInfo](speech-textreader-api.md#readinfo)[] | 是 | 要加载的文章列表。 |
| isEnd | boolean | 是 | 是否还有更多内容需要加载。  - true：已加载所有内容。  - false：还有内容未加载完。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { ReadStateCode, TextReader, TextReaderIcon } from '@kit.SpeechKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {

8. @State readInfoList: TextReader.ReadInfo[] = [];
9. @State readState: ReadStateCode = ReadStateCode.WAITING;
10. @State isInit: boolean = false;
11. @State selectedReadInfo: TextReader.ReadInfo = this.readInfoList[0];
12. aboutToAppear(){
13. let context: Context | undefined = this.getUIContext().getHostContext();
14. if (!context) {
15. console.error(`context is undefined.`);
16. return;
17. }

19. // 设置朗读参数
20. const readerParams: TextReader.ReaderParam = {
21. isVoiceBrandVisible: true,
22. businessBrandInfo: {
23. panelName: '小艺朗读',
24. panelIcon: $r('app.media.startIcon')
25. }
26. };

28. // 初始化朗读控件
29. TextReader.init(context, readerParams).then(() => {
30. console.info(`TextReader succeeded in initializing.`);
31. }).catch((e: BusinessError) => {
32. console.error(`TextReader failed to initialize. Code: ${e.code}, message: ${e.message}`);
33. })

35. /**
36. * 加载数据
37. */
38. console.info(`ReadStateCode: ${JSON.stringify(this.readState)}`);
39. let readInfoList: TextReader.ReadInfo[] = [{
40. id: '001',
41. title: {
42. text:'水调歌头.明月几时有',
43. isClickable:true
44. },
45. author:{
46. text:'宋.苏轼',
47. isClickable:true
48. },
49. date: {
50. text:'2024/01/01',
51. isClickable:false
52. },
53. bodyInfo: '明月几时有？把酒问青天。'
54. }];
55. this.readInfoList = readInfoList;
56. this.selectedReadInfo = this.readInfoList[0];
57. }

59. // 设置操作监听
60. setActionListener() {
61. // ...
62. TextReader.on('requestMore', () => {
63. console.info(`requestMore`);
64. try {
65. console.info(`loadMore`);
66. TextReader.loadMore(this.readInfoList, true);
67. } catch (e) {
68. console.error(`TextReader failed to loadMore. Code: ${e.code}, message: ${e.message}`);
69. }
70. });
71. }

74. build() {
75. Column() {
76. TextReaderIcon({ readState: this.readState })
77. .margin({ right: 20 })
78. .width(32)
79. .height(32)
80. .onClick(() => {
81. try {
82. this.setActionListener();
83. void TextReader.start(this.readInfoList, this.selectedReadInfo?.id);
84. } catch(e) {
85. console.error(`TextReader failed to start`);
86. }
87. })
88. }
89. .height('100%')
90. }
91. }
```

## queryReadStateByCategoryId

PhonePC/2in1Tablet

queryReadStateByCategoryId(categoryId: string): ReadState

根据分类id查询文章状态，查询当前分类是否有正在播报的文章。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| categoryId | string | 是 | 当前播报文章的分类id。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ReadState](speech-textreader-api.md#readstate) | 文章播报状态 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. let readState = TextReader.queryReadStateByCategoryId('categoryId_01');
5. console.info(`Succeeded in querying read state by category id, read state: ${JSON.stringify(readState)}`);
6. } catch(e) {
7. console.error(`TextReader failed to queryReadStateByCategoryId. Code: ${e.code}, message: ${e.message}`);
8. }
```

## on('setArticle')

PhonePC/2in1Tablet

on(type: 'setArticle', callback: Callback<string>): void

注册设置文章回调函数，点击文章或者切换文章时，若目标文章内容为空（bodyInfo值为空）时，触发该回调执行。同一类型监听，注册多个回调函数，仅第一次注册有效。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'setArticle'，设置文章后，目标文章内容为空（bodyInfo值为空）时，触发该事件。 |
| callback | Callback<string> | 是 | 点击文章或者切换文章时，执行的回调函数，参数为文章id。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.on('setArticle', (id: string) => {
5. console.info(`Succeeded in setting setArticleListener: ${id}`);
6. });
7. } catch (e) {
8. console.error(`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}`);
9. }
```

## off('setArticle')

PhonePC/2in1Tablet

off(type: 'setArticle', callback?: Callback<string>): void

在on(type: 'setArticle')函数调用之后使用，用于注销设置文章回调函数。注销监听后，可以重新注册。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'setArticle'，设置文章后，触发该事件。 |
| callback | Callback<string> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数是同一个，若不填，则取消当前应用监听该事件的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.off('setArticle');
5. } catch (e) {
6. console.error(`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}`);
7. }
```

## on('clickArticle')

PhonePC/2in1Tablet

on(type: 'clickArticle', callback: Callback<string>): void

注册点击事件回调函数，点击标题时，触发该回调执行。同一类型监听，注册多个回调函数，仅第一次注册有效。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'clickArticle'，点击文章标题，触发回调。 |
| callback | Callback<string> | 是 | 点击标题时执行的回调函数，参数为文章id。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.on('clickArticle', (id: string) => {
5. console.info(`Succeeded in setting clickArticleListener: ${id}`);
6. });
7. } catch (e) {
8. console.error(`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}`);
9. }
```

## off('clickArticle')

PhonePC/2in1Tablet

off(type: 'clickArticle', callback?: Callback<string>): void

在on(type: 'clickArticle')函数调用之后使用，用于注销点击事件回调函数。注销监听后，可以重新注册。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'clickArticle'，点击文章标题，取消回调。 |
| callback | Callback<string> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数是同一个，若不填，则取消当前应用监听该事件的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.off('clickArticle');
5. } catch (e) {
6. console.error(`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}`);
7. }
```

## on('clickAuthor')

PhonePC/2in1Tablet

on(type: 'clickAuthor', callback: Callback<string>): void

注册点击事件回调函数，点击作者时，触发该回调执行。同一类型监听，注册多个回调函数，仅第一次注册有效。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'clickAuthor'，点击作者，触发回调。 |
| callback | Callback<string> | 是 | 点击作者时执行的回调函数，参数为文章id。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.on('clickAuthor', (id: string) => {
5. console.info(`Succeeded in setting clickAuthorListener: ${id}`);
6. });
7. } catch (e) {
8. console.error(`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}`);
9. }
```

## off('clickAuthor')

PhonePC/2in1Tablet

off(type: 'clickAuthor', callback?: Callback<string>): void

在on('clickAuthor')函数调用之后使用，用于注销点击事件回调函数。注销监听后，可以重新注册。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'clickAuthor'，点击作者事件，取消回调。 |
| callback | Callback<string> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数是同一个，若不填，则取消当前应用监听该事件的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.off('clickAuthor');
5. } catch (e) {
6. console.error(`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}`);
7. }
```

## on( 'clickNotification')

PhonePC/2in1Tablet

on(type: 'clickNotification', callback: Callback<string>): void

注册点击事件回调函数，通知栏时，触发该回调执行。同一类型监听，注册多个回调函数，仅第一次注册有效。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'clickNotification'，点击通知栏，触发回调。预留参数，暂未支持。 |
| callback | Callback<string> | 是 | 点击通知栏时执行的回调函数，参数为文章id。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.on('clickNotification', (id: string) => {
5. console.info(`Succeeded in setting clickNotificationListener: ${id}`);
6. });
7. } catch (e) {
8. console.error(`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}`);
9. }
```

## off('clickNotification')

PhonePC/2in1Tablet

off(type: 'clickNotification', callback?: Callback<string>): void

在on(type: 'clickNotification')函数调用之后使用，用于注销点击事件回调函数。注销监听后，可以重新注册。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'clickNotification'，点击通知栏事件，取消回调。 |
| callback | Callback<string> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数是同一个，若不填，则取消当前应用监听该事件的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.off('clickNotification');
5. } catch (e) {
6. console.error(`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}`);
7. }
```

## on('showPanel')

PhonePC/2in1Tablet

on(type: 'showPanel', callback: Callback<void>): void

注册拉起播放面板回调函数，拉起播放面板时，触发该回调执行。同一类型监听，注册多个回调函数，仅第一次注册有效。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'showPanel'，拉起面板，触发回调。 |
| callback | Callback<void> | 是 | 拉起面板时执行的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.on('showPanel', () => {
5. console.info(`Succeeded in setting showPanelListener.`);
6. });
7. } catch (e) {
8. console.error(`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}`);
9. }
```

## off('showPanel')

PhonePC/2in1Tablet

off(type: 'showPanel', callback?: Callback<void>): void

在on(type: 'showPanel')函数调用之后使用，用于注销拉起播放面板监听事件。注销监听后，可以重新注册。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'showPanel'，拉起面板，取消回调。 |
| callback | Callback<void> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数是同一个，若不填，则取消当前应用监听该事件的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.off('showPanel');
5. TextReader.off('hidePanel');
6. } catch (e) {
7. console.error(`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}`);
8. }
```

## on('hidePanel')

PhonePC/2in1Tablet

on(type: 'hidePanel', callback: Callback<void>): void

注册收回播放面板回调函数，收回播放面板时，触发该回调执行。同一类型监听，注册多个回调函数，仅第一次注册有效。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'hidePanel'，收回面板，触发回调。 |
| callback | Callback<void> | 是 | 收回面板时执行的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.on('hidePanel', () => {
5. console.info(`Succeeded in setting hidePanelListener.`);
6. });
7. } catch (e) {
8. console.error(`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}`);
9. }
```

## off('hidePanel')

PhonePC/2in1Tablet

off(type: 'hidePanel', callback?: Callback<void>): void

在on(type: 'hidePanel')函数调用之后使用，用于注销收回播放面板监听事件。注销监听后，可以重新注册。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'hidePanel'，收起面板，取消回调。 |
| callback | Callback<void> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数是同一个，若不填，则取消当前应用监听该事件的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.off('showPanel');
5. TextReader.off('hidePanel');
6. } catch (e) {
7. console.error(`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}`);
8. }
```

## on('stop')

PhonePC/2in1Tablet

on(type: 'stop', callback: Callback<void>): void

注册停止回调函数，调用stop时，触发该回调执行。同一类型监听，注册多个回调函数，仅第一次注册有效。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'stop'，调用stop接口或用户主动滑动通知栏退出。 |
| callback | Callback<void> | 是 | 触发stop事件时执行的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.on('stop', () => {
5. console.info(`Succeeded in setting stopListener.`);
6. });
7. } catch (e) {
8. console.error(`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}`);
9. }
```

## off('stop')

PhonePC/2in1Tablet

off(type: 'stop', callback?: Callback<void>): void

在on(type: 'stop')函数调用之后使用，用于注销stop事件的回调函数。注销监听后，可以重新注册。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'stop'，调用stop接口或用户主动滑动通知栏退出。 |
| callback | Callback<void> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数是同一个，若不填，则取消当前应用监听该事件的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.off('stop');
5. } catch (e) {
6. console.error(`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}`);
7. }
```

## on('release')

PhonePC/2in1Tablet

on(type:'release', callback: Callback<void>): void

注册释放回调函数，调用release时，触发该回调执行。同一类型监听，注册多个回调函数，仅第一次注册有效。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'release'，调用release释放资源。 |
| callback | Callback<void> | 是 | 触发release事件时执行的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.on('release', () => {
5. console.info(`Succeeded in setting releaseListener.`);
6. });
7. } catch (e) {
8. console.error(`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}`);
9. }
```

## off('release')

PhonePC/2in1Tablet

off(type: 'release', callback?: Callback<void>): void

在on(type: 'release')函数调用之后使用，用于注销release事件的回调函数。注销监听后，可以重新注册。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'release'，调用release释放资源。 |
| callback | Callback<void> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数是同一个，若不填，则取消当前应用监听该事件的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.off('release');
5. } catch (e) {
6. console.error(`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}`);
7. }
```

## on('stateChange')

PhonePC/2in1Tablet

on(type: 'stateChange', callback: Callback<ReadState>): void

注册状态变化回调函数，当前正在播放的文章状态变更时，触发该回调执行。同一类型监听，注册多个回调函数，仅第一次注册有效。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'stateChange'，当前正在播放的文章状态变更时，触发该事件。 |
| callback | Callback<[ReadState](speech-textreader-api.md#readstate)> | 是 | 正在播放的文章状态变更时，执行的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.on('stateChange', (state: TextReader.ReadState) => {
5. console.info(`Succeeded in setting stateChangeListener: ${JSON.stringify(state)}`);
6. });
7. } catch (e) {
8. console.error(`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}`);
9. }
```

## off('stateChange')

PhonePC/2in1Tablet

off(type: 'stateChange', callback?: Callback<ReadState>): void

在on(type: 'stateChange')函数调用之后使用，用于注销正在播放的文章状态变更的回调函数。注销监听后，可以重新注册。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'stateChange'，当前正在播放的文章状态变更时，触发该事件。 |
| callback | Callback<[ReadState](speech-textreader-api.md#readstate)> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数是同一个，若不填，则取消当前应用监听该事件的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.off('stateChange');
5. } catch (e) {
6. console.error(`TextReader failed to unset on(type: 'requestMore')eventListener. Code: ${e.code}, message: ${e.message}`);
7. }
```

## on('requestMore')

PhonePC/2in1Tablet

on(type: 'requestMore', callback: Callback<void>): void

注册请求更多文章回调函数，拉到播放列表底端或播放到文章最后一篇，触发该回调执行。同一类型监听，注册多个回调函数，仅第一次注册有效。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'requestMore'，请求更多文章时，触发该事件监听。 |
| callback | Callback<void> | 是 | 拉到播放列表底端或播放到文章最后一篇，触发该回调执行。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.on('requestMore', () => {
5. console.info(`Succeeded in setting requestMoreListener.`);
6. });
7. } catch (e) {
8. console.error(`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}`);
9. }
```

## on('requestMore')

PhonePC/2in1Tablet

on(type: 'requestMore', callback: Callback<string>): void

注册请求更多文章回调函数，拉到播放列表底端或播放到文章最后一篇，触发该回调执行，返回用户自定义参数。同一类型监听，注册多个回调函数，仅第一次注册有效。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'requestMore'，拉到播放列表底端请求更多文章时，触发该事件监听。 |
| callback | Callback<string> | 是 | 拉到播放列表底端或播放到文章最后一篇，触发该回调执行。返回的自定义参数在[StartParams](speech-textreader-api.md#startparams)的callbackParam属性配置。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.on('requestMore', (callback) => {
5. console.info(`Succeeded in setting requestMoreListener. Callback is ${callback}`);
6. });
7. } catch (e) {
8. console.error(`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}`);
9. }
```

## off('requestMore')

PhonePC/2in1Tablet

off(type: 'requestMore', callback?: Callback<void>): void

在on(type: 'requestMore')函数调用之后使用，用于注销拉到播放列表底端或播放到文章最后一篇的回调函数。注销监听后，可以重新注册。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'requestMore'，请求更多文章时，触发该事件监听。 |
| callback | Callback<void> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数是同一个，若不填，则取消当前应用监听该事件的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.off('requestMore');
5. } catch (e) {
6. console.error(`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}`);
7. }
```

## off('requestMore')

PhonePC/2in1Tablet

off(type: 'requestMore', callback: Callback<string>): void

在on(type: 'requestMore')函数调用之后使用，用于注销拉到播放列表底端或播放到文章最后一篇带用户自定义参数的回调函数。注销监听后，可以重新注册。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'requestMore'，请求更多文章时，触发该事件监听。 |
| callback | Callback<string> | 是 | 需要取消监听的回调函数，需与订阅时传入的回调函数是同一个。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.off('requestMore', (callback:string) => {
5. console.info(`Succeeded in setting requestMoreListener. Callback is ${callback}`);
6. });
7. } catch (e) {
8. console.error(`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}`);
9. }
```

## on('eventNotification')

PhonePC/2in1Tablet

on(type: 'eventNotification' , callback: Callback<NotificationEvent>): void

注册播控中心状态回调函数，播控中心状态发生变化时，触发该回调执行。同一类型监听，注册多个回调函数，仅第一次注册有效。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'eventNotification'，播控中心状态变化,触发该事件。 |
| callback | Callback<[NotificationEvent](speech-textreader-api.md#notificationevent)> | 是 | 播控中心状态发生变化时，触发该回调执行。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.on('eventNotification', (ne: TextReader.NotificationEvent) => {
5. console.info(`Succeeded in setting eventNotificationListener: ${JSON.stringify(ne)}`);
6. });
7. } catch (e) {
8. console.error(`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}`);
9. }
```

## off('eventNotification')

PhonePC/2in1Tablet

off(type: 'eventNotification', callback?: Callback<NotificationEvent>): void

在on(type: 'eventNotification')函数调用之后使用，用于注销播控中心状态发生变化的回调函数。注销监听后，可以重新注册。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型。事件回调类型，支持的事件为'eventNotification'，注销该事件。 |
| callback | Callback<[NotificationEvent](speech-textreader-api.md#notificationevent)> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数是同一个，若不填，则取消当前应用监听该事件的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.off('eventNotification');
5. } catch (e) {
6. console.error(`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}`);
7. }
```

## on('eventPanel')

PhonePC/2in1Tablet

on(type: 'eventPanel', callback: Callback<PanelEvent>): void

注册播放面板状态回调函数，播放面板状态发生变化时，触发该回调执行。同一类型监听，注册多个回调函数，仅第一次注册有效。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'eventPanel'，播放面板状态变化，其中[PanelEvent](speech-textreader-api.md#panelevent)中的BPC\_10 click事件回调只支持手机。 |
| callback | Callback<[PanelEvent](speech-textreader-api.md#panelevent)> | 是 | 播放面板状态发生变化时，触发该回调执行。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.on('eventPanel', (pe: TextReader.PanelEvent) => {
5. console.info(`Succeeded in setting eventPanelListener: ${JSON.stringify(pe)}`);
6. });
7. } catch (e) {
8. console.error(`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}`);
9. }
```

## off('eventPanel')

PhonePC/2in1Tablet

off(type: 'eventPanel', callback?: Callback<PanelEvent>): void

在on(type: 'eventPanel')函数调用之后使用，用于播放面板状态发生变化的回调函数。注销监听后，可以重新注册。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'eventPanel'，播放面板状态变化。 |
| callback | Callback<[PanelEvent](speech-textreader-api.md#panelevent)> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数是同一个，若不填，则取消当前应用监听该事件的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.off('eventNotification');
5. TextReader.off('eventPanel');
6. } catch (e) {
7. console.error(`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}`);
8. }
```

## on( 'eventReadList')

PhonePC/2in1Tablet

on(type: 'eventReadList', callback: Callback<Array<ListEventState>>): void

注册播报列表相关事件监听，点击播报列表图标时，触发该回调执行。同一类型监听，注册多个回调函数，仅第一次注册有效。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'eventReadList'。 |
| callback | Callback<Array<[ListEventState](speech-textreader-api.md#listeventstate)>> | 是 | 播报列表发生相关事件时，触发该回调执行。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.on('eventReadList', (list: Array<TextReader.ListEventState>) => {
5. list.forEach((id) => {
6. console.info(`Succeeded in setting eventReadListListener, article id: ${id}`);
7. })
8. });
9. } catch (e) {
10. console.error(`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}`);
11. }
```

## off('eventReadList')

PhonePC/2in1Tablet

off(type: 'eventReadList', callback?: Callback<Array<ListEventState>>): void

在on(type: 'eventReadList')函数调用之后使用，用于注销播报列表相关事件的回调函数。注销监听后，可以重新注册。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'eventReadList'。 |
| callback | Callback<Array<[ListEventState](speech-textreader-api.md#listeventstate)>> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数是同一个，若不填，则取消当前应用监听该事件的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.off('eventReadList');
5. } catch (e) {
6. console.error(`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}`);
7. }
```

## on('readProgress')

PhonePC/2in1Tablet

on(type: 'readProgress', callback: Callback<ReadProgress>): void

注册已播放时长相关事件监听，已播放时长发生相关事件时，触发该回调执行。同一类型监听，注册多个回调函数，仅第一次注册有效。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'readProgress'。 |
| callback | Callback<[ReadProgress](speech-textreader-api.md#readprogress)> | 是 | 已播放时长发生相关事件时，触发该回调执行。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.on('readProgress', (readProgress: TextReader.ReadProgress) => {
5. console.info(`Succeeded in setting readProgressListener: ${JSON.stringify(readProgress)}`);
6. });
7. } catch (e) {
8. console.error(`TextReader failed to set readProgressListener. Code: ${e.code}, message: ${e.message}`);
9. }
```

## off('readProgress')

PhonePC/2in1Tablet

off(type: 'readProgress', callback?: Callback<ReadProgress>): void

在on(type: 'readProgress')函数调用之后使用，用于注销已播放时长相关事件的回调函数。注销监听后，可以重新注册。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'readProgress'。 |
| callback | Callback<[ReadProgress](speech-textreader-api.md#readprogress)> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数是同一个，若不填，则取消当前应用监听该事件的所有回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';

3. try {
4. TextReader.off('readProgress');
5. } catch (e) {
6. console.error(`TextReader failed to unset readProgressListener. Code: ${e.code}, message: ${e.message}`);
7. }
```

## Person

PhonePC/2in1Tablet

人物语气和风格信息

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.2(14)

| 名称 | **类型** | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| tone | number | 否 | 否 | 人物语气信息。  0：女声。 |
| style | string | 否 | 否 | 人物风格信息。  - reading：朗读风格。（暂不支持）  - interaction-oral：口语化风格。（暂不支持）  - interaction-broadcast：播音风格。 |

## ReaderParam

PhonePC/2in1Tablet

朗读参数

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

| 名称 | **类型** | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isVoiceBrandVisible | boolean | 否 | 否 | 是否显示播报品牌。  - 默认false：不显示品牌信息。  - 配置为true：显示品牌信息。 |
| businessBrandInfo | [BusinessBrandInfo](speech-textreader-api.md#businessbrandinfo) | 否 | 是 | 播报品牌信息。  - 默认是：小艺朗读。 |
| isFastForward | boolean | 否 | 是 | 快进快退逻辑。  - 默认false：上下一句切换。  - 配置为true：快进快退15秒。 |
| keepBackgroundRunning | boolean | 否 | 是 | 是否使用保持后台运行的功能。  预留参数，暂未支持。  - false：不保持后台运行。  - true：需要配置长时任务权限，具体请参见[开发指南步骤9](../harmonyos-guides/speech-textreader-guide.md#开发步骤)。 |
| online | number | 否 | 是 | 默认离线合成模式。  0为在线（暂不支持），1为离线。 |
| person | [Person](speech-textreader-api.md#person) | 否 | 是 | 朗读人员语气和风格信息，默认参数如下。  { tone: 0, style: 'interaction-broadcast' }  **起始版本：** 5.0.2(14) |
| isMinibarNeeded | boolean | 否 | 是 | 是否使用Minibar功能。  - 默认true：使用Minibar功能。  - 配置为false：不使用Minibar功能，这时hideMinibar、showMinibar 方法无效。  **起始版本：** 5.0.2(14) |
| minibarParams | [MinibarParams](speech-textreader-api.md#minibarparams) | 否 | 是 | Minibar位置设置，默认吸附左边。  **起始版本：** 5.0.2(14) |
| customFeatures | [CustomFeature[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-textreader-api#customfeature) | 否 | 是 | 朗读控件的自定义功能，默认空。  **起始版本：** 5.0.2(14) |
| displayTab | [DisplayTab](speech-textreader-api.md#displaytab) | 否 | 是 | 显示Tab页配置，默认显示封面和内容页。  **起始版本：** 5.0.2(14) |
| reportProgressPeriod | number | 否 | 是 | 多久返回一次已播放时长日志信息，默认为0，不回调。  单位：毫秒。  **起始版本：** 5.0.2(14) |

## StartParams

PhonePC/2in1Tablet

朗读控件起播参数

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.2(14)

| 名称 | **类型** | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isMinibarHidden | boolean | 否 | 是 | Minibar是否隐藏。  - 默认false：不隐藏Minibar。  - 配置为true：隐藏Minibar。  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| callbackParam | string | 否 | 是 | 用于三方自定义场景参数，在requestMore监听中返回，默认空。  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| startPercent | number | 否 | 是 | 指定起始播报位置，取值范围[0,100]，默认为0。  **元服务API：** 从版本6.0.1(21)开始，该接口支持在元服务中使用。  **起始版本：** 6.0.1(21) |

## MinibarParams

PhonePC/2in1Tablet

起播时控制Minibar的参数，可以设置Minibar初始化位置，以及与底部边框的距离。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.2(14)

| 名称 | **类型** | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| defaultAlignment | [BarAlignment](speech-textreader-api.md#baralignment) | 否 | 否 | Minibar默认吸附位置。  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| bottom | number | 否 | 是 | Minibar离底部边缘距离，垂直方向固定，仅支持左右拖动。  取值大于等于0，默认值为50，单位为vp，超过屏幕范围不显示Minibar。  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| isSpeedIconVisible | boolean | 否 | 是 | Minibar是否显示倍速播放按钮。  默认是true，显示播放按钮。  配置为false，不显示播放按钮。  **元服务API：** 从版本6.0.1(21)开始，该接口支持在元服务中使用。  **起始版本：** 6.0.1(21) |
| isNextIconVisible | boolean | 否 | 是 | Minibar是否显示下一篇按钮。  配置是true，显示下一篇按钮。  默认为false，不显示下一篇按钮。  **元服务API：** 从版本6.0.1(21)开始，该接口支持在元服务中使用。  **起始版本：** 6.0.1(21) |

## BusinessBrandInfo

PhonePC/2in1Tablet

播报品牌信息

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| panelName | string | 否 | 是 | - 播放面板顶部展示的业务名称，系统字体大小为标准时，英文占1个字符长度，中文占2个字符长度，累计超过24个字符长度时会省略显示。（系统字体大小有变动时，显示长度会有变化）  - Pura X设备不显示。 |
| panelIcon | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 播放面板顶部展示的业务图标。  预留参数，暂未支持。 |
| notificationIcon | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 通知栏展示的业务图标。  预留参数，暂未支持。 |
| notificationName | string | 否 | 是 | 通知栏展示的业务名称。  预留参数，暂未支持。 |

## ReadState

PhonePC/2in1Tablet

播报状态。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 文章id。 |
| state | [ReadStateCode](speech-readstatecode.md) | 否 | 否 | 当前的朗读状态。 |
| categoryId | string | 否 | 是 | 文章分类ID。  **起始版本：** 5.0.2(14) |
| isLastArticle | boolean | 否 | 是 | 分组播报情况时：  true表示是分组的最后一篇文章。  false则不是。  非分组播报情况时：  true表示是列表最后一篇文章。  false则不是。  **起始版本：** 5.0.2(14) |

## CustomFeature

PhonePC/2in1Tablet

朗读控件面板中的自定义功能。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.2(14)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [CustomFeatureType](speech-textreader-api.md#customfeaturetype) | 否 | 否 | 自定义特征的类型，系统应用或者用户自定义功能。 |
| name | string | 否 | 否 | 自定义特征的名称。  当type=CustomFeatureType.SYSTEM时，支持的系统特征名称包括：  - favorite（收藏）。  - countdown（定时器）。 |
| icon | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 自定义特性图标，支持url及本地资源。  默认为空。  当type=CustomFeatureType.SYSTEM时，系统特征为固定图标，不需要额外指定。 |
| callback | Callback<string> | 否 | 是 | 自定义特性的回调，回调参数为当前播放的文章id。 |

**示例：**

```
1. import { TextReader } from '@kit.SpeechKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. // 获取应用上下文
8. aboutToAppear() {
9. const customFeaturesToAdd: TextReader.CustomFeature[] = [
10. {
11. type: TextReader.CustomFeatureType.SYSTEM,
12. name: 'countdown',
13. icon: '',
14. callback: (id) => {
15. console.info(`Custom feature callback.`)
16. }
17. }
18. ]
19. const readerParams: TextReader.ReaderParam = {
20. // ... 其他字段配置
21. customFeatures: customFeaturesToAdd,
22. isVoiceBrandVisible: false
23. }
24. let context: Context | undefined = this.getUIContext().getHostContext();
25. if (context) {
26. TextReader.init(context, readerParams).then(() => {
27. console.info(`TextReader succeeded in initializing.`);
28. }).catch((e: BusinessError) => {
29. console.error(`TextReader failed to initialize. Code: ${e.code}, message: ${e.message}`);
30. })
31. }
32. }

34. build() {
35. // ...
36. }
37. }
```

## ReadInfo

PhonePC/2in1Tablet

朗读信息。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 文章标识ID，不能为空字符串。 |
| title | [TextInfo](speech-textreader-api.md#textinfo) | 否 | 否 | 标题。 |
| category | string | 否 | 是 | 类目，默认空。 |
| author | [TextInfo](speech-textreader-api.md#textinfo) | 否 | 是 | 文章的作者，默认空。 |
| date | [TextInfo](speech-textreader-api.md#textinfo) | 否 | 是 | 文章的时间（例:Mon Jul 08 2024 21:25:41 GMT+0800）。  预留参数，暂未支持。 |
| image | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 是 | 封面图图片。图片转为PixelMap后的最大大小为8MB。  若未传，采用默认封面图。 |
| imageUrl | string | 否 | 是 | 文章封面图片链接。  若未传，采用默认封面图。图片的宽高大于10242048时会进行压缩。  image和imageUrl同时存在的时候，image设置生效。  **起始版本：** 5.0.2(14) |
| bodyInfo | string | 否 | 是 | [setArticle](speech-textreader-api.md#setarticle)以及[loadMore](speech-textreader-api.md#loadmore)接口必填。  实时朗读的正文信息。  从6.1.0(23)版本开始，正文长度支持10000字符以上。6.0.2(22)及之前版本，正文中无标点符号和换行符的情况下，长度须小于等于10000字符。 |
| bodyInfoObject | [BodyInfo](speech-textreader-api.md#bodyinfo) | 否 | 是 | 正文内容信息，默认空。  **起始版本：** 5.0.2(14) |
| categoryObject | [CategoryInfo](speech-textreader-api.md#categoryinfo) | 否 | 是 | 文章分类信息，默认空。  **起始版本：** 5.0.2(14) |
| audioInfo | [AudioInfo](speech-textreader-api.md#audioinfo)[] | 否 | 是 | 音频信息，默认空。  若配置此参数，则优先使用传入音频进行播报。  **起始版本：** 5.0.2(14) |
| isFavorite | boolean | 否 | 是 | true表示已喜欢/收藏。  false表示不喜欢/未收藏。  默认false。  **起始版本：** 5.0.2(14) |

## CategoryInfo

PhonePC/2in1Tablet

文章分类信息

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 文章分类ID。 |
| name | string | 否 | 否 | 文章分类的名称。 |
| image | [image.PixelMap](arkts-apis-image-pixelmap.md) | string | 否 | 否 | 文章分类的图片或者图片的url，优先级大于文章封面图片。 |

## TextInfo

PhonePC/2in1Tablet

文字信息

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | string | 否 | 否 | 文本。 |
| isClickable | boolean | 否 | 否 | 是否支持点击收回播报面板。  - true：点击收回播报面板。  - false：点击不收回播报面板。 |

## BodyInfo

PhonePC/2in1Tablet

readInfo的正文内容信息

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [BodyInfoType](speech-textreader-api.md#bodyinfotype) | 否 | 否 | 类型。 |
| body | string | 否 | 是 | 正文内容，默认空。 |

## AudioInfo

PhonePC/2in1Tablet

朗读控件中的音频信息

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| format | string | 否 | 否 | 音频信息格式，如mp3、mp4a、wma、wav。 |
| duration | number | 否 | 否 | 音频信息的持续时间，单位：秒。 |
| size(deprecated) | number | 否 | 否 | 音频信息的大小，单位：字节。  **说明：**  从6.1.0(23)开始废弃。 |
| person | [Person](speech-textreader-api.md#person) | 否 | 是 | 音频信息的声音信息，包括音色、风格，语言等。  默认为如下参数  { tone: 3, style: 'interaction-broadcast' } |
| url | string | 否 | 否 | 音频信息的URL。 |

## ReadProgress

PhonePC/2in1Tablet

朗读控件中的音频信息

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.2(14)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 播报文章ID。  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| categoryId | string | 否 | 否 | 文章列表分组ID。  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| readProgressType | [ReadProgressType](speech-textreader-api.md#readprogresstype) | 否 | 否 | 定时上报类型。  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| person | [Person](speech-textreader-api.md#person) | 否 | 否 | 正在播报的文章使用的音色。  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| maxPercent | number | 否 | 否 | 触发该事件回调时，用户曾经播放的最大的百分比，而不是当前用户所处于的百分比  取值[0,100]。  【计算生成方式】  音频播放的最大百分比进度，四舍五入取整。例如音频播放到80%，拖动滚动条回到20%后停止播放，最终取值为80。  重播时重置。  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| currentPercent | number | 否 | 否 | 触发该事件回调时，返回用户当前播放的百分比，取值[0,100]。可用于记录上次播放位置，和[start](speech-textreader-api.md#start-1)接口配合实现下次继续播放。  **元服务API：** 从版本6.0.1(21)开始，该接口支持在元服务中使用。  **起始版本：** 6.0.1(21) |

## PanelEvent

PhonePC/2in1Tablet

播放面板事件

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 文章ID。 |
| click | string | 否 | 否 | - BPC\_01：播放按钮点击。  - BPC\_02：暂停按钮点击。  - BPC\_03：上一条按钮点击。  - BPC\_04：下一条按钮点击。  - BPC\_05：语速按钮点击。  - BPC\_06：音色按钮点击。  - BPC\_07：播报列表点击。  - BPC\_08：标题点击。  - BPC\_09：作者点击。  - BPC\_10：左上角箭头或下滑关掉。 |
| categoryId | string | 否 | 是 | 文章分类ID。  **起始版本：** 5.0.2(14) |

## NotificationEvent

PhonePC/2in1Tablet

通知栏事件

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 文章ID。 |
| type | number | 否 | 否 | 1：通知栏点击回调。  2：播控中心点击回调。 |
| click | string | 否 | 否 | - NBC\_01：播放按钮点击。  - NBC\_02：暂停按钮点击、移除通知栏播控中心。  - NBC\_03：关闭按钮点击（预留能力，暂未支持）。  - NBC\_04：上一条按钮点击。  - NBC\_05：下一条按钮点击。  - NBC\_06：文章图片点击（预留能力，暂未支持）。  - NBC\_07：文章标题点击（预留能力，暂未支持）。 |
| categoryId | string | 否 | 是 | 文章分类ID。  **起始版本：** 5.0.2(14) |

## ListEventState

PhonePC/2in1Tablet

列表事件状态

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 文章ID。 |
| categoryId | string | 否 | 是 | 文章分类ID。  **起始版本：** 5.0.2(14) |

## ResetParamType

PhonePC/2in1Tablet

用于确定重置类型的枚举类。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.2(14)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BAR\_PARAM | 1 | 重置Minibar参数。 |
| ALL | 2 | 重置所有本地数据，恢复为初始化配置参数，包括Minibar参数重置，文章列表置空。 |
| READ\_LIST | 3 | 重置文章列表。 |

## DisplayTab

PhonePC/2in1Tablet

用于确定播控面板显示的Tab标签及Tab内容的枚举类。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**设备行为差异：** 该接口在PC/2in1中无效果，在其他设备类型中可正常调用。

**起始版本：** 5.0.2(14)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COVER\_AND\_CONTENT | 1 | 显示封面页和内容页，并且显示Tab标签按钮。 |
| CONTENT | 2 | 仅显示内容页，不显示Tab标签按钮。 |
| COVER | 3 | 仅显示封面页，不显示Tab标签按钮。 |

## BarAlignment

PhonePC/2in1Tablet

用于确定Minibar默认吸附位置的枚举类。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.2(14)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LEFT | 1 | 吸附在左侧。 |
| RIGHT | 2 | 吸附在右侧。 |

## BodyInfoType

PhonePC/2in1Tablet

用于确定正文信息类型的枚举类。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.2(14)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONTENT | 1 | 正文内容类型。 |
| FILE\_PATH | 2 | 文件路径类型。 |

## CustomFeatureType

PhonePC/2in1Tablet

用于确定自定义特征类型的枚举类。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.2(14)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SYSTEM | 1 | 系统自定义功能。 |
| USER | 2 | 用户自定义功能。 |

## ReadProgressType

PhonePC/2in1Tablet

用于确定已播报时长上报类型的枚举类。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**起始版本：** 5.0.2(14)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PROGRESS | 1 | 播放中定时上报。 |
| PAUSE | 2 | 暂停时上报。 |
| STOP | 3 | 停止播放时上报。 |
| COMPLETED | 4 | 文章读完时上报。 |
