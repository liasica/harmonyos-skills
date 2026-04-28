---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-previewer-operating-3
title: 预览告警“@Consume/@Link decorated property <propertyName> not initialized”
breadcrumb: FAQ > DevEco Studio > 界面预览 > 预览告警“@Consume/@Link decorated property <propertyName> not initialized”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:06+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:82cceb71cd32da3898ec899ebb952dd3938ea0f03af5bc1ed9e6485fa6c3f642
---

**问题现象**

启动预览后，预览窗口显示白屏，上方出现错误信息：“Preview failed. View details in the PreviewerLog window.”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/ADbZQS2XSNaDFSITqh7Mvw/zh-cn_image_0000002194317968.png?HW-CC-KV=V1&HW-CC-Date=20260428T002904Z&HW-CC-Expire=86400&HW-CC-Sign=690D68BC8A9F45BAB9F8335A13919E2EF626BF9D6D6ECD7FD9C75DC61BC294E1 "点击放大")

此时，PreviewerLog 窗口显示如下告警信息：“@Consume/@Link 装饰的属性 \_<propertyName>\_未初始化。”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/7yKLU940R0qsQXGs6aNxcw/zh-cn_image_0000002194158348.png?HW-CC-KV=V1&HW-CC-Date=20260428T002904Z&HW-CC-Expire=86400&HW-CC-Sign=7350DD3902B973EED0D3900BBC78F280BE812CC44D173E6C208DD09774A26B2F)

**解决措施**

由于@Consume/@Link装饰的成员需要与父组件建立绑定关系，单独预览时无法完成初始化，因此如果预览包含@Consume（或@Link）装饰的成员的页面或组件，就可能会出现空白屏幕。

建议不要直接预览含有@Consume或@Link装饰的子组件，而应通过预览父组件来查看子组件的预览效果。

示例代码：

```
1. // Suggest adding @ Preview on ParentComp to preview the preview effect of ChildComp
2. @Preview
3. @Component
4. struct ParentComp {
5. // @Provide decoration is provided by the entrance component ParentComp as its descendant component
6. @Provide reviewVotes: number = 10;

8. build() {
9. Column() {
10. Button(`reviewVotes(${this.reviewVotes}), give +1`)
11. .onClick(() => this.reviewVotes += 1)
12. ChildComp()
13. }
14. }
15. }

17. // @Preview is not recommended to directly preview ChildComp
18. @Component
19. struct ChildComp {
20. // The variable decorated with '@Consume' is bound to the variable decorated with '@Provide' in its ancestor component ParentComp using the same attribute name
21. @Consume reviewVotes: number;
22. build() {
23. Column() {
24. Text(`reviewVotes(${this.reviewVotes})`)
25. Button(`reviewVotes(${this.reviewVotes}), give +1`)
26. .onClick(() => this.reviewVotes += 1)
27. }
28. .width('50%')
29. }
30. }
```

[PreviewFailed.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/PreviewerOperating/entry/src/main/ets/pages/PreviewFailed.ets#L3-L32)
