---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-38
title: 编译报错“The reason and usedScene attributes are mandatory for user_grant permissions”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The reason and usedScene attributes are mandatory for user_grant permissions”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:15+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3a17a49e2ed5a7f1b0ab32392450dca31e00884502f2ed49b71b14bb1396822d
---

**问题现象**

DevEco Studio编译失败，提示“The reason and usedScene attributes are mandatory for user\_grant permissions”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/2o8W9s83SZez8LAuptbE2A/zh-cn_image_0000002194158568.png?HW-CC-KV=V1&HW-CC-Date=20260428T002914Z&HW-CC-Expire=86400&HW-CC-Sign=E332E03994AF4E39C4CEB6C5B35A741D10EF28594BC484F4035BF00BB2569E51 "点击放大")

**问题原因**

从DevEco Studio NEXT Developer Preview 2版本开始，新增规则：APP包中，所有entry和feature hap的module下的requestPermissions权限清单必须指定（可以为空，若非空则name必填；user\_grant权限则必填reason和usedScene字段）。

**解决措施**

进入对应module.json5文件中，补齐requestPermissions字段下的reason和usedScene字段。如以下示例：

```
1. "requestPermissions": [
2. {
3. "name": "ohos.permission.READ_IMAGEVIDEO",
4. "reason": "$string:module_desc",
5. "usedScene": {
6. "abilities": [
7. "EntryAbility"
8. ],
9. "when": "inuse"
10. }
11. }
12. ],
```

[module.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/entry/src/main/module.json5#L56-L67)
