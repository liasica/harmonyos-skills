---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/callservice-enterprise-contact-display
title: 企业联系人信息来去电页面显示
breadcrumb: 指南 > 应用服务 > Call Service Kit（通话服务） > 企业联系人信息来去电页面显示
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d3740ad92e87d71c6477df66e683a51b03e09a9a3a5f928d26a7d80d605c8a16
---

本功能仅供企业应用开发者接入。

## 场景介绍

来去电时，页面显示已安装企业应用的联系人信息，方便用户识别来去电人信息，快速回应，增强企业内部沟通效率。

说明

来去电页面或横幅仅展示一个联系人信息，对于多个应用里存在相同联系人的情况，按照应用包名的字典序排序，展示首个查询结果。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [onQueryCallerInfo](../harmonyos-references/callservicekit-callerinfoquery-extension-ability.md#onquerycallerinfo)(phoneNumber: string)：Promise<CallerInfo> | 查询联系人信息接口。 |
| [queryNumberIdentifySwitchState](../harmonyos-references/callservicekit-numberldentify.md#querynumberidentifyswitchstate) (context: Context):SwitchState | 查询陌生号码与信息识别总开关状态以及调用该接口的应用号码识别开关状态。 |
| [isSupportEnterpriseNumberIdentify](../harmonyos-references/callservicekit-numberldentify.md#issupportenterprisenumberidentify)(context: Context): Promise<boolean> | 查询是否已开通企业来电显示权限。 |

## 申请接入

企业来电显示能力使用受限，如需接入，需要在AGC网站申请对应权限。

1.登录[AGC网站](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，选择“开发与服务”。

2.在项目列表选择项目，并在应用列表下选择需要申请企业来电显示的应用。

3.进入“项目设置 > 开放能力管理”页面，点击“企业来电显示”对应的“申请”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/c0nPFYyFQn6QwVXrlvHKiA/zh-cn_image_0000002552958836.png?HW-CC-KV=V1&HW-CC-Date=20260427T234835Z&HW-CC-Expire=86400&HW-CC-Sign=308C0A3A9536B1182AB74E922B5162DCBFC36530AB8A3BD30FF8B5A050877B72)

4.请根据实际业务需求在弹框中填写对应信息，完成后，点击右上角“提交”，提交后将在3个工作日内回复。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/DPdf-WEaQ_q10haHmemzOg/zh-cn_image_0000002583478837.png?HW-CC-KV=V1&HW-CC-Date=20260427T234835Z&HW-CC-Expire=86400&HW-CC-Sign=3628ADE40B594DE4013DB2A3EF223E99CDF004DFC70F63F647D9EE4232683D01)

## 替换调试Profile

当企业来电显示能力申请成功后，需要重新[申请调试Profile](../app/agc-help-add-debugprofile-0000001914423102.md)。并且在DevEco Studio中替换新申请的调试Profile。

## 开发步骤

1. 在工程内创建一个[ExtensionAbility](extensionability-overview.md)类型的自定义组件并继承[CallerInfoQueryExtensionAbility](../harmonyos-references/callservicekit-callerinfoquery-extension-ability.md#callerinfoqueryextensionability)，完成onQueryCallerInfo方法的复写。

   说明：

   由于调用onQueryCallerInfo方法时，系统先创建应用的AbilityStage实例，请勿在AbilityStage中添加过于复杂耗时的逻辑，避免调用超时。

   代码示例：

   ```
   1. import { CallerInfoQueryExtensionAbility, CallerInfo } from '@kit.CallServiceKit';

   3. export default class EntryCallerInfoQueryExtAbility extends CallerInfoQueryExtensionAbility {
   4. // 来去电时由系统通话应用主动调用该接口查询企业联系人信息
   5. onQueryCallerInfo(phoneNumber: string): Promise<CallerInfo> {
   6. return new Promise<CallerInfo>((resolve, reject) => {
   7. let isSuccess = true;
   8. // 在此处实现根据号码查询企业联系人的业务逻辑
   9. if (isSuccess) {
   10. // 查询成功，返回结果
   11. resolve({
   12. contactName:"xxxx",
   13. employeeId:"xxxx",
   14. department:"xxxx",
   15. position:"xxxx"
   16. });
   17. } else {
   18. // 查询失败，返回错误原因
   19. reject("error reason");
   20. }
   21. });
   22. }
   23. }
   ```
2. 在应用配置文件module.json5中注册extensionAbilities，具体详见[module.json5配置](module-configuration-file.md)。

   配置文件示例：

   ```
   1. {
   2. "extensionAbilities": [
   3. {
   4. "name": "EntryCallerInfoQueryExtAbility",
   5. "srcEntry": "./ets/callerinfoquery/EntryCallerInfoQueryExtAbility.ets",
   6. "type": "callerInfoQuery"
   7. }
   8. ]
   9. }
   ```

   * type标签需设为"callerInfoQuery"，表示该拓展类型为CallerInfoQueryExtensionAbility。
   * srcEntry标签表示上述ExtensionAbility组件所对应的代码路径。
3. 在调试设备上，前往“电话”，点击右上角的“更多”图标，前往“设置”>“陌生号码和信息识别”，打开对应企业应用的号码识别功能开关，进行调试。

## 应用跳转陌生号码和信息识别页面

从6.1.0(23)版本开始，新增支持从应用直接跳转到“电话 > 更多 > 设置 > 陌生号码和信息识别”。

通过[Deep Linking](deep-linking-startup.md)方式应用可以直接跳转“陌生号码和信息识别”页面。

以使用openLink实现应用跳转举例，在openLink接口的link字段中传入目标应用的URL信息，并将options字段中的appLinkingOnly配置为false、跳转的URL固定为"callsetting://number\_identity"。

其他跳转方式参考使用Deep Linking实现应用间跳转[拉起方应用实现应用跳转](deep-linking-startup.md#拉起方应用实现应用跳转)章节。

示例代码：

```
1. import { common, OpenLinkOptions } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. @Entry
6. @Component
7. struct Index {
8. build() {
9. Button('start link', { type: ButtonType.Capsule, stateEffect: true })
10. .width('87%')
11. .height('5%')
12. .margin({ bottom: '12vp' })
13. .onClick(() => {
14. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
15. let link: string = "callsetting://number_identity";
16. let openLinkOptions: OpenLinkOptions = {
17. appLinkingOnly: false
18. };
19. try {
20. context.openLink(link, openLinkOptions)
21. .then(() => {
22. hilog.info(0, 'TAG', 'Successed in opening link.');
23. }).catch((err: BusinessError) => {
24. hilog.error(0, 'TAG',`Failed to open link. Code is ${err.code}, message is ${err.message}`);
25. });
26. } catch (paramError) {
27. hilog.error(0, 'TAG',`Failed to start link. Code is ${paramError.code}, message is ${paramError.message}`);
28. }
29. })
30. }
31. }
```
