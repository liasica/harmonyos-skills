---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/kts-apis-avmusictemplate-avmusictemplatecontroller
title: Class (AVMusicTemplateController)
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > ArkTS API > @ohos.multimedia.avMusicTemplate (音频模板) > Class (AVMusicTemplateController)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b8193e04cc95d8f8c7961684cf0eeb6c73e9312dfd38df0cffec8457bcf2473e
---

音频模板控制器，可以获得音频模板控制器唯一的标识，用于与接入音频模板的媒体应用数据交互。

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
| sessionId | string | 否 | 否 | 音频模板控制器唯一的标识。 |
| isDestroy | boolean | 否 | 否 | 音频模板是否销毁。true表示已经销毁，false表示没有销毁。无默认值。 |

## queryMainTabs

queryMainTabs(): Promise<MediaTab[]>

查询主标签。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[MediaTab](arkts-apis-avmusictemplate-i.md#mediatab)[]> | Promise对象，返回查询的主标签页数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000003 | Template listener not registered. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000006 | AVMusicTemplateController does not exist. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

8. /**
9. * 查询主标签。
10. */
11. public async queryMainTabs(): Promise<avMusicTemplate.MediaTab[]> {
12. let tabs: avMusicTemplate.MediaTab[] = [];
13. if (!this.controller) {
14. console.info(TAG, 'queryMainTabs: controller is undefined')
15. return tabs;
16. }
17. try {
18. console.info(TAG, 'queryMainTabs')
19. tabs = await this.controller.queryMainTabs();
20. } catch (e) {
21. console.error(TAG, `queryMainTabs failed, errCode: ${e?.code}`)
22. }
23. return tabs;
24. }
25. }
```

## queryMediaTabContent

queryMediaTabContent(tabId: string): Promise<MediaTabContent>

查询媒体标签内容。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tabId | string | 是 | 标签页ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[MediaTabContent](arkts-apis-avmusictemplate-i.md#mediatabcontent)> | Promise对象，返回媒体标签页内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000003 | Template listener not registered. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000006 | AVMusicTemplateController does not exist. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

8. /**
9. * 模拟查询媒体标签页内容。
10. *
11. * @param tabId 标签页ID。
12. */
13. public async queryMediaTabContent(tabId: string): Promise<avMusicTemplate.MediaTabContent | undefined> {
14. try {
15. let tabContent: avMusicTemplate.MediaTabContent | undefined = await this.controller?.queryMediaTabContent(tabId);
16. if (tabContent?.errorCode != 0) {
17. console.warn(TAG, 'queryMediaTabContent fail')
18. return undefined;
19. }
20. console.info('Succeeded in querying media tab content.');
21. return tabContent;
22. } catch (e) {
23. console.error(TAG, `queryMediaTabContent failed, errCode: ${e?.code}`)
24. return undefined;
25. }
26. }
27. }
```

## queryMediaEntity

queryMediaEntity(params: QueryMediaEntityParam): Promise<PageMediaEntity>

查询媒体实体。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [QueryMediaEntityParam](arkts-apis-avmusictemplate-i.md#querymediaentityparam) | 是 | 查询媒体实体参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PageMediaEntity](arkts-apis-avmusictemplate-i.md#pagemediaentity)> | Promise对象，返回查询的媒体实体分页对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000003 | Template listener not registered. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000006 | AVMusicTemplateController does not exist. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

8. /**
9. * 模拟查询媒体实体。
10. *
11. * @returns 页面媒体实体。
12. */
13. public async queryMediaEntity(): Promise<avMusicTemplate.PageMediaEntity | undefined> {
14. // 查询媒体实体。
15. let queryMediaEntityParam: avMusicTemplate.QueryMediaEntityParam = {
16. entityId: 'entityId',
17. pageIndex: 0,
18. type: avMusicTemplate.EntityType.SINGLE
19. };
20. try {
21. let pageMediaEntity: avMusicTemplate.PageMediaEntity | undefined =
22. await this.controller?.queryMediaEntity(queryMediaEntityParam);
23. if (pageMediaEntity?.errorCode != 0) {
24. console.warn(TAG, 'queryMediaEntity fail')
25. return undefined;
26. }
27. console.info('Succeeded in querying media entity.');
28. return pageMediaEntity;
29. } catch (e) {
30. console.error(TAG, `queryMediaEntity failed, errCode: ${e?.code}`)
31. return undefined;
32. }
33. }
34. }
```

## queryCompilation

queryCompilation(compilationId: string, pageIndex: number): Promise<PageMediaEntity>

查询合集。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| compilationId | string | 是 | 合集的ID。 |
| pageIndex | number | 是 | 标签页的索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PageMediaEntity](arkts-apis-avmusictemplate-i.md#pagemediaentity)> | Promise对象，返回查询的合集的分页对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000003 | Template listener not registered. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000006 | AVMusicTemplateController does not exist. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

8. /**
9. * 模拟查询合集。
10. *
11. * @returns 页面媒体实体。
12. */
13. public async queryCompilation(): Promise<avMusicTemplate.PageMediaEntity | undefined> {
14. let compilationId: string = 'compilationId';
15. let pageIndex: number = 0;
16. try {
17. let pageMediaEntity: avMusicTemplate.PageMediaEntity | undefined =
18. await this.controller?.queryCompilation(compilationId, pageIndex);
19. if (pageMediaEntity?.errorCode != 0) {
20. console.warn(TAG, 'queryCompilation fail')
21. return undefined;
22. }
23. console.info('Succeeded in querying compilation.');
24. return pageMediaEntity;
25. } catch (e) {
26. console.error(TAG, `queryCompilation failed, errCode: ${e?.code}`)
27. return undefined;
28. }
29. }
30. }
```

## queryPlaylist

queryPlaylist(pageIndex: number, sort: Sort): Promise<PageMediaEntity>

