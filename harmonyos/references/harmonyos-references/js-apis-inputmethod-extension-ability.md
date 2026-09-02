---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-extension-ability
title: "@ohos.InputMethodExtensionAbility (InputMethodExtensionAbility)"
breadcrumb: API参考 > 应用框架 > IME Kit（输入法开发服务） > ArkTS API > @ohos.InputMethodExtensionAbility (InputMethodExtensionAbility)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ea1300da69fa2a479c9f5d197b75d00e2f2c9d425c65481bfb43990062a083e0
---

@ohos.InputMethodExtensionAbility模块提供输入法ExtensionAbility（扩展能力基类）的基础类定义，是开发输入法应用的入口和生命周期管理框架。

本模块是输入法ExtensionAbility的核心类模块，定义了InputMethodExtensionAbility类，作为输入法应用的Extension基类。开发者需继承该类并实现onCreate和onDestroy生命周期回调，系统在拉起和销毁输入法Extension时自动调用这些回调。

本模块提供两大核心能力：1）通过onCreate(want)回调实现输入法应用的初始化——系统拉起输入法Extension时调用，开发者在此完成资源加载、面板创建等初始化工作；2）通过onDestroy()回调实现输入法应用的资源清理——系统销毁输入法Extension时调用，开发者在此释放资源。此外，通过context属性提供InputMethodExtensionContext上下文对象，供开发者在生命周期内执行销毁自身、拉起其他应用等上下文级操作。

当开发输入法应用时必须使用本模块。开发者通过继承InputMethodExtensionAbility → 在module.json5中配置ExtensionAbility信息 → 系统拉起时触发onCreate（初始化） → 系统销毁或开发者主动调用context.destroy()时触发onDestroy（清理）。

**说明** 

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

InputMethodExtensionAbility仅定义了基础的onCreate和onDestroy两个生命周期回调。输入法的核心交互能力（如面板创建/销毁、键盘事件监听、客户端绑定等）需在onCreate回调中通过@ohos.inputMethodEngine模块获取InputMethodAbility对象来实现。onCreate是所有关键对象获取和面板创建的唯一入口，必须在该回调中完成初始化。

InputMethodExtensionAbility的context属性类型为InputMethodExtensionContext（来自@ohos.InputMethodExtensionContext模块），属于关联关系——InputMethodExtensionAbility拥有InputMethodExtensionContext的上下文能力。

| Class | 说明 |
| --- | --- |
| InputMethodExtensionAbility | 输入法ExtensionAbility基类，提供输入法应用的生命周期管理框架。关键成员包括：context属性（InputMethodExtensionContext上下文对象）、onCreate(want)方法（初始化回调）、onDestroy()方法（销毁回调）。开发者需继承此类并重写生命周期方法。 |

## 约束限制

