---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avmusictemplate-avmusictemplate
title: Class (AVMusicTemplate)
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > ArkTS API > @ohos.multimedia.avMusicTemplate (音频模板) > Class (AVMusicTemplate)
category: harmonyos-references
scraped_at: 2026-04-29T14:02:58+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:4f953904ae7feac630b07d3da5d03ccf04b18e31bd7d064198a3111331e6602f
---

调用[avMusicTemplate.createAVMusicTemplate](arkts-apis-avmusictemplate-f.md#avmusictemplatecreateavmusictemplate)获取实例后，可获取其ID，启动音频模板界面，并配置数据获取方法。随后，同步数据给模板控制方，以完成后续操作。

说明

* 本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块仅适用于API version 23及以上版本的Car设备。

## 导入模块

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';
```

## 属性

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sessionId | string | 否 | 否 | 音频模板唯一的标识。 |
| sessionTag | string | 否 | 否 | 音频模板标签。 |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private static sInstance: TemplateManager;

7. private constructor() {
8. }

10. /**
11. * 获取模板控制器实例。
12. *
13. * @returns 模板控制器实例。
14. */
15. public static getInstance(): TemplateManager {
16. if (!TemplateManager.sInstance) {
17. TemplateManager.sInstance = new TemplateManager();
18. }
19. return TemplateManager.sInstance;
20. };

22. /**
23. * 创建音频模板。
24. */
25. public createTemplate() {
26. if (this.template) {
27. console.warn('createTemplate: template not undefined');
28. return
29. }
30. this.template = avMusicTemplate.createAVMusicTemplate(avMusicTemplate.AVMusicTemplateType.DEFAULT);
31. console.info('Succeeded in creating template.');
32. }
33. }
```

## startTemplate

startTemplate(): Promise<OperResult>

启动音频模板界面。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[OperResult](arkts-apis-avmusictemplate-i.md#operresult)> | Promise对象，返回启动音频模板界面的操作结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 模拟开启模板。
8. */
9. public startTemplate() {
10. this.template?.startTemplate();
11. }
12. }
```

## onQueryMainTabs

onQueryMainTabs(callback: QueryMainTabsEvent): void

注册查询主标签的事件监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QueryMainTabsEvent](arkts-apis-avmusictemplate-t.md#querymaintabsevent) | 是 | 回调函数，返回查询主标签事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function onQueryMainTabs can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private queryMainTabsEvent: avMusicTemplate.QueryMainTabsEvent = async () => {
6. return new Promise<avMusicTemplate.MediaTab[]>(async (resolve, reject) => {
7. let tabs: avMusicTemplate.MediaTab[] = await this.getMainTabs();
8. resolve(tabs);
9. });
10. };

12. /**
13. * 注册监听。
14. */
15. private registerListener() {
16. this.template?.onQueryMainTabs(this.queryMainTabsEvent);
17. }

19. /**
20. * 模拟获取主界面的所有TAB。
21. *
22. * @returns Promise类型MediaTab数组。
23. */
24. private async getMainTabs(): Promise<avMusicTemplate.MediaTab[]> {
25. let homeTab: avMusicTemplate.MediaTab = {
26. tabId: 'home',
27. tabName: '首页'
28. };
29. let mineTab: avMusicTemplate.MediaTab = {
30. tabId: 'mine',
31. tabName: '我的'
32. };
33. let mainTabs: avMusicTemplate.MediaTab[] = [homeTab, mineTab];
34. return mainTabs;
35. };
36. }
```

## offQueryMainTabs

offQueryMainTabs(callback?: QueryMainTabsEvent): void

注销查询主标签事件监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QueryMainTabsEvent](arkts-apis-avmusictemplate-t.md#querymaintabsevent) | 否 | 查询主标签事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function offQueryMainTabs can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. this.template?.offQueryMainTabs();
11. }
12. }
```

## onQueryMediaTabContent

onQueryMediaTabContent(callback: QueryMediaTabContentEvent): void

注册查询媒体标签内容事件监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QueryMediaTabContentEvent](arkts-apis-avmusictemplate-t.md#querymediatabcontentevent) | 是 | 回调函数，返回查询媒体标签页内容的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function onQueryMediaTabContent can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private queryMediaTabContentEvent: avMusicTemplate.QueryMediaTabContentEvent = async (tabId: string) => {
6. return new Promise<avMusicTemplate.MediaTabContent>(async (resolve, reject) => {
7. let tabContent: avMusicTemplate.MediaTabContent = await this.createMediaTabContent();
8. resolve(tabContent);
9. });
10. };

12. /**
13. * 注册监听。
14. */
15. private registerListener() {
16. this.template?.onQueryMediaTabContent(this.queryMediaTabContentEvent);
17. }

19. /**
20. * 模拟获取TAB内容。
21. *
22. * @returns 标签页内容。
23. */
24. private async createMediaTabContent(): Promise<avMusicTemplate.MediaTabContent> {
25. let compilation: avMusicTemplate.Compilation = await this.createCompilation();
26. let mediaTabContent: avMusicTemplate.MediaTabContent = {
27. errorCode: 0,
28. tabId: 'tabId',
29. compilations: [compilation]
30. }
31. return mediaTabContent;
32. };

34. /**
35. * 模拟获取合集数据。
36. *
37. * @returns 合集。
38. */
39. private async createCompilation(): Promise<avMusicTemplate.Compilation> {
40. let mediaEntity: avMusicTemplate.MediaEntity = await this.createMediaEntity();
41. let compilation: avMusicTemplate.Compilation = {
42. errorCode: 0,
43. id: '',
44. title: '',
45. hasMoreData: false,
46. totalSize: 1,
47. memberMediaType: avMusicTemplate.EntityType.SINGLE,
48. topElements: [mediaEntity],
49. }
50. return compilation;
51. };

53. /**
54. * 模拟获取媒体数据。
55. *
56. * @returns 媒体数据。
57. */
58. private async createMediaEntity(): Promise<avMusicTemplate.MediaEntity> {
59. let mediaEntity: avMusicTemplate.MediaEntity = {
60. mediaId: 'mediaId',
61. mediaType: avMusicTemplate.EntityType.SINGLE,
62. parentId: 'parentId',
63. parentMediaType: avMusicTemplate.EntityType.SINGLE,
64. title: 'title',
65. imageUrl: 'imageUrl',
66. playState: avMusicTemplate.PlaybackState.PLAYBACK_STATE_PREPARE
67. };
68. return mediaEntity;
69. };
70. }
```

## offQueryMediaTabContent

offQueryMediaTabContent(callback?: QueryMediaTabContentEvent): void

取消查询媒体标签内容监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QueryMediaTabContentEvent](arkts-apis-avmusictemplate-t.md#querymediatabcontentevent) | 否 | 查询媒体标签页内容的事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function offQueryMediaTabContent can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. this.template?.offQueryMediaTabContent();
11. }
12. }
```

## onQueryMediaEntity

onQueryMediaEntity(callback: QueryMediaEntityEvent): void

注册查询媒体实体监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QueryMediaEntityEvent](arkts-apis-avmusictemplate-t.md#querymediaentityevent) | 是 | 回调函数，返回查询媒体实体的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function onQueryMediaEntity can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private queryMediaEntityEvent: avMusicTemplate.QueryMediaEntityEvent =
6. async (params: avMusicTemplate.QueryMediaEntityParam) => {
7. return new Promise<avMusicTemplate.PageMediaEntity>(async (resolve, reject) => {
8. let pageMediaEntity: avMusicTemplate.PageMediaEntity = await this.createPageMediaEntity();
9. resolve(pageMediaEntity);
10. });
11. };

13. /**
14. * 注册监听。
15. */
16. private registerListener() {
17. this.template?.onQueryMediaEntity(this.queryMediaEntityEvent);
18. }

20. /**
21. * 模拟获取PageMediaEntity。
22. *
23. * @returns PageMediaEntity实例。
24. */
25. private async createPageMediaEntity(): Promise<avMusicTemplate.PageMediaEntity> {
26. let mediaEntity: avMusicTemplate.MediaEntity = await this.createMediaEntity();
27. let pageMediaEntity: avMusicTemplate.PageMediaEntity = {
28. errorCode: 0,
29. pageIndex: 0,
30. pageSize: 1,
31. hasMoreData: false,
32. totalSize: 1,
33. memberMediaType: avMusicTemplate.EntityType.SINGLE,
34. elements: [mediaEntity]
35. }
36. return pageMediaEntity;
37. };

39. /**
40. * 模拟获取媒体数据。
41. *
42. * @returns 媒体数据。
43. */
44. private async createMediaEntity(): Promise<avMusicTemplate.MediaEntity> {
45. let mediaEntity: avMusicTemplate.MediaEntity = {
46. mediaId: 'mediaId',
47. mediaType: avMusicTemplate.EntityType.SINGLE,
48. parentId: 'parentId',
49. parentMediaType: avMusicTemplate.EntityType.SINGLE,
50. title: 'title',
51. imageUrl: 'imageUrl',
52. playState: avMusicTemplate.PlaybackState.PLAYBACK_STATE_PREPARE
53. };
54. return mediaEntity;
55. };
56. }
```

