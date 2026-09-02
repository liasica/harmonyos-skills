---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-wantagent
title: "@ohos.app.ability.wantAgent (WantAgent模块)"
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 通用能力的接口(推荐) > @ohos.app.ability.wantAgent (WantAgent模块)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fbee5575b299acd06e3f8cce3fa0083b63ffc73a9244123ed1083ec37ea4c391
---

WantAgent模块封装了[Want](js-apis-app-ability-want.md)对象，允许应用程序在未来的某个时间点触发WantAgent实例执行指定操作（如启动Ability、发送公共事件等）。

该模块提供了创建WantAgent实例、获取WantAgent实例所属应用的包名、获取WantAgent实例所属应用的UID、主动触发WantAgent实例、判断两个WantAgent实例是否相等等功能。WantAgent的一个典型应用场景是通知处理。例如，当用户点击通知时，会触发WantAgent的[trigger](js-apis-app-ability-wantagent.md#wantagenttrigger)接口，并拉起目标应用。具体使用请参考[通知模块](../harmonyos-guides/notification-with-wantagent.md)。

**说明** 

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { wantAgent } from '@kit.AbilityKit';
```

## wantAgent.getWantAgent

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

```ts
import { wantAgent, Want } from '@kit.AbilityKit';
import type { WantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// wantAgent对象
let wantAgentData: WantAgent;
// WantAgentInfo对象
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      deviceId: 'deviceId',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      action: 'action1',
      entities: ['entity1'],
      type: 'MIMETYPE',
      uri: 'key={true,true,false}',
      parameters:
      {
        mykey0: 2222,
        mykey1: [1, 2, 3],
        mykey2: '[1, 2, 3]',
        mykey3: 'ssssssssssssssssssssssssss',
        mykey4: [false, true, false],
        mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
        mykey6: true,
      }
    } as Want
  ],
  actionType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

// getWantAgent回调
function getWantAgentCallback(err: BusinessError, data: WantAgent) {
  if (err.code) {
      console.error(`getWantAgent failed, code: ${err.code}, message: ${err.message}`);
    } else {
      wantAgentData = data;
    }
}

try {
  // 调用getWantAgent接口创建WantAgent对象
wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
} catch (err) {
  console.error(`getWantAgent failed, error: ${JSON.stringify(err)}`);
}
```

## wantAgent.getWantAgent

getWantAgent(info: WantAgentInfo): Promise<WantAgent>

创建WantAgent实例，用于后续触发指定操作。使用Promise异步回调。创建成功返回WantAgent对象，创建失败返回空值。

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

```ts
import { wantAgent, Want } from '@kit.AbilityKit';
import type { WantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantAgentData: WantAgent;
// WantAgentInfo对象
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      deviceId: 'deviceId',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      action: 'action1',
      entities: ['entity1'],
      type: 'MIMETYPE',
      uri: 'key={true,true,false}',
      parameters:
      {
        mykey0: 2222,
        mykey1: [1, 2, 3],
        mykey2: '[1, 2, 3]',
        mykey3: 'ssssssssssssssssssssssssss',
        mykey4: [false, true, false],
        mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
        mykey6: true,
      }
    } as Want
  ],
  actionType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

try {
  wantAgent.getWantAgent(wantAgentInfo).then((data) => {
    // 创建WantAgent成功，保存返回的WantAgent对象
    wantAgentData = data;
  }).catch((err: BusinessError) => {
    console.error(`getWantAgent failed, code: ${JSON.stringify(err.code)}, message: ${JSON.stringify(err.message)}`);
  });
} catch (err) {
  console.error(`getWantAgent failed! ${err.code} ${err.message}`);
}
```

## wantAgent.getBundleName

getBundleName(agent: WantAgent, callback: AsyncCallback<string>): void

获取WantAgent实例所属应用的包名，使用callback异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agent | WantAgent | 是 | WantAgent对象。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当获取包名成功，err为undefined，data为获取的包名；否则err为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16000007 | Service busy. There are concurrent tasks. Try again later. |
| 16000151 | Invalid wantAgent object. |

**示例：**

```ts
import { wantAgent, Want } from '@kit.AbilityKit';
import type { WantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// wantAgent对象
let wantAgentData: WantAgent;
// WantAgentInfo对象
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      deviceId: 'deviceId',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      action: 'action1',
      entities: ['entity1'],
      type: 'MIMETYPE',
      uri: 'key={true,true,false}',
      parameters:
      {
        mykey0: 2222,
        mykey1: [1, 2, 3],
        mykey2: '[1, 2, 3]',
        mykey3: 'ssssssssssssssssssssssssss',
        mykey4: [false, true, false],
        mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
        mykey6: true,
      }
    } as Want
  ],
  actionType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

