---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-224
title: 编译构建常见报错hvigor ERROR问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译构建常见报错hvigor ERROR问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b699d31738ba49b542702c93d62b6741f9c7bb09b52748f84017c0cd218af4ff
---

## 问题现象

* **场景一：**

  hvigor ERROR: Debug Failure. False expression: Script kind should match provided ScriptKind:3 and sourceFile.scriptKind: 8.
* **场景二：**

  hvigor ERROR: Debug Failure. False expression: Script kind should match provided ScriptKind:8 and sourceFile.scriptKind: 3, !entry: false.
* **场景三：**

  hvigor ERROR：The @ohos/hvigor-ohos-plugin version () is not within the expected range 2.xx(2.xx >= 2.4.0)

## 解决方案

* **场景一：**

  此报错说明编译器在处理文件时，文件扩展名与编译器内部标记的脚本类型不一致，常见于IDE或构建工具的缓存问题，尝试清除缓存后重新构建。
  1. Build -> Clean Project。
  2. 手动删除oh\_modules文件夹后执行ohpm install。
  3. 重新构建项目。

  若清除缓存后还是报错。在hvigor-config.json5中设置"debugging":{stacktrace:true}，查看详细堆栈报错。
* **场景二：**

  修改hvigor-config.json5和oh-package.json5中的modelVersion字段，使其与当前工具版本匹配。例如："modelVersion": "6.0.2"。
* **场景三：**
  1. 更新最新的DevEco Studio，新版本hvigor依赖内置，不需要添加依赖。
  2. 若更新DevEco Studio还报错，进行如下配置：
     + 在hvigor-config.json5中配置："modelVersion": "6.0.2"。
     + build-profile.json5文件里的compatibleSdkVersion配置需要平台版本和API版本相匹配，如："compatibleSdkVersion": "6.0.2(22)"。