## offQueryMediaEntity

offQueryMediaEntity(callback?: QueryMediaEntityEvent): void

注销查询媒体实体监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QueryMediaEntityEvent](arkts-apis-avmusictemplate-t.md#querymediaentityevent) | 否 | 查询媒体实体的事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function offQueryMediaEntity can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. this.template?.offQueryMediaEntity();
11. }
12. }
```

## onQueryCompilation

onQueryCompilation(callback: QueryCompilationEvent): void

注册查询合集的监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QueryCompilationEvent](arkts-apis-avmusictemplate-t.md#querycompilationevent) | 是 | 回调函数，返回查询合集的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function onQueryCompilation can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private queryCompilationEvent: avMusicTemplate.QueryCompilationEvent =
6. async (compilationId: string, pageIndex: number) => {
7. return new Promise<avMusicTemplate.PageMediaEntity>(async (resolve, reject) => {
8. let pageMediaEntity: avMusicTemplate.PageMediaEntity = await this.createPageMediaEntity();
9. resolve(pageMediaEntity);
10. });
11. };

13. /**
14. * 注册监听。
15. */
16. private registerListener() {
17. this.template?.onQueryCompilation(this.queryCompilationEvent);
18. }

20. /**
21. * 模拟获取PageMediaEntity。
22. *
23. * @returns PageMediaEntity实例。
24. */
25. private async createPageMediaEntity(): Promise<avMusicTemplate.PageMediaEntity> {
26. let mediaEntity: avMusicTemplate.MediaEntity = await this.createMediaEntity();
27. let pageMediaEntity: avMusicTemplate.PageMediaEntity = {
28. errorCode: 0,
29. pageIndex: 0,
30. pageSize: 1,
31. hasMoreData: false,
32. totalSize: 1,
33. memberMediaType: avMusicTemplate.EntityType.SINGLE,
34. elements: [mediaEntity]
35. }
36. return pageMediaEntity;
37. };

39. /**
40. * 模拟获取媒体数据。
41. *
42. * @returns 媒体数据。
43. */
44. private async createMediaEntity(): Promise<avMusicTemplate.MediaEntity> {
45. let mediaEntity: avMusicTemplate.MediaEntity = {
46. mediaId: 'mediaId',
47. mediaType: avMusicTemplate.EntityType.SINGLE,
48. parentId: 'parentId',
49. parentMediaType: avMusicTemplate.EntityType.SINGLE,
50. title: 'title',
51. imageUrl: 'imageUrl',
52. playState: avMusicTemplate.PlaybackState.PLAYBACK_STATE_PREPARE
53. };
54. return mediaEntity;
55. };
56. }
```

## offQueryCompilation

offQueryCompilation(callback?: QueryCompilationEvent): void

注销查询合集的监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QueryCompilationEvent](arkts-apis-avmusictemplate-t.md#querycompilationevent) | 否 | 查询合集的事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function offQueryCompilation can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. this.template?.offQueryCompilation();
11. }
12. }
```

## onQueryPlaylist

onQueryPlaylist(callback: QueryPlaylistEvent): void

注册查询播放列表的监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QueryPlaylistEvent](arkts-apis-avmusictemplate-t.md#queryplaylistevent) | 是 | 回调函数，返回查询播放列表的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function onQueryPlaylist can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private queryPlaylistEvent: avMusicTemplate.QueryPlaylistEvent =
6. async (pageIndex: number, sort: avMusicTemplate.Sort) => {
7. return new Promise<avMusicTemplate.PageMediaEntity>(async (resolve, reject) => {
8. let pageMediaEntity: avMusicTemplate.PageMediaEntity = await this.createPageMediaEntity();
9. resolve(pageMediaEntity);
10. });
11. };

13. /**
14. * 注册监听。
15. */
16. private registerListener() {
17. this.template?.onQueryPlaylist(this.queryPlaylistEvent);
18. }

20. /**
21. * 模拟获取PageMediaEntity。
22. *
23. * @returns PageMediaEntity实例。
24. */
25. private async createPageMediaEntity(): Promise<avMusicTemplate.PageMediaEntity> {
26. let mediaEntity: avMusicTemplate.MediaEntity = await this.createMediaEntity();
27. let pageMediaEntity: avMusicTemplate.PageMediaEntity = {
28. errorCode: 0,
29. pageIndex: 0,
30. pageSize: 1,
31. hasMoreData: false,
32. totalSize: 1,
33. memberMediaType: avMusicTemplate.EntityType.SINGLE,
34. elements: [mediaEntity]
35. }
36. return pageMediaEntity;
37. };

39. /**
40. * 模拟获取媒体数据。
41. *
42. * @returns 媒体数据。
43. */
44. private async createMediaEntity(): Promise<avMusicTemplate.MediaEntity> {
45. let mediaEntity: avMusicTemplate.MediaEntity = {
46. mediaId: 'mediaId',
47. mediaType: avMusicTemplate.EntityType.SINGLE,
48. parentId: 'parentId',
49. parentMediaType: avMusicTemplate.EntityType.SINGLE,
50. title: 'title',
51. imageUrl: 'imageUrl',
52. playState: avMusicTemplate.PlaybackState.PLAYBACK_STATE_PREPARE
53. };
54. return mediaEntity;
55. };
56. }
```

## offQueryPlaylist

offQueryPlaylist(callback?: QueryPlaylistEvent): void

注销查询播放列表的监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QueryPlaylistEvent](arkts-apis-avmusictemplate-t.md#queryplaylistevent) | 否 | 查询播放列表的事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function offQueryPlaylist can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. this.template?.offQueryPlaylist();
11. }
12. }
```

## onQueryCurrentSingle

onQueryCurrentSingle(callback: QueryCurrentSingleEvent): void

注册查询当前单曲的监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QueryCurrentSingleEvent](arkts-apis-avmusictemplate-t.md#querycurrentsingleevent) | 是 | 回调函数，返回查询当前单曲的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function onQueryCurrentSingle can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private queryCurrentSingleEvent: avMusicTemplate.QueryCurrentSingleEvent = async () => {
6. return new Promise<avMusicTemplate.Single>(async (resolve, reject) => {
7. let single: avMusicTemplate.Single = await this.createCurrentSingle();
8. resolve(single);
9. });
10. };

12. /**
13. * 注册监听。
14. */
15. private registerListener() {
16. this.template?.onQueryCurrentSingle(this.queryCurrentSingleEvent);
17. }

19. /**
20. * 模拟获取当前单曲。
21. *
22. * @returns 当前单曲。
23. */
24. private async createCurrentSingle(): Promise<avMusicTemplate.Single> {
25. let playInfo: avMusicTemplate.PlayInfo = {
26. playCounts: '100w',
27. isSupportNext: true,
28. isSupportPrev: false,
29. isSupportQuickForward: true,
30. isSupportQuickBackward: true,
31. quickForwardStep: 10,
32. quickBackwardStep: 10,
33. isSupportSkipHead: false,
34. isSupportSkipTail: true,
35. isSupportPlayMode: true,
36. isSupportPlayRate: true,
37. supportedPlayRate: ['1', '2', '3'],
38. currentPlayRate: 'string;',
39. isSupportSoundQuality: false,
40. isSupportSoundEffect: true,
41. totalDuration: 60,
42. currentPlayDuration: 10,
43. isSupportProgress: false,
44. }
45. let favoriteData: avMusicTemplate.FavoriteData = {
46. isSupportFav: true,
47. isFavorite: false,
48. favCounts: '1000+'
49. }
50. let single: avMusicTemplate.Single = {
51. mediaId: 'mediaId',
52. mediaType: avMusicTemplate.EntityType.SINGLE,
53. parentId: 'parentId',
54. parentMediaType: avMusicTemplate.EntityType.SINGLE,
55. title: '歌曲标题',
56. desc: '歌曲描述',
57. imageUrl: '',
58. playState: 0,
59. isVip: false,
60. singer: '',
61. tags: [],
62. playInfo: playInfo,
63. favSubscribeData: favoriteData
64. }
65. return single;
66. };
67. }
```

