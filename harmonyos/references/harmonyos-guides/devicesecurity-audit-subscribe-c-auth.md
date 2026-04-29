---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-subscribe-c-auth
title: 订阅阻断类事件
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 安全审计 > 多客户端订阅场景（C/C++） > 订阅阻断类事件
category: harmonyos-guides
scraped_at: 2026-04-29T13:31:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4ad343a16a4162f160379e7b694ff2cd6502f473fa67a1c369c7edca0fe4688d
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

## 约束与限制

1. 当前能力仅支持2in1设备。
2. 一个进程最大只允许创建2个客户端实例，当前设备最多只允许创建16个客户端实例。
3. 一个客户端实例最大只允许设置256条正过滤的过滤value和256条反过滤的过滤value。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/0SEcwGzGSf6O1moN-oNc8w/zh-cn_image_0000002558764898.png?HW-CC-KV=V1&HW-CC-Date=20260429T053137Z&HW-CC-Expire=86400&HW-CC-Sign=2A550DC1741F9276C1B75F46881A8A8E28A1694D59DED4A135D978BF07373921)

**流程说明：**

1. 开发者创建审计阻断类事件（以下统称为事件）订阅客户端实例，需要提供CallBack。
2. 开发者使用步骤1中创建的实例订阅事件，需要提供想要订阅的事件id。
3. 开发者使用步骤1中创建的实例设置事件过滤条件，需要提供事件id和过滤条件信息。
4. 当事件发生时，审计服务先根据事件过滤条件过滤事件，当事件满足过滤条件时，触发回调通知订阅当前事件的客户端。
5. 开发者根据审计数据制定阻断策略。
6. 使用步骤1中创建的实例设置接收到的事件的阻断策略。
7. 当业务结束时，开发者可以使用步骤1中创建的实例解除过滤条件，取消订阅事件。
8. 当业务结束时，开发者可以删除步骤1中创建的实例。

   说明

   支持先设置过滤条件再订阅事件。

   删除实例后，被删除的实例所有的订阅以及过滤条件将被全部解除。

## 接口说明

更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-capi-securityaudit.md#hms_securityaudit_newauthclient)。

| 接口名 | 描述 |
| --- | --- |
| int32\_t HMS\_SecurityAudit\_NewAuthClient(SecurityAudit\_AuthClient\*\* client, SecurityAudit\_Handler handler); | 创建审计阻断类事件管理对象AuthClient，AuthClient提供订阅、解订阅、增加事件过滤、移除事件过滤、阻断功能 |
| int32\_t HMS\_SecurityAudit\_DeleteAuthClient(SecurityAudit\_AuthClient\* client); | 删除审计阻断类事件管理对象 |
| int32\_t HMS\_SecurityAudit\_SubscribeAuthEvent(const SecurityAudit\_AuthClient\* client, const SecurityAudit\_Auth\_Event \*events, uint64\_t count); | 订阅审计阻断类事件 |
| int32\_t HMS\_SecurityAudit\_UnsubscribeAuthEvent(const SecurityAudit\_AuthClient\* client, const SecurityAudit\_Auth\_Event \*events, uint64\_t count); | 解订阅审计阻断类事件 |
| int32\_t HMS\_SecurityAudit\_AddAuthEventFilter(const SecurityAudit\_AuthClient\* client, SecurityAudit\_Auth\_Event event, const SecurityAudit\_Filter \*filter); | 添加审计阻断类事件过滤条件 |
| int32\_t HMS\_SecurityAudit\_RemoveAuthEventFilter(const SecurityAudit\_AuthClient\* client, SecurityAudit\_Auth\_Event event, const SecurityAudit\_Filter \*filter); | 移除审计阻断类事件过滤条件 |
| int32\_t HMS\_SecurityAudit\_Auth(const SecurityAudit\_AuthClient\* client, const SecurityAudit\_Event \*event, SecurityAudit\_AuthResult authResult); | 设置审计阻断类事件的阻断结果 |

