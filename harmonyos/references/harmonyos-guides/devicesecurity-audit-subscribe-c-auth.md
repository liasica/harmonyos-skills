---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-subscribe-c-auth
title: 订阅阻断类事件
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 安全审计 > 多客户端订阅场景（C/C++） > 订阅阻断类事件
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:30+08:00
doc_updated_at: 2026-08-03
content_hash: sha256:118b8839636d3f4ad317104e0aa85e8ac3f8d1787c1c86cc9ea41d8e43763b7a
---

## 场景介绍

从6.0.0(20) 开始，新增提供统一的安全审计数据多客户端订阅/取消订阅、添加/删除过滤条件、阻断接口，应用可以获取设备上的安全审计数据（如下表），并按需进行订阅、过滤与阻断，以支撑审计相关业务。

| 审计事件ID | 说明 |
| --- | --- |
| 0x1C801100 | 文件创建阻断事件。 |
| 0x1C801101 | 文件打开阻断事件。 |
| 0x1C801102 | 文件重命名阻断事件。 |
| 0x1C801103 | 文件删除阻断事件。 |
| 0x1C801104 | 文件设置扩展属性的阻断事件。 |
| 0x1C801105 | 文件删除扩展属性的阻断事件。 |
| 0x1C801106 | 文件读结束阻断事件。  **起始版本：** 26.0.0 |
| 0x1C801400 | 进程执行的阻断事件。  **起始版本：** 26.0.0 |

## 约束与限制

1. 当前能力仅支持PC/2in1设备。
2. 一个进程最大只允许创建2个客户端实例，当前设备最多只允许创建16个客户端实例。
3. 一个客户端实例最大只允许设置256条正过滤的过滤value和256条反过滤的过滤value。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/_aLT6-aUT3qDNCmJHArTkg/zh-cn_image_0000002706834300.png)

**流程说明：**

1. 开发者创建审计阻断类事件（以下统称为事件）订阅客户端实例，需要提供CallBack。
2. 开发者使用步骤1中创建的实例订阅事件，需要提供想要订阅的事件id。
3. 开发者使用步骤1中创建的实例设置事件过滤条件，需要提供事件id和过滤条件信息。
4. 当事件发生时，审计服务先根据事件过滤条件过滤事件，当事件满足过滤条件时，触发回调通知订阅当前事件的客户端。
5. 开发者根据审计数据制定阻断策略。
6. 使用步骤1中创建的实例设置接收到的事件的阻断策略。
7. 当业务结束时，开发者可以使用步骤1中创建的实例解除过滤条件，取消订阅事件。
8. 当业务结束时，开发者可以删除步骤1中创建的实例。

   **说明** 

   支持先设置过滤条件再订阅事件。

   删除实例后，被删除的实例所有的订阅以及过滤条件将被全部解除。

## 接口说明

更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-capi-securityaudit.md#hms_securityaudit_newauthclient)。