## offQueryCurrentSingle

offQueryCurrentSingle(callback?: QueryCurrentSingleEvent): void

注销查询当前单曲的监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QueryCurrentSingleEvent](arkts-apis-avmusictemplate-t.md#querycurrentsingleevent) | 否 | 查询当前单曲的事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function offQueryCurrentSingle can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. this.template?.offQueryCurrentSingle();
11. }
12. }
```

## onQueryCompilationByKeyword

onQueryCompilationByKeyword(callback: QueryCompilationByKeywordEvent): void

注册按关键字查询合集的监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QueryCompilationByKeywordEvent](arkts-apis-avmusictemplate-t.md#querycompilationbykeywordevent) | 是 | 回调函数，返回按关键字查询合集的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function onQueryCompilationByKeyword can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private queryCompilationByKeywordEvent: avMusicTemplate.QueryCompilationByKeywordEvent = async (keyword: string) => {
6. return new Promise<avMusicTemplate.Compilation[]>(async (resolve, reject) => {
7. let compilation: avMusicTemplate.Compilation = await this.createCompilation();
8. let compilations: avMusicTemplate.Compilation[] = [compilation];
9. resolve(compilations);
10. });
11. };

13. /**
14. * 注册监听。
15. */
16. private registerListener() {
17. this.template?.onQueryCompilationByKeyword(this.queryCompilationByKeywordEvent);
18. }

20. /**
21. * 模拟获取合集数据。
22. *
23. * @returns 合集。
24. */
25. private async createCompilation(): Promise<avMusicTemplate.Compilation> {
26. let mediaEntity: avMusicTemplate.MediaEntity = await this.createMediaEntity();
27. let compilation: avMusicTemplate.Compilation = {
28. errorCode: 0,
29. id: '',
30. title: '',
31. hasMoreData: false,
32. totalSize: 1,
33. memberMediaType: avMusicTemplate.EntityType.SINGLE,
34. topElements: [mediaEntity],
35. }
36. return compilation;
37. };

39. /**
40. * 模拟获取媒体数据。
41. *
42. * @returns 媒体数据。
43. */
44. private async createMediaEntity(): Promise<avMusicTemplate.MediaEntity> {
45. let mediaEntity: avMusicTemplate.MediaEntity = {
46. mediaId: 'mediaId',
47. mediaType: avMusicTemplate.EntityType.SINGLE,
48. parentId: 'parentId',
49. parentMediaType: avMusicTemplate.EntityType.SINGLE,
50. title: 'title',
51. imageUrl: 'imageUrl',
52. playState: avMusicTemplate.PlaybackState.PLAYBACK_STATE_PREPARE
53. };
54. return mediaEntity;
55. };
56. }
```

## offQueryCompilationByKeyword

offQueryCompilationByKeyword(callback?: QueryCompilationByKeywordEvent): void

注销按关键字查询合集的监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QueryCompilationByKeywordEvent](arkts-apis-avmusictemplate-t.md#querycompilationbykeywordevent) | 否 | 按关键字查询合集的事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function offQueryCompilationByKeyword can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. this.template?.offQueryCompilationByKeyword();
11. }
12. }
```

## onQueryMediaEntityByKeyword

onQueryMediaEntityByKeyword(callback: QueryMediaEntityByKeywordEvent): void

注册按关键字查询媒体实体的监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QueryMediaEntityByKeywordEvent](arkts-apis-avmusictemplate-t.md#querymediaentitybykeywordevent) | 是 | 回调函数，返回按关键字查询媒体实体的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function onQueryMediaEntityByKeyword can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private queryMediaEntityByKeywordEvent: avMusicTemplate.QueryMediaEntityByKeywordEvent =
6. async (keyword: string, searchType: avMusicTemplate.EntityType, pageIndex: number) => {
7. return new Promise<avMusicTemplate.PageMediaEntity>(async (resolve, reject) => {
8. let pageMediaEntity: avMusicTemplate.PageMediaEntity = await this.createPageMediaEntity();
9. resolve(pageMediaEntity);
10. });
11. };

13. /**
14. * 注册监听。
15. */
16. private registerListener() {
17. this.template?.onQueryMediaEntityByKeyword(this.queryMediaEntityByKeywordEvent);
18. }

20. /**
21. * 模拟获取PageMediaEntity。
22. *
23. * @returns PageMediaEntity实例。
24. */
25. private async createPageMediaEntity(): Promise<avMusicTemplate.PageMediaEntity> {
26. let mediaEntity: avMusicTemplate.MediaEntity = await this.createMediaEntity();
27. let pageMediaEntity: avMusicTemplate.PageMediaEntity = {
28. errorCode: 0,
29. pageIndex: 0,
30. pageSize: 1,
31. hasMoreData: false,
32. totalSize: 1,
33. memberMediaType: avMusicTemplate.EntityType.SINGLE,
34. elements: [mediaEntity]
35. }
36. return pageMediaEntity;
37. };

39. /**
40. * 模拟获取媒体数据。
41. *
42. * @returns 媒体数据。
43. */
44. private async createMediaEntity(): Promise<avMusicTemplate.MediaEntity> {
45. let mediaEntity: avMusicTemplate.MediaEntity = {
46. mediaId: 'mediaId',
47. mediaType: avMusicTemplate.EntityType.SINGLE,
48. parentId: 'parentId',
49. parentMediaType: avMusicTemplate.EntityType.SINGLE,
50. title: 'title',
51. imageUrl: 'imageUrl',
52. playState: avMusicTemplate.PlaybackState.PLAYBACK_STATE_PREPARE
53. };
54. return mediaEntity;
55. };
56. }
```

## offQueryMediaEntityByKeyword

offQueryMediaEntityByKeyword(callback?: QueryMediaEntityByKeywordEvent): void

注销按关键字查询媒体实体的监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QueryMediaEntityByKeywordEvent](arkts-apis-avmusictemplate-t.md#querymediaentitybykeywordevent) | 否 | 按关键字查询媒体实体的事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function offQueryMediaEntityByKeyword can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. this.template?.offQueryMediaEntityByKeyword();
11. }
12. }
```

## onQueryRecommendMediaEntityList

onQueryRecommendMediaEntityList(callback: QueryRecommendMediaEntityListEvent): void

注册查询推荐媒体列表的监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QueryRecommendMediaEntityListEvent](arkts-apis-avmusictemplate-t.md#queryrecommendmediaentitylistevent) | 是 | 回调函数，返回查询推荐媒体列表的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function onQueryRecommendMediaEntityList can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private queryRecommendMediaEntityListEvent: avMusicTemplate.QueryRecommendMediaEntityListEvent = async () => {
6. return new Promise<avMusicTemplate.MediaEntity[]>(async (resolve, reject) => {
7. let mediaEntity: avMusicTemplate.MediaEntity = await this.createMediaEntity();
8. let mediaEntities: avMusicTemplate.MediaEntity[] = [mediaEntity];
9. resolve(mediaEntities);
10. });
11. };

13. /**
14. * 注册监听。
15. */
16. private registerListener() {
17. this.template?.onQueryRecommendMediaEntityList(this.queryRecommendMediaEntityListEvent);
18. }

20. /**
21. * 模拟获取媒体数据。
22. *
23. * @returns 媒体数据。
24. */
25. private async createMediaEntity(): Promise<avMusicTemplate.MediaEntity> {
26. let mediaEntity: avMusicTemplate.MediaEntity = {
27. mediaId: 'mediaId',
28. mediaType: avMusicTemplate.EntityType.SINGLE,
29. parentId: 'parentId',
30. parentMediaType: avMusicTemplate.EntityType.SINGLE,
31. title: 'title',
32. imageUrl: 'imageUrl',
33. playState: avMusicTemplate.PlaybackState.PLAYBACK_STATE_PREPARE
34. };
35. return mediaEntity;
36. };
37. }
```