查询播放列表。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pageIndex | number | 是 | 标签页的索引。 |
| sort | [Sort](arkts-apis-avmusictemplate-e.md#sort) | 是 | 查询到的播放列表数据的排序类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PageMediaEntity](arkts-apis-avmusictemplate-i.md#pagemediaentity)> | Promise对象，返回查询的播放列表的分页对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000003 | Template listener not registered. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000006 | AVMusicTemplateController does not exist. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

8. /**
9. * 模拟查询播放列表。
10. *
11. * @returns 页面媒体实体。
12. */
13. public async queryPlaylist(): Promise<avMusicTemplate.PageMediaEntity | undefined> {
14. let pageIndex: number = 0;
15. let sort: avMusicTemplate.Sort = avMusicTemplate.Sort.ORDER;
16. try {
17. let pageMediaEntity: avMusicTemplate.PageMediaEntity | undefined =
18. await this.controller?.queryPlaylist(pageIndex, sort);
19. if (pageMediaEntity?.errorCode != 0) {
20. console.warn(TAG, 'queryPlaylist fail')
21. return undefined;
22. }
23. console.info('Succeeded in querying playlist.');
24. return pageMediaEntity;
25. } catch (e) {
26. console.error(TAG, `queryPlaylist failed, errCode: ${e?.code}`)
27. return undefined;
28. }
29. }
30. }
```

## queryCurrentSingle

queryCurrentSingle(): Promise<Single>

查询当前单曲。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Single](arkts-apis-avmusictemplate-i.md#single)> | Promise对象，返回当前单曲。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000003 | Template listener not registered. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000006 | AVMusicTemplateController does not exist. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

8. /**
9. * 模拟查询当前单曲。
10. *
11. * @returns 单曲。
12. */
13. public async queryCurrentSingle(): Promise<avMusicTemplate.Single | undefined> {
14. try {
15. let single: avMusicTemplate.Single | undefined = await this.controller?.queryCurrentSingle();
16. if (!single?.mediaId || single?.mediaId === '') {
17. console.warn(TAG, 'queryCurrentSingle fail')
18. return undefined;
19. }
20. console.info('Succeeded in querying current single.');
21. return single;
22. } catch (e) {
23. console.error(TAG, `queryCurrentSingle failed, errCode: ${e?.code}`)
24. return undefined;
25. }
26. }
27. }
```

## queryCompilationByKeyword

queryCompilationByKeyword(keyword: string): Promise<Compilation[]>

按关键字查询合集。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyword | string | 是 | 关键字。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Compilation](arkts-apis-avmusictemplate-i.md#compilation)[]> | Promise对象，返回合集数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000003 | Template listener not registered. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000006 | AVMusicTemplateController does not exist. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

8. /**
9. * 模拟按关键字查询合集。
10. *
11. * @returns 合集数组。
12. */
13. public async queryCompilationByKeyword(): Promise<avMusicTemplate.Compilation[]> {
14. let compilations: avMusicTemplate.Compilation[] = [];
15. if (!this.controller) {
16. console.error(TAG, 'queryCompilationByKeyword controller is undefined');
17. return compilations;
18. }
19. let keyword: string = 'keyword';
20. try {
21. compilations = await this.controller.queryCompilationByKeyword(keyword);
22. console.info('Succeeded in querying compilation by keyword.');
23. } catch (e) {
24. console.error(TAG, `queryCompilationByKeyword failed, errCode: ${e?.code}`)
25. }
26. return compilations;
27. }
28. }
```

## queryMediaEntityByKeyword

queryMediaEntityByKeyword(keyword: string, searchType: EntityType, pageIndex: number): Promise<PageMediaEntity>

按关键字查询媒体实体。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyword | string | 是 | 关键字。 |
| searchType | [EntityType](arkts-apis-avmusictemplate-e.md#entitytype) | 是 | 媒体资源类型。 |
| pageIndex | number | 是 | 标签页索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PageMediaEntity](arkts-apis-avmusictemplate-i.md#pagemediaentity)> | Promise对象，返回与该关键字相关的媒体实体分页对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000003 | Template listener not registered. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000006 | AVMusicTemplateController does not exist. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

8. /**
9. * 模拟按关键字查询媒体实体。
10. *
11. * @returns 合集数组。
12. */
13. public async queryMediaEntityByKeyword(): Promise<avMusicTemplate.PageMediaEntity | undefined> {
14. let keyword: string = 'keyword';
15. let searchType: avMusicTemplate.EntityType = avMusicTemplate.EntityType.SINGER;
16. let pageIndex: number = 0;
17. try {
18. let pageMediaEntity: avMusicTemplate.PageMediaEntity | undefined =
19. await this.controller?.queryMediaEntityByKeyword(keyword, searchType, pageIndex);
20. if (pageMediaEntity?.errorCode != 0) {
21. console.warn(TAG, 'queryMediaEntityByKeyword fail')
22. return undefined;
23. }
24. console.info('Succeeded in querying media entity by keyword.');
25. return pageMediaEntity;
26. } catch (e) {
27. console.error(TAG, `queryMediaEntityByKeyword failed, errCode: ${e?.code}`)
28. }
29. return undefined;
30. }
31. }
```

## queryRecommendMediaEntityList

queryRecommendMediaEntityList(): Promise<MediaEntity[]>

