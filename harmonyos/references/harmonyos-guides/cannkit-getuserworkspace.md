---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getuserworkspace
title: GetUserWorkspace
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > workspace > GetUserWorkspace
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:b9dd8e5cac96e94bad404b1318a66a8c5ef72fd16af54f52eefa155d4ea03d04
---

## 功能说明

获取开发者使用的[workspace](cannkit-getsysworkspaceptr.md)指针。如果使用了[Matmul](cannkit-matmul-usage-description.md)等需要系统workspace的高阶API，kernel侧需要通过[SetSysWorkSpace](cannkit-setsysworkspace.md)设置系统workspace，此时开发者workspace需要通过该接口获取。

## 函数原型

```cpp
__aicore__ inline GM_ADDR GetUserWorkspace(GM_ADDR workspace)
```

## 参数说明

**表1** 接口参数说明

| 参数名称 | 输入/输出 | 描述 |
| --- | --- | --- |
| workspace | 输入 | 传入workspace的指针，包括系统workspace和开发者使用的workspace。 |

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 注意事项

无

## 返回值

开发者使用workspace指针。