## offQueryRecommendMediaEntityList

offQueryRecommendMediaEntityList(callback?: QueryRecommendMediaEntityListEvent): void

注销查询推荐媒体列表的监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QueryRecommendMediaEntityListEvent](arkts-apis-avmusictemplate-t.md#queryrecommendmediaentitylistevent) | 否 | 查询推荐媒体列表的事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function offQueryRecommendMediaEntityList can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. this.template?.offQueryRecommendMediaEntityList();
11. }
12. }
```

## onQueryHotWords

onQueryHotWords(callback: QueryHotWordsEvent): void

注册查询热词的监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QueryHotWordsEvent](arkts-apis-avmusictemplate-t.md#queryhotwordsevent) | 是 | 回调函数，返回查询热词的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function onQueryHotWords can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private queryHotWordsEvent: avMusicTemplate.QueryHotWordsEvent = async () => {
6. return new Promise<string[]>(async (resolve, reject) => {
7. let hotWords: string[] = ['热词1', '热词2', '热词3', '热词4', '热词5'];
8. resolve(hotWords);
9. });
10. };

12. /**
13. * 注册监听。
14. */
15. private registerListener() {
16. this.template?.onQueryHotWords(this.queryHotWordsEvent);
17. }
18. }
```

## offQueryHotWords

offQueryHotWords(callback?: QueryHotWordsEvent): void

注销查询热词的监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QueryHotWordsEvent](arkts-apis-avmusictemplate-t.md#queryhotwordsevent) | 否 | 查询热词的事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function offQueryHotWords can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. this.template?.offQueryHotWords();
11. }
12. }
```

## onQuerySearchHistory

onQuerySearchHistory(callback: QuerySearchHistoryEvent): void

注册查询搜索历史的监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QuerySearchHistoryEvent](arkts-apis-avmusictemplate-t.md#querysearchhistoryevent) | 是 | 回调函数，返回查询搜索历史的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function onQuerySearchHistory can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private querySearchHistoryEvent: avMusicTemplate.QuerySearchHistoryEvent = async () => {
6. return new Promise<string[]>(async (resolve, reject) => {
7. let searchHistory: string[] = ['搜索历史1', '搜索历史2', '搜索历史3', '搜索历史4', '搜索历史5'];
8. resolve(searchHistory);
9. });
10. };

12. /**
13. * 注册监听。
14. */
15. private registerListener() {
16. this.template?.onQuerySearchHistory(this.querySearchHistoryEvent);
17. }
18. }
```

## offQuerySearchHistory

offQuerySearchHistory(callback?: QuerySearchHistoryEvent): void

注销查询搜索历史的监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QuerySearchHistoryEvent](arkts-apis-avmusictemplate-t.md#querysearchhistoryevent) | 否 | 查询搜索历史的事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function offQuerySearchHistory can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. this.template?.offQuerySearchHistory();
11. }
12. }
```

## onClearSearchHistory

onClearSearchHistory(callback: ClearSearchHistoryEvent): void

注册清除搜索历史的监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ClearSearchHistoryEvent](arkts-apis-avmusictemplate-t.md#clearsearchhistoryevent) | 是 | 回调函数，返回清除搜索历史的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function onClearSearchHistory can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private clearSearchHistoryEvent: avMusicTemplate.ClearSearchHistoryEvent = async () => {
6. return new Promise<avMusicTemplate.OperResult>(async (resolve, reject) => {
7. let operResult: avMusicTemplate.OperResult = await this.createOperResult();
8. resolve(operResult);
9. });
10. };

12. /**
13. * 注册监听。
14. */
15. private registerListener() {
16. this.template?.onClearSearchHistory(this.clearSearchHistoryEvent);
17. }

19. /**
20. * 模拟操作结果。
21. *
22. * @returns 操作结果。
23. */
24. private async createOperResult(): Promise<avMusicTemplate.OperResult> {
25. let operResult: avMusicTemplate.OperResult = {
26. errorCode: 0,
27. }
28. return operResult;
29. };
30. }
```

## offClearSearchHistory

offClearSearchHistory(callback?: ClearSearchHistoryEvent): void

注销清除搜索历史的监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ClearSearchHistoryEvent](arkts-apis-avmusictemplate-t.md#clearsearchhistoryevent) | 否 | 清除搜索历史的事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function offClearSearchHistory can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. this.template?.offClearSearchHistory();
11. }
12. }
```

## onLogin

onLogin(callback: LoginEvent): void

注册登录事件的监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [LoginEvent](arkts-apis-avmusictemplate-t.md#loginevent) | 是 | 回调函数，返回登录事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function onLogin can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private loginEvent: avMusicTemplate.LoginEvent = async (controlType: avMusicTemplate.LoginType, id?: string) => {
6. return new Promise<avMusicTemplate.QrCodeInfo[]>(async (resolve, reject) => {
7. let qrCodeInfo: avMusicTemplate.QrCodeInfo = await this.createQrCodeInfo();
8. let qrCodeInfos: avMusicTemplate.QrCodeInfo[] = [qrCodeInfo];
9. resolve(qrCodeInfos);
10. });
11. };

13. /**
14. * 注册监听。
15. */
16. private registerListener() {
17. this.template?.onLogin(this.loginEvent);
18. }

20. /**
21. * 模拟创建二维码信息数组。
22. *
23. * @returns Promise类型的二维码信息数组。
24. */
25. private async createQrCodeInfo(): Promise<avMusicTemplate.QrCodeInfo> {
26. let qrCodeInfo: avMusicTemplate.QrCodeInfo = {
27. id: 'id',
28. price: '10',
29. titleName: 'title',
30. detailName: 'detail',
31. tips: 'tip',
32. content: 'content',
33. validPeriod: 1
34. };
35. return qrCodeInfo;
36. };
37. }
```

## offLogin

offLogin(callback?: LoginEvent): void

注销登录事件的监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [LoginEvent](arkts-apis-avmusictemplate-t.md#loginevent) | 否 | 登录事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function offLogin can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. this.template?.offLogin();
11. }
12. }
```

## onRequestDialogInfo

onRequestDialogInfo(callback: RequestDialogInfoEvent): void

注册请求对话框信息的监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [RequestDialogInfoEvent](arkts-apis-avmusictemplate-t.md#requestdialoginfoevent) | 是 | 回调函数，返回请求对话框信息的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function onRequestDialogInfo can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private requestDialogInfoEvent: avMusicTemplate.RequestDialogInfoEvent =
6. async (actionType: avMusicTemplate.DialogActionType, actionInfo?: avMusicTemplate.DialogActionInfo) => {
7. return new Promise<avMusicTemplate.DialogInfo>(async (resolve, reject) => {
8. let dialogInfo: avMusicTemplate.DialogInfo = await this.createDialogInfo();
9. resolve(dialogInfo);
10. });
11. };

13. /**
14. * 注册监听。
15. */
16. private registerListener() {
17. this.template?.onRequestDialogInfo(this.requestDialogInfoEvent);
18. }

20. /**
21. * 模拟对话框信息。
22. *
23. * @returns 对话框信息。
24. */
25. private async createDialogInfo(): Promise<avMusicTemplate.DialogInfo> {
26. let qrCodeInfo: avMusicTemplate.QrCodeInfo[] = [{
27. id: 'id',
28. price: '10',
29. titleName: 'title',
30. detailName: 'detail',
31. tips: 'tip',
32. content: 'content',
33. validPeriod: 1
34. }
35. ];
36. let dialogInfo: avMusicTemplate.DialogInfo = {
37. dialogId: 'dialogId',
38. dialogType: avMusicTemplate.DialogType.LOGIN,
39. qrCodes: qrCodeInfo
40. };
41. return dialogInfo;
42. };
43. }
```

