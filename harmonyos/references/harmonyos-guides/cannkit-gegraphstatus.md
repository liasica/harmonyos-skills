---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-gegraphstatus
title: ge::graphStatus
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > ge::graphStatus
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a462cc752b54e521cd629778b46348f5d811550bce85d51cd18020ed8c270b88
---

graphStatus类型即uint32\_t类型，其不同的状态说明如下。

| 状态 | 值 | 说明 |
| --- | --- | --- |
| ge::GRAPH\_SUCCESS | 0 | 对应函数执行成功。 |
| ge::GRAPH\_FAILED | 0xFFFFFFFF | 对应函数执行失败。 |
| ge::GRAPH\_PARAM\_INVALID | 50331649 | 对应函数执行失败，执行时存在参数无法通过校验的情况。 |
| ge::GRAPH\_NOT\_CHANGED | 1343242304 | 不符合常量折叠的条件时的错误码。 |
| ge::GRAPH\_NODE\_WITHOUT\_CONST\_INPUT | 50331648 | 检测到网络中的某个算子的输入没有const数据的场景。 |
