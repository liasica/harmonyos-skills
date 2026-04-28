---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-secureelement
title: @ohos.secureElement (安全单元的通道管理)
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > @ohos.secureElement (安全单元的通道管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:02+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:7b92449cc1410a3c38fd8200afe8fa27104c5e21565907e719e81b445727138f
---

本模块主要用于操作及管理安全单元（SecureElement，简称SE），电子设备上可能存在的安全单元有eSE（Embedded SE）和SIM卡。文档中出现的SE服务为SEService实例，参见[createService](js-apis-secureelement.md#omapicreateservice12)。

对于文档中出现以下类型说明：

| 类型 | 说明 |
| --- | --- |
| Reader | 此类的实例表示该设备支持的SE，如果支持eSE、SIM和SIM2，则返回3个实例，其中SIM2从API version 22开始支持。 |
| Session | 此类的实例表示在某个SE Reader实例上创建连接会话。 |
| Channel | 此类的实例表示在某个Session实例上创建通道，可能为基础通道或逻辑通道。 |

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## **导入模块**

PhoneWearable

```
1. import { omapi } from '@kit.ConnectivityKit';
```

## ServiceState

PhoneWearable

定义不同的SE服务状态值。

**系统能力：** SystemCapability.Communication.SecureElement

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DISCONNECTED | 0 | SE服务状态已断开。 |
| CONNECTED | 1 | SE服务状态已连接。 |

## omapi.newSEService(deprecated)

PhoneWearable

newSEService(type: 'serviceState', callback: Callback<ServiceState>): SEService

建立一个可用于连接到系统中所有可用SE的新连接（服务）。连接过程较为耗时，所以此方法仅提供异步方式进行的。使用callback异步回调。

仅当指定的回调或者当[isConnected](js-apis-secureelement.md#seserviceisconnected)方法返回true时，该返回SEService对象是可用的。

说明

从 API version 10 开始支持，从 API version 12 开始废弃，建议使用[createService](js-apis-secureelement.md#omapicreateservice12)替代。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 固定填'serviceState' 。 |
| callback | Callback<[ServiceState](js-apis-secureelement.md#servicestate)> | 是 | 返回SE服务状态的回调 。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| SEService | SE服务实例。 |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { omapi } from '@kit.ConnectivityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let seService : omapi.SEService;

6. function secureElementDemo() {
7. // 获取 service
8. try {
9. seService = omapi.newSEService("serviceState", (state) => {
10. hilog.info(0x0000, 'testTag', 'se service state = %{public}s', JSON.stringify(state));
11. });
12. } catch (error) {
13. hilog.error(0x0000, 'testTag', 'newSEService error %{public}s', JSON.stringify(error));
14. }
15. if (seService == undefined || !seService.isConnected()) {
16. hilog.error(0x0000, 'testTag', 'secure element service disconnected.');
17. return;
18. }
19. }
```

## omapi.createService12+

PhoneWearable

createService(): Promise<SEService>;

建立一个可用于连接到系统中所有可用SE的新连接（服务）。连接过程较为耗时，所以此方法仅提供异步方式。使用Promise异步回调。

仅当[isConnected](js-apis-secureelement.md#seserviceisconnected)方法返回true时，该返回SEService对象是可用的。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<[SEService](js-apis-secureelement.md#seservice)> | 以Promise形式异步返回可用的SE服务实例。 |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. import { omapi } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let seService : omapi.SEService;

7. function secureElementDemo() {
8. omapi.createService().then((data) => {
9. seService = data;
10. if (seService == undefined || !seService.isConnected()) {
11. hilog.error(0x0000, 'testTag', 'seservice state disconnected');
12. return;
13. }
14. hilog.info(0x0000, 'testTag', 'seservice state connected');
15. }).catch((error : BusinessError)=> {
16. hilog.error(0x0000, 'testTag', 'createService error %{public}s', JSON.stringify(error));
17. });
18. }
```

## omapi.on18+

PhoneWearable

on(type: 'stateChanged', callback: Callback<ServiceState>): void;

注册监听服务状态变化事件。

调用[omapi.newSEService](js-apis-secureelement.md#omapinewseservicedeprecated)或[omapi.createService](js-apis-secureelement.md#omapicreateservice12)创建服务成功后再用on接口注册回调。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 订阅监听的事件类型，固定填'stateChanged' 。 |
| callback | Callback<[ServiceState](js-apis-secureelement.md#servicestate)> | 是 | 返回SE服务状态的回调 。 |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

示例请参见[off](js-apis-secureelement.md#omapioff18)接口的示例。

## omapi.off18+

PhoneWearable

off(type: 'stateChanged', callback?: Callback<ServiceState>): void;

取消订阅服务状态更改事件。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅监听的事件类型，固定填'stateChanged' 。 |
| callback | Callback<[ServiceState](js-apis-secureelement.md#servicestate)> | 否 | 返回SE服务状态的回调 。 |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. import { omapi } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let seService: omapi.SEService;
6. function seStateOnCb(data: omapi.ServiceState) {
7. hilog.info(0x0000, 'testTag', 'omapi.on ServiceState: %{public}s', JSON.stringify(data));
8. }

10. function seStateOffCb(data: omapi.ServiceState) {
11. hilog.info(0x0000, 'testTag', 'omapi.off ServiceState: %{public}s', JSON.stringify(data));

13. }

15. function secureElementDemo() {
16. try{
17. omapi.createService().then((data) => {
18. seService = data;
19. if (seService == undefined || !seService.isConnected()) {
20. hilog.error(0x0000, 'testTag', 'seservice state disconnected');
21. return;
22. }
23. hilog.info(0x0000, 'testTag', 'seservice state connected');
24. }).catch((error : BusinessError)=> {
25. hilog.error(0x0000, 'testTag', 'createService error %{public}s', JSON.stringify(error));
26. });
27. omapi.on('stateChanged', seStateOnCb);
28. } catch (error) {
29. if (error as BusinessError) {
30. hilog.error(0x0000, 'testTag', 'omapi on error %{public}s', JSON.stringify(error));
31. }
32. }
33. try{
34. omapi.off('stateChanged', seStateOffCb);
35. } catch (error) {
36. if (error as BusinessError) {
37. hilog.error(0x0000, 'testTag', 'omapi off error %{public}s', JSON.stringify(error));
38. }
39. }
40. }
```

## SEService

PhoneWearable

SEService表示可用于连接到系统中所有可用SE的连接（服务），通过[createService](js-apis-secureelement.md#omapicreateservice12)获取SEService实例。

### SEService.getReaders

PhoneWearable

getReaders(): Reader[]

返回可用SE Reader的数组，包含该设备上支持的所有的安全单元。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [Reader](js-apis-secureelement.md#reader)[] | 返回可用Reader对象数组。 |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. import { omapi } from '@kit.ConnectivityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let seService : omapi.SEService;
5. let seReaders : omapi.Reader[];

7. // 在使用seService之前，需要对seService进行初始化
8. function secureElementDemo() {
9. // 获取readers
10. try {
11. seReaders = seService.getReaders();
12. } catch (error) {
13. hilog.error(0x0000, 'testTag', 'getReaders error %{public}s', JSON.stringify(error));
14. }
15. if (seReaders == undefined || seReaders.length == 0) {
16. hilog.error(0x0000, 'testTag', 'no valid reader found.');
17. // 释放SeService资源
18. seService.shutdown();
19. return;
20. }
21. }
```

### SEService.isConnected

PhoneWearable

isConnected(): boolean

检查SE服务是否已连接。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | true: SE服务状态已连接，false: SE服务状态已断开。 |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. import { omapi } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let seService : omapi.SEService;

7. function secureElementDemo() {
8. omapi.createService().then((data) => {
9. seService = data;
10. if (seService == undefined || !seService.isConnected()) {
11. hilog.error(0x0000, 'testTag', 'seservice state disconnected');
12. return;
13. }
14. hilog.info(0x0000, 'testTag', 'seservice state connected');
15. }).catch((error : BusinessError)=> {
16. hilog.error(0x0000, 'testTag', 'createService error %{public}s', JSON.stringify(error));
17. });
18. }
```

### SEService.shutdown

PhoneWearable

shutdown(): void

释放该Service分配的所有SE资源。此后[isConnected](js-apis-secureelement.md#seserviceisconnected)将返回false。

**系统能力：** SystemCapability.Communication.SecureElement

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. import { omapi } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let seService : omapi.SEService;

7. // 在使用seService之前，需要对seService进行初始化

9. try {
10. seService.shutdown();
11. } catch (error) {
12. hilog.error(0x0000, 'testTag', 'shutdown error %{public}s', JSON.stringify(error));
13. }
```

### SEService.getVersion

PhoneWearable

getVersion(): string

返回此实现所基于的Open Mobile API规范的版本号。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

| **类型** | **说明** |
| --- | --- |
| string | OMA版本号（例如，“3.3”表示Open Mobile API规范版本3.3） |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. import { omapi } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let seService : omapi.SEService;

7. // 在使用seService之前，需要对seService进行初始化

9. try {
10. let version = seService.getVersion();
11. hilog.error(0x0000, 'testTag', 'version %{public}s', JSON.stringify(version));
12. } catch (error) {
13. hilog.error(0x0000, 'testTag', 'getVersion error %{public}s', JSON.stringify(error));
14. }
```

## Reader

PhoneWearable

Reader的实例表示该设备支持的SE，如果支持eSE、SIM和SIM2，则返回3个实例，其中SIM2从API version 22开始支持。通过[SEService.getReaders](js-apis-secureelement.md#seservicegetreaders)获取Reader实例。

### Reader.getName

PhoneWearable

getName(): string

返回此Reader的名称。如果此读卡器是SIM Reader，则其名称必须为“SIM”。如果此读卡器是SIM2 Reader，则其名称必须为“SIM2”。如果读卡器是eSE，则其名称须为“eSE”。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

| **类型** | **说明** |
| --- | --- |
| string | [Reader](js-apis-secureelement.md#reader)名称。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { omapi } from '@kit.ConnectivityKit';

4. let seReaders : omapi.Reader[];

6. // 在使用seReaders之前，需要对seReaders进行初始化

8. try {
9. let reader = seReaders[0]; // 将其更改为所选的reader：eSE、SIM、SIM2
10. let name = reader.getName();
11. hilog.info(0x0000, 'testTag', 'name %{public}s', JSON.stringify(name));
12. } catch (error) {
13. hilog.error(0x0000, 'testTag', 'getName error %{public}s', JSON.stringify(error));
14. }
```

### Reader.isSecureElementPresent

PhoneWearable

isSecureElementPresent(): boolean

检查当前Reader所对应的安全单元是否可用。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | true: 安全单元可用， false: 安全单元不可用。 |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 3300101 | IllegalStateError, service state exception. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { omapi } from '@kit.ConnectivityKit';

4. let seReaders : omapi.Reader[];

6. // 在使用seReaders之前，需要对seReaders进行初始化

8. try {
9. let reader = seReaders[0]; // 将其更改为所选的reader：eSE、SIM、SIM2
10. let isPresent = reader.isSecureElementPresent();
11. hilog.info(0x0000, 'testTag', 'isPresent %{public}s', JSON.stringify(isPresent));
12. } catch (error) {
13. hilog.error(0x0000, 'testTag', 'isSecureElementPresent error %{public}s', JSON.stringify(error));
14. }
```

### Reader.openSession

PhoneWearable

openSession(): Session

在SE Reader实例上创建连接会话，返回Session实例。在一个Reader上可能同时打开多个会话。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [Session](js-apis-secureelement.md#session) | 连接会话Session实例。 |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 3300101 | IllegalStateError, service state exception. |
| 3300104 | IOError, there is a communication problem to the reader or the SE. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { omapi } from '@kit.ConnectivityKit';

4. let seReaders : omapi.Reader[];
5. let seSession : omapi.Session;

7. // 在使用seReaders之前，需要对seReaders进行初始化
8. function secureElementDemo() {
9. try {
10. let reader = seReaders[0]; // 将其更改为所选的reader：eSE、SIM、SIM2
11. seSession = reader.openSession();
12. } catch (error) {
13. hilog.error(0x0000, 'testTag', 'openSession error %{public}s', JSON.stringify(error));
14. }
15. if (seSession == undefined) {
16. hilog.error(0x0000, 'testTag', 'seSession invalid.');
17. return;
18. }
19. }
```

### Reader.closeSessions

PhoneWearable

closeSessions(): void

关闭在此Reader上打开的所有Session。所有这些Session打开的所有Channel都将关闭。

**系统能力：** SystemCapability.Communication.SecureElement

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 3300101 | IllegalStateError, service state exception. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { omapi } from '@kit.ConnectivityKit';

4. let seReaders : omapi.Reader[];
5. let seSession : omapi.Session;
6. let reader : omapi.Reader;

8. // 在使用seReaders之前，需要对seReaders进行初始化
9. function secureElementDemo() {
10. try {
11. reader = seReaders[0]; // 将其更改为所选的reader：eSE、SIM、SIM2
12. seSession = reader.openSession();
13. } catch (error) {
14. hilog.error(0x0000, 'testTag', 'openSession error %{public}s', JSON.stringify(error));
15. }
16. if (seSession == undefined) {
17. hilog.error(0x0000, 'testTag', 'seSession invalid.');
18. // 释放SeService资源
19. seService.shutdown();
20. return;
21. }
22. try {
23. reader.closeSessions();
24. } catch (error) {
25. hilog.error(0x0000, 'testTag', 'closeSessions error %{public}s', JSON.stringify(error));
26. }
27. }
```

## Session

PhoneWearable

Session的实例表示在某个SE Reader实例上创建连接会话。通过[Reader.openSession](js-apis-secureelement.md#readeropensession)获取Session实例。

### Session.getReader

PhoneWearable

getReader(): Reader

获取提供此Session的Reader实例。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [Reader](js-apis-secureelement.md#reader) | 返回此Session的Reader实例。 |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { omapi } from '@kit.ConnectivityKit';

4. let seReaders : omapi.Reader[];
5. let seSession : omapi.Session;
6. let reader : omapi.Reader;

8. // 在使用seReaders之前，需要对seReaders进行初始化
9. function secureElementDemo() {
10. try {
11. reader = seReaders[0]; // 将其更改为所选的reader：eSE、SIM、SIM2
12. seSession = reader.openSession();
13. } catch (error) {
14. hilog.error(0x0000, 'testTag', 'openSession error %{public}s', JSON.stringify(error));
15. }
16. if (seSession == undefined) {
17. hilog.error(0x0000, 'testTag', 'seSession invalid.');
18. return;
19. }
20. try {
21. let sessionReader = seSession.getReader();
22. } catch (error) {
23. hilog.error(0x0000, 'testTag', 'getReader error %{public}s', JSON.stringify(error));
24. }
25. }
```

### Session.getATR

PhoneWearable

getATR(): number[]

获取该SE的ATR。如果该SE的ATR不可用，则应返回空数组。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number[] | 返回SE的ATR，SE的ATR不可用时，返回空的数组。 |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 3300101 | IllegalStateError, service state exception. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { omapi } from '@kit.ConnectivityKit';

4. let seSession : omapi.Session;

6. // 在使用seSession之前，需要对seSession进行初始化

8. try {
9. let atr = seSession.getATR();
10. hilog.info(0x0000, 'testTag', 'atr %{public}s', JSON.stringify(atr));
11. } catch (error) {
12. hilog.error(0x0000, 'testTag', 'getATR error %{public}s', JSON.stringify(error));
13. }
```

### Session.close

PhoneWearable

close(): void

关闭与SE的当前会话连接。这将关闭此Session打开的所有Channel。

**系统能力：** SystemCapability.Communication.SecureElement

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 3300101 | IllegalStateError, service state exception. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { omapi } from '@kit.ConnectivityKit';

4. let seSession : omapi.Session;

6. // 在使用seSession之前，需要对seSession进行初始化

8. try {
9. seSession.close();
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'close error %{public}s', JSON.stringify(error));
12. }
```

### Session. isClosed

PhoneWearable

isClosed(): boolean

检查Session是否关闭。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | true：Session状态已关闭，false：Session是打开的。 |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { omapi } from '@kit.ConnectivityKit';

4. let seSession : omapi.Session;

6. // 在使用seSession之前，需要对seSession进行初始化

8. try {
9. let isClosed = seSession.isClosed();
10. hilog.info(0x0000, 'testTag', 'isClosed %{public}s', JSON.stringify(isClosed));
11. } catch (error) {
12. hilog.error(0x0000, 'testTag', 'isClosed error %{public}s', JSON.stringify(error));
13. }
```

### Session.closeChannels

PhoneWearable

closeChannels(): void

关闭此Session上打开的所有Channel。

**系统能力：** SystemCapability.Communication.SecureElement

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 3300101 | IllegalStateError, service state exception. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { omapi } from '@kit.ConnectivityKit';

4. let seSession : omapi.Session;

6. // 在使用seSession之前，需要对seSession进行初始化

8. try {
9. seSession.closeChannels();
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'closeChannels error %{public}s', JSON.stringify(error));
12. }
```

### Session.openBasicChannel

PhoneWearable

openBasicChannel(aid: number[]): Promise<Channel>

打开基础通道，参考[ISO 7816-4]协议，返回基础Channel实例对象。SE不能提供基础Channel或应用程序没有访问SE的权限时，返回null。使用Promise异步回调。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| aid | number[] | 是 | 在此Channel上选择的Applet的AID或如果没有Applet被选择时空的数组。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<[Channel](js-apis-secureelement.md#channel)> | 以Promise形式异步返回可用的基础Channel对象实例。 |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3300101 | IllegalStateError, an attempt is made to use an SE session that has been closed. |
| 3300102 | NoSuchElementError, the AID on the SE is not available or cannot be selected. |
| 3300103 | SecurityError, the calling application cannot be granted access to this AID or the default applet on this session. |
| 3300104 | IOError, there is a communication problem to the reader or the SE. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { omapi } from '@kit.ConnectivityKit';

4. let seSession : omapi.Session;
5. let seChannel : omapi.Channel;
6. let aidArray : number[] = [0xA0, 0x00, 0x00, 0x00, 0x03, 0x10, 0x10];

8. // 在使用seSession之前，需要对seSession进行初始化
9. function secureElementDemo() {
10. try {
11. // 改为在此channel上选择的App的aid
12. seSession.openBasicChannel(aidArray).then((data) => {
13. seChannel = data;
14. }).catch((error : BusinessError)=> {
15. hilog.error(0x0000, 'testTag', 'openBasicChannel error %{public}s', JSON.stringify(error));
16. });
17. } catch (exception) {
18. hilog.error(0x0000, 'testTag', 'openBasicChannel exception %{public}s', JSON.stringify(exception));
19. }
20. if (seChannel == undefined) {
21. hilog.error(0x0000, 'testTag', 'seChannel invalid.');
22. return;
23. }
24. }
```

### Session.openBasicChannel

PhoneWearable

openBasicChannel(aid: number[], callback: AsyncCallback<Channel>): void

打开基础通道，参考[ISO 7816-4]协议，返回基础Channel实例对象。SE不能提供基础Channel或应用程序没有访问SE的权限时，返回null。使用callback异步回调。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| aid | number[] | 是 | 在此Channel上选择的Applet的AID或如果没有Applet被选择时空的数组。 |
| callback | AsyncCallback<[Channel](js-apis-secureelement.md#channel)> | 是 | 以callback形式异步返回可用的基础Channel对象实例。 |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3300101 | IllegalStateError, an attempt is made to use an SE session that has been closed. |
| 3300102 | NoSuchElementError, the AID on the SE is not available or cannot be selected. |
| 3300103 | SecurityError, the calling application cannot be granted access to this AID or the default applet on this session. |
| 3300104 | IOError, there is a communication problem to the reader or the SE. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { omapi } from '@kit.ConnectivityKit';

4. let seSession : omapi.Session;
5. let seChannel : omapi.Channel;
6. let aidArray : number[] = [0xA0, 0x00, 0x00, 0x00, 0x03, 0x10, 0x10];

8. // 在使用seSession之前，需要对seSession进行初始化
9. function secureElementDemo() {
10. try {
11. // 改为在此channel上选择的App的aid
12. seSession.openBasicChannel(aidArray, (error, data) => {
13. if (error) {
14. hilog.error(0x0000, 'testTag', 'openBasicChannel error %{public}s', JSON.stringify(error));
15. } else {
16. seChannel = data;
17. }
18. });
19. } catch (exception) {
20. hilog.error(0x0000, 'testTag', 'openBasicChannel exception %{public}s', JSON.stringify(exception));
21. }
22. if (seChannel == undefined) {
23. hilog.error(0x0000, 'testTag', 'seChannel invalid.');
24. return;
25. }
26. }
```

### Session.openBasicChannel

PhoneWearable

openBasicChannel(aid: number[], p2: number): Promise<Channel>

打开基础通道，参考[ISO 7816-4]协议，返回基础Channel实例对象。SE不能提供基础Channel或应用程序没有访问SE的权限时，返回null。使用Promise异步回调。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| aid | number[] | 是 | 在此Channel上选择的Applet的AID或如果没有Applet被选择时空的数组。 |
| p2 | number | 是 | 在该Channel上执行的SELECT APDU的P2参数。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<[Channel](js-apis-secureelement.md#channel)> | 以Promise形式异步返回可用的基础Channel对象实例。 |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3300101 | IllegalStateError, an attempt is made to use an SE session that has been closed. |
| 3300102 | NoSuchElementError, the AID on the SE is not available or cannot be selected. |
| 3300103 | SecurityError, the calling application cannot be granted access to this AID or the default applet on this session. |
| 3300104 | IOError, there is a communication problem to the reader or the SE. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { omapi } from '@kit.ConnectivityKit';

4. let seSession : omapi.Session;
5. let seChannel : omapi.Channel;
6. let aidArray : number[] = [0xA0, 0x00, 0x00, 0x00, 0x03, 0x10, 0x10];
7. let p2 : number = 0x00;

9. // 在使用seSession之前，需要对seSession进行初始化
10. function secureElementDemo() {
11. try {
12. // 改为在此channel上选择的App的aid
13. seSession.openBasicChannel(aidArray, p2).then((data) => {
14. seChannel = data;
15. }).catch((error : BusinessError)=> {
16. hilog.error(0x0000, 'testTag', 'openBasicChannel error %{public}s', JSON.stringify(error));
17. });
18. } catch (exception) {
19. hilog.error(0x0000, 'testTag', 'openBasicChannel exception %{public}s', JSON.stringify(exception));
20. }
21. if (seChannel == undefined) {
22. hilog.error(0x0000, 'testTag', 'seChannel invalid.');
23. return;
24. }
25. }
```

### Session.openBasicChannel

PhoneWearable

openBasicChannel(aid: number[], p2:number, callback: AsyncCallback<Channel>): void

打开基础通道，参考[ISO 7816-4]协议，返回基础Channel实例对象。SE不能提供基础Channel或应用程序没有访问SE的权限时，返回null。使用callback异步回调。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| aid | number[] | 是 | 在此Channel上选择的Applet的AID或如果没有Applet被选择时空的数组。 |
| p2 | number | 是 | 此Channel上执行SELECT APDU命令的P2参数。 |
| callback | AsyncCallback<[Channel](js-apis-secureelement.md#channel)> | 是 | 以callback形式异步返回可用的基础Channel对象实例。 |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3300101 | IllegalStateError, an attempt is made to use an SE session that has been closed. |
| 3300102 | NoSuchElementError, the AID on the SE is not available or cannot be selected. |
| 3300103 | SecurityError, the calling application cannot be granted access to this AID or the default applet on this session. |
| 3300104 | IOError, there is a communication problem to the reader or the SE. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { omapi } from '@kit.ConnectivityKit';

4. let seSession : omapi.Session;
5. let seChannel : omapi.Channel;
6. let aidArray : number[] = [0xA0, 0x00, 0x00, 0x00, 0x03, 0x10, 0x10];
7. let p2 : number = 0x00;

9. // 在使用seSession之前，需要对seSession进行初始化
10. function secureElementDemo() {
11. try {
12. // 改为在此channel上选择的App的aid
13. seSession.openBasicChannel(aidArray, p2, (error, data) => {
14. if (error) {
15. hilog.error(0x0000, 'testTag', 'openBasicChannel error %{public}s', JSON.stringify(error));
16. } else {
17. seChannel = data;
18. }
19. });
20. } catch (exception) {
21. hilog.error(0x0000, 'testTag', 'openBasicChannel exception %{public}s', JSON.stringify(exception));
22. }
23. if (seChannel == undefined) {
24. hilog.error(0x0000, 'testTag', 'seChannel invalid.');
25. return;
26. }
27. }
```

### Session.openLogicalChannel

PhoneWearable

openLogicalChannel(aid: number[]): Promise<Channel>

打开逻辑通道，参考[ISO 7816-4]协议，返回逻辑Channel实例对象。SE不能提供逻辑Channel或应用程序没有访问SE的权限时，返回null。使用Promise异步回调。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| aid | number[] | 是 | 在此Channel上选择的Applet的AID或如果没有Applet被选择时空的数组。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<[Channel](js-apis-secureelement.md#channel)> | 以Promise形式异步返回可用的逻辑Channel对象实例。 |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3300101 | IllegalStateError, an attempt is made to use an SE session that has been closed. |
| 3300102 | NoSuchElementError, the AID on the SE is not available or cannot be selected or a logical channel is already open to a non-multi-selectable applet. |
| 3300103 | SecurityError, the calling application cannot be granted access to this AID or the default applet on this session. |
| 3300104 | IOError, there is a communication problem to the reader or the SE. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { omapi } from '@kit.ConnectivityKit';

4. let seSession : omapi.Session;
5. let seChannel : omapi.Channel;
6. let aidArray : number[] = [0xA0, 0x00, 0x00, 0x00, 0x03, 0x10, 0x10];

8. // 在使用seSession之前，需要对seSession进行初始化
9. function secureElementDemo() {
10. try {
11. // 改为在此channel上选择的App的aid
12. seSession.openLogicalChannel(aidArray).then((data) => {
13. seChannel = data;
14. }).catch((error : BusinessError)=> {
15. hilog.error(0x0000, 'testTag', 'openLogicalChannel error %{public}s', JSON.stringify(error));
16. });
17. } catch (exception) {
18. hilog.error(0x0000, 'testTag', 'openLogicalChannel exception %{public}s', JSON.stringify(exception));
19. }
20. if (seChannel == undefined) {
21. hilog.error(0x0000, 'testTag', 'seChannel invalid.');
22. return;
23. }
24. }
```

### Session.openLogicalChannel

PhoneWearable

openLogicalChannel(aid: number[], callback: AsyncCallback<Channel>): void

打开逻辑通道，参考[ISO 7816-4]协议，返回逻辑Channel实例对象。SE不能提供逻辑Channel或应用程序没有访问SE的权限时，返回null。使用callback异步回调。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| aid | number[] | 是 | 在此Channel上选择的Applet的AID或如果没有Applet被选择时空的数组。 |
| callback | AsyncCallback<[Channel](js-apis-secureelement.md#channel)> | 是 | 以callback形式异步返回可用的逻辑Channel对象实例。 |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3300101 | IllegalStateError, an attempt is made to use an SE session that has been closed. |
| 3300102 | NoSuchElementError, the AID on the SE is not available or cannot be selected or a logical channel is already open to a non-multi-selectable applet. |
| 3300103 | SecurityError, the calling application cannot be granted access to this AID or the default applet on this session. |
| 3300104 | IOError, there is a communication problem to the reader or the SE. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { omapi } from '@kit.ConnectivityKit';

4. let seSession : omapi.Session;
5. let seChannel : omapi.Channel;
6. let aidArray : number[] = [0xA0, 0x00, 0x00, 0x00, 0x03, 0x10, 0x10];

8. // 在使用seSession之前，需要对seSession进行初始化
9. function secureElementDemo() {
10. try {
11. // 改为在此channel上选择的App的aid
12. seSession.openLogicalChannel(aidArray, (error, data) => {
13. if (error) {
14. hilog.error(0x0000, 'testTag', 'openLogicalChannel error %{public}s', JSON.stringify(error));
15. } else {
16. seChannel = data;
17. }
18. });
19. } catch (exception) {
20. hilog.error(0x0000, 'testTag', 'openLogicalChannel exception %{public}s', JSON.stringify(exception));
21. }
22. if (seChannel == undefined) {
23. hilog.error(0x0000, 'testTag', 'seChannel invalid.');
24. return;
25. }
26. }
```

### Session.openLogicalChannel

PhoneWearable

openLogicalChannel(aid: number[], p2: number): Promise<Channel>

打开逻辑通道，参考[ISO 7816-4]协议，返回逻辑Channel实例对象。SE不能提供逻辑Channel或应用程序没有访问SE的权限时，返回null。使用Promise异步回调。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| aid | number[] | 是 | 在此Channel上选择的Applet的AID或如果没有Applet被选择时空的数组。 |
| p2 | number | 是 | 此Channel上执行SELECT APDU命令的P2参数。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<[Channel](js-apis-secureelement.md#channel)> | 以Promise形式异步返回可用的逻辑Channel实例对象。 |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3300101 | IllegalStateError, an attempt is made to use an SE session that has been closed. |
| 3300102 | NoSuchElementError, the AID on the SE is not available or cannot be selected or a logical channel is already open to a non-multi-selectable applet. |
| 3300103 | SecurityError, the calling application cannot be granted access to this AID or the default applet on this session. |
| 3300104 | IOError, there is a communication problem to the reader or the SE. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { omapi } from '@kit.ConnectivityKit';

4. let seSession : omapi.Session;
5. let seChannel : omapi.Channel;
6. let aidArray : number[] = [0xA0, 0x00, 0x00, 0x00, 0x03, 0x10, 0x10];
7. let p2 : number = 0x00;

9. // 在使用seSession之前，需要对seSession进行初始化
10. function secureElementDemo() {
11. try {
12. // 改为在此channel上选择的App的aid
13. seSession.openLogicalChannel(aidArray, p2).then((data) => {
14. seChannel = data;
15. }).catch((error : BusinessError)=> {
16. hilog.error(0x0000, 'testTag', 'openLogicalChannel error %{public}s', JSON.stringify(error));
17. });
18. } catch (exception) {
19. hilog.error(0x0000, 'testTag', 'openLogicalChannel exception %{public}s', JSON.stringify(exception));
20. }
21. if (seChannel == undefined) {
22. hilog.error(0x0000, 'testTag', 'seChannel invalid.');
23. return;
24. }
25. }
```

### Session.openLogicalChannel

PhoneWearable

openLogicalChannel(aid: number[], p2: number, callback: AsyncCallback<Channel>):void

打开逻辑通道，参考[ISO 7816-4]协议，返回Channel实例对象。SE不能提供逻辑Channel或应用程序没有访问SE的权限时，返回null。使用callback异步回调。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| aid | number[] | 是 | 在此Channel上选择的Applet的AID或如果没有Applet被选择时空的数组。 |
| p2 | number | 是 | 此Channel上执行SELECT APDU命令的P2参数。 |
| callback | AsyncCallback<[Channel](js-apis-secureelement.md#channel)> | 是 | 以callback形式异步返回可用的逻辑Channel对象实例。 |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3300101 | IllegalStateError, an attempt is made to use an SE session that has been closed. |
| 3300102 | NoSuchElementError, the AID on the SE is not available or cannot be selected or a logical channel is already open to a non-multi-selectable applet. |
| 3300103 | SecurityError, the calling application cannot be granted access to this AID or the default applet on this session. |
| 3300104 | IOError, there is a communication problem to the reader or the SE. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { omapi } from '@kit.ConnectivityKit';

4. let seSession : omapi.Session;
5. let seChannel : omapi.Channel;
6. let aidArray : number[] = [0xA0, 0x00, 0x00, 0x00, 0x03, 0x10, 0x10];
7. let p2 : number = 0x00;

9. // 在使用seSession之前，需要对seSession进行初始化
10. function secureElementDemo() {
11. try {
12. // 改为在此channel上选择的App的aid
13. seSession.openLogicalChannel(aidArray, p2, (error, data) => {
14. if (error) {
15. hilog.error(0x0000, 'testTag', 'openLogicalChannel error %{public}s', JSON.stringify(error));
16. } else {
17. seChannel = data;
18. }
19. });
20. } catch (exception) {
21. hilog.error(0x0000, 'testTag', 'openLogicalChannel exception %{public}s', JSON.stringify(exception));
22. }
23. if (seChannel == undefined) {
24. hilog.error(0x0000, 'testTag', 'seChannel invalid.');
25. return;
26. }
27. }
```

## Channel

PhoneWearable

Channel的实例表示在某个Session实例上创建通道，可能为基础通道或逻辑通道。通过[Session.openBasicChannel](js-apis-secureelement.md#sessionopenbasicchannel)或[Session.openLogicalChannel](js-apis-secureelement.md#sessionopenlogicalchannel)获取Channel实例。

### Channel.getSession

PhoneWearable

getSession(): Session

获取打开该Channel的Session对象。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [Session](js-apis-secureelement.md#session) | 该Channel绑定的Session 对象。 |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { omapi } from '@kit.ConnectivityKit';

4. let seSession : omapi.Session;
5. let seChannel : omapi.Channel;

7. // 在使用seChannel之前，需要对seChannel进行初始化

9. try {
10. seSession = seChannel.getSession();
11. } catch (exception) {
12. hilog.error(0x0000, 'testTag', 'getSession exception %{public}s', JSON.stringify(exception));
13. }
```

### Channel.close

PhoneWearable

close(): void

关闭Channel。

**系统能力：** SystemCapability.Communication.SecureElement

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { omapi } from '@kit.ConnectivityKit';

4. let seChannel : omapi.Channel;

6. // 在使用seChannel之前，需要对seChannel进行初始化
7. try {
8. seChannel.close();
9. } catch (exception) {
10. hilog.error(0x0000, 'testTag', 'close exception %{public}s', JSON.stringify(exception));
11. }
```

### Channel.isBasicChannel

PhoneWearable

isBasicChannel(): boolean

检查该Channel是否为基础Channel。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | true: 该Channel是基础Channel, false：该Channel逻辑Channel 。 |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { omapi } from '@kit.ConnectivityKit';

4. let seChannel : omapi.Channel;

6. // 在使用seChannel之前，需要对seChannel进行初始化
7. try {
8. let isBasic = seChannel.isBasicChannel();
9. hilog.info(0x0000, 'testTag', 'isBasic = %{public}s', JSON.stringify(isBasic));
10. } catch (exception) {
11. hilog.error(0x0000, 'testTag', 'isBasicChannel exception %{public}s', JSON.stringify(exception));
12. }
```

### Channel.isClosed

PhoneWearable

isClosed(): boolean

检查该Channel是否已被关闭。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | true: Channel是关闭的，false: 不是关闭的。 |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { omapi } from '@kit.ConnectivityKit';

4. let seChannel : omapi.Channel;

6. // 在使用seChannel之前，需要对seChannel进行初始化
7. try {
8. let isClosed = seChannel.isClosed();
9. hilog.info(0x0000, 'testTag', 'isClosed = %{public}s', JSON.stringify(isClosed));
10. } catch (exception) {
11. hilog.error(0x0000, 'testTag', 'isClosed exception %{public}s', JSON.stringify(exception));
12. }
```

### Channel.getSelectResponse

PhoneWearable

getSelectResponse(): number[]

获取SELECT Applet时的响应数据，包含状态字。

**系统能力：** SystemCapability.Communication.SecureElement

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number[] | SELECT Applet时的响应数据，包含状态字。 |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { omapi } from '@kit.ConnectivityKit';

4. let seChannel : omapi.Channel;

6. // 在使用seChannel之前，需要对seChannel进行初始化
7. try {
8. let response = seChannel.getSelectResponse();
9. hilog.info(0x0000, 'testTag', 'response = %{public}s', JSON.stringify(response));
10. } catch (exception) {
11. hilog.error(0x0000, 'testTag', 'getSelectResponse exception %{public}s', JSON.stringify(exception));
12. }
```

### Channel.transmit

PhoneWearable

transmit(command: number[]): Promise<number[]>

向SE发送APDU数据，数据符合ISO/IEC 7816规范。使用Promise异步回调。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| command | number[] | 是 | 需要发送到SE的APDU数据。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<number[]> | 以Promise形式异步返回接收到的响应APDU数据，number数组。若芯片捕获未知异常则返回全0。 |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3300101 | IllegalStateError, an attempt is made to use an SE session or channel that has been closed. |
| 3300103 | SecurityError, the command is filtered by the security policy. |
| 3300104 | IOError, there is a communication problem to the reader or the SE. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { omapi } from '@kit.ConnectivityKit';

4. let seChannel : omapi.Channel;

6. // 在使用seChannel之前，需要对seChannel进行初始化
7. let cmdData = [0x01, 0x02, 0x03, 0x04]; // 请更改为正确的data
8. try {
9. seChannel.transmit(cmdData).then((response) => {
10. // 若芯片捕获未知异常则response返回全0
11. hilog.info(0x0000, 'testTag', 'transmit response = %{public}s.', JSON.stringify(response));
12. }).catch((error : BusinessError) => {
13. hilog.error(0x0000, 'testTag', 'transmit error = %{public}s.', JSON.stringify(error));
14. });
15. } catch (exception) {
16. hilog.error(0x0000, 'testTag', 'transmit exception = %{public}s.', JSON.stringify(exception));
17. }
```

### Channel.transmit

PhoneWearable

transmit(command: number[], callback: AsyncCallback<number[]>): void

向SE发送APDU数据，数据符合ISO/IEC 7816规范。使用callback异步回调。

**系统能力：** SystemCapability.Communication.SecureElement

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| command | number[] | 是 | 需要发送到SE的APDU数据。 |
| callback | AsyncCallback<number[]> | 是 | 返回接收到的响应APDU数据，number数组。若芯片捕获未知异常则返回全0。 |

**错误码：**

错误码的详细介绍请参见[SE(secureElement)错误码](errorcode-se.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3300101 | IllegalStateError, an attempt is made to use an SE session or channel that has been closed. |
| 3300103 | SecurityError, the command is filtered by the security policy. |
| 3300104 | IOError, there is a communication problem to the reader or the SE. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { omapi } from '@kit.ConnectivityKit';

4. let seChannel : omapi.Channel;

6. // 在使用seChannel之前，需要对seChannel进行初始化
7. let cmdData = [0x01, 0x02, 0x03, 0x04]; // 请更改为正确的data
8. try {
9. seChannel.transmit(cmdData, (error, response) => {
10. if (error) {
11. hilog.error(0x0000, 'testTag', 'transmit error %{public}s', JSON.stringify(error));
12. } else {
13. // 若芯片捕获未知异常则response返回全0
14. hilog.info(0x0000, 'testTag', 'transmit response = %{public}s.', JSON.stringify(response));
15. }
16. });
17. } catch (exception) {
18. hilog.error(0x0000, 'testTag', 'transmit exception %{public}s', JSON.stringify(exception));
19. }
```
