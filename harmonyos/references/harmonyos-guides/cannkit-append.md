---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-append
title: Append
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingData > Append
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9d307c8eb9af17adbca2c9e2b21fa076076f0c06bde71c3f4941d8cf6462bb9a
---

## 函数功能

向后添加tiling data，若添加超过可容纳的最大长度，则添加失败。

## 函数原型

```cpp
template<typename T, typename std::enable_if<std::is_standard_layout<T>::value, int>::type = 0>  ge::graphStatus Append(const T &data);
template<typename T, typename std::enable_if<std::is_standard_layout<T>::value, int>::type = 0>  ge::graphStatus Append(const T *data, size_t append_num);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| T | 输入 | 添加的tiling data的类型。 |
| const T &data | 输入 | 添加的tiling data实例。 |
| const T \*data | 输入 | 添加的tiling data起始地址。 |
| append\_num | 输入 | 添加的tiling data的个数，共添加append\_num个T类型的tiling data。 |

## 返回值

* 成功返回ge::GRAPH\_SUCCESS。
* 失败返回ge::GRAPH\_FAILED。

## 约束说明

添加的tiling data必须为符合standard\_layout，即内存平铺。

## 调用示例

```cpp
auto td_buf = TilingData::CreateCap(100U);
auto td = reinterpret_cast<TilingData *>(td_buf.get());
 
// 1
struct AppendData{
  int a = 10;
  int b = 100;
};
AppendData ad;
auto ret = td->Append<AppendData>(ad); // ge::GRAPH_SUCCESS
 
// 2
size_t append_num = 10;
int32_t *td = new int32_t[append_num];
auto ret = td->Append<int32_t>(td, append_num); // ge::GRAPH_SUCCESS
 
// 3
size_t append_num = 50;
int32_t *td = new int32_t[append_num];
auto ret = td->Append<int32_t>(td, append_num); // ge::GRAPH_FAILED
```
