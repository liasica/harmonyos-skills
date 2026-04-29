---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-check-tool
title: 扫描工具
breadcrumb: 指南 > 系统 > 调测调优 > 调试命令 > 扫描工具
category: harmonyos-guides
scraped_at: 2026-04-29T13:34:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f600fe70761da2aeae9f9e79e731eeaf3c5b3733f08a351248166348055a5e2a
---

## 简介

扫描工具可用于分析检测应用安装包，根据不同的参数设定，扫描指定路径的HAP、HSP、App包内容并输出检测结果报告，为开发者优化包结构或排查问题提供数据支撑。目前扫描工具支持以下几种分析统计：

* 扫描重复文件。
* 扫描超出指定大小的文件。
* 统计分析各类型文件的总大小和占比。

工具扫描结果默认以JSON和HTML两种文件格式输出。

扫描工具app\_check\_tool.jar需要从SDK路径下的toolchains目录中获取。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/eM3ufJQeQ16B8TzDmx5LTg/zh-cn_image_0000002558765022.png?HW-CC-KV=V1&HW-CC-Date=20260429T053417Z&HW-CC-Expire=86400&HW-CC-Sign=3E83BE081831AAD9EEDD478FB2EE82E480746CD90EA66596458466BAF84C1507)

## 约束与限制

* 扫描工具需运行在Java8及其以上环境。
* 扫描工具运行所在的目录需要有读写权限。

## 扫描重复文件示例

**命令示例：**

```
1. java -jar app_check_tool.jar --input ./test.app --out-path ./test --stat-duplicate true
```

**表1 扫描重复文件指令参数说明**

| 指令 | 是否必选项 | 描述 |
| --- | --- | --- |
| --input | 是 | 指定传入的HAP、HSP、App包文件路径。 |
| --out-path | 是 | 指定结果输出文件夹目录。 |
| --stat-duplicate | 否 | 是否扫描重复文件。默认为false。  true：启用。  false：不启用。 |

**JSON统计结果：**

```
1. [{
2. "taskType":1,
3. "taskDesc":"find the duplicated files",
4. "param":"--stat-duplicate",
5. "startTime":"2023-11-17 14:48:01:265",
6. "stopTime":"2023-11-17 14:48:01:434",
7. "result":[{
8. "md5":"975c41f5727b416b1ffefa5bb0f073b2",
9. "size":1108880,
10. "files":[
11. "/application-entry-default.hap/libs/armeabi-v7a/example.so",
12. "/entry-default.hap/libs/armeabi-v7a/example.so"
13. ]
14. }]
15. }]
```

**表2 扫描重复文件字段信息**

| 字段 | 类型 | 描述 |
| --- | --- | --- |
| taskType | int | 取值为1，表示扫描重复文件。 |
| taskDesc | String | 任务的详细描述。 |
| param | String | 扫描程序传入参数。 |
| startTime | String | 任务开始时间。 |
| stopTime | String | 任务结束时间。 |
| result | Struct | 重复文件统计结果字段信息，具体内容参考表3。 |

**表3 重复文件统计结果字段信息**

| 字段 | 类型 | 描述 |
| --- | --- | --- |
| md5 | String | 相同文件的MD5值。 |
| size | int | 相同文件的大小。单位为Byte。 |
| files | Vector<String> | 相同文件名的对应路径。 |

## 扫描超出指定大小的文件示例

**命令示例：**

```
1. java -jar app_check_tool.jar --input ./test.app --out-path ./test --stat-file-size 4
```

**表4 扫描超出指定大小的文件的指令参数说明**

| 指令 | 是否必选项 | 描述 |
| --- | --- | --- |
| --input | 是 | 指定传入的HAP、HSP、App包文件路径。 |
| --out-path | 是 | 指定结果输出文件夹目录。 |
| --stat-file-size | 否 | 扫描超过设定大小的文件，单位KB。  范围为 0-4294967295 KB。 |

**JSON统计结果：**

