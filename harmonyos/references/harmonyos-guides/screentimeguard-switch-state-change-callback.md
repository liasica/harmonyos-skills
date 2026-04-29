---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-switch-state-change-callback
title: 健康使用设备授权列表页中应用授权开关打开/关闭时触发回调
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 用户授权管理 > 健康使用设备授权列表页中应用授权开关打开/关闭时触发回调
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:edef7a1d872af2597658dc69c1b92c2895bb6710bfb2899d9c991690ede81216
---

## 场景介绍

当通过健康使用设备授权列表页中的授权开关开启或者关闭应用授权时（设置-健康使用设备-右上角四点设置![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/NrRTHc56R0KqkllGkMUDvw/zh-cn_image_0000002558606010.png?HW-CC-KV=V1&HW-CC-Date=20260429T054026Z&HW-CC-Expire=86400&HW-CC-Sign=CD4B4D30844A630C330EEF798FA6769DF89110E99B199405EED34B2E4DF1509D)-可访问健康使用设备的应用），会执行TimeGuardExtensionAbility中的onUserAuthSwitchOn/onUserAuthSwitchOff回调方法，支持开发者在用户授予授权和撤销授权时执行特定逻辑。若之前已设置过健康使用设备的密码，则在此页面取消应用授权时需要输入健康使用设备的密码。

注意

应用调用Screen Time Guard Kit接口获取授权或者取消授权时，不会触发onUserAuthSwitchOn/onUserAuthSwitchOff回调方法。只有在健康使用设备授权列表页操作授权开关时才会触发。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/iQinrq2mRZqOctbYHYcnHw/zh-cn_image_0000002589325537.png?HW-CC-KV=V1&HW-CC-Date=20260429T054026Z&HW-CC-Expire=86400&HW-CC-Sign=4833EB4F1E2311FD08B66E34441E945B8BCC4344FDCCD3971E4666AD529B6910)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/rF7rDIp0QMqDTveslQGjWw/zh-cn_image_0000002589245475.png?HW-CC-KV=V1&HW-CC-Date=20260429T054026Z&HW-CC-Expire=86400&HW-CC-Sign=0F7422AC514AD64BEBA899597C5CF39A30CFA6E7EDD6323C1DA9CDD2CCE31950)

流程说明（以关闭授权开关为例）：

1. 应用继承TimeGuardExtensionAbility，实现onUserAuthSwitchOn、onUserAuthSwitchOff方法，以监听用户授权状态。
2. 用户在健康使用设备的授权列表页中关闭授权开关后会拉起extension进程，执行TimeGuardExtensionAbility的onUserAuthSwitchOff回调。
3. onUserAuthSwitchOff回调执行，应用可以在该回调中可以执行特定逻辑。

## 接口说明

授权开关打开/关闭时的回调关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [onUserAuthSwitchOn](../harmonyos-references/screentimeguard-timeguardextensionability.md#onuserauthswitchon)(): Promise<void> | 当用户授予授权时执行特定逻辑。 |
| [onUserAuthSwitchOff](../harmonyos-references/screentimeguard-timeguardextensionability.md#onuserauthswitchoff)(): Promise<void> | 当用户撤销授权时执行特定逻辑。 |

说明

1. TimeGuardExtensionAbility与应用运行在不同进程，但共用沙箱。
2. TimeGuardExtensionAbility与应用直接无法直接传递数据，如需传递数据可以通过[用户首选项](../harmonyos-references/js-apis-data-preferences.md)/[数据库](../harmonyos-references/js-apis-data-relationalstore.md)等数据持久化手段进行传递，或者通过[公共事件模块](../harmonyos-references/js-apis-commoneventmanager.md)传递。

## 开发步骤

1. 导入相关模块。

   ```
   1. import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 继承TimeGuardExtensionAbility，重写onUserAuthSwitchOn和onUserAuthSwitchOff 回调。

   ```
   1. export default class EntryAbility extends TimeGuardExtensionAbility {
   2. async onUserAuthSwitchOn(): Promise<void> {
   3. hilog.info(0x0000, 'EntryAbility', 'test --- onUserAuthSwitchOn');
   4. }

   6. async onUserAuthSwitchOff(): Promise<void> {
   7. hilog.info(0x0000, 'EntryAbility', 'test --- onUserAuthSwitchOff');
   8. }
   9. }
   ```
3. 在工程中entry模块的module.json5文件中的"extensionAbilities"节点添加如下代码。

   ```
   1. "extensionAbilities": [{
   2. "name": "EntryAbility",
   3. "type": "screenTimeGuard",
   4. "srcEntry": "./ets/entryability/EntryAbility.ets",
   5. "exported": false,
   6. "skills": [{
   7. "actions": ["action.ohos.timeGuard.listener"]
   8. }]
   9. }],
   ```
