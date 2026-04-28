---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wantagent
title: @ohos.wantAgent (WantAgent模块)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 已停止维护的接口 > @ohos.wantAgent (WantAgent模块)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:51+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b499a2b51d36a86359585bbfc7d2818d4004928bc65ae9d178612f94dee949be
---

WantAgent模块提供了创建WantAgent实例、获取实例的用户ID、获取want信息、比较WantAgent实例和获取bundle名称等能力。

说明

本模块首批接口从API version 7开始支持，从API version 9废弃，替换模块为[@ohos.app.ability.wantAgent](js-apis-app-ability-wantagent.md)。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import wantAgent from '@ohos.wantAgent';
```

## wantAgent.getWantAgent

PhonePC/2in1TabletTVWearable

getWantAgent(info: WantAgentInfo, callback: AsyncCallback<WantAgent>): void

创建WantAgent。创建失败返回的WantAgent为空值。使用callback异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [WantAgentInfo](js-apis-inner-wantagent-wantagentinfo.md) | 是 | WantAgent信息。 |
| callback | AsyncCallback<WantAgent> | 是 | 创建WantAgent的回调方法。 |

**示例：**

```
1. import wantAgent, { WantAgent as _WantAgent } from '@ohos.wantAgent';
2. import { BusinessError } from '@ohos.base';

4. // getWantAgent回调
5. function getWantAgentCallback(err: BusinessError, data: _WantAgent) {
6. if (err.code) {
7. console.info('getWantAgent Callback err:' + JSON.stringify(err));
8. } else {
9. console.info('getWantAgent Callback success');
10. }
11. }