查询推荐的媒体实体列表。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[MediaEntity](arkts-apis-avmusictemplate-i.md#mediaentity)[]> | Promise对象，返回推荐的媒体实体数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000003 | Template listener not registered. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000006 | AVMusicTemplateController does not exist. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

8. /**
9. * 模拟查询推荐的媒体实体列表。
10. *
11. * @returns 媒体实体数组。
12. */
13. public async queryRecommendMediaEntityList(): Promise<avMusicTemplate.MediaEntity[]> {
14. let mediaEntities: avMusicTemplate.MediaEntity[] = [];
15. if (!this.controller) {
16. console.error(TAG, 'queryRecommendMediaEntityList controller is undefined');
17. return mediaEntities;
18. }
19. try {
20. mediaEntities = await this.controller.queryRecommendMediaEntityList();
21. console.info('Succeeded in querying recommend media entity list.');
22. } catch (e) {
23. console.error(TAG, `queryRecommendMediaEntityList failed, errCode: ${e?.code}`)
24. }
25. return mediaEntities;
26. }
27. }
```

## queryHotWords

queryHotWords(): Promise<string[]>

查询热词。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string[]> | Promise对象，返回热词数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000003 | Template listener not registered. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000006 | AVMusicTemplateController does not exist. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

8. /**
9. * 模拟查询热词。
10. *
11. * @returns 热词数组。
12. */
13. public async queryHotWords(): Promise<string[]> {
14. let hotWords: string[] = [];
15. if (!this.controller) {
16. console.error(TAG, 'queryHotWords controller is undefined');
17. return hotWords;
18. }
19. try {
20. hotWords = await this.controller.queryHotWords();
21. console.info('Succeeded in querying hot words.');
22. } catch (e) {
23. console.error(TAG, `queryHotWords failed, errCode: ${e?.code}`)
24. }
25. return hotWords;
26. }
27. }
```

## querySearchHistory

querySearchHistory(): Promise<string[]>

查询搜索历史。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string[]> | Promise对象，返回历史搜索词数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000003 | Template listener not registered. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000006 | AVMusicTemplateController does not exist. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

8. /**
9. * 模拟查询搜索历史。
10. *
11. * @returns 搜索历史数组。
12. */
13. public async querySearchHistory(): Promise<string[]> {
14. let searchHistory: string[] = [];
15. if (!this.controller) {
16. console.error(TAG, 'querySearchHistory controller is undefined');
17. return searchHistory;
18. }
19. try {
20. searchHistory = await this.controller.querySearchHistory();
21. console.info('Succeeded in querying search history.');
22. } catch (e) {
23. console.error(TAG, `querySearchHistory failed, errCode: ${e?.code}`)
24. }
25. return searchHistory;
26. }
27. }
```

## clearSearchHistory

clearSearchHistory(): Promise<OperResult>

清除搜索历史。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[OperResult](arkts-apis-avmusictemplate-i.md#operresult)> | Promise对象，返回清除搜索历史的操作结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000003 | Template listener not registered. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000006 | AVMusicTemplateController does not exist. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

8. /**
9. * 模拟清除搜索历史。
10. *
11. * @returns Promise类型的boolean，清除成功或者失败。
12. */
13. public async clearSearchHistory(): Promise<boolean> {
14. try {
15. let operResult: avMusicTemplate.OperResult | undefined = await this.controller?.clearSearchHistory()
16. if (operResult?.errorCode != 0) {
17. console.warn(TAG, 'clearSearchHistory fail');
18. return false;
19. }
20. console.info('Succeeded in clearing search history.');
21. return true;
22. } catch (e) {
23. console.error(TAG, `clearSearchHistory failed, errCode: ${e?.code}`);
24. return false;
25. }
26. }
27. }
```

## updateSettings

updateSettings(settingItem: SettingItem): Promise<SettingItem>

更新设置信息。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| settingItem | [SettingItem](arkts-apis-avmusictemplate-i.md#settingitem) | 是 | 待更新的设置项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SettingItem](arkts-apis-avmusictemplate-i.md#settingitem)> | Promise对象，返回更新后的设置项。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000003 | Template listener not registered. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000006 | AVMusicTemplateController does not exist. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

8. /**
9. * 模拟更新设置信息。
10. *
11. * @returns Promise类型更新后的设置项。
12. */
13. public async updateSettings(): Promise<avMusicTemplate.SettingItem | undefined> {
14. let settingItem: avMusicTemplate.SettingItem = {
15. id: 'id',
16. title: 'title',
17. desc: 'desc',
18. mediaId: 'mediaId',
19. settingType: avMusicTemplate.SettingType.SWITCH,
20. settingValue: false
21. };
22. try {
23. let setting: avMusicTemplate.SettingItem | undefined = await this.controller?.updateSettings(settingItem);
24. if (!setting?.id || setting?.id !== settingItem.id) {
25. console.warn(TAG, 'updateSettings fail')
26. return settingItem;
27. }
28. console.info('Succeeded in updating settings.');
29. return setting;
30. } catch (e) {
31. console.error(TAG, `updateSettings failed, errCode: ${e?.code}`)
32. return settingItem;
33. }
34. }
35. }
```

## reportProblemAndAdvice

reportProblemAndAdvice(advice: string): Promise<OperResult>

报告问题和建议。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| advice | string | 是 | 问题或者建议。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[OperResult](arkts-apis-avmusictemplate-i.md#operresult)> | Promise对象，返回报告问题和建议的操作结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000003 | Template listener not registered. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000006 | AVMusicTemplateController does not exist. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

8. /**
9. * 模拟报告问题和建议。
10. *
11. * @returns Promise类型上报结果。true：成功。false：失败。
12. */
13. public async reportProblemAndAdvice(): Promise<boolean> {
14. let advice: string = 'advice';
15. try {
16. let operResult: avMusicTemplate.OperResult | undefined = await this.controller?.reportProblemAndAdvice(advice);
17. if (operResult?.errorCode != 0) {
18. console.warn(TAG, 'reportProblemAndAdvice fail')
19. return false;
20. }
21. console.info('Succeeded in reporting problem and advice.');
22. return true;
23. } catch (e) {
24. console.error(TAG, `reportProblemAndAdvice failed, errCode: ${e?.code}`)
25. return false;
26. }
27. }
28. }
```

## login

login(controlType: LoginType, id?: string): Promise<QrCodeInfo[]>

