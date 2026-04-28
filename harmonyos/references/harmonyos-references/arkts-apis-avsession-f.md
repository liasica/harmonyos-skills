---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-f
title: Functions
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > ArkTS API > @ohos.multimedia.avsession (媒体会话管理) > Functions
category: harmonyos-references
scraped_at: 2026-04-28T08:12:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dae41a60256b5d271fb573886330bec9abdca9f71e0f64ad0183ded801396412
---

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { avSession } from '@kit.AVSessionKit';
```

## avSession.createAVSession10+

PhonePC/2in1TabletTVWearable

createAVSession(context: Context, tag: string, type: AVSessionType): Promise<AVSession>

创建会话对象，一个应用进程仅允许存在一个会话，重复创建会失败，结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-app-context.md) | 是 | 需要使用UIAbilityContext，用于系统获取应用组件的相关信息。 |
| tag | string | 是 | 会话的自定义名称。 |
| type | [AVSessionType](arkts-apis-avsession-t.md#avsessiontype10) | 是 | 会话类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AVSession](arkts-apis-avsession-avsession.md)> | Promise对象。回调返回会话实例对象，可用于获取会话ID，以及设置元数据、播放状态，发送按键事件等操作。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |

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
11. let currentAVSession: avSession.AVSession;
12. let tag = "createNewSession";
13. let context: Context = this.getUIContext().getHostContext() as Context;
14. let sessionId: string;  // 供后续函数入参使用。

16. avSession.createAVSession(context, tag, "audio").then(async (data: avSession.AVSession) => {
17. currentAVSession = data;
18. sessionId = currentAVSession.sessionId;
19. console.info(`Succeeded in creating AV session, sessionId: ${sessionId}`);
20. });
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

## avSession.createAVSession10+

PhonePC/2in1TabletTVWearable

createAVSession(context: Context, tag: string, type: AVSessionType, callback: AsyncCallback<AVSession>): void

创建会话对象，一个应用程序仅允许存在一个会话，重复创建会失败，结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-app-context.md) | 是 | 需要使用UIAbilityContext，用于系统获取应用组件的相关信息。 |
| tag | string | 是 | 会话的自定义名称。 |
| type | [AVSessionType](arkts-apis-avsession-t.md#avsessiontype10) | 是 | 会话类型。 |
| callback | AsyncCallback<[AVSession](arkts-apis-avsession-avsession.md)> | 是 | 回调函数。回调返回会话实例对象，可用于获取会话ID，以及设置元数据、播放状态，发送按键事件等操作。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |

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
11. let currentAVSession: avSession.AVSession;
12. let tag = "createNewSession";
13. let context: Context = this.getUIContext().getHostContext() as Context;
14. let sessionId: string;  // 供后续函数入参使用。

16. avSession.createAVSession(context, tag, "audio", async (data: avSession.AVSession) => {
17. currentAVSession = data;
18. sessionId = currentAVSession.sessionId;
19. console.info(`Succeeded in creating AV session, sessionId: ${sessionId}`);
20. });
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

## avSession.getAVSession22+

PhonePC/2in1TabletTVWearable

getAVSession(context: Context): Promise<AVSession>

获取会话对象。使用Promise异步回调。

该接口可将当前进程已创建过的会话对象返回，如果没有创建过会话对象，当前接口会调用失败抛出异常。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-app-context.md) | 是 | 需要使用UIAbilityContext，用于系统获取应用组件的相关信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AVSession](arkts-apis-avsession-avsession.md)> | Promise对象。回调返回会话实例对象，可用于获取会话ID、设置元数据及播放状态、发送按键事件等操作。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
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
11. let currentAVSession: avSession.AVSession;
12. let context: Context = this.getUIContext().getHostContext() as Context;
13. let sessionId: string;  // 供后续函数入参使用。
14. let sessionTag: string;

16. avSession.getAVSession(context).then(async (data: avSession.AVSession) => {
17. currentAVSession = data;
18. sessionId = currentAVSession.sessionId;
19. sessionTag = currentAVSession.sessionTag;
20. console.info(`Succeeded in getting AV session, sessionId: ${sessionId}, sessionTag: ${sessionTag}`);
21. });
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

## avSession.getAllSessionDescriptors23+

PhonePC/2in1TabletTVWearable

getAllSessionDescriptors(): Promise<Array<Readonly<AVSessionDescriptor>>>

获取所有设置过媒体信息且注册过控制回调的会话的描述符信息。结果通过Promise异步回调方式返回。

**需要权限：** ohos.permission.MANAGE\_MEDIA\_RESOURCES 或 ohos.permission.MANAGE\_MEDIA\_RESOURCES\_FOR\_PUBLIC

系统应用可以从ohos.permission.MANAGE\_MEDIA\_RESOURCES或ohos.permission.MANAGE\_MEDIA\_RESOURCES\_FOR\_PUBLIC两个权限中选择一个进行申请，普通应用仅允许申请ohos.permission.MANAGE\_MEDIA\_RESOURCES\_FOR\_PUBLIC受限权限。

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<Readonly<[AVSessionDescriptor](arkts-apis-avsession-i.md#avsessiondescriptor-23)>>> | Promise对象。返回所有会话描述的只读对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | permission denied. |
| 6600101 | Session service exception. |

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
11. avSession.getAllSessionDescriptors().then((descriptors: avSession.AVSessionDescriptor[]) => {
12. console.info(`Succeeded in getting all session descriptors, length: ${descriptors.length}`);
13. if (descriptors.length > 0 ) {
14. console.info(`Succeeded in getting session descriptor, isActive: ${descriptors[0].isActive}`);
15. console.info(`Succeeded in getting session descriptor, type: ${descriptors[0].type}`);
16. console.info(`Succeeded in getting session descriptor, sessionTag: ${descriptors[0].sessionTag}`);
17. }
18. });
19. })
20. }
21. .width('100%')
22. .height('100%')
23. }
24. }
```