// getWantAgent回调
function getWantAgentCallback(err: BusinessError, data: WantAgent) {
  if (err) {
    console.error(`getWantAgent failed, code: ${JSON.stringify(err.code)}, message: ${JSON.stringify(err.message)}`);
  } else {
    // 创建WantAgent成功，保存返回的WantAgent对象
    wantAgentData = data;
  }
  // getBundleName回调
  let getBundleNameCallback = (err: BusinessError, data: string) => {
    if (err) {
      console.error(`getBundleName failed! ${err.code} ${err.message}`);
    } else {
      console.info(`getBundleName ok! ${JSON.stringify(data)}`);
    }
  }
  try {
    // 调用getBundleName接口获取WantAgent实例的包名
    wantAgent.getBundleName(wantAgentData, getBundleNameCallback);
  } catch (err) {
    console.error(`getBundleName failed! ${err.code} ${err.message}`);
  }
}

try {
  // 调用getWantAgent接口创建WantAgent对象
  wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
} catch (err) {
  console.error(`getWantAgent failed! ${err.code} ${err.message}`);
}
```

## wantAgent.getBundleName

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

```ts
import { wantAgent, Want } from '@kit.AbilityKit';
import type { WantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// wantAgent对象
let wantAgentData: WantAgent;
// WantAgentInfo对象
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      deviceId: 'deviceId',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      action: 'action1',
      entities: ['entity1'],
      type: 'MIMETYPE',
      uri: 'key={true,true,false}',
      parameters:
      {
        mykey0: 2222,
        mykey1: [1, 2, 3],
        mykey2: '[1, 2, 3]',
        mykey3: 'ssssssssssssssssssssssssss',
        mykey4: [false, true, false],
        mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
        mykey6: true,
      }
    } as Want
  ],
  actionType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  wantAgentFlags:[wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

// getWantAgent回调
function getWantAgentCallback(err: BusinessError, data: WantAgent) {
  if (err) {
    console.error(`getWantAgent failed, code: ${JSON.stringify(err.code)}, message: ${JSON.stringify(err.message)}`);
  } else {
    // 创建WantAgent成功，保存返回的WantAgent对象
    wantAgentData = data;
  }
  try {
    // 使用Promise方式获取WantAgent实例的包名
    wantAgent.getBundleName(wantAgentData).then((data) => {
      console.info(`getBundleName ok! ${JSON.stringify(data)}`);
    }).catch((err: BusinessError) => {
      console.error(`getBundleName failed! ${err.code} ${err.message}`);
    });
  } catch(err){
    console.error(`getBundleName failed! ${err.code} ${err.message}`);
  }
}
try {
  // 调用getWantAgent接口创建WantAgent对象
  wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
} catch(err) {
  console.error(`getWantAgent failed! ${err.code} ${err.message}`);
}
```

## wantAgent.getUid

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

```ts
import { wantAgent, Want } from '@kit.AbilityKit';
import type { WantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// wantAgent对象
let wantAgentData: WantAgent;
// WantAgentInfo对象
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      deviceId: 'deviceId',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      action: 'action1',
      entities: ['entity1'],
      type: 'MIMETYPE',
      uri: 'key={true,true,false}',
      parameters:
      {
        mykey0: 2222,
        mykey1: [1, 2, 3],
        mykey2: '[1, 2, 3]',
        mykey3: 'ssssssssssssssssssssssssss',
        mykey4: [false, true, false],
        mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
        mykey6: true,
      }
    } as Want
  ],
  actionType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

// getWantAgent回调
function getWantAgentCallback(err: BusinessError, data: WantAgent) {
  if (err) {
    console.error(`getWantAgent failed, code: ${err.code}, message: ${err.message}.`);
  } else {
    // 创建WantAgent成功，保存返回的WantAgent对象
    wantAgentData = data;
  }
  // getUid回调
  let getUidCallback = (err: BusinessError, data: number) => {
    if (err) {
      console.error(`getUid failed, err code: ${err.code}, err msg: ${err.message}.`);
    } else {
      console.info(`getUid ok, data: ${JSON.stringify(data)}.`);
    }
  }
  try {
    // 调用getUid接口获取WantAgent实例所属应用的UID
    wantAgent.getUid(wantAgentData, getUidCallback);
  } catch (err) {
    let code = (err as BusinessError).code;
    let msg = (err as BusinessError).message;
    console.error(`getUid failed, err code: ${code}, err msg: ${msg}.`);
  }
}

