---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-form-update
title: 推送卡片刷新消息
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > 推送场景化消息 > 推送卡片刷新消息
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:55+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:1014bfa72fd881f1ad2960e2e66f19eaa6a619b85e73613435dc2a3d3b52d318
---

## 场景介绍

如今衣食住行娱乐影音应用占据了大多数人的手机，一部手机可以满足日常大多需求，但对需要经常查看或进行简单操作的应用来说，总需要用户点开应用体验较繁琐。针对此种场景，HarmonyOS提供了[Form Kit（卡片开发服务）](form-kit.md)，您可以将应用的重要信息或操作前置到卡片，以达到服务直达、减少体验层级的目的。

面对需要实时更新信息的应用卡片，Push Kit向开发者提供了卡片刷新服务。应用通过集成Push Kit后获取Push Token，基于Push Kit的系统级通道，便可以在合适场景向用户即时推送卡片内容，从而提升用户的感知度和活跃度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/fUMR5u2eQlKMlB2sai78vg/zh-cn_image_0000002558765624.png?HW-CC-KV=V1&HW-CC-Date=20260429T053954Z&HW-CC-Expire=86400&HW-CC-Sign=E35EAA0D4E638FB00E906D08515B544E09F00F77C93901655BB9AC0CFD9CB271)

## 约束与限制

推送卡片刷新消息支持Phone、Tablet、PC/2in1设备。并且从6.1.0(23)版本开始，新增支持Wearable、TV设备。

## 频控规则

**调测阶段**，每个项目每日全网最多可推送1000条测试消息。发送测试消息需设置[testMessage](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)为true。

