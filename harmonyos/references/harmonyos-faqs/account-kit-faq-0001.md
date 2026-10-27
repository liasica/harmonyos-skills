---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/account-kit-faq-0001
title: 华为账号登录与授权常见问题
breadcrumb: FAQ > 应用服务开发 > 华为账号服务（Account Kit） > 常见问题 > 华为账号登录与授权常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:39+08:00
doc_updated_at: 2026-10-22
content_hash: sha256:a07b9037ba4bd65e29bbdeeacad66be7aecb246fd0421fa6923fde68bafaa7e9
---

**Q：华为账号登录报错，常见错误码是1001500001，主要报错信息如下：**

```txt
Failed to auth, errorCode=1001500001, errorMsg=Failed to check the fingerprint of the app bundle.Fingerprint verification error.
```

**A**：问题一：错误码1001500001的含义为应用指纹证书验证失败。

可能原因：应用的指纹证书未配置或配置错误（HarmonyOS 6.0后不再要求配置公钥指纹）。

检查步骤：

1. 登录[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console/#/home/)查看[配置公钥指纹](../app/agc-help-cert-fingerprint-0000002278002933.md)：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/P5Ero_AcTmGs8-5cTAFgCw/zh-cn_image_0000002794282667.png "点击放大")
2. 使用DevEco Studio打开项目工程，打开File->Project Structure->Project->Signing Configs界面，不能勾选"Automatically generate signature"进行自动签名，需要手动配置签名。可以按照开发准备里面的说明配置：[配置签名信息](../harmonyos-guides/application-dev-overview.md#配置签名信息)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/q2vfeBfpSEWhKDf5OCa5JQ/zh-cn_image_0000002794282669.png)
3. 查看应用签名证书指纹，安装应用后执行：
   * Windows系统

     ```shell
     hdc shell bm dump -n 包名 | findstr appId
     ```
   * Mac系统

     ```shell
     hdc shell bm dump -n 包名 | grep appId
     ```
   * 将"appId"中包名下划线后的字符串拷贝到新文件中（文件名可自行定义，例如SHA.txt）再执行下面的命令行即可得到公钥指纹。检查应用签名证书指纹与HarmonyOS 开发者中心是否一致。

     ```shell
     certutil -hashfile F:\\SHA.txt SHA256
     ```

4. Client ID配置：

   检查module type为entry的模块下module.json5中的client\_id是否配置错误，请参考[配置Client ID](../harmonyos-guides/account-client-id.md)。

   注意：此处client\_id的获取路径为：HarmonyOS 开发者中心中应用管理->基本信息->OAuth 2.0客户端ID（凭据)->Client ID。

   在工程中entry模块的module.json5文件中，新增metadata，配置name为client\_id，value为Client ID的值。

   错误示例1：client\_id在工程里面没有配置。

   错误示例2：client\_id的value写到string里面（比如："value": "$string:clientId"）也会导致授权报错。

   错误示例3：client\_id的value里面配置成APP ID，而不是Client ID的值。

   错误示例4：module.json5里面配置了多个client\_id。

**Q：华为账号一键登录获取手机号码，常见错误码是1001500003，主要报错信息如下：**

```txt
Failed to login, errorCode=1001500003, errorMessage is The scopes or permissions are not supported.
```

A：问题二：错误码1001500003的原因是当前登录华为账号或者设备不支持应用请求的数据。

可能原因：

* 在获取实名信息、实名信息校验、人脸核身等场景下，用户登录的账号为中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）注册的华为账号，但使用了港澳台通行证进行实名。
* 在实名信息校验、人脸核身等场景下，PC/2in1设备或前置摄像功能异常的设备不支持传入verifyRealName和verifyFace 2个scope进行授权。
* 元服务开发过程中，调AuthorizationWithHuaweiIDRequest接口时传了profile这个scope，且supportAtomicService参数未设置为true。
* 元服务开发过程中，调AuthorizationWithHuaweiIDRequest接口时传了phone这个scope。
* 在实名信息校验、人脸核身场景，登录的华为账号是儿童账号。
* Wearable、TV设备申请获取不支持的scope。

解决方案：

* 提示用户当前华为账号不支持，引导用户更换使用大陆身份证实名的华为账号。
* 在实名信息校验、人脸核身等场景下，使用其他前置摄像功能正常的设备授权verifyRealName和verifyFace 2个 scope。
* 元服务开发过程中，调[AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest)接口时传了profile这个scope，并将supportAtomicService参数设置为true。
* 元服务不能直接调用该接口获取手机号，可参考场景化控件[快速验证手机号Button](../harmonyos-guides/scenario-fusion-button-getphonenumber.md)获取。

**Q：错误码1001502014，主要报错信息如下：**

```txt
 Failed to auth. Code: 1001502014, message: The app does not have the required scopes or permissions.no scope permission.
```

A：问题三：错误码1001502014的含义为应用未申请scopes或permissions权限。

可能原因和解决方法：[AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest)中scopes配置与已申请的账号权限不匹配，具体参照[开发前提](../harmonyos-guides/account-get-phonenumber.md#开发前提)。详细排查步骤参考[1001502014 应用未申请scopes或permissions权限的可能原因和解决方法](../harmonyos-guides/account-faq-2.md)。

**Q：通过"/oauth2/v6/quickLogin/getPhoneNumber"获取手机号码报错，常见错误码是60180007，主要报错信息如下：**

```txt
scope not contain quickLoginMobilePhone.
```

A：问题四：错误码60180007的含义是通过Authorization Code无法获取到华为账号一键登录手机号。

可能原因：

* 应用未申请quickLoginMobilePhone权限。
* 调用服务器接口/oauth2/v6/quickLogin/getPhoneNumber的入参code，不是通过调用华为账号的一键登录组件获取到的。

解决方案：

* [申请账号权限](../harmonyos-guides/account-config-permissions.md#section144591410155511)，确认应用满足华为账号一键权限申请条件并确认申请已通过。
* 确认/oauth2/v6/quickLogin/getPhoneNumber需要的入参code是通过华为账号一键登录接口获取的。请参考[客户端开发](../harmonyos-guides/account-phone-unionid-login.md#客户端开发)。

**Q：通过"/oauth2/agent/v1/access-token"[获取用户级Token](../FASP-by-Template-develop-References/get-token-user-0000001622722589.md)报错：**

```txt
sub_error=20001, error_description=missing required parameter: client_id, error=1102.
```

通过"oauth2/v3/token"[获取用户级凭证](../harmonyos-references/account-api-obtain-user-token.md)报错：

```txt
sub_error=20154，error_description=client_id not match，error=1101.
```

A：问题五：错误码1101、1102、1103的含义是使用oauth2/v3/token接口时入参错误。

可能原因：

* 调用服务器接口oauth2/v3/token的入参client\_id为空或不正确。
* 调用服务器接口oauth2/v3/token的入参grant\_type不符合选值要求（"authorization\_code"、"refresh\_token"、"client\_credentials"）。
* 其他参数无效或错误。解决方案：对照[开放接口调用凭证](../harmonyos-references/account-api-obtain-token.md)排查对应接口的入参。

**Q：使用华为账号服务报错，错误码1001502003：**

```txt
1001502003 Invalid input parameter value.clientId or appId is invalid.
```

```txt
1001502003 Invalid input parameter value.
```

A：问题六：错误码1001502003的含义为输入参数值无效。

可能原因及解决方案：

* client\_id未配置或配置错误，参考上文Client ID配置当中的排查方法。
* client\_id配置value值错误，比如空格等异常字符。
* 传入的匿名手机号不正确，或是未调用授权API（[AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest)）获取匿名手机号。
* 接口传参异常，如调用授权API（[AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest)）时scope和permission都未传。
* 检查应用的签名文件是否配置正确，且需要进行[手动签名](../harmonyos-guides/ide-signing.md#section297715173233)，并使用调试证书而非发布证书。
* 申请的Profile文件不包含APP ID，需要重新申请Profile文件。

**Q：后端一键登录通过token换取手机号调用报错，报错信息如下：**

```txt
GOpen.User.getInfo service is not found
```

**A**：问题七：后端调用接口通过token换取手机号时报"GOpen.User.getInfo service is not found"。

可能原因：调用接口的URL中存在大小写错误，且URL中包含多余的回车符。

解决方案：

* 检查调用接口的URL，将接口名称中错误的小写字母修改为大写。
* 去除URL中多余的回车符。
* 建议使用新接口开发，参考[通过Code换取用户信息（一键登录）](../harmonyos-references/account-api-get-user-info-quicklogin-by-code.md)。

**Q：HarmonyOS 开发者中心和应用的证书指纹已经确认一致还是报错？**

**A**：在HarmonyOS 开发者中心上面，添加公钥指纹（HarmonyOS API 9及以上）后，指纹有一定时间的缓存，不会立刻生效，建议配置完成后等半小时再尝试。检查手机是否有修改系统时间。

**Q：点击《华为账号用户认证协议》无反应？**

**A**：需排查[《华为账号用户认证协议》](https://privacy.consumer.huawei.com/legal/id/authentication-terms.htm?code=CN&language=zh-CN)的链接，目前链接已更改，需在之前的链接后增加&language=zh-CN。

**Q：本地使用调试证书可以登录成功，但替换正式证书打包APP后登录失败？**

**A**：发布证书签名的包是不能在本地进行调试安装。利用发布证书及对应的profile所打包的APP，只能用于上架发布，正式包可以通过[邀请测试](../app/agc-help-invite-test-0000002270829393.md)方式验证。

**Q：新增HarmonyOS应用，client\_id和client\_secret和原来的不一样，传入的Authorization Code怎么区分是HarmonyOS还是其他平台？**

**A**：服务端处理Authorization Code时，必须使用对应应用的Client ID/Secret组合换取Access Token。此时：

1. 若使用HarmonyOS应用的Client ID/Secret成功换取Token→判定为HarmonyOS来源；
2. 若使用其他平台应用的Client ID/Secret成功换取Token→判定为其他平台来源。

**Q：华为账号一键登录获取公钥指纹报错：Failed to login with LoginWithHuaweiIDButton. errorCode=1001500001, errorMsg is Failed to check the fingerprint of the app bundle.Incomplete response information from gateway.？**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/jpOA0aN0TuGCaMiof49fAA/zh-cn_image_0000002765095280.png "点击放大")

**A**：首先排查是否企业开发者，个人开发者暂不支持一键登录，再根据当前知识解决方案思路依次排查。

**Q：TV设备在调用executeRequest时报错1001500003根据文档排查无法解决问题？**

**A**：华为账号一键登录支持Phone、Tablet、PC/2in1设备。并且从5.1.1(19)版本开始，新增支持TV设备。需排查TV设备软件版本是否高于5.1.1(19)版本。

**Q：为什么华为账号一键登录，获取匿名手机号，有些手机可以，有些手机报错误码:1001500001？**

**A**：华为账号一键登录在API>=20以后，不需要配置公钥指纹，而低于API20版本的手机，依旧需要配置公钥指纹。参考[配置签名和指纹](../harmonyos-guides/account-sign-fingerprints.md)。

**Q：利用手动签名和调试证书成功登录，如果接下来要发布软件如何发布？软件如何打包？其次发布的时候是不是要正式签名？或者说是正式证书？**

**A**：正式上架需要使用发布证书构建出.app包，打包发布可以参照：[发布应用](../harmonyos-guides/ide-publish-app.md)。

**Q：为什么使用华为账号登录，使用调试证书或者发布证书，只有当前开发者可以正常登录，其他人报错误码:1001500001？**

**A**：如您的应用当前集成的华为相关服务（如华为账号服务）依赖公钥指纹，您需要在应用调试或上架前将公钥指纹配置到HarmonyOS 开发者中心。调试和发布使用的签名证书不同，因此调试和发布前请分别基于使用的证书配置相应的公钥指纹。发布应用前，需在HarmonyOS 开发者中心中将调试应用的指纹更新为发布证书指纹。具体操作请参见[配置公钥指纹](../app/agc-help-cert-fingerprint-0000002278002933.md)。

**Q：调试证书华为账号一键登录正常，提交上架的版本使用华为账号一键登录失败？**

**A**：调试证书指纹已添加到应用下，发布证书未配置，请登录[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console/#/home/)检查。

**Q：使用账号登录时，服务端返回ResponseCode：403如何排查？**

**A**：客户端能拉起账号登录流程但服务端返回403，属于服务端鉴权失败，建议按以下顺序排查：

1. 确认真机/模拟器里安装包的bundleName/package与HarmonyOS 开发者中心注册应用一致，当前调试或发布证书的SHA-256指纹已配置到同一个应用下。换过签名证书后，要重新下载配置文件并重新打包。
2. 后端使用的Client ID、Client Secret必须与当前应用属于同一个HarmonyOS 开发者中心项目/应用，避免混用Web客户端、其他包名应用或旧项目的Client信息。
3. 如果请求了手机号、匿名手机号、riskLevel等scope/permission，先确认对应权限已申请并通过。未申请所需scope/permission会对应错误码1001502014，不支持的scope/permission会对应错误码1001500003。
4. 后端换取用户信息时要传客户端刚获取到的authorizationCode，该code只能用一次且有效期较短；重复使用、过期，或和错误Client ID搭配，都可能导致服务端拒绝。
5. 建议把后端调用接口的完整响应体、错误码以及requestId/traceId一并记录，方便区分是签名指纹校验、scope权限，还是服务端凭据不匹配。

Q：登录授权模拟器时，若提示华为账号需要实名制认证，请在账号中心检查账号状态。若状态显示“已实名”，请核对相关信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/HIlmZsnnQ96z80pIp_SVAw/zh-cn_image_0000002764937408.png)

**A**：华为账号实名分两种，一个是账号实名认证，即上图展示的状态，还有一个是开发者实名认证。这两种实名认证方式是不一样的，模拟器的登录授权是需要开发者实名认证，请根据[实名认证指导](../start/itrna-0000001076878172.md)进行处理。开发者实名认证后的结果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/UD8ZuKVcQymUcBBivn-KzA/zh-cn_image_0000002794455925.png)

**Q：使用浏览器登录华为账号后，如果账号已实名认证但未出现授权的“允许”按钮，界面也未跳转或提示，该如何处理？**

**A**：该问题由浏览器兼容性问题导致。模拟器登录授权已在Chrome、IE11和Safari浏览器中进行了充分验证，建议将默认浏览器设置为其中一种。

1. 设置或更改默认浏览器。
   * Windows平台：以Windows 10为例，打开“控制面板 > 程序 > 默认程序 > 设置默认程序”，更改或设置默认浏览器。
   * macOS平台：以macOS 15为例，打开系统设置，选择“桌面与程序坞”，再选择“默认网页浏览器”，更改或设置默认浏览器。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/cTTCQYfzR2Kd5P8eGl92Sg/zh-cn_image_0000002764939608.png "点击放大")

     使用Safari浏览器时，点击Safari 浏览器 > 偏好设置>隐私/高级，取消“防止跨站跟踪”和“阻止所有Cookie”设置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/Sf7iOKVpSiGjh79ndrFQ4g/zh-cn_image_0000002764940340.png "点击放大")

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/rrDjiTOFQfa8q0Gl8hynlQ/zh-cn_image_0000002794379077.png "点击放大")
2. 在DevEco Studio界面，点击Cancel按钮，然后重新登录授权。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/Z4b_GIaST2ScfbYX2d5j2w/zh-cn_image_0000002764941134.png "点击放大")