## offRequestDialogInfo

offRequestDialogInfo(callback?: RequestDialogInfoEvent): void

注销请求对话框信息的监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [RequestDialogInfoEvent](arkts-apis-avmusictemplate-t.md#requestdialoginfoevent) | 否 | 请求对话框信息的事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function offRequestDialogInfo can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. this.template?.offRequestDialogInfo();
11. }
12. }
```

## onHandleMemberPurchase

onHandleMemberPurchase(callback: HandleMemberPurchaseEvent): void

注册处理购买会员事件的监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [HandleMemberPurchaseEvent](arkts-apis-avmusictemplate-t.md#handlememberpurchaseevent) | 是 | 回调函数，返回处理购买会员的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function onHandleMemberPurchase can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private handleMemberPurchaseEvent: avMusicTemplate.HandleMemberPurchaseEvent =
6. async (info: avMusicTemplate.MemberPurchaseInfo) => {
7. return new Promise<avMusicTemplate.DialogInfo>(async (resolve, reject) => {
8. let dialogInfo: avMusicTemplate.DialogInfo = await this.createDialogInfo();
9. resolve(dialogInfo);
10. });
11. };

13. /**
14. * 注册监听。
15. */
16. private registerListener() {
17. this.template?.onHandleMemberPurchase(this.handleMemberPurchaseEvent);
18. }

20. /**
21. * 模拟对话框信息。
22. *
23. * @returns 对话框信息。
24. */
25. private async createDialogInfo(): Promise<avMusicTemplate.DialogInfo> {
26. let qrCodeInfo: avMusicTemplate.QrCodeInfo[] = [{
27. id: 'id',
28. price: '10',
29. titleName: 'title',
30. detailName: 'detail',
31. tips: 'tip',
32. content: 'content',
33. validPeriod: 1
34. }
35. ];
36. let dialogInfo: avMusicTemplate.DialogInfo = {
37. dialogId: 'dialogId',
38. dialogType: avMusicTemplate.DialogType.LOGIN,
39. qrCodes: qrCodeInfo
40. };
41. return dialogInfo;
42. };
43. }
```

## offHandleMemberPurchase

offHandleMemberPurchase(callback?: HandleMemberPurchaseEvent): void

注销处理购买会员事件的监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [HandleMemberPurchaseEvent](arkts-apis-avmusictemplate-t.md#handlememberpurchaseevent) | 否 | 处理购买会员的事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function offHandleMemberPurchase can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. this.template?.offHandleMemberPurchase();
11. }
12. }
```

## onQueryMemberPurchase

onQueryMemberPurchase(callback: QueryMemberPurchaseEvent): void

注册查询购买会员事件的监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QueryMemberPurchaseEvent](arkts-apis-avmusictemplate-t.md#querymemberpurchaseevent) | 是 | 回调函数，返回查询购买会员的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function onQueryMemberPurchase can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private queryMemberPurchaseEvent: avMusicTemplate.QueryMemberPurchaseEvent =
6. async (memberPurchaseType: avMusicTemplate.MemberPurchaseType) => {
7. return new Promise<avMusicTemplate.MemberPurchaseInfo[]>(async (resolve, reject) => {
8. let memberPurchaseInfo: avMusicTemplate.MemberPurchaseInfo = await this.createQueryMemberPurchase();
9. let memberPurchaseInfos: avMusicTemplate.MemberPurchaseInfo[] = [memberPurchaseInfo];
10. resolve(memberPurchaseInfos);
11. });
12. };

14. /**
15. * 注册监听。
16. */
17. private registerListener() {
18. this.template?.onQueryMemberPurchase(this.queryMemberPurchaseEvent);
19. }

21. /**
22. * 模拟查询会员购买信息。
23. *
24. * @returns Promise类型的购买会员信息数组。
25. */
26. private async createQueryMemberPurchase(): Promise<avMusicTemplate.MemberPurchaseInfo> {
27. let memberPurchaseInfo: avMusicTemplate.MemberPurchaseInfo = {
28. id: 'id',
29. diagramUrl: 'diagramUrl',
30. diagramContent: 'diagramContent',
31. memberPurchaseType: avMusicTemplate.MemberPurchaseType.NORMAL
32. };
33. return memberPurchaseInfo;
34. };
35. }
```

## offQueryMemberPurchase

offQueryMemberPurchase(callback?: QueryMemberPurchaseEvent): void

注销查询购买会员事件的监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QueryMemberPurchaseEvent](arkts-apis-avmusictemplate-t.md#querymemberpurchaseevent) | 否 | 查询购买会员的事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function offQueryMemberPurchase can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. this.template?.offQueryMemberPurchase();
11. }
12. }
```

## onQueryCustomContent

onQueryCustomContent(callback: QueryCustomContentEvent): void

注册查询自定义内容事件的监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QueryCustomContentEvent](arkts-apis-avmusictemplate-t.md#querycustomcontentevent) | 是 | 回调函数，返回查询自定义内容的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function onQueryCustomContent can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private queryCustomContentEvent: avMusicTemplate.QueryCustomContentEvent =
6. async (queryTypes: avMusicTemplate.CustomType[]) => {
7. return new Promise<avMusicTemplate.CustomElement>(async (resolve, reject) => {
8. let customElement: avMusicTemplate.CustomElement = await this.createCustomContent();
9. resolve(customElement);
10. });
11. };

13. /**
14. * 注册监听。
15. */
16. private registerListener() {
17. this.template?.onQueryCustomContent(this.queryCustomContentEvent);
18. }

20. /**
21. * 模拟获取自定义内容。
22. *
23. * @returns 自定义元素。
24. */
25. private async createCustomContent(): Promise<avMusicTemplate.CustomElement> {
26. let mediaEntity: avMusicTemplate.MediaEntity = {
27. mediaId: 'mediaId',
28. mediaType: avMusicTemplate.EntityType.SINGLE,
29. parentId: 'parentId',
30. parentMediaType: avMusicTemplate.EntityType.SINGLE,
31. title: 'title',
32. imageUrl: 'imageUrl',
33. playState: avMusicTemplate.PlaybackState.PLAYBACK_STATE_PREPARE
34. }
35. let compilation: avMusicTemplate.Compilation = {
36. errorCode: 0,
37. errorMsg: 'success',
38. id: 'id',
39. title: 'title',
40. hasMoreData: false,
41. totalSize: 1,
42. memberMediaType: avMusicTemplate.EntityType.SINGLE,
43. topElements: [mediaEntity]
44. };
45. let customElement: avMusicTemplate.CustomElement = {
46. errorCode: 0,
47. customCompilations: [compilation],
48. };
49. return customElement;
50. };
51. }
```

## offQueryCustomContent

offQueryCustomContent(callback?: QueryCustomContentEvent): void

