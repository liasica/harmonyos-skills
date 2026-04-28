---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/change-description-510-release
title: 变更说明
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > DevEco Studio > 变更说明
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:17+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:08f94335bfef741d8d34ca5f668338fd791a28c5e4dfe17429553d1bcfdc12be
---

## DevEco Studio中fastjson版本升级

DevEco Studio使用的fastjson版本升级至fastjson2。

**变更影响**

若基于DevEco Studio开发插件时，使用了DevEco Studio携带的fastjson版本，在DevEco Studio 5.1.0.828中使用该插件将报错，提示找不到fastjson lib库。

**适配指导**

请将该插件适配fastjson2，或在插件中自行打包fastjson。

## 堆栈格式变化

升级到DevEco Studio 5.1.0.828及以上版本，堆栈路径前增加模块的packageName，用于确认堆栈对应的模块。

```
1. at anonymous (entry/src/main/ets/pages/Index.ets:21:19)     // 变更前
2. at anonymous entry (entry/src/main/ets/pages/Index.ets:21:19)   // 变更后
```

**变更影响**

DevEco Studio已做兼容，不影响通过DevEco Studio查看和解析日志，但可能影响用户自定义的工具。

**适配指导**

用户根据新格式适配修改。