登录。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| controlType | [LoginType](arkts-apis-avmusictemplate-t.md#logintype) | 是 | 登录类型。 |
| id | string | 否 | 二维码ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[QrCodeInfo](arkts-apis-avmusictemplate-i.md#qrcodeinfo)[]> | Promise对象，返回二维码信息的数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000003 | Template listener not registered. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000006 | AVMusicTemplateController does not exist. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

8. /**
9. * 模拟登录。
10. *
11. * @returns Promise类型的二维码信息数组。
12. */
13. public async login(): Promise<avMusicTemplate.QrCodeInfo[]> {
14. let qrCodeInfos: avMusicTemplate.QrCodeInfo[] = [];
15. if (!this.controller) {
16. console.error(TAG, 'login controller is undefined');
17. return qrCodeInfos;
18. }
19. let controlType: avMusicTemplate.LoginType = 'queryLoginInfo';
20. // 可不传id。id为QrCodeInfo.id，用于LoginType为refreshLoginInfo场景。
21. let id: string | undefined = undefined;
22. try {
23. qrCodeInfos = await this.controller.login(controlType, id);
24. console.info('Succeeded in logging in callback.');
25. } catch (e) {
26. console.error(TAG, `login callback failed, errCode: ${e?.code}`)
27. }
28. return qrCodeInfos;
29. }
30. }
```

## requestDialogInfo

requestDialogInfo(actionType: DialogActionType, actionInfo?: DialogActionInfo): Promise<DialogInfo>

请求对话框信息。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| actionType | [DialogActionType](arkts-apis-avmusictemplate-t.md#dialogactiontype) | 是 | 对话框操作类型。 |
| actionInfo | [DialogActionInfo](arkts-apis-avmusictemplate-i.md#dialogactioninfo) | 否 | 对话框操作的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DialogInfo](arkts-apis-avmusictemplate-i.md#dialoginfo)> | Promise对象，返回对话框信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000003 | Template listener not registered. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000006 | AVMusicTemplateController does not exist. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

8. /**
9. * 模拟请求对话框信息。
10. *
11. * @returns Promise类型的对话框信息。
12. */
13. public async requestDialogInfo(): Promise<avMusicTemplate.DialogInfo | undefined> {
14. let actionType: avMusicTemplate.DialogActionType = 'open';
15. // 可不传actionInfo。用于DialogActionType为refresh和close场景。
16. let actionInfo: avMusicTemplate.DialogActionInfo = {
17. dialogId: 'dialogId',
18. isChecked: true,
19. clickedBtnId: 'clickedBtnId'
20. };
21. try {
22. let dialogInfo: avMusicTemplate.DialogInfo | undefined =
23. await this.controller?.requestDialogInfo(actionType, actionInfo);
24. if (!dialogInfo?.dialogId || dialogInfo?.dialogId === '') {
25. console.info(TAG, 'requestDialogInfo fail')
26. return undefined;
27. }
28. console.info('Succeeded in requesting dialog info.');
29. return dialogInfo;
30. } catch (e) {
31. console.error(TAG, `requestDialogInfo failed, errCode: ${e?.code}`)
32. }
33. return undefined;
34. }
35. }
```

## handleMemberPurchase

handleMemberPurchase(info: MemberPurchaseInfo): Promise<DialogInfo>

处理购买会员情况。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [MemberPurchaseInfo](arkts-apis-avmusictemplate-i.md#memberpurchaseinfo) | 是 | 购买会员的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DialogInfo](arkts-apis-avmusictemplate-i.md#dialoginfo)> | Promise对象，返回对话框信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000003 | Template listener not registered. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000006 | AVMusicTemplateController does not exist. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

8. /**
9. * 模拟请求对话框信息。
10. *
11. * @returns Promise类型的对话框信息。
12. */
13. public async handleMemberPurchase(): Promise<avMusicTemplate.DialogInfo | undefined> {
14. let memberPurchaseInfo: avMusicTemplate.MemberPurchaseInfo = {
15. id: 'id',
16. diagramUrl: 'diagramUrl',
17. diagramContent: 'diagramContent',
18. memberPurchaseType: avMusicTemplate.MemberPurchaseType.NORMAL
19. };
20. try {
21. let dialogInfo: avMusicTemplate.DialogInfo | undefined =
22. await this.controller?.handleMemberPurchase(memberPurchaseInfo);
23. if (!dialogInfo?.dialogId || dialogInfo?.dialogId === '') {
24. console.info(TAG, 'handleMemberPurchase fail')
25. return undefined;
26. }
27. console.info('Succeeded in handling member purchase.');
28. return dialogInfo;
29. } catch (e) {
30. console.error(TAG, `handleMemberPurchase failed, errCode: ${e?.code}`)
31. }
32. return undefined;
33. }
34. }
```

## queryMemberPurchase

queryMemberPurchase(memberPurchaseType: MemberPurchaseType): Promise<MemberPurchaseInfo[]>

查询购买会员的情况。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| memberPurchaseType | [MemberPurchaseType](arkts-apis-avmusictemplate-e.md#memberpurchasetype) | 是 | 会员购买类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[MemberPurchaseInfo](arkts-apis-avmusictemplate-i.md#memberpurchaseinfo)[]> | Promise对象，返回购买会员信息的数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000003 | Template listener not registered. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000006 | AVMusicTemplateController does not exist. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

8. /**
9. * 模拟查询购买会员的情况。
10. *
11. * @returns 会员购买信息列表。
12. */
13. public async queryMemberPurchase(): Promise<avMusicTemplate.MemberPurchaseInfo[]> {
14. let memberPurchaseInfo: avMusicTemplate.MemberPurchaseInfo[] = [];
15. if (!this.controller) {
16. console.error(TAG, 'queryMemberPurchase controller is undefined');
17. return memberPurchaseInfo;
18. }
19. let memberPurchaseType: avMusicTemplate.MemberPurchaseType = avMusicTemplate.MemberPurchaseType.NORMAL;
20. try {
21. memberPurchaseInfo = await this.controller.queryMemberPurchase(memberPurchaseType);
22. console.info('Succeeded in querying member purchase.');
23. } catch (e) {
24. console.error(TAG, `queryMemberPurchase failed, errCode: ${e?.code}`)
25. }
26. return memberPurchaseInfo;
27. }
28. }
```

## queryCustomContent

queryCustomContent(queryType: CustomType[]): Promise<CustomElement>

查询自定义内容。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| queryType | [CustomType](arkts-apis-avmusictemplate-t.md#customtype)[] | 是 | 自定义类型数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[CustomElement](arkts-apis-avmusictemplate-i.md#customelement)> | Promise对象，返回查询的自定义元素。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000003 | Template listener not registered. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000006 | AVMusicTemplateController does not exist. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

8. /**
9. * 模拟查询自定义内容。
10. *
11. * @returns 自定义元素。
12. */
13. public async queryCustomContent(): Promise<avMusicTemplate.CustomElement | undefined> {
14. let queryType: avMusicTemplate.CustomType[] = ['USER_INFO', 'TAB', 'COMPILATION', 'SETTINGS'];
15. try {
16. let customElement: avMusicTemplate.CustomElement | undefined =
17. await this.controller?.queryCustomContent(queryType);
18. if (customElement?.errorCode != 0) {
19. console.warn(TAG, 'queryCustomContent fail')
20. return undefined;
21. }
22. console.info('Succeeded in querying custom content.');
23. return customElement;
24. } catch (e) {
25. console.error(TAG, `queryCustomContent failed, errCode: ${e?.code}`)
26. return undefined;
27. }
28. }
29. }
```

## downloadMediaEntity

downloadMediaEntity(controlType: DownloadControlType, mediaEntity: MediaEntity): Promise<OperResult>

下载媒体实体。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| controlType | [DownloadControlType](arkts-apis-avmusictemplate-t.md#downloadcontroltype) | 是 | 下载的控制类型。 |
| mediaEntity | [MediaEntity](arkts-apis-avmusictemplate-i.md#mediaentity) | 是 | 媒体实体。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[OperResult](arkts-apis-avmusictemplate-i.md#operresult)> | Promise对象，返回下载媒体实体的操作结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000003 | Template listener not registered. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000006 | AVMusicTemplateController does not exist. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

8. /**
9. * 模拟下载媒体实体。
10. *
11. * @returns Promise类型操作结果。
12. */
13. public async downloadMediaEntity(): Promise<boolean> {
14. let controlType: avMusicTemplate.DownloadControlType = 'startDownload';
15. let mediaEntity: avMusicTemplate.MediaEntity = {
16. mediaId: 'mediaId',
17. mediaType: avMusicTemplate.EntityType.SINGLE,
18. parentId: 'parentId',
19. parentMediaType: avMusicTemplate.EntityType.SINGLE,
20. title: 'title',
21. imageUrl: 'imageUrl',
22. playState: avMusicTemplate.PlaybackState.PLAYBACK_STATE_PREPARE
23. };
24. try {
25. let operResult: avMusicTemplate.OperResult | undefined =
26. await this.controller?.downloadMediaEntity(controlType, mediaEntity);
27. if (operResult?.errorCode != 0) {
28. console.warn(TAG, 'start downloadMediaEntity fail')
29. return false;
30. }
31. console.info('Succeeded in starting download media entity.');
32. return true;
33. } catch (e) {
34. console.error(TAG, `start downloadMediaEntity failed, errCode: ${e?.code}`)
35. return false;
36. }
37. }
38. }
```

## playForSearch

playForSearch(command: SearchPlayInfoType, args: SearchPlayInfo): Promise<OperResult>

搜播，支持音视频，示例仅以音频为例。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| command | [SearchPlayInfoType](arkts-apis-avmusictemplate-e.md#searchplayinfotype) | 是 | 搜播的信息类型枚举。 |
| args | [SearchPlayInfo](arkts-apis-avmusictemplate-i.md#searchplayinfo) | 是 | 搜播信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[OperResult](arkts-apis-avmusictemplate-i.md#operresult)> | Promise对象，返回操作结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000003 | Template listener not registered. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000006 | AVMusicTemplateController does not exist. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

8. /**
9. * 模拟搜播。
10. *
11. * @returns Promise类型操作结果。
12. */
13. public async playForSearch(): Promise<boolean> {
14. let command: avMusicTemplate.SearchPlayInfoType = avMusicTemplate.SearchPlayInfoType.PLAY_MUSIC;
15. let searchPlayMusicItems: avMusicTemplate.SearchPlayMusicItem[] = [{
16. entityId: 'entityId',
17. entityName: 'entityName'
18. }];
19. let searchPlayMusicInfo: avMusicTemplate.SearchPlayMusicInfo = {
20. items: searchPlayMusicItems,
21. displayName: 'displayName',
22. description: 'description'
23. };
24. let searchPlayInfo: avMusicTemplate.SearchPlayInfo = {
25. musicInfo: searchPlayMusicInfo
26. };
27. try {
28. let operResult: avMusicTemplate.OperResult | undefined =
29. await this.controller?.playForSearch(command, searchPlayInfo);
30. if (operResult?.errorCode != 0) {
31. console.warn(TAG, 'playForSearch fail')
32. return false;
33. }
34. console.info('Succeeded in playing for search.');
35. return true;
36. } catch (e) {
37. console.error(TAG, `playForSearch failed, errCode: ${e?.code}`)
38. return false;
39. }
40. }
41. }
```

## executeAction

executeAction(actionType: string, params: string): Promise<string>

执行动作。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| actionType | string | 是 | 动作类型。 |
| params | string | 是 | 动作信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回执行动作的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000003 | Template listener not registered. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000006 | AVMusicTemplateController does not exist. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

8. /**
9. * 模拟执行动作。
10. *
11. * @returns Promise<string>类型操作结果。
12. */
13. public async executeAction(): Promise<string> {
14. let actionType: string = 'actionType';
15. let params: string = 'params';
16. try {
17. let result: string | undefined = await this.controller?.executeAction(actionType, params);
18. if (!result || result === '') {
19. console.warn(TAG, 'executeAction fail')
20. return '';
21. }
22. console.info('Succeeded in executing action.');
23. return result;
24. } catch (e) {
25. console.error(TAG, `executeAction failed, errCode: ${e?.code}`)
26. return '';
27. }
28. }
29. }
```

## playMediaEntity

playMediaEntity(mediaEntity: MediaEntity): Promise<void>

播放媒体。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mediaEntity | [MediaEntity](arkts-apis-avmusictemplate-i.md#mediaentity) | 是 | 包含标题、作者等元数据的媒体实体对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000003 | Template listener not registered. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000006 | AVMusicTemplateController does not exist. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class ControllerManager {
4. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

6. /**
7. * 模拟播放媒体。
8. */
9. public async playMediaEntity() {
10. let mediaEntity: avMusicTemplate.MediaEntity = {
11. mediaId: 'mediaId',
12. mediaType: avMusicTemplate.EntityType.SINGLE,
13. parentId: 'parentId',
14. parentMediaType: avMusicTemplate.EntityType.SINGLE,
15. title: 'title',
16. imageUrl: 'imageUrl',
17. playState: avMusicTemplate.PlaybackState.PLAYBACK_STATE_PREPARE
18. };
19. this.controller?.playMediaEntity(mediaEntity);
20. }
21. }
```

## favoriteMediaEntity

favoriteMediaEntity(actionType: MediaFavoriteType, mediaEntity: MediaEntity): Promise<OperResult>

收藏媒体。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| actionType | [MediaFavoriteType](arkts-apis-avmusictemplate-t.md#mediafavoritetype) | 是 | 媒体收藏的类型。 |
| mediaEntity | [MediaEntity](arkts-apis-avmusictemplate-i.md#mediaentity) | 是 | 媒体实体。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[OperResult](arkts-apis-avmusictemplate-i.md#operresult)> | Promise对象，返回收藏媒体的操作结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000003 | Template listener not registered. |
| 35000005 | AVMusicTemplate does not exist. |
| 35000006 | AVMusicTemplateController does not exist. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

8. /**
9. * 模拟收藏媒体。
10. *
11. * @returns Promise类型操作结果。
12. */
13. public async favoriteMediaEntity(): Promise<boolean> {
14. let actionType: avMusicTemplate.MediaFavoriteType = 'addFavorite';
15. let mediaEntity: avMusicTemplate.MediaEntity = {
16. mediaId: 'mediaId',
17. mediaType: avMusicTemplate.EntityType.SINGLE,
18. parentId: 'parentId',
19. parentMediaType: avMusicTemplate.EntityType.SINGLE,
20. title: 'title',
21. imageUrl: 'imageUrl',
22. playState: avMusicTemplate.PlaybackState.PLAYBACK_STATE_PREPARE
23. };
24. try {
25. let operResult: avMusicTemplate.OperResult | undefined =
26. await this.controller?.favoriteMediaEntity(actionType, mediaEntity);
27. if (operResult?.errorCode != 0) {
28. console.warn(TAG, 'favoriteMediaEntity fail')
29. return false;
30. }
31. console.info('Succeeded in favoriting media entity.');
32. return true;
33. } catch (e) {
34. console.error(TAG, `favoriteMediaEntity failed, errCode: ${e?.code}`)
35. return false;
36. }
37. }
38. }
```

## onUserInfoChange

onUserInfoChange(callback: Callback<UserInfo>): void

注册用户信息改变的回调。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[UserInfo](arkts-apis-avmusictemplate-i.md#userinfo)> | 是 | 回调函数，返回用户信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000006 | AVMusicTemplateController does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;
7. private userInfoChangeCallback: Callback<avMusicTemplate.UserInfo> = (userInfo: avMusicTemplate.UserInfo) => {
8. console.info(TAG, 'userInfoChangeCallback');
9. };

11. public registerListener() {
12. // 注册用户信息改变的监听。
13. this.controller?.onUserInfoChange(this.userInfoChangeCallback);
14. }
15. }
```

## offUserInfoChange

offUserInfoChange(callback?: Callback<UserInfo>): void

注销用户信息改变的回调。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[UserInfo](arkts-apis-avmusictemplate-i.md#userinfo)> | 否 | 回调函数，返回用户信息。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000006 | AVMusicTemplateController does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class ControllerManager {
4. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. // 注销用户信息改变的监听。
11. this.controller?.offUserInfoChange();
12. }
13. }
```

## onDialogCommandChange

onDialogCommandChange(callback: ReportDialogCommandEvent): void

注册对话框命令改变的回调。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ReportDialogCommandEvent](arkts-apis-avmusictemplate-t.md#reportdialogcommandevent) | 是 | 回调函数，上报对话框命令事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000006 | AVMusicTemplateController does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;
7. private reportDialogCommandEvent: avMusicTemplate.ReportDialogCommandEvent =
8. (type: avMusicTemplate.DialogControlType, buttonInfo: avMusicTemplate.DialogInfo) => {
9. console.info(TAG, 'reportDialogCommandEvent');
10. };

12. public registerListener() {
13. // 注册对话框命令改变的监听。
14. this.controller?.onDialogCommandChange(this.reportDialogCommandEvent);
15. }
16. }
```

## offDialogCommandChange

offDialogCommandChange(callback?: ReportDialogCommandEvent): void

注销对话框命令改变的回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ReportDialogCommandEvent](arkts-apis-avmusictemplate-t.md#reportdialogcommandevent) | 否 | 上报对话框命令事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000006 | AVMusicTemplateController does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class ControllerManager {
4. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. // 注销对话框命令改变的监听。
11. this.controller?.offDialogCommandChange();
12. }
13. }
```

## onCurrentSingleChange

onCurrentSingleChange(callback: Callback<Single>): void

注册当前单曲改变的回调。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[Single](arkts-apis-avmusictemplate-i.md#single)> | 是 | 回调函数，返回当前单曲的信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000006 | AVMusicTemplateController does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;
7. private currentSingleChangeCallback: Callback<avMusicTemplate.Single> = (single: avMusicTemplate.Single) => {
8. console.info(TAG, 'onCurrentSingleChange');
9. };

11. public registerListener() {
12. // 注册当前单曲改变的监听。
13. this.controller?.onCurrentSingleChange(this.currentSingleChangeCallback);
14. }
15. }
```

## offCurrentSingleChange

offCurrentSingleChange(callback?: Callback<Single>): void

注销当前单曲改变的回调。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[Single](arkts-apis-avmusictemplate-i.md#single)> | 否 | 回调函数，返回当前单曲的信息。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000006 | AVMusicTemplateController does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class ControllerManager {
4. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. // 注销当前单曲改变的监听。
11. this.controller?.offCurrentSingleChange();
12. }
13. }
```

## onMediaEntitiesChange

onMediaEntitiesChange(callback: Callback<MediaEntity[]>): void

注册媒体实体改变的回调。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[MediaEntity](arkts-apis-avmusictemplate-i.md#mediaentity)[]> | 是 | 回调函数，返回媒体实体数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000006 | AVMusicTemplateController does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;
7. private mediaEntitiesChangeCallback: Callback<avMusicTemplate.MediaEntity[]> =
8. (single: avMusicTemplate.MediaEntity[]) => {
9. console.info(TAG, 'mediaEntitiesChangeCallback');
10. }

12. public registerListener() {
13. // 注册媒体实体改变的监听。
14. this.controller?.onMediaEntitiesChange(this.mediaEntitiesChangeCallback);
15. }
16. }
```

## offMediaEntitiesChange

offMediaEntitiesChange(callback?: Callback<MediaEntity[]>): void

注销媒体实体改变的回调。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[MediaEntity](arkts-apis-avmusictemplate-i.md#mediaentity)[]> | 否 | 回调函数，返回媒体实体数组。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000006 | AVMusicTemplateController does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class ControllerManager {
4. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. // 注销媒体实体改变的监听。
11. this.controller?.offMediaEntitiesChange();
12. }
13. }
```

## onTabContentChange

onTabContentChange(callback: ReportTabContentEvent): void

注册标签页内容改变的回调。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ReportTabContentEvent](arkts-apis-avmusictemplate-t.md#reporttabcontentevent) | 是 | 回调函数，上报标签页内容事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000006 | AVMusicTemplateController does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;
7. private reportTabContentEvent: avMusicTemplate.ReportTabContentEvent =
8. (tabId: string, tabContent: avMusicTemplate.MediaTabContent) => {
9. console.info(TAG, 'reportTabContentEvent');
10. };

12. public registerListener() {
13. // 注册标签页内容改变的监听。
14. this.controller?.onTabContentChange(this.reportTabContentEvent);
15. }
16. }
```

## offTabContentChange

offTabContentChange(callback?: ReportTabContentEvent): void

注销标签页内容改变的回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ReportTabContentEvent](arkts-apis-avmusictemplate-t.md#reporttabcontentevent) | 否 | 上报标签页内容事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000006 | AVMusicTemplateController does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class ControllerManager {
4. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. // 注销标签页内容改变的监听。
11. this.controller?.offTabContentChange();
12. }
13. }
```

