---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-faqs-1
title: 判断模型能否在手机上运行？
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d559cc4fe265fc0eb76800f21c819167d5480916135653cd9cfd1c583cc874df
---

通过调用接口[HMS\_HiAICompatibility\_CheckFromFile](../harmonyos-references/cannkit.md#hms_hiaicompatibility_checkfromfile)或者[HMS\_HiAICompatibility\_CheckFromBuffer](../harmonyos-references/cannkit.md#hms_hiaicompatibility_checkfrombuffer)，传入编译后的模型文件或者模型buffer，如果返回“HIAI\_COMPATIBILITY\_COMPATIBLE”表示兼容性检查通过，模型可以在手机上运行。
