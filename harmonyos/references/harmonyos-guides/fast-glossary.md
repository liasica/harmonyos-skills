---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-glossary
title: FAST Kit术语
breadcrumb: 指南 > 系统 > 基础功能 > FAST Kit（算法加速服务） > FAST Kit术语
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:36+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:09ce205484cfc3fca9d541f59c0a4f2cd6a4a66692a17bf88ded3b07b521b758
---

## C

### Concurrent HashMap；并发哈希表

一种专为高并发场景设计的键值对数据结构，支持多线程环境下的安全存储、快速访问与高效更新，适用于对并发吞吐量和数据一致性要求较高的增删改查场景。

## D

### Direct Form II Transposed Structure；直接II型转置结构

二阶IIR滤波器的一种实现结构，具有延迟单元最少、数值稳定性好的特点。FAST Kit中的IIR滤波器支持多通道和多节级联配置。

## N

### Natural Sort；自然语言排序

一种智能的字符串排序方式，将字符串中的数字序列视为数值进行比较（而非逐个字符比较），使排序结果更符合人类直觉。例如"file1, file2, file10"而非"file1, file10, file2"。

## O

### Opaque Configuration；不透明配置

一种ABI稳定的配置抽象机制，库以不完整类型前向声明配置对象，外部代码仅通过指针句柄进行传递与操作，实现细节完全由库内部定义，保证后续版本可在不破坏二进制兼容性的前提下变更存储格式与语义。

## P

### Partial Sort；部分排序

仅保证指定区间内的元素处于完全排序后的位置，即部分排序后指定区间内的每个元素与全部排序后同一区间内的元素内容和顺序完全一致。区间外的元素仅满足与区间内元素的大小关系，不保证完全排序。适用于Top-K选择、中位数查找等无需全排序的场景。

## R

### Rectangular Partition Problem；矩形划分问题

给定N个彼此不相交的矩形，求M个彼此不相交且并集与输入完全相同的矩形，并使M尽可能少的优化问题。

## S

### Segment Map；线段表

一种用于高效处理数据序列区间段信息的数据结构，支持单点修改、区间修改、区间查询等操作，能将区间操作的时间复杂度从O(N)优化至O(logN)。典型实现为线段树（Segment Tree）。

### Split Complex Format；分离复数格式

一种复数数组存储格式，将实部和虚部分别存储在独立的数组中，而非交错存储（real0, imag0, real1, imag1, ...）。FAST Kit提供交错格式与分离格式之间的相互转换接口。

### Strict Weak Ordering；严格弱序

比较函数必须满足的一种序关系性质，要求比较关系是传递的、非自反的、非对称的，不可比性是传递的，且对于任意两个元素，比较结果必须确定。严格弱序是排序功能和关联容器比较函数必须要满足的核心要求。

### Sweep Line Algorithm；扫描线算法

一种二维线性扫描算法，可用于高效解决矩形划分问题，通过扫描线沿坐标轴方向扫描，动态维护当前活跃的矩形集合，从而快速合并相邻矩形，输出数量尽可能少的不相交矩形集合。