## onPlaylistChange

onPlaylistChange(callback: Callback<PageMediaEntity>): void

注册上报播放列表改变的回调。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[PageMediaEntity](arkts-apis-avmusictemplate-i.md#pagemediaentity)> | 是 | 回调函数，返回标签页媒体实体信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000006 | AVMusicTemplateController does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;
7. private playlistChangeCallback: Callback<avMusicTemplate.PageMediaEntity> =
8. (pageMediaEntity: avMusicTemplate.PageMediaEntity) => {
9. console.info(TAG, 'playlistChangeCallback');
10. }

12. public registerListener() {
13. // 注册播放列表改变的监听。
14. this.controller?.onPlaylistChange(this.playlistChangeCallback);
15. }
16. }
```

## offPlaylistChange

offPlaylistChange(callback?: Callback<PageMediaEntity>): void

注销上报播放列表改变的回调。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[PageMediaEntity](arkts-apis-avmusictemplate-i.md#pagemediaentity)> | 否 | 回调函数，返回标签页媒体实体信息。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000006 | AVMusicTemplateController does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class ControllerManager {
4. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. // 注销播放列表改变的监听。
11. this.controller?.offPlaylistChange();
12. }
13. }
```

## onDownloadMediaEntityStatusChange

onDownloadMediaEntityStatusChange(callback: Callback<MediaEntity>): void

