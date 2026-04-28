---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-date
title: 使用JSVM-API接口进行Date相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口进行Date相关开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:18+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:0aa53ec2ecb61f1c9e7a44a9b6df8407a4f693bc2f3f74b2d1e472ab2e1b60ce
---

## 简介

JSVM-API中date相关接口用于处理JavaScript Date对象，并在JSVM模块和JavaScript代码之间进行日期数据的转换和处理。这对于在JSVM模块中处理时间和日期相关逻辑非常有用。

## 基本概念

在JSVM-API中，JavaScript Date对象的数据表示从UTC时间1970年1月1日0时0分0秒起至现在的总毫秒数。

JavaScript Date对象在JavaScript中用于表示和操作日期和时间。它们允许开发者创建表示特定时刻的日期对象，执行日期和时间计算（如添加或减去时间间隔），以及格式化日期为字符串以供显示。

在JSVM-API中，通过提供与Date对象交互的函数，JSVM模块能够更紧密地与JavaScript环境集成，执行复杂的日期和时间相关操作。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_CreateDate | 创建一个表示给定毫秒数的Date对象。 |
| OH\_JSVM\_GetDateValue | 获取给定JavaScript Date的时间值的Double基础类型值。 |
| OH\_JSVM\_IsDate | 判断一个JavaScript对象是否为Date类型对象。 |

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅展示接口对应C++相关代码。

### OH\_JSVM\_CreateDate

创建一个表示给定毫秒数的Date对象。

cpp部分代码：

```
1. #include <time.h>
2. // OH_JSVM_CreateDate的样例方法
3. static JSVM_Value CreateDate(JSVM_Env env, JSVM_CallbackInfo info) {
4. // 通过c接口获取Unix纪元以来经过的秒数，并转化为毫秒数为单位
5. double value = static_cast<double>(static_cast<uint64_t>(time(NULL)) * 1000ULL);
6. // 调用OH_JSVM_CreateDate接口将double值转换成表示日期时间的JavaScript值返回出去
7. JSVM_Value returnValue = nullptr;

9. JSVM_CALL(OH_JSVM_CreateDate(env, value, &returnValue));

11. bool isDate = false;
12. JSVM_CALL(OH_JSVM_IsDate(env, returnValue, &isDate));
13. if (!isDate) {
14. OH_LOG_ERROR(LOG_APP, "JSVM IsDate fail");
15. return returnValue;
16. }

18. value = 0;
19. JSVM_CALL(OH_JSVM_GetDateValue(env, returnValue, &value));

21. uint64_t time = static_cast<uint64_t>(value) / 1000;
22. char *date = ctime(reinterpret_cast<time_t *>(&time));
23. OH_LOG_INFO(LOG_APP, "JSVM CreateDate success:%{public}s", date);

25. return returnValue;
26. }

28. // CreateDate注册回调
29. static JSVM_CallbackStruct param[] = {
30. {.data = nullptr, .callback = CreateDate},
31. };
32. static JSVM_CallbackStruct *method = param;
33. // CreateDate方法别名，供JS调用
34. static JSVM_PropertyDescriptor descriptor[] = {
35. {"createDate", nullptr, method, nullptr, nullptr, nullptr, JSVM_DEFAULT},
36. };
37. // 样例测试js
38. const char *srcCallNative = R"JS(createDate())JS";
```

预期结果：

```
1. JSVM CreateDate success:Mon Jul 7 10:42:34 2025
```

### OH\_JSVM\_GetDateValue

获取给定JavaScript Date的时间值的Double基础类型值。

cpp部分代码：

```
1. #include <ctime>
2. // OH_JSVM_GetDateValue的样例方法
3. static JSVM_Value GetDateValue(JSVM_Env env, JSVM_CallbackInfo info) {
4. size_t argc = 1;
5. JSVM_Value args[1] = {nullptr};
6. JSVM_CALL(OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr));
7. // 获取传入的Unix Time Stamp时间
8. double value = 0;
9. JSVM_CALL(OH_JSVM_GetDateValue(env, args[0], &value));

11. // 将获取到的Unix Time Stamp时间转化为日期字符串打印
12. uint64_t time = static_cast<uint64_t>(value) / 1000;
13. char *date = ctime(reinterpret_cast<time_t *>(&time));
14. OH_LOG_INFO(LOG_APP, "JSVM GetDateValue success:%{public}s", date);

16. JSVM_Value returnValue = nullptr;
17. JSVM_CALL(OH_JSVM_CreateDouble(env, value, &returnValue));
18. return returnValue;
19. }

21. // CreateDate注册回调
22. static JSVM_CallbackStruct param[] = {
23. {.data = nullptr, .callback = GetDateValue},
24. };
25. static JSVM_CallbackStruct *method = param;
26. // CreateDate方法别名，供JS调用
27. static JSVM_PropertyDescriptor descriptor[] = {
28. {"getDateValue", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
29. };
30. // 样例测试js
31. const char *srcCallNative = R"JS(getDateValue(new Date(Date.now())))JS";
```

预期结果：

```
1. JSVM GetDateValue success:Mon Jul 7 10:47:08 2025
```

### OH\_JSVM\_IsDate

判断一个JavaScript对象是否为Date类型对象。

cpp部分代码：

```
1. // OH_JSVM_IsDate的样例方法
2. static JSVM_Value IsDate(JSVM_Env env, JSVM_CallbackInfo info) {
3. size_t argc = 1;
4. JSVM_Value args[1] = {nullptr};
5. JSVM_CALL(OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr));
6. bool isDate = false;
7. JSVM_CALL(OH_JSVM_IsDate(env, args[0], &isDate));
8. OH_LOG_INFO(LOG_APP, "JSVM IsDate success:%{public}d", isDate);

10. JSVM_Value result = nullptr;
11. JSVM_CALL(OH_JSVM_GetBoolean(env, isDate, &result));
12. return result;
13. }
14. // CreateDate注册回调
15. static JSVM_CallbackStruct param[] = {
16. {.data = nullptr, .callback = IsDate},
17. };
18. static JSVM_CallbackStruct *method = param;
19. // CreateDate方法别名，供JS调用
20. static JSVM_PropertyDescriptor descriptor[] = {
21. {"isDate", nullptr, method, nullptr, nullptr, nullptr, JSVM_DEFAULT},
22. };
23. // 样例测试js
24. const char *srcCallNative = R"JS(isDate(new Date(Date.now())))JS";
```

预期结果：

```
1. JSVM IsDate success:1
```