**Q：获取匿名手机号只能与openid同时使用。在获取匿名手机号时如何同时获取头像和昵称？**

**A**：获取华为账号绑定的匿名手机号是通过quickLoginAnonymousPhone，该scope只能与openid同时使用，而获取头像昵称是通过profile值获取，quickLoginAnonymousPhone和profile同时使用会报错："1001500003不支持该scopes或permissions"。

若需要同时获取匿名化手机号和头像昵称，建议分2个方法调用，不会影响返回结果。示例代码如下：

```ts
import { util } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { authentication } from '@kit.AccountKit';

@Entry
@Component
struct Page {
  getPhotoName() {
    // 创建授权请求，并设置参数
    const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
    // 获取头像昵称需要传如下scope
    authRequest.scopes = ['profile'];
    // 若开发者需要进行服务端开发，则需传如下permission获取authorizationCode
    authRequest.permissions = ['serviceauthcode'];
    // 用户是否需要登录授权，该值为true且用户未登录或未授权时，会拉起用户登录或授权页面
    authRequest.forceAuthorization = true;
    // 用于防跨站点请求伪造
    authRequest.state = util.generateRandomUUID();
    // 执行授权请求
    try {

      const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext() as Context);
      controller.executeRequest(authRequest).then((data) => {
        const authorizationWithHuaweiIDResponse = data as authentication.AuthorizationWithHuaweiIDResponse;
        const state = authorizationWithHuaweiIDResponse.state;
        if (state != undefined && authRequest.state != state) {
          hilog.error(0x0000, 'testTag', `Failed to authorize. The state is different, response state: ${state}`);
          return;
        }
        hilog.info(0x0000, 'testTag', 'Succeeded in authentication.');

        const authorizationWithHuaweiIDCredential = authorizationWithHuaweiIDResponse.data!;
        const avatarUri = authorizationWithHuaweiIDCredential.avatarUri; // 用户头像链接
        const nickName = authorizationWithHuaweiIDCredential.nickName; // 用户昵称
        const unionID = authorizationWithHuaweiIDCredential.unionID;
        const openID = authorizationWithHuaweiIDCredential.openID;
        const authorizationCode = authorizationWithHuaweiIDCredential.authorizationCode;

        hilog.info(0x0000, 'testTag',
          `获取到nickName、avatarUri、UnionID、OpenID、authorizationCode:${nickName}、${avatarUri}、${unionID}、${openID}、${authorizationCode}`);
      }).catch((error: BusinessError) => {
        hilog.error(0x0000, 'testTag',
          `Failed to get huaweiIdState, errorCode=${error.code}, errorMsg=${error.message}`);
      });
    } catch (error) {
      hilog.error(0x0000, 'testTag', `Failed to get huaweiIdState, errorCode=${error.code}, errorMsg=${error.message}`);
    }
  }

  getQuickLoginAnonymousPhone() {
    const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
    authRequest.scopes = ['quickLoginAnonymousPhone'];

    // 用于防跨站点请求伪造
    authRequest.state = util.generateRandomUUID();
    // 一键登录场景该参数只能设置为false
    authRequest.forceAuthorization = false;
    const controller = new authentication.AuthenticationController();
    try {
      controller.executeRequest(authRequest).then((response: authentication.AuthorizationWithHuaweiIDResponse) => {
        // 获取到UnionID、OpenID、匿名手机号
        const unionID = response.data?.unionID;
        const openID = response.data?.openID;
        const authCode = response.data?.authorizationCode;
        hilog.info(0x0000, 'testTag', `获取到UnionID、OpenID、匿名手机号:${unionID}、${openID}、${authCode}`);
        const anonymousPhone = response.data?.extraInfo?.quickLoginAnonymousPhone as string;
        if (anonymousPhone) {
          hilog.info(0x0000, 'testTag', 'Succeeded in authentication getQuickLoginAnonymousPhone.');
          return;
        }
        hilog.info(0x0000, 'testTag', 'Succeeded in authentication. AnonymousPhone is empty.');
        // 未获取到匿名手机号需要跳转到应用自定义的登录页面
      })
        .catch((error: BusinessError) => {
          hilog.error(0x0000, 'testTag',
            `Failed to get huaweiIdState, errorCode=${error.code}, errorMsg=${error.message}`);

        });
    } catch (error) {
      hilog.error(0x0000, 'testTag', `Failed to get huaweiIdState, errorCode=${error.code}, errorMsg=${error.message}`);
    }
  }

  build() {
    Column() {
      // 应用使用华为账号一键登录功能之前，需要完成quickLoginMobilePhone（华为账号一键登录）的scope权限申请，详情参见配置scope权限:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-config-permissions
      Button('获取头像、昵称')
        .onClick(() => {
          this.getPhotoName();
        })
        .margin({ bottom: 10 });
      Button('获取匿名手机号')
        .onClick(() => {
          this.getQuickLoginAnonymousPhone();
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

**Q：使用华为账号一键登录功能时，是以华为账号的UnionID/OpenID还是以手机号作为用户的主要标识？**

**A**：推荐使用华为账号的UnionID/OpenID作为用户的主要标识，并将应用与华为账号绑定的手机号关联。华为账号的UnionID/OpenID不会发生变化，即使换绑手机号，仍然可以使用华为账号登录原来绑定的应用账号。

**Q：Access Token和Refresh Token的有效时长是多久？**

**A**：Access Token的有效时长是1个小时，Refresh Token的有效时长是180天。

**Q：向用户申请获取昵称/头像授权是在华为账号一键登录前还是登录后？**

**A**：同意获取昵称/头像授权包含在[《华为账号用户认证协议》](https://privacy.consumer.huawei.com/legal/id/authentication-terms.htm?code=CN&language=zh-CN)内，用户同意[《华为账号用户认证协议》](https://privacy.consumer.huawei.com/legal/id/authentication-terms.htm?code=CN&language=zh-CN)后才能进入华为账号一键登录流程。

**Q：华为账号登录流程中服务端需要存什么凭据，使用什么字段作为唯一标识？**

**A**：华为账号登录会向服务端返回UnionID 、OpenID 、authorization Code 、ID token，建议都存储，其中UnionID、OpenID是唯一标识。参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。

* 开发者账号下管理了多个应用时，针对同一个华为账号，不同的应用返回的OpenID值不同，但返回的UnionID相同，所以建议使用OpenID来作为唯一ID。
* 如果开发者账号下管理了多个应用，并且这些应用需要共享同一个华为账号的用户信息，可以使用UnionID作为用户标识。

**Q：HarmonyOS 4.3及以下版本授权登录使用的是OpenID作为唯一标识，HarmonyOS 5及以上版本设备下获取到的OpenID和之前的不一样，该如何处理？**

**A**：处理方式如下：

1. HarmonyOS 4.3及以下版本和HarmonyOS 5及以上版本获取的OpenID确实不相同，首先用户OpenID的生成规则是：由用户账号和应用ID加密生成的；在这个基础上HarmonyOS 4.3及以下版本和HarmonyOS 5及以上版本的应用ID是不相同的，所以获取的OpenID是不同的。
2. 推荐使用UnionID，其生成规则是：由用户账号和应用开发者账号签名而成，如果开发者账号下管理了多个应用，并且这些应用需要共享同一个华为账号的用户信息，可以使用UnionID作为用户标识。

**Q：HarmonyOS 4.3及以下版本和HarmonyOS 5及以上版本获取的OpenID不相同，UnionID相同，如何通过用户OpenID获取UnionID？**

**A**：可调用REST API接口[通过OpenID获取UnionID](../harmonyos-references/account-api-get-unionid.md)。

**Q：用户更换绑定华为账号的手机号码，华为账号一键登录返回的UnionID是否会变？**

**A**：用户更换绑定华为账号的手机号码，华为账号一键登录返回的UnionID不会变，可以作为用户的唯一标识。

**Q：应用在主体迁移后，UnionID是否会改变？**

**A**：UnionID是同一个开发者账号下的用户唯一标识，当应用转移到另外一个账号主体后，UnionID值也会变化。参考[UnionID介绍](../HMSCore-Guides/unionid-introduction-0000001125697651.md)。

**Q：华为一键登录和账号登录获取的UnionID是否是同一个值？**

**A**：华为一键登录和账号登录获取的UnionID是同一个值。

**Q：同一应用在其他平台端和HarmonyOS端分别接入华为账号登录，如何识别是同一个身份？分别使用什么接入方案？**

**A**：接入方案和身份识别方式如下：

1. 其他平台端应用接入华为帐号服务，参考[其他平台帐号服务开发指南](../HMSCore-Guides/android-introduction-0000001098842325.md)。HarmonyOS 5及以上版本应用接入华为账号服务，参考[Account Kit开发指南](../harmonyos-guides/account-introduction.md)。
2. 使用UnionID作为跨平台同一身份的标识。UnionID由用户账号和应用开发者账号签名生成，同一开发者账号下的应用无论在哪个平台，同一个华为账号返回的UnionID相同。参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。

**Q：应用接入第三方账号登录时是否必须接入华为账号登录？国家网络身份认证App授权获取凭证登录是否属于第三方账号登录，以及接入该方式是否必须提供华为账号登录选项？**

**A**：为了帮助用户省去多次输入不同应用账号登录的繁琐过程，我们为HarmonyOS应用和元服务提供了使用华为账号快捷登录的能力。提交至华为应用市场的HarmonyOS应用和元服务，需要遵循如下规范：

如果您的应用支持用户使用第三方账号登录，则该应用需提供华为账号登录选项。用户可通过华为账号快捷地登录您的应用，并获得华为账号的安全配置。

其中登录场景全部满足以下三点时，华为账号登录为**必选**：

1. 接入了第三方账号登录方式。
2. 应用和第三方账号服务商不属于同一企业或关联企业。
3. 不涉及使用公民真实身份信息来鉴定用户身份。其中公民真实身份信息包括中国大陆居民身份证、中华人民共和国外国人永久居留身份证、护照、台湾居民来往大陆通行证、台湾居民居住证、港澳居民来往内地通行证、港澳居民居住证、香港身份证、澳门身份证、军人身份证。

国家网络身份认证、社保卡等基于公民真实身份信息鉴定用户身份的认证方式不属于第三方账号登录，接入此类方式时不强制提供华为账号登录选项。
