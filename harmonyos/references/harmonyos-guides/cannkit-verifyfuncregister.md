---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-verifyfuncregister
title: VerifyFuncRegister
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > VerifyFuncRegister
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:625dea7816438defadcd44319e1cc05589de8f9ce397836d8979a685d2522be5
---

## 函数功能

VerifyFuncRegister构造函数和析构函数。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. VerifyFuncRegister(const std::string &operator_type, const VerifyFunc &verify_func);
2. VerifyFuncRegister(const char_t *const operator_type, const VerifyFunc &verify_func);
3. ~VerifyFuncRegister() = default;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| operator\_type | 输入 | 算子类型。 |
| verify\_func | 输入 | 算子verify函数。 |

## 返回值

VerifyFuncRegister构造函数返回VerifyFuncRegister类型的对象。

## 约束说明

算子verifyFunc函数注册接口，此接口被其他头文件引用，一般不用由算子开发者直接调用。