注册上报下载媒体状态改变的回调。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[MediaEntity](arkts-apis-avmusictemplate-i.md#mediaentity)> | 是 | 回调函数，返回媒体实体信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000006 | AVMusicTemplateController does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;
7. private downloadStatusChangeCallback: Callback<avMusicTemplate.MediaEntity> =
8. (mediaEntity: avMusicTemplate.MediaEntity) => {
9. console.info(TAG, 'downloadStatusChangeCallback');
10. };

12. public registerListener() {
13. // 注册下载媒体状态改变的监听。
14. this.controller?.onDownloadMediaEntityStatusChange(this.downloadStatusChangeCallback);
15. }
16. }
```

## offDownloadMediaEntityStatusChange

offDownloadMediaEntityStatusChange(callback?: Callback<MediaEntity>): void

注销上报下载媒体状态改变的回调。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[MediaEntity](arkts-apis-avmusictemplate-i.md#mediaentity)> | 否 | 回调函数，返回媒体实体信息。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000006 | AVMusicTemplateController does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class ControllerManager {
4. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. // 注销下载媒体状态改变的监听。
11. this.controller?.offDownloadMediaEntityStatusChange();
12. }
13. }
```

## onCustomElementsChange

onCustomElementsChange(callback: ReportCustomElementsChangeEvent): void