为保障系统安全性和稳定性，防止InputMethodExtensionAbility滥用系统资源，系统对其能力进行管控，不支持部分模块的引用，详情请参考[附录](js-apis-inputmethod-extension-ability.md#附录)。

另外输入法应用区分基础模式和完整体验模式，关于基础模式和完整体验模式说明如下：

**基础模式介绍：**

基础模式下，输入法扩展（InputMethodExtensionAbility）进程无法拉起其他UIAbility或ExtensionAbility。

基础模式下，输入法扩展会受到系统管控，不能使用涉及访问或泄露用户个人数据的各种接口，同时无法将数据传递出进程。管控功能包括但不限于：网络、短信、电话、麦克风、定位、相机、蓝牙、壁纸、支付、日历、游戏、扬声器、Wi-Fi、剪贴板、多媒体、联系人、公共事件、系统账号、健康数据、地图服务、推送服务、融合搜索、共享内存、分布式特性、广告设备标识、振动等。

基础模式下，输入法扩展可以使用基础输入功能必要的系统能力，例如，IME Kit、ArkUI、窗口、图形、屏幕管理等。

基础模式下，输入法扩展对共享沙箱只读，对输入法扩展独立沙箱可读写；应用主入口可以对共享沙箱及其独立沙箱读写。

**完整体验模式介绍：**

完整体验模式下，输入法扩展不受基础模式相关限制，例如可以拉起其他UIAbility或ExtensionAbility、可以调用访问用户数据的接口等。

完整体验模式下，输入法扩展可以对共享沙箱读写。

## 导入模块

```ts
import { InputMethodExtensionAbility } from '@kit.IMEKit';
```

## InputMethodExtensionAbility

输入法ExtensionAbility类，提供了输入法应用的核心能力，支持开发者创建输入法应用。

下列API均需通过继承InputMethodExtensionAbility创建子类后，在子类中重写或使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [InputMethodExtensionContext](js-apis-inputmethod-extension-context.md) | 否 | 否 | InputMethodExtensionAbility的上下文环境，继承于ExtensionContext。 |

context参数使用建议：

* 含义/功能：提供InputMethodExtensionContext上下文对象，用于执行输入法应用上下文级操作，包括销毁自身（destroy()）和拉起其他应用（startAbility()）。
* 使用场景：当输入法应用需要主动终止自身运行或拉起目标应用时使用context属性。context在onCreate回调触发后即可使用。
* 使用后效果：通过context.destroy()可销毁当前ExtensionAbility；通过context.startAbility(want)可拉起目标应用。
* 前提条件：context由系统在创建InputMethodExtensionAbility实例时自动赋值，开发者无需手动创建。context仅在ExtensionAbility生命周期内有效，onDestroy回调执行后context将不可用。
* 相关接口间的配合/制约关系：context需配合@ohos.inputMethodEngine模块使用——在onCreate回调中，context作为InputMethodAbility.createPanel()的参数传入，用于创建输入法面板。

### onCreate

onCreate(want: Want): void

生命周期回调，在拉起输入法Extension时调用，用于初始化输入法应用。

* 含义/功能：系统拉起输入法ExtensionAbility时触发的初始化回调。开发者在该回调中完成输入法应用的所有关键初始化工作，包括获取核心能力对象、创建输入法面板、订阅事件等。
* 使用场景：当系统根据module.json5配置拉起输入法ExtensionAbility时自动触发。这是输入法应用初始化的唯一入口，所有关键对象的获取和面板创建必须在此回调中完成。
* 使用后效果：回调执行完成后，输入法应用进入正常运行状态。系统将随后触发键盘显示/隐藏请求、客户端绑定等事件，输入法应用需在此之前完成初始化（如已订阅on('inputStart')事件、已创建面板等），否则后续事件可能无法正常响应。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 当前Extension相关的Want类型信息，包括Ability名称、bundle名称等。 |

want参数使用建议：

* 含义/功能：系统传递给onCreate回调的Want信息，描述当前ExtensionAbility的启动信息。
* 使用场景：开发者可通过want获取启动参数（如abilityName、bundleName等），用于判断启动场景或获取配置参数。
* 取值范围：Want对象包含多种类型的属性，常见属性如abilityName、bundleName等为string类型。want中包含的abilityName和bundleName与module.json5中配置的值一致。
* 注意事项：want参数由系统自动传入，开发者无需手动构造。

注意事项：

* 前提条件：onCreate是输入法应用初始化的核心入口。必须在onCreate中完成以下关键初始化工作：
  1. 通过inputMethodEngine.getInputMethodAbility()获取InputMethodAbility实例。
  2. 通过inputMethodEngine.getKeyboardDelegate()获取KeyboardDelegate实例。
  3. 订阅on('inputStart')事件以接收编辑框绑定通知。
  4. 创建输入法面板（InputMethodAbility.createPanel(this.context, panelInfo)），注意this.context参数必须传入。
  5. 订阅其他必要事件（如on('keyboardShow')、on('setSubtype')等）。
* 开发建议：建议将面板创建和事件订阅集中放在onCreate中完成，避免在其他时机初始化导致事件遗漏或面板创建失败。

相关接口间的配合/制约关系：onCreate需配合以下接口使用：

* inputMethodEngine.getInputMethodAbility()：获取输入法能力对象。
* inputMethodEngine.getKeyboardDelegate()：获取键盘代理对象。
* InputMethodAbility.createPanel(this.context, panelInfo)：创建面板时必须使用onCreate中可获取的this.context作为参数。
* InputMethodAbility.on('inputStart')：必须在onCreate中订阅，否则后续编辑框绑定事件无法接收。

**示例：**

```ts
import { InputMethodExtensionAbility, inputMethodEngine } from '@kit.IMEKit';
import { Want } from '@kit.AbilityKit';

class InputMethodExt extends InputMethodExtensionAbility {
  onCreate(want: Want): void {
    console.info(`onCreate, want: ${want.abilityName}`);

    // 获取输入法能力对象
    let ability: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();

    // 获取键盘代理对象
    let keyboardDelegate: inputMethodEngine.KeyboardDelegate = inputMethodEngine.getKeyboardDelegate();

    // 创建面板
    let panelInfo: inputMethodEngine.PanelInfo = {
      type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
      flag: inputMethodEngine.PanelFlag.FLG_FIXED
    };
    ability.createPanel(this.context, panelInfo, (err, panel) => {
      if (err) {
        console.error(`Failed to create panel: ${err.code}`);
        return;
      }
      console.info('Succeeded in creating panel.');
    });

    // 订阅输入法绑定事件
    ability.on('inputStart', (kbController, inputClient) => {
      console.info('Input method bound to client.');
    });
  }
}
```

### onDestroy

onDestroy(): void

生命周期回调，在销毁输入法应用时调用，用于资源清理。

* 含义/功能：系统销毁输入法ExtensionAbility时触发的清理回调。开发者在该回调中释放面板、取消事件订阅等资源清理工作。
* 使用场景：当系统主动销毁输入法ExtensionAbility（如系统回收资源、用户切换到其他输入法）或开发者主动调用context.destroy()触发销毁时自动触发。注意：onDestroy回调执行后，context将不可用，不应在回调中或回调后继续使用context对象。
* 使用后效果：回调执行完成后，输入法ExtensionAbility进程终止，所有资源应已释放。调用后再进行其他操作将不起效。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**注意事项：**

* 开发建议：建议在onDestroy中完成以下清理工作：
  1. 销毁已创建的面板（InputMethodAbility.destroyPanel(panel)）。
  2. 取消所有事件订阅（InputMethodAbility.off('inputStart')等）。
  3. 释放其他应用资源（如缓存数据、定时器等）。
* 开发建议：未在onDestroy中正确销毁面板可能导致面板资源泄漏，影响系统资源使用。

相关接口间的配合/制约关系：onDestroy需配合以下接口使用：

* InputMethodAbility.destroyPanel(panel)：销毁在onCreate中创建的面板，必须与createPanel配对调用。
* InputMethodAbility.off('inputStart')等：取消在onCreate中订阅的事件。
* context.destroy()：开发者主动调用context.destroy()会触发系统执行onDestroy回调。

**示例：**

```ts
import { InputMethodExtensionAbility } from '@kit.IMEKit';

class InputMethodExt extends InputMethodExtensionAbility {
  onDestroy(): void {
    // 销毁面板、取消事件订阅等清理工作
    console.info('onDestroy');
  }
}
```

## 附录

InputMethodExtensionAbility不支持以下模块的引用。

| Kit | 模块 |
| --- | --- |
| Ability Kit | [@ohos.ability.featureAbility (FeatureAbility模块)](js-apis-ability-featureability.md)  [@ohos.ability.particleAbility (ParticleAbility模块)](js-apis-ability-particleability.md) |
| Background Tasks Kit | [@ohos.resourceschedule.backgroundTaskManager (后台任务管理)](js-apis-resourceschedule-backgroundtaskmanager.md)  [@ohos.reminderAgentManager (后台代理提醒)](js-apis-reminderagentmanager.md)  [@ohos.reminderAgent (后台代理提醒)](js-apis-reminderagent.md) |
| Basic Services Kit | [@ohos.account.osAccount (系统账号管理)](js-apis-osaccount.md)  [@ohos.account.distributedAccount (分布式账号管理)](js-apis-distributed-account.md)  [@ohos.wallpaper (壁纸)](js-apis-wallpaper.md) |
| Connectivity Kit | [@ohos.bluetooth (蓝牙)](js-apis-bluetooth.md)  [@ohos.bluetoothManager (蓝牙)](js-apis-bluetoothmanager.md)  [nfctech (标准NFC-Tag Nfc 技术)](js-apis-nfctech.md)  [@ohos.nfc.controller (标准NFC)](js-apis-nfccontroller.md)  [@ohos.nfc.cardEmulation (标准NFC-cardEmulation)](js-apis-cardemulation.md)  [@ohos.connectedTag (有源标签)](js-apis-connectedtag.md)  [@ohos.wifiext (WLAN扩展接口)](js-apis-wifiext.md)  [@ohos.wifiManager (WLAN)](js-apis-wifimanager.md)  [@ohos.wifiManagerExt (WLAN扩展接口)](js-apis-wifimanagerext.md)  [tagSession (标准NFC-Tag TagSession)](js-apis-tagsession.md) |
| Location Kit | [@ohos.geolocation (位置服务)](js-apis-geolocation.md)  [@ohos.geoLocationManager (位置服务)](js-apis-geolocationmanager.md) |
| Telephony Kit | [@ohos.telephony.call (拨打电话)](js-apis-call.md)  [@ohos.telephony.data (蜂窝数据)](js-apis-telephony-data.md)  [@ohos.telephony.observer (电话服务状态监听)](js-apis-observer.md)  [@ohos.telephony.radio (网络搜索)](js-apis-radio.md)  [@ohos.telephony.sms (短信服务)](js-apis-sms.md)  [@ohos.telephony.sim (SIM卡管理)](js-apis-sim.md) |