注销查询自定义内容事件的监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QueryCustomContentEvent](arkts-apis-avmusictemplate-t.md#querycustomcontentevent) | 否 | 查询自定义内容的事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function offQueryCustomContent can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. this.template?.offQueryCustomContent();
11. }
12. }
```

## onDownloadMediaEntity

onDownloadMediaEntity(callback: DownloadMediaEntityEvent): void

注册下载媒体实体事件的监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [DownloadMediaEntityEvent](arkts-apis-avmusictemplate-t.md#downloadmediaentityevent) | 是 | 回调函数，返回下载媒体实体的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function onDownloadMediaEntity can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private downloadMediaEntityEvent: avMusicTemplate.DownloadMediaEntityEvent =
6. async (controlType: avMusicTemplate.DownloadControlType, mediaEntity: avMusicTemplate.MediaEntity) => {
7. return new Promise<avMusicTemplate.OperResult>(async (resolve, reject) => {
8. let operResult: avMusicTemplate.OperResult = await this.createOperResult();
9. this.downloadMediaEntity(mediaEntity);
10. resolve(operResult);
11. });
12. };

14. /**
15. * 注册监听。
16. */
17. private registerListener() {
18. this.template?.onDownloadMediaEntity(this.downloadMediaEntityEvent);
19. }

21. /**
22. * 下载状态，进度刷新。
23. */
24. public setDownloadMediaEntityStatus(mediaEntity: avMusicTemplate.MediaEntity) {
25. this.template?.setDownloadMediaEntityStatus(mediaEntity);
26. };

28. /**
29. * 模拟设置改变。
30. *
31. * @returns Promise类型的设置条目。
32. */
33. /**
34. * 模拟操作结果。
35. *
36. * @returns 操作结果。
37. */
38. private async createOperResult(): Promise<avMusicTemplate.OperResult> {
39. let operResult: avMusicTemplate.OperResult = {
40. errorCode: 0,
41. }
42. return operResult;
43. };

45. /**
46. * 模拟下载过程。
47. *
48. * @param mediaEntity 媒体实体。
49. */
50. private async downloadMediaEntity(mediaEntity: avMusicTemplate.MediaEntity) {
51. // 下载完成之后。
52. this.setDownloadMediaEntityStatus(mediaEntity);
53. };
54. }
```

## offDownloadMediaEntity

offDownloadMediaEntity(callback?: DownloadMediaEntityEvent): void

注销下载媒体实体事件的监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [DownloadMediaEntityEvent](arkts-apis-avmusictemplate-t.md#downloadmediaentityevent) | 否 | 下载媒体实体的事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function offDownloadMediaEntity can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. this.template?.offDownloadMediaEntity();
11. }
12. }
```

## onSettingsChange

onSettingsChange(callback: SettingsChangeEvent): void

注册设置改变事件的监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [SettingsChangeEvent](arkts-apis-avmusictemplate-t.md#settingschangeevent) | 是 | 回调函数，返回设置改变的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function onSettingsChange can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private settingsChangeEvent: avMusicTemplate.SettingsChangeEvent =
6. async (settingItem: avMusicTemplate.SettingItem) => {
7. return new Promise<avMusicTemplate.SettingItem>(async (resolve, reject) => {
8. let settingItem: avMusicTemplate.SettingItem = await this.settingsChange();
9. resolve(settingItem);
10. });
11. };

13. /**
14. * 注册监听。
15. */
16. private registerListener() {
17. this.template?.onSettingsChange(this.settingsChangeEvent);
18. }

20. /**
21. * 模拟设置改变。
22. *
23. * @returns Promise类型的设置条目。
24. */
25. private async settingsChange(): Promise<avMusicTemplate.SettingItem> {
26. let setting: avMusicTemplate.SettingItem = {
27. id: 'id',
28. title: 'title',
29. desc: 'desc',
30. mediaId: 'mediaId',
31. settingType: avMusicTemplate.SettingType.SWITCH,
32. settingValue: false
33. }
34. return setting;
35. };
36. }
```

## offSettingsChange

offSettingsChange(callback?: SettingsChangeEvent): void

注销设置改变事件的监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [SettingsChangeEvent](arkts-apis-avmusictemplate-t.md#settingschangeevent) | 否 | 设置改变的事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function offSettingsChange can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. this.template?.offSettingsChange();
11. }
12. }
```

## onProblemAndAdvice

onProblemAndAdvice(callback: ProblemAndAdviceEvent): void

注册问题与建议事件的监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ProblemAndAdviceEvent](arkts-apis-avmusictemplate-t.md#problemandadviceevent) | 是 | 回调函数，返回问题与建议的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function onProblemAndAdvice can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private problemAndAdviceEvent: avMusicTemplate.ProblemAndAdviceEvent = async (advice: string) => {
6. return new Promise<avMusicTemplate.OperResult>(async (resolve, reject) => {
7. let operResult: avMusicTemplate.OperResult = await this.createOperResult();
8. resolve(operResult);
9. });
10. };

12. /**
13. * 注册监听。
14. */
15. private registerListener() {
16. this.template?.onProblemAndAdvice(this.problemAndAdviceEvent);
17. }

19. /**
20. * 模拟操作结果。
21. *
22. * @returns 操作结果。
23. */
24. private async createOperResult(): Promise<avMusicTemplate.OperResult> {
25. let operResult: avMusicTemplate.OperResult = {
26. errorCode: 0,
27. }
28. return operResult;
29. };
30. }
```

## offProblemAndAdvice

offProblemAndAdvice(callback?: ProblemAndAdviceEvent): void

注销问题与建议事件的监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ProblemAndAdviceEvent](arkts-apis-avmusictemplate-t.md#problemandadviceevent) | 否 | 处理问题与建议的回调。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function offProblemAndAdvice can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. this.template?.offProblemAndAdvice();
11. }
12. }
```

## onPlayForSearch

onPlayForSearch(callback: PlayForSearchEvent): void

注册搜播事件的监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [PlayForSearchEvent](arkts-apis-avmusictemplate-t.md#playforsearchevent) | 是 | 回调函数，返回搜播的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function onPlayForSearch can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private playForSearchEvent: avMusicTemplate.PlayForSearchEvent = async (command: avMusicTemplate.SearchPlayInfoType,
6. args: avMusicTemplate.SearchPlayInfo) => {
7. return new Promise<avMusicTemplate.OperResult>(async (resolve, reject) => {
8. let operResult: avMusicTemplate.OperResult = await this.createOperResult();
9. resolve(operResult);
10. });
11. };

13. /**
14. * 注册监听。
15. */
16. private registerListener() {
17. this.template?.onPlayForSearch(this.playForSearchEvent);
18. }

20. /**
21. * 模拟操作结果。
22. *
23. * @returns 操作结果。
24. */
25. private async createOperResult(): Promise<avMusicTemplate.OperResult> {
26. let operResult: avMusicTemplate.OperResult = {
27. errorCode: 0,
28. }
29. return operResult;
30. };
31. }
```

## offPlayForSearch

offPlayForSearch(callback?: PlayForSearchEvent): void

注销搜播事件的监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [PlayForSearchEvent](arkts-apis-avmusictemplate-t.md#playforsearchevent) | 否 | 搜播的事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function offPlayForSearch can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. this.template?.offPlayForSearch();
11. }
12. }
```

## onExecuteAction

onExecuteAction(callback: ExecuteActionEvent): void

注册执行操作事件的监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ExecuteActionEvent](arkts-apis-avmusictemplate-t.md#executeactionevent) | 是 | 回调函数，返回执行操作的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function onExecuteAction can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private executeActionEvent: avMusicTemplate.ExecuteActionEvent = async (actionType: string, params: string) => {
6. return new Promise<string>(async (resolve, reject) => {
7. let result: string = 'success';
8. resolve(result);
9. });
10. };

12. /**
13. * 注册监听。
14. */
15. private registerListener() {
16. this.template?.onExecuteAction(this.executeActionEvent);
17. }
18. }
```

## offExecuteAction

offExecuteAction(callback?: ExecuteActionEvent): void

注销执行操作事件的监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ExecuteActionEvent](arkts-apis-avmusictemplate-t.md#executeactionevent) | 否 | 执行操作的事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function offExecuteAction can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. this.template?.offExecuteAction();
11. }
12. }
```

## onPlayMediaEntity

onPlayMediaEntity(callback: PlayMediaEntityEvent): void

注册播放媒体实体事件的监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [PlayMediaEntityEvent](arkts-apis-avmusictemplate-t.md#playmediaentityevent) | 是 | 回调函数，返回播放媒体实体的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function onPlayMediaEntity can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private playMediaEntityEvent: avMusicTemplate.PlayMediaEntityEvent =
6. async (mediaEntity: avMusicTemplate.MediaEntity) => {
7. console.info('playMediaEntity');
8. };

10. /**
11. * 注册监听。
12. */
13. private registerListener() {
14. this.template?.onPlayMediaEntity(this.playMediaEntityEvent);
15. }
16. }
```