```
1. [{
2. "taskType":2,
3. "taskDesc":"find files whose size exceed the limit size",
4. "param":"--stat-file-size 4",
5. "startTime":"2023-11-17 14:48:01:458",
6. "stopTime":"2023-11-17 14:48:01:491",
7. "result":[{
8. "file":"/application-entry-default.hap/libs/x86_64/example.so",
9. "size":1292840
10. }]
11. }]
```

**表5 扫描超出指定大小的文件字段信息**

| 字段 | 类型 | 描述 |
| --- | --- | --- |
| taskType | int | 取值为2，表示扫描超出指定大小文件。 |
| taskDesc | String | 任务的详细描述。 |
| param | String | 扫描程序传入参数。 |
| startTime | String | 任务开始时间。 |
| stopTime | String | 任务结束时间。 |
| result | Struct | 超出指定大小的文件统计结果字段信息，具体内容参考表6。 |

**表6 超出指定大小的文件统计结果字段信息**

| 字段 | 类型 | 描述 |
| --- | --- | --- |
| file | String | 扫描的大文件的对应路径。 |
| size | int | 扫描的大文件的对应大小，单位为Byte。 |

## 统计各类型文件大小占比示例

**命令示例：**

```
1. java -jar app_check_tool.jar --input ./test.app --out-path ./test --stat-suffix true
```

**表7 统计各类型文件大小占比指令参数说明**

| 指令 | 是否必选项 | 描述 |
| --- | --- | --- |
| --input | 是 | 指定传入的HAP、HSP、App包文件路径。 |
| --out-path | 是 | 指定结果输出文件夹目录。 |
| --stat-suffix | 否 | 是否统计各类型文件大小及占比。默认为false。  true：启用。  false：不启用。 |

**JSON统计结果：**

```
1. [{
2. "taskType":3,
3. "taskDesc":"show files group by file type[.suffix]",
4. "param":"--stat-suffix",
5. "startTime":"2023-11-17 14:48:01:497",
6. "stopTime":"2023-11-17 14:48:01:537",
7. "pathList":[
8. "test.app/application-entry-default.hap",
9. "test.app/entry-default.hap"
10. ],
11. "result":[{
12. "suffix":"so",
13. "totalSize":1292840,
14. "files":[{
15. "compress":"false",
16. "file":"/application-entry-default.hap/libs/x86_64/example.so",
17. "size":1292840
18. }]
19. },
20. {
21. "suffix":"abc",
22. "totalSize":84852,
23. "files":[{
24. "file":"/application-entry-default.hap/ets/modules.abc",
25. "size":76304
26. },
27. {
28. "file":"/entry-default.hap/ets/modules.abc",
29. "size":8548
30. }]
31. }]
32. }]
```

**表8 统计各类型文件大小占比字段信息**

| 字段 | 类型 | 描述 |
| --- | --- | --- |
| taskType | int | 取值为3，表示统计各类型文件大小占比。 |
| taskDesc | String | 任务的详细描述。 |
| param | String | 扫描程序传入参数。 |
| startTime | String | 任务开始时间。 |
| stopTime | String | 任务结束时间。 |
| pathList | Vector<String> | 多个HAP、HSP包的路径。 |
| result | Struct | 各类型文件大小占比统计结果字段信息，具体内容参考表9。 |

**表9 各类型文件大小占比统计结果字段信息**

| 字段 | 类型 | 描述 |
| --- | --- | --- |
| suffix | String | 同类型文件后缀名。 |
| totalSize | int | 扫描的同类型文件的总大小，单位为Byte。 |
| files | Struct | 同类型文件的对应路径和大小字段信息，具体内容参考表10。 |

**表10 同类型文件的对应路径和大小字段信息**

| 字段 | 类型 | 描述 |
| --- | --- | --- |
| file | String | 文件路径。 |
| size | int | 文件的大小，单位为Byte。 |
| compress | bool | 是否是压缩文件（仅so类型文件展示）。  true：是压缩文件。  false：不是压缩文件。 |