注册上报自定义元素改变的回调。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ReportCustomElementsChangeEvent](arkts-apis-avmusictemplate-t.md#reportcustomelementschangeevent) | 是 | 回调函数，上报自定义元素改变事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000006 | AVMusicTemplateController does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;
7. private reportCustomElementsChangeEvent: avMusicTemplate.ReportCustomElementsChangeEvent =
8. (actionType: avMusicTemplate.ActionType, customType: avMusicTemplate.CustomType,
9. customElement: avMusicTemplate.CustomElement) => {
10. console.info(TAG, 'reportCustomElementsChangeEvent');
11. };

13. public registerListener() {
14. // 注册自定义元素改变的监听。
15. this.controller?.onCustomElementsChange(this.reportCustomElementsChangeEvent);
16. }
17. }
```

## offCustomElementsChange

offCustomElementsChange(callback?: ReportCustomElementsChangeEvent): void

注销上报自定义元素改变的回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ReportCustomElementsChangeEvent](arkts-apis-avmusictemplate-t.md#reportcustomelementschangeevent) | 否 | 上报自定义元素改变事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000006 | AVMusicTemplateController does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class ControllerManager {
4. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. // 注销自定义元素改变的监听。
11. this.controller?.offCustomElementsChange();
12. }
13. }
```