try {
  // 调用getWantAgent接口创建WantAgent对象
  wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
} catch (err) {
  let code = (err as BusinessError).code;
  let msg = (err as BusinessError).message;
  console.error(`getWantAgent failed, err code: ${code}, err msg: ${msg}.`);
}
```

## wantAgent.getUid

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

```ts
import { wantAgent, Want } from '@kit.AbilityKit';
import type { WantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// wantAgent对象
let wantAgentData: WantAgent;
// WantAgentInfo对象
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      deviceId: 'deviceId',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      action: 'action1',
      entities: ['entity1'],
      type: 'MIMETYPE',
      uri: 'key={true,true,false}',
      parameters:
      {
        mykey0: 2222,
        mykey1: [1, 2, 3],
        mykey2: '[1, 2, 3]',
        mykey3: 'ssssssssssssssssssssssssss',
        mykey4: [false, true, false],
        mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
        mykey6: true,
      }
    } as Want
  ],
  actionType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

// getWantAgent回调
function getWantAgentCallback(err: BusinessError, data: WantAgent) {
  if (err) {
    console.error(`getWantAgent failed, err code: ${err.code}, err msg: ${err.message}.`);
  } else {
    // 创建WantAgent成功，保存返回的WantAgent对象
    wantAgentData = data;
  }
  try {
    // 使用Promise方式获取WantAgent实例所属应用的UID
    wantAgent.getUid(wantAgentData).then((data) => {
      console.info(`getUid ok, data: ${JSON.stringify(data)}.`);
    }).catch((err: BusinessError) => {
      console.error(`getUid failed, err code: ${err.code}, err msg: ${err.message}.`);
    });
  } catch (err) {
    let code = (err as BusinessError).code;
    let msg = (err as BusinessError).message;
    console.error(`getUid failed, err code: ${code}, err msg: ${msg}.`);
  }
}

try {
  // 调用getWantAgent接口创建WantAgent对象
  wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
} catch (err) {
  let code = (err as BusinessError).code;
  let msg = (err as BusinessError).message;
  console.error(`getWantAgent failed, err code: ${code}, err msg: ${msg}.`);
}
```

## wantAgent.cancel

cancel(agent: WantAgent, callback: AsyncCallback<void>): void

取消WantAgent实例，取消后该实例将无法被触发。使用callback异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agent | WantAgent | 是 | WantAgent对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当取消WantAgent实例成功，err为undefined，data为undefined；否则err为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16000007 | Service busy. There are concurrent tasks. Try again later. |
| 16000151 | Invalid wantAgent object. |

**示例：**

```ts
import { wantAgent, Want } from '@kit.AbilityKit';
import type { WantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// wantAgent对象
let wantAgentData: WantAgent;
// WantAgentInfo对象
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      deviceId: 'deviceId',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      action: 'action1',
      entities: ['entity1'],
      type: 'MIMETYPE',
      uri: 'key={true,true,false}',
      parameters:
      {
        mykey0: 2222,
        mykey1: [1, 2, 3],
        mykey2: '[1, 2, 3]',
        mykey3: 'ssssssssssssssssssssssssss',
        mykey4: [false, true, false],
        mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
        mykey6: true,
      }
    } as Want
  ],
  actionType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

// getWantAgent回调
function getWantAgentCallback(err: BusinessError, data: WantAgent) {
  if (err) {
    console.error(`getWantAgent failed, err code: ${err.code}, err msg: ${err.message}.`);
  } else {
    // 创建WantAgent成功，保存返回的WantAgent对象
    wantAgentData = data;
  }
  // cancel回调
  let cancelCallback = (err: BusinessError, data: void) => {
    if (err) {
      console.error(`cancel failed, err code: ${err.code}, err msg: ${err.message}.`);
    } else {
      console.info(`cancel success.`);
    }
  }
  try {
    // 调用cancel接口取消WantAgent实例
    wantAgent.cancel(wantAgentData, cancelCallback);
  } catch (err) {
    let code = (err as BusinessError).code;
    let msg = (err as BusinessError).message;
    console.error(`cancel failed, err code: ${code}, err msg: ${msg}.`);
  }
}

