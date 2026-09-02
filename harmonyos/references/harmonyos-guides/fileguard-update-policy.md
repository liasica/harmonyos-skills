---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-update-policy
title: 更新安全管控策略
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 文件分级管控 > 更新安全管控策略
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:02+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:7a3504e9e2aecf91ee4c4b4e8cc0da4d5be62dce0fc56a1b86cbd616a067993c
---

## 场景介绍

Enterprise Data Guard Kit为应用提供下发管控策略的能力，相关策略会被分发到HarmonyOS系统中执行。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/dataguard-fileguard.md)。

| 接口名 | 描述 |
| --- | --- |
| [updatePolicy](../harmonyos-references/dataguard-fileguard.md#updatepolicy)(policy: string, callback: AsyncCallback<void>): void | 使用Callback方式更新安全管控策略。 |
| [updatePolicy](../harmonyos-references/dataguard-fileguard.md#updatepolicy-1)(policy: string): Promise<void> | 使用Promise方式更新安全管控策略。 |
| [getPolicy](../harmonyos-references/dataguard-fileguard.md#getpolicy)(): Promise<string | null> | 使用Promise方式获取当前设备生效的管控策略内容。 |

## 开发步骤

1. 导入模块。

   ```typescript
   import { bundleManager } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { fileGuard } from '@kit.EnterpriseDataGuardKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 初始化[FileGuard](../harmonyos-references/dataguard-fileguard.md#fileguard)对象guard，调用接口[updatePolicy](../harmonyos-references/dataguard-fileguard.md#updatepolicy)，更新安全管控策略。

   * 通过回调函数方式，更新安全管控策略。

     ```typescript
     const TAG: string = 'FileGuard_Policy';
     const DOMAIN: number = 0x0000;

     /**
      * 更新安全管控策略。使用callback异步回调。
      * @param accountId: 用户ID
      */
     async function updatePolicyCallback(accountId: number) {
       let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION |
         bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
       let bundleInfo: bundleManager.BundleInfo = await bundleManager.getBundleInfoForSelf(bundleFlags);
       let appId: string = bundleInfo.signatureInfo.appId;
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       let policy: string = '{' +
         // 网络策略
         '"net_intercept_toggle":1,' +
         '"default_policy":1,' +
         '"boundary":["10.0.0.0-10.255.255.255","172.16.0.0-172.31.255.255"],' +
         '"netsegment_trustlist":["10.0.0.0-10.255.255.255","192.168.0.0-192.168.255.255"],' +
         '"netsegment_blocklist":["172.16.0.0-172.31.255.255"],' +
         '"netsegment_update_type": 0,' +
         '"net_reject_cache_time":30,' +
         // 文件策略
         '"usb_intercept_toggle":1,' +
         '"smb_client_intercept_toggle":1,' +
         '"smb_server_intercept_toggle":1,' +
         '"new_file_audit_toggle":1,' +
         '"kia_variant_toggle":1,' +
         '"audit_filter_toggle":1,' +
         '"print_intercept_toggle":0,' +
         // 蓝牙策略
         '"bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
         '"bluetooth_intercept_time":30,' +
         // 星闪策略
         '"nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
         '"nearlink_intercept_time":30,' +
         // 多用户策略
         `"user_id":${accountId},` +
         // 可信任应用列表
         `"trust_app_list":["${appId}"],` +
         '"kia_file_access_toggle":0,' +
         // 五种自定义标签
         '"Tag1":{' +
         '   "tag":"sensitive",' +
         '   "usb_intercept_toggle":1,' +
         '   "net_intercept_toggle":1,' +
         '   "boundary":["10.0.0.0-10.255.255.255"],' +
         '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
         '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"],' +
         '   "smb_client_intercept_toggle":1,' +
         '   "smb_server_intercept_toggle":1,' +
         '   "print_intercept_toggle":1,' +
         '   "bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
         '   "bluetooth_intercept_time":30,' +
         '   "nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
         '   "nearlink_intercept_time":30' +
         '  },' +
         '"Tag2":{' +
         '   "tag":"confidential",' +
         '   "usb_intercept_toggle":1,' +
         '   "net_intercept_toggle":1,' +
         '   "boundary":["10.0.0.0-10.255.255.255"],' +
         '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
         '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"],' +
         '   "smb_client_intercept_toggle":1,' +
         '   "smb_server_intercept_toggle":1,' +
         '   "print_intercept_toggle":1,' +
         '   "bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
         '   "bluetooth_intercept_time":30,' +
         '   "nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
         '   "nearlink_intercept_time":30' +
         '  },' +
         '"Tag3":{' +
         '   "tag":"public",' +
         '   "usb_intercept_toggle":0,' +
         '   "net_intercept_toggle":0,' +
         '   "boundary":["10.0.0.0-10.255.255.255"],' +
         '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
         '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"],' +
         '   "smb_client_intercept_toggle":1,' +
         '   "smb_server_intercept_toggle":1,' +
         '   "print_intercept_toggle":1,' +
         '   "bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
         '   "bluetooth_intercept_time":30,' +
         '   "nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
         '   "nearlink_intercept_time":30' +
         '  },' +
         '"Tag4":{' +
         '   "tag":"general",' +
         '   "usb_intercept_toggle":1,' +
         '   "net_intercept_toggle":0,' +
         '   "boundary":["10.0.0.0-10.255.255.255"],' +
         '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
         '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"],' +
         '   "smb_client_intercept_toggle":1,' +
         '   "smb_server_intercept_toggle":1,' +
         '   "print_intercept_toggle":1,' +
         '   "bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
         '   "bluetooth_intercept_time":30,' +
         '   "nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
         '   "nearlink_intercept_time":30' +
         '  },' +
         '"Tag5":{' +
         '   "tag":"special",' +
         '   "usb_intercept_toggle":1,' +
         '   "net_intercept_toggle":1,' +
         '   "boundary":["10.0.0.0-10.255.255.255"],' +
         '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
         '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"],' +
         '   "smb_client_intercept_toggle":1,' +
         '   "smb_server_intercept_toggle":1,' +
         '   "print_intercept_toggle":1,' +
         '   "bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
         '   "bluetooth_intercept_time":30,' +
         '   "nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
         '   "nearlink_intercept_time":30' +
         '  }' +
         '}';
       guard.updatePolicy(policy, (err: BusinessError) => {
         if (err) {
           hilog.error(DOMAIN, TAG, `Failed to update policy. Code: ${err.code}, message: ${err.message}.`);
         } else {
           hilog.info(DOMAIN, TAG, `Succeeded in updating policy.`);
         }
       });
     }
     ```
   * 通过Promise方式，更新安全管控策略。

     ```typescript
     const TAG: string = 'FileGuard_Policy';
     const DOMAIN: number = 0x0000;

     // ...
     /**
      * 更新安全管控策略。使用Promise异步回调。
      * @param accountId: 用户ID
      */
     async function updatePolicyPromise(accountId: number) {
       let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION |
         bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
       let bundleInfo: bundleManager.BundleInfo = await bundleManager.getBundleInfoForSelf(bundleFlags);
       let appId: string = bundleInfo.signatureInfo.appId;
       let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
       let policy: string = '{' +
         // 网络策略
         '"net_intercept_toggle":1,' +
         '"default_policy":1,' +
         '"boundary":["10.0.0.0-10.255.255.255","172.16.0.0-172.31.255.255"],' +
         '"netsegment_trustlist":["10.0.0.0-10.255.255.255","192.168.0.0-192.168.255.255"],' +
         '"netsegment_blocklist":["172.16.0.0-172.31.255.255"],' +
         '"netsegment_update_type": 0,' +
         '"net_reject_cache_time":30,' +
         // 文件策略
         '"usb_intercept_toggle":1,' +
         '"smb_client_intercept_toggle":1,' +
         '"smb_server_intercept_toggle":1,' +
         '"new_file_audit_toggle":1,' +
         '"kia_variant_toggle":1,' +
         '"audit_filter_toggle":1,' +
         '"print_intercept_toggle":0,' +
         // 蓝牙策略
         '"bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
         '"bluetooth_intercept_time":30,' +
         // 星闪策略
         '"nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
         '"nearlink_intercept_time":30,' +
         // 多用户策略
         `"user_id":${accountId},` +
         // 可信任应用列表
         `"trust_app_list":["${appId}"],` +
         '"kia_file_access_toggle":0,' +
         // 五种自定义标签
         '"Tag1":{' +
         '   "tag":"sensitive",' +
         '   "usb_intercept_toggle":1,' +
         '   "net_intercept_toggle":1,' +
         '   "boundary":["10.0.0.0-10.255.255.255"],' +
         '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
         '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"],' +
         '   "smb_client_intercept_toggle":1,' +
         '   "smb_server_intercept_toggle":1,' +
         '   "print_intercept_toggle":1,' +
         '   "bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
         '   "bluetooth_intercept_time":30,' +
         '   "nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
         '   "nearlink_intercept_time":30' +
         '  },' +
         '"Tag2":{' +
         '   "tag":"confidential",' +
         '   "usb_intercept_toggle":1,' +
         '   "net_intercept_toggle":1,' +
         '   "boundary":["10.0.0.0-10.255.255.255"],' +
         '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
         '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"],' +
         '   "smb_client_intercept_toggle":1,' +
         '   "smb_server_intercept_toggle":1,' +
         '   "print_intercept_toggle":1,' +
         '   "bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
         '   "bluetooth_intercept_time":30,' +
         '   "nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
         '   "nearlink_intercept_time":30' +
         '  },' +
         '"Tag3":{' +
         '   "tag":"public",' +
         '   "usb_intercept_toggle":0,' +
         '   "net_intercept_toggle":0,' +
         '   "boundary":["10.0.0.0-10.255.255.255"],' +
         '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
         '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"],' +
         '   "smb_client_intercept_toggle":1,' +
         '   "smb_server_intercept_toggle":1,' +
         '   "print_intercept_toggle":1,' +
         '   "bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
         '   "bluetooth_intercept_time":30,' +
         '   "nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
         '   "nearlink_intercept_time":30' +
         '  },' +
         '"Tag4":{' +
         '   "tag":"general",' +
         '   "usb_intercept_toggle":1,' +
         '   "net_intercept_toggle":0,' +
         '   "boundary":["10.0.0.0-10.255.255.255"],' +
         '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
         '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"],' +
         '   "smb_client_intercept_toggle":1,' +
         '   "smb_server_intercept_toggle":1,' +
         '   "print_intercept_toggle":1,' +
         '   "bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
         '   "bluetooth_intercept_time":30,' +
         '   "nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
         '   "nearlink_intercept_time":30' +
         '  },' +
         '"Tag5":{' +
         '   "tag":"special",' +
         '   "usb_intercept_toggle":1,' +
         '   "net_intercept_toggle":1,' +
         '   "boundary":["10.0.0.0-10.255.255.255"],' +
         '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
         '   "netsegment_blocklist":["172.16.0.0-172.31.255.255"],' +
         '   "smb_client_intercept_toggle":1,' +
         '   "smb_server_intercept_toggle":1,' +
         '   "print_intercept_toggle":1,' +
         '   "bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
         '   "bluetooth_intercept_time":30,' +
         '   "nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
         '   "nearlink_intercept_time":30' +
         '  }' +
         '}';
       guard.updatePolicy(policy).then(() => {
         hilog.info(DOMAIN, TAG, `Succeeded in updating policy.`);
       }).catch((err: BusinessError) => {
         hilog.error(DOMAIN, TAG, `Failed to update policy. Code: ${err.code}, message: ${err.message}.`);
       });
     }
     ```
3. 初始化[FileGuard](../harmonyos-references/dataguard-fileguard.md#fileguard)对象guard，调用接口[getPolicy](../harmonyos-references/dataguard-fileguard.md#getpolicy)，获取当前设备生效的管控策略内容。

   ```typescript
   const TAG: string = 'FileGuard_Policy';
   const DOMAIN: number = 0x0000;

   // ...
   /**
    * 获取当前设备生效的管控策略内容
    */
   function getPolicyPromise() {
     let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
     guard.getPolicy().then((policy: string | null) => {
       if (policy === null) {
         hilog.info(DOMAIN, TAG, `The obtained policy is null.`);
         return;
       }
       hilog.info(DOMAIN, TAG, `Succeeded in getting policy. policy length: ${policy.length}`);
       // 返回字符串较长，分次打印
       let len: number = 2000; // 每次打印 2000 字符
       let totalLen: number = policy.length;
       for (let i: number = 0; i < totalLen; i += len) {
         let end: number = Math.min(i + len, totalLen);
         let item: string = policy.substring(i, end);
         hilog.info(DOMAIN, TAG, `policy: ${item}`);
       }
     }).catch((err: BusinessError) => {
       hilog.error(DOMAIN, TAG, `Failed to get policy. Code: ${err.code}, message: ${err.message}.`);
     });
   }
   ```