## 开发步骤

说明

* 在开发准备过程中，需要申请权限：ohos.permission.kernel.AUTH\_AUDIT\_EVENT。
* 只允许清单内的企业类应用申请该权限，申请方式请参考：[申请使用企业类应用可用权限](permissions-for-enterprise-apps.md)。

1. 在CMakeLists.txt中导入安全审计共享库，并链接该库。

   ```
   1. find_library(dsm-lib libsecurityaudit_ndk.z.so)
   2. target_link_libraries(entry PUBLIC libace_napi.z.so ${dsm-lib})
   ```
2. 导入安全审计的头文件。

   ```
   1. #include <DeviceSecurityKit/security_audit.h>
   2. #include <cstdio>
   ```
3. 全局范围定义阻断类事件客户端以及携带阻断策略的回调函数。

   ```
   1. SecurityAudit_AuthClient *client = nullptr;
   2. void AuthAllowCb(const SecurityAudit_Event *events, uint64_t count)
   3. {
   4. if (events == nullptr) {
   5. printf("events nullptr");
   6. return;
   7. }
   8. if (client == nullptr) {
   9. printf("client nullptr");
   10. return;
   11. }
   12. for (uint64_t i = 0; i < count; i++) {
   13. printf("event metadata = %s \n", events[i].metadata);
   14. printf("event content = %s \n", events[i].content);
   15. printf("event id = %ld \n", events[i].eventId);
   16. const SecurityAudit_Event *singleEvent = &events[i];
   17. HMS_SecurityAudit_Auth(client, singleEvent, SECURITY_AUDIT_AUTH_RESULT_DENY);
   18. }
   19. }
   ```
4. 创建审计阻断类事件客户端实例。

   ```
   1. SecurityAudit_Handler handler = AuthAllowCb;
   2. HMS_SecurityAudit_NewAuthClient(&client, handler);
   3. if (client == nullptr) {
   4. printf("client is null");
   5. return;
   6. }
   ```
5. 订阅审计阻断类事件。

   ```
   1. SecurityAudit_Auth_Event event[1] = {};
   2. event[0] = SECURITY_AUDIT_AUTH_EVENT_FILE_CREATE;
   3. int ret = HMS_SecurityAudit_SubscribeAuthEvent(client, event, 1);
   4. if (ret != 0) {
   5. printf("subscribe fail");
   6. return;
   7. }
   ```
6. 设置审计阻断类事件过滤条件。

   ```
   1. SecurityAudit_Filter filter = {};
   2. filter.type = PROCESS_NAME_PREFIX;
   3. const char* filterStr[1] = {};
   4. filterStr[0] = "1";
   5. filter.value = filterStr;
   6. filter.valueCount = 1;
   7. ret = HMS_SecurityAudit_AddAuthEventFilter(client, SECURITY_AUDIT_AUTH_EVENT_FILE_CREATE, &filter);
   8. if (ret != 0) {
   9. printf("addfilter fail");
   10. return;
   11. }
   ```
7. 解除审计阻断类事件订阅。

   ```
   1. ret = HMS_SecurityAudit_UnsubscribeAuthEvent(client, event, 1);
   2. if (ret != 0) {
   3. printf("unsubscribe fail");
   4. return;
   5. }
   ```
8. 解除审计阻断类事件过滤条件。

   ```
   1. ret = HMS_SecurityAudit_RemoveAuthEventFilter(client, SECURITY_AUDIT_AUTH_EVENT_FILE_CREATE, &filter);
   2. if (ret != 0) {
   3. printf("removefilter fail");
   4. return;
   5. }
   ```
9. 删除审计阻断类事件客户端实例。

   ```
   1. ret = HMS_SecurityAudit_DeleteAuthClient(client);
   2. if (ret != 0) {
   3. printf("deleteclient fail");
   4. return;
   5. }
   ```