13. wantAgent.getWantAgent({
14. wants: [
15. {
16. deviceId: 'deviceId',
17. bundleName: 'com.neu.setResultOnAbilityResultTest1',
18. abilityName: 'com.example.test.EntryAbility',
19. action: 'action1',
20. entities: ['entity1'],
21. type: 'MIMETYPE',
22. uri: 'key={true,true,false}',
23. parameters:
24. {
25. mykey0: 2222,
26. mykey1: [1, 2, 3],
27. mykey2: '[1, 2, 3]',
28. mykey3: 'ssssssssssssssssssssssssss',
29. mykey4: [false, true, false],
30. mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
31. mykey6: true,
32. }
33. }
34. ],
35. operationType: wantAgent.OperationType.START_ABILITY,
36. requestCode: 0,
37. wantAgentFlags:[wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
38. }, getWantAgentCallback);
```

## wantAgent.getWantAgent

PhonePC/2in1TabletTVWearable

getWantAgent(info: WantAgentInfo): Promise<WantAgent>

创建WantAgent。创建失败返回的WantAgent为空值。使用Promise异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [WantAgentInfo](js-apis-inner-wantagent-wantagentinfo.md) | 是 | WantAgent信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<WantAgent> | 以Promise形式返回WantAgent。 |

**示例：**

```
1. import wantAgent, { WantAgent as _WantAgent } from '@ohos.wantAgent';

3. wantAgent.getWantAgent({
4. wants: [
5. {
6. deviceId: 'deviceId',
7. bundleName: 'com.neu.setResultOnAbilityResultTest1',
8. abilityName: 'com.example.test.EntryAbility',
9. action: 'action1',
10. entities: ['entity1'],
11. type: 'MIMETYPE',
12. uri: 'key={true,true,false}',
13. parameters:
14. {
15. mykey0: 2222,
16. mykey1: [1, 2, 3],
17. mykey2: '[1, 2, 3]',
18. mykey3: 'ssssssssssssssssssssssssss',
19. mykey4: [false, true, false],
20. mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
21. mykey6: true,
22. }
23. }
24. ],
25. operationType: wantAgent.OperationType.START_ABILITY,
26. requestCode: 0,
27. wantAgentFlags:[wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
28. }).then((data: _WantAgent) => {
29. console.info('==========================>getWantAgentCallback=======================>');
30. });
```

## wantAgent.getBundleName

PhonePC/2in1TabletTVWearable

getBundleName(agent: WantAgent, callback: AsyncCallback<string>): void

获取WantAgent实例的Bundle名称。使用callback异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agent | WantAgent | 是 | WantAgent对象。 |
| callback | AsyncCallback<string> | 是 | 获取WantAgent实例的包名的回调方法。 |

**示例：**

```
1. import wantAgent, { WantAgent as _WantAgent } from '@ohos.wantAgent';
2. import { BusinessError } from '@ohos.base';

4. // wantAgent对象
5. let wantAgentObj: _WantAgent;

7. // getWantAgent回调
8. function getWantAgentCallback(err: BusinessError, data: _WantAgent) {
9. console.info('==========================>getWantAgentCallback=======================>');
10. if (err.code == 0) {
11. wantAgentObj = data;
12. } else {
13. console.error('getWantAgent failed, error: ' + JSON.stringify(err));
14. return;
15. }

17. // getBundleName回调
18. let getBundleNameCallback = (err: BusinessError, data: string) => {
19. console.info('==========================>getBundleNameCallback=======================>');
20. }
21. wantAgent.getBundleName(wantAgentObj, getBundleNameCallback);
22. }

24. wantAgent.getWantAgent({
25. wants: [
26. {
27. deviceId: 'deviceId',
28. bundleName: 'com.neu.setResultOnAbilityResultTest1',
29. abilityName: 'com.example.test.EntryAbility',
30. action: 'action1',
31. entities: ['entity1'],
32. type: 'MIMETYPE',
33. uri: 'key={true,true,false}',
34. parameters:
35. {
36. mykey0: 2222,
37. mykey1: [1, 2, 3],
38. mykey2: '[1, 2, 3]',
39. mykey3: 'ssssssssssssssssssssssssss',
40. mykey4: [false, true, false],
41. mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
42. mykey6: true,
43. }
44. }
45. ],
46. operationType: wantAgent.OperationType.START_ABILITY,
47. requestCode: 0,
48. wantAgentFlags:[wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
49. }, getWantAgentCallback);
```

## wantAgent.getBundleName

PhonePC/2in1TabletTVWearable

getBundleName(agent: WantAgent): Promise<string>

获取WantAgent实例的Bundle名称。使用Promise异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agent | WantAgent | 是 | WantAgent对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 以Promise形式返回获取WantAgent实例的Bundle名称。 |

**示例：**

```
1. import wantAgent, { WantAgent as _WantAgent } from '@ohos.wantAgent';

3. // wantAgent对象
4. let wantAgentObj: _WantAgent;

6. wantAgent.getWantAgent({
7. wants: [
8. {
9. deviceId: 'deviceId',
10. bundleName: 'com.neu.setResultOnAbilityResultTest1',
11. abilityName: 'com.example.test.EntryAbility',
12. action: 'action1',
13. entities: ['entity1'],
14. type: 'MIMETYPE',
15. uri: 'key={true,true,false}',
16. parameters:
17. {
18. mykey0: 2222,
19. mykey1: [1, 2, 3],
20. mykey2: '[1, 2, 3]',
21. mykey3: 'ssssssssssssssssssssssssss',
22. mykey4: [false, true, false],
23. mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
24. mykey6: true,
25. }
26. }
27. ],
28. operationType: wantAgent.OperationType.START_ABILITY,
29. requestCode: 0,
30. wantAgentFlags:[wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
31. }).then((data: _WantAgent) => {
32. console.info('==========================>getWantAgentCallback=======================>');
33. wantAgentObj = data;
34. if (wantAgentObj) {
35. wantAgent.getBundleName(wantAgentObj).then((data) => {
36. console.info('==========================>getBundleNameCallback=======================>');
37. });
38. }
39. });
```

## wantAgent.getUid

PhonePC/2in1TabletTVWearable

getUid(agent: WantAgent, callback: AsyncCallback<number>): void

获取WantAgent实例的用户ID。使用callback异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agent | WantAgent | 是 | WantAgent对象。 |
| callback | AsyncCallback<number> | 是 | 获取WantAgent实例的用户ID的回调方法。 |

**示例：**

```
1. import wantAgent, { WantAgent as _WantAgent } from '@ohos.wantAgent';
2. import { BusinessError } from '@ohos.base';

4. // wantAgent对象
5. let wantAgentObj: _WantAgent;

7. // getWantAgent回调
8. function getWantAgentCallback(err: BusinessError, data: _WantAgent) {
9. console.info('==========================>getWantAgentCallback=======================>');
10. if (err.code == 0) {
11. wantAgentObj = data;
12. } else {
13. console.error('getWantAgent failed, error: ' + JSON.stringify(err));
14. return;
15. }

17. // getUid回调
18. let getUidCallback = (err: BusinessError, data: number) => {
19. console.info('==========================>getUidCallback=======================>');
20. }
21. wantAgent.getUid(wantAgentObj, getUidCallback);
22. }

24. wantAgent.getWantAgent({
25. wants: [
26. {
27. deviceId: 'deviceId',
28. bundleName: 'com.neu.setResultOnAbilityResultTest1',
29. abilityName: 'com.example.test.EntryAbility',
30. action: 'action1',
31. entities: ['entity1'],
32. type: 'MIMETYPE',
33. uri: 'key={true,true,false}',
34. parameters:
35. {
36. mykey0: 2222,
37. mykey1: [1, 2, 3],
38. mykey2: '[1, 2, 3]',
39. mykey3: 'ssssssssssssssssssssssssss',
40. mykey4: [false, true, false],
41. mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
42. mykey6: true,
43. }
44. }
45. ],
46. operationType: wantAgent.OperationType.START_ABILITY,
47. requestCode: 0,
48. wantAgentFlags:[wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
49. }, getWantAgentCallback);
```

## wantAgent.getUid

PhonePC/2in1TabletTVWearable

getUid(agent: WantAgent): Promise<number>

获取WantAgent实例的用户ID。使用Promise异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agent | WantAgent | 是 | WantAgent对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以Promise形式返回获取WantAgent实例的用户ID。 |

**示例：**

```
1. import wantAgent, { WantAgent as _WantAgent } from '@ohos.wantAgent';

3. // wantAgent对象
4. let wantAgentObj: _WantAgent;

6. wantAgent.getWantAgent({
7. wants: [
8. {
9. deviceId: 'deviceId',
10. bundleName: 'com.neu.setResultOnAbilityResultTest1',
11. abilityName: 'com.example.test.EntryAbility',
12. action: 'action1',
13. entities: ['entity1'],
14. type: 'MIMETYPE',
15. uri: 'key={true,true,false}',
16. parameters:
17. {
18. mykey0: 2222,
19. mykey1: [1, 2, 3],
20. mykey2: '[1, 2, 3]',
21. mykey3: 'ssssssssssssssssssssssssss',
22. mykey4: [false, true, false],
23. mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
24. mykey6: true,
25. }
26. }
27. ],
28. operationType: wantAgent.OperationType.START_ABILITY,
29. requestCode: 0,
30. wantAgentFlags:[wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
31. }).then((data) => {
32. console.info('==========================>getWantAgentCallback=======================>');
33. wantAgentObj = data;
34. if (wantAgentObj) {
35. wantAgent.getUid(wantAgentObj).then((data) => {
36. console.info('==========================>getUidCallback=======================>');
37. });
38. }
39. });
```

## wantAgent.cancel

PhonePC/2in1TabletTVWearable

cancel(agent: WantAgent, callback: AsyncCallback<void>): void

取消WantAgent实例。使用callback异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agent | WantAgent | 是 | WantAgent对象。 |
| callback | AsyncCallback<void> | 是 | 取消WantAgent实例的回调方法。 |

**示例：**

```
1. import wantAgent, { WantAgent as _WantAgent } from '@ohos.wantAgent';
2. import { BusinessError } from '@ohos.base';

4. // wantAgent对象
5. let wantAgentObj: _WantAgent;

7. // getWantAgent回调
8. function getWantAgentCallback(err: BusinessError, data: _WantAgent) {
9. console.info('==========================>getWantAgentCallback=======================>');
10. if (err.code == 0) {
11. wantAgentObj = data;
12. } else {
13. console.error('getWantAgent failed, error: ' + JSON.stringify(err));
14. return;
15. }

17. // cancel回调
18. let cancelCallback = (err: BusinessError) => {
19. console.info('==========================>cancelCallback=======================>');
20. }
21. wantAgent.cancel(wantAgentObj, cancelCallback);
22. }

24. wantAgent.getWantAgent({
25. wants: [
26. {
27. deviceId: 'deviceId',
28. bundleName: 'com.neu.setResultOnAbilityResultTest1',
29. abilityName: 'com.example.test.EntryAbility',
30. action: 'action1',
31. entities: ['entity1'],
32. type: 'MIMETYPE',
33. uri: 'key={true,true,false}',
34. parameters:
35. {
36. mykey0: 2222,
37. mykey1: [1, 2, 3],
38. mykey2: '[1, 2, 3]',
39. mykey3: 'ssssssssssssssssssssssssss',
40. mykey4: [false, true, false],
41. mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
42. mykey6: true,
43. }
44. }
45. ],
46. operationType: wantAgent.OperationType.START_ABILITY,
47. requestCode: 0,
48. wantAgentFlags:[wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
49. }, getWantAgentCallback);
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
| Promise<void> | 以Promise形式获取异步返回结果。 |

**示例：**

```
1. import wantAgent, { WantAgent as _WantAgent } from '@ohos.wantAgent';
2. import { BusinessError } from '@ohos.base';

4. // wantAgent对象
5. let wantAgentObj: _WantAgent;

7. wantAgent.getWantAgent({
8. wants: [
9. {
10. deviceId: 'deviceId',
11. bundleName: 'com.neu.setResultOnAbilityResultTest1',
12. abilityName: 'com.example.test.EntryAbility',
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
27. }
28. ],
29. operationType: wantAgent.OperationType.START_ABILITY,
30. requestCode: 0,
31. wantAgentFlags:[wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
32. }).then((data) => {
33. console.info('==========================>getWantAgentCallback=======================>');
34. wantAgentObj = data;
35. if (wantAgentObj) {
36. wantAgent.cancel(wantAgentObj).then((data) => {
37. console.info('==========================>cancelCallback=======================>');
38. });
39. }
40. });
```

## wantAgent.trigger

PhonePC/2in1TabletTVWearable

trigger(agent: WantAgent, triggerInfo: TriggerInfo, callback?: Callback<CompleteData>): void

主动激发WantAgent实例。使用callback异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agent | WantAgent | 是 | WantAgent对象。 |
| triggerInfo | [TriggerInfo](js-apis-inner-wantagent-triggerinfo.md) | 是 | TriggerInfo对象。 |
| callback | Callback<CompleteData> | 否 | 主动激发WantAgent实例的回调方法。 |

**示例：**

```
1. import wantAgent, { WantAgent as _WantAgent } from '@ohos.wantAgent';
2. import { BusinessError } from '@ohos.base';

4. // wantAgent对象
5. let wantAgentObj: _WantAgent;

7. // getWantAgent回调
8. function getWantAgentCallback(err: BusinessError, data: _WantAgent) {
9. console.info('==========================>getWantAgentCallback=======================>');
10. if (err.code == 0) {
11. wantAgentObj = data;
12. } else {
13. console.error('getWantAgent failed, error: ' + JSON.stringify(err));
14. return;
15. }

17. // trigger回调
18. let triggerCallback = (data: wantAgent.CompleteData) => {
19. console.info('==========================>triggerCallback=======================>');
20. };

22. wantAgent.trigger(wantAgentObj, {code:0}, triggerCallback);
23. }

25. wantAgent.getWantAgent({
26. wants: [
27. {
28. deviceId: 'deviceId',
29. bundleName: 'com.neu.setResultOnAbilityResultTest1',
30. abilityName: 'com.example.test.EntryAbility',
31. action: 'action1',
32. entities: ['entity1'],
33. type: 'MIMETYPE',
34. uri: 'key={true,true,false}',
35. parameters:
36. {
37. mykey0: 2222,
38. mykey1: [1, 2, 3],
39. mykey2: '[1, 2, 3]',
40. mykey3: 'ssssssssssssssssssssssssss',
41. mykey4: [false, true, false],
42. mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
43. mykey6: true,
44. }
45. }
46. ],
47. operationType: wantAgent.OperationType.START_ABILITY,
48. requestCode: 0,
49. wantAgentFlags:[wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
50. }, getWantAgentCallback);
```

## wantAgent.equal

PhonePC/2in1TabletTVWearable

equal(agent: WantAgent, otherAgent: WantAgent, callback: AsyncCallback<boolean>): void

判断两个WantAgent实例是否相等，以此来判断是否是来自同一应用的相同操作。使用callback异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agent | WantAgent | 是 | WantAgent对象。 |
| otherAgent | WantAgent | 是 | WantAgent对象。 |
| callback | AsyncCallback<boolean> | 是 | 判断两个WantAgent实例是否相等的回调方法。返回true表示两个WantAgent实例相等；返回false表示不相等。 |

**示例：**

```
1. import wantAgent, { WantAgent as _WantAgent } from '@ohos.wantAgent';
2. import { BusinessError } from '@ohos.base';

4. // wantAgent对象
5. let wantAgentObj1: _WantAgent;
6. let wantAgentObj2: _WantAgent;

8. // getWantAgent回调
9. function getWantAgentCallback(err: BusinessError, data: _WantAgent) {
10. console.info('==========================>getWantAgentCallback=======================>');
11. if (err.code == 0) {
12. wantAgentObj1 = data;
13. wantAgentObj2 = data;
14. } else {
15. console.error('getWantAgent failed, error: ' + JSON.stringify(err));
16. return;
17. }

19. // equal回调
20. let equalCallback = (err: BusinessError, data: boolean) => {
21. console.info('==========================>equalCallback=======================>');
22. };
23. wantAgent.equal(wantAgentObj1, wantAgentObj2, equalCallback);
24. }

26. wantAgent.getWantAgent({
27. wants: [
28. {
29. deviceId: 'deviceId',
30. bundleName: 'com.neu.setResultOnAbilityResultTest1',
31. abilityName: 'com.example.test.EntryAbility',
32. action: 'action1',
33. entities: ['entity1'],
34. type: 'MIMETYPE',
35. uri: 'key={true,true,false}',
36. parameters:
37. {
38. mykey0: 2222,
39. mykey1: [1, 2, 3],
40. mykey2: '[1, 2, 3]',
41. mykey3: 'ssssssssssssssssssssssssss',
42. mykey4: [false, true, false],
43. mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
44. mykey6: true,
45. }
46. }
47. ],
48. operationType: wantAgent.OperationType.START_ABILITY,
49. requestCode: 0,
50. wantAgentFlags:[wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
51. }, getWantAgentCallback);
```

## wantAgent.equal

PhonePC/2in1TabletTVWearable

equal(agent: WantAgent, otherAgent: WantAgent): Promise<boolean>

判断两个WantAgent实例是否相等，以此来判断是否是来自同一应用的相同操作。使用Promise异步回调。

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
| Promise<boolean> | 以Promise形式返回获取判断两个WantAgent实例是否相等的结果。返回true表示两个WantAgent实例相等；返回false表示不相等。 |

**示例：**

```
1. import wantAgent, { WantAgent as _WantAgent } from '@ohos.wantAgent';

3. // wantAgent对象
4. let wantAgentObj1: _WantAgent;
5. let wantAgentObj2: _WantAgent;

7. wantAgent.getWantAgent({
8. wants: [
9. {
10. deviceId: 'deviceId',
11. bundleName: 'com.neu.setResultOnAbilityResultTest1',
12. abilityName: 'com.example.test.EntryAbility',
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
27. }
28. ],
29. operationType: wantAgent.OperationType.START_ABILITY,
30. requestCode: 0,
31. wantAgentFlags:[wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
32. }).then((data) => {
33. console.info('==========================>getWantAgentCallback=======================>');
34. wantAgentObj1 = data;
35. wantAgentObj2 = data;
36. if (data) {
37. wantAgent.equal(wantAgentObj1, wantAgentObj2).then((data) => {
38. console.info('==========================>equalCallback=======================>');
39. });
40. }
41. });
```

## WantAgentFlags

PhonePC/2in1TabletTVWearable

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ONE\_TIME\_FLAG | 0 | WantAgent仅能使用一次。 |
| NO\_BUILD\_FLAG | 1 | 如果指定WantAgent对象不存在，则不创建它，直接返回null。 |
| CANCEL\_PRESENT\_FLAG | 2 | 在生成一个新的WantAgent对象前取消已存在的一个WantAgent对象。 |
| UPDATE\_PRESENT\_FLAG | 3 | 使用新的WantAgent的额外数据替换已存在的WantAgent中的额外数据。 |
| CONSTANT\_FLAG | 4 | WantAgent是不可变的。 |
| REPLACE\_ELEMENT | 5 | 当前Want中的element属性可被WantAgent.trigger()中Want的element属性取代。 |
| REPLACE\_ACTION | 6 | 当前Want中的action属性可被WantAgent.trigger()中Want的action属性取代。 |
| REPLACE\_URI | 7 | 当前Want中的uri属性可被WantAgent.trigger()中Want的uri属性取代。 |
| REPLACE\_ENTITIES | 8 | 当前Want中的entities属性可被WantAgent.trigger()中Want的entities属性取代。 |
| REPLACE\_BUNDLE | 9 | 当前Want中的bundleName属性可被WantAgent.trigger()中Want的bundleName属性取代。 |

## OperationType

PhonePC/2in1TabletTVWearable

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN\_TYPE | 0 | 不识别的类型。 |
| START\_ABILITY | 1 | 开启一个有页面的Ability。 |
| START\_ABILITIES | 2 | 开启多个有页面的Ability。 |
| START\_SERVICE | 3 | 开启一个无页面的ability。 |
| SEND\_COMMON\_EVENT | 4 | 发送一个公共事件。 |

## CompleteData

PhonePC/2in1TabletTVWearable

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| info | WantAgent | 否 | 否 | 触发的wantAgent。 |
| want | Want | 否 | 否 | 存在的被触发的want。 |
| finalCode | number | 否 | 否 | 触发wantAgent的请求代码。 |
| finalData | string | 否 | 否 | 公共事件收集的最终数据。 |
| extraInfo | { [key: string]: any } | 否 | 是 | 额外数据。 |

## WantAgent

PhonePC/2in1TabletTVWearable

type WantAgent = object

WantAgent对象。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| object | WantAgent对象。 |
