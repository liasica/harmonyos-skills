---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-policy-push
title: 配置空间互传单双通策略
breadcrumb: 指南 > 应用服务 > Enterprise Space Kit（企业数字空间服务） > 空间互传 > 配置空间互传单双通策略
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2e661e4808d4a55bfed6f2bdee247382ef567563b112f144cbedd3be41b6e04b
---

## 场景介绍

Enterprise Space Kit支持HEM配置空间互传单双通策略。空间初始化时，通过调用接口配置空间互传应用文件外发策略。具体而言，单通表示只允许个人空间向企业空间发送文件，不允许企业空间向个人空间发送文件；双通表示允许个人空间和企业空间互相发送文件。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprisespace-spacedatatransfer.md#policypush)。

| 接口名 | 描述 |
| --- | --- |
| [policyPush](../harmonyos-references/enterprisespace-spacedatatransfer.md#policypush)(policyContext: string): void | 配置空间互传单双通策略。 |

## 开发步骤

1. 导入Enterprise Space Kit模块。

   ```
   1. import { fileTransfer } from '@kit.EnterpriseSpaceKit';
   ```
2. 调用[policyPush](../harmonyos-references/enterprisespace-spacedatatransfer.md#policypush)接口，配置空间互传单双通策略，并且查看打印信息。

   ```
   1. const policyContext: string =
   2. '{\"config\":{\"inEnable\":\"1\",\"incoming_check\":{\"data_list\":[{\"allow\":\"VirusCheck.result == 0\",\"approval\":\"\",\"check_point\":\"VirusCheck\",\"check_point_name\":\"VirusCheck_in\",\"is_enable\":\"true\",\"forbidden\":\"VirusCheck.result == 1\",\"order\":\"0\"}]},\"outEnable\":\"0\",\"outgoing_check\":{\"data_list\":[{\"allow\":\"SecurityCheck.Result == 3 or SecurityCheck.Result == 4 or SecurityCheck.Result == 6 or SecurityCheck.Result == 7\",\"approval\":\"SecurityCheck.Result == 10\",\"check_point\":\"SecurityCheck\",\"check_point_name\":\"SecurityCheck_out\",\"is_enable\":\"true\",\"forbidden\":\"SecurityCheck.Result == 0 or SecurityCheck.Result == 1 or SecurityCheck.Result == 12 or SecurityCheck.Result == 2 or SecurityCheck.Result == 5 or SecurityCheck.Result == 8 or SecurityCheck.Result == 9 or SecurityCheck.Result == 11\",\"order\":\"0\"}]},\"checkpoint_config\":{\"data_list\":[{\"check_point_name\":\"SecurityCheck\",\"bundle_name\":\"com.example.enterprisespacekit_samplecode_clientdemo_arkts\",\"ability_name\":\"TestScanAbility\",\"func_code\":\"2\",\"type\":\"2\"},{\"check_point_name\":\"VirusCheck\",\"bundle_name\":\"com.example.enterprisespacekit_samplecode_clientdemo_arkts\",\"ability_name\":\"TestScanAbility\",\"func_code\":\"3\",\"type\":\"1\"}]},\"approvalpoint_config\":{\"data_list\":[{\"bundle_name\":\"com.example.enterprisespacekit_samplecode_clientdemo_arkts\",\"ability_name\":\"TestApprovalAbility\"}]}}}';
   3. try {
   4. fileTransfer.policyPush(policyContext);
   5. console.info(`Succeeded in pushing policy`);
   6. } catch (err) {
   7. console.error(`Failed to push policy. Code: ${err.code}, message: ${err.message}`);
   8. }
   ```