## avSession.createController23+

PhonePC/2in1TabletTVWearable

createController(sessionId: string): Promise<AVSessionController>

根据会话ID创建会话控制器。使用Promise异步回调。

**需要权限：** ohos.permission.MANAGE\_MEDIA\_RESOURCES 或 ohos.permission.MANAGE\_MEDIA\_RESOURCES\_FOR\_PUBLIC

系统应用可以从ohos.permission.MANAGE\_MEDIA\_RESOURCES或ohos.permission.MANAGE\_MEDIA\_RESOURCES\_FOR\_PUBLIC两个权限中选择一个进行申请，普通应用仅允许申请ohos.permission.MANAGE\_MEDIA\_RESOURCES\_FOR\_PUBLIC受限权限。

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | string | 是 | 会话ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AVSessionController](arkts-apis-avsession-avsessioncontroller.md)> | Promise对象。返回会话控制器实例，可查看会话ID，  并完成对会话发送命令及事件，获取元数据、播放状态信息等操作。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
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
11. avSession.getAllSessionDescriptors().then((descriptors: avSession.AVSessionDescriptor[]) => {
12. console.info(`Succeeded in getting all session descriptors, length: ${descriptors.length}`);
13. if (descriptors.length > 0 ) {
14. avSession.createController(descriptors[0]?.sessionId).then((avcontroller: avSession.AVSessionController) => {
15. console.info('Succeeded in creating controller.');
16. });
17. }
18. });
19. })
20. }
21. .width('100%')
22. .height('100%')
23. }
24. }
```

## avSession.onSessionCreate23+

PhonePC/2in1TabletTVWearable

onSessionCreate(callback: Callback<AVSessionDescriptor>): void

监听会话创建事件。使用callback异步回调。

**需要权限：** ohos.permission.MANAGE\_MEDIA\_RESOURCES\_FOR\_PUBLIC

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[AVSessionDescriptor](arkts-apis-avsession-i.md#avsessiondescriptor-23)> | 是 | 回调函数。参数为会话相关描述。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | permission denied. |
| 6600101 | Session service exception. |

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
11. avSession.onSessionCreate((descriptor: avSession.AVSessionDescriptor) => {
12. console.info(`on sessionCreate : isActive : ${descriptor.isActive}`);
13. console.info(`on sessionCreate : type : ${descriptor.type}`);
14. console.info(`on sessionCreate : sessionTag : ${descriptor.sessionTag}`);
15. });
16. })
17. }
18. .width('100%')
19. .height('100%')
20. }
21. }
```

## avSession.onSessionDestroy23+

PhonePC/2in1TabletTVWearable

onSessionDestroy(callback: Callback<AVSessionDescriptor>): void

监听会话的销毁事件。使用callback异步回调。