**正式发布阶段**，单设备单应用下每日推送消息总条数受[设备消息频控](../harmonyos-references/push-msg-freq-control.md#设备消息频控)限制，系统会根据现网使用场景和流量进行管控，不合理的使用场景系统会进行频控。

单张服务卡片刷新消息数量受应用是否上架影响：

* 已上架：单设备单应用下单张卡片每日限制发送2条消息。
* 未上架：单设备单应用下单张卡片每日限制发送5条消息。

说明

不论是测试消息还是正式消息，卡片刷新消息单次发送仅能携带一个Token。

## 开发步骤

### 开发卡片

推送卡片刷新消息前，您需先完成本地卡片的开发。

1. 参见[创建一个ArkTS卡片](arkts-ui-widget-creation.md)，完成本地服务卡片的创建。
2. 在项目模块级别下的**src/main/resources/base/profile/form\_config.json**中配置dataProxyEnabled字段为**true**，开启卡片代理刷新功能。

   ```
   1. {
   2. "forms": [
   3. {
   4. "name": "widget",
   5. "src": "./ets/widget/pages/WidgetCard.ets",
   6. "uiSyntax": "arkts",
   7. "window": {
   8. "designWidth": 720,
   9. "autoDesignWidth": true
   10. },
   11. "colorMode": "auto",
   12. "isDefault": true,
   13. "updateEnabled": true,
   14. "updateDuration": 1,
   15. "scheduledUpdateTime": "10:30",
   16. "defaultDimension": "2*2",
   17. "supportDimensions": ["2*2"],
   18. "dataProxyEnabled": true
   19. }
   20. ]
   21. }
   ```
3. 在卡片生命周期管理文件（下以EntryFormAbility为例）的[onAddForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonaddform)()回调中获取**formId**，定义需要在卡片页面文件（下以WidgetCard为例）中和通过Push Kit要刷新的字段，如下以**text\_key**和**image\_key**为例。

   ```
   1. // 文件路径: src/main/ets/entryformability/EntryFormAbility.ets
   2. import { formBindingData, formInfo, FormExtensionAbility } from '@kit.FormKit';
   3. import { Want } from '@kit.AbilityKit';

   5. export default class EntryFormAbility extends FormExtensionAbility {
   6. onAddForm(want: Want): formBindingData.FormBindingData {
   7. // 获取formId
   8. const formId = want.parameters![formInfo.FormParam.IDENTITY_KEY] as string;

   10. // 定义需要在WidgetCard中刷新的字段
   11. class CreateFormData {
   12. formId: string = '';
   13. text_key: string = '';
   14. image_key: string = '';
   15. }

   17. const obj: CreateFormData = {
   18. formId: formId,
   19. text_key: '默认文本',
   20. image_key: ''
   21. }
   22. const bindingData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);

   24. // 定义需要通过Push Kit代理刷新的字段，每个key均需要在上面bindingData中定义
   25. const text_key: formBindingData.ProxyData = {
   26. key: 'text_key',
   27. subscriberId: formId
   28. };
   29. const image_key: formBindingData.ProxyData = {
   30. key: 'image_key',
   31. subscriberId: formId
   32. };
   33. bindingData.proxies = [text_key, image_key];
   34. return bindingData;
   35. }
   36. }
   ```
4. 卡片页面文件（**下以src/main/ets/widget/pages/WidgetCard.ets为例**）中，创建[LocalStorage](arkts-localstorage.md)变量并与[@Entry](arkts-create-custom-components.md#entry)装饰器绑定，使用[@LocalStorageProp](arkts-localstorage.md#localstorageprop)装饰器创建key-value的变量。

   本文创建了formId、text和image三个变量，对应的key为**formId**、**text\_key**和**image\_key**，需要注意的是卡片页面布局中image对应的组件是Image图片组件，图片组件传递的变量必须以**memory://** 开头。

   ```
   1. // 文件路径: src/main/ets/widget/pages/WidgetCard.ets
   2. // 定义页面级的UI状态存储LocalStorage
   3. const storage = new LocalStorage();

   5. // 绑定
   6. @Entry(storage)
   7. @Component
   8. struct WidgetCard {
   9. @LocalStorageProp('formId') formId: string = '';
   10. @LocalStorageProp('text_key') text: string = '';
   11. @LocalStorageProp('image_key') image: string = '';

   13. build() {
   14. Flex({ direction: FlexDirection.Column }) {
   15. Row() {
   16. Text() {
   17. // Span是Text组件的子组件，用于显示行内文本
   18. Span('formID:')
   19. Span(this.formId)
   20. }
   21. .fontSize(10)
   22. }

   24. Row() {
   25. Text() {
   26. Span('文本:')
   27. Span(this.text)
   28. }
   29. .fontSize(10)
   30. }

   32. Row() {
   33. if (this.image) {
   34. Image('memory://' + this.image).height(80)
   35. }
   36. }
   37. }
   38. .padding(10)
   39. .onClick(() => {
   40. postCardAction(this, {
   41. action: 'router',
   42. abilityName: 'MainAbility', // 请配置为应用实际的abilityName
   43. });
   44. })
   45. }
   46. }
   ```

### 推送卡片刷新消息

1. 参见指导[获取Push Token](push-get-token.md)。
2. （可选）建议您将**formId**、**pushToken**等信息上报到应用服务端，用于向应用发送卡片刷新消息。

   ```
   1. // 以下为伪代码
   2. import { Want } from '@kit.AbilityKit';
   3. import { pushService } from '@kit.PushKit';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';
   5. import { BusinessError } from '@kit.BasicServicesKit';
   6. import { formInfo } from '@kit.FormKit';

   8. async function saveFormInfo(want: Want): Promise<void> {
   9. try {
   10. const formId = want.parameters![formInfo.FormParam.IDENTITY_KEY] as string;
   11. const moduleName = want.moduleName;
   12. const abilityName = want.abilityName;
   13. const formName = want.parameters![formInfo.FormParam.NAME_KEY] as string;
   14. const pushToken: string = await pushService.getToken();

   16. // 将formId, moduleName, abilityName, formName, pushToken 上报到应用服务端
   17. } catch (err) {
   18. let e: BusinessError = err as BusinessError;
   19. hilog.error(0x0000, 'testTag', 'Failed to save form info: %{public}d %{public}s', e.code, e.message);
   20. }
   21. }
   ```
3. 应用服务端调用REST API推送卡片刷新消息，消息详情可参见[场景化消息API接口功能介绍](../harmonyos-references/push-scenariozed-api-intro.md)，请求示例如下：

   ```
   1. // Request URL
   2. POST "https://push-api.cloud.huawei.com/v3/[projectId]/messages:send"

   4. // Request Header
   5. Content-Type: application/json
   6. Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
   7. push-type: 1

   9. // Request Body
   10. {
   11. "payload": {
   12. "moduleName": "entry",
   13. "abilityName": "EntryFormAbility",
   14. "formName": "widget",
   15. "formId": 423434262,
   16. "version": 123456,
   17. "formData": {
   18. "text_key": "刷新文本内容"
   19. },
   20. "images": [
   21. {
   22. "keyName": "image_key",
   23. "url": "https://***.png",
   24. "require": 1
   25. }
   26. ]
   27. },
   28. "target": {
   29. "token": [
   30. "MAMzLg**********lPW"
   31. ]
   32. },
   33. "pushOptions": {
   34. "testMessage": true
   35. }
   36. }
   ```

   * [projectId]：项目ID，登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”，在该页面获取。
   * Authorization：JWT格式字符串，可参见[Authorization](../harmonyos-references/push-scenariozed-api-request-struct.md#request-header)获取。
   * push-type：1表示服务卡片刷新场景。
   * moduleName：项目模块级别下的 **src/main/module.json5** 中的 **module **标签下的**name**值。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/A7rpv3x8QTKrXQC24mPcvw/zh-cn_image_0000002558605968.png?HW-CC-KV=V1&HW-CC-Date=20260429T053954Z&HW-CC-Expire=86400&HW-CC-Sign=9D33BA6AD0D42E803904360FA0C05BE42CE64FACF4D914F709AC0EC38DB3C748)
   * abilityName：项目模块级别下的**src/main/module.json5**中的**extensionAbilities**标签下的服务卡片的ability名称。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/VTSONYX4TMS8s5moXPw3RQ/zh-cn_image_0000002589325495.png?HW-CC-KV=V1&HW-CC-Date=20260429T053954Z&HW-CC-Expire=86400&HW-CC-Sign=516C4904BF1215E0C4A2EB0FD045B1C1C43F4E723FFB1C883EE98CCF1D30E5EB)
   * formName：项目模块级别下的**src/main/resources/base/profile/form\_config.json**中**forms**标签下服务卡片的名称。下图以卡片配置文件form\_config为例：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/7Qr8JYg-QlusC4R7iB5BJA/zh-cn_image_0000002589245433.png?HW-CC-KV=V1&HW-CC-Date=20260429T053954Z&HW-CC-Expire=86400&HW-CC-Sign=6790BF08BF0ABD81C6B8945EB93F5D3562A169402C515BB15ABB305C302B304A)
   * version：当前卡片刷新消息的版本号，新的卡片刷新消息的版本号需**大于**当前卡片刷新消息版本号，否则会刷新失败。详情参见[version](../harmonyos-references/push-scenariozed-api-request-param.md#formupdatepayload-卡片刷新消息)。
   * formId：服务卡片的实例ID，当卡片的[onAddForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonaddform)()方法被调用时（卡片使用方添加卡片至桌面）进行获取。最大值为**231-1**。
   * formData：填写待刷新服务卡片的业务数据，该数据来源于项目模块级别下的**src/main/ets/widget/pages/WidgetCard.ets**文件下的声明式范式组件名称。下图以卡片页面文件WidgetCard为例：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/7QroMG2wSDy4ZuK4UyjAcw/zh-cn_image_0000002558765626.png?HW-CC-KV=V1&HW-CC-Date=20260429T053954Z&HW-CC-Expire=86400&HW-CC-Sign=A053C60A3792A3DDA66A47AF088E4605671B8DA8A9319CB4AB20168595DB46C5)
   * images：待刷新服务卡片业务数据中的图片数据，其中keyName为您服务卡片中图片控件的key值，url为图片的地址，下图以卡片页面文件**WidgetCard**为例：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/w0Ii6LuzQFGynqWvnuzR8w/zh-cn_image_0000002558605970.png?HW-CC-KV=V1&HW-CC-Date=20260429T053954Z&HW-CC-Expire=86400&HW-CC-Sign=C0C3073A50EDEEBFB81531B1540CBDC1C8433BEE7C54093CFF395F3B0156A02F)

     说明

     Push Kit禁止推送包含敏感信息的图片。

     支持图片的格式为PNG、JPG、JPEG、WEBP，图片文件最大为512KB，若超过则图片不展示。
   * require：图片刷新策略控制，“0”表示如果图片下载失败，仅刷新文字；“1”表示如果图片下载失败，则不进行刷新操作。
   * token：Push Token，可参见[获取Push Token](push-get-token.md)获取。
   * testMessage：（选填）测试消息标识，true表示测试消息。每个项目每天限制发送1000条测试消息，单次推送仅能发送一个Token。详情请参见[testMessage](../harmonyos-references/push-scenariozed-api-request-param.md#pushoptions)。