## offPlayMediaEntity

offPlayMediaEntity(callback?: PlayMediaEntityEvent): void

注销播放媒体实体事件的监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [PlayMediaEntityEvent](arkts-apis-avmusictemplate-t.md#playmediaentityevent) | 否 | 播放媒体实体的事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function offPlayMediaEntity can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. this.template?.offPlayMediaEntity();
11. }
12. }
```

## onFavoriteMediaEntity

onFavoriteMediaEntity(callback: FavoriteMediaEntityEvent): void

注册收藏媒体实体事件的监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [FavoriteMediaEntityEvent](arkts-apis-avmusictemplate-t.md#favoritemediaentityevent) | 是 | 回调函数，返回收藏媒体实体的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function onFavoriteMediaEntity can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private favoriteMediaEntityEvent: avMusicTemplate.FavoriteMediaEntityEvent =
6. async (actionType: avMusicTemplate.MediaFavoriteType, mediaEntity: avMusicTemplate.MediaEntity) => {
7. return new Promise<avMusicTemplate.OperResult>(async (resolve, reject) => {
8. let operResult: avMusicTemplate.OperResult = await this.createOperResult();
9. resolve(operResult);
10. });
11. };

13. /**
14. * 注册监听。
15. */
16. private registerListener() {
17. this.template?.onFavoriteMediaEntity(this.favoriteMediaEntityEvent);
18. }

20. /**
21. * 模拟操作结果。
22. *
23. * @returns 操作结果。
24. */
25. private async createOperResult(): Promise<avMusicTemplate.OperResult> {
26. let operResult: avMusicTemplate.OperResult = {
27. errorCode: 0,
28. }
29. return operResult;
30. };
31. }
```

## offFavoriteMediaEntity

offFavoriteMediaEntity(callback?: FavoriteMediaEntityEvent): void

注销收藏媒体实体事件的监听。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [FavoriteMediaEntityEvent](arkts-apis-avmusictemplate-t.md#favoritemediaentityevent) | 否 | 收藏媒体实体的事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function offFavoriteMediaEntity can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. this.template?.offFavoriteMediaEntity();
11. }
12. }
```

## setUserInfo

setUserInfo(userInfo: UserInfo): Promise<void>

向音频模板控制方同步用户信息。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userInfo | [UserInfo](arkts-apis-avmusictemplate-i.md#userinfo) | 是 | 用户信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function setUserInfo can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000011 | The data write error, data is invalid. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. private isLogin: boolean = false;

7. /**
8. * 模拟登录状态改变。
9. *
10. * @param isLogin 是否登录。
11. */
12. public setLoginState(isLogin: boolean) {
13. this.isLogin = isLogin;
14. this.setUserInfo();
15. }

17. /**
18. * 用户信息发生变化后通知界面刷新用户信息，如登陆账号后。
19. */
20. public setUserInfo() {
21. let userInfo: avMusicTemplate.UserInfo = {
22. userInfoId: this.isLogin ? 'userInfoId' : '',
23. nickName: this.isLogin ? '昵称' : '',
24. profilePicUrl: this.isLogin ? 'profilePicUrl' : '',
25. tips: this.isLogin ? 'tips' : '',
26. isLogin: this.isLogin,
27. isVip: false
28. };
29. this.template?.setUserInfo(userInfo);
30. };
31. }
```

## setDialogCommand

setDialogCommand(type: DialogControlType, dialogInfo: DialogInfo): Promise<void>