**需要权限：** ohos.permission.MANAGE\_MEDIA\_RESOURCES\_FOR\_PUBLIC

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[AVSessionDescriptor](arkts-apis-avsession-i.md#avsessiondescriptor-23)> | 是 | 回调函数。参数为会话相关描述。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | permission denied. |
| 6600101 | Session service exception. |

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
11. avSession.onSessionDestroy((descriptor: avSession.AVSessionDescriptor) => {
12. console.info(`on sessionDestroy : ${descriptor.sessionId}`);
13. });
14. })
15. }
16. .width('100%')
17. .height('100%')
18. }
19. }
```

## avSession.onTopSessionChange23+

PhonePC/2in1TabletTVWearable

onTopSessionChange(callback: Callback<AVSessionDescriptor>): void

监听最新播放会话变更的事件。使用callback异步回调。

**需要权限：** ohos.permission.MANAGE\_MEDIA\_RESOURCES\_FOR\_PUBLIC

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[AVSessionDescriptor](arkts-apis-avsession-i.md#avsessiondescriptor-23)> | 是 | 回调函数。参数为会话相关描述。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | permission denied. |
| 6600101 | Session service exception. |

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
11. avSession.onTopSessionChange((descriptor: avSession.AVSessionDescriptor) => {
12. console.info(`on topSessionChange : isActive : ${descriptor.isActive}`);
13. console.info(`on topSessionChange : type : ${descriptor.type}`);
14. console.info(`on topSessionChange : sessionTag : ${descriptor.sessionTag}`);
15. });
16. })
17. }
18. .width('100%')
19. .height('100%')
20. }
21. }
```

## avSession.offSessionCreate23+

PhonePC/2in1TabletTVWearable

offSessionCreate(callback?: Callback<AVSessionDescriptor>): void

注销会话创建事件监听。注销后，不再接收该事件。

**需要权限：** ohos.permission.MANAGE\_MEDIA\_RESOURCES\_FOR\_PUBLIC

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[AVSessionDescriptor](arkts-apis-avsession-i.md#avsessiondescriptor-23)> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为会话相关描述，为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | permission denied. |
| 6600101 | Session service exception. |

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
11. avSession.onSessionCreate((descriptor: avSession.AVSessionDescriptor) => {
12. });
13. avSession.offSessionCreate();
14. })
15. }
16. .width('100%')
17. .height('100%')
18. }
19. }
```

## avSession.offSessionDestroy23+

PhonePC/2in1TabletTVWearable

offSessionDestroy(callback?: Callback<AVSessionDescriptor>): void

注销会话销毁事件监听。注销后，不再监听该事件。

**需要权限：** ohos.permission.MANAGE\_MEDIA\_RESOURCES\_FOR\_PUBLIC

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[AVSessionDescriptor](arkts-apis-avsession-i.md#avsessiondescriptor-23)> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为会话相关描述，为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | permission denied. |
| 6600101 | Session service exception. |

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
11. avSession.onSessionDestroy((descriptor: avSession.AVSessionDescriptor) => {
12. });
13. avSession.offSessionDestroy();
14. })
15. }
16. .width('100%')
17. .height('100%')
18. }
19. }
```

## avSession.offTopSessionChange23+

PhonePC/2in1TabletTVWearable

offTopSessionChange(callback?: Callback<AVSessionDescriptor>): void

注销最新播放会话变更事件监听。注销后，不再进行该事件的监听。

**需要权限：** ohos.permission.MANAGE\_MEDIA\_RESOURCES\_FOR\_PUBLIC

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[AVSessionDescriptor](arkts-apis-avsession-i.md#avsessiondescriptor-23)> | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。  该参数为会话相关描述，为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | permission denied. |
| 6600101 | Session service exception. |

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
11. avSession.offTopSessionChange((descriptor: avSession.AVSessionDescriptor) => {
12. });
13. avSession.offTopSessionChange();
14. })
15. }
16. .width('100%')
17. .height('100%')
18. }
19. }
```

## avSession.isDesktopLyricSupported23+

PhonePC/2in1TabletTVWearable

isDesktopLyricSupported(): Promise<boolean>

设备是否支持桌面歌词功能。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示设备支持桌面歌词功能；返回false表示设备不支持桌面歌词功能。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](errorcode-avsession.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |

**示例：**

```
1. import { avSession } from '@kit.AVSessionKit';

3. avSession.isDesktopLyricSupported().then((isSupported: boolean) => {
4. console.info(`Succeeded in checking desktop lyric supported: ${isSupported}`);
5. });
```
