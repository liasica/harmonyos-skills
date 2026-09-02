---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nfc-tag-access-guide
title: NFC标签读写开发指南
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > NFC > NFC标签读写开发指南
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:33+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:21332efe8f411accf116e230da9f6a40a23f99cf2d5b8f0eb8db075c87372e53
---

## 简介

近场通信(Near Field Communication，NFC)是一种短距高频的无线电技术，在13.56MHz频率运行，通信距离一般在10厘米距离内。电子设备可以通过NFC通信技术和NFC标签通信，从标签中读取数据，或写入数据到标签。

NFC标签支持一种或多种通信技术，具体技术如下：

* NfcA (也称为 ISO 14443-3A)
* NfcB (也称为 ISO 14443-3B)
* NfcF (也称为 JIS 6319-4)
* NfcV (也称为 ISO 15693)
* IsoDep (也称为 ISO 14443-4)
* NDEF
* MifareClassic
* MifareUltralight

## 场景介绍

电子设备通过NFC天线位置触碰NFC标签卡片，完成NFC标签卡片的读取或写入。从使用场景上，可以分成NFC标签前台读写和NFC标签后台读写。

* NFC标签前台读写

  前台读写是指在触碰NFC标签之前，用户先在电子设备上打开特定的应用程序，用户明确想使用所打开的应用程序和NFC标签进行读写操作。用户打开应用程序在前台，并且进入应用的刷卡页面之后，电子设备触碰NFC标签，只会把读取到的卡片分发给前台应用。
* NFC标签后台读写

  后台读写是指不打开特定的NFC标签应用程序，电子设备触碰发现NFC标签后，根据NFC标签的技术类型，分发给能够处理的应用程序。如果能匹配到多个应用程序，则弹出应用选择器列举出应用列表给用户手动选择。用户选择指定的应用后，自动跳转到应用程序的NFC标签读写卡页面。