try {
  // 调用getWantAgent接口创建WantAgent对象
  wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
} catch (err) {
  let code = (err as BusinessError).code;
  let msg = (err as BusinessError).message;
  console.error(`getWantAgent failed, err code: ${code}, err msg: ${msg}.`);
}
```

## wantAgent.cancel

cancel(agent: WantAgent): Promise<void>

取消WantAgent实例，取消后该实例将无法被触发。使用Promise异步回调。

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

```ts
import { wantAgent, Want } from '@kit.AbilityKit';
import type { WantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// wantAgent对象
let wantAgentData: WantAgent;
// WantAgentInfo对象
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      deviceId: 'deviceId',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      action: 'action1',
      entities: ['entity1'],
      type: 'MIMETYPE',
      uri: 'key={true,true,false}',
      parameters:
      {
        mykey0: 2222,
        mykey1: [1, 2, 3],
        mykey2: '[1, 2, 3]',
        mykey3: 'ssssssssssssssssssssssssss',
        mykey4: [false, true, false],
        mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
        mykey6: true,
      }
    } as Want
  ],
  actionType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

// getWantAgent回调
function getWantAgentCallback(err: BusinessError, data: WantAgent) {
  if (err) {
    console.error(`getWantAgent failed, err code: ${err.code}, err msg: ${err.message}.`);
  } else {
    // 创建WantAgent成功，保存返回的WantAgent对象
    wantAgentData = data;
  }
  try {
    // 使用Promise方式取消WantAgent实例
    wantAgent.cancel(wantAgentData).then((data) => {
      console.info('cancel success.');
    }).catch((err: BusinessError) => {
      console.error(`cancel failed, err code: ${err.code}, err msg: ${err.message}.`);
    });
  } catch (err) {
    let code = (err as BusinessError).code;
    let msg = (err as BusinessError).message;
    console.error(`cancel failed, err code: ${code}, err msg: ${msg}.`);
  }
}

try {
  // 调用getWantAgent接口创建WantAgent对象
  wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
} catch (err) {
  let code = (err as BusinessError).code;
  let msg = (err as BusinessError).message;
  console.error(`getWantAgent failed, err code: ${code}, err msg: ${msg}.`);
}
```

## wantAgent.trigger

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

```ts
import { wantAgent, Want } from '@kit.AbilityKit';
import type { WantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// wantAgent对象
let wantAgentData: WantAgent;
// triggerInfo
let triggerInfo: wantAgent.TriggerInfo = {
  code: 0 // 自定义结果码
};
// WantAgentInfo对象
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      deviceId: 'deviceId',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      action: 'action1',
      entities: ['entity1'],
      type: 'MIMETYPE',
      uri: 'key={true,true,false}',
      parameters:
      {
        mykey0: 2222,
        mykey1: [1, 2, 3],
        mykey2: '[1, 2, 3]',
        mykey3: 'ssssssssssssssssssssssssss',
        mykey4: [false, true, false],
        mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
        mykey6: true,
      }
    } as Want
  ],
  actionType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

// getWantAgent回调
function getWantAgentCallback(err: BusinessError, data: WantAgent) {
  if (err) {
    console.error(`getWantAgent failed, code: ${err.code}, message: ${err.message}`);
  } else {
    // 创建WantAgent成功，保存返回的WantAgent对象
    wantAgentData = data;
  }
  // trigger回调
  let triggerCallback = (err: BusinessError, data: wantAgent.CompleteData) => {
    if (err) {
      console.error(`trigger failed, code: ${err.code}, message: ${err.message}`);
    } else {
      console.info(`trigger success, data: ${JSON.stringify(data)}`);
    }
  }
  try {
    // 调用trigger接口触发WantAgent实例执行指定操作
    wantAgent.trigger(wantAgentData, triggerInfo, triggerCallback);
  } catch (err) {
    let code = (err as BusinessError).code;
    let msg = (err as BusinessError).message;
    console.error(`trigger failed, code: ${code}, message: ${msg}.`);
  }
}

try {
  // 调用getWantAgent接口创建WantAgent对象
  wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
} catch (err) {
  let code = (err as BusinessError).code;
  let msg = (err as BusinessError).message;
  console.error(`getWantAgent failed, code: ${code}, message: ${msg}.`);
}
```

## wantAgent.equal

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

```ts
import { wantAgent, Want } from '@kit.AbilityKit';
import type { WantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// wantAgent对象
let wantAgent1: WantAgent;
let wantAgent2: WantAgent;
// WantAgentInfo对象
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      deviceId: 'deviceId',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      action: 'action1',
      entities: ['entity1'],
      type: 'MIMETYPE',
      uri: 'key={true,true,false}',
      parameters:
      {
        mykey0: 2222,
        mykey1: [1, 2, 3],
        mykey2: '[1, 2, 3]',
        mykey3: 'ssssssssssssssssssssssssss',
        mykey4: [false, true, false],
        mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
        mykey6: true,
      }
    } as Want
  ],
  actionType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