| 接口名 | 描述 |
| --- | --- |
| int32\_t HMS\_SecurityAudit\_NewAuthClient(SecurityAudit\_AuthClient\*\* client, SecurityAudit\_Handler handler); | 创建审计阻断类事件管理对象AuthClient，AuthClient提供订阅、解订阅、增加事件过滤、移除事件过滤、阻断功能。超时默认放行。 |
| int32\_t HMS\_SecurityAudit\_NewAuthClientWithConfiguration(SecurityAudit\_AuthClient\*\* outOwnedClient, SecurityAudit\_Handler handler, const SecurityAudit\_AuthClientConfiguration\* configuration); | 创建一个新的阻断类事件客户端，可配置超时默认阻断策略。  **起始版本：** 26.0.0 |
| int32\_t HMS\_SecurityAudit\_DeleteAuthClient(SecurityAudit\_AuthClient\* client); | 删除审计阻断类事件管理对象。 |
| int32\_t HMS\_SecurityAudit\_SubscribeAuthEvent(const SecurityAudit\_AuthClient\* client, const SecurityAudit\_Auth\_Event \*events, uint64\_t count); | 订阅审计阻断类事件。 |
| int32\_t HMS\_SecurityAudit\_UnsubscribeAuthEvent(const SecurityAudit\_AuthClient\* client, const SecurityAudit\_Auth\_Event \*events, uint64\_t count); | 解订阅审计阻断类事件。 |
| int32\_t HMS\_SecurityAudit\_AddAuthEventFilter(const SecurityAudit\_AuthClient\* client, SecurityAudit\_Auth\_Event event, const SecurityAudit\_Filter \*filter); | 添加审计阻断类事件过滤条件。 |
| int32\_t HMS\_SecurityAudit\_RemoveAuthEventFilter(const SecurityAudit\_AuthClient\* client, SecurityAudit\_Auth\_Event event, const SecurityAudit\_Filter \*filter); | 移除审计阻断类事件过滤条件。 |
| int32\_t HMS\_SecurityAudit\_Auth(const SecurityAudit\_AuthClient\* client, const SecurityAudit\_Event \*event, SecurityAudit\_AuthResult authResult); | 设置审计阻断类事件的阻断结果。 |
| int32\_t HMS\_SecurityAudit\_CreateAuthClientConfiguration(SecurityAudit\_AuthClientConfiguration\*\* outOwnedConfiguration); | 创建阻断类事件客户端配置对象。  **起始版本：** 26.0.0 |
| int32\_t HMS\_SecurityAudit\_DestroyAuthClientConfiguration(SecurityAudit\_AuthClientConfiguration\* configuration); | 销毁阻断类事件客户端配置对象。  **起始版本：** 26.0.0 |
| int32\_t HMS\_SecurityAudit\_AuthClientConfiguration\_SetTimeoutAuthResult(SecurityAudit\_AuthClientConfiguration\* configuration, SecurityAudit\_AuthResult authResult); | 设置超时默认授权结果。  **起始版本：** 26.0.0 |

## 开发步骤

**说明** 

* 在开发准备过程中，需要申请权限：ohos.permission.kernel.AUTH\_AUDIT\_EVENT。
* 只允许清单内的企业类应用申请该权限，申请方式请参考：[企业类应用可用权限](permissions-for-enterprise-apps.md)。

1. 在CMakeLists.txt中导入安全审计共享库，并链接该库。

   ```cmake
   find_library(dsm-lib libsecurityaudit_ndk.z.so)
   target_link_libraries(entry PUBLIC libace_napi.z.so ${dsm-lib})
   ```
2. 导入安全审计的头文件。

   ```
   #include <cstdio>
   #include "DeviceSecurityKit/security_audit.h"
   ```
3. 全局范围定义阻断类事件客户端以及携带阻断策略的回调函数。

   ```
   SecurityAudit_AuthClient *client = nullptr;
   void AuthAllowCb(const SecurityAudit_Event *events, uint64_t count)
   {
       if (events == nullptr) {
           printf("events nullptr");
           return;
       }
       if (client == nullptr) {
           printf("client nullptr");
           return;
       }
       for (uint64_t i = 0; i < count; i++) {
           printf("event metadata = %s \n", events[i].metadata);
           printf("event content = %s \n", events[i].content);
           printf("event id = %ld \n", events[i].eventId);
           const SecurityAudit_Event *singleEvent = &events[i];
           HMS_SecurityAudit_Auth(client, singleEvent, SECURITY_AUDIT_AUTH_RESULT_DENY);
       }
   }
   ```