* 常用读写NDEF格式Tag定制功能

  手机NFC支持读取卡片信息并跳转到生态应用，有使用NDEF通用协议和应用接入[AirTouch服务](https://developer.huawei.com/consumer/cn/airtouch/)两种方式：

  1. NDEF通用协议跳转应用：在标签内写入应用的信息，电子设备触碰发现NFC标签后，根据NFC标签的NDEF信息，分发给对应的应用。
  2. 接入AirTouch服务：更高阶的应用拉起方案，通过碰一碰服务直达，满足用户碎片化需求，如：NFC碰一碰点单、支付、活动推广等，详细应用开发接入指导及标签制作参考[AirTouch服务](https://developer.huawei.com/consumer/cn/airtouch/)。

  更多NDEF标签格式规范请关注[NFC论坛](https://nfc-forum.org/)。
* 标签读写约束条件

  不管是前台读写，还是后台读写，电子设备能够发现NFC标签的前提条件是设备必须是亮屏和解锁状态。

## 接口说明

NFC标签读写完整的JS API说明以及实例代码请参考：[@ohos.nfc.tag (标准NFC-Tag)](../harmonyos-references/js-apis-nfctag.md)。

获取不同技术类型标签对象的接口说明如下表，根据不同技术的标签对象来执行NFC标签的读写。

| 接口名 | 支持版本 | 功能描述 |
| --- | --- | --- |
| getNfcA(tagInfo: TagInfo): NfcATag | 从API version 9开始支持 | 获取NfcA技术类型的标签对象。 |
| getNfcB(tagInfo: TagInfo): NfcBTag | 从API version 9开始支持 | 获取NfcB技术类型的标签对象。 |
| getNfcF(tagInfo: TagInfo): NfcFTag | 从API version 9开始支持 | 获取NfcF技术类型的标签对象。 |
| getNfcV(tagInfo: TagInfo): NfcVTag | 从API version 9开始支持 | 获取NfcV技术类型的标签对象。 |
| getIsoDep(tagInfo: TagInfo): IsoDepTag | 从API version 9开始支持 | 获取IsoDep技术类型的标签对象。 |
| getNdef(tagInfo: TagInfo): NdefTag | 从API version 9开始支持 | 获取NDEF技术类型的标签对象。 |
| getMifareClassic(tagInfo: TagInfo): MifareClassicTag | 从API version 9开始支持 | 获取MIFARE Classic技术类型的标签对象。 |
| getMifareUltralight(tagInfo: TagInfo): MifareUltralightTag | 从API version 9开始支持 | 获取MifareUltralight技术类型的标签对象。 |

## 开发准备

### NFC标签前台读写、后台读写或Tag定制的选择

NFC标签读写应用开发者根据业务需要，可以选择实现前台读卡、后台读卡或者通过定制的Tag跳转到对应的应用。三种不同的读卡方式，代码实现和标签内容上会存在一些差异。

* NFC标签前台读写

1. 在配置文件module.json5中，不需要静态声明过滤读取NFC标签的技术类型，而是通过[tag.registerForegroundDispatch](../harmonyos-references/js-apis-nfctag.md#tagregisterforegrounddispatch10)或者[tag.on](../harmonyos-references/js-apis-nfctag.md#tagonreadermode11)来完成动态注册。
2. 通过tag.registerForegroundDispatch或tag.on来动态注册前台读写标签时，入参中必须指定需要读取NFC标签的技术类型。
3. 如果选择tag.registerForegroundDispatch注册，当应用运行在前台并进入该页面，NFC的卡模拟功能在打开时，可以同时完成刷卡。如果选择tag.on注册，当应用运行在前台并进入该页面时，NFC的卡模拟是关闭的，无法同时进行刷卡功能。
4. 当应用页面切换到后台时，需要显式调用[tag.unregisterForegroundDispatch](../harmonyos-references/js-apis-nfctag.md#tagunregisterforegrounddispatch10)或者[tag.off](../harmonyos-references/js-apis-nfctag.md#tagoffreadermode11)来取消注册，退出前台读卡优先功能。

* NFC标签后台读写

1. 在配置文件module.json5中，需要静态声明过滤读取NFC标签的技术类型。根据业务需要至少定义一种读标签的技术类型，‘tag-tech/’是前缀，后面跟着技术类型描述。
2. 技术类型的描述字符，必须完整匹配并区分大小写，需要严格匹配。

* NDEF格式Tag定制

  对NFC标签的内容有要求，NDEF标签可能存在1或多个Record，需要在Record中写入应用相关信息（包名/URI/AirtouchId），可以实现应用在后台时，一碰拉起应用的功能。

**注意** 

* 从API version 9之后的应用开发新增支持[Stage模型](ability-terminology.md#stage模型)，作为目前主推并长期演进的模型。
* NFC标签读写示例代码的提供，全部按照[Stage模型](ability-terminology.md#stage模型)来说明。

## 开发步骤

### 前台读取标签

1. 在module.json5文件中声明NFC标签读取的权限，以及声明NFC标签特定的action。
2. import需要的tag模块和其他相关的模块。
3. 判断设备是否支持NFC能力。
4. 调用tag模块中前台优先的接口，使能前台应用程序优先处理所发现的NFC标签功能。
5. 获取特定技术类型的NFC标签对象。
6. 执行读写接口完成标签数据的读取或写入数据到标签。
7. 退出应用程序NFC标签页面时，调用tag模块退出前台优先功能。

```ts
    "abilities": [
      {
        "name": "EntryAbility",
        "srcEntry": "./ets/entryability/EntryAbility.ts",
        "description": "$string:EntryAbility_desc",
        "icon": "$media:icon",
        "label": "$string:EntryAbility_label",
        "startWindowIcon": "$media:icon",
        "startWindowBackground": "$color:start_window_background",
        "exported": true,
        "skills": [
          {
            "entities": [
              "entity.system.home"
            ],
            "actions": [
              "ohos.want.action.home",

              // actions必须包含"ohos.nfc.tag.action.TAG_FOUND"
              "ohos.nfc.tag.action.TAG_FOUND"
            ]
          }
        ]
      }
    ],
    "requestPermissions": [
      {
        // 添加NFC标签操作的权限
        "name": "ohos.permission.NFC_TAG",
        "reason": "$string:app_name",
      }
    ]
```

```ts
import { tag, nfcController } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { AbilityConstant, UIAbility, Want, bundleManager } from '@kit.AbilityKit';

let nfcTagElementName: bundleManager.ElementName;
let foregroundRegister: boolean;

async function readerModeCb(error: BusinessError, tagInfo: tag.TagInfo) {
  if (!error) {
    // 获取特定技术类型的NFC标签对象
    if (tagInfo == null) {
      hilog.error(0x0000, 'testTag', 'readerModeCb tagInfo is invalid');
      return;
    }
    if (tagInfo.uid == null) {
      hilog.error(0x0000, 'testTag', 'readerModeCb uid is invalid');
      return;
    }
    if (tagInfo.technology == null || tagInfo.technology.length == 0) {
      hilog.error(0x0000, 'testTag', 'readerModeCb technology is invalid');
      return;
    }

    // 标签里面可能支持多种技术类型，选择特定的技术类型接口，完成标签数据的读取或写入
    // 下面示例代码，使用IsoDep完成标签数据的读取或写入
    let isoDep: tag.IsoDepTag | null = null;
    for (let i = 0; i < tagInfo.technology.length; i++) {
      if (tagInfo.technology[i] == tag.ISO_DEP) {
        try {
          isoDep = tag.getIsoDep(tagInfo);
        } catch (error) {
          hilog.error(0x0000, 'testTag', 'readerModeCb getIsoDep error = %{public}s', JSON.stringify(error));
          return;
        }
      }
      // 也可以按需选择其它类型的技术读写标签
    }
    if (isoDep == null) {
      hilog.error(0x0000, 'testTag', 'readerModeCb getIsoDep is invalid');
      return;
    }

    // 使用IsoDep技术连接到NFC标签
    try {
      isoDep.connect();
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'readerModeCb isoDep.connect() error = %{public}s', JSON.stringify(error));
      return;
    }
    if (!isoDep.isConnected()) {
      hilog.error(0x0000, 'testTag', 'readerModeCb isoDep.isConnected() false.');
      return;
    }

    // 发送指令到已连接的标签，获取标签的响应数据
    let cmdData = [0x01, 0x02, 0x03, 0x04]; // 修改为正确的访问标签的指令数据
    try {
      isoDep.transmit(cmdData).then((response: number[]) => {
        hilog.info(0x0000, 'testTag', 'readerModeCb isoDep.transmit() response = %{public}s.', JSON.stringify(response));
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, 'testTag', 'readerModeCb isoDep.transmit() err = %{public}s.', JSON.stringify(err));
        return;
      });
    } catch (businessError) {
      hilog.error(0x0000, 'testTag', 'readerModeCb isoDep.transmit() businessError = %{public}s.', JSON.stringify(businessError));
      return;
    }
  } else {
    hilog.info(0x0000, 'testTag', 'readerModeCb readerModeCb error %{public}s', JSON.stringify(error));
  }
}

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');

    // 判断设备是否支持NFC能力
    if (!canIUse("SystemCapability.Communication.NFC.Core")) {
      hilog.error(0x0000, 'testTag', 'NFC System Capability not supported.');
      return;
    }
    if (!nfcController.isNfcSupported()) {
      hilog.error(0x0000, 'testTag', 'NFC not supported on this device.');
      return;
    }

    // 根据应用程序信息，初始化正确的值
    nfcTagElementName = {
      bundleName: want.bundleName ?? '',
      abilityName: want.abilityName ?? '',
      moduleName: want.moduleName,
    }
  }

  onForeground() {
    // 应用进入前台，调用tag模块中前台优先的接口，使能前台应用程序优先处理所发现的NFC标签功能
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
    if (nfcTagElementName != undefined) {
      // 根据业务需要，选择需要读取标签的通信技术
      let techList: number[] = [tag.NFC_A, tag.NFC_B, tag.NFC_F, tag.NFC_V];
      try {
        tag.on('readerMode', nfcTagElementName, techList, readerModeCb);
        foregroundRegister = true;
      } catch (error) {
        hilog.error(0x0000, 'testTag', 'on readerMode error = %{public}s', JSON.stringify(error));
      }
    }
  }

  onBackground() {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
    // 退出应用程序NFC标签页面时，调用tag模块退出前台优先功能
    if (foregroundRegister) {
      foregroundRegister = false;
      try {
        tag.off('readerMode', nfcTagElementName);
      } catch (error) {
        hilog.error(0x0000, 'testTag', 'off readerMode error = %{public}s', JSON.stringify(error));
      }
    }
  }
}
```

### 后台读取标签

1. 在module.json5文件中声明NFC标签读取的权限，声明NFC标签特定的action，以及声明本应用程序的能够处理的NFC标签技术类型。
2. import需要的tag模块和其他相关的模块。
3. 获取特定技术类型的NFC标签对象。
4. 执行读写接口完成标签数据的读取或写入数据到标签。

应用程序需要支持后台读卡时，需要在应用的属性配置文件中，声明与NFC相关的属性值。比如，在module.json5文件中，声明下面属性值。

**说明** 

1. 声明"actions"字段的内容填写，必须包含"ohos.nfc.tag.action.TAG\_FOUND"，不能更改。
2. 声明技术时"uris"中"type"字段的内容填写，前缀必须是"tag-tech/"，后面接着NfcA/NfcB/NfcF/NfcV/IsoDep/Ndef/MifareClassic/MifareUL/NdefFormatable"中的一个。如果存在多个"type"时，需要分行填写。填写错误会造成解析失败。
3. 声明权限时"requestPermissions"中的"name"字段的内容填写，必须是"ohos.permission.NFC\_TAG"，不能更改。
4. Wearable设备不支持后台读卡。

```ts
    "abilities": [
      {
        "name": "EntryAbility",
        "srcEntry": "./ets/entryability/EntryAbility.ts",
        "description": "$string:EntryAbility_desc",
        "icon": "$media:icon",
        "label": "$string:EntryAbility_label",
        "startWindowIcon": "$media:icon",
        "startWindowBackground": "$color:start_window_background",
        "exported": true,
        "skills": [
          {
            "entities": [
              "entity.system.home"
            ],
            "actions": [
              "ohos.want.action.home",

              // actions必须包含"ohos.nfc.tag.action.TAG_FOUND"
              "ohos.nfc.tag.action.TAG_FOUND"
            ],

            // 根据业务需要至少定义一种读标签的技术类型，‘tag-tech/’是前缀，后面跟着技术类型描述
            "uris": [
              {
                  "type":"tag-tech/NfcA"
              },
              {
                  "type":"tag-tech/IsoDep"
              }
              // 必要时可添加其他技术类型
              // 例如: NfcB/NfcF/NfcV/Ndef/MifareClassic/MifareUL/NdefFormatable
            ]
          }
        ]
      }
    ],
    "requestPermissions": [
      {
        // 添加NFC标签操作的权限
        "name": "ohos.permission.NFC_TAG",
        "reason": "$string:app_name",
      }
    ]
```

```ts
import { tag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');

    // 获取特定技术类型的NFC标签对象
    let tagInfo: tag.TagInfo;
    try {
      tagInfo = tag.getTagInfo(want);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'getTagInfo error = %{public}s', JSON.stringify(error));
      return;
    }

    if (tagInfo == null) {
      hilog.error(0x0000, 'testTag', 'tagInfo is invalid');
      return;
    }
    if (tagInfo.uid == null) {
      hilog.error(0x0000, 'testTag', 'uid is invalid');
      return;
    }
    if (tagInfo.technology == null || tagInfo.technology.length == 0) {
      hilog.error(0x0000, 'testTag', 'technology is invalid');
      return;
    }

    // 标签里面可能支持多种技术类型，选择特定的技术类型接口，完成标签数据的读取或写入
    // 下面示例代码，使用IsoDep完成标签数据的读取或写入
    let isoDep: tag.IsoDepTag | null = null;
    for (let i = 0; i < tagInfo.technology.length; i++) {
      if (tagInfo.technology[i] == tag.ISO_DEP) {
        try {
          isoDep = tag.getIsoDep(tagInfo);
        } catch (error) {
          hilog.error(0x0000, 'testTag', 'getIsoDep error = %{public}s', JSON.stringify(error));
          return;
        }
      }
      // 也可以按需选择其它类型的技术读写标签
    }
    if (isoDep == null) {
      hilog.error(0x0000, 'testTag', 'getIsoDep is invalid');
      return;
    }

    // 使用IsoDep技术连接到NFC标签
    try {
      isoDep.connect();
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'isoDep.connect() error = %{public}s', JSON.stringify(error));
      return;
    }
    if (!isoDep.isConnected()) {
      hilog.error(0x0000, 'testTag', 'isoDep.isConnected() false.');
      return;
    }

    // 发送指令到已连接的标签，获取标签的响应数据
    let cmdData = [0x01, 0x02, 0x03, 0x04]; // 修改为正确的访问标签的指令数据
    try {
      isoDep.transmit(cmdData).then((response: number[]) => {
        hilog.info(0x0000, 'testTag', 'isoDep.transmit() response = %{public}s.', JSON.stringify(response));
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, 'testTag', 'isoDep.transmit() err = %{public}s.', JSON.stringify(err));
        return;
      });
    } catch (businessError) {
      hilog.error(0x0000, 'testTag', 'isoDep.transmit() businessError = %{public}s.', JSON.stringify(businessError));
      return;
    }
  }
}
```

### NDEF格式Tag定制

* NFC标签定制

  1. NDEF标签可能存在1或多个Record。通过包名拉起HarmonyOS应用需要特定的Record记录：其中type为“ohos.com:pkg”，payload为“应用实际包名”。
  2. 根据应用业务逻辑的需要，标签内的第一个Record可以放入一个URI类型的数据（可选）。如果存在URI类型的Record，NFC拉起应用时会以want.uri格式传递给应用，此时应用可以通过识别URI来跳转到指定页面。

  **说明** 

  若应用拉起时需要URI数据，第一个Record必须为URI类型。
* 应用接收参数示例

  拉起应用时，应用可以通过want里传入的参数来完成业务逻辑，通过卡片拉起应用时，携带的want内容如下：

```ts
want = {
    "deviceId": "",
    "bundleName": "xxx",
    "abilityName": "xxx",
    "moduleName": "xxx",
    "uri": "https://xxx.com", // NFC卡片里写入的uri
    "type": "",
    "flags": 0,
    "action": "action.system.home",
    "parameters": {
        // NFC相关字段
        "Atqa": "4400",
        "MifareUltralightC": false,
        "NdefForumType": 2,
        "NdefMsg": "xxxxxxxxxx", // 16进制字节码格式的完整NDEF message
        "NdefTagLength": 868,
        "NdefTagMode": 2,
        "Sak": 0,
        "tagRfDiscId": 2,
        "technology": [1, 9, 6], // 读取到的卡片支持的协议类型，NfcA，NfcB，NfcF，NfcV，Ndef，IsoDep等
        "uid": "xxxxxxxx", // 读取到的卡片的uid
        // 其它内容
        "component.startup.newRules": true,
        "isCallBySCB": false,
        "isShellCall": false,
        "moduleName": "entry",
        "ohos.aafwk.param.callerAbilityName": "",
        "ohos.aafwk.param.callerBundleName": "",
        "ohos.aafwk.param.callerNativeName": "_nfc_service", // NFC进程名
        "ohos.aafwk.param.callerPid": xxx,
        "ohos.aafwk.param.callerToken": xxxx,
        "ohos.aafwk.param.callerUid": xxxx,
        "ohos.aafwk.param.displayId": 0,
        "ohos.dlp.params.sandbox": false,
        "ohos.param.callerAppCloneIndex": 0,
        "remoteTagService": {
            "type": "RemoteObject",
            "value": {}
            }
        },
        "fds": {},
        "entities": ["entity.system.home"]
    }
```