// getWantAgent回调
function getWantAgentCallback(err: BusinessError, data: WantAgent) {
  if (err) {
    console.error(`getWantAgent failed, code: ${JSON.stringify(err.code)}, message: ${JSON.stringify(err.message)}`);
  } else {
    // 创建WantAgent成功，保存返回的WantAgent对象
    wantAgent1 = data;
    wantAgent2 = data;
  }
  // equal回调
  let equalCallback = (err: BusinessError, data: boolean) => {
    if (err) {
      console.error(`equal failed! ${err.code} ${err.message}`);
    } else {
      console.info(`equal ok! ${JSON.stringify(data)}`);
    }
  }
  try {
    // 调用equal接口判断两个WantAgent实例是否相等
    wantAgent.equal(wantAgent1, wantAgent2, equalCallback);
  } catch (err) {
    console.error(`equal failed! ${(err as BusinessError).code} ${(err as BusinessError).message}`);
  }
}

try {
  // 调用getWantAgent接口创建WantAgent对象
  wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
} catch (err) {
  console.error(`getWantAgent failed! ${(err as BusinessError).code} ${(err as BusinessError).message}`);
}
```

## wantAgent.equal

equal(agent: WantAgent, otherAgent: WantAgent): Promise<boolean>

判断两个WantAgent实例是否相等，使用Promise异步回调，以此来确定是否是来自同一应用的相同操作。

当两个WantAgent实例由当前用户下的同一应用使用相同的[WantAgentInfo](js-apis-inner-wantagent-wantagentinfo.md)信息创建，并且实例未被[cancel](js-apis-app-ability-wantagent.md#wantagentcancel)取消，这两个实例相等。在通知（携带WantAgent实例）场景，通知更新时会比较2个通知中的WantAgent实例，不相等时会把旧通知的WantAgent实例删除。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agent | [WantAgent](js-apis-app-ability-wantagent.md#wantagent) | 是 | WantAgent对象。 |
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

```ts
import { wantAgent, Want } from '@kit.AbilityKit';
import type { WantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// wantAgent对象
let wantAgent1: WantAgent;
let wantAgent2: WantAgent;
// WantAgentInfo对象
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      deviceId: 'deviceId',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      action: 'action1',
      entities: ['entity1'],
      type: 'MIMETYPE',
      uri: 'key={true,true,false}',
      parameters:
      {
        mykey0: 2222,
        mykey1: [1, 2, 3],
        mykey2: '[1, 2, 3]',
        mykey3: 'ssssssssssssssssssssssssss',
        mykey4: [false, true, false],
        mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
        mykey6: true,
      }
    } as Want
  ],
  actionType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

// getWantAgent回调
function getWantAgentCallback(err: BusinessError, data: WantAgent) {
  if (err) {
    console.error(`getWantAgent failed, code: ${JSON.stringify(err.code)}, message: ${JSON.stringify(err.message)}`);
  } else {
    // 创建WantAgent成功，保存返回的WantAgent对象
    wantAgent1 = data;
    wantAgent2 = data;
  }
  try {
    // 使用Promise方式判断两个WantAgent实例是否相等
    wantAgent.equal(wantAgent1, wantAgent2).then((data) => {
      console.info(`equal ok! ${JSON.stringify(data)}`);
    }).catch((err: BusinessError) => {
    console.error(`equal failed! ${err.code} ${err.message}`);
  });
  } catch (err) {
    console.error(`equal failed! ${(err as BusinessError).code} ${(err as BusinessError).message}`);
  }
}

try {
  // 调用getWantAgent接口创建WantAgent对象
  wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
} catch (err) {
  console.error(`getWantAgent failed! ${(err as BusinessError).code} ${(err as BusinessError).message}`);
}
```

## wantAgent.getOperationType

getOperationType(agent: WantAgent, callback: AsyncCallback<number>): void

获取一个WantAgent实例的[OperationType](js-apis-app-ability-wantagent.md#operationtype)信息，使用callback异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agent | WantAgent | 是 | WantAgent对象。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取OperationType信息成功，err为undefined，data为OperationType的数值；否则err为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16000007 | Service busy. There are concurrent tasks. Try again later. |
| 16000015 | Service timeout. |
| 16000151 | Invalid wantAgent object. |

**示例：**

```ts
import { wantAgent, Want } from '@kit.AbilityKit';
import type { WantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// wantAgent对象
let wantAgentData: WantAgent;
// WantAgentInfo对象
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      deviceId: 'deviceId',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      action: 'action1',
      entities: ['entity1'],
      type: 'MIMETYPE',
      uri: 'key={true,true,false}',
      parameters:
      {
        mykey0: 2222,
        mykey1: [1, 2, 3],
        mykey2: '[1, 2, 3]',
        mykey3: 'ssssssssssssssssssssssssss',
        mykey4: [false, true, false],
        mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
        mykey6: true,
      }
    } as Want
  ],
  actionType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

