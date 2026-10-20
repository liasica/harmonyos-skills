---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/package-structure-faq-0003
title: HSP多包加载崩溃cppcrash异常问题排查
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 常见问题 > HSP多包加载崩溃cppcrash异常问题排查
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:17+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:3944d39a6a6ca0d6a24df8cfd673b552e1d4affb20e9b62cdd8e13c0f56bf834
---

**Q：使用HSP的多包场景下，直接崩溃并产生cppcrash异常日志，错误信息为resolveBufferCallback get buffer failed，如何排查？**

**A**：该问题是由于HSP包解析失败导致的。常见的加载失败原因包括安装失败、文件丢失、缺少权限和安全内存校验失败。开发者可以根据关键日志进行排查。重新安装应用通常可以解决问题。

| 已知关键错误日志 | 修改建议 |
| --- | --- |
| realHapPath is empty | 路径查询失败，无法获取用户安装包信息。建议开发者重新安装应用。 |
| transform real path error: ERROR, pathName: PATH | 使用realpath函数解析路径失败，ERROR表示错误信息，PATH表示hsp路径。建议开发者重新安装应用。 |
| CreateFileMapper, mmap failed, errno ERROR. fileName: FILENAME | 使用mmap函数映射内存失败，ERROR表示错误信息，FILENAME表示文件名。常见原因是系统内存不足、文件未签名。 |
