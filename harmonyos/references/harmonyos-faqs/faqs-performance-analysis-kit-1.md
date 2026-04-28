---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-1
title: hilog日志如何落盘存储
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > hilog日志如何落盘存储
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:14+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1ba42367404aa5a039192c57ea9d4aa74fa2494c2a7a52c0716c4af285e60fef
---

运行命令：hilog -w start -f ckTest -l 1M -n 5 -m zlib -j 11

文件保存在目录：/data/log/hilog/

参数解释：

```
1. -w 开启日志落盘任务,start表示开始，stop表示停止。
2. -f 设置日志文件名
3. -l 设置单个日志文件大小，单位可以是：B/K/M/G
4. -n 设置最大日志文件编号，当文件计数超过此编号时，日志文件旋转。范围：[2,1000]
5. -m 设置日志文件压缩算法
6. -j 任务ID，范围：[10,0xffffffffff)
7. 更多参数含义请使用hilog --help查看。
```
