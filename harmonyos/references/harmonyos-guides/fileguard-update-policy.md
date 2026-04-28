---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-update-policy
title: 更新安全管控策略
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 文件分级管控 > 更新安全管控策略
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:64031f9d9df48bca9b3ef11f353dc2fc621eee4c2aa18e874aff48486e348042
---

## 场景介绍

Enterprise Data Guard Kit为应用提供下发管控策略的能力，相关策略会被分发到HarmonyOS系统中执行。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/dataguard-fileguard.md)。

| 接口名 | 描述 |
| --- | --- |
| [updatePolicy](../harmonyos-references/dataguard-fileguard.md#updatepolicy)(policy: string, callback: AsyncCallback<void>): void | 使用Callback方式更新安全管控策略。 |
| [updatePolicy](../harmonyos-references/dataguard-fileguard.md#updatepolicy-1)(policy: string): Promise<void> | 使用Promise方式更新安全管控策略。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { fileGuard } from '@kit.EnterpriseDataGuardKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 初始化[FileGuard](../harmonyos-references/dataguard-fileguard.md#fileguard)对象guard，调用接口updatePolicy，更新安全管控策略。

   * 通过回调函数方式，更新安全管控策略。

     ```
     1. function updatePolicyCallback() {
     2. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
     3. let policy: string = '{' +
     4. '"net_intercept_toggle":1,' +
     5. '"default_policy":1,' +
     6. '"net_reject_cache_time":30,' +
     7. '"boundary":["10.0.0.0-10.255.255.255","172.16.0.0-172.31.255.255"],' +
     8. '"netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
     9. '"netsegment_blocklist":["172.16.0.0-172.31.255.255","192.168.0.0-192.168.255.255"],' +
     10. '"netsegment_update_type": 0,' +
     11. '"usb_intercept_toggle":1,' +
     12. '"smb_client_intercept_toggle":1,' +
     13. '"smb_server_intercept_toggle":1,' +
     14. '"new_file_audit_toggle":1,' +
     15. '"kia_variant_toggle":1,' +
     16. '"audit_filter_toggle":1,' +
     17. '"bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
     18. '"bluetooth_intercept_time":30,' +
     19. '"nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
     20. '"nearlink_intercept_time":30,' +
     21. '"trust_app_list":["ohos.app.hap.myapplication_BPch04bPYBrkJX8RAsmiGDbHFaG+BYvhkg4TK4fHQzJOL4VnoBCZU3boBBXGVEB+M/j0X2nnd7KVeyWuEORVxI2g="],' +
     22. '"Tag1":{' +
     23. '   "tag":"sensitive",' +
     24. '   "usb_intercept_toggle":1,' +
     25. '   "net_intercept_toggle":1,' +
     26. '   "boundary":["10.0.0.0-10.255.255.255"],' +
     27. '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
     28. '   "netsegment_blocklist":["192.168.0.0-192.168.255.255"]' +
     29. '  }' +
     30. '}';
     31. guard.updatePolicy(policy, (err: BusinessError) => {
     32. if (err) {
     33. console.error(`Failed to update policy. Code: ${err.code}, message: ${err.message}.`);
     34. } else {
     35. console.info(`Succeeded in updating policy.`);
     36. }
     37. });
     38. }
     ```
   * 通过Promise方式，更新安全管控策略。

     ```
     1. function updatePolicyPromise() {
     2. let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
     3. let policy: string = '{' +
     4. '"net_intercept_toggle":1,' +
     5. '"default_policy":1,' +
     6. '"net_reject_cache_time":30,' +
     7. '"boundary":["10.0.0.0-10.255.255.255","172.16.0.0-172.31.255.255"],' +
     8. '"netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
     9. '"netsegment_blocklist":["172.16.0.0-172.31.255.255","192.168.0.0-192.168.255.255"],' +
     10. '"netsegment_update_type": 0,' +
     11. '"usb_intercept_toggle":1,' +
     12. '"smb_client_intercept_toggle":1,' +
     13. '"smb_server_intercept_toggle":1,' +
     14. '"new_file_audit_toggle":1,' +
     15. '"kia_variant_toggle":1,' +
     16. '"audit_filter_toggle":1,' +
     17. '"bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
     18. '"bluetooth_intercept_time":30,' +
     19. '"nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
     20. '"nearlink_intercept_time":30,' +
     21. '"trust_app_list":["ohos.app.hap.myapplication_BPch04bPYBrkJX8RAsmiGDbHFaG+BYvhkg4TK4fHQzJOL4VnoBCZU3boBBXGVEB+M/j0X2nnd7KVeyWuEORVxI2g="],' +
     22. '"Tag1":{' +
     23. '   "tag":"sensitive",' +
     24. '   "usb_intercept_toggle":1,' +
     25. '   "net_intercept_toggle":1,' +
     26. '   "boundary":["10.0.0.0-10.255.255.255"],' +
     27. '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
     28. '   "netsegment_blocklist":["192.168.0.0-192.168.255.255"]' +
     29. '  }' +
     30. '}';
     31. guard.updatePolicy(policy).then(() => {
     32. console.info(`Succeeded in updating policy.`);
     33. }).catch((err: BusinessError) => {
     34. console.error(`Failed to update policy. Code: ${err.code}, message: ${err.message}.`);
     35. });
     36. }
     ```
