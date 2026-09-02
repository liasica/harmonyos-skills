---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-multipath_reco
title: NetworkBoost_MultiPathRecommendation
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 结构体 > NetworkBoost_MultiPathRecommendation
category: harmonyos-references
scraped_at: 2026-09-02T15:01:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a16e83668d79c228a2c9fe38ebe9815add8eb8a84e5d6efb1f1a410c9c696765
---

## 概述

多网推荐信息，用于注册多网推荐变化事件回调后，系统多网推荐状态发生变化的事件通知。

**起始版本：** 6.0.2(22)

**相关模块：** [NetworkBoost](network-boost-c-overview.md)

**所在头文件：** [network\_boost\_handover.h](network-boost-c-files-handover.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [NetworkBoost\_MultiPathAction](network-boost-c-overview.md#networkboost_multipathaction) [action](network-boost-c-struct-multipath_reco.md#action) | 多网推荐动作。 |

## 结构体成员变量说明

## action

```c
NetworkBoost_MultiPathAction NetworkBoost_MultiPathRecommendation::action
```

**描述**

表明多网推荐动作。
