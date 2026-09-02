---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-user-authentication-5
title: 应用指纹登录开关已经打开，但仍显示未打开
breadcrumb: FAQ > 系统开发 > 安全 > 用户身份认证（User Authentication） > 应用指纹登录开关已经打开，但仍显示未打开
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:215344bed7916c7424614bf48256e456cbb4bc494c4302c97ccba325eeee1ff7
---

## 问题现象

APP内开启指纹登录功能，验证指纹和登录密码之后返回到设置界面，设置界面显示为关闭状态，但功能实际已启用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/nYGua9gyS9COnPxUue3v3Q/zh-cn_image_0000002628769788.png "点击放大")

## 背景知识

* [userAuth.getUserAuthInstance](../harmonyos-references/js-apis-useriam-userauth.md#userauthgetuserauthinstance10)：获取UserAuthInstance对象，用于执行用户身份认证，并支持使用统一用户身份认证控件。
* [UserAuthInstance](../harmonyos-references/js-apis-useriam-userauth.md#userauthinstance10)：用于执行用户身份认证，并支持使用统一用户身份认证控件。

## 问题定位

1. 根据用户提供的日志，查找UserAuthInstance关键字。

   ```txt
   CQ2401/应用包名/USER_AUTH_NAPI[GetUserAuthInstanceV10/user_auth_entry.cpp:555]: start  
   CQ2401/应用包名/USER_AUTH_NAPI[InitUserAuthInstanceV10Constructor/user_auth_entry.cpp:337]: start  
   CQ2401/应用包名/USER_AUTH_NAPI[CheckNapiType/user_auth_napi_helper.cpp:253]: check valuetype fail  
   CQ2401/应用包名/USER_AUTH_NAPI[CheckNapiType/user_auth_napi_helper.cpp:253]: check valuetype fail  
   CQ2401/应用包名/USER_AUTH_NAPI[InitChallenge/user_auth_instance_v10.cpp:148]: challenge size:6  
   CQ2401/应用包名/USER_AUTH_NAPI[InitAuthType/user_auth_instance_v10.cpp:180]: get authType:4  
   CQ2401/应用包名/USER_AUTH_NAPI[InitAuthType/user_auth_instance_v10.cpp:194]: authType size：1
   CQ2401/应用包名/USER_AUTH_NAPI[CheckNapiType/user_auth_api_helper.cpp:253]: check valuetype fail  
   CQ2401/应用包名/USER_AUTH_NAPI[CheckTrustlevel/user_auth_instance_v10.cpp:218]: authTrustLevel:40000  
   CQ2401/应用包名/USER_AUTH_NAPI[CheckNapiType/user_auth_api_helper.cpp:253]: check valuetype fail  
   CQ2401/应用包名/USER_AUTH_NAPI[ProcessWindowMode/user_auth_instance_v10.cpp:467]: widgetParam title:请验证已有指纹, navBtnText:, winMode:3  
   CQ2401/应用包名/USER_AUTH_NAPI[ProcessContext/user_auth_instance_v10.cpp:411]: process uiContext  
   CQ2401/应用包名/USER_AUTH_NAPI[Init/user_auth_instance_v10.cpp:530]: Init SUCCESS 
   CQ2401/应用包名/USER_AUTH_NAPI:[GetUserAuthInstanceV10/user_auth_entry.cpp:582]: GetUserAuthInstanceV10 SUCCESS
   CQ2401/应用包名/USER_AUTH_NAPI[Start/user_auth_instance_v10.cpp:301]: start
   ```
2. 分析日志，得到如下报错。

   ```txt
   CQ2401/应用包名/USER_AUTH_NAPI[CheckNapiType/user_auth_api_helper.cpp:253]: check valuetype fail  
   CQ2401/应用包名/USER_AUTH_NAPI[ProcessWindowMode/user_auth_instance_v10.cpp:467]: widgetParam title:请验证已有指纹, navBtnText:, winMode:3  
   C014A0/composer_host/HDM[hdmcore]: ReportVsycEvent(Dev0vsyncThread) -72224385793723552_failed
   ```

## 分析结论

1. 日志中提到CheckNapiType失败，是因为应用在调用UserAuthInstance的方法时，传入的参数类型不符合预期，这是应用与底层系统之间的状态同步问题导致的。例如，应用在获取UserAuthInstance后，没有正确地处理认证结果，导致状态更新不及时或状态不正确，从而使得指纹登录开关的显示状态与实际状态不一致。
2. 日志中提到ReportVsyncEvent失败，可能与硬件或驱动有关。硬件或驱动问题会导致指纹传感器无法正确工作，从而使得指纹登录功能的开关状态显示不正确。经过验证，其他应用指纹功能能正常实现，说明不是指纹传感器的问题。

## 修改建议

按照指纹识别具体实现内容，检测并修复应用同步系统指纹功能状态的相关逻辑。

指纹识别具体实现：

1. 指纹识别依赖系统的指纹设置，先在手机系统中设置指纹。
2. 在module.json5文件中增加权限ohos.permission.ACCESS\_BIOMETRIC。

   ```json
   {
     "name": "ohos.permission.ACCESS_BIOMETRIC"
   },
   ```
3. 实现认证逻辑。核心代码如下：

   ```ts
   import userAuth from '@ohos.userIAM.userAuth';

   @Entry
   @Component
   struct Index {
     private challenge: Uint8Array = new Uint8Array([49, 49, 49, 49, 49, 49]);
     private authType: userAuth.UserAuthType = userAuth.UserAuthType.FINGERPRINT;
     private authTrustLevel: userAuth.AuthTrustLevel = userAuth.AuthTrustLevel.ATL1;
     private authInstance: userAuth.UserAuthInstance | undefined = undefined;

     createInstance() {
       this.authInstance = undefined;
       const authParam: userAuth.AuthParam = {
         challenge: this.challenge,
         authType: [this.authType],
         authTrustLevel: this.authTrustLevel,
       };
       const widgetParam: userAuth.WidgetParam = {
         title: '请输入密码',
       };
       // AuthInstance对象，用于执行用户认证
       this.authInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
       this.authInstance.on('result', {
         onResult(result) {
           console.info(`userAuth 验证成功: ${JSON.stringify(result)}`);
         }
       });
       // 开始认证
       this.authInstance.start();
     }

     build() {
       Row() {
         Column() {
           Button('指纹识别')
             .width(100)
             .onClick(() => {
               this.createInstance();
             });
         }
         .width('100%');
       }
       .height('100%');
     }
   }
   ```
