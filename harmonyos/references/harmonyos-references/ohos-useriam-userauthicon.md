---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-useriam-userauthicon
title: @ohos.userIAM.userAuthIcon (嵌入式用户身份认证控件)
breadcrumb: API参考 > 系统 > 安全 > User Authentication Kit（用户认证服务） > ArkTS组件 > @ohos.userIAM.userAuthIcon (嵌入式用户身份认证控件)
category: harmonyos-references
scraped_at: 2026-04-28T08:07:52+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:195309f234c6f1f4ac003ec853a034019b396854fe4a8a674bf3be56cfbf7f0c
---

提供应用界面上展示的人脸、指纹认证图标，具体功能如下：

1. 提供嵌入式的人脸、指纹认证控件图标，可被应用集成。
2. 支持自定义图标的颜色和大小，但图标样式不可变更。
3. 点击控件图标后将以系统弹窗的方式，拉起人脸、指纹认证控件。

说明

* 本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { userAuth, UserAuthIcon } from '@kit.UserAuthenticationKit';
```

## 子组件

PhonePC/2in1TabletWearable

无

## 属性

PhonePC/2in1TabletWearable

不支持通用属性。

## UserAuthIcon

PhonePC/2in1TabletWearable

```
1. UserAuthIcon({
2. authParam: userAuth.AuthParam,
3. widgetParam: userAuth.WidgetParam,
4. iconHeight?: Dimension,
5. iconColor?: ResourceColor,
6. onIconClick?: ()=>void,
7. onAuthResult: (result: userAuth.UserAuthResult)=>void
8. })
```

**装饰器类型：**@Component

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authParam | [userAuth.AuthParam](js-apis-useriam-userauth.md#authparam10) | 是 | 用户认证相关参数。 |
| widgetParam | [userAuth.WidgetParam](js-apis-useriam-userauth.md#widgetparam10) | 是 | 用户认证界面配置相关参数。 |
| iconHeight | [Dimension](ts-types.md#dimension10) | 否 | 设置icon的高度，宽高比1:1，默认64fp，不支持百分比字符串。 |
| iconColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 设置icon的颜色，默认值：$r('sys.color.ohos\_id\_color\_activated')。 |
| onIconClick | ()=>void | 否 | 用户点击icon回调接口。 |
| onAuthResult | (result: [userAuth.UserAuthResult](js-apis-useriam-userauth.md#userauthresult10))=>void | 是 | 用户认证结果信息回调接口。  应用需要申请ohos.permission.ACCESS\_BIOMETRIC权限，否则应用将仅展示图标，无法正常拉起身份认证控件。 |

## 事件

PhonePC/2in1TabletWearable

不支持通用事件。

## 示例

PhonePC/2in1TabletWearable

```
1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
2. import { userAuth, UserAuthIcon } from '@kit.UserAuthenticationKit';

4. @Entry
5. @Component
6. struct Index {
7. rand = cryptoFramework.createRandom();
8. len: number = 16;
9. randData: Uint8Array = this.rand?.generateRandomSync(this.len)?.data;
10. authParam: userAuth.AuthParam = {
11. challenge: this.randData,
12. authType: [userAuth.UserAuthType.FACE, userAuth.UserAuthType.PIN],
13. authTrustLevel: userAuth.AuthTrustLevel.ATL3
14. };
15. widgetParam: userAuth.WidgetParam = {
16. title: '请进行身份认证'
17. };

19. build() {
20. Row() {
21. Column() {
22. UserAuthIcon({
23. authParam: this.authParam,
24. widgetParam: this.widgetParam,
25. iconHeight: 200,
26. iconColor: Color.Blue,
27. onIconClick: () => {
28. console.info('The user clicked the icon.');
29. },
30. onAuthResult: (result: userAuth.UserAuthResult) => {
31. console.info(`Get user auth result, result = ${result.result}`);
32. }
33. })
34. }
35. }
36. }
37. }
```

调用onAuthResult可能会抛出错误码，错误码详细介绍请参见[通用错误码](errorcode-universal.md)和[用户认证错误码](errorcode-useriam.md)。

**人脸认证图例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/-jtn9h5FTYK-02oPq8dI0A/zh-cn_image_0000002552800884.png?HW-CC-KV=V1&HW-CC-Date=20260428T000750Z&HW-CC-Expire=86400&HW-CC-Sign=85324F011E25638562B67BB9505E9051E61D977C2C44F6A86139121B1ADB3045)

**指纹认证图例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/uftU2x9-QaGxgOefi20jsA/zh-cn_image_0000002583440579.png?HW-CC-KV=V1&HW-CC-Date=20260428T000750Z&HW-CC-Expire=86400&HW-CC-Sign=ED21E6E39416234C5F57BEFBE7FC68A1CA8EDBBCCA519F143BD110BDA6D8170E)