4. （可选）创建并配置阻断类事件客户端配置对象，用于设置超时默认阻断策略（从API版本26.0.0开始支持）。

   如果不配置，默认超时放行。使用[HMS\_SecurityAudit\_NewAuthClientWithConfiguration](../harmonyos-references/devicesecurity-capi-securityaudit.md#hms_securityaudit_newauthclientwithconfiguration)创建客户端时，需配合此配置对象使用。

   ```
   SecurityAudit_AuthClientConfiguration *configuration = nullptr;
   int32_t retConfig = HMS_SecurityAudit_CreateAuthClientConfiguration(&configuration);
   if (retConfig != 0 || configuration == nullptr) {
       printf("create configuration fail");
       return nullptr;
   }
   // 设置超时默认阻断结果为拒绝
   retConfig = HMS_SecurityAudit_AuthClientConfiguration_SetTimeoutAuthResult(configuration,
       SECURITY_AUDIT_AUTH_RESULT_DENY);
   if (retConfig != 0) {
       printf("set timeout auth result fail");
       HMS_SecurityAudit_DestroyAuthClientConfiguration(configuration);
       return nullptr;
   }
   ```
5. 创建审计阻断类事件客户端实例。

   如果已创建配置对象，使用[HMS\_SecurityAudit\_NewAuthClientWithConfiguration](../harmonyos-references/devicesecurity-capi-securityaudit.md#hms_securityaudit_newauthclientwithconfiguration)创建客户端。

   ```
   SecurityAudit_Handler handler = AuthAllowCb;
   client = nullptr;
   HMS_SecurityAudit_NewAuthClientWithConfiguration(&client, handler, configuration);
   if (client == nullptr) {
       printf("client is null");
       HMS_SecurityAudit_DestroyAuthClientConfiguration(configuration);
       return;
   }
   ```

   如果不需自定义超时默认阻断策略，也可使用[HMS\_SecurityAudit\_NewAuthClient](../harmonyos-references/devicesecurity-capi-securityaudit.md#hms_securityaudit_newauthclient)创建客户端（默认超时放行）。

   ```
   SecurityAudit_Handler handler = AuthAllowCb;
   HMS_SecurityAudit_NewAuthClient(&client, handler);
   if (client == nullptr) {
       printf("client is null");
       return;
   }
   ```

   **说明** 

   配置对象在传入[HMS\_SecurityAudit\_NewAuthClientWithConfiguration](../harmonyos-references/devicesecurity-capi-securityaudit.md#hms_securityaudit_newauthclientwithconfiguration)后，客户端会接管该对象的所有权，开发者无需再调用[HMS\_SecurityAudit\_DestroyAuthClientConfiguration](../harmonyos-references/devicesecurity-capi-securityaudit.md#hms_securityaudit_destroyauthclientconfiguration)销毁配置对象。
6. 订阅审计阻断类事件。

   ```
   SecurityAudit_Auth_Event event[1] = {SECURITY_AUDIT_AUTH_EVENT_FILE_CREATE};
   int32_t ret = HMS_SecurityAudit_SubscribeAuthEvent(client, event, 1);
   if (ret != 0) {
       // ...
       printf("subscribe fail");
       return;
   }
   ```
7. 设置审计阻断类事件过滤条件。

   ```
   SecurityAudit_Filter filter = {};
   filter.type = PROCESS_NAME_PREFIX;
   const char* filterStr[1] = {"1"};
   filter.value = filterStr;
   filter.valueCount = 1;
       
   ret = HMS_SecurityAudit_AddAuthEventFilter(client, SECURITY_AUDIT_AUTH_EVENT_FILE_CREATE, &filter);
   if (ret != 0) {
       // ...
       printf("addfilter fail");
       return;
   }
   ```
8. 解除审计阻断类事件订阅。

   ```
   ret = HMS_SecurityAudit_UnsubscribeAuthEvent(client, event, 1);
   if (ret != 0) {
       // ...
       printf("unsubscribe fail");
       return;
   }
   ```
9. 解除审计阻断类事件过滤条件。

   ```
   ret = HMS_SecurityAudit_RemoveAuthEventFilter(client, SECURITY_AUDIT_AUTH_EVENT_FILE_CREATE, &filter);
   if (ret != 0) {
       // ...
       printf("removefilter fail");
       return;
   }
   ```
10. 删除审计阻断类事件客户端实例。

```
ret = HMS_SecurityAudit_DeleteAuthClient(client);
if (ret != 0) {
    printf("deleteclient fail");
}
```