## onSettingsChange

onSettingsChange(callback: Callback<SettingItem[]>): void

注册上报设置改变的回调。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[SettingItem](arkts-apis-avmusictemplate-i.md#settingitem)[]> | 是 | 回调函数，返回设置项数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000006 | AVMusicTemplateController does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;
7. private settingsChangeCallback: Callback<avMusicTemplate.SettingItem[]> =
8. (settingItems: avMusicTemplate.SettingItem[]) => {
9. console.info(TAG, 'settingsChangeCallback');
10. };

12. public registerListener() {
13. // 注册设置改变的监听。
14. this.controller?.onSettingsChange(this.settingsChangeCallback);
15. }
16. }
```

## offSettingsChange

offSettingsChange(callback?: Callback<SettingItem[]>): void

注销上报设置改变的回调。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[SettingItem](arkts-apis-avmusictemplate-i.md#settingitem)[]> | 否 | 回调函数，用于接收并处理设置项数组。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000006 | AVMusicTemplateController does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class ControllerManager {
4. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. // 注销设置改变的监听。
11. this.controller?.offSettingsChange();
12. }
13. }
```

## onReportExecuteAction

onReportExecuteAction(callback: ReportExecuteActionEvent): void

注册上报执行动作的回调。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ReportExecuteActionEvent](arkts-apis-avmusictemplate-t.md#reportexecuteactionevent) | 是 | 回调函数，上报对应按钮动作的事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000006 | AVMusicTemplateController does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;
7. private reportExecuteActionEvent: avMusicTemplate.ReportExecuteActionEvent =
8. (actionType: string, customType: string) => {
9. console.info(TAG, 'reportExecuteActionEvent');
10. };

12. public registerListener() {
13. // 注册上报执行动作的监听。
14. this.controller?.onReportExecuteAction(this.reportExecuteActionEvent);
15. }
16. }
```

## offReportExecuteAction

offReportExecuteAction(callback?: ReportExecuteActionEvent): void

注销上报执行动作的回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ReportExecuteActionEvent](arkts-apis-avmusictemplate-t.md#reportexecuteactionevent) | 否 | 上报执行动作的事件。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000006 | AVMusicTemplateController does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class ControllerManager {
4. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. // 注销上报执行动作的监听。
11. this.controller?.offReportExecuteAction();
12. }
13. }
```

## onExtensionAbilityChange

onExtensionAbilityChange(callback: ReportExecuteAbilityEvent): void

注册通知音频模板控制方拉起由用户指定的媒体应用界面的信息的回调。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ReportExecuteAbilityEvent](arkts-apis-avmusictemplate-t.md#reportexecuteabilityevent) | 是 | 回调函数，通知音频模板控制方拉起指定三方应用界面的事件，包含应用包名和界面名称等信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000006 | AVMusicTemplateController does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';
2. import { WantAgent } from '@kit.AbilityKit';

4. const TAG: string = 'ControllerManager';

6. export class ControllerManager {
7. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;
8. private reportExecuteAbilityEvent: avMusicTemplate.ReportExecuteAbilityEvent = (want: WantAgent) => {
9. console.info(TAG, 'reportExecuteAbilityEvent');
10. };

12. public registerListener() {
13. // 注册通知媒体中心拉起指定三方应用界面的信息的监听。
14. this.controller?.onExtensionAbilityChange(this.reportExecuteAbilityEvent);
15. }
16. }
```

## offExtensionAbilityChange

offExtensionAbilityChange(callback?: ReportExecuteAbilityEvent): void

注销通知音频模板控制方拉起指定媒体应用播放界面的信息的回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ReportExecuteAbilityEvent](arkts-apis-avmusictemplate-t.md#reportexecuteabilityevent) | 否 | 通知音频模板控制方拉起指定的媒体应用界面的事件回调。不填该参数则注销该类型对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[音频模板错误码](errorcode-avmusictemplate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 35000006 | AVMusicTemplateController does not exist. |
| 35000012 | AVMusicTemplate error. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. export class ControllerManager {
4. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;

6. /**
7. * 注销监听。
8. */
9. public unregisterListener() {
10. // 注销通知媒体中心拉起指定三方应用界面的信息的监听。
11. this.controller?.offExtensionAbilityChange();
12. }
13. }
```

## destroy

destroy(): Promise<void>

销毁音频模板控制器。使用Promise异步回调。

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
| 801 | capability not supported. |

**示例：**

```
1. import { avMusicTemplate } from '@kit.AVSessionKit';

3. const TAG: string = 'ControllerManager';

5. export class ControllerManager {
6. private controller: avMusicTemplate.AVMusicTemplateController | undefined = undefined;
7. private currentBundleName: string | undefined = undefined;

9. /**
10. * 销毁控制器。
11. */
12. public destroyController() {
13. console.info(TAG, 'destroyController')
14. this.controller?.destroy();
15. this.controller = undefined;
16. this.currentBundleName = undefined;
17. }
18. }
```
