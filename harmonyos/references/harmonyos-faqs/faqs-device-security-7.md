---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-device-security-7
title: 涉诈剧本检测接口多次调用成功后再次调用出现报错
breadcrumb: FAQ > 系统开发 > 安全 > 设备安全服务（Device Security） > 涉诈剧本检测接口多次调用成功后再次调用出现报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:7023abfdefdc71e6dde2190080137481ac7a2705171fd586bf075e49a7c020aa
---

## 问题现象

使用涉诈剧本检测功能时，当多次调用接口成功后，再次调用接口时会出现报错。

报错信息如下：

```txt
code:1012500001 message:Internal error.
```

错误信息日志：

```txt
=====================Backtrace========================
#00 pc 00000000006ec4cc /system/lib64/platformsdk/libark_jsruntime.so
#01 pc 00000000006eca40 /system/lib64/platformsdk/libark_jsruntime.so
#02 pc 00000000003244b0 /system/lib64/platformsdk/libark_jsruntime.so
#03 pc 00000000001bc734 /system/lib64/platformsdk/libark_jsruntime.so
#04 pc 00000000001bc1c4 /system/lib64/platformsdk/libark_jsruntime.so
#05 pc 000000000024ec2c /system/lib64/platformsdk/libark_jsruntime.so
#06 pc 00000000005cb424 /system/lib64/platformsdk/libark_jsruntime.so
#07 pc 00000000005a21e0 /system/lib64/platformsdk/libark_jsruntime.so
#08 pc 0000000000057480 /system/lib64/platformsdk/libace_napi.z.so
#09 pc 00000000000067cc /system/lib64/module/hms/security/libbusinessriskintelligentdetection_napi.z.so
#10 pc 00000000000660c0 /system/lib64/platformsdk/libace_napi.z.so
#11 pc 000000000007ee58 /system/lib64/platformsdk/libruntime.z.so
```

## 背景知识

[涉诈剧本检测](../harmonyos-guides/devicesecurity-fraudriskdetection.md)：金融支付类应用在用户转账、支付前，通过调用Device Security kit的detectFraudRisk接口，检测用户是否受到欺诈威胁。该接口返回一个风险分，以及涉诈行为的线索，例如，接收到涉诈引导信息、设备有被操控风险等，应用可以根据风险分及线索，进行有效提示或拦截。

## 问题定位

1. 根据错误码[1012500001](../harmonyos-references/errorcode-devicesecurity-brid.md#section1012500001-内部异常)信息，分析错误原因可能为接口执行流程中调用系统其它接口出现异常。
2. 检查nonce值是否符合参数要求：nonce值必须为24至80字节之间。
3. 更换设备重新执行检测，确认是否由于触发接口使用限制导致报错。
4. 检查接口的[约束与限制](../harmonyos-guides/devicesecurity-fraudriskdetection.md#约束与限制)，每个应用在每个设备上每天最多可以调用10次，超出限制则会报错。

## 分析结论

涉诈剧本检测接口存在使用约束与限制，每个应用在每个设备上每天最多可以调用10次。若调用接口达到限制次数后，再次调用接口会出现该报错。

## 修改建议

根据文档说明，每个应用在每个设备上每天最多可以调用10次此接口，目前最大调用次数无法自定义修改。

若应用处于调测阶段，可以通过以下方案来规避每日最大调用次数的限制：

* 通过以下hdc命令清理缓存重置接口调用次数：hdc shell bm clean -d -n com.huawei.hmos.brid。
* 在手机设置中修改手机系统的时间，规避接口每日使用次数限制。
