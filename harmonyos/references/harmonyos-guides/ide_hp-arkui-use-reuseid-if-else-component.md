---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-reuseid-if-else-component
title: @performance/hp-arkui-suggest-reuseid-for-if-else-reusable-component
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-suggest-reuseid-for-if-else-reusable-component
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:07+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:016f0fd7972ba842202a97a45b3366cbdbe30c397b79307bf8564d5469424f09
---

建议使用reuseId标记不同结构的组件构成。

滑动丢帧场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-suggest-reuseid-for-if-else-reusable-component": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. // 源码文件，请以工程实际为准
2. import { MyDataSource } from './MyDataSource';
3. import { ChartInfoEntry } from './data/DataEntry';
4. import { PublicChatItem } from './component/PublicChatItem';
5. import { ChatItem } from './component/ChatItem';

7. @Entry
8. @Component
9. struct MyComponent{
10. private scroller: Scroller = new Scroller()
11. private lazyChatList: MyDataSource = new MyDataSource();

13. build() {
14. Column() {
15. List({ scroller: this.scroller }) {
16. LazyForEach(this.lazyChatList, (item: ChartInfoEntry, index: number) => {
17. ListItem() {
18. // 使用reuseId进行组件复用的控制
19. InnerRecentChat({ chatInfo: item }).reuseId(this.lazyChatList.getReuseIdByIndex(index))
20. }
21. .height(72)
22. }, (item: ChartInfoEntry) => item.id)
23. }
24. .cachedCount(3)
25. .width('100%')
26. .height('100%')
27. }
28. }
29. }

31. @Reusable
32. @Component
33. struct InnerRecentChat {
34. @State chatInfo: ChartInfoEntry = new ChartInfoEntry()

36. aboutToReuse(params: Record<string, ESObject>): void {
37. this.chatInfo = params.chatInfo as ChartInfoEntry
38. }

40. build() {
41. Button({ type: ButtonType.Normal }) {
42. Row() {
43. if (this.chatInfo['isPublicChat']) {
44. // 源码文件，请以工程实际为准
45. PublicChatItem({ chatInfo: chatInfo as ChartInfoEntry })
46. } else {
47. // 源码文件，请以工程实际为准
48. ChatItem({ chatInfo: this.chatInfo as ChatItem })
49. }
50. }.padding({ left: 16, right: 16 })
51. }
52. .type(ButtonType.Normal)
53. .width('100%')
54. .height('100%')
55. .borderRadius(0)
56. }
57. }
```

## 反例

```
1. // 源码文件，请以工程实际为准
2. import { MyDataSource } from './MyDataSource';
3. import { ChartInfoEntry } from './data/DataEntry';
4. import { PublicChatItem } from './component/PublicChatItem';
5. import { ChatItem } from './component/ChatItem';

7. @Entry
8. @Component
9. struct MyComponent{
10. private scroller: Scroller = new Scroller()
11. private lazyChatList: MyDataSource = new MyDataSource();

13. build() {
14. Column() {
15. List({ scroller: this.scroller }) {
16. LazyForEach(this.lazyChatList, (item: ChartInfoEntry, index: number) => {
17. ListItem() {
18. // ListItem里有if-else并且直接在分支里使用了自定义复用组件
19. Button({ type: ButtonType.Normal }) {
20. Row() {
21. if (item['isPublicChat']) {
22. // 源码文件，请以工程实际为准
23. PublicChatItem({ chatInfo: item as PublicChatItem })
24. } else {
25. // 源码文件，请以工程实际为准
26. ChatItem({ chatInfo: item as ChatItem })
27. }
28. }.padding({ left: 16, right: 16 })
29. }
30. .type(ButtonType.Normal)
31. .width('100%')
32. .height('100%')
33. .borderRadius(0)
34. }
35. .height(72)
36. }, (item: ChartInfoEntry) => item.id)
37. }
38. .cachedCount(3)
39. .width('100%')
40. .height('100%')
41. }
42. }
43. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