向音频模板控制方同步对话框命令。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [DialogControlType](arkts-apis-avmusictemplate-t.md#dialogcontroltype) | 是 | 对话框控制类型。 |
| dialogInfo | [DialogInfo](arkts-apis-avmusictemplate-i.md#dialoginfo) | 是 | 对话框信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function setDialogCommand can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000011 | The data write error, data is invalid. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 对话框相关的操作，如：打开，关闭。
8. */
9. public setDialogCommand() {
10. let type: avMusicTemplate.DialogControlType = 'open';
11. let qrCodeInfo: avMusicTemplate.QrCodeInfo[] = [{
12. id: 'id',
13. price: '10',
14. titleName: 'title',
15. detailName: 'detail',
16. tips: 'tip',
17. content: 'content',
18. validPeriod: 1
19. }];
20. let dialogInfo: avMusicTemplate.DialogInfo = {
21. dialogId: 'dialogId',
22. dialogType: avMusicTemplate.DialogType.LOGIN,
23. qrCodes: qrCodeInfo
24. };
25. this.template?.setDialogCommand(type, dialogInfo);
26. };
27. }
```

## setCurrentSingle

setCurrentSingle(single: Single): Promise<void>

向音频模板控制方同步当前单曲。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| single | [Single](arkts-apis-avmusictemplate-i.md#single) | 是 | 当前单曲。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function setCurrentSingle can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000011 | The data write error, data is invalid. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. public async setCurrentSingle() {
7. let single: avMusicTemplate.Single = await this.createCurrentSingle()
8. this.template?.setCurrentSingle(single);
9. };

11. /**
12. * 模拟获取当前单曲。
13. *
14. * @returns 当前单曲。
15. */
16. private async createCurrentSingle(): Promise<avMusicTemplate.Single> {
17. let playInfo: avMusicTemplate.PlayInfo = {
18. playCounts: '100w',
19. isSupportNext: true,
20. isSupportPrev: false,
21. isSupportQuickForward: true,
22. isSupportQuickBackward: true,
23. quickForwardStep: 10,
24. quickBackwardStep: 10,
25. isSupportSkipHead: false,
26. isSupportSkipTail: true,
27. isSupportPlayMode: true,
28. isSupportPlayRate: true,
29. supportedPlayRate: ['1', '2', '3'],
30. currentPlayRate: 'string;',
31. isSupportSoundQuality: false,
32. isSupportSoundEffect: true,
33. totalDuration: 60,
34. currentPlayDuration: 10,
35. isSupportProgress: false,
36. }
37. let favoriteData: avMusicTemplate.FavoriteData = {
38. isSupportFav: true,
39. isFavorite: false,
40. favCounts: '1000+'
41. }
42. let single: avMusicTemplate.Single = {
43. mediaId: 'mediaId',
44. mediaType: avMusicTemplate.EntityType.SINGLE,
45. parentId: 'parentId',
46. parentMediaType: avMusicTemplate.EntityType.SINGLE,
47. title: '歌曲标题',
48. desc: '歌曲描述',
49. imageUrl: '',
50. playState: 0,
51. isVip: false,
52. singer: '',
53. tags: [],
54. playInfo: playInfo,
55. favSubscribeData: favoriteData
56. }
57. return single;
58. };
59. }
```

## setMediaEntities

setMediaEntities(entities: MediaEntity[]): Promise<void>

向音频模板控制方同步媒体资源变更信息。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| entities | [MediaEntity](arkts-apis-avmusictemplate-i.md#mediaentity)[] | 是 | 媒体实体的数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function setMediaEntities can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000011 | The data write error, data is invalid. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 媒体播放后信息后，如：歌单的播放状态。
8. */
9. public setMediaEntities() {
10. let mediaEntities: avMusicTemplate.MediaEntity[] = [{
11. mediaId: 'mediaId',
12. mediaType: avMusicTemplate.EntityType.SINGLE,
13. parentId: 'parentId',
14. parentMediaType: avMusicTemplate.EntityType.SINGLE,
15. title: 'title',
16. imageUrl: 'imageUrl',
17. playState: avMusicTemplate.PlaybackState.PLAYBACK_STATE_PREPARE
18. }];
19. this.template?.setMediaEntities(mediaEntities);
20. };
21. }
```

## setTabContent

setTabContent(tabId: string, tabContent: MediaTabContent): Promise<void>

向音频模板控制方同步标签页内容信息。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tabId | string | 是 | 标签的ID。 |
| tabContent | [MediaTabContent](arkts-apis-avmusictemplate-i.md#mediatabcontent) | 是 | 媒体标签页内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function setTabContent can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000011 | The data write error, data is invalid. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;
5. /**
6. * 某个tab页签下的内容发生变化后通知界面刷新。
7. */
8. public setTabContent() {
9. let mediaEntity: avMusicTemplate.MediaEntity[] = [{
10. mediaId: 'mediaId',
11. mediaType: avMusicTemplate.EntityType.SINGLE,
12. parentId: 'parentId',
13. parentMediaType: avMusicTemplate.EntityType.SINGLE,
14. title: 'title',
15. imageUrl: 'imageUrl',
16. playState: avMusicTemplate.PlaybackState.PLAYBACK_STATE_PREPARE
17. }]
18. let compilation: avMusicTemplate.Compilation[] = [{
19. errorCode: 0,
20. errorMsg: 'success',
21. id: 'id',
22. title: 'title',
23. hasMoreData: true,
24. totalSize: 2,
25. memberMediaType: avMusicTemplate.EntityType.SINGLE,
26. topElements: mediaEntity
27. }]
28. let mediaTabContent: avMusicTemplate.MediaTabContent = {
29. errorCode: 0,
30. errorMsg: 'success',
31. tabId: 'tabId',
32. compilations: compilation
33. }
34. this.template?.setTabContent('tabId', mediaTabContent);
35. };
36. }
```

## setPlaylist

setPlaylist(playlist: PageMediaEntity): Promise<void>

向音频模板控制方同步播放列表。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| playlist | [PageMediaEntity](arkts-apis-avmusictemplate-i.md#pagemediaentity) | 是 | 分页媒体实体。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function setPlaylist can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000011 | The data write error, data is invalid. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 播放列表发送变化后通知界面刷新。
8. */
9. public setPlaylist() {
10. let mediaEntity: avMusicTemplate.MediaEntity = {
11. mediaId: 'mediaId',
12. mediaType: avMusicTemplate.EntityType.SINGLE,
13. parentId: 'parentId',
14. parentMediaType: avMusicTemplate.EntityType.SINGLE,
15. title: 'title',
16. imageUrl: 'imageUrl',
17. playState: avMusicTemplate.PlaybackState.PLAYBACK_STATE_PREPARE
18. }
19. let pageMediaEntity: avMusicTemplate.PageMediaEntity = {
20. errorCode: 0,
21. errorMsg: 'success',
22. pageIndex: 0,
23. pageSize: 1,
24. hasMoreData: true,
25. totalSize: 2,
26. memberMediaType: avMusicTemplate.EntityType.SINGLE,
27. elements: [mediaEntity]
28. }
29. this.template?.setPlaylist(pageMediaEntity);
30. };
31. }
```

## setDownloadMediaEntityStatus

setDownloadMediaEntityStatus(single: MediaEntity): Promise<void>

向音频模板控制方同步单曲下载状态信息。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| single | [MediaEntity](arkts-apis-avmusictemplate-i.md#mediaentity) | 是 | 媒体实体。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function setDownloadMediaEntityStatus can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000011 | The data write error, data is invalid. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 下载状态，进度刷新。
8. */
9. public setDownloadMediaEntityStatus(mediaEntity: avMusicTemplate.MediaEntity) {
10. this.template?.setDownloadMediaEntityStatus(mediaEntity);
11. };

13. /**
14. * 模拟下载过程。
15. *
16. * @param mediaEntity 媒体实体。
17. */
18. private async downloadMediaEntity(mediaEntity: avMusicTemplate.MediaEntity) {
19. // 下载完成之后。
20. this.setDownloadMediaEntityStatus(mediaEntity);
21. };
22. }
```

## setCustomElements

setCustomElements(actionType: ActionType, customType: CustomType, customElement: CustomElement): Promise<void>

向音频模板控制方同步自定义元素变更信息。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| actionType | [ActionType](arkts-apis-avmusictemplate-t.md#actiontype) | 是 | 操作类型。 |
| customType | [CustomType](arkts-apis-avmusictemplate-t.md#customtype) | 是 | 自定义类型。 |
| customElement | [CustomElement](arkts-apis-avmusictemplate-i.md#customelement) | 是 | 自定义元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function setCustomElements can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000011 | The data write error, data is invalid. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 自定义数据发生变化后通知。
8. */
9. public setCustomElements() {
10. let mediaEntity: avMusicTemplate.MediaEntity = {
11. mediaId: 'mediaId',
12. mediaType: avMusicTemplate.EntityType.SINGLE,
13. parentId: 'parentId',
14. parentMediaType: avMusicTemplate.EntityType.SINGLE,
15. title: 'title',
16. imageUrl: 'imageUrl',
17. playState: avMusicTemplate.PlaybackState.PLAYBACK_STATE_PREPARE
18. }
19. let compilation: avMusicTemplate.Compilation = {
20. errorCode: 0,
21. errorMsg: 'success',
22. id: 'id',
23. title: 'title',
24. hasMoreData: true,
25. totalSize: 2,
26. memberMediaType: avMusicTemplate.EntityType.SINGLE,
27. topElements: [mediaEntity]
28. }
29. let customElement: avMusicTemplate.CustomElement = {
30. errorCode: 0,
31. errorMsg: 'success',
32. customCompilations: [compilation]
33. }
34. this.template?.setCustomElements('add', 'COMPILATION', customElement);
35. };
36. }
```

## setSettings

setSettings(settingItems: SettingItem[]): Promise<void>

向音频模板控制方同步设置信息。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| settingItems | [SettingItem](arkts-apis-avmusictemplate-i.md#settingitem)[] | 是 | 设置项数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function setSettings can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000011 | The data write error, data is invalid. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 设置项变化后通知。
8. */
9. public setSettings() {
10. let settingItems: avMusicTemplate.SettingItem[] = [{
11. id: 'id',
12. title: 'title',
13. desc: 'desc',
14. mediaId: 'mediaId',
15. settingType: avMusicTemplate.SettingType.SWITCH,
16. settingValue: false
17. }];
18. this.template?.setSettings(settingItems);
19. };
20. }
```

## reportExecuteAction

reportExecuteAction(actionType: string, params: string): Promise<void>

向音频模板控制方同步执行操作信息。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| actionType | string | 是 | 行为类型。 |
| params | string | 是 | 行为信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function reportExecuteAction can not work correctly due to limited device capabilities. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000011 | The data write error, data is invalid. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. /**
7. * 模拟向媒体中心同步执行操作信息。
8. */
9. public reportExecuteAction() {
10. let actionType: string = 'actionType';
11. let params: string = 'params';
12. this.template?.reportExecuteAction(actionType, params);
13. };
14. }
```

## setExtensionAbility

setExtensionAbility(want: WantAgent): Promise<void>

向音频模板控制方同步用于被拉起的Ability。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [WantAgent](js-apis-app-ability-wantagent.md#wantagent) | 是 | 能力信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000011 | The data write error, data is invalid. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';
2. import { wantAgent } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export class TemplateManager {
6. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

8. /**
9. * 媒体应用需要拉起应用的自定义界面时调用。
10. */
11. public setExtensionAbility() {
12. let wantAgentInfo: wantAgent.WantAgentInfo = {
13. wants: [
14. {
15. bundleName: "com.example.templateprovider",
16. abilityName: 'EntryAbility',
17. type: 'action',
18. parameters: {
19. 'ability.want.params.uiExtensionType': 'action'
20. }
21. }
22. ],
23. actionType: wantAgent.OperationType.START_ABILITIES,
24. requestCode: 0
25. }
26. wantAgent.getWantAgent(wantAgentInfo).then((agent) => {
27. this.template?.setExtensionAbility(agent);
28. })
29. };
30. }
```

## destroy

destroy(): Promise<void>

销毁音频模板实例。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function destroy can not work correctly due to limited device capabilities. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class TemplateManager {
4. private template: avMusicTemplate.AVMusicTemplate | undefined = undefined;

6. public unregisterListener() {
7. this.template?.destroy();
8. this.template = undefined;
9. }
10. }
```
