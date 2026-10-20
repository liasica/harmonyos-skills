---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/natural-language-kit-faq-0001
title: AI中英文语义分词功能
breadcrumb: FAQ > AI功能开发 > 机器学习 > 自然语言理解（Natural Language） > 常见问题 > AI中英文语义分词功能
category: harmonyos-faqs
scraped_at: 2026-10-21T07:12:55+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:982fc18979426c5e709a519721a5dfec3af504da4f87b78a673e53ed6e81580b
---

**Q：使用分词功能，中文是正常分词的，英文分词异常，英文分词是简单按照空格分词，如下：**

```ts
let result = await textProcessing.getWordSegment('Storage specifications refer to capacity before formatting. Actual formatted capacity will be less.');
```

返回结果：

```txt
[{"word":"Storage","wordTag":"n"},{"word":" ","wordTag":"w"},{"word":"specifications","wordTag":"d"},{"word":" ","wordTag":"w"},{"word":"refer","wordTag":"v"},{"word":" ","wordTag":"w"},{"word":"to","wordTag":"pba"},{"word":" ","wordTag":"w"},{"word":"capacity","wordTag":"n"},{"word":" ","wordTag":"w"},{"word":"before","wordTag":"p"},{"word":" ","wordTag":"w"},{"word":"formatting","wordTag":"a"},{"word":".","wordTag":"wj"},{"word":" ","wordTag":"w"},{"word":"Actual","wordTag":"a"},{"word":" ","wordTag":"w"},{"word":"formatted","wordTag":"n"},{"word":" ","wordTag":"w"},{"word":"capacity","wordTag":"n"},{"word":" ","wordTag":"w"},{"word":"will","wordTag":"nrf"},{"word":" ","wordTag":"w"},{"word":"be","wordTag":"vshi"},{"word":" ","wordTag":"w"},{"word":"less","wordTag":"rzs"},{"word":".","wordTag":"wj"}]
```

**A**：[Natural Language Kit](../harmonyos-guides/natural-language-introduction.md)（自然语言理解服务）提供[分词](../harmonyos-guides/natural-language-getwordsegmentation.md)能力，可以将一段文本切分成独立的词语单元，识别出句子中的每个词汇。支持的语言：简体中文、英文、繁体中文。中文会一定程度上进行语义上分词，目前英文分词仅支持以空格进行分词。