// getWantAgent回调
function getWantAgentCallback(err: BusinessError, data: WantAgent) {
  if (err) {
    console.error(`getWantAgent failed, code: ${JSON.stringify(err.code)}, message: ${JSON.stringify(err.message)}`);
  } else {
    // 创建WantAgent成功，保存返回的WantAgent对象
    wantAgentData = data;
  }
  // getOperationTypeCallback回调
  let getOperationTypeCallback = (err: BusinessError, data: number) => {
    if (err) {
      console.error(`getOperationType failed! ${err.code} ${err.message}`);
    } else {
      console.info(`getOperationType ok! ${JSON.stringify(data)}`);
    }
  }
  try {
    // 调用getOperationType接口获取WantAgent实例的操作类型
    wantAgent.getOperationType(wantAgentData, getOperationTypeCallback);
  } catch (err) {
    console.error(`getOperationTypeCallback failed! ${(err as BusinessError).code} ${(err as BusinessError).message}`);
  }
}

try {
  // 调用getWantAgent接口创建WantAgent对象
  wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
} catch (err) {
  console.error(`getWantAgent failed! ${(err as BusinessError).code} ${(err as BusinessError).message}`);
}
```

## wantAgent.getOperationType

getOperationType(agent: WantAgent): Promise<number>

获取一个WantAgent实例的[OperationType](js-apis-app-ability-wantagent.md#operationtype)信息。使用Promise异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agent | [WantAgent](js-apis-app-ability-wantagent.md#wantagent) | 是 | WantAgent对象。 |

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

```ts
import { wantAgent, Want } from '@kit.AbilityKit';
import type { WantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// wantAgent对象
let wantAgentData: WantAgent;
// WantAgentInfo对象
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      deviceId: 'deviceId',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      action: 'action1',
      entities: ['entity1'],
      type: 'MIMETYPE',
      uri: 'key={true,true,false}',
      parameters:
      {
        mykey0: 2222,
        mykey1: [1, 2, 3],
        mykey2: '[1, 2, 3]',
        mykey3: 'ssssssssssssssssssssssssss',
        mykey4: [false, true, false],
        mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
        mykey6: true,
      }
    } as Want
  ],
  actionType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

// getWantAgent回调
function getWantAgentCallback(err: BusinessError, data: WantAgent) {
  if (err) {
    console.error(`getWantAgent failed, code: ${JSON.stringify(err.code)}, message: ${JSON.stringify(err.message)}`);
  } else {
    // 创建WantAgent成功，保存返回的WantAgent对象
    wantAgentData = data;
  }
  try {
    // 使用Promise方式获取WantAgent实例的操作类型
    wantAgent.getOperationType(wantAgentData).then((data) => {
      console.info(`getOperationType ok! ${JSON.stringify(data)}`);
    }).catch((err: BusinessError) => {
      console.error(`getOperationType failed! ${err.code} ${err.message}`);
    });
  } catch (err) {
    console.error(`getOperationType failed! ${(err as BusinessError).code} ${(err as BusinessError).message}`);
  }
}

try {
  // 调用getWantAgent接口创建WantAgent对象
  wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
} catch (err) {
  console.error(`getWantAgent failed! ${(err as BusinessError).code} ${(err as BusinessError).message}`);
}
```

## WantAgentFlags

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

type TriggerInfo = \_TriggerInfo

TriggerInfo对象。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_TriggerInfo](js-apis-inner-wantagent-triggerinfo.md) | TriggerInfo对象。 |

## WantAgentInfo

type WantAgentInfo = \_WantAgentInfo

WantAgentInfo对象。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_WantAgentInfo](js-apis-inner-wantagent-wantagentinfo.md) | WantAgentInfo对象。 |

## WantAgent

type WantAgent = object

WantAgent对象。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| object | WantAgent对象。 |
