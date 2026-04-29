---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-wantagent
title: @ohos.app.ability.wantAgent (WantAgent模块)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 通用能力的接口(推荐) > @ohos.app.ability.wantAgent (WantAgent模块)
category: harmonyos-references
scraped_at: 2026-04-29T13:48:46+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:62b1abe1fee77441d1d6e0d7ef33547c5932ad6a121b95db32c198b6175c8a0d
---

WantAgent模块封装了[Want](js-apis-app-ability-want.md)对象，允许应用程序在未来的某个时间点触发WantAgent实例执行指定操作（如启动Ability、发送公共事件等）。

该模块提供了创建WantAgent实例、获取WantAgent实例所属应用的包名、获取WantAgent实例所属应用的UID、主动触发WantAgent实例、判断两个WantAgent实例是否相等等功能。WantAgent的一个典型应用场景是通知处理。例如，当用户点击通知时，会触发WantAgent的[trigger](js-apis-app-ability-wantagent.md#wantagenttrigger)接口，并拉起目标应用。具体使用请参考[通知模块](../harmonyos-guides/notification-with-wantagent.md)。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { wantAgent } from '@kit.AbilityKit';
```

## wantAgent.getWantAgent

PhonePC/2in1TabletTVWearable

getWantAgent(info: WantAgentInfo, callback: AsyncCallback<WantAgent>): void

创建WantAgent，使用callback异步回调。创建成功返回WantAgent对象，创建失败返回空值。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [WantAgentInfo](js-apis-inner-wantagent-wantagentinfo.md) | 是 | 表示创建WantAgent所需的配置信息，包括目标UIAbility、操作类型、请求码等。三方应用在WantAgentInfo中只能设置本应用的UIAbility。 |
| callback | AsyncCallback<WantAgent> | 是 | 回调函数。当创建WantAgent成功，err为undefined，data为创建的WantAgent；否则err为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16000007 | Service busy. There are concurrent tasks. Try again later. |
| 16000151 | Invalid wantAgent object. |

**示例：**

```
1. import { wantAgent, Want } from '@kit.AbilityKit';
2. import type { WantAgent } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // wantAgent对象
6. let wantAgentData: WantAgent;
7. // WantAgentInfo对象
8. let wantAgentInfo: wantAgent.WantAgentInfo = {
9. wants: [
10. {
11. deviceId: 'deviceId',
12. bundleName: 'com.example.myapplication',
13. abilityName: 'EntryAbility',
14. action: 'action1',
15. entities: ['entity1'],
16. type: 'MIMETYPE',
17. uri: 'key={true,true,false}',
18. parameters:
19. {
20. mykey0: 2222,
21. mykey1: [1, 2, 3],
22. mykey2: '[1, 2, 3]',
23. mykey3: 'ssssssssssssssssssssssssss',
24. mykey4: [false, true, false],
25. mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
26. mykey6: true,
27. }
28. } as Want
29. ],
30. actionType: wantAgent.OperationType.START_ABILITY,
31. requestCode: 0,
32. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
33. };

35. // getWantAgent回调
36. function getWantAgentCallback(err: BusinessError, data: WantAgent) {
37. if (err.code) {
38. console.error(`getWantAgent failed, code: ${JSON.stringify(err.code)}, message: ${JSON.stringify(err.message)}`);
39. } else {
40. wantAgentData = data;
41. }
42. }

44. try {
45. wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
46. } catch (err) {
47. console.error(`getWantAgent failed, error: ${JSON.stringify(err)}`);
48. }
```

## wantAgent.getWantAgent

PhonePC/2in1TabletTVWearable

getWantAgent(info: WantAgentInfo): Promise<WantAgent>

创建WantAgent。使用Promise异步回调。创建成功返回WantAgent对象，创建失败返回空值。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [WantAgentInfo](js-apis-inner-wantagent-wantagentinfo.md) | 是 | 表示创建WantAgent所需的配置信息，包括目标UIAbility、操作类型、请求码等。三方应用在WantAgentInfo中只能设置本应用的UIAbility。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[WantAgent](js-apis-app-ability-wantagent.md#wantagent)> | Promise对象，返回创建的WantAgent。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16000007 | Service busy. There are concurrent tasks. Try again later. |
| 16000151 | Invalid wantAgent object. |

**示例：**

```
1. import { wantAgent, Want } from '@kit.AbilityKit';
2. import type { WantAgent } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let wantAgentData: WantAgent;
6. // WantAgentInfo对象
7. let wantAgentInfo: wantAgent.WantAgentInfo = {
8. wants: [
9. {
10. deviceId: 'deviceId',
11. bundleName: 'com.example.myapplication',
12. abilityName: 'EntryAbility',
13. action: 'action1',
14. entities: ['entity1'],
15. type: 'MIMETYPE',
16. uri: 'key={true,true,false}',
17. parameters:
18. {
19. mykey0: 2222,
20. mykey1: [1, 2, 3],
21. mykey2: '[1, 2, 3]',
22. mykey3: 'ssssssssssssssssssssssssss',
23. mykey4: [false, true, false],
24. mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
25. mykey6: true,
26. }
27. } as Want
28. ],
29. actionType: wantAgent.OperationType.START_ABILITY,
30. requestCode: 0,
31. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
32. };

34. try {
35. wantAgent.getWantAgent(wantAgentInfo).then((data) => {
36. wantAgentData = data;
37. }).catch((err: BusinessError) => {
38. console.error(`getWantAgent failed, code: ${JSON.stringify(err.code)}, message: ${JSON.stringify(err.message)}`);
39. });
40. } catch (err) {
41. console.error(`getWantAgent failed! ${err.code} ${err.message}`);
42. }
```

## wantAgent.getBundleName

PhonePC/2in1TabletTVWearable

getBundleName(agent: WantAgent, callback: AsyncCallback<string>): void

获取WantAgent实例所属应用的包名，使用callback异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agent | WantAgent | 是 | WantAgent对象。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当获取包名成功，err为undefined，data为创建的WantAgent；否则err为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16000007 | Service busy. There are concurrent tasks. Try again later. |
| 16000151 | Invalid wantAgent object. |

**示例：**

```
1. import { wantAgent, Want } from '@kit.AbilityKit';
2. import type { WantAgent } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // wantAgent对象
6. let wantAgentData: WantAgent;
7. // WantAgentInfo对象
8. let wantAgentInfo: wantAgent.WantAgentInfo = {
9. wants: [
10. {
11. deviceId: 'deviceId',
12. bundleName: 'com.example.myapplication',
13. abilityName: 'EntryAbility',
14. action: 'action1',
15. entities: ['entity1'],
16. type: 'MIMETYPE',
17. uri: 'key={true,true,false}',
18. parameters:
19. {
20. mykey0: 2222,
21. mykey1: [1, 2, 3],
22. mykey2: '[1, 2, 3]',
23. mykey3: 'ssssssssssssssssssssssssss',
24. mykey4: [false, true, false],
25. mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
26. mykey6: true,
27. }
28. } as Want
29. ],
30. actionType: wantAgent.OperationType.START_ABILITY,
31. requestCode: 0,
32. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
33. };

35. // getWantAgent回调
36. function getWantAgentCallback(err: BusinessError, data: WantAgent) {
37. if (err) {
38. console.error(`getWantAgent failed, code: ${JSON.stringify(err.code)}, message: ${JSON.stringify(err.message)}`);
39. } else {
40. wantAgentData = data;
41. }
42. // getBundleName回调
43. let getBundleNameCallback = (err: BusinessError, data: string) => {
44. if (err) {
45. console.error(`getBundleName failed! ${err.code} ${err.message}`);
46. } else {
47. console.info(`getBundleName ok! ${JSON.stringify(data)}`);
48. }
49. }
50. try {
51. wantAgent.getBundleName(wantAgentData, getBundleNameCallback);
52. } catch (err) {
53. console.error(`getBundleName failed! ${err.code} ${err.message}`);
54. }
55. }

57. try {
58. wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
59. } catch (err) {
60. console.error(`getWantAgent failed! ${err.code} ${err.message}`);
61. }
```

## wantAgent.getBundleName

PhonePC/2in1TabletTVWearable

getBundleName(agent: WantAgent): Promise<string>

获取WantAgent实例所属应用的包名。使用Promise异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agent | WantAgent | 是 | WantAgent对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回获取WantAgent实例的包名。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16000007 | Service busy. There are concurrent tasks. Try again later. |
| 16000151 | Invalid wantAgent object. |

**示例：**

```
1. import { wantAgent, Want } from '@kit.AbilityKit';
2. import type { WantAgent } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // wantAgent对象
6. let wantAgentData: WantAgent;
7. // WantAgentInfo对象
8. let wantAgentInfo: wantAgent.WantAgentInfo = {
9. wants: [
10. {
11. deviceId: 'deviceId',
12. bundleName: 'com.example.myapplication',
13. abilityName: 'EntryAbility',
14. action: 'action1',
15. entities: ['entity1'],
16. type: 'MIMETYPE',
17. uri: 'key={true,true,false}',
18. parameters:
19. {
20. mykey0: 2222,
21. mykey1: [1, 2, 3],
22. mykey2: '[1, 2, 3]',
23. mykey3: 'ssssssssssssssssssssssssss',
24. mykey4: [false, true, false],
25. mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
26. mykey6: true,
27. }
28. } as Want
29. ],
30. actionType: wantAgent.OperationType.START_ABILITY,
31. requestCode: 0,
32. wantAgentFlags:[wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
33. };

35. // getWantAgent回调
36. function getWantAgentCallback(err: BusinessError, data: WantAgent) {
37. if (err) {
38. console.error(`getWantAgent failed, code: ${JSON.stringify(err.code)}, message: ${JSON.stringify(err.message)}`);
39. } else {
40. wantAgentData = data;
41. }
42. try {
43. wantAgent.getBundleName(wantAgentData).then((data)=>{
44. console.info(`getBundleName ok! ${JSON.stringify(data)}`);
45. }).catch((err: BusinessError)=>{
46. console.error(`getBundleName failed! ${err.code} ${err.message}`);
47. });
48. } catch(err){
49. console.error(`getBundleName failed! ${err.code} ${err.message}`);
50. }
51. }
52. try {
53. wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
54. } catch(err) {
55. console.error(`getWantAgent failed! ${err.code} ${err.message}`);
56. }
```

## wantAgent.getUid

PhonePC/2in1TabletTVWearable

getUid(agent: WantAgent, callback: AsyncCallback<number>): void

获取WantAgent实例所属应用的UID，使用callback异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agent | WantAgent | 是 | WantAgent对象。 |
| callback | AsyncCallback<number> | 是 | 获取WantAgent实例所属应用的UID的回调方法。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16000007 | Service busy. There are concurrent tasks. Try again later. |
| 16000151 | Invalid wantAgent object. |

**示例：**

```
1. import { wantAgent, Want } from '@kit.AbilityKit';
2. import type { WantAgent } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // wantAgent对象
6. let wantAgentData: WantAgent;
7. // WantAgentInfo对象
8. let wantAgentInfo: wantAgent.WantAgentInfo = {
9. wants: [
10. {
11. deviceId: 'deviceId',
12. bundleName: 'com.example.myapplication',
13. abilityName: 'EntryAbility',
14. action: 'action1',
15. entities: ['entity1'],
16. type: 'MIMETYPE',
17. uri: 'key={true,true,false}',
18. parameters:
19. {
20. mykey0: 2222,
21. mykey1: [1, 2, 3],
22. mykey2: '[1, 2, 3]',
23. mykey3: 'ssssssssssssssssssssssssss',
24. mykey4: [false, true, false],
25. mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
26. mykey6: true,
27. }
28. } as Want
29. ],
30. actionType: wantAgent.OperationType.START_ABILITY,
31. requestCode: 0,
32. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
33. };

35. // getWantAgent回调
36. function getWantAgentCallback(err: BusinessError, data: WantAgent) {
37. if (err) {
38. console.error(`getWantAgent failed, code: ${err.code}, message: ${err.message}.`);
39. } else {
40. wantAgentData = data;
41. }
42. // getUid回调
43. let getUidCallback = (err: BusinessError, data: number) => {
44. if (err) {
45. console.error(`getUid failed, err code: ${err.code}, err msg: ${err.message}.`);
46. } else {
47. console.info(`getUid ok, data: ${JSON.stringify(data)}.`);
48. }
49. }
50. try {
51. wantAgent.getUid(wantAgentData, getUidCallback);
52. } catch (err) {
53. let code = (err as BusinessError).code;
54. let msg = (err as BusinessError).message;
55. console.error(`getUid failed, err code: ${code}, err msg: ${msg}.`);
56. }
57. }

59. try {
60. wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
61. } catch (err) {
62. let code = (err as BusinessError).code;
63. let msg = (err as BusinessError).message;
64. console.error(`getWantAgent failed, err code: ${code}, err msg: ${msg}.`);
65. }
```

## wantAgent.getUid

PhonePC/2in1TabletTVWearable

getUid(agent: WantAgent): Promise<number>

获取WantAgent实例所属应用的UID。使用Promise异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agent | WantAgent | 是 | WantAgent对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回获取WantAgent实例所属应用的UID。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16000007 | Service busy. There are concurrent tasks. Try again later. |
| 16000151 | Invalid wantAgent object. |

**示例：**

```
1. import { wantAgent, Want } from '@kit.AbilityKit';
2. import type { WantAgent } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // wantAgent对象
6. let wantAgentData: WantAgent;
7. // WantAgentInfo对象
8. let wantAgentInfo: wantAgent.WantAgentInfo = {
9. wants: [
10. {
11. deviceId: 'deviceId',
12. bundleName: 'com.example.myapplication',
13. abilityName: 'EntryAbility',
14. action: 'action1',
15. entities: ['entity1'],
16. type: 'MIMETYPE',
17. uri: 'key={true,true,false}',
18. parameters:
19. {
20. mykey0: 2222,
21. mykey1: [1, 2, 3],
22. mykey2: '[1, 2, 3]',
23. mykey3: 'ssssssssssssssssssssssssss',
24. mykey4: [false, true, false],
25. mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
26. mykey6: true,
27. }
28. } as Want
29. ],
30. actionType: wantAgent.OperationType.START_ABILITY,
31. requestCode: 0,
32. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
33. };

35. // getWantAgent回调
36. function getWantAgentCallback(err: BusinessError, data: WantAgent) {
37. if (err) {
38. console.error(`getWantAgent failed, err code: ${err.code}, err msg: ${err.message}.`);
39. } else {
40. wantAgentData = data;
41. }
42. try {
43. wantAgent.getUid(wantAgentData).then((data) => {
44. console.info(`getUid ok, data: ${JSON.stringify(data)}.`);
45. }).catch((err: BusinessError) => {
46. console.error(`getUid failed, err code: ${err.code}, err msg: ${err.message}.`);
47. });
48. } catch (err) {
49. let code = (err as BusinessError).code;
50. let msg = (err as BusinessError).message;
51. console.error(`getUid failed, err code: ${code}, err msg: ${msg}.`);
52. }
53. }

55. try {
56. wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
57. } catch (err) {
58. let code = (err as BusinessError).code;
59. let msg = (err as BusinessError).message;
60. console.error(`getWantAgent failed, err code: ${code}, err msg: ${msg}.`);
61. }
```

## wantAgent.cancel

PhonePC/2in1TabletTVWearable

cancel(agent: WantAgent, callback: AsyncCallback<void>): void

取消WantAgent实例，使用callback异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agent | WantAgent | 是 | WantAgent对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当取消WantAgent实例成功，err为undefined，否则err为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16000007 | Service busy. There are concurrent tasks. Try again later. |
| 16000151 | Invalid wantAgent object. |

**示例：**

```
1. import { wantAgent, Want } from '@kit.AbilityKit';
2. import type { WantAgent } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // wantAgent对象
6. let wantAgentData: WantAgent;
7. // WantAgentInfo对象
8. let wantAgentInfo: wantAgent.WantAgentInfo = {
9. wants: [
10. {
11. deviceId: 'deviceId',
12. bundleName: 'com.example.myapplication',
13. abilityName: 'EntryAbility',
14. action: 'action1',
15. entities: ['entity1'],
16. type: 'MIMETYPE',
17. uri: 'key={true,true,false}',
18. parameters:
19. {
20. mykey0: 2222,
21. mykey1: [1, 2, 3],
22. mykey2: '[1, 2, 3]',
23. mykey3: 'ssssssssssssssssssssssssss',
24. mykey4: [false, true, false],
25. mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
26. mykey6: true,
27. }
28. } as Want
29. ],
30. actionType: wantAgent.OperationType.START_ABILITY,
31. requestCode: 0,
32. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
33. };

35. // getWantAgent回调
36. function getWantAgentCallback(err: BusinessError, data: WantAgent) {
37. if (err) {
38. console.error(`getWantAgent failed, err code: ${err.code}, err msg: ${err.message}.`);
39. } else {
40. wantAgentData = data;
41. }
42. // cancel回调
43. let cancelCallback = (err: BusinessError, data: void) => {
44. if (err) {
45. console.error(`cancel failed, err code: ${err.code}, err msg: ${err.message}.`);
46. } else {
47. console.info(`cancel success.`);
48. }
49. }
50. try {
51. wantAgent.cancel(wantAgentData, cancelCallback);
52. } catch (err) {
53. let code = (err as BusinessError).code;
54. let msg = (err as BusinessError).message;
55. console.error(`cancel failed, err code: ${code}, err msg: ${msg}.`);
56. }
57. }

59. try {
60. wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
61. } catch (err) {
62. let code = (err as BusinessError).code;
63. let msg = (err as BusinessError).message;
64. console.error(`getWantAgent failed, err code: ${code}, err msg: ${msg}.`);
65. }
```

## wantAgent.cancel

PhonePC/2in1TabletTVWearable

cancel(agent: WantAgent): Promise<void>

取消WantAgent实例。使用Promise异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agent | WantAgent | 是 | WantAgent对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16000007 | Service busy. There are concurrent tasks. Try again later. |
| 16000151 | Invalid wantAgent object. |

**示例：**

```
1. import { wantAgent, Want } from '@kit.AbilityKit';
2. import type { WantAgent } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // wantAgent对象
6. let wantAgentData: WantAgent;
7. // WantAgentInfo对象
8. let wantAgentInfo: wantAgent.WantAgentInfo = {
9. wants: [
10. {
11. deviceId: 'deviceId',
12. bundleName: 'com.example.myapplication',
13. abilityName: 'EntryAbility',
14. action: 'action1',
15. entities: ['entity1'],
16. type: 'MIMETYPE',
17. uri: 'key={true,true,false}',
18. parameters:
19. {
20. mykey0: 2222,
21. mykey1: [1, 2, 3],
22. mykey2: '[1, 2, 3]',
23. mykey3: 'ssssssssssssssssssssssssss',
24. mykey4: [false, true, false],
25. mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
26. mykey6: true,
27. }
28. } as Want
29. ],
30. actionType: wantAgent.OperationType.START_ABILITY,
31. requestCode: 0,
32. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
33. };

35. // getWantAgent回调
36. function getWantAgentCallback(err: BusinessError, data: WantAgent) {
37. if (err) {
38. console.error(`getWantAgent failed, err code: ${err.code}, err msg: ${err.message}.`);
39. } else {
40. wantAgentData = data;
41. }
42. try {
43. wantAgent.cancel(wantAgentData).then((data) => {
44. console.info('cancel success.');
45. }).catch((err: BusinessError) => {
46. console.error(`cancel failed, err code: ${err.code}, err msg: ${err.message}.`);
47. });
48. } catch (err) {
49. let code = (err as BusinessError).code;
50. let msg = (err as BusinessError).message;
51. console.error(`cancel failed, err code: ${code}, err msg: ${msg}.`);
52. }
53. }

55. try {
56. wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
57. } catch (err) {
58. let code = (err as BusinessError).code;
59. let msg = (err as BusinessError).message;
60. console.error(`getWantAgent failed, err code: ${code}, err msg: ${msg}.`);
61. }
```

## wantAgent.trigger

PhonePC/2in1TabletTVWearable

trigger(agent: WantAgent, triggerInfo: TriggerInfo, callback?: AsyncCallback<CompleteData>): void

触发WantAgent实例，执行指定的操作（启动Ability、发送公共事件等）。使用callback异步回调。

这里所执行的操作类型，是在创建WantAgent实例时通过[WantAgentInfo](js-apis-inner-wantagent-wantagentinfo.md)参数中的actionType属性指定的。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agent | WantAgent | 是 | WantAgent对象。 |
| triggerInfo | [TriggerInfo](js-apis-inner-wantagent-triggerinfo.md) | 是 | 表示触发WantAgent实例时携带的信息，如自定义的extraInfos。 |
| callback | AsyncCallback<[CompleteData](js-apis-app-ability-wantagent.md#completedata)> | 否 | 回调函数。当主动触发WantAgent实例成功，err为undefined，data为主动触发返回的数据；否则err为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { wantAgent, Want } from '@kit.AbilityKit';
2. import type { WantAgent } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // wantAgent对象
6. let wantAgentData: WantAgent;
7. // triggerInfo
8. let triggerInfo: wantAgent.TriggerInfo = {
9. code: 0 // 自定义结果码
10. };
11. // WantAgentInfo对象
12. let wantAgentInfo: wantAgent.WantAgentInfo = {
13. wants: [
14. {
15. deviceId: 'deviceId',
16. bundleName: 'com.example.myapplication',
17. abilityName: 'EntryAbility',
18. action: 'action1',
19. entities: ['entity1'],
20. type: 'MIMETYPE',
21. uri: 'key={true,true,false}',
22. parameters:
23. {
24. mykey0: 2222,
25. mykey1: [1, 2, 3],
26. mykey2: '[1, 2, 3]',
27. mykey3: 'ssssssssssssssssssssssssss',
28. mykey4: [false, true, false],
29. mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
30. mykey6: true,
31. }
32. } as Want
33. ],
34. actionType: wantAgent.OperationType.START_ABILITY,
35. requestCode: 0,
36. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
37. };

39. // getWantAgent回调
40. function getWantAgentCallback(err: BusinessError, data: WantAgent) {
41. if (err) {
42. console.info(`getWantAgent failed, code: ${err.code}, message: ${err.message}`);
43. } else {
44. wantAgentData = data;
45. }
46. // trigger回调
47. let triggerCallback = (err: BusinessError, data: wantAgent.CompleteData) => {
48. if (err) {
49. console.error(`trigger failed, code: ${err.code}, message: ${err.message}`);
50. } else {
51. console.info(`trigger success, data: ${JSON.stringify(data)}`);
52. }
53. }
54. try {
55. wantAgent.trigger(wantAgentData, triggerInfo, triggerCallback);
56. } catch (err) {
57. let code = (err as BusinessError).code;
58. let msg = (err as BusinessError).message;
59. console.error(`trigger failed, code: ${code}, message: ${msg}.`);
60. }
61. }

63. try {
64. wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
65. } catch (err) {
66. let code = (err as BusinessError).code;
67. let msg = (err as BusinessError).message;
68. console.error(`getWantAgent failed, code: ${code}, message: ${msg}.`);
69. }
```

## wantAgent.equal

PhonePC/2in1TabletTVWearable

equal(agent: WantAgent, otherAgent: WantAgent, callback: AsyncCallback<boolean>): void

判断两个WantAgent实例是否相等，使用callback异步回调，以此来确定是否是来自同一应用的相同操作。

当两个WantAgent实例由当前用户下的同一应用使用相同的[WantAgentInfo](js-apis-inner-wantagent-wantagentinfo.md)信息创建，并且实例未被[cancel](js-apis-app-ability-wantagent.md#wantagentcancel)取消，这两个实例相等。在通知（携带WantAgent实例）场景，通知更新时会比较2个通知中的WantAgent实例，不相等时会把旧通知的WantAgent实例删除。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agent | WantAgent | 是 | WantAgent对象。 |
| otherAgent | WantAgent | 是 | WantAgent对象。 |
| callback | AsyncCallback<boolean> | 是 | 判断两个WantAgent实例是否相等的回调方法。返回true表示两个WantAgent实例相等，false表示两个WantAgent实例不相等。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { wantAgent, Want } from '@kit.AbilityKit';
2. import type { WantAgent } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // wantAgent对象
6. let wantAgent1: WantAgent;
7. let wantAgent2: WantAgent;
8. // WantAgentInfo对象
9. let wantAgentInfo: wantAgent.WantAgentInfo = {
10. wants: [
11. {
12. deviceId: 'deviceId',
13. bundleName: 'com.example.myapplication',
14. abilityName: 'EntryAbility',
15. action: 'action1',
16. entities: ['entity1'],
17. type: 'MIMETYPE',
18. uri: 'key={true,true,false}',
19. parameters:
20. {
21. mykey0: 2222,
22. mykey1: [1, 2, 3],
23. mykey2: '[1, 2, 3]',
24. mykey3: 'ssssssssssssssssssssssssss',
25. mykey4: [false, true, false],
26. mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
27. mykey6: true,
28. }
29. } as Want
30. ],
31. actionType: wantAgent.OperationType.START_ABILITY,
32. requestCode: 0,
33. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
34. };

36. // getWantAgent回调
37. function getWantAgentCallback(err: BusinessError, data: WantAgent) {
38. if (err) {
39. console.error(`getWantAgent failed, code: ${JSON.stringify(err.code)}, message: ${JSON.stringify(err.message)}`);
40. } else {
41. wantAgent1 = data;
42. wantAgent2 = data;
43. }
44. // equal回调
45. let equalCallback = (err: BusinessError, data: boolean) => {
46. if (err) {
47. console.error(`equal failed! ${err.code} ${err.message}`);
48. } else {
49. console.info(`equal ok! ${JSON.stringify(data)}`);
50. }
51. }
52. try {
53. wantAgent.equal(wantAgent1, wantAgent2, equalCallback);
54. } catch (err) {
55. console.error(`equal failed! ${(err as BusinessError).code} ${(err as BusinessError).message}`);
56. }
57. }

59. try {
60. wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
61. } catch (err) {
62. console.error(`getWantAgent failed! ${(err as BusinessError).code} ${(err as BusinessError).message}`);
63. }
```

## wantAgent.equal

PhonePC/2in1TabletTVWearable

equal(agent: WantAgent, otherAgent: WantAgent): Promise<boolean>

判断两个WantAgent实例是否相等，使用Promise异步回调，以此来确定是否是来自同一应用的相同操作。

当两个WantAgent实例由当前用户下的同一应用使用相同的[WantAgentInfo](js-apis-inner-wantagent-wantagentinfo.md)信息创建，并且实例未被[cancel](js-apis-app-ability-wantagent.md#wantagentcancel)取消，这两个实例相等。在通知（携带WantAgent实例）场景，通知更新时会比较2个通知中的WantAgent实例，不相等时会把旧通知的WantAgent实例删除。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agent | WantAgent | 是 | WantAgent对象。 |
| otherAgent | WantAgent | 是 | WantAgent对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回获取判断两个WantAgent实例是否相等的结果。返回true表示两个WantAgent实例相等，false表示两个WantAgent实例不相等。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { wantAgent, Want } from '@kit.AbilityKit';
2. import type { WantAgent } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // wantAgent对象
6. let wantAgent1: WantAgent;
7. let wantAgent2: WantAgent;
8. // WantAgentInfo对象
9. let wantAgentInfo: wantAgent.WantAgentInfo = {
10. wants: [
11. {
12. deviceId: 'deviceId',
13. bundleName: 'com.example.myapplication',
14. abilityName: 'EntryAbility',
15. action: 'action1',
16. entities: ['entity1'],
17. type: 'MIMETYPE',
18. uri: 'key={true,true,false}',
19. parameters:
20. {
21. mykey0: 2222,
22. mykey1: [1, 2, 3],
23. mykey2: '[1, 2, 3]',
24. mykey3: 'ssssssssssssssssssssssssss',
25. mykey4: [false, true, false],
26. mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
27. mykey6: true,
28. }
29. } as Want
30. ],
31. actionType: wantAgent.OperationType.START_ABILITY,
32. requestCode: 0,
33. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
34. };

36. // getWantAgent回调
37. function getWantAgentCallback(err: BusinessError, data: WantAgent) {
38. if (err) {
39. console.error(`getWantAgent failed, code: ${JSON.stringify(err.code)}, message: ${JSON.stringify(err.message)}`);
40. } else {
41. wantAgent1 = data;
42. wantAgent2 = data;
43. }
44. try {
45. wantAgent.equal(wantAgent1, wantAgent2).then((data) => {
46. console.info(`equal ok! ${JSON.stringify(data)}`);
47. }).catch((err: BusinessError) => {
48. console.error(`equal failed! ${err.code} ${err.message}`);
49. })
50. } catch (err) {
51. console.error(`equal failed! ${(err as BusinessError).code} ${(err as BusinessError).message}`);
52. }
53. }

55. try {
56. wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
57. } catch (err) {
58. console.error(`getWantAgent failed! ${(err as BusinessError).code} ${(err as BusinessError).message}`);
59. }
```

## wantAgent.getOperationType

PhonePC/2in1TabletTVWearable

getOperationType(agent: WantAgent, callback: AsyncCallback<number>): void

获取一个WantAgent实例的[OperationType](js-apis-app-ability-wantagent.md#operationtype)信息，使用callback异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agent | WantAgent | 是 | WantAgent对象。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取一个WantAgent的OperationType信息成功，err为undefined，data为OperationType；否则err为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16000007 | Service busy. There are concurrent tasks. Try again later. |
| 16000015 | Service timeout. |
| 16000151 | Invalid wantAgent object. |

**示例：**

```
1. import { wantAgent, Want } from '@kit.AbilityKit';
2. import type { WantAgent } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // wantAgent对象
6. let wantAgentData: WantAgent;
7. // WantAgentInfo对象
8. let wantAgentInfo: wantAgent.WantAgentInfo = {
9. wants: [
10. {
11. deviceId: 'deviceId',
12. bundleName: 'com.example.myapplication',
13. abilityName: 'EntryAbility',
14. action: 'action1',
15. entities: ['entity1'],
16. type: 'MIMETYPE',
17. uri: 'key={true,true,false}',
18. parameters:
19. {
20. mykey0: 2222,
21. mykey1: [1, 2, 3],
22. mykey2: '[1, 2, 3]',
23. mykey3: 'ssssssssssssssssssssssssss',
24. mykey4: [false, true, false],
25. mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
26. mykey6: true,
27. }
28. } as Want
29. ],
30. actionType: wantAgent.OperationType.START_ABILITY,
31. requestCode: 0,
32. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
33. };

35. // getWantAgent回调
36. function getWantAgentCallback(err: BusinessError, data: WantAgent) {
37. if (err) {
38. console.error(`getWantAgent failed, code: ${JSON.stringify(err.code)}, message: ${JSON.stringify(err.message)}`);
39. } else {
40. wantAgentData = data;
41. }
42. // getOperationTypeCallback回调
43. let getOperationTypeCallback = (err: BusinessError, data: number) => {
44. if (err) {
45. console.error(`getOperationType failed! ${err.code} ${err.message}`);
46. } else {
47. console.info(`getOperationType ok! ${JSON.stringify(data)}`);
48. }
49. }
50. try {
51. wantAgent.getOperationType(wantAgentData, getOperationTypeCallback);
52. } catch (err) {
53. console.error(`getOperationTypeCallback failed! ${(err as BusinessError).code} ${(err as BusinessError).message}`);
54. }
55. }

57. try {
58. wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
59. } catch (err) {
60. console.error(`getWantAgent failed! ${(err as BusinessError).code} ${(err as BusinessError).message}`);
61. }
```

## wantAgent.getOperationType

PhonePC/2in1TabletTVWearable

getOperationType(agent: WantAgent): Promise<number>

获取一个WantAgent实例的[OperationType](js-apis-app-ability-wantagent.md#operationtype)信息。使用Promise异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agent | WantAgent | 是 | WantAgent对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回OperationType的结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16000007 | Service busy. There are concurrent tasks. Try again later. |
| 16000015 | Service timeout. |
| 16000151 | Invalid wantAgent object. |

**示例：**

```
1. import { wantAgent, Want } from '@kit.AbilityKit';
2. import type { WantAgent } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // wantAgent对象
6. let wantAgentData: WantAgent;
7. // WantAgentInfo对象
8. let wantAgentInfo: wantAgent.WantAgentInfo = {
9. wants: [
10. {
11. deviceId: 'deviceId',
12. bundleName: 'com.example.myapplication',
13. abilityName: 'EntryAbility',
14. action: 'action1',
15. entities: ['entity1'],
16. type: 'MIMETYPE',
17. uri: 'key={true,true,false}',
18. parameters:
19. {
20. mykey0: 2222,
21. mykey1: [1, 2, 3],
22. mykey2: '[1, 2, 3]',
23. mykey3: 'ssssssssssssssssssssssssss',
24. mykey4: [false, true, false],
25. mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
26. mykey6: true,
27. }
28. } as Want
29. ],
30. actionType: wantAgent.OperationType.START_ABILITY,
31. requestCode: 0,
32. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
33. };

35. // getWantAgent回调
36. function getWantAgentCallback(err: BusinessError, data: WantAgent) {
37. if (err) {
38. console.error(`getWantAgent failed, code: ${JSON.stringify(err.code)}, message: ${JSON.stringify(err.message)}`);
39. } else {
40. wantAgentData = data;
41. }
42. try {
43. wantAgent.getOperationType(wantAgentData).then((data) => {
44. console.info(`getOperationType ok! ${JSON.stringify(data)}`);
45. }).catch((err: BusinessError) => {
46. console.error(`getOperationType failed! ${err.code} ${err.message}`);
47. });
48. } catch (err) {
49. console.error(`getOperationType failed! ${(err as BusinessError).code} ${(err as BusinessError).message}`);
50. }
51. }

53. try {
54. wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
55. } catch (err) {
56. console.error(`getWantAgent failed! ${(err as BusinessError).code} ${(err as BusinessError).message}`);
57. }
```

## WantAgentFlags

PhonePC/2in1TabletTVWearable

表示WantAgent行为控制标志，用于配置WantAgent的创建和触发行为。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ONE\_TIME\_FLAG | 0 | WantAgent仅能使用一次，trigger触发后自动cancel取消。 |
| NO\_BUILD\_FLAG | 1 | 如果描述WantAgent对象不存在，则不创建它，直接返回null。 |
| CANCEL\_PRESENT\_FLAG | 2 | 在生成一个新的WantAgent对象前取消已存在的一个WantAgent对象。 |
| UPDATE\_PRESENT\_FLAG | 3 | 使用新的WantAgent的额外数据替换已存在的WantAgent中的额外数据。 |
| CONSTANT\_FLAG | 4 | WantAgent是不可变的。 |
| REPLACE\_ELEMENT | 5 | 当前Want中的element属性可被WantAgent.trigger()中Want的element属性取代。当前版本暂不支持。 |
| REPLACE\_ACTION | 6 | 当前Want中的action属性可被WantAgent.trigger()中Want的action属性取代。当前版本暂不支持。 |
| REPLACE\_URI | 7 | 当前Want中的uri属性可被WantAgent.trigger()中Want的uri属性取代。当前版本暂不支持。 |
| REPLACE\_ENTITIES | 8 | 当前Want中的entities属性可被WantAgent.trigger()中Want的entities属性取代。当前版本暂不支持。 |
| REPLACE\_BUNDLE | 9 | 当前Want中的bundleName属性可被WantAgent.trigger()中Want的bundleName属性取代。当前版本暂不支持。 |

## OperationType

PhonePC/2in1TabletTVWearable

表示WantAgent支持的操作类型。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN\_TYPE | 0 | 不识别的类型。 |
| START\_ABILITY | 1 | 开启一个有页面的Ability。 |
| START\_ABILITIES | 2 | 开启多个有页面的Ability。 |
| START\_SERVICE | 3 | 开启一个无页面的Ability（仅在FA模型下生效）。 |
| SEND\_COMMON\_EVENT | 4 | 发送一个公共事件。 |

## CompleteData

PhonePC/2in1TabletTVWearable

表示主动触发WantAgent返回的数据。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| info | WantAgent | 否 | 否 | 触发的wantAgent。 |
| want | [Want](js-apis-app-ability-want.md) | 否 | 否 | 触发wantAgent时实际使用的want信息。 |
| finalCode | number | 否 | 否 | 触发wantAgent的返回码。 |
| finalData | string | 否 | 否 | 触发wantAgent的返回数据。返回"canceled"时表示触发失败，WantAgent实例已经被取消。 |
| extraInfo | Record<string, Object> | 否 | 是 | 额外数据。 |

## TriggerInfo

PhonePC/2in1TabletTVWearable

type TriggerInfo = \_TriggerInfo

TriggerInfo对象。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_TriggerInfo](js-apis-inner-wantagent-triggerinfo.md) | TriggerInfo对象。 |

## WantAgentInfo

PhonePC/2in1TabletTVWearable

type WantAgentInfo = \_WantAgentInfo

WantAgentInfo对象。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_WantAgentInfo](js-apis-inner-wantagent-wantagentinfo.md) | WantAgentInfo对象。 |

## WantAgent

PhonePC/2in1TabletTVWearable

type WantAgent = object

WantAgent对象。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| object | WantAgent对象。 |
